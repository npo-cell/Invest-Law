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

## Procédure (session Claude sur le Mac, avec Claude in Chrome)

1. Copier ce dossier `INVESTLAW` sur le Mac et le connecter à la session.
2. Coller la consigne suivante :

> Utilise le skill investlaw-rapport-gestion pour uploader, pour chaque ligne de INVESTLAW/MANIFEST_UPLOAD.xlsx, le PDF dans « Rapports de Gestion » de la fiche du fonds sur invest-law.eu.
> - Upload seulement, ne modifie pas les champs de la fiche.
> - Avant chaque upload, contrôle que l'ISIN de la fiche est celui du fichier.
> - Contrôle aussi qu'aucun rapport n'existe déjà avec la même date ou le même mois. Dans ce cas, n'uploade pas, note « déjà présent » dans la colonne Statut upload et ne supprime rien.
> - Si le fonds n'existe pas sur le site, note « fonds absent ».
> - Pour les lignes avec « À contrôler » renseigné, demande-moi avant d'uploader.
> - Utilise exactement le nom et la date du manifeste.
> - Mets à jour la colonne Statut upload après chaque fonds.

## Fonds sans document (non inclus)

Voir `factsheets/factsheets_gamme_one_life.xlsx`, onglet 2 : 23 introuvables, 23 fonds internes d'assurance (XFCS), 9 non vérifiés et 4 venant uniquement d'une source tierce.
