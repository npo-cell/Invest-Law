# 2026-10-20 — Contrôle des VNI d'invest-law.eu

Photo du site au 20/10/2026 (lecture seule, rien modifié). Tableau de bord : https://claude.ai/artifact/E3kwtSBzrF4KKKR5XSu8R6
Données complètes : `docs/controle-vni/controle-vni-2026-10-20.json`. Script : `tools/controle_vni.py`.

Règle : date de création de la fiche comparée à la 1re VNI. OK si la 1re VNI tombe entre 7 jours avant et 3 mois après la création.

| Statut | Fonds | dont actifs |
|---|---|---|
| OK | 121 | 90 |
| VNI fausses | 2 | 2 |
| VNI avant la création | 31 | 23 |
| Début manquant | 17 | 8 |
| Création absente | 3 | 3 |
| Aucune VNI | 314 | 17 |

Autres anomalies : 122 fonds avec des VNI datées un week-end (décalage probable d'un jour à l'import) ; 61 fonds plus mis à jour depuis plus de 45 jours (surtout depuis le 7–8/06/2026) ; 7 fonds avec un historique en francs avant le passage à l'euro.

## VNI fausses
- DNCA ALPHA BONDS (LU1694789451, actif) : création 2017-12-14, 1re VNI 2017-12-12, écart -2 j — 424 sauts de plus de 20 % (ex. 2020-01-23 : 102.17 → 123.44) · 835 VNI datées un week-end (28 %) : dates probablement décalées d'un jour
- ECHIQUIER AGRESSOR A EUR (FR0010321802, actif) : création 1991-11-29, 1re VNI 1991-11-28, écart -1 j — 370 sauts de plus de 20 % (ex. 1991-12-05 : 95.28 → 626.48) · historique en francs avant 1998-12-30 (÷ 6,56 au passage à l'euro) · 1244 VNI datées un week-end (14 %) : dates probablement décalées d'un jour

## VNI avant la création (plus de 7 jours)
- ALLIANZ STRATEGY 50 NT EUR (LU1093406186, inactif) : création 2014-09-03, 1re VNI 2002-12-01, écart -4294 j
- Allianz Dyn Mlt Asst Strat SRI75 AT EUR (LU1594335520, inactif) : création 2017-05-02, 1re VNI 2007-05-01, écart -3654 j
- Amundi Income Opportunities (LU1894680757, actif) : création 2019-06-07, 1re VNI 2018-11-26, écart -193 j
- Amundi Obligations Internationales EUR-P-C (FR0010156604, inactif) : création 2005-04-25, 1re VNI 1999-12-27, écart -1946 j
- CAPITAL GROUP GLOBAL HIGH INCOME OPP (LUX) B EUR (LU0110451209, inactif) : création 2001-01-15, 1re VNI 1999-12-30, écart -382 j
- COMGEST GROWTH EMERGING MARKETS R EUR (IE00B65D2871, inactif) : création 2012-06-15, 1re VNI 2009-12-30, écart -898 j
- COMGEST GROWTH GLOBAL EUR (IE00BD5HXK71, inactif) : création 2014-01-21, 1re VNI 2010-12-30, écart -1118 j
- Carmignac Emerging Patrimoine (LU0992631647, inactif) : création 2013-12-30, 1re VNI 2011-03-30, écart -1006 j
- Carmignac Patrimoine A EUR (FR0010135103, actif) : création 1989-11-07, 1re VNI 1989-10-19, écart -19 j
- FFG BLI GLOBAL IMPACT EQUITIES R EUR (LU2612532759, actif) : création 2024-03-25, 1re VNI 2024-03-12, écart -13 j
- FFG GLOBAL EQUITY CONVICTIONS R EUR (LU2059537873, actif) : création 2021-08-31, 1re VNI 2008-03-30, écart -4902 j
- FFG GLOBAL FLEXIBLE CONVICTIONS R EUR (LU1697917083, actif) : création 2018-02-28, 1re VNI 2017-12-28, écart -62 j
- FVS BOND OPPORTUNITIES RT EUR (LU1481583711, actif) : création 2016-10-17, 1re VNI 2009-06-03, écart -2693 j
- Flossbach V S Multiple Opportunities II (LU1038809395, actif) : création 2014-04-03, 1re VNI 2007-10-22, écart -2355 j
- GS Patrimonial Balanced EUR Sustainable (LU1444115874, inactif) : création 2016-12-16, 1re VNI 1999-12-27, écart -6199 j
- M&G (LUX) INCOME ALLOCATION FUND A EUR (LU1582984818, actif) : création 2018-01-16, 1re VNI 2013-11-06, écart -1532 j
- M&G (LUX) OPTIMAL INCOME A EUR (LU1670724373, actif) : création 2018-09-07, 1re VNI 2007-04-19, écart -4159 j
- M&G (Lux) Asian A EUR Acc (LU1670618187, actif) : création 2018-10-26, 1re VNI 1999-12-27, écart -6878 j
- M&G (Lux) Dynamic Allocation A EUR Acc (LU1582988058, actif) : création 2018-01-16, 1re VNI 2009-12-02, écart -2967 j
- M&G (Lux) Emerging Markets Bond Fund A EUR Acc (LU1670631016, actif) : création 2018-09-21, 1re VNI 1999-12-27, écart -6843 j
- M&G (Lux) European Strategic Value Fund A EUR (LU1670707527, actif) : création 2018-09-20, 1re VNI 2008-01-31, écart -3885 j
- M&G (Lux) Global Corporate Bond Fund A-H EUR (LU1670713335, actif) : création 2018-12-07, 1re VNI 2013-09-04, écart -1920 j
- M&G (Lux) Global Emerging Markets A EUR (LU1670618690, actif) : création 2018-10-26, 1re VNI 2009-02-04, écart -3551 j
- ODDO BHF Avenir Euro CR-EUR (FR0000990095, actif) : création 1998-12-30, 1re VNI 1985-10-03, écart -4836 j
- ODDO BHF Convertibles Global CR-EUR (LU1493433004, actif) : création 2016-12-16, 1re VNI 2013-12-30, écart -1082 j
- ODDO BHF Global Equity Trend CRw-EUR (DE0009772988, actif) : création 2005-09-30, 1re VNI 1998-01-02, écart -2828 j
- ODDO BHF Polaris Balanced CRw-EUR (LU1864504425, actif) : création 2018-12-03, 1re VNI 2007-10-22, écart -4060 j
- ODDO BHF Polaris Dynamic CR-EUR (LU1849528234, actif) : création 2019-01-25, 1re VNI 2007-10-22, écart -4113 j
- ODDO BHF Polaris Flexible CR-EUR (LU1874836890, actif) : création 2019-02-13, 1re VNI 2007-10-09, écart -4145 j
- ODDO BHF Polaris Moderate CR-EUR (DE000A2JJ1W5, actif) : création 2018-12-10, 1re VNI 2005-07-14, écart -4897 j
- R-co Valor F Eur (FR0011261197, actif) : création 2012-10-03, 1re VNI 2006-02-27, écart -2410 j

## Début d'historique manquant (plus de 3 mois)
- ALKEN SMALL CAP EUROPE (LU0524465548, inactif) : création 2010-09-25, 1re VNI 2013-06-25, écart 1004 j
- BGF FIXED INCOME GLOBAL OPPS A2 EUR (LU1005243255, inactif) : création 2013-12-18, 1re VNI 2015-05-11, écart 509 j
- CAPITAL GROUP GLOBAL ALLOCATION B EUR (LU1006075656, inactif) : création 2014-01-31, 1re VNI 2015-01-01, écart 335 j
- CARMIGNAC ABSOLUTE RETURN EUROPE A EUR (FR0010149179, actif) : création 1997-02-03, 1re VNI 2003-01-02, écart 2159 j
- CT GLOBAL FOCUS (LU0757431068, inactif) : création 2005-12-06, 1re VNI 2025-04-06, écart 7061 j
- CT GLOBAL SMALLER COMPANIES (LU0570870567, inactif) : création 2011-03-03, 1re VNI 2013-11-18, écart 991 j
- Carmignac Portfolio Global Bond A EUR ACC (LU0336083497, actif) : création 2007-12-14, 1re VNI 2010-07-11, écart 940 j
- FFG GLOBAL DEFENSIVE I EUR (LU0945617289, inactif) : création 2017-08-01, 1re VNI 2024-10-24, écart 2641 j
- FFG GLOBAL EQUITY CONVICTIONS I EUR (LU2059537956, inactif) : création 2021-09-01, 1re VNI 2025-12-12, écart 1563 j
- JPM Global Balanced (LU0070212591, inactif) : création 1995-07-18, 1re VNI 2008-07-31, écart 4762 j
- Keren Patrimoine (KER---, inactif) : création 1999-03-15, 1re VNI 2002-01-10, écart 1032 j
- LAZARD BAYLIGHT US SMALL CAP EQUITY FUND BP EUR (IE0009FUD0M1, actif) : création 2024-10-30, 1re VNI 2025-09-08, écart 313 j
- LAZARD GLOBAL LIST INF EQUITY B EUR (IE00BX9C2459, actif) : création 2016-11-25, 1re VNI 2025-09-08, écart 3209 j
- LAZARD PATRIMOINE OPPORTUNITIES SRI RC EUR (FR0007028543, actif) : création 1999-01-08, 1re VNI 1999-12-27, écart 353 j
- LAZARD RATHMORE ALTERNATIVE FUND BP EUR (IE00BFZ4RX34, actif) : création 2019-09-20, 1re VNI 2025-09-08, écart 2180 j
- LELEUX INVEST PATRIMONIAL WORLD FOF PA EUR (BE6327306930, actif) : création 2021-05-03, 1re VNI 2021-11-02, écart 183 j
- NORDEN EUR (FR0000299356, actif) : création 1995-01-02, 1re VNI 2002-06-18, écart 2724 j

## Date de création absente
- DNCA Mandat Patrimoniale (FID DNCA Equil, actif) : création —, 1re VNI 2021-01-01
- M&G (LUX) GLOBAL STRATEGIC VALUE A EUR (LU3332968026, actif) : création —, 1re VNI 2026-05-29
- OMEGA ALLOCATION FLEXIBLE R EUR (FR0013357704, actif) : création —, 1re VNI 2018-09-03

## Fonds actifs sans aucune VNI
- AMUNDI ACTIONS EMERGENTS P C EUR (FR0010188383)
- Carmignac Pf Grandchildren A Eur Acc (LU196663100)
- DNCA FID - allocation evolutive (012010101)
- DNCA Mandat Evolutif (000000000000000000000)
- DNCA Mandat Prudent (000000000000000)
- FFG BLI AMERICAN IMPACT EQUITIES R USD (LU2612531785)
- FFG BLI EUROPEAN IMPACT EQUITIES R EUR (LU2612530977)
- FIC DNCA INFLATION TREND (XFCS00OL1561)
- FVS DIVIDEND RT EUR (LU2473801830)
- FVS GLOBAL QUALITY RT EUR (LU2673417882)
- Fid-keren-gestion-dynamique (000000004)
- Fid-keren-gestion-prudent (0000000000005)
- LELEUX FMP- One Life Portefeuille Modèle Dynamique en fonds externes (000000000000)
- LELEUX FMP- One Life Portefeuille Modèle Neutre en fonds externes (000000000000000000)
- Leleux Secu (Leleux Secu)
- M&G (Lux) Episode Macro Funds S EUR (LU3149167358)
- Rothschild & Co - FID - profil équilibre (01010101)

Les 297 fonds inactifs sans VNI sont dans le fichier JSON.
