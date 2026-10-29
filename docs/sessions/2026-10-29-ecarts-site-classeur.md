# 2026-10-29 — Écarts invest-law.eu ↔ classeur « Gamme One Life complète »

- **Demande** : après l'avis de l'extension Chrome sur la qualité des données du site, lister les écarts entre le site et le Google Sheet.
- **Fait** : connexion au site (code Gmail mis à la corbeille), lecture seule de `GET /api/funds` (488 fiches), comparaison champ par champ avec l'onglet Fiches. Rien modifié sur invest-law.eu ni dans le Sheet.
- **Résultat** : 463 fiches comparées, 78 identiques, 385 avec écarts (2 984 écarts : 1 853 à corriger, 556 à remplir, 575 à vider) ; 25 fiches hors classeur, 16 ISIN invalides, 167 fiches sans classification, 74 sans SRI, 3 classifications contraires au risque. Détail et décisions à prendre : `docs/ecarts-site-2026-10-29/README.md`.
- **Fichiers** : `docs/ecarts-site-2026-10-29/ecarts-site-classeur.xlsx`, `comparer.py`, `ecarts-site-classeur.json`. La copie brute de l'API n'est pas versionnée (elle contient les e-mails des maisons).
