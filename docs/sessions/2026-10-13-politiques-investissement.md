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
