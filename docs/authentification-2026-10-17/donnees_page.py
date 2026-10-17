#!/usr/bin/env python3
"""Prépare les données compactes de la page d'authentification et les injecte dans le modèle HTML.
Usage : python3 -I donnees_page.py <final.json> <modele.html> <sortie.html>"""
import json, sys, collections
LAB = {'date_creation': 'Date de création', 'devise': 'Devise', 'compartiment': 'Compartiment', 'gerants': 'Gérants',
       'encours': 'Encours', 'encours_devise': "Devise de l'encours", 'encours_date': "Date de l'encours",
       'frais_gestion': 'Frais de gestion', 'frais_courants': 'Frais courants / TER', 'sri': 'SRI', 'indice': 'Indice',
       'categorie': 'Catégorie', 'sfdr': 'SFDR', 'durable_pct': 'Invest. durables (%)', 'duration': 'Duration',
       'qualite': 'Qualité des émetteurs', 'disclaimer': 'Disclaimer', 'politique_fr': 'Politique FR',
       'politique_en': 'Politique EN'}


def org(o):
    return 'site' if o.startswith('invest') else 'wb' if o.startswith('Wealth') else 'new' if o.startswith('Fiche') else 'none'


def verdict(r):
    if r['origine'].startswith('Aucune'):
        return 'none'
    st = [x['st'] for x in r['cells'].values()]
    a = r['alloc']['st'] if r['alloc'] else None
    if 'DIFFERENT' in st or a == 'DIFFERENT' or r['autre_part']:
        return 'fix'
    if 'ABSENT' in st or a in ('ABSENT', 'PARTIEL'):
        return 'part'
    return 'ok'


F = json.load(open(sys.argv[1]))
out, tot, per = [], collections.Counter(), collections.Counter()
for r in F:
    iss = []
    for k, x in r['cells'].items():
        tot[x['st']] += 1
        if x['st'] in ('DIFFERENT', 'ABSENT', 'AUTRE_SOURCE'):
            per[(LAB.get(k, k), x['st'])] += 1
            iss.append([LAB.get(k, k), x['st'][0], x['v'][:160], (x.get('vdoc') or '')[:160], (x.get('note') or '')[:220]])
    out.append({'n': int(r['n']), 'i': r['isin'], 'm': r['nom'], 'o': org(r['origine']), 'v': verdict(r),
                'f': r['fs_date'], 'c': sum(1 for x in r['cells'].values() if x['st'] == 'CONFORME'),
                't': sum(1 for x in r['cells'].values() if x['st'] != 'JUGEMENT'), 'x': iss,
                'a': [r['alloc']['st'], r['alloc']['note'][:200]] if r['alloc'] and r['alloc']['st'] != 'CONFORME' else None,
                'al': r['alloc_total'], 'fr': r['fraicheur'], 'ap': r['autre_part'], 'rn': r.get('renomme', ''),
                'dk': r['doc_site_est_kid']})
fields = sorted({k for k, _ in per}, key=lambda k: -(per[(k, 'DIFFERENT')] + per[(k, 'ABSENT')]))
meta = {'tot': dict(tot), 'champs': [[k, per[(k, 'DIFFERENT')], per[(k, 'ABSENT')]] for k in fields if k != 'Catégorie'],
        'alloc': dict(collections.Counter(r['alloc']['st'] for r in F if r['alloc'])),
        'alloc_lignes': sum(r['alloc_total'] for r in F)}
html = open(sys.argv[2]).read().replace('/*DATA*/null', json.dumps(out, ensure_ascii=False, separators=(',', ':'))) \
    .replace('/*META*/null', json.dumps(meta, ensure_ascii=False, separators=(',', ':')))
open(sys.argv[3], 'w').write(html)
print(meta)
