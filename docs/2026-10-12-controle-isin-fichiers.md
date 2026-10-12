# 2026-10-12 — Contrôle ISIN des fichiers en ligne sur invest-law.eu

Lecture seule. Chaque rapport en ligne (730 fichiers, 488 fiches) a été téléchargé ; on vérifie que l'ISIN affiché sur la fiche figure dans le PDF (ISIN validés par clé de contrôle).

| Résultat | Nombre |
|---|---|
| ISIN de la fiche présent dans le PDF | 711 |
| À examiner | 19 |

## Fichiers à examiner

| Fiche | ISIN fiche | Fonds | Rapport | Fichier | Constat |
|---|---|---|---|---|---|
| 448 | LU1100076550 | CLARTAN VALEURS C EUR | Rapport de Gestion Septembre 2026 | LU1100076550__Factsheet_FR_2026-09-30.pdf | Texte du PDF brouillé (police encodée) : ISIN non lisible automatiquement ; vérifié par décodage lors de la recherche. |
| 458 | LU2389405163 | CPR INVEST HYDROGEN A2 EUR | Rapport de gestion Août 2026 | LU2389405163__Factsheet_FR_2026-08_partA-LU2389405080.pdf | Même fonds, autre part : PDF de la part A (LU2389405080), fiche = part A2. |
| 93 | LU1515062757 | DNCA INVEST EUROPE GROWTH IG EUR | Fiche mensuelle Juillet 2026 | Fiche_mensuelle_DNCA_Invest_SRI_Europe_Growth_A_2026-07.pdf | Même fonds (renommé SRI Europe Growth), autre part : PDF part A (LU0870553020 = fiche 94), fiche = part IG. |
| 468 | LU1515062674 | DNCA INVEST VALUE EUROPE IG EUR | Fiche mensuelle Août 2026 | Fiche_mensuelle_DNCA_Invest_Value_Europe_A_2026-08.pdf | Même fonds, autre part : PDF part A (LU0284396016 = fiche 71), fiche = part IG. |
| 106 | LU0945616984 | FFG GLOBAL DEFENSIVE R EUR | Rapport semestriel Juin 2026 | Rapport_semestriel_FFG_2026-06-30.pdf | Rapport semestriel/annuel multi-fonds : pas d'ISIN par part dans le document (normal). |
| 59 | LU2736456596 | FFG GLOBAL EQUITIES LOW CARBON R EUR | Rapport semestriel Juin 2026 | Rapport_semestriel_FFG_2026-06-30.pdf | Rapport semestriel/annuel multi-fonds : pas d'ISIN par part dans le document (normal). |
| 107 | LU2059537873 | FFG GLOBAL EQUITY CONVICTIONS R EUR | Rapport semestriel Juin 2026 | Rapport_semestriel_FFG_2026-06-30.pdf | Rapport semestriel/annuel multi-fonds : pas d'ISIN par part dans le document (normal). |
| 15 | LU1697917083 | FFG GLOBAL FLEXIBLE CONVICTIONS R EUR | Rapport semestriel Juin 2026 | Rapport_semestriel_FFG_2026-06-30.pdf | Rapport semestriel/annuel multi-fonds : pas d'ISIN par part dans le document (normal). |
| 187 | 000000000000000000 | LELEUX FMP- One Life Portefeuille Modèle Neutre en fonds externes | Fiche mensuelle Mai 2026 | Fiche_mensuelle_OneLife_Portefeuille_Modele_Neutre_2026-05.pdf | Portefeuille modèle (pas d'ISIN propre) : normal. |
| 116 | BE6370437590 | LELEUX INVEST DYNAMIC WORLD FOF PA EUR | Fiche mensuelle Août 2026 | Fiche_mensuelle_Leleux_Invest_Dynamic_World_FOF_R_2026-08.pdf | Même fonds, autre part : PDF classe R (BE6370436584), fiche = PA. |
| 118 | BE6327306930 | LELEUX INVEST PATRIMONIAL WORLD FOF PA EUR | Fiche mensuelle Août 2026 | Fiche_mensuelle_Leleux_Invest_Patrimonial_World_FOF_RDIS_2026-08.pdf | Même fonds, autre part : PDF classe R Dis (BE6269807184), fiche = PA. |
| 119 | BE6327307946 | LELEUX INVEST RESPONSIBLE WORLD FOF PA EUR | Fiche mensuelle Août 2026 | Fiche_mensuelle_Leleux_Invest_Responsible_World_FOF_R_2026-08.pdf | Même fonds, autre part : PDF classe R (BE6304593781), fiche = PA. |
| 75 | LU3149167358 | M&G (Lux) Episode Macro Funds S EUR | Rapport de Gestion Juillet 2026 | _lux_-episode-macro-fund_eur_sh_acc_lu_monthly-fund-review_eng_pe_lu1670714226.pdf | Même fonds, PDF part S-H : liste d'autres parts, ISIN de la fiche absent. |
| 127 | LU2381585830 | MAINFIRST MEGATRENDS ASIA A USD | Rapport de gestion Août 2026 | LU2381585830__Factsheet_EN_2026-08_partC1-LU2381586309.pdf | Même fonds, autre part : PDF part C1 (LU2381586309), fiche = part A USD. |
| 360 | FR0013357704 | OMEGA ALLOCATION FLEXIBLE R EUR | Rapport de gestion Juin 2026 | FR0013357704__RapportSemestriel_FR_2026-06-30.pdf | Rapport semestriel/annuel multi-fonds : pas d'ISIN par part dans le document (normal). |
| 387 | RCOG387 | R-CO GOLD MINING EUR C | Rapport de gestion Août 2026 | FR0007001581__Factsheet_FR_2026-08.pdf | ISIN de la fiche invalide (« RCOG387 ») : le PDF est bien R-co Gold Mining FR0007001581 → corriger l'ISIN de la fiche. |
| 417 | LU0556665551 | SMART VALUE INVESTORS EQUITY FLEXIBLE A EUR | Rapport de gestion Juin 2025 | LU0556665551__RapportSemestriel_EN_2025-06-30.pdf | Rapport semestriel/annuel multi-fonds : pas d'ISIN par part dans le document (normal). |
| 444 | LU0558384706 | VECTOR FLEXIBLE C3 EUR | Rapport de gestion Août 2026 | LU0558384706__Factsheet_EN_2026-08.pdf | Même fonds (Vector Flexible), le PDF liste d'autres parts ; ISIN de la part C3 absent. |
| 445 | LU0366797354 | VECTOR NAVIGATOR C3 EUR | Rapport de gestion Août 2026 | LU0366797354__Factsheet_EN_2026-08.pdf | Même fonds (Vector Navigator), le PDF liste d'autres parts ; ISIN de la part C3 absent. |

## ISIN non conformes sur les fiches

- 387 R-CO GOLD MINING EUR C : « RCOG387 » → FR0007001581.
- 165 Carmignac Pf Grandchildren A EUR Acc : « LU196663100 » (11 caractères, tronqué).
- 373 : ISIN « LU373 » et nom « LU0128499588 » (champs inversés ?).
- Mandats / fonds internes sans ISIN (normal) : 70, 10, 171, 172, 173, 178, 187, 191, 192, 193, 194, 195.
- ROBECO INDIAN EQUITIES D EUR (LU0491217419) : aucune fiche sur le site.

## Constat

- Aucun fichier d'un autre fonds n'a été trouvé : les 19 cas sont soit une autre part du même fonds, soit un document multi-fonds, soit un PDF illisible, soit un ISIN de fiche erroné.
- Les fiches 458, 93, 468, 116, 118, 119, 127, 75, 444 et 445 affichent un document d'une autre part : frais, encours et date de création peuvent différer de la part de la fiche.
