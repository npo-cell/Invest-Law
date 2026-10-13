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

## Audit des fiches vs dernière factsheet (lecture seule)
- Contrôle ISIN de tous les fichiers en ligne (730) : `docs/2026-10-12-controle-isin-fichiers.md`. Aucun fichier d'un autre fonds. ISIN de la fiche 387 corrigé en FR0007001581 à la demande de l'utilisateur.
- Audit de 439 fiches (8 agents en parallèle, lecture des PDF) : 1 481 écarts (180 ERREUR, 574 MAJ, 727 MANQUANT), 133 fiches sans écart, 74 fiches quasi vides (devise « E »). Rien n'a été modifié sur le site.
- Livrables : `docs/2026-10-12-audit-fiches-investlaw.xlsx` (onglets Synthèse, Écarts, Par fonds, Fiches à compléter, Contrôle ISIN) et la page de synthèse `docs/2026-10-12-audit-fiches-investlaw.html`, publiée en artefact : https://claude.ai/artifact/GfTSsC7oUyEeoruciDXX3J
- Limites : SRI rarement lisible (image), certaines répartitions seulement en graphique, encours fonds vs part ; chaque correction sera montrée avant application.

## Corrections des fiches (appliquées le 12/10/2026 après confirmation explicite de l'utilisateur)
- Plan : `docs/corrections-2026-10-12/` (un JSON par fiche dans `plan/`, simulation dans `simulation-corrections.xlsx`, journal `application.log`, contrôle `verification.json`).
- Résultat : 263 fiches sur 266 enregistrées. 1 202 champs vérifiés conformes après relecture (valeurs comparées sans tenir compte du format ni de l'ordre des lignes).
- Refusées par le site (409 « Ce code ISIN est déjà enregistré », rien n'a été modifié) : 245 BL-Global 30 (LU0048292394), 246 BL-Global 50 (LU0048292808), 519 Gavekal China Fixed Income (IE00BYRGXY37). Aucune autre fiche visible n'a cet ISIN : le doublon est probablement un fonds masqué ou supprimé, à voir avec un administrateur du site.
- Non faits : 64 benchmarks absents du référentiel (`Benchmarks à créer`), 242 valeurs incertaines (`Non corrigés`), 28 listes au total incohérent, ISIN de la fiche 165.
- Le site a remis « Mise à jour » au 12/10/2026 sur les fiches corrigées.

## Partage avec l'équipe (13/10/2026)
- Constat : la branche par défaut du dépôt est `claude/kind-edison-2o3dsu` ; tout le travail était sur `claude/lucid-edison-kjhbfm`, donc invisible pour les collègues.
- Demande de fusion mise à jour : https://github.com/npo-cell/Invest-Law/pull/1 (inclut aussi le contenu de la demande n°2, factsheets One Life).
- Règle ajoutée dans `AGENTS.md` : en fin de tâche, fusionner vers la branche par défaut ; en début de tâche, consulter les demandes de fusion ouvertes.

## Consigne (13/10/2026)
- Après chaque connexion à invest-law.eu, mettre à la corbeille le mail du code de vérification utilisé. Ajouté à la compétence `invest-law` et au guide.

## 13/10/2026 — Fonds sans factsheet, règles de l'équipe
- Noa confirme la fusion automatique vers la branche par défaut (règle de `AGENTS.md`), demande n°3 fusionnée.
- Règles notées dans le guide et la compétence : fonds internes/mandats exclus des manques ; 4 contrôles de recherche ; « mieux vaut incomplet que faux » ; mail du code de connexion mis à la corbeille après usage.
- Recherche sur 30 fonds externes : 9 factsheets trouvées et rangées dans `INVESTLAW/` (FFG ×7, Candriam Robotic, IVO IG 2030), 2 à valider (Alken : factsheet multi-parts ; Waterloo : marquée « Internal use only »), 3 non conformes (factsheet d'une autre classe : Leleux P, SPM Y), 16 introuvables. Détail : `docs/2026-10-13-recherche-factsheets-manquantes.md`. Rien n'a été mis en ligne.
- Page d'audit mise à jour (section « Fonds sans factsheet ») : https://claude.ai/artifact/GfTSsC7oUyEeoruciDXX3J
- Upload des 9 factsheets trouvées (FundId 199-205, 250, 278) à la demande de Noa : toutes en ligne, PDF vérifiés. Alken (65) et Waterloo (446) laissés de côté sur décision de Noa. Remplissage des champs de ces fiches : pas encore fait.
