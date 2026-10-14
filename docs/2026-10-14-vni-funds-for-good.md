# 2026-10-14 — Fichier VNI de Funds For Good (VNIs.xlsx)

Source : mail de Maxime Desaive (Funds For Good) du 14/10/2026, pièce jointe compilée par François Scarnière. Rien n'a été importé sur le site.

## Contenu
| Feuille | Part | ISIN | Fiche | Période | VNI réelles (2 décimales) | Valeurs reconstituées |
|---|---|---|---|---|---|---|
| GD | R | LU0945616984 | 106 | 01/2018 → 30/09/2026 | depuis 24/10/2024 | 2018 → 23/10/2024 (backtest « diminué des coûts actuels ») |
| GD | I | LU0945617289 | 205 | 01/2018 → 30/09/2026 | depuis 24/10/2024 | idem |
| GELC | I | LU2736456752 | 200 | 04/2021 → 30/09/2026 | depuis 28/03/2024 | 2021 → 27/03/2024 |
| GELC | R | LU2736456596 | 59 | 04/2021 → 30/09/2026 | depuis 27/05/2024 | 2021 → 24/05/2024 |
| GFC | R | LU1697917083 | 15 | 27/02/2018 → 30/09/2026 | tout | — |
| GFC | I | LU1697917166 | 204 | 24/04/2019 → 30/09/2026 | tout | — |
| GIE | R | LU2612532759 | 196 | 12/03/2024 → 30/09/2026 | tout | — |
| GIE | I | LU2612532833 | 201 | 12/03/2024 → 30/09/2026 | tout | — |
| GEC | I | LU2059537956 | 199 | 01/2018 → 30/09/2026 | depuis 12/2025 | 2018 → 11/12/2025 (« track extension » MSCI + fonds irlandais) |
| GEC | R | LU2059537873 | 107 | 01/2018 → 30/09/2026 | depuis 12/2025 | 2018 → 12/12/2025 |

Absents du fichier : FFG BLI American Impact (197, 202) et European Impact (198, 203).

## Comparaison avec invest-law
- 7 des 10 parts n'ont aucune VNI sur le site (205, 200, 59, 196, 201, 199, 204).
- 106, 107, 15 ont un historique, arrêté au 07/06/2026.
- **Décalage d'un jour sur le site** : sur les dates communes (VNI réelles), la valeur du site à la date J est celle que FFG date au jour ouvré suivant (106 : 314/314 ; 107 : 93/93 ; 15 : 1 608/1 608). Le site n'a presque aucun vendredi et beaucoup de dimanches pour ces fiches et pour d'autres (5, 23, 87…), alors que Leleux (116, saisi récemment) est correct du lundi au vendredi. Probable bug de fuseau horaire lors d'un import ancien (date à minuit convertie la veille). À signaler au développeur.
- 106 et 107 : avant les dates ci-dessus, le site a un historique différent du fichier (ex. 106 au 01/01/2018 : site 113,77, fichier 91,44 reconstitué) : ancienne stratégie réelle sur le site, backtest de la nouvelle stratégie dans le fichier.
