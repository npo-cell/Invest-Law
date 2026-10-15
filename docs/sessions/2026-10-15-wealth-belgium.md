# 2026-10-15 — Gamme Wealth Belgium (One Life) : mise en place

## Objectif
Intégrer sur invest-law.eu les fonds de la gamme **Wealth Belgium** de One Life, étape par étape.

## Étape 1 (15/10/2026) : liste nom + ISIN
- Source : fichier `FundsRange2026-10-15.xlsx` fourni par l'utilisatrice (export One Life, 29 colonnes : type, ISIN, nom, risque, maison, région, VNI, devise, catégorie MS, SFDR, performances…), copié dans `docs/wealth-belgium-2026-10-15/`.
- **347 fonds** (348 lignes avec l'en-tête) : 172 actions, 97 flexibles, 59 obligations, 15 ETF, 4 monétaires. ISIN tous valides, aucun doublon. Dont 5 fonds internes d'assurance (`XFCS…`, « FIC … »).
- Google Sheet créé sur le Drive de l'utilisatrice (colonnes « Nom du fonds », « ISIN », ordre du fichier source) : [Gamme Wealth Belgium One Life – Fonds et ISIN](https://docs.google.com/spreadsheets/d/1zL7Y2v4wVW6YQfu-eH8FLvzCQeoO6S8Eri8NOToHmq8/edit). Contenu relu après création : 347 paires nom/ISIN identiques à la source, même ordre.
- Copie CSV : `docs/wealth-belgium-2026-10-15/fonds-isin.csv`.
- Rien modifié sur invest-law.eu.

## À noter
- Le connecteur Google Sheets (édition) n'est pas actif dans la session : le fichier a été créé par Drive (import CSV). Pour ajouter des colonnes au même fichier aux étapes suivantes, il faut activer le connecteur Google Sheets.
- Repères : la gamme One Life déjà traitée compte 482 fonds (`factsheets/factsheets_gamme_one_life.xlsx`) ; le site a 488 fiches. Le rapprochement avec le site reste à faire.

## Étape 2 (15/10/2026) : maison de gestion
- Connecteur Google Sheets activé par l'utilisatrice ; colonne C « Maison de gestion » ajoutée dans le même Google Sheet (même lien), reprise telle quelle de la colonne « Fund company » du fichier source. Relu après écriture : 347 lignes nom / ISIN / maison conformes à la source.
- 104 libellés différents. Points d'attention pour le rattachement aux maisons du site :
  - variantes d'écriture d'une même société (ex. « BLACKROCK ASSET MANAGEMENT IRELAND LTD » / « BlackRock Asset Management Ireland Ltd », « La Financière de l'Echiquier » / « LA FINANCIERE DE L'ECHIQUIER », « FundRock Management Company S.A » / « S.A. ») ;
  - certains libellés désignent la société de gestion juridique (ManCo) ou un prestataire, pas le gérant : Waystone (8 fonds), FundRock (3), FundPartner Solutions (3), Universal-Investment, Hauck & Aufhäuser, Link Fund Manager Solutions, Degroof Petercam Asset Services, Andbank Luxembourg - PLEDGE…
- CSV du dépôt complété : `docs/wealth-belgium-2026-10-15/fonds-isin.csv` (nom, ISIN, maison).
