# Consigne : recherche factsheet + KID, gamme Wealth Belgium (15/10/2026)

Demande de l'utilisatrice (15/10/2026) : pour chacun des 347 fonds de `fonds-isin.csv`, trouver **la factsheet la plus récente** et **le KID**, les ranger dans le dépôt et tenir à jour le Google Sheet (colonnes « Factsheet » et « KID » : `Trouvé` / `Non trouvé`).

## Règles
- **Exactitude avant tout** : seulement des documents vrais, venant de sources fiables, avec **le bon ISIN**. Un document non trouvé n'est pas grave : on le note « Non trouvé ». Jamais de document approximatif.
- **Langue** : français d'abord ; s'il n'existe pas en français, anglais. Éviter toute autre langue (si seule une autre langue existe → « Non trouvé », avec une note).
- **Parts institutionnelles** : la gamme Wealth Belgium utilise des parts institutionnelles (frais plus bas) des mêmes fonds que la gamme One Life classique. Les ISIN sont donc différents : le document doit porter **exactement l'ISIN de la ligne**, jamais celui d'une autre part du même fonds.
- **Factsheet** = reporting mensuel (ou trimestriel s'il n'y a que ça) le plus récent : en octobre 2026, normalement fin septembre 2026, à défaut fin août. Pour un fonds multi-parts, la factsheet peut lister plusieurs ISIN : accepté si l'ISIN de la ligne y figure **et** que la factsheet n'est pas celle d'une autre part (les performances/frais affichés doivent être ceux de notre part, ou la factsheet couvre explicitement toutes les parts).
- **KID** = document d'informations clés PRIIPs (« Document d'informations clés », « Key Information Document »). Version la plus récente. Pour la Belgique / le Luxembourg de préférence en français. L'ISIN de la part doit figurer dans le KID.
- **Sources**, par ordre : site du gestionnaire (ou de sa société de gestion), puis fundinfo, puis Morningstar (doc.morningstar.com). Jamais un site tiers qui recopie le document.
- **Fonds FIC (ISIN `XFCS…`)** : fonds internes d'assurance, documents rarement publics. Une recherche rapide suffit ; sinon « Non trouvé ».

## Rangement (mémoire du dépôt)
- PDF : `INVESTLAW/<MAISON>/<ISIN>/<ISIN>__Factsheet_<FR|EN>_<AAAA-MM-JJ>.pdf` et `<ISIN>__KID_<FR|EN>_<AAAA-MM-JJ>.pdf` (date = date du document).
- À côté de chaque PDF, son texte extrait (`pdftotext -layout`) : même nom en `.txt`, pour retrouver les informations sans rouvrir les PDF.
- Résultats par lot : `docs/wealth-belgium-2026-10-15/recherche/lot-XX-resultat.json` (statut, fichier, URL source, date, langue, ISIN vérifié, notes).
