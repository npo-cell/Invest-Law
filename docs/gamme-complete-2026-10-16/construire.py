#!/usr/bin/env python3
"""Classeur « Gamme One Life complète » : construit les CSV importés dans le Google Sheet.

Sources : export One Life (FundsRange2026-10-16.xlsx), fiches invest-law.eu (site_full.json, lu via l'API),
fiches préparées Wealth Belgium (docs/wealth-belgium-2026-10-15/sheet/), PDF rangés dans INVESTLAW/.
Usage : python3 construire.py <site_full.json>
"""
import csv, html, json, os, re, sys, urllib.parse, datetime
import openpyxl

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
WB = os.path.join(RACINE, 'docs/wealth-belgium-2026-10-15/sheet')
OUT = os.path.join(ICI, 'sheet')
BRANCHE = 'claude/kind-edison-2o3dsu'
GITHUB = 'https://github.com/npo-cell/Invest-Law/blob/%s/' % BRANCHE
SITE = 'https://www.invest-law.eu/simulation.html?fundId=%s'
MOIS = {m: i + 1 for i, m in enumerate(['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet',
                                         'aout', 'septembre', 'octobre', 'novembre', 'decembre'])}
ALLOC = [('positions', 'Positions'), ('sectors', 'Secteurs'), ('assets', "Classes d'actifs"),
         ('geographies', 'Zones géographiques')]


