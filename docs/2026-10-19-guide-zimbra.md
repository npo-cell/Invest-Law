# Connecter Claude à la boîte mail Zimbra d'invest-law

But : Claude lit les mails Zimbra (VNI, factsheets, nouvelles des maisons de gestion) et les reporte sur invest-law.eu.
Claude ne voit pas les onglets du navigateur : il se connecte à Zimbra (OVH, `zimbra1.mail.ovh.net`) par son adresse web, avec des identifiants rangés dans les réglages de l'environnement cloud.
L'IMAP ne marche pas : le proxy des sessions cloud ne laisse passer que HTTPS.

**Chaque personne (Louis, Noa, …) fait ce réglage une fois dans son propre environnement.** Les identifiants ne sont jamais écrits dans le dépôt ni collés dans le chat.

## Étapes (5 minutes, une fois par personne)

1. **Ouvrir les réglages.** Dans Claude Code (app ou claude.ai/code), cliquer sur le nom de l'environnement dans la barre de titre de la session, puis **Edit**.
2. **Autoriser le serveur.** Section **Network access**, niveau *Limited* (ou *Custom*), champ **Allowed domains** : écrire seulement
   ```
   zimbra1.mail.ovh.net
   ```
   sans `https://`, sans `/modern/email/Inbox`. Laisser cochée la case des gestionnaires de paquets.
3. **Ajouter 2 variables** (là où se trouvent déjà `INVESTLAW_EMAIL` et `INVESTLAW_PASSWORD`) :
   ```
   ZIMBRA_USER=adresse@invest-law.eu
   ZIMBRA_PASSWORD=le mot de passe Zimbra
   ```
4. **Enregistrer et ouvrir une nouvelle session** (les sessions déjà ouvertes ne voient pas les nouveaux réglages).
5. Dans la nouvelle session, écrire : « teste la connexion Zimbra ». Claude lance `python3 tools/zimbra_mail.py test`.

## Utilisation

Demander par exemple : « lis les mails Zimbra de Leleux reçus depuis lundi et mets les VNI à jour sur le site ».

Commandes (lecture seule, rien n'est marqué comme lu, supprimé ou envoyé) :

```
python3 tools/zimbra_mail.py list 20 --query "from:leleux after:10/15/2026"
python3 tools/zimbra_mail.py get <id> --save /tmp/pj      # texte + pièces jointes (PDF factsheets)
```

## En cas de problème

- `KeyError: 'ZIMBRA_...'` : variable absente ou session ouverte avant l'ajout → nouvelle session.
- `403` / erreur de connexion : `zimbra1.mail.ovh.net` pas dans **Allowed domains** (étape 2), ou session ouverte avant.
- `401` : identifiant ou mot de passe faux.
