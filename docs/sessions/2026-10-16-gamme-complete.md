# 2026-10-16 — Gamme One Life complète : combien de fonds déjà faits

- **Source** : `FundsRange2026-10-16.xlsx` (export One Life fourni par l'utilisatrice, copié dans `docs/gamme-complete-2026-10-16/`) : 863 lignes, **852 ISIN uniques** (11 BGF en double).
- **Comparé à** : les 488 fiches d'invest-law.eu (API, 16/10 ~07h UTC) et les 347 fonds Wealth Belgium (`docs/wealth-belgium-2026-10-15/fonds-isin.csv`), par ISIN.
- **Résultat : 799 / 852 fonds faits (94 %)**
  - 463 déjà sur invest-law.eu (dont 11 sont aussi dans Wealth Belgium) ;
  - 336 préparés dans le Google Sheet Wealth Belgium, pas encore sur le site ;
  - **53 ni l'un ni l'autre** (`fonds-non-couverts.csv`) : 21 fonds internes FIC, 25 flexibles, 17 actions, 8 obligations, 3 monétaires ; 22 étaient déjà dans la gamme du 12/10 (factsheet introuvable à l'époque), 31 sont nouveaux.
- Autres constats : les 347 Wealth Belgium sont tous dans la gamme ; 25 fiches du site ne sont plus dans la gamme.
- Script : `docs/gamme-complete-2026-10-16/comparer.py`. Rien modifié sur le site.
