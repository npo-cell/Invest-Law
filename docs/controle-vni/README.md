# Contrôle des VNI : point de départ pour tout travail sur les VNI

À lire avant de corriger ou d'importer des VNI à la main. Import quotidien automatique : `docs/zimbra-vni/CONSIGNE.md`.

## Ce qui existe
- **Tableau de bord** : https://claude.ai/artifact/E3kwtSBzrF4KKKR5XSu8R6 (artéfact de Louis, type Dashboard ; données : `controle-vni-2026-10-20.json`, y compris ISIN invalides, doublons, devises, VNI vérifiées à la source). Statuts cliquables, liste filtrable, colonne Remarques. Pour y accéder, demander à Louis de le partager. Sans accès en modification, publier une copie (cf. `AGENTS.md`).
- **Script** : `python3 tools/controle_vni.py` (après login/verify). Il lit tout le site en lecture seule et écrit `docs/controle-vni/controle-vni-AAAA-MM-JJ.json`, une ligne par fonds, avec les colonnes du tableau de bord. Il affiche ensuite le bilan.
- **Contrôles** : `controle-vni-2026-10-20.json`, et le rapport lisible `docs/2026-10-20-controle-vni.md`, qui liste les fonds par statut.

## Règles du contrôle (choisies le 20/10/2026 avec Louis)
On compare la date de création de la fiche (`CreationDate`) à la 1re VNI enregistrée.

| Statut | Règle |
|---|---|
| OK | 1re VNI entre 7 jours avant et 3 mois après la création |
| VNI fausses | 3 sauts ou plus de plus de 20 % entre deux VNI consécutives, hors passage à l'euro |
| VNI avant la création | 1re VNI plus de 7 jours avant la création |
| Début manquant | 1re VNI plus de 3 mois après la création |
| Création absente | VNI présentes, pas de date de création |
| Aucune VNI | aucune VNI sur le site |

La tolérance de 7 jours vient du décalage d'un jour décrit plus bas. Sans elle, une centaine de fonds sortiraient « avant la création » à 1 ou 2 jours près.

## Bilan au 20/10/2026 (488 fiches)
- 121 OK (90 actifs) ; 2 VNI fausses ; 31 VNI avant la création ; 17 début manquant ; 3 création absente ; 314 sans VNI, dont 17 actifs.
- **VNI fausses** :
  - **Echiquier Agressor A** : francs et euros alternent dans l'historique (625 → 95 → 626…).
  - **DNCA Alpha Bonds** : sauts de ±21 % répétés depuis 2020, probablement deux parts mélangées.
- **VNI avant la création** : il faut vérifier fonds par fonds, la cause n'est pas toujours la même.
  - Pour M&G (Lux), ODDO BHF Polaris, FFG Global Equity Convictions R, Flossbach, GS Patrimonial…, l'historique vient probablement de l'ancien fonds (fusion, « re-domiciliation » en 2018) ou d'une part sœur.
  - Ou bien la date de création de la fiche est fausse.

## Anomalies qui touchent beaucoup de fonds
1. **Dates décalées d'un jour (122 fonds).** Beaucoup d'historiques n'ont aucune VNI le vendredi, mais en ont le dimanche : les dates ont reculé d'un jour.
   - C'est probablement un problème de fuseau horaire lors d'anciens imports.
   - Certains fonds sont décalés seulement en partie (avant une certaine date).
   - Les imports récents de la routine Zimbra (DNCA, Leleux) tombent bien en semaine.
   - **Ne pas corriger en masse sans accord** : chaque VNI changerait de date.
2. **Plus mises à jour (61 fonds)** : dernière VNI le 7 ou le 8/06/2026 pour la plupart. Le flux qui les alimentait s'est arrêté, et la plupart de ces fonds ne viennent ni de CACEIS ni de DNCA.
3. **Historique en francs (7 fonds : Carmignac, ODDO BHF Avenir, Lazard…)** : chute de 85 % (÷ 6,55957) entre fin 1998 et début 1999. Les performances longues de ces fonds sont donc faussées.

## Ce que le contrôle ne prouve pas (question de Louis, 20/10)
Le contrôle vérifie la cohérence des séries de VNI. Il ne compare **pas** les valeurs à une source officielle : une VNI plausible peut être fausse.
- **Vérifié** : les 178 VNI importées par la routine Zimbra (`docs/zimbra-vni/journal.csv`) sont identiques sur le site à celles des fichiers CACEIS et DNCA.
- **ISIN** : pas de doublon. 16 fiches ont un ISIN invalide, dont 2 avec des VNI :
  - fiche 172 « DNCA Mandat Patrimoniale » (ISIN `FID DNCA Equil`) ;
  - fiche 10 « Keren Patrimoine » (`KER---`, inactive), dont la série est **identique** à celle de la fiche 115 « KEREN PATRIMOINE C EUR » (FR0000980427) : c'est un doublon.
- **Autres fiches à revoir** :
  - fiche 373 : le nom et l'ISIN sont inversés (nom « LU0128499588 », ISIN « LU373 ») ;
  - devise « E » au lieu de « EUR » sur 19 fiches ;
  - « DRIEHAUS US SMALL CAP EQUITY FUND B USD » a la devise « E ».
- **Pas vérifié** :
  - les VNI anciennes (avant la routine), dont on ne connaît pas la source ;
  - la devise des VNI (EUR ou USD) ;
  - le fait que chaque série corresponde bien à la classe de part de l'ISIN.

  Pour les vérifier : comparer par échantillon avec les factsheets officielles (VNI de fin de mois) ou les fichiers des maisons.

## Pistes pour la suite (aucune n'est décidée)
- Fonds aux VNI fausses : retrouver la bonne série auprès de la maison de gestion, puis remplacer l'historique. Montrer ancien → nouveau d'abord.
- Dates décalées : décider avec l'équipe s'il faut recaler les dates (`PUT /api/funds/{id}/vl?month=`).
- Fonds plus mis à jour : trouver la source d'origine, ou demander les VNI aux maisons.
- Francs : convertir en euros les VNI d'avant le passage à l'euro (÷ 6,55957), ou les supprimer. À décider.
- Règle de l'équipe : en cas de doute, ne rien mettre sur le site (cf. skill invest-law).

## Mettre à jour le tableau de bord après un nouveau contrôle
1. Lancer `python3 tools/controle_vni.py`.
2. Envoyer le nouveau JSON dans l'artéfact : outil Artifact, `asset: true`, avec l'`url` du tableau de bord.
3. Mettre à jour le document `datasets/fonds` avec `ArtifactData` `update` : `source.url`, `source.name`, `updated`.
4. Committer le JSON et une note dans `docs/sessions/`.
