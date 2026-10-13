# 2026-10-13 — Création des benchmarks manquants (Noa)

- **Objectif** : créer dans la liste du site les indices de référence cités par les factsheets mais absents, et les rattacher aux fiches.
- **Modifications du site (13/10/2026, ~08h55-09h00 UTC)** :
  - 55 indices créés (`POST /api/benchmarks`, ids 176 et suivants), codes mnémoniques (même convention que les indices créés le même jour par Louis) ;
  - 59 fiches rattachées à leur indice, vérifiées une par une (dont 6, 44, 67, 505 qui avaient un indice faux : S&P500 ou €STR) ;
  - libellé de l'indice 39 corrigé (tronqué : « … MSCI France » → « 10% €STR + 8,5 bp + 90% MSCI France Smid Cap Loc Net »), utilisé uniquement par la fiche 132.
- **Écartés** (indice non établi clairement par la factsheet) : 236 (deux indices cités), 332 (trois indices selon les usages), 406 (devise non précisée), 434 (objectif de gestion, pas un indice).
- **Contrôles** : chaque libellé retrouvé dans le texte de la factsheet du fonds ; aucun code ni nom déjà présent ; indices identiques regroupés (BGF Gold, Mining, Global Allocation ; Carnegie Small Cap).
- **Fichiers** : `docs/benchmarks-2026-10-13/` (plan avec ids créés, un JSON par fiche, journal d'application).
- **Page d'audit** recalculée sur le site (13/10/2026 09h02 UTC) : 228 fiches complètes, 199 presque complètes, 21 incomplètes, 13 quasi vides ; benchmark vide sur 93 fiches (148 avant). https://claude.ai/artifact/GfTSsC7oUyEeoruciDXX3J
