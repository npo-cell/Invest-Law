# 2026-10-12 — Upload des factsheets sur invest-law.eu (en cours)

- **Objectif** : uploader les factsheets de `INVESTLAW/` avec `tools/investlaw_upload.py`, en suivant `INVESTLAW/LISEZMOI.md`.
- **Fait** : branche `claude/adoring-planck-eamiy1` fusionnée ; connexion OK. `plan` donne 129 `A_UPLOADER`, 291 `DEJA_PRESENT` et 2 `FONDS_ABSENT`. Premier upload test : LU0231459107 (FundId 206), « Rapport de Gestion Août 2026 ».
- **Problème** : ce premier upload fait doublon avec « Rapport de gestion Aout 2026 » (sans accent), déjà en ligne. `plan` compare le nom exact et le mois de `report_date`. Or `report_date` correspond à la date d'upload sur le site, pas au mois du rapport.
- **À décider** : supprimer le doublon à la main sur le site ; corriger la détection (mois/année lus dans le nom du rapport, comparaison sans accents ni casse, en ignorant les DIC) avant de lancer le reste.
- **Fichiers** : `INVESTLAW/MANIFEST_UPLOAD.xlsx` (colonnes du plan et statut).
