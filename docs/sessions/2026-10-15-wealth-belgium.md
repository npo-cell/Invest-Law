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

## Étape 3 (15/10/2026) : factsheet la plus récente + KID pour les 347 fonds
- Consigne écrite : `docs/wealth-belgium-2026-10-15/CONSIGNE-recherche.md` (FR d'abord, sinon EN, jamais d'autre langue ; ISIN exact de la part institutionnelle ; sources gestionnaire > fundinfo > Morningstar ; non trouvé = noté). Règle de langue ajoutée au guide.
- Recherche en 12 lots parallèles (sous-agents), entrées/résultats dans `docs/wealth-belgium-2026-10-15/recherche/`.
- Rangement : `INVESTLAW/<MAISON>/<ISIN>/<ISIN>__Factsheet_<FR|EN>_<date>.pdf` et `__KID_…`, avec le texte extrait `.txt` à côté de chaque PDF (pour retrouver les informations sans rouvrir les PDF).
- Contrôle indépendant (`consolider.py` → `recapitulatif.csv`) : vrai PDF, ISIN dans le texte, type de document, langue FR/EN. Puis relecture des 60 factsheets où l'ISIN n'est pas seul en page 1 (`audit-parts.json`) : 57 OK, 0 autre part, 3 douteuses.
- **Résultat : factsheets 289/347 (dont 3 « à vérifier »), KID 330/347.** Factsheets au 30/09/2026 : 180 ; au 31/08/2026 : 106 ; autres : 3.
- Google Sheet mis à jour (colonnes D « Factsheet », E « KID », F « Remarque »), relu ligne à ligne contre `recapitulatif.csv` : 0 écart.
- Factsheets « à vérifier » (multi-parts, performances d'une autre classe) : Blue Whale T (IE00BJM0B852), DUNN WMA AP EUR (IE00BYZJ5G02), Fundsmith I (LU0690374029).
- Non trouvés, raisons principales : la part institutionnelle n'a pas de reporting propre (FFG I, BLI BI, Flossbach IT, LAIQON R, Leleux P, Qualion, certaines M&G où fundinfo ne propose que la fiche d'une autre part), fonds récents, 5 FIC (documents non publics). Détail par fonds : `recapitulatif.csv` et notes des `lot-XX-resultat.json`.
- Anomalies du fichier source One Life (colonne Fund company) : IE00B4L5Y983 iShares → « GOLDMAN SACHS AM », IE000N6I8IU2 JPM → « GOLDMAN SACHS AM », IE000L98FUF7 LAIQON → « AMUNDI ASSET MANAGEMENT » (signalé dans le Sheet ; les dossiers INVESTLAW suivent le fichier source).
- Fonds renommés (même ISIN) : DNCA Beyond Climate/Semperosa, DNCA Europe Growth, Schroder Global Energy Transition (→ Global Alternative Energy), Candriam Multi-Asset Premia, R-co Club, Sextant Bond Picking, Chahine (→ Irivest).
- Rien modifié sur invest-law.eu.

## Étape 4 (15/10/2026) : français d'abord partout, ménage
- Décision de l'utilisatrice : **français d'abord partout**, même si la version française est plus ancienne que l'anglaise ; fichiers en trop à supprimer.
- Recherche d'une version FR (fundinfo BE/LU/FR/CH/IE + site Ruffer) pour les 45 documents retenus en anglais. 9 factsheets passées en français, l'anglaise retirée : abrdn ×4 (FR au 30/06/2026), BlackRock MyMap ×2 (FR au 30/09/2026), PIMCO ×2 (FR au 31/08/2026), Ruffer (FR au 31/05/2026, la plus récente en français). Rejetée : M&G Global Listed Infrastructure (la FR est celle de la catégorie A). Les 35 autres n'existent qu'en anglais.
- 18 fichiers non retenus supprimés (anciennes versions, doublons EN, KID Enigma 2024). Seuls des fichiers ajoutés par cette recherche ont été touchés.
- Contrôle relancé : 289 factsheets, 330 KID, 0 anomalie. Statuts du Google Sheet inchangés.
