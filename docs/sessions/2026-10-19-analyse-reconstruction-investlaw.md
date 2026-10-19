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

## Mise à jour du prompt (même jour)

Précisions de l'utilisatrice et changements apportés au prompt :
- **Infrastructure** : code sur **GitHub**, qui reste le seul chemin vers la production ; application sur **Vercel** ; base de données, authentification et fichiers sur **Supabase**. Cela s'est traduit par :
  - Supabase Auth avec MFA ;
  - RLS sur toutes les tables ;
  - Storage privé ;
  - migrations versionnées appliquées par GitHub Actions ;
  - projets `prod` et `staging` à Francfort ;
  - plans Pro de Vercel et de Supabase.
- **« Tout contrôler »** signifie avoir accès au compte Data, au compte gestionnaire (Responsable) et au compte mère. Ajouts :
  - **dans le prompt**, une section 3 bis sur les trois niveaux d'accès : comptes d'infrastructure, rôle Administrateur, jetons d'API. Elle comprend le mode « Voir comme », l'impossibilité de supprimer le dernier Administrateur, une procédure de secours et le fichier `docs/ACCES.md` ;
  - **dans l'analyse**, une section 7 qui liste les accès à demander dès maintenant au développeur sur le site actuel : compte Responsable, droits du compte mère (aujourd'hui liés à son email dans le code), accès propriétaire à l'infrastructure, export complet.

## Prompt « page blanche » (même jour)

- **Demande** : un second prompt, écrit comme si l'on partait de zéro. Il ne mentionne ni le site actuel, ni la migration, ni les détails techniques (« comment faire »), mais il doit aboutir à une plateforme très proche d'invest-law.
- **Fichier** : `docs/livrables/2026-10-19-prompt-creation-plateforme.md`.
- **Contenu** :
  - vision, rôles et trois niveaux d'accès, menu et charte graphique ;
  - fonctions détaillées : fonds, sélection et simulateur, fiche à 5 onglets, maisons, banques, actualités, documentation, arbre LAW, simulation fiscale, outils intégrés, administration ;
  - qualité attendue.
  - Seules contraintes techniques indiquées : GitHub, Vercel et Supabase.
- Le prompt détaillé (`2026-10-19-prompt-reconstruction-investlaw.md`) reste disponible si l'on veut migrer les données ou garder l'API existante.
