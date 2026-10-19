# Connecter Claude à la boîte mail Zimbra d'invest-law

But : Claude lit les mails Zimbra (VNI, factsheets, nouvelles des maisons de gestion) et les reporte sur invest-law.eu.
Claude ne voit pas les onglets du navigateur : il se connecte à Zimbra par IMAP, avec des identifiants rangés dans les réglages de l'environnement cloud.

**Chaque personne (Louis, Noa, …) fait ce réglage une fois dans son propre environnement.** Les identifiants ne sont jamais écrits dans le dépôt ni collés dans le chat.

## Étapes (5 minutes, une fois par personne)

1. **Trouver le nom du serveur.** Dans l'onglet Zimbra, regarder l'adresse : `https://mail.exemple.eu/...` → le serveur est `mail.exemple.eu`.
2. **Ouvrir les réglages.** Dans Claude Code (app ou claude.ai/code), cliquer sur le nom de l'environnement dans la barre de titre de la session, puis **Edit**.
3. **Ajouter 3 variables** (là où se trouvent déjà `INVESTLAW_EMAIL` et `INVESTLAW_PASSWORD`) :
   ```
   ZIMBRA_IMAP_HOST=mail.exemple.eu
   ZIMBRA_USER=adresse@invest-law.eu
   ZIMBRA_PASSWORD=le mot de passe Zimbra
   ```
4. **Autoriser le serveur.** Même écran, section **Network access** : ajouter `mail.exemple.eu` aux domaines autorisés (laisser cochée la case des gestionnaires de paquets). Doc : https://code.claude.com/docs/en/cloud-environments#network-access
5. **Enregistrer et ouvrir une nouvelle session** (les sessions déjà ouvertes ne voient pas les nouvelles variables).
6. Dans la nouvelle session, écrire : « teste la connexion Zimbra ». Claude lance `python3 tools/zimbra_mail.py test`.

## Utilisation

Demander par exemple : « lis les mails Zimbra de Leleux reçus depuis lundi et mets les VNI à jour sur le site ».

Commandes (lecture seule, rien n'est marqué comme lu, supprimé ou envoyé) :

```
python3 tools/zimbra_mail.py list 20 --from leleux --since 15-Oct-2026
python3 tools/zimbra_mail.py get <uid> --save /tmp/pj      # texte + pièces jointes (PDF factsheets)
```

## En cas de problème

- `KeyError: 'ZIMBRA_...'` : variable absente ou session ouverte avant l'ajout → nouvelle session.
- Erreur réseau / 403 : le serveur n'est pas dans les domaines autorisés (étape 4).
- `AUTHENTICATIONFAILED` : identifiant ou mot de passe faux, ou IMAP désactivé sur le compte (à activer chez l'hébergeur Zimbra).
