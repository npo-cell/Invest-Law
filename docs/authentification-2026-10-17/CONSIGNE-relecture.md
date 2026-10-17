# Consigne : relecture des cases non retrouvées automatiquement (17/10/2026)

Demande de l'utilisatrice : authentifier tout le classeur « Gamme One Life complète ». Chaque information doit venir de la factsheet la plus récente ou du KID du fonds. Le script `authentifier.py` a cherché chaque case dans le texte des PDF. Les cases qu'il n'a pas retrouvées sont à relire à la main, dans les PDF.

## Entrée
Fichier de lot (JSON), une entrée par fonds :
- `pdfs` : la factsheet utilisée (la plus récente) puis le KID s'il existe ;
- `cases` : champ → valeur notée dans le classeur ;
- `allocations_non_retrouvees` : lignes d'allocation (type, libellé, %) non retrouvées (60 au plus ; total dans `allocations_non_retrouvees_total`).

## Méthode
- Lire le texte (`pdftotext -layout <pdf> -`). Si l'information est dans un graphique ou un tableau image, regarder la page : `pdftoppm -r 90 -f <p> -l <p> -png <pdf> /tmp/.../page`, puis ouvrir l'image avec Read.
- Ne jamais chercher ailleurs que dans ces PDF.

## Verdict par case
- `CONFORME` : la même information figure dans la factsheet ou le KID. L'écriture peut différer : format de date, virgule ou point, « % », espace, mise en page, césure, nom traduit (secteur ou pays du site), ou arrondi d'un même chiffre (1,65 noté 1.65). Pour un texte, le sens et la quasi-totalité des phrases doivent être repris du document.
- `DIFFERENT` : le document donne une autre valeur. Indiquer `valeur_document`. Par exemple, une autre date, d'autres frais, un autre SRI, un autre indice, un autre gérant ou un autre encours ; un encours ou des allocations d'une autre date compte aussi.
- `ABSENT` : l'information ne figure ni dans la factsheet ni dans le KID. La case vient d'une autre source, ou d'un texte rédigé ou résumé.
- Mettre une `note` courte et factuelle (page, formulation exacte du document).

## Allocations (un verdict global par fonds)
- `CONFORME` : les lignes listées figurent dans la factsheet, y compris lues sur l'image.
- `PARTIEL` : certaines figurent et d'autres non. Dire combien et lesquelles.
- `DIFFERENT` : la factsheet donne d'autres pourcentages, d'une autre date par exemple.
- `ABSENT` : la factsheet ne contient pas cette répartition.

## Sortie
Écrire `docs/authentification-2026-10-17/relecture/lot-<K>-verdicts.json` :
```json
[{"isin": "...", "cases": {"indice": {"verdict": "DIFFERENT", "valeur_document": "MSCI World NR EUR", "note": "factsheet p.1"}},
  "allocations": {"verdict": "CONFORME", "note": "secteurs lus sur le graphique p.2"}}]
```
Mettre une entrée par fonds du lot, et la clé `allocations` seulement s'il y avait des allocations à relire. Pas de commit, pas de push, rien sur invest-law.eu.
