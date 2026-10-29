#!/usr/bin/env python3
"""Plan du report des VALEURS du classeur vers invest-law.eu (29/10/2026).
Usage : python3 -I plan.py <funds.json> <sortie_dir>
Pour chaque fiche du site présente dans le classeur, valeurs « à corriger » ou « à remplir » (jamais « à vider ») des champs :
encours, frais de gestion, frais courants, SRI, classification, qualité des émetteurs, date de création, devise, catégorie.
Écrit <sortie_dir>/<FundId>.json (corps partiel pour `investlaw.py set --json`) et plan.csv (ancien -> nouveau)."""
import csv, json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'ecarts-site-2026-10-29'))
from comparer import COLS, SHEET, plain, num, egal, jetons

# fiches dont le nom ne correspond pas à l'ISIN : à trancher avant tout report
EXCLUS = {9: 'nom « ALLIANZ STRATEGY 50 NT EUR » mais ISIN LU1093406186 = Allianz Dynamic Multi Asset Strat SRI 50 AT',
          401: 'nom « ROCHE-BRUNE ZONE EURO ACTIONS P » mais ISIN FR0010283838 = Stratégie Euro Div Responsables P (renommage ?)'}
CLASSES = {'Défensif': 1, 'Equilibré': 2, 'Dynamique': 4, 'Agressif': 3}
CHAMPS = [('encours', 'total_assets', 'TotalAssets', 'num'), ('frais_gestion', 'fees', 'Fees', 'num'),
          ('frais_courants', 'ter', 'TER', 'num'), ('sri', 'risque', 'Risque', 'num'),
          ('classification', 'classification_id', 'Classification', 'txt'),
          ('qualite', 'issuer_quality', 'IssuerQuality', 'txt'), ('date_creation', 'creation_date', 'CreationDate', 'date'),
          ('devise', 'currency', 'Currency', 'txt'), ('categorie', 'category', 'Category', 'txt')]


def main(fj, out):
    os.makedirs(out, exist_ok=True)
    feuille = {}
    for f in ('fiches-1.csv', 'fiches-2.csv'):
        for r in csv.reader(open(SHEET + f)):
            feuille[r[1].strip().upper()] = dict(zip(COLS, r))
    lignes = []
    for f in sorted(json.load(open(fj)), key=lambda x: x['FundId']):
        g = feuille.get((f['ISIN'] or '').strip().upper())
        if not g or f['FID'] or f['FundId'] in EXCLUS:
            continue
        corps = {}
        for k, champ, sk, nat in CHAMPS:
            a, b = g[k].strip(), plain(f.get(sk))
            if not a:
                continue  # « à vider » : pas dans cette passe
            if b and (egal(nat, a, b) or jetons(a) == jetons(b)):
                continue
            if nat == 'num' and num(a) is None:
                continue
            if k == 'classification':
                if a not in CLASSES or CLASSES[a] == f.get('ClassificationId'):
                    continue
                corps[champ] = CLASSES[a]
            elif nat == 'num':
                corps[champ] = ('%.2f' % num(a)) if champ in ('total_assets', 'fees', 'ter') else int(num(a))
            else:
                corps[champ] = a
            lignes.append([f['FundId'], f['ISIN'], f['Name'], champ, b, a])
        if corps:
            json.dump(corps, open(os.path.join(out, '%s.json' % f['FundId']), 'w'), ensure_ascii=False)
    with open(os.path.join(out, 'plan.csv'), 'w', newline='') as h:
        w = csv.writer(h)
        w.writerow(['FundId', 'ISIN', 'Nom', 'Champ', 'Avant (site)', 'Après (classeur)'])
        w.writerows(lignes)
    print(len({l[0] for l in lignes}), 'fiches,', len(lignes), 'valeurs')


if __name__ == '__main__':
    main(*sys.argv[1:3])