def txt(v):
    """Texte du site : entités HTML décodées, paragraphes séparés par une ligne vide."""
    if v is None:
        return ''
    s = str(v)
    s = re.sub(r'(?i)<br\s*/?>', '\n', s)
    s = re.sub(r'(?i)</p>\s*', '\n\n', s)
    s = re.sub(r'(?i)<li[^>]*>', '- ', s)
    s = re.sub(r'(?i)</li>', '\n', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(html.unescape(s)).replace('\xa0', ' ')
    s = re.sub(r'[ \t]+\n', '\n', s)
    return re.sub(r'\n{3,}', '\n\n', s).strip()


def num(v):
    try:
        x = float(v)
    except (TypeError, ValueError):
        return ''
    return ('%.4f' % x).rstrip('0').rstrip('.')


def date_rapport(r):
    """Fin du mois cité dans le nom du rapport (« Rapport de gestion Septembre 2026 »), sinon date du rapport."""
    n = html.unescape(r.get('report_name') or '').lower()
    n = n.translate(str.maketrans('éèêûô', 'eeeuo'))
    m = re.search(r'(janvier|fevrier|mars|avril|mai|juin|juillet|aout|septembre|octobre|novembre|decembre)\s+(\d{4})', n)
    if m:
        y, mo = int(m.group(2)), MOIS[m.group(1)]
        d = datetime.date(y + (mo == 12), mo % 12 + 1, 1) - datetime.timedelta(days=1)
        return d.isoformat()
    m = re.search(r'(\d{4}-\d{2}-\d{2})', r.get('file_name') or '')
    return m.group(1) if m else (r.get('report_date') or '')


def pdfs_depot():
    """ISIN -> liste de PDF rangés dans INVESTLAW/ (type, langue, date, chemin)."""
    out = {}
    for d, _, fs in os.walk(os.path.join(RACINE, 'INVESTLAW')):
        for f in fs:
            m = re.match(r'([A-Z0-9]{12})__([A-Za-z-]+)_([A-Z]{2})_(\d{4}-\d{2}-\d{2})\.pdf$', f)
            if m:
                chemin = os.path.relpath(os.path.join(d, f), RACINE)
                out.setdefault(m.group(1), []).append(
                    {'type': 'KID' if m.group(2) == 'KID' else 'Factsheet' + (' hebdo' if 'hebdo' in m.group(2) else ''),
                     'langue': m.group(3), 'date': m.group(4),
                     'url': GITHUB + urllib.parse.quote(chemin)})
    return out


def dernier(docs, typ):
    c = [d for d in docs if d['type'] == typ]
    return max(c, key=lambda d: d['date']) if c else None


def main(site_json):
    os.makedirs(OUT, exist_ok=True)
    s = json.load(open(site_json))
    site = {f['ISIN'].strip().upper(): f for f in s['funds'] if f.get('ISIN')}
    detail = s['detail']
    wb_f = {r[1].strip().upper(): r for r in csv.reader(open(os.path.join(WB, 'fiches.csv')))}
    wb_a = {}
    for k in (1, 2):
        for r in csv.reader(open(os.path.join(WB, 'allocations-%d.csv' % k))):
            wb_a.setdefault(r[1].strip().upper(), []).append(r)
    depot = pdfs_depot()
    # 53 fonds restants : fiches préparées le 16/10 (fonds-restants/fiches), même ordre de colonnes que Wealth Belgium
    CLES = ['n', 'isin', 'nom', 'maison', 'factsheet_date', 'kid_date', 'date_creation', 'devise', 'type_fonds',
            'compartiment', 'gerants', 'encours_millions', 'encours_devise', 'encours_date', 'frais_gestion',
            'frais_courants', 'sri', 'indice', 'classification', 'categorie', 'sfdr', 'durable_pct', 'duration',
            'qualite_emetteurs', 'disclaimer', 'politique_fr', 'politique_en', 'source_politique', 'remarques']
    rf, rf_docs = {}, {}
    for fj in sorted(os.listdir(os.path.join(ICI, 'fonds-restants', 'fiches'))):
        j = json.load(open(os.path.join(ICI, 'fonds-restants', 'fiches', fj)))
        isin = j['isin'].strip().upper()
        rf[isin] = [str(j.get(k) or '') for k in CLES]
        rf_docs[isin] = (j.get('factsheet_fichier') or '', j.get('kid_fichier') or '')
        wb_a[isin] = [['', isin, j['nom'], a['type'], a['libelle'], a['pct'], j.get('factsheet_date') or '']
                      for a in j.get('allocations') or []]
    # fiches refaites le 19/10 après l'authentification (docs/correction-2026-10-19/fiches) : prioritaires
    cf, cf_docs, cf_a = {}, {}, {}
    cdir = os.path.join(RACINE, 'docs', 'correction-2026-10-19', 'fiches')
    for fj in sorted(os.listdir(cdir)) if os.path.isdir(cdir) else []:
        j = json.load(open(os.path.join(cdir, fj)))
        isin = j['isin'].strip().upper()
        cf[isin] = [str(j.get(k) or '') for k in CLES]
        cf_docs[isin] = (j.get('factsheet_fichier') or '', j.get('kid_fichier') or '')
        cf_a[isin] = [[a['type'], a['libelle'], a['pct'], j.get('factsheet_date') or ''] for a in j.get('allocations') or []]

    rows = list(openpyxl.load_workbook(os.path.join(ICI, 'FundsRange2026-10-16.xlsx'), read_only=True)
                .active.iter_rows(values_only=True))
    vus, gamme = set(), []
    for r in rows[1:]:
        if r[1] and r[1].strip().upper() not in vus:
            vus.add(r[1].strip().upper())
            gamme.append(r)

    G, F, A, D = [], [], [], []
    for i, r in enumerate(gamme):
        n = i + 2
        isin, nom, maison = r[1].strip().upper(), r[2], r[6]
        f, w = site.get(isin), wb_f.get(isin) or rf.get(isin)
        restant = isin in rf and isin not in wb_f
        docs = depot.get(isin, [])
        fs_dep, kid = dernier(docs, 'Factsheet'), dernier(docs, 'KID')
        rap = sorted(detail.get(str(f['FundId']), {}).get('rapports', []) if f else [],
                     key=date_rapport, reverse=True)
        if f and w:
            statut = 'Sur invest-law (aussi préparé Wealth Belgium)'
        elif f:
            statut = 'Sur invest-law'
        elif restant:
            statut = 'Préparé (gamme complète)' if any(rf_docs[isin]) else 'À faire (aucun document public)'
        elif w:
            statut = 'Préparé (Wealth Belgium)'
        else:
            statut = 'À faire'
        lien_site = SITE % f['FundId'] if f else ''

        # Documents : PDF du dépôt + rapports en ligne sur invest-law
        for d in sorted(docs, key=lambda d: (d['type'], d['date']), reverse=True):
            D.append([n, isin, nom, d['type'], d['langue'], d['date'], 'Dépôt (dossier INVESTLAW)', d['url']])
        for x in rap:
            D.append([n, isin, nom, 'Rapport de gestion (en ligne)', '', date_rapport(x), 'invest-law.eu',
                      x.get('file_url') or ''])

        if isin in cf:
            c = cf[isin]
            fs_url, kid_url = [GITHUB + urllib.parse.quote(p) if p else '' for p in cf_docs[isin]]
            F.append([n, isin, nom, maison, statut, lien_site, c[4], fs_url if c[4] else '', c[5], kid_url if c[5] else '']
                     + c[6:29] + ['Corrigée le 19/10 (factsheet / KID les plus récents)'])
            for x in cf_a[isin]:
                A.append([n, isin, nom] + x + ['Fiche corrigée le 19/10 (factsheet)'])
        elif f:
            fs_date, fs_url = (date_rapport(rap[0]), rap[0].get('file_url') or '') if rap else (
                (fs_dep['date'], fs_dep['url']) if fs_dep else ('', ''))
            sfdr = re.search(r'Article\s*(\d)', f.get('ESG_code') or '')
            esg = num(f.get('ESG'))
            rem = []
            if not f.get('IsActive'):
                rem.append('Fiche inactive sur invest-law.eu.')
            if w:
                rem.append('Une fiche Wealth Belgium a aussi été préparée (classeur Wealth Belgium).')
            if f.get('ESG_code') and not sfdr:
                rem.append('Code ESG du site : %s.' % f['ESG_code'])
            if f.get('last_update'):
                rem.append('Fiche mise à jour sur le site le %s.' % f['last_update'])
            pol_fr, pol_en = txt(f.get('InvestmentPolicy')), txt(f.get('InvestmentPolicyEN'))
            F.append([n, isin, nom, maison, statut, lien_site, fs_date, fs_url,
                      kid['date'] if kid else '', kid['url'] if kid else '',
                      f.get('CreationDate') or '', f.get('Currency') or '', txt(f.get('FundType')),
                      txt(f.get('Compartment')), txt(f.get('fund_manager')), num(f.get('TotalAssets')), '', '',
                      num(f.get('Fees')), num(f.get('TER')), f.get('Risque') or '', txt(f.get('BenchmarkName')),
                      f.get('Classification') or '', txt(f.get('Category')), sfdr.group(1) if sfdr else '',
                      esg if esg not in ('', '0') else '', num(f.get('Duration')), txt(f.get('IssuerQuality')),
                      txt(f.get('Disclaimer')), pol_fr, pol_en, 'invest-law.eu' if (pol_fr or pol_en) else '',
                      ' '.join(rem), 'invest-law.eu'])
            al = detail[str(f['FundId'])]['allocations']
            for k, lib in ALLOC:
                for x in al.get(k) or []:
                    A.append([n, isin, nom, lib, txt(x.get('label_fr') or x.get('displayName') or x.get('name')),
                              num(x.get('percentage')), fs_date, 'invest-law.eu'])
        elif w:
            # colonnes Wealth Belgium : n ISIN nom maison fs_date kid_date creation devise type compartiment
            # gérants encours devise date frais courants sri indice classif catégorie sfdr durable duration
            # qualité disclaimer pol_fr pol_en source remarques
            fs_url = fs_dep['url'] if fs_dep and fs_dep['date'] == w[4] else (fs_dep['url'] if fs_dep else '')
            kid_url = kid['url'] if kid else ''
            if restant:
                fs_url, kid_url = [GITHUB + urllib.parse.quote(p) if p else '' for p in rf_docs[isin]]
                origine = 'Fiche préparée le 16/10 (factsheet / KID)' if any(rf_docs[isin]) else 'Aucune (aucun document public)'
            else:
                origine = 'Wealth Belgium (factsheet / KID)'
            F.append([n, isin, nom, maison, statut, '', w[4], fs_url if w[4] else '', w[5], kid_url if w[5] else '']
                     + w[6:29] + [origine])
            for x in wb_a.get(isin, []):
                A.append([n, isin, nom] + x[3:7] + ['Fiche du 16/10 (factsheet)' if restant else 'Wealth Belgium (factsheet)'])
        else:
            F.append([n, isin, nom, maison, statut] + [''] * 28 + ['Aucune (à faire)'])

        G.append([n, nom, isin, maison, statut, r[0], r[3], r[7], r[9], r[10], r[11] or '', r[12] or '',
                  r[8] if r[8] not in (None, '-') else '',
                  r[13].strftime('%Y-%m-%d') if hasattr(r[13], 'strftime') else (r[13] or '')]
                 + [x if isinstance(x, (int, float)) else '' for x in (r[16], r[23], r[19], r[20], r[21])]
                 + [lien_site])

    A.sort(key=lambda x: (x[0], x[3]))
    # fichiers de moins de ~1,2 Mo pour IMPORTDATA
    for nomf, data, parts in [('gamme', G, 1), ('fiches', F, 2), ('allocations', A, 2), ('documents', D, 1)]:
        t = -(-len(data) // parts)
        for k in range(parts):
            suffixe = '' if parts == 1 else '-%d' % (k + 1)
            with open(os.path.join(OUT, nomf + suffixe + '.csv'), 'w', newline='') as fh:
                csv.writer(fh).writerows(data[k * t:(k + 1) * t])
        print(nomf, len(data), 'lignes', len(data[0]), 'colonnes')
    import collections
    print(collections.Counter(g[4] for g in G))


if __name__ == '__main__':
    main(sys.argv[1])
