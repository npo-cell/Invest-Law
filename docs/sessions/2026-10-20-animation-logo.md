# 2026-10-20 — Animation d'apparition du logo

**Objectif** : créer une animation d'apparition du logo Invest Law.

**Décisions**
- Logo redessiné en SVG vectoriel à partir de l'image fournie (géométrie relevée au pixel ; couleurs #60A0BE, #425262, fond #EFF1F4). Texte en Montserrat 400, ajusté à la largeur d'origine (`textLength`).
- Séquence (1,9 s) : chevron bleu en diagonale depuis le haut, pièce ardoise depuis le bas, léger resserrement au contact, puis INVEST et LAW dévoilés de gauche à droite. Pur CSS, sans JavaScript ; `prefers-reduced-motion` affiche le logo fixe.
- Variable CSS `--k` sur le `<svg>` pour multiplier les durées (ralenti).

**Fichiers**
- `docs/logo/invest-law-logo-anime.svg` — SVG animé autonome (utilisable sur le site). La police Montserrat n'est chargée que si le SVG est intégré en ligne ou ouvert directement ; en `<img>`, police de repli.
- `docs/logo/2026-10-20-animation-logo.html` — page de démonstration (Rejouer, ralenti ×3).

**Liens**
- Artéfact : https://claude.ai/artifact/5iVMPkqiapFZ4ZCbiDz8Ai (privé, à partager depuis le menu Partager)
