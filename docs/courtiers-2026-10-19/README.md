# Courtiers Bruxelles-Wallonie et compagnies partenaires (19/10/2026)

Résultat : Google Sheet « Courtiers Bruxelles-Wallonie – compagnies partenaires (prospection One Life) » dans le Drive personnel de npo (retiré du Drive partagé Invest-Law le 19/10, à sa demande ; accès privé) :
https://docs.google.com/spreadsheets/d/1Tddg0OVJRDBajif7ynzEt-03wPeaieAnx2e4oUuHN7A/edit

Les données (noms, contacts) ne sont **pas** versionnées ici : le dépôt est public.

## Méthode
1. `fsma_crawl.py <dossier>` : registre FSMA (data portal), intermédiaires actifs, secteur « intermédiaires d'assurances », activité IDD ILP (assurance-vie avec composante d'investissement) → 6 900 inscrits, dont 4 153 « courtiers d'assurances belges » ; export JSON de chaque fiche (adresse, BCE, n° FSMA, statuts).
2. Annuaires publics « trouver un courtier » des compagnies :
   - AG Insurance : `https://iservices.aginsurance.be/Services/BrokerInfo/api/v2/brokers/list?optInApplicationCode=AGWBST&optInCode=BROSCH` (avec BCE) ;
   - AXA : `https://www.fo.axa.be/dltaws/POSList/100.json?v=axa_prod` (avec BCE) ;
   - NN : API de brokerfinder.nn.be (iframe de nn.be/fr/courtiers) ;
   - Patronale Life : marqueurs de la carte sur patronale.be/fr/courtiers ;
   - Baloise et Allianz : `loc_collect.py` (requêtes par code postal, 651 CP de Bruxelles + Wallonie ; 50 / 20 courtiers les plus proches par requête).
   Seuls les champs publics affichés (nom, adresse, tél., email, site, BCE) sont utilisés. Les segmentations commerciales internes présentes dans certains flux (AXA, Allianz) sont volontairement ignorées.
3. `fusion.py <scratchpad> <sortie.csv>` : garde les courtiers à adresse belge 1000-1499 / 4000-7999, rattache chaque annuaire par BCE, sinon par domaine (+ un mot du nom en commun), sinon par nom (Jaccard ≥ 0,5) dans le même code postal.

## Chiffres
1 516 courtiers ; 22 présents chez les 6 compagnies, 521 chez au moins 4, 149 sans compagnie identifiée. Rattachés : AG 1 045, AXA 1 402, Baloise 1 176, NN 630, Allianz 453, Patronale 186.

## Limites
- KBC, Belfius, Ethias, Federale : pas de courtiers (réseau propre). Athora, Vivium, Cardif : pas d'annuaire exploitable. Assureurs luxembourgeois : aucune liste publique de courtiers partenaires.
- « Compagnies identifiées » est un minimum. Rattachements par nom à vérifier avant contact.
- Contrôle Sheet ↔ CSV cellule par cellule : 0 écart (les « + » des téléphones ont été réécrits en texte).

## Taille (ajout du 20/10/2026)
- `nbb_collect.py <scratchpad>` : pour chaque n° BCE, dernier dépôt de comptes à la Centrale des bilans (`consult.cbso.nbb.be/api/rs-consult/published-deposits?enterpriseNumber=…`, puis CSV du dépôt `…/api/external/broker/public/deposits/consult/csv/<id>`). Codes repris : 70 (chiffre d'affaires), 9900 (marge brute), 10/49 (total du bilan), 9087 / 1003 (ETP), 9905 (résultat).
- Comptes trouvés pour 1 456 courtiers (surtout exercice 2025) ; chiffre d'affaires publié par 114 seulement (modèles abrégé/micro), marge brute par 1 428.
- Sheet : colonnes T à AA (exercice, CA, marge brute, bilan, ETP, résultat, « Revenus = CA sinon marge brute », taille), tri par revenus décroissants. Seuils de taille modifiables dans Lisez-moi (Grand ≥ 1 M€, Moyen ≥ 250 k€, Petit ≥ 100 k€) : 107 grands, 436 moyens, 357 petits, 543 très petits, 73 sans comptes.
- Contrôle Sheet ↔ données BNB cellule par cellule après tri : 0 écart.
