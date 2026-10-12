# 2026-10-12 — Factsheets de la gamme One Life

> Résumé reconstitué à partir des commits et fichiers de la branche `claude/adoring-planck-eamiy1` ([PR npo-cell/Invest-Law#2](https://github.com/npo-cell/Invest-Law/pull/2)). Ce n'est pas la conversation d'origine.
> Session Claude d'origine (visible uniquement par son auteur, sauf partage) : https://claude.ai/code/session_016duzj35V5tvynUCGyvuejq

## Objectif
Trouver la dernière factsheet (reporting mensuel) de chacun des **482 fonds** de la gamme One Life, avec URL, date et vérification que l'ISIN figure bien dans le document.

## Déroulé (commits, heures UTC)
1. **08:19 — Passe 1 (partielle)** : 97 fonds trouvés, 343 introuvables. Beaucoup de sites gestionnaires injoignables depuis l'environnement cloud (DNS bloqué).
2. **08:31 — Liste des domaines** : 242 domaines de gestionnaires validés (`domaines_gestionnaires.xlsx`, `allowed_domains.txt`, 276 lignes) pour ouvrir l'accès réseau de l'environnement.
3. **09:30 — Passe 2** : PDF réellement ouverts et ISIN vérifiés → 408/482.
4. **09:35 — Rattrapage** : 25 fonds supplémentaires via fundinfo et Morningstar.

## Résultat final (`factsheets/factsheets_gamme_one_life.xlsx`)
| Statut | Nombre |
|---|---|
| TROUVE | 423 (dont 14 factsheets anciennes, > 3 mois) |
| FONDS_INTERNE (codes `XFCS…`, pas de reporting public) | 23 |
| INTROUVABLE | 23 |
| NON_VERIFIE | 9 |
| AUTRE_SOURCE | 4 |

- Sources : site du gestionnaire 366, fundinfo 53, Morningstar 13, autre 4.
- ISIN vérifié dans le PDF : 427/482.
- Dates dominantes : 31/08/2026 et 30/09/2026.

Colonnes : ISIN, Nom, Gestionnaire, Statut, Source, Date factsheet, Ancienne (>3 mois), ISIN vérifié, URL factsheet, Page fonds, Notes.
Onglet **« A vérifier - introuvables »** : les 69 lignes à revoir manuellement.

## Fonds à traiter manuellement
**Introuvables (23)** : Apicil Trésorerie GAC, Arcipelagos Serenity, AXA WF Sustainable Equity QI, Capertino Flexible Allocation, Conviction Patrimoine, IVO IG 2030, M&G Global Strategic Value, MFP Global Systematic, Omega Allocation Flexible, Orcadia Global Sustainable Balanced, Quest Cleantech, Roche-Brune Zone Euro Actions, Shelter UCITS (×3), Smart Value Investors (×2), SPM Global Flexible, Stratégie Rendement, Stratégie Souveraineté Européenne, TC New Horizon, Trusteam Optimum, Waterloo Global Flexible.

**Non vérifiés (9)** : Candriam Robotic, Driehaus US Small Cap, Leleux Invest (×3), M&G Episode Macro, Tobam Global Blockchain, Vector Flexible, Vector Navigator.

**Autre source (4)** : BNY Mellon Global Real Return, Mainfirst (×3).

**Fonds internes (23)** : fonds dédiés `FIC …` (Fiducenter, Delcap, Privalux, Andbank, Invest4Growth, etc.) — à demander directement à l'assureur ou au gestionnaire.

**Gestionnaires sans domaine validé (23)** : voir onglet « Sans domaine validé » de `domaines_gestionnaires.xlsx` (ex. Delcap, IVO Capital Partners, J. Safra Sarasin).

## Fichiers
- `factsheets/factsheets_gamme_one_life.xlsx` — tableau final
- `factsheets/domaines_gestionnaires.xlsx`, `factsheets/allowed_domains.txt` — domaines validés
- `factsheets/raw/` (passe 1), `factsheets/raw_v2/` (passe 2) — données brutes JSON
