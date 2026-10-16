# 2026-10-16 — Gamme One Life complète : combien de fonds déjà faits

- **Source** : `FundsRange2026-10-16.xlsx` (export One Life fourni par l'utilisatrice, copié dans `docs/gamme-complete-2026-10-16/`) : 863 lignes, **852 ISIN uniques** (11 BGF en double).
- **Comparé à** : les 488 fiches d'invest-law.eu (API, 16/10 ~07h UTC) et les 347 fonds Wealth Belgium (`docs/wealth-belgium-2026-10-15/fonds-isin.csv`), par ISIN.
- **Résultat : 799 / 852 fonds faits (94 %)**
  - 463 déjà sur invest-law.eu (dont 11 sont aussi dans Wealth Belgium) ;
  - 336 préparés dans le Google Sheet Wealth Belgium, pas encore sur le site ;
  - **53 ni l'un ni l'autre** (`fonds-non-couverts.csv`) : 21 fonds internes FIC, 25 flexibles, 17 actions, 8 obligations, 3 monétaires ; 22 étaient déjà dans la gamme du 12/10 (factsheet introuvable à l'époque), 31 sont nouveaux.
- Autres constats : les 347 Wealth Belgium sont tous dans la gamme ; 25 fiches du site ne sont plus dans la gamme.
- Script : `docs/gamme-complete-2026-10-16/comparer.py`. Rien modifié sur le site.

## Suite : classeur de toute la gamme (16/10/2026, demande de l'utilisatrice)
- **Google Sheet** : [Gamme One Life complète – Fiches, allocations et documents](https://docs.google.com/spreadsheets/d/1TqVoLkuq0yKgI4cVJKzPt3q1Jxi6UGyCHh6SbPa5_20/edit), copie du classeur Wealth Belgium (l'original n'est pas modifié), agrandie aux 852 fonds.
- Onglets : Lisez-moi (chiffres clés en formules, légende, sources), Gamme (export One Life + statut), Fiches (37 colonnes : champs de la fiche, liens fiche en ligne / factsheet / KID), Allocations (19 034 lignes), Documents (1 772 PDF : 1 059 du dossier `INVESTLAW/` du dépôt, liens GitHub ; rapports publiés sur invest-law.eu, liens directs).
- Données : 463 fonds repris de invest-law.eu (API, 16/10 ~07h UTC ; les 11 fonds Wealth Belgium déjà en ligne suivent le site) ; 336 fiches préparées Wealth Belgium ; 53 fonds « À faire » avec seulement les données One Life.
- Import par `IMPORTDATA` (séparateur `;` : classeur en fr_FR, locale `en_US` pour les nombres) depuis le commit 37855fd, collage en valeurs. Contrôle cellule par cellule classeur ↔ CSV : 0 écart (15 libellés de maturité « 1-3 »… convertis en dates par Google, corrigés en texte).
- Mise en forme : en-têtes bleu foncé figés, colonnes n / ISIN / nom figées, lignes alternées, filtres, statut coloré, SRI vert→rouge, classification colorée, performances rouge/vert, dates jj/mm/aaaa, adresses brutes des liens dans des colonnes groupées (repliées).
- Fichiers : `docs/gamme-complete-2026-10-16/construire.py` (génère `sheet/*.csv`). Les liens « Voir la fiche » demandent d'être connecté à invest-law.eu.
- Rien modifié sur invest-law.eu.
