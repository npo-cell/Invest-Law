# 2026-10-15 — Historique VNI Leleux Invest (mail de Laetitia De Noyette)

Source : mail de Laetitia De Noyette (Leleux Fund Management & Partners) du 15/10/2026, 13h47 UTC, fil « Envoi des VNI à une plateforme contrepartie » : « Voici les historiques jusqu'à la date du 7/10 ». Contexte du fil : historique jusqu'au 02/10 envoyé le 09/10 ; envoi quotidien CACEIS (réf. REF0000207682) reçu à partir du 12/10 avec la VNI du 08/10 ; trou à combler entre le 02/10 et le 08/10.

Pièce jointe : `docs/vni-leleux-2026-10-15/originaux/Leleux Invest - Historique VNI des fonds.xlsx` (8 onglets, un par part, colonnes Date / Price, du lundi au vendredi, sans valeur vide). Toutes les séries : `docs/vni-leleux-2026-10-15/toutes_les_series.csv`.

## Comparaison avec le site (15/10/2026)
| Part | ISIN | Fiche | Fichier | Site |
|---|---|---|---|---|
| Equities World R | BE6202762975 | 117 | 3 946 VNI, 17/09/2010 → 07/10 | 3 923 VNI, jusqu'au 02/10 ; **décalé d'un jour jusqu'au 03/06/2026**, juste depuis le 05/06/2026 |
| Equities World P | BE6288463506 | 530 | 2 430, 31/10/2016 → 07/10 | 2 427, identiques |
| Patrimonial World P | BE6288478652 | 531 | 2 422, 31/10/2016 → 07/10 | 2 419, identiques |
| Patrimonial World PA | BE6327306930 | 118 | 1 218, 02/11/2021 → 07/10 | 1 215, identiques |
| Responsible World P | BE6304594797 | 539 | 2 012, 29/06/2018 → 07/10 | 2 009, identiques |
| Responsible World PA | BE6327307946 | 119 | 1 280, 06/07/2021 → 07/10 | 1 277, identiques |
| Dynamic World P | BE6370440628 | 536 | 151, 02/03/2026 → 07/10 | 148, identiques |
| Dynamic World PA | BE6370437590 | 116 | 151, 02/03/2026 → 07/10 | 148, identiques |

- Sur le site, les 8 fiches s'arrêtent au 02/10/2026 : il manque les 05, 06 et 07/10 (dans le fichier) et les VNI à partir du 08/10 (envoi CACEIS, pas encore sur le site).
- Fiche 117 : même décalage d'un jour que les autres fiches touchées (`docs/2026-10-14-vni-decalees.html`) sur l'historique 2010 → 03/06/2026 (3 830 dates). À corriger quand la suppression de VNI fonctionnera.

## Import (15/10/2026, accord de l'utilisatrice)
- Sauvegarde avant import : `docs/vni-leleux-2026-10-15/avant_<fiche>.json`. Test d'une ligne (116, 07/10, 1 033,45) puis les 23 autres par `POST /api/funds/vl/upload-by-isin`.
- Relecture : 24/24 conformes, ancien historique intact, aucune date en plus ; les 8 fiches vont maintenant jusqu'au 07/10/2026. Journal : `docs/vni-leleux-2026-10-15/import.log`.
- Reste : VNI depuis le 08/10 (envoi CACEIS) pas encore sur le site.

## Détail de l'import
- 24 VNI : 05, 06 et 07/10/2026 pour les 8 parts : `docs/vni-leleux-2026-10-15/import-propose.csv`.
- Rien d'autre : l'historique des 7 parts correctes est déjà complet ; celui de 117 n'est pas modifié (décalage).
