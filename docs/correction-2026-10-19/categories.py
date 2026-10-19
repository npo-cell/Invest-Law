#!/usr/bin/env python3
"""Remplit la catégorie des fiches corrigées : « Asset Type (Level 2) » du fichier OneLife Fund Classification
(même ISIN, sinon autre part du même fonds via les tables de correspondance), sinon catégorie du site gardée avec remarque.
Usage : python3 -I categories.py <OneLife Fund Classification.xlsx>   (fichier interne, non versionné)"""
import csv, glob, json, os, sys, openpyxl
RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
cls = {str(r[1]).strip().upper(): r[4] for r in list(openpyxl.load_workbook(sys.argv[1], read_only=True).worksheets[0]
                                                    .iter_rows(values_only=True))[1:] if r[1] and r[4]}
corr = {}
for r in csv.DictReader(open(os.path.join(RAC, 'docs/wealth-belgium-2026-10-15/categorie/correspondances.csv'))):
    v = list(r.values())
    if v[-1]:
        corr[v[1]] = (v[-1], v[3], v[4])
for r in csv.DictReader(open(os.path.join(RAC, 'docs/gamme-complete-2026-10-16/fonds-restants/categorie/correspondances.csv'))):
    v = list(r.values())
    corr[v[0]] = (v[3], v[1], v[2])
F = {r[1]: r for f in ('fiches-1.csv', 'fiches-2.csv')
     for r in csv.reader(open(os.path.join(RAC, 'docs/gamme-complete-2026-10-16/sheet', f)))}
stat = {'fichier': 0, 'autre part': 0, 'site': 0, 'vide': 0}
for p in sorted(glob.glob(os.path.join(RAC, 'docs/correction-2026-10-19/fiches/*.json'))):
    d = json.load(open(p))
    i = d['isin']
    rem = d.get('remarques', '') or ''
    if i in cls:
        d['categorie'], note, k = cls[i], 'Catégorie : « Asset Type (Level 2) » du fichier OneLife Fund Classification (même ISIN).', 'fichier'
    elif i in corr:
        c, nom, src = corr[i]
        d['categorie'], note, k = c, f'Catégorie : fichier OneLife Fund Classification, reprise de la part {nom} ({src}) du même fonds.', 'autre part'
    elif F.get(i) and F[i][23]:
        d['categorie'], note, k = F[i][23], 'Catégorie : celle du site invest-law.eu (le fonds n’est pas dans le fichier OneLife Fund Classification).', 'site'
    else:
        d['categorie'], note, k = '', '', 'vide'
    if note and 'Catégorie :' not in rem:
        d['remarques'] = (rem.rstrip() + ' ' + note).strip()
    stat[k] += 1
    json.dump(d, open(p, 'w'), ensure_ascii=False, indent=1)
print(stat)
