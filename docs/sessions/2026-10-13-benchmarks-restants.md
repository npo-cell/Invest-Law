# 2026-10-13 — Benchmarks des fiches restantes

- **Objectif** : compléter le benchmark des fiches qui n'en ont pas (105 selon l'API, 93 selon l'audit).
- **Méthode** : texte de chaque factsheet locale / rapport publié (80 fiches), indice retenu seulement s'il est présenté comme indice de référence du fonds, avec citation.
- **Décision de l'utilisatrice** : fonds sans indice → champ laissé vide (pas « n/a »).
- **Modifications du site (13/10/2026 ~09h40 UTC)** : benchmark 231 créé (`BGF-ESGMA-COMPOSITE`) ; fiche 13 → 231 ; fiche 245 → 49. Relecture : aucun écart. 103 fiches restent sans benchmark.
- **Non appliqué, à trancher** : 26 et 515 (First Eagle, « Indice de référence : Aucun » mais comparatif SOFR + 430 bp), 273 et 319 (Carmignac, composite cité seulement en ESG), 402, 267 ; 236/332/406/434 laissés comme décidé par Noa.
- **Fichiers** : `docs/benchmarks-2026-10-13-complement/` (analyse par fiche, JSON appliqués).
- **Retour arrière (~09h35 UTC)** : sur consigne de l'utilisatrice (« si c'est ambigu, ne mets pas, ou demande »), fiches 13 et 245 remises à vide (relecture : aucun écart). Benchmark 231 inutilisé, non supprimable par l'API. 105 fiches sans benchmark. Consigne ajoutée au skill `invest-law`.
- **Page d'audit recalculée** (13/10/2026 09h40 UTC, données du site) : 461 fiches externes, 228 complètes, 199 presque complètes, 21 incomplètes, 13 quasi vides ; champs vides : frais de gestion 105, benchmark 93, gérant 79, TER 48, encours 39, date de création 32, devise 12. Identique au calcul de 09h02 fiche par fiche. Ligne ajoutée dans « Ce qui a été fait » (105 fiches sans indice relues). https://claude.ai/artifact/GfTSsC7oUyEeoruciDXX3J
