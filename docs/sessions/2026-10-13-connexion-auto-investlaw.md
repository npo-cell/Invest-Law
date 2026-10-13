# 2026-10-13 — Connexion automatique à invest-law.eu

- Objectif : connexion au site sans intervention (code 2FA lu dans Gmail).
- Réglages faits par l'utilisateur dans l'environnement : `invest-law.eu` et `www.invest-law.eu` en domaines autorisés, secrets `INVESTLAW_EMAIL` / `INVESTLAW_PASSWORD`, connecteur Gmail.
- Connexion testée : `login` → code lu dans Gmail → `verify` → `OK role=Data`.
- Décision : après chaque `verify` réussi, le fil Gmail du code est mis à la corbeille.
- Règle déjà ajoutée par un collègue dans le skill et le guide ; seule cette note de session est ajoutée.
