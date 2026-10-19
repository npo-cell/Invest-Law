# 2026-10-19 — Analyse complète d'invest-law.eu et prompt de reconstruction

- **Demande** : analyser tout le site et écrire un prompt qui fasse reconstruire par Claude, de A à Z, une plateforme équivalente. Précision de l'utilisatrice : le but est de **ne plus dépendre du développeur**, pas un contrôle personnel.
- **Méthode** : connexion avec le compte Data (code Gmail mis à la corbeille ensuite), puis téléchargement en lecture seule des 37 fichiers du front-end (HTML, JS, CSS) et des traductions. Lecture intégrale de ces fichiers par deux sous-agents. Relevé des volumes et des formats renvoyés par l'API. Recensement des blocages « développeur » cités dans `docs/sessions/`. **Rien n'a été modifié sur le site.**
- **Livrables** :
  - `docs/analyses/2026-10-19-analyse-complete-investlaw.md` : fonctions, architecture, volumes, dépendances au développeur, défauts, et vérifications contractuelles à faire d'abord (domaine, hébergement, propriété du code, export des données) ;
  - `docs/livrables/2026-10-19-prompt-reconstruction-investlaw.md` : prompt à coller dans une session Claude Code ouverte sur un nouveau dépôt de l'organisation. Il comprend :
    - 11 phases, chacune avec ses critères de validation ;
    - l'annexe B : cahier des charges complet, avec les formules, les droits, l'arbre décisionnel et l'API à conserver ;
    - l'annexe C : les défauts à corriger.
- **Décisions prises dans le prompt** :
  - comptes au nom de la société, avec 2 administrateurs ;
  - pile standard : TypeScript, Next.js, PostgreSQL, stockage S3 privé, Docker, hébergement dans l'UE ;
  - permissions configurables, sans aucun email codé en dur ;
  - API actuelle conservée pour que `tools/*.py` et les routines continuent de fonctionner ;
  - jetons d'API pour les routines ;
  - export complet des données ;
  - RUNBOOK et guides d'administration ;
  - migration idempotente des données.
- **À faire par l'équipe** : vérifier le contrat avec le développeur (point 6 de l'analyse) avant de lancer la reconstruction.
