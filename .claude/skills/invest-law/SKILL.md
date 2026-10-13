---
name: invest-law
description: Toute tâche sur le site invest-law.eu (fiches fonds, rapports de gestion/factsheets, VNI, commentaires analystes, maisons de gestion, banques dépositaires, nouvelles, documentation, benchmarks) — via l'API JSON du site depuis une session cloud.
---

# invest-law.eu

1. Lire `docs/2026-10-12-guide-invest-law.md`, qui contient la carte complète des pages, des rôles et de l'API, avec les recettes.
2. Connexion : `python3 tools/investlaw_upload.py login`, lire le **dernier** code envoyé par `info@invest-law.eu` via Gmail, puis `python3 tools/investlaw_upload.py verify <code>`. En cas de 401, recommencer.
3. Outils :
   - `tools/investlaw.py` : `fund`, `set` (simulation par défaut, `--apply` pour enregistrer), `delete-report`, `call METHODE chemin [corps.json]` ;
   - `tools/investlaw_upload.py` : upload en masse des factsheets, procédure dans `INVESTLAW/LISEZMOI.md`.
4. Règles :
   - montrer ancien → nouveau avant toute modification de fiche ;
   - `PUT /api/funds/{id}` remplace toute la fiche : passer par `set` ;
   - le mois couvert par un rapport se lit dans son nom, pas dans `report_date` ;
   - ne jamais supprimer le travail d'autres personnes sans accord.
