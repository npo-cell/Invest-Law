#!/usr/bin/env python3
"""Contrôle des VNI d'invest-law.eu (lecture seule) : fonds avec / sans VNI, cohérence avec la date de création.

Prérequis : session invest-law ouverte (investlaw_upload.py login/verify).
  python3 tools/controle_vni.py            # lit le site, écrit docs/controle-vni/controle-vni-AAAA-MM-JJ.json, affiche le bilan

Méthode et historique des contrôles : docs/controle-vni/README.md
"""
import calendar, collections, csv, json, os, re, sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from investlaw_upload import api

TOL_AVANT = 7       # jours tolérés avant la création (décalage de dates d'un jour à l'import)
SAUT = 0.20         # variation entre deux VNI consécutives jugée anormale
SAUTS_FAUSSES = 3   # à partir de ce nombre de sauts (hors passage à l'euro), les VNI sont « fausses »
PERIME = 45         # jours sans nouvelle VNI → « plus mise à jour »
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'controle-vni')
JOURNAL = os.path.join(OUT, '..', 'zimbra-vni', 'journal.csv')
ORDRE = ['OK', 'VNI fausses', 'VNI avant la création', 'Début manquant', 'Création absente', 'Aucune VNI']


def add3m(x):
    m = x.month + 3; y = x.year + (m - 1) // 12; m = (m - 1) % 12 + 1
    return date(y, m, min(x.day, calendar.monthrange(y, m)[1]))


def isin_valide(s):
    if not re.fullmatch(r'[A-Z]{2}[A-Z0-9]{9}[0-9]', s): return False
    digs = ''.join(str(int(c, 36)) for c in s[:-1]); t = 0
    for i, ch in enumerate(reversed(digs)):
        n = int(ch) * (2 if i % 2 == 0 else 1); t += n // 10 + n % 10
    return (10 - t % 10) % 10 == int(s[-1])


def devise_suspecte(f):
    cur, nom = (f['Currency'] or '').strip(), f['Name'].upper().split()
    if cur not in ('EUR', 'USD', 'GBP', 'CHF', 'JPY', 'SEK', 'NOK', 'DKK'): return f'devise « {cur} » mal saisie'
    for c in ('EUR', 'USD', 'GBP', 'CHF'):
        if c in nom[-3:] and cur != c: return f'devise {cur} mais {c} dans le nom'
    return ''


def analyse(f, vl, today):
    D = lambda s: date.fromisoformat(s[:10])
    v = sorted((D(e['VLDate']), float(e['VL'])) for e in vl if e.get('VL') not in (None, ''))
    c = D(f['CreationDate']) if f['CreationDate'] else None
    ecart = (v[0][0] - c).days if v and c else None
    sauts = [(d1, a, b) for (_, a), (d1, b) in zip(v, v[1:]) if a > 0 and abs(b / a - 1) > SAUT]
    franc = [s for s in sauts if s[0].year <= 2002 and 6.3 < s[1] / s[2] < 6.8]   # FRF → EUR (÷ 6,55957)
    autres = [s for s in sauts if s not in franc]
    if not v: statut = 'Aucune VNI'
    elif len(autres) >= SAUTS_FAUSSES: statut = 'VNI fausses'
    elif not c: statut = 'Création absente'
    elif ecart < -TOL_AVANT: statut = 'VNI avant la création'
    elif v[0][0] > add3m(c): statut = 'Début manquant'
    else: statut = 'OK'
    rem = []
    if statut == 'VNI fausses':
        d1, a, b = autres[0]; rem.append(f'{len(autres)} sauts de plus de 20 % (ex. {d1} : {a:g} → {b:g})')
    elif autres:
        rem.append('; '.join(f'saut {(b / a - 1) * 100:+.0f} % le {d1} ({a:g} → {b:g})' for d1, a, b in autres))
    if franc: rem.append(f"historique en francs avant {franc[-1][0]} (÷ 6,56 au passage à l'euro)")
    we = sum(1 for x, _ in v if x.weekday() >= 5)
    if v and we / len(v) > 0.03: rem.append(f"{we} VNI datées un week-end ({we * 100 // len(v)} %) : dates probablement décalées d'un jour")
    if any(x <= 0 for _, x in v): rem.append('VNI nulle ou négative')
    if v and v[-1][0] > today: rem.append(f'date future {v[-1][0]}')
    perime = bool(v) and (today - v[-1][0]).days > PERIME
    if perime: rem.append(f'plus mise à jour depuis le {v[-1][0].strftime("%d/%m/%Y")}')
    if statut == 'OK' and ecart is not None and ecart < 0: rem.append(f'1re VNI {-ecart} j avant la création (décalage de date)')
    isin = (f['ISIN'] or '').strip().upper()
    if not isin_valide(isin): rem.append(f'ISIN « {isin} » invalide')
    dev = devise_suspecte(f)
    if dev: rem.append(dev)
    return dict(id=f['FundId'], fonds=f['Name'].strip(), isin=f['ISIN'], maison=(f.get('MaisonName') or '').strip(),
                etat='Actif' if f['IsActive'] else 'Inactif', statut=statut, creation=f['CreationDate'] or '',
                premiere_vni=v[0][0].isoformat() if v else '', derniere_vni=v[-1][0].isoformat() if v else '',
                ecart_jours=ecart, nb_vni=len(v), dates_decalees=any('week-end' in x for x in rem), plus_a_jour=perime,
                francs=bool(franc), remarques=' · '.join(rem), isin_invalide=not isin_valide(isin), devise_suspecte=bool(dev),
                doublon_de='', vni_verifiees=0)


