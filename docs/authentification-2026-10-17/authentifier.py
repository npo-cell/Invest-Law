#!/usr/bin/env python3
"""Authentification du classeur « Gamme One Life complète » (17/10/2026).

Pour chaque fonds et chaque case remplie de l'onglet Fiches (et chaque ligne d'Allocations), cherche la valeur dans
le texte de la factsheet la plus récente et du KID du fonds. Statuts :
  OK            la valeur figure dans le document
  NON_RETROUVE  la valeur n'est pas retrouvée automatiquement (à relire dans le PDF)
  SANS_SOURCE   case remplie mais aucun document pour le fonds
  AUTRE_SOURCE  valeur reprise du site qui ne vient ni de la factsheet/KID ni du fichier One Life
  JUGEMENT      champ de synthèse (type de fonds, classification) : contrôlé par cohérence, pas par recopie
Usage : python3 -I authentifier.py <dossier des PDF du site> <sortie.json>
"""
import csv, json, os, re, subprocess, sys, unicodedata, urllib.parse, openpyxl

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
SHEET = os.path.join(RACINE, 'docs/gamme-complete-2026-10-16/sheet')
GH = 'https://github.com/npo-cell/Invest-Law/blob/claude/kind-edison-2o3dsu/'
COLS = ['n', 'isin', 'nom', 'maison', 'statut', 'lien_site', 'fs_date', 'fs_url', 'kid_date', 'kid_url',
        'date_creation', 'devise', 'type_fonds', 'compartiment', 'gerants', 'encours', 'encours_devise',
        'encours_date', 'frais_gestion', 'frais_courants', 'sri', 'indice', 'classification', 'categorie', 'sfdr',
        'durable_pct', 'duration', 'qualite', 'disclaimer', 'politique_fr', 'politique_en', 'source_politique',
        'remarques', 'origine']
MOIS_FR = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre',
           'novembre', 'décembre']
ABR_FR = ['janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin', 'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.']
MOIS_EN = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
           'november', 'december']


CACHE = {}


def texte(pdf):
    if pdf in CACHE:
        return CACHE[pdf]
    c = os.path.join(os.environ.get('AUTH_CACHE', '/tmp'), re.sub(r'\W', '_', pdf) + '.txt')
    if os.path.exists(c):
        CACHE[pdf] = open(c).read()
        return CACHE[pdf]
    t = ''
    for mode in ([], ['-raw'], ['-layout']):
        t += subprocess.run(['pdftotext', *mode, pdf, '-'], capture_output=True, text=True).stdout + '\n'
    open(c, 'w').write(t)
    CACHE[pdf] = t
    return t


def norm(s):
    s = unicodedata.normalize('NFKC', s).lower()
    s = s.replace('’', "'").replace('‘', "'").replace('`', "'").replace('«', '"').replace('»', '"')
    s = s.replace('“', '"').replace('”', '"').replace('–', '-').replace('—', '-').replace('­', '')
    s = re.sub(r'-\s*\n\s*', '', s)
    return re.sub(r'[\s"]+', '', s)


def nombres(v):
    """Écritures possibles d'un nombre dans un document."""
    try:
        x = float(v)
    except ValueError:
        return set()
    out = set()
    for d in range(0, 5):
        s = ('%.' + str(d) + 'f') % x
        if abs(float(s) - x) > 1e-9:
            continue
        ent, _, dec = s.partition('.')
        neg = ent.startswith('-')
        ent = ent.lstrip('-')
        groupes = [ent]
        if len(ent) > 3:
            g = re.sub(r'(?<=\d)(?=(\d{3})+$)', '\x00', ent)
            groupes += [g.replace('\x00', sep) for sep in (' ', ',', '.', "'", ' ', '\xa0')]
        for e in groupes:
            for sep in ('.', ','):
                out.add(('-' if neg else '') + e + (sep + dec if dec else ''))
    return out


def trouve_nombre(v, T, raw):
    for c in nombres(v):
        if re.search(r'(?<![\d,.])' + re.escape(c) + r'(?![\d])', raw):
            return True
    return False


