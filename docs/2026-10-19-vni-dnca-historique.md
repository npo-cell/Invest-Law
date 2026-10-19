# VNI DNCA : rattrapage depuis la source officielle et décalage de dates (19/10/2026)

## Rattrapage (fait le 19/10)
Source : le site officiel de DNCA (JSON du graphique « NAV evolution » de chaque part, `https://www.dnca-investments.com/api/v1/funds/{fund_slug}/shares/{share_slug}/components/nav_evolution?locale=en`). Il faut d'abord ouvrir la page de la part en gardant les cookies, et envoyer l'en-tête `X-Requested-With: XMLHttpRequest`. Les slugs se trouvent dans `assets/json/funds_INT_en.json`. Scripts : `docs/vni-dnca-2026-10-19/`.

Contrôle de la source : les 119 VNI des mails DNCA reçus sur Zimbra (06–15/10) sont identiques.

**14 932 VNI importées** (`docs/vni-dnca-2026-10-19/vni-importees.csv`), puis relues une par une sur le site : aucun écart.
- 7 fiches arrêtées au 07/06 (44, 89, 91, 92, 5, 90, 71) : VNI du 09/06 au 05/10, soit 84 par fiche.
- Fiche 8 (Évolutif A) : VNI du 04/03 au 05/10 (148).
- 7 fiches vides, historique complet : 93 Europe Growth IG (depuis 2017), 464 Global New World A3 (depuis 2025), 465 Norden Europe A (depuis 2016), 466 Sérénité Plus B (depuis 2016), 94 SRI Europe Growth A (depuis 2012), 467 Strategic Resources A (depuis 2024), 468 Value Europe IG (depuis 2017).

Les dates importées ne chevauchent pas l'historique existant : l'import commence le lendemain de la dernière VNI réellement présente.

## Décalage de dates dans l'historique existant (NON corrigé, décision à prendre)
Comparaison de chaque VNI déjà présente sur le site avec la VNI officielle DNCA :

| Fiche | VNI sur le site | Bonne date | Datée 1 jour trop tôt | Datée 2 jours trop tôt | Autre |
|---|---|---|---|---|---|
| 89 Beyond Alterosa A | 1 871 | 28 | 1 843 | 0 | 0 |
| 91 Beyond Semperosa A | 1 871 | 5 | 1 865 | 0 | 1 |
| 92 Credit Conviction A | 4 562 | 153 | 4 408 | 0 | 1 |
| 90 Sustain Climate A | 1 337 | 4 | 1 333 | 0 | 0 |
| 5 Eurose A | 5 734 | 33 | 2 167 | 3 534 | 0 |
| 8 Évolutif A | 4 591 | 11 | 1 039 | 3 541 | 0 |
| 71 Value Europe A | 4 524 | 4 | 1 063 | 3 457 | 0 |
| 44 Alpha Bonds A | 2 878 | 17 | 559 | 1 554 | 748 (week-ends remplis) |

Conclusion : **presque tout l'historique DNCA déjà présent sur le site est daté 1 ou 2 jours trop tôt**, depuis l'origine (2007–2008 pour les plus anciens). Les valeurs, elles, sont justes. L'effet reste faible sur les graphiques, mais une performance calculée à une date précise (fin de mois, fin d'année) est légèrement fausse.

Leleux Invest (fiche 117) montre la même anomalie jusqu'en mai 2026 (dates du dimanche au jeudi). Aucune source officielle n'a été trouvée pour vérifier son historique.

**Correction possible** : remplacer l'historique de ces 8 fiches par les VNI officielles DNCA, mois par mois (`PUT /api/funds/{id}/vl?month=`), après simulation, puis relecture. À faire seulement avec l'accord de l'équipe, car ce sont des données déjà en ligne.
