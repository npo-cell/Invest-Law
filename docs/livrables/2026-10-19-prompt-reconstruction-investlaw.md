# Prompt : reconstruire une plateforme équivalente à invest-law.eu, possédée et maintenue par l'organisation

**Infrastructure retenue** : code sur **GitHub** (seul chemin vers la production), application hébergée sur **Vercel**, base de données, authentification et fichiers sur **Supabase**.

**Mode d'emploi.**
1. Créer l'organisation GitHub, l'équipe Vercel et l'organisation Supabase, en étant Owner des trois (voir section 3).
2. Créer un dépôt GitHub **vide** dans l'organisation (pas sur un compte personnel ni sur celui d'un prestataire).
3. Ouvrir une session Claude Code sur ce dépôt et coller tout ce document, de « DÉBUT DU PROMPT » à « FIN DU PROMPT ». Le travail se fait en plusieurs sessions : chacune relit `PLAN.md` et reprend à la phase en cours.

Analyse dont découle ce prompt : `docs/analyses/2026-10-19-analyse-complete-investlaw.md`.

---

## DÉBUT DU PROMPT

### 1. Mission

Tu vas construire, de A à Z, une plateforme web B2B qui reproduit **toutes les fonctionnalités** du site actuel invest-law.eu (cahier des charges complet en annexe B), en corrigeant ses défauts connus (annexe C).

Le but premier est l'**indépendance**. Aujourd'hui, toute correction, tout réglage et toute publication passent par un développeur externe. Demain, l'organisation doit :

- **posséder** tout : code, comptes, domaine, hébergement, données, sauvegardes ;
- **régler elle-même**, depuis un écran d'administration et sans toucher au code, tout ce qui relève du paramétrage : droits, textes, URL, modèles d'email, listes de valeurs ;
- **faire évoluer et réparer** le site avec Claude Code, grâce à un code simple, standard, testé et documenté. N'importe quel développeur, ou Claude, doit pouvoir le reprendre en une heure de lecture.

Chaque fois que tu hésites entre deux solutions, choisis celle qui réduit la dépendance à une personne ou à un fournisseur unique : technologies standard, données exportables, rien de magique, tout écrit dans le dépôt.

Tu travailles pour l'organisation, pas pour une personne en particulier. Aucun compte, secret ou droit ne doit dépendre d'un seul individu.

**Infrastructure imposée** :
- **GitHub** : code, historique, intégration continue ;
- **Vercel** : hébergement de l'application (pages et routes `/api`), déploiement automatique depuis GitHub ;
- **Supabase** : base PostgreSQL, authentification, stockage des fichiers, tâches planifiées.

**Accès complet de la personne qui pilote le projet.** Elle doit détenir, à son nom ou à celui de l'organisation dont elle est administratrice, les trois niveaux d'accès décrits en section 3 bis :
- le **compte mère**, qui a accès à tout ;
- un compte **gestionnaire** (Responsable) ;
- un compte **Data**.

Rien ne doit pouvoir être fait sur le site, ni sur son infrastructure, sans qu'elle puisse le faire aussi.

### 2. Règles de travail (valables pour toute la durée du projet)

1. **Langue** : documentation, interface par défaut, messages de commit et échanges avec moi en français. Code et identifiants en anglais.
2. **Plan vivant** : crée `PLAN.md` à la racine (phases ci-dessous, avec cases à cocher) et tiens-le à jour à chaque fin d'étape. Au début de chaque session, lis `PLAN.md`, `CLAUDE.md` et `docs/decisions/` avant d'agir.
3. **Décisions** : chaque choix structurant (technologie, hébergeur, modèle de données, formule de calcul) fait l'objet d'une courte note `docs/decisions/NNNN-titre.md` : contexte, options, choix, conséquences.
4. **Petits pas vérifiés** : une fonctionnalité à la fois, avec ses tests. Un commit par étape cohérente, push, puis demande de fusion vers la branche principale une fois les tests au vert.
5. **Me demander avant** :
   - toute action irréversible ou visible de l'extérieur : DNS, envoi d'emails réels, suppression de données, mise en production, achat ;
   - toute création de compte chez un fournisseur. C'est moi qui crée les comptes, au nom de l'organisation ; tu me dis lesquels et pourquoi.
6. **Secrets** : jamais dans le dépôt, le chat ou les logs. Fichier `.env.example` documenté ; vraies valeurs dans les variables d'environnement Vercel, les secrets Supabase et GitHub Actions, et dans le coffre de mots de passe de l'organisation.
7. **Pas de dépendance exotique** : uniquement des librairies largement utilisées et maintenues, versions épinglées, mises à jour automatiques proposées (Dependabot ou Renovate).
8. **Exactitude des données** : ne jamais inventer ni compléter une donnée financière. Mieux vaut un champ vide qu'une valeur fausse.
9. **Quand tu bloques**, dis-le clairement avec ce qu'il te faut, au lieu de contourner en silence.

### 3. Phase 0 : prérequis de propriété (avant toute ligne de code)

Produis `docs/00-prerequis-comptes.md`, une liste à cocher de ce que l'organisation doit détenir. Pour chaque ligne : titulaire (la société), au moins **2 administrateurs** de l'organisation, facturation au nom de la société, et accès rangé dans le coffre de mots de passe partagé.

| Élément | Exigence |
|---|---|
| Organisation GitHub | Je suis **propriétaire (Owner)** de l'organisation, plus un second propriétaire de confiance ; double authentification obligatoire ; dépôt privé ; branche principale protégée. **GitHub est le seul chemin vers la production** (voir section 4) |
| Organisation Supabase | Je suis **Owner** de l'organisation Supabase, plus un second Owner ; double authentification. **Plan Pro au minimum** : le plan gratuit met le projet en pause après une semaine d'inactivité et n'a pas de sauvegardes. Deux projets, `prod` et `staging`, en région **Frankfurt (eu-central-1)** pour le RGPD |
| Équipe Vercel | Je suis **Owner** de l'équipe Vercel de la société, avec double authentification. **Plan Pro** : l'usage commercial est interdit sur le plan gratuit (Hobby). Projet relié au dépôt GitHub, région des fonctions **Frankfurt (fra1)**, au plus près de la base Supabase. Intégration officielle Vercel ↔ Supabase pour les variables d'environnement |
| Nom de domaine | Titulaire = la société (vérifier au registre EURid), compte du registrar à mon nom ou à celui de la société ; DNS accessible |
| Envoi d'emails | Fournisseur SMTP de la société (Resend, Brevo, Postmark…) branché sur Supabase Auth (« Custom SMTP ») et sur les fonctions. L'envoi intégré de Supabase est limité et réservé aux tests. Domaine vérifié : SPF, DKIM, DMARC |
| Coffre de mots de passe partagé | Bitwarden, 1Password ou équivalent, dont je suis administratrice |
| Clé API de traduction | Pour la traduction automatique FR/EN/NL : clé de la société, rangée dans les secrets Supabase |
| Supervision | Disponibilité et erreurs ; alertes vers une adresse partagée et vers moi |

Avant d'écrire du code, **vérifie dans les documentations officielles de Supabase et de Vercel** (supabase.com/docs, vercel.com/docs) l'état actuel des fonctions dont tu dépends :
- **Supabase** : MFA, Auth Hooks, SMTP personnalisé, Storage, pg_cron, branching, sauvegardes et PITR, prix ;
- **Vercel** : limites de durée et de taille des fonctions, Cron Jobs, intégration Supabase, prix.

Ce que tu sais peut être dépassé. Note ce que tu as vérifié, avec la date, dans `docs/decisions/0001-vercel-supabase.md`.

Pose-moi ensuite ces questions, une fois, et note les réponses dans `docs/decisions/` :

1. Le domaine pointe-t-il vers Vercel (recommandé) ? Qui a accès au DNS ?
2. A-t-on obtenu du développeur actuel un export de la base et des fichiers ? Sinon, la migration se fera par l'API du site actuel (phase 9).
3. Nom de domaine de recette (ex. `beta.<domaine>`) et date visée pour la bascule.
4. Le Portfolio Builder (pb.invest-law.eu) reste-t-il une application externe, intégrée par URL configurable, ou est-il reconstruit plus tard ? Par défaut : URL configurable, et une phase ultérieure facultative.
5. Les adresses email des 3 comptes de la section 3 bis : compte mère, gestionnaire, Data.

### 3 bis. Les trois niveaux d'accès (exigence centrale)

