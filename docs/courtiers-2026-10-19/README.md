# Courtiers Bruxelles-Wallonie et compagnies partenaires (19/10/2026)

Résultat : Google Sheet « Courtiers Bruxelles-Wallonie – compagnies partenaires (prospection One Life) » sur le Drive « Invest-Law Noa et Louis » :
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
