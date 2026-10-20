# 2026-10-20 — La veille « Nouvelles » relève aussi la boîte Zimbra

- **Demande** (Noa) : la routine quotidienne « Veille nouvelles invest-law » relève désormais deux boîtes, Gmail (npo@lifeb2b.com) et Zimbra « data » (data@invest-law.eu), et trie les mails utiles pour écrire des nouvelles.
- **Routine** (`trig_01Aivzt515Ne1Ak6DCMTHrjG`, tous les jours 7h59 Paris, environnement « Invest-Law V » qui contient `ZIMBRA_USER` / `ZIMBRA_PASSWORD`) : invite mise à jour (deux boîtes, VNI Zimbra laissées à la routine « VNI Zimbra », doublons entre boîtes, une boîte en panne n'arrête pas l'autre).
- **Consigne** `docs/nouvelles/CONSIGNE.md` : étape 2 bis Zimbra, identifiants `z-<id>` dans `etat.json` / `articles/`, règle des doublons, note de session par boîte.
- **Outil** `tools/zimbra_mail.py get` : affiche le texte des mails HTML sans partie texte (newsletters).
- **Test** : connexion Zimbra OK depuis l'environnement (71 messages) ; lecture d'une newsletter transférée (CMF Hebdo) OK. Premier passage réel : demain 21/10 à 7h59.
