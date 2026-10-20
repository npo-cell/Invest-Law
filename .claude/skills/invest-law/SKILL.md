---
name: invest-law
description: Toute tâche sur le site invest-law.eu (fiches fonds, rapports de gestion/factsheets, VNI, commentaires analystes, maisons de gestion, banques dépositaires, nouvelles, documentation, benchmarks) — via l'API JSON du site depuis une session cloud.
---

# invest-law.eu

1. Lire `docs/2026-10-12-guide-invest-law.md`, qui contient la carte complète des pages, des rôles et de l'API, avec les recettes.
2. Connexion : `python3 tools/investlaw_upload.py login`, lire le **dernier** code envoyé par `info@invest-law.eu` via Gmail, puis `python3 tools/investlaw_upload.py verify <code>`. En cas de 401, recommencer. **Une fois connecté (verify OK), mettre à la corbeille le mail du code utilisé** (Gmail `trash_thread`) : consigne de l'utilisatrice, le code ne sert plus.
3. Outils :
   - `tools/investlaw.py` : `fund`, `set` (simulation par défaut, `--apply` pour enregistrer), `delete-report`, `call METHODE chemin [corps.json]` ;
   - `tools/investlaw_upload.py` : upload en masse des factsheets, procédure dans `INVESTLAW/LISEZMOI.md`.
   - `tools/controle_vni.py` : contrôle des VNI de tout le site (avec/sans VNI, cohérence avec la date de création, anomalies) ; **avant tout travail sur les VNI, lire `docs/controle-vni/README.md`** (état des lieux, anomalies connues, tableau de bord) ;
   - `tools/zimbra_mail.py` : lecture seule de la boîte Zimbra, boîte « data » d'invest-law où arrivent la plupart des données (VNI quotidiennes et mensuelles, mails des maisons de gestion ; routine quotidienne de synchronisation des VNI : `docs/zimbra-vni/CONSIGNE.md`, VNI, factsheets en pièce jointe) ; réglage par personne dans `docs/2026-10-19-guide-zimbra.md`.
4. Règles :
   - montrer ancien → nouveau avant toute modification de fiche ;
   - `PUT /api/funds/{id}` remplace toute la fiche : passer par `set` ;
   - le mois couvert par un rapport se lit dans son nom, pas dans `report_date` ;
   - ne jamais supprimer le travail d'autres personnes sans accord.
   - priorité absolue à l'exactitude : pas de document original et conforme, ou valeur douteuse → on ne met rien sur le site (mieux vaut incomplet que faux).
   - valeur ambiguë (ex. indice cité seulement « à titre de comparaison », pour la gestion du risque, dans la partie ESG, ou document contradictoire) → ne pas la mettre, ou demander à l'utilisatrice avant (consigne du 13/10/2026).
