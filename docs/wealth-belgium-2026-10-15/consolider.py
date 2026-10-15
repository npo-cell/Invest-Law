"""Consolide les résultats des lots et revérifie chaque PDF retenu.

Contrôles indépendants des agents : le fichier existe, c'est un PDF, son texte
contient l'ISIN de la ligne, langue FR/EN dans le nom, type de document cohérent.
Un document qui échoue est compté « Non trouvé » (exactitude avant tout).

Sortie : recapitulatif.csv (une ligne par fonds) + affichage des anomalies.
Usage : python3 -I docs/wealth-belgium-2026-10-15/consolider.py
"""
import csv, glob, json, os, re, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
D = os.path.join(ROOT, 'docs', 'wealth-belgium-2026-10-15')

KID_WORDS = ('informations cl', 'key information document')


def texte(pdf):
    txt = pdf[:-4] + '.txt'
    if not os.path.exists(txt):
        subprocess.run(['pdftotext', '-layout', pdf, txt], check=False)
    return open(txt, encoding='utf-8', errors='ignore').read() if os.path.exists(txt) else ''


def controle(isin, doc, kind):
    if not doc or doc.get('statut') != 'Trouvé':
        return 'Non trouvé', ''
    f = doc.get('fichier') or ''
    p = f if os.path.isabs(f) else os.path.join(ROOT, f)
    if not os.path.exists(p):
        return 'Non trouvé', 'fichier absent'
    if open(p, 'rb').read(5) != b'%PDF-':
        return 'Non trouvé', "n'est pas un PDF"
    name = os.path.basename(p)
    if not re.match(rf'{isin}__{kind}_(FR|EN)_\d{{4}}-\d\d-\d\d\.pdf$', name):
        return 'Non trouvé', f'nom/langue non conforme : {name}'
    t = texte(p)
    if isin not in re.sub(r'\s', '', t) and isin not in t:
        return 'Non trouvé', 'ISIN absent du PDF'
    low = t.lower()
    if kind == 'KID' and not any(w in low for w in KID_WORDS):
        return 'Non trouvé', 'ne ressemble pas à un KID'
    fs_words = ('fiche', 'factsheet', 'fact sheet', 'reporting', 'mensuel', 'monthly', 'données au', 'as at', 'as of')
    if kind == 'Factsheet' and not any(w in low for w in fs_words):
        return 'Non trouvé', 'ne ressemble pas à une factsheet'
    if kind == 'KID' and any(w in low[:1500] for w in ('fiche technique', 'factsheet', 'reporting mensuel')):
        return 'Non trouvé', 'ressemble à une factsheet, pas à un KID'
    return 'Trouvé', os.path.relpath(p, ROOT)


def main():
    entree = {o['isin']: o for f in sorted(glob.glob(os.path.join(D, 'recherche', 'lot-*-entree.json')))
              for o in json.load(open(f, encoding='utf-8'))}
    res = {}
    for f in sorted(glob.glob(os.path.join(D, 'recherche', 'lot-*-resultat.json'))):
        for r in json.load(open(f, encoding='utf-8')):
            res[r['isin']] = r
    rows, anomalies = [], []
    for isin, o in sorted(entree.items(), key=lambda kv: kv[1]['n']):
        r = res.get(isin, {})
        out = {'n': o['n'], 'isin': isin, 'nom': o['nom']}
        for kind, key in (('Factsheet', 'factsheet'), ('KID', 'kid')):
            doc = r.get(key) or {}
            st, info = controle(isin, doc, kind)
            if doc.get('statut') == 'Trouvé' and st != 'Trouvé':
                anomalies.append(f"{o['n']} {isin} {kind}: {info}")
            out[kind] = st
            out[kind + '_fichier'] = info if st == 'Trouvé' else ''
            out[kind + '_date'] = doc.get('date', '') if st == 'Trouvé' else ''
            out[kind + '_url'] = doc.get('url', '') if st == 'Trouvé' else ''
        out['traite'] = isin in res
        out['notes'] = r.get('notes', '')
        rows.append(out)
    with open(os.path.join(D, 'recapitulatif.csv'), 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print('fonds', len(rows), 'traités', sum(r['traite'] for r in rows),
          'factsheets', sum(r['Factsheet'] == 'Trouvé' for r in rows),
          'KID', sum(r['KID'] == 'Trouvé' for r in rows))
    print('anomalies', len(anomalies))
    print('\n'.join(anomalies))


if __name__ == '__main__':
    main()
