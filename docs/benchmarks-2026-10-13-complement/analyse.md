# Benchmarks restants — analyse du 13/10/2026

105 fiches sans benchmark (`GET /api/funds`, 13/10/2026 ~09h20 UTC). Texte lu : factsheet locale (`INVESTLAW/`) ou rapport publié sur la fiche. Décision de l'utilisatrice : fonds sans indice → champ laissé vide (pas de rattachement à « n/a », id 51).

## Appliqué puis retiré (13/10/2026 ~09h35 UTC, décision de l'utilisatrice : ambigu → on ne met pas)
- 245 BL-Global 30 → 49 « Lipper Global Mixed Asset EUR Balanced - Global » (« Reference Index » de la factsheet).
- 13 BGF ESG Multi-Asset → 231 (créé, code `BGF-ESGMA-COMPOSITE`) « 25% MSCI World Index hedged to EUR, 25% MSCI World Index, 50% Bloomberg Global Aggregate Bond Index hedged to EUR » (« indice di riferimento composito », factsheet IT 31/08/2026) — indice « ai fini della gestione del rischio ».
- 245 : Lipper cité « for comparison purposes only », fonds « not managed by reference to a benchmark index ».
- Les deux fiches sont revenues à vide. Le benchmark 231 reste dans la liste, inutilisé : l'API ne permet pas de le supprimer (`DELETE /api/benchmarks/231` → 404).

## Indice cité mais non appliqué (à trancher)
- 26 First Eagle AU-C USD : « Indice de référence : Aucun », mais indice comparatif « SOFR + 430 basis points ». 515 (part AHE-C EUR) : idem, « CAPITALIZED US SOFR + 4.3% (BASE 365) ».
- 273 Carmignac Absolute Return Europe, 319 Carmignac Ptf Long-Short European Eq : « 75% MSCI Europe index + 25% S&P 500 » cité seulement dans la partie ESG/carbone.
- 402 Sapienta Absolu : contradiction (€STR capitalisé +1,85 % / +1 %).
- 267 IFP Global Age : « MSCI World in EUR » dans l'objectif, factsheet de 2020.
- 236, 332, 406, 434 : déjà écartés par Noa le 13/10 (voir `docs/sessions/2026-10-13-benchmarks.md`), laissés tels quels. Pour 434, la factsheet dit « €STR + 38,5 points de base … cet indice est utilisé exclusivement en tant qu'indicateur de performance ex post ».

## Absence d'indice écrite dans le document (laissé vide)
1, 16, 27, 29, 74, 109, 110, 120, 122, 305, 340, 358, 361, 363, 364, 365, 383, 389, 392, 393, 394, 424, 462, 469, 473, 475, 476, 477, 478, 486, 493, 494.

## Rien dans le document (ni indice, ni absence explicite) — laissé vide
116, 117, 118, 119, 139, 208, 210, 211, 262, 278, 282, 283, 291, 314, 315, 325, 338, 339, 343, 345, 384, 403, 410, 417, 422, 448, 481, 487, 495, 501, 506, 508, 509, 510, 536.

## Aucun document disponible (ni local, ni sur la fiche) — laissé vide
108, 171, 172, 173, 178, 191, 192, 193, 216, 217, 259, 335, 344, 373, 418, 419, 420, 425, 446, 454, 479, 496, 530, 531, 539.
