# Consigne : reprise des fiches à corriger (19/10/2026)

Demande de l'utilisatrice, après l'authentification du 17/10 (`docs/authentification-2026-10-17/`) : corriger tout ce qu'il faut pour que le classeur « Gamme One Life complète » soit le plus véridique possible. 417 fonds sont repris :
- les fiches du site avec des valeurs qui contredisent les documents ou qui n'y figurent pas ;
- les fiches dont la factsheet est celle d'une autre part, ou dont le seul document est un KID ;
- les fiches, du site ou préparées, pour lesquelles une factsheet plus récente existe.

**Rien n'est modifié sur invest-law.eu à ce stade.**

## Principe
Chaque fiche est refaite **à partir des documents les plus récents de la part exacte**, selon `docs/wealth-belgium-2026-10-15/CONSIGNE-fiches.md` : mêmes champs, mêmes règles, mêmes précisions. Seules sources admises : la factsheet la plus récente et le KID le plus récent. Ce qui n'est pas écrit dans ces documents reste vide. On ne garde jamais une valeur du site qu'on ne retrouve pas dans les documents.

## Documents
Chaque entrée du lot donne :
- `documents_recents` : la factsheet et le KID les plus récents trouvés sur fundinfo, déjà rangés dans `INVESTLAW/`. Le champ `isin_verifie` est faux quand l'ISIN n'a pas été retrouvé dans le texte : à vérifier sur l'image de la page ;
- `autres_pdf_du_depot` et `pdf_du_site` : les documents déjà connus.

Règles :
- Prendre la factsheet la plus récente **de la part exacte** : français d'abord, sinon anglais, jamais une autre langue. Une factsheet multi-parts est admise si elle donne explicitement les chiffres de notre part.
  - **Consigne de l'utilisatrice du 27/10/2026** (remplace la règle « français d'abord, même plus ancien ») : on prend la factsheet **la plus récente** ; si cette version récente n'existe pas en français, l'anglais est accepté. À date égale, le français reste prioritaire.
- Si `documents_recents` ne contient pas de factsheet conforme, chercher sur le site du gestionnaire. Ranger tout nouveau PDF dans `INVESTLAW/<MAISON>/<ISIN>/<ISIN>__Factsheet_<FR|EN>_<date>.pdf`, ou `__KID_…`, avec son `.txt` (`pdftotext -layout`).
- Ne jamais utiliser le document d'une autre part. S'il n'existe rien pour la part, laisser les champs propres à la part vides et l'expliquer dans `remarques`. Les champs propres à la part sont : frais, date de création, devise, SRI, encours de la part.

## Aide
- `ecarts_constates` liste ce que l'authentification a relevé ; `valeurs_actuelles` donne ce qui est dans le classeur. Ce sont des pistes, pas des sources.
- Encours : celui du fonds s'il est donné, sinon celui de la part, en le précisant en remarque. La date de l'encours est celle de la factsheet.
- `categorie` : laisser vide. Elle est remplie ensuite depuis le fichier One Life.

## Sortie
- Une fiche `docs/correction-2026-10-19/fiches/<ISIN>.json` par fonds. Elle a les clés de `docs/wealth-belgium-2026-10-15/fiches/IE00BKSBGS44.json`, plus `factsheet_fichier` et `kid_fichier` (chemins relatifs à la racine du dépôt, vides si aucun). Les champs `n`, `nom` et `maison` viennent de l'entrée.
- Dans `remarques`, une phrase dit ce qui a changé par rapport au classeur : « Corrigé : encours 664508 → 529223 (factsheet 30/09/2026) ; … ».
- Contrôle obligatoire après chaque fiche : `python3 -I docs/correction-2026-10-19/verif_fiche.py <ISIN>`, jusqu'à 0 manquant. Un écart restant qui vient d'un artefact d'extraction est expliqué en remarque.
- Pas de commit, pas de push, rien sur invest-law.eu.