Il y a trois niveaux. Le site doit les distinguer clairement, et les documenter dans `docs/ACCES.md` : qui détient quoi, comment le récupérer, comment le transmettre.

**Niveau 1 : comptes d'infrastructure (le vrai « compte mère »).** Owner de l'organisation GitHub, Owner de l'équipe Vercel, Owner de l'organisation Supabase, compte du registrar du domaine, compte du fournisseur d'emails. Qui les détient peut tout faire, y compris lire et restaurer la base. Au moins 2 personnes de l'organisation, dont moi. **Jamais** de compte au nom d'un prestataire ; un prestataire reçoit au plus un accès « membre » révocable.

**Niveau 2 : rôles dans le site.**

| Rôle | Pour qui | Droits |
|---|---|---|
| **Administrateur** (compte mère applicatif) | moi + 1 suppléant | **toutes** les permissions, y compris : gérer tous les utilisateurs et tous les rôles, modifier la matrice des permissions, paramètres, modèles d'emails, journal d'audit, export complet, publication des nouvelles, documentation, jetons d'API. Ce rôle remplace le super-administrateur codé en dur de l'ancien site |
| **Responsable** (gestionnaire) | direction, équipe commerciale | admin des utilisateurs Courtier et Maison, activité et relances, import VNI, tout le contenu ; pas la matrice des permissions ni l'export complet, sauf si l'Administrateur les lui donne |
| **Data** | équipe données | fonds, VNI, rapports, benchmarks, maisons, banques, commentaires, nouvelles, documentation |
| **Maison** | une maison de gestion | sa fiche, ses fonds, ses nouvelles (soumises à validation) |
| **Courtier** | clients | lecture, sa sélection, ses simulations |

**Garde-fous du rôle Administrateur :**
- Le site refuse de retirer ou désactiver le **dernier** Administrateur.
- La double authentification est **obligatoire** pour les rôles Administrateur et Responsable.
- Une procédure de secours écrite dans `docs/ACCES.md` permet, depuis le tableau de bord Supabase (niveau 1), de redonner le rôle Administrateur à un compte. Elle sert si tous les Administrateurs ont perdu leur accès.

**Mode « Voir comme ».** Un Administrateur peut voir le site exactement comme un utilisateur ou un rôle donné, **en lecture seule** et tracé dans le journal d'audit. Cela permet de vérifier ce que voit un gestionnaire, une Maison ou un Courtier sans emprunter son mot de passe.

**Niveau 3 : comptes d'automatisation.** Les jetons d'API (routines Claude, scripts) appartiennent à un utilisateur et ont un sous-ensemble de ses droits. Exemple : un jeton « routine VNI » limité à `nav.import`. Ils sont créés, listés et révoqués par l'Administrateur.

Dès la phase 2, crée mes 3 comptes de test : Administrateur, Responsable et Data. Je dois pouvoir me connecter avec chacun et constater la différence.

### 4. Choix techniques imposés (sauf objection argumentée de ta part)

- **Un seul dépôt, un seul langage** : TypeScript partout.
- **Tout passe par GitHub.** Aucun déploiement depuis un poste (`vercel deploy` interdit), aucune modification de schéma dans le tableau de bord Supabase.
  - Vercel est relié au dépôt : chaque demande de fusion produit un aperçu ; la fusion dans `staging` met à jour la recette ; la fusion dans `main` met à jour la production.
  - Les migrations Supabase et les autres déploiements sont lancés par GitHub Actions.
  - Revenir en arrière = revenir à un commit précédent dans GitHub, ou utiliser « Instant Rollback » dans Vercel, puis le noter dans le dépôt.
- **Application** : Next.js (App Router), hébergée sur **Vercel**. Les routes API JSON sont sous `/api`, sur le même domaine que le site : la compatibilité avec l'ancienne API reste donc possible. Interface en React + Tailwind CSS ; composants accessibles (shadcn/ui ou équivalent).
- **Graphiques** : une librairie standard (Recharts ou ECharts), pas de SVG fait à la main.
- **Base de données : Supabase PostgreSQL.**
  - Schéma géré **uniquement** par des migrations SQL versionnées dans `supabase/migrations/` (Supabase CLI). **Aucune modification de schéma à la main** dans le tableau de bord : tout ce qui n'est pas dans le dépôt n'existe pas.
  - Accès aux données côté serveur : client Supabase, ou un ORM typé (Drizzle) branché sur la base Supabase. Choisis, et écris ton choix dans une note de décision.
  - Toutes les dates métier (VNI, rapports, création) en type `date`, **jamais en timestamp** : c'est la cause probable du décalage d'un jour sur l'ancien site.
- **Droits : double protection.**
  1. Contrôle des permissions dans chaque route `/api` (middleware commun).
  2. **Row Level Security (RLS) activée sur toutes les tables**, avec des politiques qui reflètent la matrice des permissions. Même une requête directe à Supabase avec la clé publique ne voit que ce qu'elle a le droit de voir.
  - La clé `service_role` (qui contourne la RLS) n'est utilisée que côté serveur, jamais exposée au navigateur, et seulement là où c'est justifié et commenté.
  - Tests automatiques des politiques RLS pour chaque rôle.
- **Fichiers : Supabase Storage**, buckets **privés** (rapports, documents de banque, logos, avatars, images des nouvelles). Téléchargement par URL signées de courte durée, générées après contrôle des droits. Plus d'images en base64 en base.
- **Authentification : Supabase Auth**, sans recoder un système maison.
  - Email + mot de passe (12 caractères au moins), invitations, mot de passe oublié, changement d'email.
  - Deuxième facteur : **MFA par application d'authentification (TOTP)**, native dans Supabase, obligatoire pour Administrateur et Responsable, proposée aux autres. Si l'équipe préfère garder le code à 6 chiffres par email comme sur l'ancien site, vérifie ce que Supabase permet (Auth Hooks, OTP par email) et propose la solution la plus simple à maintenir.
  - Emails d'authentification envoyés par le SMTP de la société, avec des modèles en FR/EN/NL.
  - Le rôle et la maison de chaque utilisateur sont stockés dans une table `profiles` liée à `auth.users`, lisible par les politiques RLS.
- **Jetons d'API** pour l'automatisation : un Administrateur crée des jetons nominatifs, avec des droits limités, une date d'expiration et la possibilité de les révoquer. Ils sont stockés hachés et acceptés par les routes `/api` via l'en-tête `Authorization: Bearer`. Ils permettent aux scripts et routines de l'équipe d'appeler l'API sans code email.
- **Emails** : fournisseur SMTP ou API de la société, interchangeable par configuration. Modèles éditables en admin.
- **Traduction automatique** : derrière une interface interne (`translate(text, from, to)`), fournisseur interchangeable par configuration.
- **Tâches planifiées** (imports VNI automatiques, export hebdomadaire, alertes de fraîcheur) : Vercel Cron Jobs ou `pg_cron` de Supabase, à choisir dans une note de décision. Chaque exécution est journalisée et visible en admin.
- **Traitements lourds** (import de 600 000 VNI, conversion DOCX→HTML, migration) : respecter les limites de durée des fonctions Vercel en traitant par lots, ou via un script en ligne de commande (`npm run …`) lancé localement ou par GitHub Actions.
- **Local** : `supabase start` (Supabase complet en local avec Docker) + `npm run dev`. Un `README` permet de tout lancer en moins de 10 minutes. Jeu de données de démonstration (`supabase/seed.sql`) sans données réelles.
- **Qualité** : ESLint, Prettier, TypeScript strict. Tests unitaires (Vitest), tests d'API et de RLS, et tests de bout en bout (Playwright) pour les parcours clés. Intégration continue GitHub Actions : lint, typage, tests, build, à chaque demande de fusion.
- **Environnements** :
  - **Production** : projet Supabase `prod` + domaine de production Vercel ;
  - **Recette** : projet Supabase `staging` + déploiement Vercel de la branche `staging` (ou les « Preview Deployments » branchés sur `staging`) ;
  - **Local** : Supabase local.
  - Migrations appliquées automatiquement à la recette par GitHub Actions (`supabase db push`), puis à la production après mon accord (workflow manuel). Les variables d'environnement de chaque environnement sont dans Vercel et listées, sans leurs valeurs, dans `.env.example`.