def main():
    today = date.today()
    st, funds = api('GET', '/api/funds')
    if st != 200: sys.exit(f'ECHEC {st} {funds}')
    get = lambda f: api('GET', f"/api/funds/{f['FundId']}/vl")
    with ThreadPoolExecutor(8) as ex: vls = list(ex.map(get, funds))
    bad = [f['FundId'] for f, (s, _) in zip(funds, vls) if s != 200]
    if bad: sys.exit(f'ECHEC lecture VNI des fonds {bad}')
    rows = [analyse(f, v, today) for f, (_, v) in zip(funds, vls)]
    by_id = {r['id']: r for r in rows}
    # séries identiques entre deux fiches (même VNI sur plus de la moitié d'au moins 50 dates communes)
    ser = {f['FundId']: {e['VLDate'][:10]: e['VL'] for e in v} for f, (_, v) in zip(funds, vls) if v}
    ids = list(ser)
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            com = ser[a].keys() & ser[b].keys()
            if len(com) >= 50 and sum(ser[a][k] == ser[b][k] for k in com) / len(com) > 0.5:
                for x, y in ((a, b), (b, a)):
                    by_id[x]['doublon_de'] = f"{by_id[y]['fonds']} ({by_id[y]['isin']})"
                    by_id[x]['remarques'] = ' · '.join(filter(None, [by_id[x]['remarques'], 'même série de VNI que ' + by_id[x]['doublon_de']]))
    # VNI importées par la routine Zimbra et retrouvées identiques sur le site
    isin_id = {(f['ISIN'] or '').strip().upper(): f['FundId'] for f in funds}
    if os.path.exists(JOURNAL):
        for j in csv.DictReader(open(JOURNAL, encoding='utf-8')):
            fid = int(j['fund_id']) if j['fund_id'] else isin_id.get(j['isin'])
            if j['statut'] == 'importee' and fid in ser and ser[fid].get(j['date']) is not None \
                    and abs(float(ser[fid][j['date']]) - float(j['vni'])) < 1e-6:
                by_id[fid]['vni_verifiees'] += 1
    out = os.path.join(OUT, f'controle-vni-{today}.json')
    json.dump(rows, open(out, 'w', encoding='utf-8'), ensure_ascii=False)
    n = collections.Counter(r['statut'] for r in rows); a = collections.Counter(r['statut'] for r in rows if r['etat'] == 'Actif')
    print(out)
    for s in ORDRE: print(f'{s:24} {n[s]:4}  dont actifs {a[s]}')
    print('dates décalées', sum(r['dates_decalees'] for r in rows), '· plus à jour', sum(r['plus_a_jour'] for r in rows),
          '· francs', sum(r['francs'] for r in rows), '· ISIN invalides', sum(r['isin_invalide'] for r in rows),
          '· doublons', sum(bool(r['doublon_de']) for r in rows), '· devises', sum(r['devise_suspecte'] for r in rows),
          '· VNI vérifiées à la source', sum(r['vni_verifiees'] for r in rows), 'sur', sum(1 for r in rows if r['vni_verifiees']), 'fonds')


if __name__ == '__main__':
    main()
