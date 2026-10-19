# 2026-10-19 — Connexion de Claude à la boîte Zimbra

- **Objectif** : permettre à Claude de lire les mails Zimbra d'invest-law pour mettre le site à jour, pour Louis et Noa.
- **Décision** : accès en lecture seule par l API REST Zimbra en HTTPS (IMAP port 993 bloqué par le proxy cloud) ; serveur OVH `zimbra1.mail.ovh.net` ; identifiants dans les variables d environnement de chaque personne (`ZIMBRA_USER`, `ZIMBRA_PASSWORD`), jamais dans le dépôt ni le chat. Le serveur Zimbra doit être ajouté aux domaines autorisés de l'environnement.
- **Fichiers** : `tools/zimbra_mail.py` (test / list / get), `docs/2026-10-19-guide-zimbra.md` (guide pas à pas), ligne ajoutée dans `.claude/skills/invest-law/SKILL.md`.
- **Reste à faire** : chaque personne fait le réglage (guide), puis « teste la connexion Zimbra » dans une nouvelle session. Testé OK le 19/10 pour Louis ; reste Noa.
- **Test** : connexion OK depuis la session de Louis (57 messages dans INBOX). L'outil accepte une URL complète dans `ZIMBRA_IMAP_HOST` / `ZIMBRA_HOST`.
- **Test 2** (19/10, autre session) : connexion OK, 58 messages dans INBOX.
- **Rôle de la boîte** (précisé le 19/10) : c'est la boîte « data » d'invest-law, où arrivent la plupart des données, notamment les VNI quotidiennes et mensuelles. Ajouté au guide et au skill.
- **Contrôle VNI Zimbra vs site** (19/10) : aucune valeur fausse, mais 159 VNI des mails manquent sur le site (Leleux depuis le 08/10, DNCA depuis juin ou jamais) ; décalage d'un jour probable dans l'historique. Rapport : `docs/2026-10-19-controle-vni-zimbra.md` ; CSV prêt (non importé) : `docs/controle-vni-2026-10-19/vni-manquantes.csv`.
