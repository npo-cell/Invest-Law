# Contrôle des VNI reçues sur Zimbra vs invest-law.eu (19/10/2026)

Source : les 58 mails de la boîte Zimbra « data » (reçus du 05/10 au 19/10/2026), avec 3 652 VNI pour 231 ISIN, dates de VNI du 06/10 au 15/10.
- **CACEIS (OLIS)** : rapports Excel « Fund Prices Providers » pour les fonds Leleux Invest. Ils arrivent plusieurs jours après la date de VNI : le rapport du 19/10 donne la VNI du 14/10.
- **DNCA Finance** : CSV quotidiens (`cotation_mailing_dnca_sicav/fcp_*.csv`), avec toute la gamme DNCA.
- Les deux autres mails ne contiennent pas de VNI : une newsletter Probus Pleion transférée et un test d'adresse.

Seuls 23 de ces ISIN ont une fiche sur le site. Le contrôle porte sur ces 23 fiches.

## Résultat

**Aucune valeur fausse.** Les 8 VNI présentes à la fois dans les mails et sur le site sont identiques (Leleux, 07/10). Les mails en double donnent les mêmes valeurs.

**Mais la plupart des VNI des mails ne sont pas sur le site.** Il manque 159 valeurs ; elles ont été importées le 19/10 (159/159 vérifiées) depuis `docs/controle-vni-2026-10-19/vni-manquantes.csv`, au format `ISIN,Date,VNI`.

### Leleux Invest (CACEIS) : 8 fiches, à jour jusqu'au 07/10
Il manque les VNI des 08, 09, 12, 13 et 14/10, soit 40 valeurs.
Fiches : 117 Equities World FOF R, 530 Equities World FOF P, 531 Patrimonial World FOF P, 118 Patrimonial World FOF PA, 539 Responsible World FOF P, 119 Responsible World FOF PA, 536 Dynamic World FOF P, 116 Dynamic World FOF PA.

Quatre parts reçues de CACEIS n'ont pas de fiche sur le site : BE6269807184 (Patrimonial DIS), BE6286029416 (Patrimonial R CAP), BE6304593781 (Responsible RC) et BE6370436584 (Dynamic R). C'est peut-être voulu.

### DNCA : 15 fiches, très en retard
- **Dernière VNI le 07/06/2026** : 44 Alpha Bonds A, 89 Beyond Alterosa A, 91 Beyond Semperosa A, 92 Credit Conviction A, 5 Eurose A, 90 Sustain Climate A, 71 Value Europe A.
- **Dernière VNI le 01/03/2026** : 8 Évolutif A.
- **Aucune VNI** : 93 Europe Growth IG, 464 Global New World A3, 465 Norden Europe A, 466 Sérénité Plus B, 94 SRI Europe Growth A, 467 Strategic Resources A, 468 Value Europe IG.

Les mails fournissent les VNI du 06 au 15/10 (119 valeurs). Le trou entre juin et début octobre ne peut pas être comblé depuis Zimbra : la boîte ne reçoit des mails que depuis le 05/10.

### Anomalie probable : historique décalé d'un jour (à vérifier)
Sur le site, plusieurs historiques n'ont aucune VNI le vendredi mais en ont le dimanche. C'est le signe de dates enregistrées un jour trop tôt (VNI du lundi au vendredi stockées du dimanche au jeudi).
- DNCA 44, 89, 91, 92, 5, 90, 71 : décalés depuis mars 2026 environ. Le fonds 8 (Évolutif) a des VNI du samedi au mercredi, soit peut-être un décalage de 2 jours.
- Leleux 117 : décalé jusqu'en mai 2026, correct depuis juin.

Ce constat n'a pas été vérifié valeur par valeur : les mails ne couvrent qu'octobre. Pour confirmer, il faut comparer une VNI de juin avec une source DNCA. **Avant un import en masse, importer une seule ligne et relire la date enregistrée**, pour s'assurer que l'import ne décale pas les dates.

## Refaire le contrôle
Scripts dans `docs/controle-vni-2026-10-19/` : télécharger les mails avec `tools/zimbra_mail.py get <id> --save <dossier>/zmail/<id>` (`pip install xlrd` pour les .XLS), puis lancer `parse.py <dossier>`, `fetch.py <dossier>` (après connexion au site) et `compare.py <dossier>`.