def trouve_date(v, raw):
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})$', v)
    if not m:
        return norm(v) in norm(raw)
    y, mo, d = m.groups()
    yi, moi, di = int(y), int(mo), int(d)
    cands = [f'{d}/{mo}/{y}', f'{d}.{mo}.{y}', f'{d}-{mo}-{y}', f'{y}-{mo}-{d}', f'{y}/{mo}/{d}',
             f'{d}/{mo}/{y[2:]}', f'{d}.{mo}.{y[2:]}', f'{mo}/{d}/{y}', f'{di}/{moi}/{y}', f'{d}{mo}{y}',
             f'{di} {MOIS_FR[moi-1]} {y}', f'{di}er {MOIS_FR[moi-1]} {y}', f'{di} {MOIS_EN[moi-1]} {y}',
             f'{MOIS_EN[moi-1]} {di}, {y}', f'{d} {MOIS_EN[moi-1][:3]} {y}', f'{di} {MOIS_EN[moi-1][:3]} {y}',
             f'{d}-{MOIS_EN[moi-1][:3]}-{y}', f'{d} {MOIS_FR[moi-1][:4]}. {y}', f'{d}.{mo}.{y}',
             f'{d}-{ABR_FR[moi-1]}-{y}', f'{d}-{ABR_FR[moi-1].rstrip(".")}-{y}']
    R = norm(raw)
    return any(norm(c) in R for c in cands)


def morceaux(txt):
    out = []
    for line in txt.split('\n'):
        for s in re.split(r'(?<=[.;:])\s+', line):
            if len(s.strip()) > 3:
                out.append(s.strip())
    return out


def part_trouvee(txt, R):
    m = morceaux(txt)
    if not m:
        return 1.0, []
    manq = [s for s in m if norm(s) not in R]
    return 1 - len(manq) / len(m), manq


SRI_RE = r'(sri|srri|indicateur (synthétique )?de risque|classe de risque|risk indicator|risk class|niveau de risque|catégorie de risque|profil de risque|risk category|risk and reward|risque et de rendement)'


def trouve_sri(d, raw):
    low = raw.lower()
    if re.search(SRI_RE + r'[\s\S]{0,120}?(?<!\d)' + d + r'(?![\d,.%])', low):
        return True
    if re.search(r'(?<!\d)' + d + r'\s*(/|sur|out of|de)\s*7', low):
        return True
    return False


