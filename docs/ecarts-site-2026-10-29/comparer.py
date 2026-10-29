#!/usr/bin/env python3
"""Écarts entre invest-law.eu (GET /api/funds) et le classeur « Gamme One Life complète » (onglet Fiches).
Lecture seule. Usage : python3 -I comparer.py <funds.json> <classif.json> <maisons.json> <sortie.xlsx>"""
import csv, html, json, re, sys, collections, unicodedata, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment

RACINE = '/home/user/Invest-Law/'
SHEET = RACINE + 'docs/gamme-complete-2026-10-16/sheet/'
COLS = ['n', 'isin', 'nom', 'maison', 'statut', 'x', 'fs_date', 'fs_url', 'kid_date', 'kid_url', 'date_creation', 'devise',
        'type_fonds', 'compartiment', 'gerants', 'encours', 'encours_devise', 'encours_date', 'frais_gestion',
        'frais_courants', 'sri', 'indice', 'classification', 'categorie', 'sfdr', 'durable_pct', 'duration', 'qualite',
        'disclaimer', 'politique_fr', 'politique_en', 'source_politique', 'remarques', 'origine']
# champ du classeur -> (libellé, clé du site, nature)
CHAMPS = [('date_creation', 'Date de création', 'CreationDate', 'date'), ('devise', 'Devise', 'Currency', 'txt'),
          ('type_fonds', 'Type de fonds', 'FundType', 'txt'), ('compartiment', 'Compartiment', 'Compartment', 'long'),
          ('gerants', 'Gérant(s)', 'fund_manager', 'txt'), ('encours', 'Encours (M)', 'TotalAssets', 'num'),
          ('frais_gestion', 'Frais de gestion', 'Fees', 'num'), ('frais_courants', 'Frais courants / TER', 'TER', 'num'),
          ('sri', 'SRI', 'Risque', 'num'), ('indice', 'Indice', 'Benchmark', 'txt'),
          ('classification', 'Classification', 'Classification', 'txt'), ('categorie', 'Catégorie', 'Category', 'txt'),
          ('sfdr', 'SFDR', 'ESG_code', 'sfdr'), ('durable_pct', 'Invest. durables (%)', 'ESG', 'num'),
          ('duration', 'Duration', 'Duration', 'txt'), ('qualite', 'Qualité des émetteurs', 'IssuerQuality', 'txt'),
          ('disclaimer', 'Disclaimer', 'Disclaimer', 'long'), ('politique_fr', 'Politique FR', 'InvestmentPolicy', 'long'),
          ('politique_en', 'Politique EN', 'InvestmentPolicyEN', 'long')]


def plain(v):
    if v is None:
        return ''
    s = html.unescape(str(v))
    s = re.sub(r'<br\s*/?>|</p>|</li>', '\n', s, flags=re.I)
    s = re.sub(r'<[^>]+>', '', s)
    return s.strip()


def key(s):
    s = plain(s).lower().replace('’', "'").replace('«', '"').replace('»', '"').replace(' ', ' ')
    return re.sub(r'[\s"\']+', '', s)


def num(v):
    try:
        return float(str(v).replace(',', '.').replace('%', '').strip())
    except ValueError:
        return None


def egal(nature, a, b):
    if nature == 'num':
        x, y = num(a), num(b)
        if x is None or y is None:
            return key(a) == key(b)
        return abs(x - y) < 0.005
    if nature == 'date':
        return str(a)[:10] == str(b)[:10]
    if nature == 'sfdr':
        m = re.search(r'\d', plain(b))
        return (m.group() if m else '') == str(a).strip()
    return key(a) == key(b)


def jetons(s):
    s = unicodedata.normalize('NFKD', plain(s).lower()).encode('ascii', 'ignore').decode()
    s = re.sub(r'(\d),(\d)', r'\1.\2', s)
    return sorted(t for t in re.findall(r'[a-z]+|\d+(?:\.\d+)?', s) if t not in ('ans', 'an', 'years', 'year', 'co', 'gerant', 'suppleant', 'et', 'and'))


def nature(nat, k, a, b):
    """Valeur : un chiffre, une note ou une valeur courte change vraiment ; Forme : même contenu écrit autrement ;
    Texte : texte rédigé (type, compartiment, disclaimer, politiques) différent du document."""
    if a and b and jetons(a) == jetons(b):
        return 'Forme'
    if nat == 'long' or k == 'type_fonds':
        return 'Texte'
    return 'Valeur'


def isin_ok(i):
    if not re.fullmatch(r'[A-Z]{2}[A-Z0-9]{9}\d', i or ''):
        return False
    d = ''.join(str(int(c, 36)) for c in i[:-1])
    t = sum(int(c) if k % 2 else sum(divmod(2 * int(c), 10)) for k, c in enumerate(reversed(d)))
    return (10 - t % 10) % 10 == int(i[-1])


