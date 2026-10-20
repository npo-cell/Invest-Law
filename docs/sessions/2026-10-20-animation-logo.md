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

## Mise à jour — version « spectaculaire »
- `docs/logo/invest-law-logo-anime-v2.svg` (3,2 s) : tracé au trait des deux pièces, emboîtement avec impact et deux ondes, remplissage, lettres une à une avec rebond, reflet final. Classes préfixées `il2-` pour coexister avec la v1 dans une même page. Positions des lettres relevées sur Montserrat (étirement horizontal ×1,083 pour INVEST, comme le logo).
- La page de démo propose les deux versions (Spectaculaire par défaut / Sobre) ; même lien d'artéfact, version 2.