- **Sécurité** : en-têtes équivalents à l'actuel (CSP stricte, HSTS, X-Frame-Options, nosniff), définis dans `next.config` ou `vercel.json`. Validation de toutes les entrées (Zod). Protection CSRF sur les routes à cookie. Journal d'audit.
- **Réversibilité** : tout reste du standard (PostgreSQL, fichiers, Next.js). Documente dans `docs/RUNBOOK.md` comment déplacer la base hors de Supabase (`pg_dump`) et l'application hors de Vercel (`next build` dans un conteneur) si un jour c'est nécessaire.

### 5. Modèle de données (à affiner, puis à documenter dans `docs/modele-donnees.md`)

Toute table a un `id`, `created_at`, `updated_at`, `created_by` et `updated_by`.

- **Accès et paramétrage** :
  - `auth.users` (géré par Supabase Auth : email, mot de passe, MFA, dernière connexion) et `profiles` (même id) : nom, téléphone, mobile, rôle, maison_id (si rôle Maison), langue (FR/EN/NL), actif, date de validité, plan_id, statut de paiement, avatar ;
  - `roles` et `role_permissions` : les permissions sont des codes (ex. `funds.edit`, `news.publish`, `users.manage_staff`, `nav.import`, `docs.manage`, `audit.read`). La matrice rôle → permissions est **éditable en admin**. Il n'y a **aucune adresse email codée en dur** : le « super-administrateur » actuel devient une permission ;
  - `api_tokens` (hachés). Sessions, codes et invitations sont gérés par Supabase Auth ;
  - `plans` ;
  - `settings` (clé → valeur JSON, éditable en admin) : URL agenda, URL et activation du Portfolio Builder, modification d'email autorisée, durée de session, expéditeur des emails, mentions légales, etc. ;
  - `email_templates` : par type et par langue (code de connexion, invitation, relance d'activité…) ;
  - `audit_log` : utilisateur ou jeton, date et heure, entité, id, action, valeurs avant et après en JSON. **Jamais de SQL brut.**
- **Référentiels** :
  - `classifications` : libellés FR/EN/NL, ordre, interne/externe ;
  - `categories` : liste gérée, libellés FR/EN/NL (et non plus du texte libre) ;
  - `allocation_labels` : clé → libellés FR/EN/NL, pour les secteurs et zones ;
  - `currencies` : codes ISO 4217 ; « E » est migré en « EUR ».
- **Maisons et banques** :
  - `maisons` : nom, adresse, slogan, site, logo, sponsor, propose FID, propose fonds externes, description, spécialités et type de gestion pour chacun des deux volets, seuil FID ;
  - `maison_contacts` : nom, email, téléphone, langue, photo ;
  - `banques` : nom, pays, statut, site, adresse, contact, email, téléphone, description, logo, lombard, frais de transaction, frais lombard ;
  - `banque_documents`.
- **Benchmarks** : `benchmarks` (code unique, nom) et `benchmark_values` (benchmark_id, date, valeur ; clé unique benchmark + date).
- **Fonds** :
  - `funds` : nom, ISIN (unique pour les fonds externes), code interne, interne/externe (FID), actif, maison, banque dépositaire (fonds internes), classification, catégorie, type de fonds, compartiment, date de création, devise, actifs totaux (avec leur **date de référence**), frais de gestion, TER, benchmark, SRI 1–7, score ESG 0–100, code ESG, duration, qualité de l'émetteur, disclaimer, politique d'investissement FR/EN/NL (HTML assaini), gérant, analyste, `data_updated_at` (date de dernière mise à jour **des données par une personne**, distincte de `updated_at` technique), dernier rappel ;
  - `fund_allocations` : fonds, type (positions, sectors, assets, geographies), clé ou libellé, pourcentage décimal, ordre ;
  - `fund_reports` : fonds, nom, **type** (rapport mensuel, factsheet, KID, rapport annuel…), **période couverte** (mois et année, champ dédié), date de dépôt, langue, clé du fichier, taille, empreinte SHA-256 ;
  - `fund_comments` : date, analyste, texte HTML ;
  - `fund_nav` : fonds, **date**, valeur, source, date d'import ; clé unique fonds + date ;
  - `user_selections` : **pondérations par utilisateur**. Sur l'ancien site, elles étaient globales, stockées sur le fonds.
- **Contenus** :
  - `news` : maison, auteur, langue (FR/EN/NL), statut (brouillon, à valider, publié, archivé), date, titre, HTML ;
  - `news_images` ;
  - `documentation` : titre, auteur, badge Invest ou Law, statut, date, contenu HTML, fichier source.

### 6. Phases (une demande de fusion au moins par phase ; ne passe à la suivante qu'avec ses critères validés)

**Phase 1 : socle.**
- Squelette Next.js + TypeScript + Tailwind ; dossier `supabase/` (configuration, migrations, seed) ; projets Vercel et Supabase reliés au dépôt ; intégration continue ; `README.md` (lancer en local en moins de 10 minutes) ; `CLAUDE.md` (conventions, commandes, règles de ce prompt résumées).
- Mise en page commune :
  - barre latérale de 250 px avec sections INVEST et LAW ;
  - tiroir mobile sous 900 px ;
  - avatar en haut à droite ;
  - charte de l'annexe B.15 en variables CSS (thème modifiable en un seul fichier).
- Internationalisation FR/EN/NL : fichiers de traduction, aucun texte en dur dans les composants.
- *Critère* : `supabase start` + `npm run dev` affichent une page d'accueil vide traduite ; la recette Vercel est en ligne et se met à jour à chaque fusion ; l'intégration continue est verte.

**Phase 2 : comptes, rôles, sécurité.**
- Connexion en deux étapes, déconnexion, mot de passe oublié, invitation, paramètres du compte (annexe B.10).
- Permissions configurables en base, middleware de contrôle sur chaque route, journal d'audit, jetons d'API.
- Écran Admin > Utilisateurs (annexe B.11) et Admin > Rôles et permissions.
- Script `npm run create-admin` pour créer le premier Administrateur sans passer par l'interface ; procédure de secours (section 3 bis) écrite et testée.
- Création de mes 3 comptes de test (Administrateur, Responsable, Data) sur la recette ; mode « Voir comme » ; refus de supprimer le dernier Administrateur ; double authentification obligatoire pour Administrateur et Responsable.
- *Critère* : des tests prouvent qu'un Courtier ne peut appeler aucune route d'écriture, qu'une Maison ne voit et ne modifie que sa maison, ses fonds et ses nouvelles, et qu'un jeton révoqué est refusé.

**Phase 3 : référentiels.**
- Maisons, avec leurs contacts (B.6) ; banques dépositaires, avec leurs documents (B.7) ; benchmarks, avec leurs valeurs (B.4.9) ; classifications, catégories, libellés d'allocation et devises, tous en admin.
- Page d'accueil : maisons sponsors (B.1).

**Phase 4 : fonds.**
- Liste des fonds et fiche complète (B.2 à B.4) : allocations, rapports, commentaires, politique d'investissement multilingue avec traduction automatique.
- `PATCH /api/funds/{id}` (mise à jour partielle) **en plus** du `PUT` complet.
- Renommage et changement de période d'un rapport. Doublon d'ISIN refusé côté serveur.

**Phase 5 : VNI et calculs.**
- Historique VNI : affichage, édition par ligne (ajouter, modifier, supprimer **une** VNI, sans réécrire tout le mois), import CSV par fonds et en masse `ISIN,Date,VNI` avec rapport détaillé (lignes importées, ignorées, en conflit), page « Importer les VNI » (B.12).
- Module `lib/finance/` **pur et testé** : toutes les formules de l'annexe B.5, harmonisées selon l'annexe C. Chaque formule a des tests avec des valeurs calculées à la main, et `docs/formules.md` les explique à un non-développeur.
- Comparateur (B.4.7), sélection et simulateur (B.3).
- *Critère* : tests de bout en bout « importer un CSV → voir la courbe → corriger une VNI → la performance change ».

**Phase 6 : contenus.**
- Nouvelles, avec circuit de validation (B.8) : une Maison soumet, une personne ayant `news.publish` publie. Le droit se donne en admin, sans développeur.
- Documentation, avec import DOCX/XLSX/PDF converti en HTML (B.9).
- Éditeur riche commun : gras, italique, souligné, listes, liens, images ; HTML assaini côté serveur avec une liste blanche.

**Phase 7 : administration et activité.**
- Admin > Activité et relances (B.13) : envoi réel de l'email, modèle par langue éditable, historique des relances.
- Admin > Paramètres : toutes les `settings`. Admin > Modèles d'emails. Admin > Journal d'audit, filtrable et exportable en CSV.
- **Exports** : bouton « Exporter toutes les données » (ZIP de CSV et JSON par table, plus la liste des fichiers) réservé aux administrateurs, et l'équivalent en ligne de commande. C'est la garantie que les données ne sont jamais prisonnières.

**Phase 8 : LAW et outils intégrés.**
- Arbre décisionnel de planification (B.14), traduit FR/EN/NL, avec le parcours affiché et un export PDF du résultat.
- Page Simulation Taxe : structure prête, règles fiscales belges de B.9.1 dans un fichier de paramètres daté et éditable en admin (taux TOB et plafonds, précompte, taxe sur les plus-values, Reynders, TCT) ; calculateur simple. Les taux changent chaque année : **aucun taux en dur dans le code**.
- Agenda : URL configurable, bouton d'ouverture, aperçu si la CSP l'autorise (ajouter le domaine dans `frame-src` via les paramètres).
- Portfolio Builder et Analyzer : iframe avec l'échange `postMessage` de B.4.8, URL et activation configurables. Prévoir que l'application cible puisse ne pas suivre ; dans ce cas la carte « À venir » s'affiche.

**Phase 9 : migration des données.**
- Script `scripts/migrate-from-legacy/` **idempotent** (relançable sans créer de doublon) qui lit l'ancien site, soit par le dump fourni par le développeur, soit par son API JSON (annexe B.16, connexion avec un compte Data ou Responsable, code email saisi à la main). Il importe :
  - les référentiels, maisons et leurs contacts, banques et leurs documents, benchmarks et leurs valeurs ;
  - les fonds, leurs allocations et commentaires ;
  - les VNI (environ 620 000 ; par lots) ;
  - les rapports : téléchargement de chaque PDF, vérification de l'en-tête `%PDF`, empreinte, envoi dans Supabase Storage (bucket privé) ;
  - les nouvelles et leurs images, la documentation.
- **Utilisateurs** : les mots de passe ne sont pas récupérables. On crée les comptes (même email, rôle, maison, langue), puis on envoie une **invitation** à définir un nouveau mot de passe, seulement le jour de la bascule et après mon accord.
- **Corrections pendant la migration** :
  - devise « E » → « EUR » ;
  - catégories texte → table `categories` ;
  - période des rapports déduite du nom (« Rapport de gestion Août 2026 » → 2026-08), sinon laissée vide et listée ;
  - VNI décalées d'un jour : **ne pas corriger automatiquement**. Produire un rapport et me demander. Une analyse existe déjà dans le dépôt Invest-Law (`docs/2026-10-14-diagnostic-dates-vni.xlsx`).
- **Rapport de migration** `docs/migration/rapport-AAAA-MM-JJ.md` : comptes source → cible par table, écarts, fichiers manquants, données douteuses.
- *Critère* : les nombres correspondent pour chaque table ; 20 fiches tirées au hasard sont identiques à l'œil sur l'ancien et le nouveau site.

**Phase 10 : recette, compatibilité et bascule.**
- **Compatibilité de l'API** : l'équipe a des scripts et des routines Claude qui appellent l'API actuelle. Ils se trouvent dans le dépôt Invest-Law : `tools/investlaw.py`, `tools/investlaw_upload.py` et le guide `docs/2026-10-12-guide-invest-law.md`.
  - Les routes, noms de champs et formats de l'annexe B.16 doivent **continuer de fonctionner à l'identique** (couche de compatibilité `/api/...`).
  - Les nouvelles routes et améliorations sont ajoutées sans casser l'existant.
  - Une documentation OpenAPI est générée automatiquement et servie sur `/api/docs`.
  - Fournis un test qui rejoue les appels de ces scripts sur la recette.
- **Recette** : liste de contrôle `docs/recette.md`, une ligne par fonctionnalité de l'annexe B, à cocher par l'équipe sur l'environnement de recette.
- **Performance** : liste des 500 fonds en moins de 1 s ; historique de 10 ans de VNI en moins de 1 s.
- **Bascule**, avec mon accord à chaque étape :
  1. gel des écritures sur l'ancien site ;
  2. migration finale ;
  3. contrôle ;
  4. DNS ;
  5. invitations ;
  6. surveillance renforcée pendant 7 jours.
  Retour arrière documenté (remettre l'ancien DNS).

**Phase 11 : autonomie (livrables obligatoires).**
- `docs/RUNBOOK.md`, pour un non-développeur :
  - où est quoi (comptes, tableaux de bord) ;
  - comment déployer, revenir à la version précédente, restaurer une sauvegarde (procédure **testée réellement une fois** sur la recette, date notée) ;
  - comment ajouter un administrateur, renouveler un secret, lire les erreurs ;
  - qui alerter.
- `docs/GUIDE-ADMIN.md` : chaque écran d'administration et chaque paramètre, avec captures.
- `docs/ARCHITECTURE.md` : un schéma, les dossiers du code, le chemin d'une requête, où ajouter une fonctionnalité.
- `docs/FAIRE-EVOLUER-AVEC-CLAUDE.md` : comment demander une évolution à Claude Code sur ce dépôt (ouvrir une session, décrire le besoin, relire la demande de fusion, tester en recette, mettre en production), avec 3 exemples concrets.
- Une compétence `.claude/skills/<nom>/SKILL.md` qui décrit l'API et les tâches courantes (fiche, VNI, rapports), pour que les sessions Claude de l'équipe travaillent sur le nouveau site comme sur l'ancien, mais avec un jeton d'API au lieu du code email.
- `docs/ACCES.md` : les trois niveaux d'accès de la section 3 bis, qui détient quoi, et comment transmettre ou retirer un accès (arrivée ou départ d'une personne, fin de mission d'un prestataire).
- Sauvegardes : sauvegardes quotidiennes Supabase (plus PITR si le budget le permet) ; export complet hebdomadaire (`pg_dump` + fichiers du Storage) par GitHub Actions vers un second emplacement appartenant à l'organisation, hors Supabase.

### 7. Définition de « terminé »

1. Chaque fonctionnalité de l'annexe B existe, ou son absence est une décision écrite dans `docs/decisions/`.
2. Chaque défaut de l'annexe C est corrigé ou a fait l'objet d'une décision écrite.
3. L'intégration continue est verte. Il y a des tests de droits pour chaque rôle, des tests des formules et des tests de bout en bout des parcours clés.
4. Un membre de l'équipe sans compétence technique a réalisé seul, en suivant les guides :
   - créer un utilisateur ;
   - donner le droit de publier les nouvelles ;
   - changer l'URL de l'agenda ;
   - modifier un modèle d'email ;
   - corriger une VNI ;
   - exporter toutes les données.
5. Une restauration de sauvegarde a été testée.
6. Je me suis connectée avec les comptes Administrateur, Responsable et Data, et je suis Owner sur GitHub, Vercel et Supabase.
7. Aucun compte, secret ou droit d'administration ne dépend d'une seule personne.

---

## Annexe A : contexte métier

- **Public** : courtiers et conseillers en Belgique, maisons de gestion (asset managers) et équipe interne (Data, Responsable).
- **Langues** : FR (par défaut), EN, NL. Les nombres s'affichent au format belge (virgule décimale), les dates en jj/mm/aaaa.
- **Vocabulaire** :
  - VNI = valeur nette d'inventaire (NAV) ;
  - FID = fonds interne dédié (assurance-vie branche 23), sans ISIN public ;
  - SRI = indicateur de risque 1–7 du KID ;
  - TER = frais courants ;
  - KID = document d'informations clés ;
  - factsheet = rapport mensuel du fonds.
- **Règle d'or des données** : mieux vaut une fiche incomplète qu'une fiche fausse.

## Annexe B : cahier des charges fonctionnel (reconstitué du site actuel, 19/10/2026)

### B.0 Rôles et droits actuels

Quatre rôles : `Responsable`, `Data`, `Maison`, `Courtier`, plus un super-administrateur codé en dur par email. Dans le nouveau site, ce super-administrateur devient le rôle **Administrateur** (section 3 bis), qui a tous les droits du tableau ci-dessous plus ceux notés « permission ».

| Fonction | Responsable | Data | Maison | Courtier |
|---|---|---|---|---|
| Admin (utilisateurs, import VNI, activité) | oui | import VNI seulement | non | non |
| Créer et modifier des utilisateurs Courtier/Maison | oui | non | non | non |
| Attribuer les rôles Data/Responsable, lire les journaux | permission spéciale | – | – | – |
| Fonds : créer et modifier | oui | oui | ses fonds | lecture |
| Pondération et sélection | oui | oui | non (onglet masqué) | **oui** (sa sélection) |
| Maisons : créer et supprimer | oui | oui | non | non |
| Maisons : modifier | oui | oui | la sienne | lecture |
| Banques : créer, modifier, documents | oui | oui | pas de menu | lecture (actives seulement) |
| Benchmarks | oui | oui | non | lecture |
| Nouvelles : rédiger | permission | permission | oui (soumise, invisible tant que non publiée) | non |
| Nouvelles : publier et supprimer | permission `news.publish` | idem | non | non |
| Documentation : gérer | permission `docs.manage` | idem | non | non |
| Voir le statut actif/inactif des fonds | oui | oui | non | non |

**Menu.**
- **Maison** : Nouvelles, Liste des fonds, Fiche maison, Paramètres ; le logo mène à la Liste des fonds.
- **Autres rôles** :
  - Admin (Responsable) ;
  - Importer les VNI (Data) ;
  - Nouvelles ;
  - **INVEST** : Liste des fonds, Maisons de gestion, Banques dépositaires, Agenda, Portfolio Builder, Analyser ma sélection ;
  - **LAW** : Simulation taxe, Planification (arbre décisionnel) ;
  - Documentation ;
  - Paramètres.

### B.1 Accueil

Titre « Les maisons prestigieuses qui nous distinguent » et grille de cartes (logo et nom) des maisons marquées **sponsor**. Chaque carte mène à la fiche maison. Le rôle Maison est redirigé vers la Liste des fonds.

### B.2 Liste des fonds

- **Colonnes** :
  - Actif : pastille, visible pour Responsable et Data ;
  - Nom ;
  - ISIN, ou « FID » pour un fonds interne ;
  - Maison ;
  - Classification (libellé dans la langue de l'utilisateur) ;
  - Pondération (champ éditable) ;
  - Risque.
- **Filtres** : un champ par colonne ; correspondance « contient », insensible à la casse, virgule = point ; tous les filtres combinés (ET). Sur mobile, une recherche unique sur nom, ISIN et maison.
- **Tri** : par clic sur l'en-tête. Le premier clic trie en décroissant pour Actif, Pondération et Risque, en croissant pour les autres. Les valeurs vides vont à la fin ; comparaison numérique ou alphabétique (fr). Tri par défaut : pondération décroissante, puis nom.
- **Onglets** : « Tous les fonds (N) » et « Ma sélection (M) » ; la sélection regroupe les fonds de pondération > 0.
- **Pondération** :
  - saisie en ligne, enregistrée à la sortie du champ ;
  - affichage avec 2 décimales ;
  - total affiché dans l'en-tête, en vert s'il vaut 100 %, en rouge sinon ;
  - en onglet Sélection, une pondération ramenée à 0 retire le fonds de la liste.
- **Rôle Maison** : seulement ses fonds, sans onglets ni filtres de colonnes ; sous-titre « Cette liste présente les fonds {maison} disponibles… ».
- Un clic sur une ligne ouvre la fiche. Le lien profond `?fundId=…&tab=details|vl|comments|compare|report-pb` ouvre directement la fiche et l'onglet. Échap revient à la liste.
- **Ajouts souhaités** : export CSV/Excel de la liste filtrée ; pagination ou défilement virtuel si nécessaire.

### B.3 Ma sélection : courbe et simulateur

- **Courbe du portefeuille** : sur les dates communes à tous les fonds sélectionnés. Version corrigée : voir C.1.
- **Plage affichée** : « depuis la date d'investissement » ou « depuis la création ». Indicateurs affichés : performance annualisée et dernière valeur.
- **Simulateur** :
  - champs : investissement initial (€) ; date d'investissement (1er janvier de l'année en cours par défaut) ; apport récurrent avec périodicité 1, 3 ou 12 mois ; retrait récurrent avec les mêmes périodicités ; frais de contrat annuels (%) ; taxe sur versement (%).
  - recalcul à chaque saisie ; une valeur négative ou invalide compte pour 0.
- **Algorithme de référence** :
  1. Point de départ : première VNI à la date de départ ou après.
  2. Unités initiales = investissement / VNI. Frais initiaux = investissement × taxe.
  3. Échéances : date de départ + k × période (le jour est ramené au dernier jour du mois si besoin ; au plus 1 200 échéances ; jusqu'à la dernière VNI). Chaque échéance s'exécute à la première VNI à sa date ou après. À date égale, l'apport passe avant le retrait.
  4. Avant chaque échéance, et à la fin, les frais courent : max(investi net, 0) × taux annuel × jours / 365.
  5. Apport : frais += montant × taxe ; unités += montant / VNI ; investi net et investi brut augmentent du montant.
  6. Retrait : unités retirées = min(unités, montant / VNI) ; investi net diminue du montant retiré, sans descendre sous 0 ; total retiré augmente d'autant.
  7. Résultats :
     - valeur finale = max(0, unités × VNI finale − frais) ;
     - gain = valeur finale + total retiré − investi brut ;
     - performance totale = gain / investi brut ;
     - performance annualisée = (1 + performance totale)^(365/jours) − 1 ;
     - affichage : valeur finale en € et les deux performances, colorées selon le signe.
- **Avertissement juridique** en pied de bloc : « … ne constituent en aucun cas un conseil en investissement ». Texte éditable en admin.
- « Analyser ma sélection » (Portfolio Analyzer) exige une sélection dont le total vaut 100 %.

### B.4 Fiche fonds

#### B.4.1 Champs

- **Colonne de gauche** :
  - Nom (obligatoire) ;
  - ISIN : obligatoire et unique pour un fonds externe, masqué pour un FID ;
  - Code interne : calculé pour un FID = 3 premières lettres du nom en majuscules + « - » + classification ;
  - Type de fonds ;
  - Benchmark : liste, avec un crayon qui ouvre la gestion des benchmarks ;
  - Compartiment ;
  - Maison ;
  - Gérant, Analyste ;
  - Banque dépositaire (FID seulement) ;
  - Politique d'investissement FR/EN/NL ;
  - Duration et Qualité de l'émetteur (fonds externes) ;
  - Disclaimer ;
  - Rapports de gestion.
- **Colonne de droite** :
  - Statut actif/inactif (inactif par défaut à la création) ;
  - FID ou externe : filtre les classifications proposées et affiche ou masque les champs propres à chaque type ;
  - Date de création ;
  - Dernière mise à jour ;
  - Classification ;
  - Catégorie ;
  - Risque SRI : 7 cases cliquables ;
  - Devise (ISO) ;
  - Actifs totaux (millions) ;
  - Frais de gestion (%), TER (%) ;
  - ESG : curseur 0–100 ; vide = gris ; rouge < 50, jaune ≤ 70, vert au-delà ;
  - Code ESG ;
  - Allocations.
- **Rôle Courtier** : tout en lecture seule. Statut, code interne et bouton Annuler sont masqués ; la politique s'affiche dans la langue de l'utilisateur, avec repli sur le FR.
- **Rôle Maison** : maison préremplie et non modifiable ; onglets Comparateur et Rapport PB masqués.

#### B.4.2 Enregistrement

- **Création** : boutons Enregistrer et Annuler ; validations (nom ; ISIN si externe et non dupliqué ; dates AAAA-MM-JJ ; devise ; nombres ; espaces et « % » retirés, virgule = point).
- **Modification** : enregistrement automatique environ 0,5 s après chaque changement, un appel à la fois, avec l'indicateur « Enregistré ».
- **Amélioration** : envoyer seulement les champs modifiés (PATCH), et ne mettre à jour la date « dernière mise à jour des données » que si une donnée a réellement changé.

#### B.4.3 Allocations

Quatre listes : principales positions, secteurs, classes d'actifs, zones géographiques. Chaque ligne contient un nom et un pourcentage ; il y a toujours une ligne vide à la fin, un « + » sur la dernière ligne et un « × » sur les autres. Les secteurs et zones utilisent des clés traduites (ex. `Information Technology` → « Technologies de l'information »). Ajouts souhaités : total affiché, avec alerte s'il dépasse 100 %.

#### B.4.4 Rapports de gestion

- **Tableau** : nom, fichier, période, date de dépôt, lien PDF (nouvel onglet), suppression avec confirmation.
- **Ajout** : modale avec nom, type, période (mois et année), langue et fichier PDF. Le type MIME et la signature `%PDF` sont vérifiés.
- **Modification** : renommage et changement de période possibles (inexistants sur l'ancien site).

#### B.4.5 Politique d'investissement

- Onglets FR/EN/NL, ouverts par défaut sur la langue de l'utilisateur.
- Éditeur riche limité à `p`, `br`, `strong`, `em`, `u`, `ul`, `ol`, `li`. Le collage se fait en texte brut ; 3 sauts de ligne ou plus sont ramenés à 2.
- Bouton « Traduire depuis {langue} » : visible quand la langue cible est vide et qu'une autre langue est remplie. Il remplit la cible, puis enregistre.

#### B.4.6 Historique VNI

- **Bandeau** : jauge, performance annualisée, classification, volatilité, Sharpe, perte maximale, dernière VNI.
- **Jauge** : seuil selon la classification (défensif 4 %, équilibré 6 %, dynamique 8 %, agressif 10 %). Rouge si la performance est < 0, verte si elle dépasse le seuil, jaune entre les deux. Les seuils sont éditables en admin.
- **Courbe** et tableau des performances YTD, 1, 3, 5 et 10 ans, colorés selon le signe.
- **Édition** (éditeurs) : sélecteur de mois ; lignes date + VNI triées par date décroissante ; ajout, modification et suppression **ligne par ligne**.
- **Import CSV** `date,valeur` : rapport des lignes importées et ignorées.
- **Import automatique** depuis une source configurable : prévoir une interface d'« importeurs » (fichier, email, API fournisseur), activable par fonds.

#### B.4.7 Comparateur

- **Fonds comparé** : choisi par recherche parmi les fonds actifs (« Nom (ISIN) »).
- **Tableau côte à côte** : nom, date de création, classification, catégorie, risque, actifs totaux (x,xx M), frais, TER, performance annualisée, volatilité, Sharpe, perte maximale, alpha.
- **Graphique base 100** depuis la première date commune : VNI / VNI de départ × 100. Couleurs : bleu pour le fonds de la fiche, orange pour le fonds comparé ; ligne pointillée à 100.
- **Conclusion** rédigée : **enregistrée** (elle ne l'était pas sur l'ancien site).

#### B.4.8 Rapport PB

Iframe de l'application Portfolio Builder (`{embed_url}/scorecard/?isin=…`).

Échange `postMessage`, avec vérification de l'origine :
1. l'iframe envoie `pb-ready` ;
2. le serveur fournit un code à usage unique (`POST /api/portfolio-builder/embed-code {requested_path}` → `{code}`) ;
3. la page l'envoie à l'iframe en `pb-auth` (ou `pb-auth-error` en cas d'échec) ;
4. l'iframe répond `pb-authenticated` ou `pb-auth-failed`, et envoie `pb-resize {mode: content|viewport, height}`.

Sans ISIN : message « Aucun code ISIN disponible ». Configuration : `GET /api/portfolio-builder-url` → `{enabled, embed_url, app_origin}`.

#### B.4.9 Benchmarks

Modale : liste (code et nom) avec recherche ; création et modification avec un code unique sans tenir compte de la casse ; onglet VNI du benchmark (mêmes fonctions qu'en B.4.6, plus import CSV).

#### B.4.10 Commentaires analystes

Cartes triées par date décroissante, avec analyste (obligatoire), date et texte riche (obligatoire). Ajout, modification sur place, suppression avec confirmation.

### B.5 Formules financières de référence

Les VNI ≤ 0 sont exclues ; T = jours / 365.

| Indicateur | Formule |
|---|---|
| Performance annualisée | (VNI_fin / VNI_début)^(1/T) − 1 |
| Rendements | r_t = VNI_t / VNI_{t−1} − 1 |
| Volatilité | écart-type d'échantillon des r_t × √k, avec k selon l'écart médian entre dates : ≤ 10 j → 252 ; ≤ 20 → 52 ; ≤ 45 → 12 ; ≤ 90 → 4 ; sinon 1 |
| Sharpe | (performance annualisée − taux sans risque) / volatilité ; taux sans risque paramétrable en admin, 0 par défaut |
| Perte maximale (max drawdown) | min(VNI_t / plus haut atteint jusqu'à t − 1) |
| YTD | VNI_fin / première VNI à partir du 1er janvier de l'année de la dernière VNI − 1 |
| Performance sur N ans | VNI_fin / dernière VNI à (date de fin − N ans) ou avant − 1 ; seulement si l'historique couvre N ans |
| Base 100 | VNI_t / VNI_base × 100 |
| Alpha | voir C.1 |

### B.6 Maisons de gestion

- **Liste** :
  - deux onglets avec compteur : « Fonds internes dédiés (FID) » et « Fonds externes » ; une maison peut être dans les deux ;
  - recherche insensible aux accents ;
  - colonnes : logo, nom, adresse, site ;
  - suppression (Responsable et Data) avec avertissement donnant le nombre de fonds liés ;
  - « + Ajouter » crée la fiche et l'ouvre.
- **Fiche** :
  - logo, nom (obligatoire), site (lien cliquable), propose FID oui/non, propose fonds externes oui/non, adresse, slogan, sponsor oui/non ;
  - contacts : photo, nom, email, téléphone, langue ; ajout et suppression de lignes ;
  - panneau FID : liste des FID de la maison (lien vers chaque fiche), description, spécialités, type de gestion, seuil FID ;
  - panneau Fonds externes : liste des fonds externes, description, spécialités, type de gestion ;
  - éditeur riche ; enregistrement automatique.
- **Rôle Maison** : la fiche s'ouvre directement, sans retour à la liste. **Courtier** : lecture seule. Lien profond `?maisonId=`.

### B.7 Banques dépositaires

- **Mise en page** : liste à gauche (recherche, ajout, suppression avec nombre de fonds liés) et fiche à droite ; panneau plein écran sur mobile.
- **Champs** : logo, nom (obligatoire), site, statut actif/inactif, adresse, pays, contact, email, téléphone, description, lombard oui/non, frais de transaction, frais lombard.
- **Documents PDF** : nom et fichier ; ajout et suppression.
- **Maisons partenaires** : cartes qui mènent aux fiches maisons.
- **Courtier** : banques actives seulement ; les blocs vides sont masqués.

### B.8 Nouvelles

- **Mise en page** : liste à gauche (recherche sur titre, auteur, maison, langue ; logo de la maison ; titre ; « Maison · date » ; badge de langue ; pastille de statut pour les administrateurs) et article à droite.
- **Formulaire** : maison (imposée pour le rôle Maison), statut, auteur, date, langue (FR/EN/NL), titre (255 caractères au plus), texte riche avec images (png, jpeg, gif ou webp, 2 Mo au plus).
- **Circuit** : une Maison soumet (statut « à valider »), une personne ayant `news.publish` publie, refuse ou archive. Les lecteurs ne voient que les nouvelles publiées.
- **Ajout souhaité** : notification email à l'auteur lors de la publication, et aux validateurs lors d'une soumission. Activable en admin.

### B.9 Documentation (menu « Documentation »)

- **Mise en page** : comme les Nouvelles.
- **Champs** : titre, auteur, badge Invest ou Law, date, statut visible/invisible, document source (DOCX, XLS, XLSX ou PDF, 15 Mo au plus) converti en HTML à l'enregistrement, et contenu HTML éditable.
- **Contenus à reprendre** : les 2 articles actuels, « Les frais et la fiscalité en Belgique » et « Fiscalité des principaux actifs financiers en Belgique » ; les récupérer à la migration.

#### B.9.1 Règles fiscales belges citées dans ces articles (à mettre en paramètres datés, pas en dur)

- **TOB** :
  - obligations, SIR et SICAV/ETF de distribution : 0,12 % (plafond 1 300 €) ;
  - actions : 0,35 % (plafond 1 600 €) ;
  - SICAV/ETF de capitalisation inscrits à la FSMA : 1,32 % (plafond 4 000 €) ;
  - ETF de capitalisation inscrits auprès d'un autre régulateur de l'EEE : 0,12 % (plafond 1 300 €) ;
  - SICAV non cotée de distribution : exonérée.
- **Précompte mobilier** :
  - 30 %, avec exonération des dividendes jusqu'à 833 € ;
  - épargne réglementée : 0 % jusqu'à 1 020 €, puis 15 % ;
  - SIR de soins de santé : 15 %.
- **Plus-values (depuis le 01/01/2026)** :
  - 10 %, avec exonération de 10 000 € par an (report d'un dixième par an pendant 5 ans au plus, soit 15 000 € maximum) ;
  - moins-values de la même année compensables ;
  - plus-values spéculatives : 33 %.
- **Taxe Reynders** : 30 % sur la part obligataire de la plus-value, pour les fonds détenant plus de 10 % d'obligations.
- **Taxe sur les comptes-titres** : 0,30 % au-delà de 1 000 000 € de valeur moyenne.

### B.10 Connexion et paramètres du compte

- **Connexion** :
  1. email + mot de passe ;
  2. code à 6 chiffres par email. Le message indique l'adresse masquée (2 premiers caractères, puis des `*`, puis `@domaine`). Messages d'erreur distincts : identifiants, code manquant, code invalide, code expiré.
  3. redirection vers la Liste des fonds pour le rôle Maison, vers l'Accueil pour les autres.
- **Paramètres du compte** :
  - avatar : recadré en 192×192, retirable ;
  - nom (obligatoire) et mobile, enregistrés à la sortie du champ ;
  - langue, appliquée immédiatement ;
  - changement d'email : nouvel email, puis code ; activable en admin ;
  - changement de mot de passe : mot de passe actuel, nouveau mot de passe de 12 caractères au moins, confirmation, puis code ;
  - déconnexion.

### B.11 Admin > Utilisateurs

- **Liste** : nom (avec la maison pour le rôle Maison), email, téléphone, mobile, rôle, statut (inactif en rouge), validité, et accès au journal.
- **Modale** :
  - date de création ;
  - statut actif/inactif : désactivation, sans suppression ;
  - nom (obligatoire), email (obligatoire et valide), téléphone, mobile ;
  - rôle, et maison (obligatoire si le rôle est Maison) ;
  - langue ;
  - plan ;
  - statut de paiement : « En attente », « Payée » ou « Aucun plan payant actif » ;
  - date de validité.
- **Création** : envoie une invitation (lien pour définir le mot de passe).
- **Journal par utilisateur** : date et heure, table, type (création, modification, suppression), objet, différences avant/après. Filtres par colonne.

### B.12 Importer les VNI

- **Tableau** : nom, ISIN, date de la dernière VNI, dernière VNI ; filtres et tri (par nom par défaut).
- **Import CSV** `ISIN,Date,VNI` (ex. `LU0524465548,2025-11-01,99.34`) : les lignes invalides sont ignorées et listées. Résultat : « N lignes importées, M ignorées ».
- Un clic sur une ligne ouvre l'onglet VNI de la fiche.
- **Ajout souhaité** : signaler les fonds dont la dernière VNI a plus de X jours (X éditable en admin).

### B.13 Admin > Activité et relances

- **Tableau des fonds** : actif, nom, maison, date de dernière mise à jour des données, dernier rappel, jours écoulés (tri décroissant), bouton « Écrire » (vert si moins de 30 jours, rouge sinon ; seuil éditable).
- **Modale de relance** : destinataire (email du contact de la maison), objet, message, langue FR/EN/NL. La langue est initialisée sur celle du contact et recharge le modèle correspondant.
- **Modèle FR actuel** : objet « Mise à jour des informations de votre fonds » ; message : « Bonjour, … la dernière mise à jour des données de votre fonds {fundName} remonte au {lastUpdate} … vous invitons à vérifier les données … invest-law.eu … Bien cordialement, L'équipe ». Les modèles sont éditables en admin.
- L'envoi enregistre le rappel (date, expéditeur, destinataire, texte).

### B.14 LAW > Planification : arbre décisionnel

- **Assistant** une question à la fois : barre de progression, « Question n · rubrique », boutons de réponse, Retour, Recommencer, fil des réponses déjà données. Résultat : titre, cartes de contrats recommandés et note éventuelle.
- **Contrats** : trois lignes chacun, correspondant probablement à preneur / assuré(s) / bénéficiaire décès. **Faire valider les libellés par le juriste de l'équipe.**
  - A : M+Mme / M+Mme+Enfant / NIHIL
  - B : M+Mme / M+Mme / NIHIL
  - C : M(UF)+Mme(UF)+Enfant(NP) / idem / NIHIL
  - D : M(UF)+Mme(UF)+NP / idem / NIHIL
  - E : M+Mme / M+Mme+futur NP/PP / NIHIL
  - F (cession de tous les droits) : Enfant (PP) / M+Mme+Enfant / NIHIL
  - G (cession de la nue-propriété) : Survivant (UF)+enfant (NP) / idem / NIHIL
  - H (donation préalable fonds) : Enfant / Enfants + parents / 1° Parents, 2° NIHIL
- **Logique** :
  1. **Profil** : cohabitants de fait (patrimoine = biens propres) ou cohabitants légaux / mariés. Dans ce second cas, question supplémentaire : biens propres ou biens communs.
  2. **Orientation** : horizontale, verticale ou investissement financier.
- **Investissement** : avertissement « Protection financière et fiscale ».
- **Verticale** : « Y a-t-il dépouillement ? »
  - Oui : « Donation préalable fonds » (étapes : contrôle, rente financière), contrat H.
  - Non : « Le dépouillement porte-t-il sur le capital au premier décès ? »
    - Non : A + G.
    - Oui : « La règle des 4 % est-elle acceptable ? » Oui : A + F. Non : A + G.
- **Horizontale, biens communs** : « La génération 2 est-elle impliquée ? »
  - Non : « Modification du régime matrimonial ».
  - Oui : « Y a-t-il dépouillement du capital à la souscription ? » Oui : D. Non : E.
- **Horizontale, biens propres** : « Les chances de survie sont-elles équivalentes ? »
  - Non : « Génération 2 impliquée ? » Oui : C. Non : « Donations réciproques » B + B ; pour les cohabitants légaux ou mariés, note « OU Verblijvingsbeding en Flandre : acte notarié et co-souscription classique ».
  - Oui : « L'équivalence en euros est-elle respectée ? »
    - Oui : « Génération 2 impliquée ? » Oui : A. Non : B.
    - Non : « Un rééquilibrage par donations est-il prévu ? » Non : avertissement « Rééquilibrage par donations : à analyser avant de poursuivre ». Oui : même question Génération 2 (A ou B).
- **Stockage** : l'arbre est une **donnée** (JSON versionné, éditable par un administrateur avec prévisualisation), pas du code.

### B.15 Charte graphique actuelle (à reproduire, en variables)

- **Police** : 'Avenir Next', Avenir, 'Trebuchet MS', sans-serif.
- **Couleurs** :
  - texte #2c3e50 ; texte secondaire #7f8c8d ; titres et en-têtes de tableau #3d5263 ;
  - accent #48a1c1 (INVEST, menu actif) ; LAW #3e5263 ;
  - fond de la barre latérale et de la carte de connexion #eef1f4 ;
  - bouton principal #1a88d4 (survol #166da8) ; secondaire #2c3e50 ; danger #e74c3c (survol #c0392b) ;
  - succès #27ae60.
- **Éléments** :
  - cartes blanches : rayon 12, ombre `0 10px 30px rgba(30,45,60,.08)` ;
  - champs : bordure #dfe6e9, rayon 6 ;
  - tableaux : en-tête #f2f5f8, bordures #e4e8ed ;
  - modales : voile `rgba(15,23,42,.45)`, largeur 560 px au plus.
- **Mise en page** :
  - barre latérale fixe de 250 px ; élément actif avec bordure gauche de 10 px #47a2c1 ;
  - contenu de 1 200 px au plus ; titre h1 de 28 px ; sous-titre de 16 px, gras, #48a1c1 ;
  - mobile (900 px ou moins) : en-tête de 64 px avec menu hamburger et tiroir à droite ; police des champs à 16 px.
- **Logos** : utiliser ceux de l'organisation, fournis par l'équipe.

### B.16 API actuelle à conserver (JSON, cookies de session ; dates AAAA-MM-JJ ; fichiers en base64 `file_name` + `file_data`)

**Session**
- `POST /api/login {username,password}` → `{success, step:'verify', user_id, verification_id, email, langue}`
- `POST /api/login/verify {user_id,verification_id,code}` → `{success,user_id,role,name,email,langue}`
- `POST /api/logout`
- `GET /api/session` → `{user_id,role,name,email,langue,maison_id,maison_name,expires_at}`

**Compte**
- `GET/PUT /api/users/{id}` `{name|mobile|langue|avatar}`
- `POST /api/settings/email/request {user_id,new_email}` puis `/verify {user_id,verification_id,code}`
- `POST /api/settings/password/request {user_id,current_password}` puis `/verify {…,code,current_password,new_password}`
- `GET /api/settings/config` → `{email_modification_enabled}`

**Utilisateurs**
- `GET/POST /api/users`, `PUT /api/users/{id}/admin` `{name,email,phone,mobile,role,langue,isActive,plan_id,payment_status,maison_id}`
- `GET /api/users/logs`
- `GET /api/plans`

**Fonds**
- `GET /api/funds` : liste complète, avec les clés `FundId, Name, ISIN, FID, IsActive, MaisonId, MaisonName, MaisonEmail, MaisonContactLanguage, ClassificationId, Classification(EN/NL), Category, CategoryFR/EN/NL/Display, Ponderation, Risque, BanqueId, FundCode, fund_manager, fund_analyst, CreationDate, last_update, LastReminder, Currency, FundType, Compartment, TotalAssets, Fees, TER, BenchmarkId, BenchmarkName, Benchmark, Disclaimer, InvestmentPolicy, InvestmentPolicyEN, InvestmentPolicyNL, InvestmentPolicyDisplay, Duration, IssuerQuality, ESG, ESG_code`
- `POST /api/funds` et `PUT /api/funds/{id}` : corps complet en snake_case, `classification_id, category, fid, is_active, maison_id, banque_id, name, isin, fund_code, creation_date, currency, fund_type, fund_manager, fund_analyst, compartment, total_assets, fees, ter, benchmark_id, disclaimer, investment_policy(=fr), investment_policy_fr/en/nl, duration, issuer_quality, esg, esg_code, last_update, risque, positions, sectors, assets, geographies` (chaque allocation = `[{name, percentage}]`). Erreur `{error, code:'fund_isin_duplicate'}`. **Ajouter** `PATCH`.
- `PUT /api/funds/{id}/ponderation {ponderation}` → `{ponderation}` : à rattacher désormais à l'utilisateur
- `POST /api/funds/{id}/investment-policy/translate {source_language,target_language,source_text}` → `{translation}`
- `GET /api/funds/{id}/allocations` → `{positions,sectors,assets,geographies}`, éléments `{name,displayName,label_fr,label_en,label_nl,percentage}`
- `GET/POST/DELETE /api/funds/{id}/reports` : élément `{report_name,file_name,display_file_name,report_date,file_url}` ; le POST prend `{report_name,report_date,file_name,file_data}` ; le DELETE prend `{report_name,file_name,report_date}`. **Ajouter** un identifiant, la période, le type et `PATCH`.
- `GET/POST /api/funds/{id}/comments`, `PUT/DELETE /api/funds/{id}/comments/{cid}` : `{date,analyst_name,analyst_comment}`

**VNI**
- `GET /api/funds/{id}/vl` → `[{VLDate,VL}]`
- `PUT /api/funds/{id}/vl?month=AAAA-MM {entries:[{vl_date,vl}]}` : doit **fonctionner**
- `POST /api/funds/{id}/vl/upload {csv}` → `{imported,skipped}`
- `POST /api/funds/{id}/vl/import`
- `POST /api/funds/vl/upload-by-isin {csv}`
- `GET /api/funds/latest-vl` → `[{FundId,ISIN,Name,LastVL,LastVLDate}]`
- **Ajouter** `DELETE /api/funds/{id}/vl/{date}` et `PUT /api/funds/{id}/vl/{date}`.

**Référentiels**
- `GET /api/classifications` → `[{ClassId,ClassOrder,FID,FundClass,FundClassEN,FundClassNL}]`
- `GET/POST /api/benchmarks`, `PUT /api/benchmarks/{id}` `{benchmark_code,benchmark_name}`
- `GET /api/benchmarks/{id}/vni` → `[{vni_date,vni}]`, `PUT …/vni?month=`, `POST …/vni/upload {csv}`

**Maisons**
- `GET/POST /api/maisons`, `PUT/DELETE /api/maisons/{id}`
- `GET /api/maisons/options`
- `GET /api/maisons/{id}/contacts|funds|funds/count`
- Champs : `Nom, Adresse, Slogan, Sponsor, Site, FID, FondsExternes, PointsForts, FID_Specialites, FID_TypeGestion, FID_Seuil, FondsExternes_Description, FondsExternes_Specialites, FondsExternes_TypeGestion, Logo`. Le PUT est en snake_case et accepte `contacts:[{contact_id,name,email,tel,langue,photo}]`.

**Banques dépositaires**
- `GET/POST /api/banques-depositaires`, `GET/PUT/DELETE /api/banques-depositaires/{id}` : `{nom,site,adresse,pays,contact,email_contact,tel_contact,description,logo,status,lombard,frais_transaction,frais_lombard}`
- `…/{id}/documents` (GET, POST `{document_name,file_name,file_data}`), `DELETE …/documents/{doc}`
- `…/{id}/funds/count`, `…/{id}/partner-maisons`

**Contenus**
- `GET/POST /api/nouvelles`, `GET/PUT/DELETE /api/nouvelles/{id}` `{maison_id,auteur,langue,status,creation_date,titre,nouvelle}`
- `POST /api/nouvelles/images {file_name,content_type,file_data}` → `{url}`
- `GET/POST /api/documentation`, `GET/PUT/DELETE /api/documentation/{id}` `{title,author,badge,status,creation_date}`
- `PUT /api/documentation/{id}/content {file_name,file_data}` → `{Content}`

**Admin et intégrations**
- `POST /api/admin/activity/reminder {fund_id,to,subject,message,language}` → `{last_reminder}`
- `GET /api/agenda-url` → `{url}`
- `GET /api/portfolio-builder-url` → `{url,embed_url,app_origin,enabled}`
- `POST /api/portfolio-builder/embed-code {requested_path}` → `{code}`
- `GET /api/portfolio-analyzer/selection-status` → `{has_selection}`

## Annexe C : défauts de l'ancien site à corriger

1. **Formules à harmoniser** (décision à écrire dans `docs/decisions/`) :
   - même définition de la performance annualisée partout ; en dessous d'un an, afficher la performance cumulée avec la mention « non annualisée » ;
   - **courbe de la sélection** : portefeuille en base 100 à partir des rendements pondérés (poids normalisés à 100 %, rebalancement mensuel par défaut, paramétrable), et non plus une somme de VNI pondérées ;
   - **Alpha** : performance annualisée du fonds moins celle de son benchmark sur la même période (VNI du benchmark), ou masqué s'il n'y a pas de benchmark. Sur l'ancien site, l'alpha était égal à la performance du fonds.
2. **Modification et suppression d'une VNI** impossibles (erreur 500) : elles doivent fonctionner ligne par ligne.
3. **Décalage d'un jour** de l'historique VNI : dates en type `date`, aucune conversion de fuseau ; test automatique qui importe `2026-01-31` et relit `2026-01-31`.
4. **Rapports** : période couverte distincte de la date de dépôt ; renommage possible ; type de document.
5. **`PUT` complet obligatoire** et date de mise à jour écrasée à chaque enregistrement : ajouter `PATCH` et `data_updated_at` dédié.
6. **Droits contrôlés côté navigateur seulement**, et super-administrateur codé en dur par email : permissions côté serveur, configurables.
7. **Pondérations globales** : elles deviennent une sélection par utilisateur.
8. **Fichiers PDF accessibles par URL publique** : URL signées après contrôle des droits.
9. **Images en base64 en base** : stockage de fichiers.
10. **Journaux en SQL brut** : journal d'audit structuré.
11. **Paramètres modifiables uniquement par le développeur** (agenda, Portfolio Builder, modification d'email, modèles d'emails, seuils) : écran Admin > Paramètres.
12. **Aucun accès programmatique sans code email** : jetons d'API.
13. **Données** : devise « E » ; catégories en texte libre ; actifs totaux sans date de référence.
14. **Textes non traduits** (Nouvelles, Documentation, arbre décisionnel) ; nouvelles limitées à FR et NL.
15. **Conclusion du comparateur non enregistrée** ; page Simulation taxe vide.
16. **Aucun export** de la liste des fonds ni des données.

## FIN DU PROMPT
