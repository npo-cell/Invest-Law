# 13/10/2026 — Partage en direct : fusion automatique

## Objectif
Permettre à Louis et Noa de travailler en même temps et de voir le travail de l'autre sans action manuelle.

## Décisions
- Fusion automatique vers la branche par défaut (`claude/kind-edison-2o3dsu`) sans relecture humaine, demandée explicitement par Louis.
- Chaque session fusionne elle-même après chaque étape notable et en fin de tâche ; elle intègre d'abord la branche par défaut à jour pour éviter les conflits.
- Rappel : les modifications du site invest-law.eu sont visibles immédiatement ; les artéfacts restent privés tant que leur lien n'est pas partagé (le noter ici).

## Fichiers modifiés
- `AGENTS.md` (règles de partage)