def main(fj, cj, mj, sortie):
    site = json.load(open(fj))
    feuille = {}
    for f in ('fiches-1.csv', 'fiches-2.csv'):
        for r in csv.reader(open(SHEET + f)):
            feuille[r[1].strip().upper()] = dict(zip(COLS, r))
    ecarts, autres = [], []
    stats = collections.Counter()
    for f in sorted(site, key=lambda x: x['FundId']):
        isin = (f['ISIN'] or '').strip().upper()
        g = feuille.get(isin)
        base = [f['FundId'], isin, f['Name'], 'Actif' if f['IsActive'] else 'Inactif']
        if not isin_ok(isin):
            autres.append(base + ['ISIN invalide', f'« {f["ISIN"]} » ({len(f["ISIN"] or "")} caractères)'
                                  + (' : code interne OneLife (fonds FIC)' if isin.startswith('XFCS') else
                                     ' : mandat / profil FID sans ISIN propre' if f['FID'] else '')])
        cid, sri = f.get('ClassificationId'), num(f.get('Risque'))
        if cid in (5, 6, 7) and not f['FID']:
            autres.append(base + ['Classification hors grille', '« %s » (classe réservée aux fiches FID)' % f.get('Classification')])
        cl = (f.get('Classification') or '').lower()
        if sri and cl and ((sri <= 2 and cl in ('dynamique', 'agressif')) or (sri >= 5 and cl in ('défensif', 'sécuritaire'))
                           or (sri >= 4 and cl == 'sécuritaire')):
            autres.append(base + ['Classification contraire au risque', '%s avec un SRI de %g' % (f.get('Classification'), sri)])
        if f['FID'] == 0 and not cid:
            autres.append(base + ['Classification vide', ''])
        if f['FID'] == 0 and not sri:
            autres.append(base + ['SRI vide', ''])
        if not g:
            autres.append(base + ['Absente du classeur', 'Fiche du site hors gamme One Life (pas de valeur de référence)'])
            continue
        stats['fiches comparées'] += 1
        ref = g['origine']
        n_ec = 0
        for k, lab, sk, nat in CHAMPS:
            a, b = g[k].strip(), f.get(sk)
            b_txt = plain(b)
            if not a and not b_txt:
                continue
            if a and b_txt and egal(nat, a, b):
                continue
            if nat == 'num' and a and b_txt and num(b_txt) == 0 and num(a) is None:
                continue
            if not a and nat == 'num' and num(b_txt) == 0:
                continue  # 0 sur le site = non renseigné
            genre = 'à remplir' if not b_txt or (nat == 'num' and num(b_txt) == 0) else 'à vider' if not a else 'à corriger'
            if nat == 'long':
                av, ap = (b_txt[:200] + ('…' if len(b_txt) > 200 else '')), (a[:200] + ('…' if len(a) > 200 else ''))
            else:
                av, ap = b_txt, a
            ecarts.append(base + [g['statut'], ref, lab, genre, nature(nat, k, a, b_txt), av, ap])
            stats['nature ' + ecarts[-1][8]] += 1
            stats[genre] += 1
            n_ec += 1
        stats['fiches avec écarts' if n_ec else 'fiches identiques'] += 1
    # sortie
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Synthèse'
    par_champ = collections.Counter((e[6], e[7]) for e in ecarts if e[8] != 'Forme')
    lignes = [['Écarts entre invest-law.eu et le classeur « Gamme One Life complète »'],
              ['Site lu le 29/10/2026 (GET /api/funds, lecture seule) ; classeur = onglet Fiches (CSV du dépôt).'],
              ['« Avant » = valeur du site, « Après » = valeur du classeur (vérifiée contre la factsheet et le KID).'], []]
    lignes += [[k, v] for k, v in stats.most_common()]
    lignes += [[], ['Par champ (hors écarts de forme)', 'à corriger', 'à remplir', 'à vider']]
    for lab in [c[1] for c in CHAMPS]:
        lignes.append([lab] + [par_champ[(lab, t)] for t in ('à corriger', 'à remplir', 'à vider')])
    lignes += [[], ['Autres points', len(autres)]]
    for r in lignes:
        ws.append(r)
    ws['A1'].font = Font(bold=True, size=13)
    ws.column_dimensions['A'].width = 34
    for nom, hdr, rows in [('Écarts', ['FundId', 'ISIN', 'Nom', 'Actif', 'Statut classeur', 'Origine classeur', 'Champ',
                                       'Type', 'Avant (site)', 'Après (classeur)'], ecarts),
                           ('Autres points', ['FundId', 'ISIN', 'Nom', 'Actif', 'Point', 'Détail'], autres)]:
        w = wb.create_sheet(nom)
        w.append(hdr)
        for r in rows:
            w.append(r)
        for c in w[1]:
            c.font = Font(bold=True, color='FFFFFF')
            c.fill = PatternFill('solid', fgColor='1F3A5F')
        w.freeze_panes = 'D2'
        w.auto_filter.ref = w.dimensions
        for col, wd in zip('ABCDEFGHIJK', [8, 15, 40, 8, 22, 26, 20, 11, 9, 50, 50]):
            w.column_dimensions[col].width = wd
        for row in w.iter_rows(min_row=2):
            for c in row:
                c.alignment = Alignment(wrap_text=True, vertical='top')
    wb.save(sortie)
    json.dump({'stats': stats, 'par_champ': {f'{a}|{b}': v for (a, b), v in par_champ.items()},
               'autres': collections.Counter(a[4] for a in autres)}, open(sortie.replace('.xlsx', '.json'), 'w'),
              ensure_ascii=False, indent=1)
    print(dict(stats))
    print(collections.Counter(a[4] for a in autres))
    print(par_champ.most_common(30))


if __name__ == '__main__':
    main(*sys.argv[1:5])
