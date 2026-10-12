# 2026-10-12 — Upload des factsheets sur invest-law.eu

- **Objectif** : chaque fonds doit avoir sur invest-law.eu la factsheet la plus récente trouvée (dossier `INVESTLAW/`, script `tools/investlaw_upload.py`, procédure `INVESTLAW/LISEZMOI.md`).
- **Résultat** : 250 factsheets uploadées sans erreur (1 test, puis 249). 162 fonds avaient déjà le rapport du même mois et 7 un rapport plus récent : rien n'a été envoyé pour eux. Les 3 lignes « À contrôler » ont été incluses, à la demande de l'utilisateur.
- **Décision** : sur le site, `report_date` est la date d'upload, pas le mois du rapport. Les doublons se repèrent donc au mois lu dans le nom du rapport (sans accents ni majuscules, DIC ignorés). Avant cette correction, le plan comptait 129 fonds à uploader au lieu de 250.
- **Reste à faire** :
  - Doublon créé par le test sur la fiche 206 (LU0231459107, Aberdeen Asian Smaller Companies) : supprimer à la main « Rapport de Gestion Août 2026 » (`LU0231459107__Factsheet_EN_2026-08-31.pdf`) avec la croix. Le script ne supprime rien.
  - ACATIS VALUE EVENT (DE000A0X7541), `A_VERIFIER` : le site a un « rapport de gestion » sans mois, déposé le 28/09/2026. C'est peut-être la même factsheet d'août.
  - 2 fonds `FONDS_ABSENT` sur le site (voir le manifeste).
- **Fichiers** : `tools/investlaw_upload.py`, `INVESTLAW/LISEZMOI.md`, `INVESTLAW/MANIFEST_UPLOAD.xlsx` (plan et statut par ligne), `.gitignore`.
