# 2026-10-13 — Politique d'investissement = texte de la factsheet

- **Objectif** (demande de l'utilisatrice) : l'onglet « Politique d'investissement » de chaque fiche reprend littéralement le texte descriptif de la factsheet, aéré en paragraphes. Pas de factsheet ou pas de texte descriptif → on ne touche pas.
- **Décisions de l'utilisatrice** : factsheet FR → champ FR ; factsheet EN → champ EN (FR inchangé) ; autres langues (14 fiches : DE, SV, NL, ES, IT) non touchées ; reprendre objectif + politique/stratégie, jamais le commentaire du mois.
- **Méthode** : dernière factsheet en ligne de chaque fiche (440), extraction par 8 agents, contrôle automatique phrase par phrase contre le texte du PDF (403 textes), 6 textes de PDF mal codés vérifiés sur l'image. Libertés : découpe en paragraphes, lettres perdues par le PDF rétablies (ligatures, traits d'union).
- **Modifications du site (13/10/2026, ~12h55–13h30 UTC)** : 409 fiches — 283 champ FR, 126 champ EN. Relecture finale : 409/409 conformes (`docs/politiques-2026-10-13/verification.json`). Le site enregistre l'apostrophe droite en `&#39;` (identique à l'affichage).
- **Non modifiées (18)** : sans texte descriptif (8), factsheet d'une autre part (75, 116, 118, 119, 127, 444, 445), rapport annuel seulement (357, 384), phrase commune à la gamme Helium (261). Liste : `docs/politiques-2026-10-13/non-modifiees.json`.
- **Fichiers** : `docs/2026-10-13-politiques-investissement.xlsx` (avant / après), `docs/politiques-2026-10-13/` (JSON par fiche, journal, vérification). Consigne ajoutée au guide.

## Suite : recherche de factsheets pour 31 fiches (13/10/2026 après-midi)
- **Demande** : pour les 13 fiches à factsheet en langue étrangère et les 18 non touchées, chercher la factsheet du bon ISIN (FR de préférence, sinon EN) sur le site du gestionnaire, sinon Morningstar ; puis même traitement.
- **Trouvées et appliquées (7 fiches, ~15h UTC)** : 3 Amundi Income Opportunities (FR, 30/09/2026, amundi.com), 16 FvS Multiple Opportunities II (EN, champ EN, flossbachvonstorch.de), 23 PTAM Global Allocation (FR, ptam.de), 109 FvS Bond Opportunities (FR, flossbachvonstorch.de), 357 Norden (EN 08-2026, champ EN, lazardassetmanagement.com), 366 Pictet Clean Energy Transition (FR, fundinfo), 492 Pareto Småbolagsfond E (FR, paretoam.com). Textes contrôlés mot pour mot contre le PDF, relecture sur le site : 7/7 conformes. PDF rangés dans `INVESTLAW/<maison>/<ISIN>/` (non uploadés sur le site). Détail des recherches : `docs/politiques-2026-10-13/recherche/`.
- **Non trouvées (24)** :
  - pas de version FR/EN pour cette part : 110, 111 (FvS, allemand seulement), 318, 320, 321, 322 (Lannebo, suédois seulement ; EN arrêté fin 2024), 433 (CT, AEH seulement en italien), 458 (CPR A2 : dernière factsheet 06/2024) ;
  - le gestionnaire ne publie que la factsheet d'une autre part (texte du fonds identique) : 116, 118, 119 (Leleux, classes R), 444, 445 (Vector, C1), 75 (M&G, EUR S-H) ;
  - pas de factsheet publiée : 383 Protea, 384 Quest Cleantech, 417 Smart Value, 279 Carmignac Court Terme (seul un reporting hebdo sans texte), 127 MainFirst Megatrends Asia (fusionné le 01/10/2026 dans LAIQON SICAV, devenue part R USD) ;
  - factsheet conforme mais sans texte descriptif : 24 Lazard Patrimoine Croissance, 520 GemAsia, 521 GemEquity, 261 Helium Selection (phrase de gamme) ;
  - site inaccessible depuis l'environnement : 360 Omega (lazardfreresgestion.fr), et Morningstar (403) pour tous.

## Upload des factsheets conformes retrouvées (13/10/2026 ~15h30 UTC, demande de l'utilisatrice)
- Ajoutées : 357 Norden « Rapport de Gestion Août 2026 » (EN ; la fiche n'avait qu'un rapport annuel) ; 261 Helium Selection « Rapport de Gestion Août 2026 » (FR, plus récente que juillet EN).
- Remplacées (même mois, un seul rapport par mois) : septembre 2026 en espagnol/allemand/suédois remplacé par la version FR (3, 23, 109, 492) ou EN (16) ; 366 Pictet : le « Monthly Fund Insights » de septembre remplacé par la fiche technique mensuelle FR de septembre. Anciens fichiers supprimés après vérification que le nouveau était en ligne.
- Non envoyées : 24 (identique au rapport d'août déjà en ligne), 520 et 521 (août EN, plus ancien que le septembre FR déjà en ligne).
- Contrôle : les 8 PDF téléchargés depuis le site sont identiques aux fichiers source (md5). Journal : `docs/politiques-2026-10-13/upload-factsheets.log`.
- Morningstar : le site refuse les accès depuis l'environnement cloud (403 de sa protection anti-robots CloudFront/AWS WAF, y compris avec un vrai navigateur) ; la recherche Morningstar doit se faire à la main.

## Factsheets FR fournies par l'utilisatrice (Morningstar / Chrome)
- 110 FvS Dividend RT (LU2473801830) et 111 FvS Global Quality RT (LU2673417882) : factsheets FR du 30/09/2026 (générées par FactsheetsLIVE pour Flossbach von Storch), ISIN et part RT vérifiés. Mises en ligne en remplacement du septembre en allemand, politique d'investissement FR reprise telle quelle (phrases prospectus, distribution, SFDR exclues comme pour 109). Vérifié : PDF identique en ligne, politique conforme.
- Les autres fonds de la liste (360, 458, 433, Lannebo 318/320/321/322) : rien trouvé par l'utilisatrice non plus.
