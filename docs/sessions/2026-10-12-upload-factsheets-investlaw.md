# 2026-10-12 — Upload des factsheets sur invest-law.eu

- **Objectif** : chaque fonds doit avoir sur invest-law.eu la factsheet la plus récente trouvée (dossier `INVESTLAW/`, script `tools/investlaw_upload.py`, procédure `INVESTLAW/LISEZMOI.md`).
- **Résultat** : 250 factsheets uploadées sans erreur (1 test, puis 249). 162 fonds avaient déjà le rapport du même mois et 7 un rapport plus récent : rien n'a été envoyé pour eux. Les 3 lignes « À contrôler » ont été incluses, à la demande de l'utilisateur.
- **Décision** : sur le site, `report_date` est la date d'upload, pas le mois du rapport. Les doublons se repèrent donc au mois lu dans le nom du rapport (sans accents ni majuscules, DIC ignorés). Avant cette correction, le plan comptait 129 fonds à uploader au lieu de 250.
- **Reste à faire** :
  - ACATIS VALUE EVENT (DE000A0X7541), `A_VERIFIER` : le site a un « rapport de gestion » sans mois, déposé le 28/09/2026. C'est peut-être la même factsheet d'août.
  - 2 fonds `FONDS_ABSENT` sur le site (voir le manifeste).
- **Fichiers** : `tools/investlaw_upload.py`, `INVESTLAW/LISEZMOI.md`, `INVESTLAW/MANIFEST_UPLOAD.xlsx` (plan et statut par ligne), `.gitignore`.

## Suite : apprentissage complet du site
- Le site a été cartographié (15 pages, environ 75 appels d'API, rôles) dans `docs/2026-10-12-guide-invest-law.md`. Une compétence `.claude/skills/invest-law/SKILL.md` est ajoutée au dépôt, et un outil `tools/investlaw.py` (fund / set / delete-report / call).
- Le doublon créé par le test sur la fiche 206 a été supprimé (`DELETE /api/funds/206/reports`). Le rapport d'origine est conservé.
- 7 doublons ODDO BHF (fiches 129 à 134 et 137) : à la demande de l'utilisateur, les versions du 14/09 ont été supprimées ; la version « Factsheet_ODDO_BHF… » du 05/10 est conservée.
- `set --apply` (PUT d'une fiche) n'a pas encore été testé sur une vraie fiche : le test a été refusé par le contrôle de sécurité automatique.

## Harmonisation des rapports sans mois
- 82 rapports sans mois : le mois a été lu dans chaque PDF, puis chaque rapport a été redéposé avec « Rapport de gestion <Mois> <Année> » et la date de la factsheet, et l'ancien supprimé (`tools/investlaw.py rename-report`). 4 étaient des DIC, renommés « DIC (Document d'informations clés) ». Détail dans `docs/2026-10-12-harmonisation-rapports-sans-mois.md`.
- ACATIS (DE000A0X7541) : le rapport sans mois était un DIC. La factsheet d'août 2026 a été uploadée. La fiche a maintenant 2 DIC (`DIC_ACATIS…` du 30/09 et l'ancien `t_l_chargement`, renommé).
- Le classifieur du mode Auto de Claude Code bloque les écritures groupées en production tant que l'utilisateur ne les a pas confirmées explicitement dans le chat.
- Bug corrigé dans `plan` : seuls les noms contenant « rapport » étaient comptés, si bien qu'une « Fiche mensuelle Août 2026 » n'était pas vue. Cela a causé un doublon sur la fiche 91 (LU1907595398, notre upload `LU1907595398__Factsheet_FR_2026-08-31.pdf`), à supprimer après confirmation. Doublon de la fiche 91 supprimé après confirmation (la « Fiche mensuelle Août 2026 » est conservée).
- Doublons d'août antérieurs, à arbitrer : fiche 92 (LU0284393930) et fiche 468 (LU1515062674), qui ont chacune un « Rapport de gestion Août 2026 » et une « Fiche mensuelle Août 2026 ». 10 rapports s'appellent « Fiche mensuelle … » et 1 « Fiche produit … ».
