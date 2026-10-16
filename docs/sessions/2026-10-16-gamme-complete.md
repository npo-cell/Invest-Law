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

## Suite : les 53 fonds sans fiche (16/10/2026, demande de l'utilisatrice)
- Consigne : `docs/gamme-complete-2026-10-16/fonds-restants/CONSIGNE.md` (mêmes règles que Wealth Belgium : recherche + fiches). 5 lots en parallèle (4 × 8 fonds classiques, 1 lot de 21 FIC).
- **Résultat : 28 fonds préparés** (26 factsheets, 28 KID, rangés dans `INVESTLAW/` avec leur `.txt`), **25 sans document public** : 21 FIC (fonds internes, rien de public, comme le 12/10), Holberg Likviditet et Lannebo Sverige Plus / Teknik (documents seulement en norvégien / suédois), LAIQON Global Equities Dynamic R (lancé le 01/10/2026, KID seulement en allemand). Fairwin Evolution Strategy et Investerum : KID seul (pas de factsheet publiée).
- Contrôle indépendant : chaque PDF retenu est un vrai PDF contenant l'ISIN de la ligne ; `verif_fiche.py` : 0 manquant sauf 5 écarts expliqués en remarque (libellés imprimés en double, indice « Aucun »).
- Catégorie One Life : 7 fonds (Robeco Indian même ISIN ; FvS MO II, JPM America Equity / Global Balanced / Global Focus, Templeton GTR SEK / USD via une autre part du même fonds), `fonds-restants/categorie/correspondances.csv`.
- Points à valider (détail dans les remarques des fiches) : Aviva EM Equity Income (renommé Global EM Core, synthèse trimestrielle professionnelle seulement), factsheets « réservées aux professionnels » (Candriam, Aviva), allocations limitées aux 10 lignes quand les répartitions sont des images (BlackRock, Candriam, ODDO), encours abrdn Liquidity laissé vide (« EUR4,3M » ambigu), Templeton A SEK = part couverte SEK-H1, ODDO « Exklusiv » renommé, Investerum renommé Global Value, KID anglais 2026 retenu pour East Capital Frontier (le KID français date de 2024).
- **Google Sheet mis à jour** (même lien) : statuts « Préparé (gamme complète) » (28) et « À faire (aucun document public) » (25) ; Fiches, Allocations (19 755 lignes) et Documents (1 826 PDF) réimportés depuis le commit 3aea9d3 ; contrôle cellule par cellule : 0 écart de valeur (16 libellés de maturité remis en texte, arrondis d'affichage corrigés). Chiffres clés : 463 en ligne, 364 préparés, 25 à faire (97,1 % faits).
- Rien modifié sur invest-law.eu.
