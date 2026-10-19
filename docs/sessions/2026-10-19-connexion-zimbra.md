# 2026-10-19 — Connexion de Claude à la boîte Zimbra

- **Objectif** : permettre à Claude de lire les mails Zimbra d'invest-law pour mettre le site à jour, pour Louis et Noa.
- **Décision** : accès en lecture seule par l API REST Zimbra en HTTPS (IMAP port 993 bloqué par le proxy cloud) ; serveur OVH `zimbra1.mail.ovh.net` ; identifiants dans les variables d environnement de chaque personne (`ZIMBRA_USER`, `ZIMBRA_PASSWORD`), jamais dans le dépôt ni le chat. Le serveur Zimbra doit être ajouté aux domaines autorisés de l'environnement.
- **Fichiers** : `tools/zimbra_mail.py` (test / list / get), `docs/2026-10-19-guide-zimbra.md` (guide pas à pas), ligne ajoutée dans `.claude/skills/invest-law/SKILL.md`.
- **Reste à faire** : chaque personne fait le réglage (guide), puis « teste la connexion Zimbra » dans une nouvelle session. Pas encore testé contre le vrai serveur.
