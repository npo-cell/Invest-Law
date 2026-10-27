# 2026-10-27 — Gamme One Life : les 7 « factsheets plus récentes »

- **Demande** : la page d'authentification signalait 7 fonds avec une factsheet plus récente sur fundinfo ; les récupérer et mettre à jour le Google Sheet et la page.
- **Nouvelle consigne de l'utilisatrice** : factsheet la plus récente ; anglais accepté si la version récente n'existe pas en français (français prioritaire à date égale). Écrite dans `docs/correction-2026-10-19/CONSIGNE.md`. Recherche sur les sites des gestionnaires (l'API fundinfo n'a pas été utilisée : accès refusé par la session).
- **Mis à jour (3)** — fiches `docs/correction-2026-10-19/fiches/`, origine « Mise à jour le 27/10 » :
  - abrdn Liquidity Sterling X-2 GBP (LU1914336968) : factsheet EN 31/08 (au lieu de FR 30/06) ; encours 13 700 M GBP ajouté, gérant « Liquidity Team » retiré (absent de la factsheet EN), politique et disclaimer en anglais, 28 lignes d'allocation.
  - Allianz China A-Shares AT USD (LU1997245177) : factsheet EN 30/09 (au lieu de FR 31/08) ; encours 2 930,80 M USD, investissements durables 47,40 %, politique et disclaimer en anglais, 26 lignes.
  - PTAM Defensiv Portfolio P (LU0260464168) : nouvelle factsheet FR **quotidienne** du 26/10 trouvée sur ptam.de (rangée dans `INVESTLAW/`) ; encours 40,66 M EUR, 28 lignes. Un KID plus récent existe seulement en allemand (16/04/2026), non utilisé.
  - Sites abrdn et Allianz : documents chargés dynamiquement, rien de plus récent téléchargeable.
- **Inchangés (4 parts M&G)** LU3149167275, LU3149167358, LU2813324576, LU2509757758 : M&G ne publie de factsheet que pour d'autres parts (S-H, W) ; pages fonds sans document. Remarque « Vérifié le 27/10/2026 » ajoutée.
- **Google Sheet** « Gamme One Life complète » (même lien) : lignes Fiches 20, 357, 781 réécrites, remarques des 4 M&G, Allocations des 3 fonds remplacées (PTAM 29 → 28 lignes), 1 ligne Documents ajoutée (PTAM FR 26/10), Lisez-moi daté du 27/10. CSV `docs/gamme-complete-2026-10-16/sheet/` mis à jour à l'identique (seules ces lignes changent).
- **Authentification** : `authentifier.py` relancé, les 3 fiches sont entièrement conformes (Allianz : compartiment et SRI repris de la relecture, KID illisible par pdftotext) ; plus aucun fonds signalé « factsheet plus récente ». Page republiée au même lien : https://claude.ai/artifact/7GsXisc2YK4wPHHni72WLx
- Rien modifié sur invest-law.eu.
- À décider : PTAM sur factsheet quotidienne (la mensuelle FR reste celle du 30/09).
