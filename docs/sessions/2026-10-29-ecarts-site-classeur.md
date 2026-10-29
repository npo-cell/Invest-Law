# 2026-10-29 — Écarts invest-law.eu ↔ classeur « Gamme One Life complète »

- **Demande** : après l'avis de l'extension Chrome sur la qualité des données du site, lister les écarts entre le site et le Google Sheet.
- **Fait** : connexion au site (code Gmail mis à la corbeille), lecture seule de `GET /api/funds` (488 fiches), comparaison champ par champ avec l'onglet Fiches. Rien modifié sur invest-law.eu ni dans le Sheet.
- **Résultat** : 463 fiches comparées, 78 identiques, 385 avec écarts (2 984 écarts : 1 853 à corriger, 556 à remplir, 575 à vider) ; 25 fiches hors classeur, 16 ISIN invalides, 167 fiches sans classification, 74 sans SRI, 3 classifications contraires au risque. Détail et décisions à prendre : `docs/ecarts-site-2026-10-29/README.md`.
- **Fichiers** : `docs/ecarts-site-2026-10-29/ecarts-site-classeur.xlsx`, `comparer.py`, `ecarts-site-classeur.json`. La copie brute de l'API n'est pas versionnée (elle contient les e-mails des maisons).

## Report des valeurs sur invest-law.eu (29/10/2026)
- Plan : `docs/report-valeurs-2026-10-29/` (`plan.py`, `corps/<FundId>.json`, `plan-report-valeurs.xlsx`) : 622 valeurs sur 323 fiches — encours, classification, frais courants, frais de gestion, SRI, qualité des émetteurs, date de création, devise, catégorie ; seulement « à corriger » et « à remplir » (rien n'est vidé). Hors de cette passe : indice (identifiant de benchmark), SFDR et % durable (champs ESG / ESG_code du site au sens ambigu), duration (unités et « sensibilité »), gérants et textes.
- Écartées (nom ≠ ISIN sur le site, à trancher) : fiche 9 « ALLIANZ STRATEGY 50 NT EUR » avec l'ISIN LU1093406186 (Allianz Dynamic Multi Asset Strat SRI 50 AT) ; fiche 401 « ROCHE-BRUNE ZONE EURO ACTIONS P » avec l'ISIN FR0010283838 (Stratégie Euro Div Responsables P).
- **Modifié sur le site le 29/10/2026** (lot 1, accord de l'utilisatrice pour 10 fiches) : fiches 1, 3, 4, 5, 6, 11, 12, 13, 14, 15 ; PUT 200 et relecture conforme pour chacune, aucun autre champ modifié. Détail ancien → nouveau : `docs/report-valeurs-2026-10-29/journal.txt`.
