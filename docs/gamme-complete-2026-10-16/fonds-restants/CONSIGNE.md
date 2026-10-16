# Consigne : les 53 fonds de la gamme One Life sans fiche (16/10/2026)

Demande de l'utilisatrice (16/10/2026) : pour les 53 fonds de `../fonds-non-couverts.csv` (ni sur invest-law.eu, ni dans Wealth Belgium), trouver factsheet + KID puis préparer la fiche, comme pour Wealth Belgium. **Rien n'est mis sur invest-law.eu.**

## Règles (reprises telles quelles)
- Recherche des documents : `docs/wealth-belgium-2026-10-15/CONSIGNE-recherche.md` (exactitude avant tout, FR d'abord sinon EN, jamais une autre langue, ISIN exact de la part, sources gestionnaire > fundinfo > Morningstar, FIC : recherche rapide).
- Préparation des fiches : `docs/wealth-belgium-2026-10-15/CONSIGNE-fiches.md` (mêmes champs, mêmes règles, classification par jugement, catégorie vide).
- Ici, les parts sont souvent des parts « retail » de la gamme classique : le document doit porter exactement l'ISIN de la ligne.
- Un PDF déjà présent dans `INVESTLAW/` pour l'ISIN peut être réutilisé s'il est conforme ; chercher quand même une version plus récente.

## Fichiers
- Entrées / résultats par lot : `recherche/lot-0X-entree.json`, `recherche/lot-0X-resultat.json` (même format que Wealth Belgium).
- Fiches : `fiches/<ISIN>.json`, mêmes clés que `docs/wealth-belgium-2026-10-15/fiches/*.json`, plus `factsheet_fichier` et `kid_fichier` (chemins des PDF utilisés, vides si aucun).
- Contrôle obligatoire après chaque fiche : `python3 -I docs/gamme-complete-2026-10-16/fonds-restants/verif_fiche.py <ISIN>` jusqu'à 0 écart (ou écart expliqué en remarque : artefact d'extraction).
