# INVESTLAW : factsheets à uploader sur invest-law.eu

422 factsheets (une par ISIN) téléchargées depuis le site du gestionnaire, fundinfo ou Morningstar. Pour chaque PDF, l'ISIN de la part et la date ont été vérifiés dans le document.

## Arborescence et nommage

`INVESTLAW/<MAISON_DE_GESTION>/<ISIN>/<ISIN>__<TypeDoc>_<LANGUE>_<AAAA-MM-JJ>.pdf`

- `TypeDoc` : `Factsheet` (mensuelle) ou `Factsheet-hebdo`.
- `LANGUE` : FR, EN, DE, ES, IT, NL ou SV.
- La date est celle de la factsheet.

## Manifeste

`MANIFEST_UPLOAD.xlsx` contient une ligne par fonds :

- ISIN ;
- nom du rapport à saisir (« Rapport de Gestion <Mois> <Année> », ou « Rapport hebdomadaire … ») ;
- date à saisir (jj/mm/aaaa) ;
- chemin du fichier ;
- points « À contrôler » ;
- une colonne « Statut upload », à remplir au fur et à mesure.

## Procédure (100 % cloud, depuis une session Claude Code sur ce dépôt)

Pré-requis : définir les variables `INVESTLAW_EMAIL` et `INVESTLAW_PASSWORD` dans les variables d'environnement de l'environnement cloud. Ne jamais les mettre dans le dépôt ni dans le chat.

1. `python3 tools/investlaw_upload.py login` : le site envoie un code à 6 chiffres par email. Claude le lit via le connecteur Gmail.
2. `python3 tools/investlaw_upload.py verify <code>`
3. `python3 tools/investlaw_upload.py plan` : associe chaque ISIN à sa fiche, puis compare la factsheet aux rapports déjà en ligne. Attention : sur le site, `report_date` est la **date d'upload**, pas le mois du rapport. Le mois est donc lu dans le **nom** du rapport (« Rapport de gestion Aout 2026 »), sans tenir compte des accents ni des majuscules. Les DIC sont ignorés. Résultats possibles :
   - `DEJA_PRESENT` : un rapport du même mois (ou du même nom) existe ;
   - `PLUS_RECENT_PRESENT` : le site a déjà un rapport plus récent, on n'envoie rien ;
   - `A_VERIFIER` : un rapport sans mois dans son nom a été déposé après le mois de notre factsheet, ce qui peut faire doublon ;
   - `A_UPLOADER` : notre factsheet est la plus récente ;
   - `FONDS_ABSENT` / `ISIN_EN_DOUBLE`.
4. `python3 tools/investlaw_upload.py upload --limit 1` : premier essai sur un seul fonds, à contrôler sur le site. Ensuite, `upload` sans limite.
5. Les lignes « A contrôler » ne sont envoyées qu'avec `--include-flagged`. Consigne du 12/10/2026 : chaque fonds doit avoir la factsheet la plus récente trouvée, donc on les inclut.
6. La session expire (erreur 401) : relancer `login` puis `verify` avec le **dernier** code reçu par email.

Le script ne supprime jamais de rapport et ne modifie pas les champs des fiches. Un doublon se supprime à la main sur le site, en cliquant sur la croix du rapport.

## Fonds sans document (non inclus)

Voir `factsheets/factsheets_gamme_one_life.xlsx`, onglet 2 : 23 introuvables, 23 fonds internes d'assurance (XFCS), 9 non vérifiés et 4 venant uniquement d'une source tierce.