def main(pdfdir, sortie):
    F = [r for f in ('fiches-1.csv', 'fiches-2.csv') for r in csv.reader(open(os.path.join(SHEET, f)))]
    A = [r for f in ('allocations-1.csv', 'allocations-2.csv') for r in csv.reader(open(os.path.join(SHEET, f)))]
    alloc = {}
    for r in A:
        alloc.setdefault(r[1], []).append(r)
    docs = [r for r in csv.reader(open(os.path.join(SHEET, 'documents.csv')))]
    fs_dispo = {}
    for r in docs:
        if 'Factsheet' in r[3] or 'Rapport' in r[3]:
            fs_dispo[r[1]] = max(fs_dispo.get(r[1], ''), r[5])
    # catégorie One Life : fichier de classification (même ISIN) ou correspondances (autre part du même fonds)
    cat_ok = {}
    wb = openpyxl.load_workbook(sys.argv[3], read_only=True) if len(sys.argv) > 3 else None
    if wb:
        for row in list(wb.worksheets[0].iter_rows(values_only=True))[1:]:
            if row[1]:
                cat_ok[str(row[1]).strip().upper()] = row[4]
    corr = {}
    for p in ('docs/wealth-belgium-2026-10-15/categorie/correspondances.csv',
              'docs/gamme-complete-2026-10-16/fonds-restants/categorie/correspondances.csv'):
        for r in csv.DictReader(open(os.path.join(RACINE, p))):
            vals = list(r.values())
            if vals[-1]:
                corr[vals[1] if 'wealth' in p else vals[0]] = vals[-1]

    res = []
    for r in F:
        f = dict(zip(COLS, r))
        isin = f['isin']
        src = []
        if f['fs_url']:
            if 'digitalocean' in f['fs_url']:
                src.append(os.path.join(pdfdir, isin + '__site.pdf'))
            else:
                src.append(os.path.join(RACINE, urllib.parse.unquote(f['fs_url'].replace(GH, ''))))
        if f['kid_url']:
            src.append(os.path.join(RACINE, urllib.parse.unquote(f['kid_url'].replace(GH, ''))))
        src = [p for p in src if os.path.exists(p)]
        raw = ''.join(texte(p) for p in src)
        R = norm(raw)
        cells = {}

        def put(k, st, det=''):
            cells[k] = {'v': f[k][:300], 'st': st, 'det': det}

        for k in COLS[10:31]:
            v = f[k].strip()
            if not v:
                continue
            if k in ('type_fonds', 'classification'):
                put(k, 'JUGEMENT')
                continue
            if k == 'categorie':
                ok = cat_ok.get(isin) == v or corr.get(isin) == v
                if ok:
                    put(k, 'OK', 'fichier OneLife Fund Classification')
                else:  # catégorie saisie sur le site avant le 13/10, absente du fichier One Life
                    put(k, 'AUTRE_SOURCE', 'catégorie du site, absente du fichier OneLife Fund Classification')
                continue
            if not raw:
                put(k, 'SANS_SOURCE')
                continue
            if k in ('date_creation', 'encours_date'):
                put(k, 'OK' if trouve_date(v, raw) else 'NON_RETROUVE')
            elif k in ('devise', 'encours_devise'):
                put(k, 'OK' if re.search(r'\b' + re.escape(v) + r'\b', raw) or (v == 'EUR' and '€' in raw)
                    or (v == 'USD' and '$' in raw) else 'NON_RETROUVE')
            elif k in ('encours', 'frais_gestion', 'frais_courants', 'durable_pct'):
                ok = trouve_nombre(v, R, raw)
                if not ok and k == 'encours':
                    try:
                        ok = trouve_nombre(str(round(float(v) / 1000, 4)), R, raw)  # milliards
                    except ValueError:
                        pass
                put(k, 'OK' if ok else 'NON_RETROUVE')
            elif k == 'duration':
                num = re.match(r'-?[\d.,]+', v)
                put(k, 'OK' if num and trouve_nombre(num.group().replace(',', '.'), R, raw) else 'NON_RETROUVE')
            elif k == 'sri':
                put(k, 'OK' if trouve_sri(v, raw) else 'NON_RETROUVE')
            elif k == 'sfdr':
                put(k, 'OK' if re.search(r'(article|art\.?)\s*' + v + r'\b', raw, re.I) else 'NON_RETROUVE')
            elif k == 'gerants':
                noms = [g.strip() for g in re.split(r',|;| et | and |\n', v) if g.strip()]
                manq = [g for g in noms if norm(g) not in R and norm(g.split()[-1]) not in R]
                put(k, 'OK' if not manq else 'NON_RETROUVE', '; '.join(manq))
            elif k == 'indice' and v.lower() in ('aucun', 'none', 'n/a'):
                ok = re.search(r"(aucun indice|pas d.indice|no benchmark|not managed in reference|n.a pas d.indice|néant|sans indice|n'est pas géré par rapport|is not managed against|does not have a benchmark|no reference)", raw, re.I)
                put(k, 'OK' if ok else 'NON_RETROUVE')
            elif k == 'qualite':
                put(k, 'OK' if norm(v) in R else 'NON_RETROUVE')
            else:  # textes : compartiment, indice, disclaimer, politiques
                p, manq = part_trouvee(v, R)
                put(k, 'OK' if p == 1 else 'NON_RETROUVE', ('%d %% retrouvé ; manque : ' % round(p * 100)) +
                    ' | '.join(m[:120] for m in manq[:3]) if p < 1 else '')
        # allocations
        al = alloc.get(isin, [])
        al_bad = []
        for a in al:
            lab, pct = a[4], a[5]
            ok_l = norm(lab) in R
            ok_p = trouve_nombre(pct, R, raw) if pct else True
            if not (ok_l and ok_p):
                al_bad.append({'type': a[3], 'libelle': lab, 'pct': pct, 'libelle_ok': ok_l, 'pct_ok': ok_p})
        recent = ''
        if f['fs_date'] and fs_dispo.get(isin) and fs_dispo[isin] > f['fs_date']:
            recent = 'Une factsheet plus récente (%s) existe dans nos documents' % fs_dispo[isin]
        res.append({'n': f['n'], 'isin': isin, 'nom': f['nom'], 'statut': f['statut'], 'origine': f['origine'],
                    'fs_date': f['fs_date'], 'kid_date': f['kid_date'], 'sources': [os.path.basename(p) for p in src],
                    'cells': cells, 'alloc_total': len(al), 'alloc_bad': al_bad, 'plus_recente': recent})
    json.dump(res, open(sortie, 'w'), ensure_ascii=False, indent=0)
    import collections
    c = collections.Counter(x['st'] for r in res for x in r['cells'].values())
    print('cases', sum(c.values()), dict(c))
    print('allocations', sum(r['alloc_total'] for r in res), 'non retrouvées', sum(len(r['alloc_bad']) for r in res))
    k = collections.Counter(kk for r in res for kk, x in r['cells'].items() if x['st'] == 'NON_RETROUVE')
    print('non retrouvé par champ', dict(k))
    print('factsheet plus récente disponible', sum(1 for r in res if r['plus_recente']))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
