# Consigne : préparation des fiches Wealth Belgium dans le Google Sheet (15/10/2026)

Demande de l'utilisatrice : préparer dans le Google Sheet « Gamme Wealth Belgium One Life – Fonds et ISIN » toutes les informations qui iront plus tard sur les fiches invest-law.eu. **Rien n'est mis sur invest-law.eu à ce stade.** Objectif : le plus d'informations possible, toutes exactes.

## Sources
- Uniquement la factsheet et le KID retenus pour la part (voir `recapitulatif.csv`, colonnes `Factsheet_fichier` / `KID_fichier`), lus dans les `.txt` à côté des PDF (et le PDF si le texte est illisible).
- Jamais une autre part, jamais une fiche invest-law existante d'une autre part (au plus : signaler une incohérence en remarque).
- Valeur douteuse, ambiguë ou absente → case vide + explication dans « Remarques ». Ne rien deviner.

## Onglet « Fiches » (une ligne par fonds, ligne = même numéro que l'onglet principal)
| Col | Champ | Règle |
|---|---|---|
| A | n | numéro de ligne |
| B | ISIN | |
| C | Nom du fonds | nom du fichier One Life |
| D | Maison de gestion | fichier One Life |
| E | Factsheet utilisée | date du document (AAAA-MM-JJ), vide si aucune |
| F | KID utilisé | date du KID, vide si aucun |
| G | Date de création | date de lancement **de la part** (AAAA-MM-JJ) ; si seule la date du fonds est donnée, la mettre et le préciser en remarque |
| H | Devise | devise de la part (EUR, USD…) |
| I | Type de fonds | type court en français (ex. « Actions internationales », « Obligataire », « Multi-actifs », « Monétaire ») |
| J | Compartiment | structure juridique telle qu'écrite (ex. « Compartiment de la SICAV Pictet (droit luxembourgeois) ») |
| K | Gérant(s) | nom(s) du ou des gérants |
| L | Encours (millions) | encours du fonds en millions, nombre avec point décimal |
| M | Devise de l'encours | |
| N | Date de l'encours | |
| O | Frais de gestion (%) | frais de gestion de la part (factsheet), nombre (1.50) |
| P | Frais courants / TER (%) | frais courants du KID (« frais de gestion et autres frais administratifs et d'exploitation »), sinon TER/frais courants de la factsheet ; préciser la source en remarque si factsheet |
| Q | SRI (1-7) | indicateur de risque du KID |
| R | Indice de référence | nom exact ; vide si l'indice n'est cité qu'« à titre de comparaison », pour le suivi du risque ou dans la partie ESG (remarque) ; « Aucun » si le document dit qu'il n'y a pas d'indice |
| S | Classification | Défensif / Equilibré / Dynamique / Agressif (voir ci-dessous) |
| T | Catégorie | **laisser vide** (décision du 15/10/2026) |
| U | SFDR (article) | 6, 8 ou 9 seulement si écrit dans un document |
| V | Investissements durables (%) | seulement si un pourcentage est écrit |
| W | Duration | fonds obligataires : valeur écrite (ex. « 3.2 ans ») |
| X | Qualité des émetteurs | notation moyenne écrite (ex. « BBB+ ») |
| Y | Disclaimer | avertissement principal de la factsheet, copié tel quel (une ou deux phrases sur les performances passées / le risque de perte) |
| Z | Politique d'investissement FR | texte copié-collé **sans reformulation** (objectif + politique/stratégie), paragraphes séparés par une ligne vide ; jamais le commentaire du mois, les frais, les risques ou les mentions légales |
| AA | Politique d'investissement EN | idem si le document est en anglais |
| AB | Source de la politique | « Factsheet » ou « KID » (si pas de factsheet ou factsheet sans texte : section « Objectifs / En quoi consiste ce produit » du KID, copiée telle quelle) |
| AC | Remarques | doutes, valeurs non retenues, renommages, etc. |

### Classification (jugement, décision du 15/10/2026)
- **Défensif** : monétaire, obligataire, fonds à échéance, ou majoritairement obligataire (SRI en général 1–3).
- **Equilibré** : diversifié / mixte (actions environ 20–60 %), flexibles prudents à modérés (SRI en général 3).
- **Dynamique** : actions diversifiées (monde, Europe, US…) ou mixte à dominante actions (SRI en général 4–5).
- **Agressif** : actions thématiques, sectorielles, small caps spécialisées, pays émergents/pays uniques, matières premières, crypto/blockchain (SRI en général 5–7).
Indiquer en remarque la raison en quelques mots si le cas n'est pas évident.

## Onglet « Allocations » (une ligne par élément, en pourcentage, factsheet la plus récente)
Colonnes : n | ISIN | Nom du fonds | Type | Libellé | % | Date de la factsheet.
- Types : `Positions` (principales lignes), `Secteurs`, `Classes d'actifs`, `Zones géographiques`, et tout autre tableau en % présent (`Devises`, `Notations`, `Maturités`, `Capitalisations`, `Pays`…).
- Libellé et % tels qu'écrits (% en nombre avec point : 4.4). Pas d'allocation pour un fonds sans factsheet.
- Si une même répartition est donnée pour le fonds et l'indice, ne prendre que le fonds.

## Mémoire
Chaque fonds est d'abord écrit dans `docs/wealth-belgium-2026-10-15/fiches/<ISIN>.json` (source de vérité), puis recopié dans le Sheet.

## Précisions après l'essai sur 5 fonds (15/10/2026)
- **Nombres** : recopiés avec la précision du document, point décimal (1,4 % → `1.4`). Encours en milliards converti en millions (9,3 Md → `9300`) ; sans date propre, date de l'encours = date de la factsheet.
- **Frais** : « frais de gestion » = frais de gestion (ou commission de gestion) de la part. Si le document ne donne que des « frais courants », « TER » ou « frais de gestion totaux / et autres frais » → colonne Frais courants seulement, Frais de gestion vide.
- **Indice** : indice composite → recopié en entier tel qu'écrit. Devise différente selon le document → celle du tableau de la part dans la factsheet, divergence en remarque. Indice servant au risque ET à l'objectif ou à la mesure de performance → retenu. Uniquement « à titre de comparaison », pour le risque, ou « n'est pas un objectif » → vide + remarque.
- **Duration** : duration ou « sensibilité » acceptée ; valeur telle qu'écrite, préciser « (sensibilité) » si c'est le terme du document, et « ans » seulement si écrit.
- **Investissements durables (%)** : seulement une part effective ; un minimum (« au moins 10 % ») va en remarque.
- **Gérant(s)** : noms de personnes ; un nom d'équipe est accepté (« Asia Pacific Equity Team ») ; jamais la société de gestion.
- **Allocations** : types autorisés : Positions, Secteurs, Classes d'actifs, Zones géographiques, Pays, Devises, Notations, Maturités, Capitalisations, Styles, Instruments. Exclus : contributions à la performance, sensibilités par pays, répartitions de l'indice. Valeurs négatives et totaux ≠ 100 % gardés tels quels. Positions datées d'une autre date que la factsheet → remarque.
- **Politique** : garder les intertitres du bloc (Objectif, Stratégie…) ; exclure les « atouts », arguments commerciaux, commentaires et risques. Si la factsheet n'a qu'un texte marketing de une ou deux phrases sans objectif/politique → prendre le KID (source « KID »).
- **Contrôle obligatoire** : après chaque fiche, `python3 -I docs/wealth-belgium-2026-10-15/verif_fiche.py <ISIN>` (vérifie que chaque phrase de la politique, du disclaimer, du compartiment, de l'indice, des gérants et chaque libellé/% d'allocation figure dans les PDF) ; corriger jusqu'à 0 écart.
