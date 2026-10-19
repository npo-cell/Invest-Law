# Analyse complète d'invest-law.eu (19/10/2026)

Objectif : savoir précisément ce que fait le site, comment il est construit et où l'équipe dépend du développeur, pour pouvoir **reconstruire une plateforme équivalente que l'organisation possède et maintient elle-même** (code, hébergement, données, comptes), sans dépendre d'une personne.

Méthode : lecture intégrale du front-end du site (37 fichiers HTML/JS/CSS, dont 268 Ko pour la page Fonds), des en-têtes HTTP, des dictionnaires de traduction, des réponses de l'API avec le compte Data (lecture seule, rien modifié), et des notes de `docs/sessions/`.

Prompt de reconstruction qui découle de cette analyse : `docs/livrables/2026-10-19-prompt-reconstruction-investlaw.md`.

## 1. Ce qu'est le site

Plateforme B2B belge, en FR/EN/NL, de **sélection de fonds d'investissement** pour courtiers, avec un volet « Law » (fiscalité et planification successorale). Quatre rôles :

| Rôle | Usage |
|---|---|
| Responsable | administration : utilisateurs, import VNI, activité et relances des maisons |
| Data | équipe interne : tient à jour fonds, VNI, rapports, maisons, banques, benchmarks |
| Maison | une maison de gestion : sa fiche et ses fonds, ses nouvelles |
| Courtier | client : consulte, compose sa sélection, simule |

En plus, un **super-administrateur codé en dur par adresse email** (`omar@xsreturn.com`, le développeur) dans 4 fichiers : lui seul peut publier des nouvelles, gérer la documentation, attribuer les rôles Data/Responsable, voir les journaux et lancer l'import VNI automatique.

## 2. Fonctions (détail dans l'annexe B du prompt)

- **Liste des fonds** : filtres par colonne, tri, pondération éditable, onglet « Ma sélection » avec courbe du portefeuille et simulateur (apports, retraits, frais, taxe).
- **Fiche fonds** (5 onglets) :
  - Fiche : données clés, SRI 1–7, ESG, politique d'investissement FR/EN/NL avec traduction automatique, allocations (positions, secteurs, actifs, zones), rapports de gestion PDF ;
  - Historique VNI : courbe, YTD/1/3/5/10 ans, volatilité, Sharpe, drawdown, édition par mois, import CSV ;
  - Commentaires analystes ;
  - Comparateur de 2 fonds en base 100 ;
  - Rapport PB : iframe vers l'application séparée pb.invest-law.eu.
- **Maisons de gestion** (120), **banques dépositaires** (80, avec documents PDF), **benchmarks** (226, avec VNI).
- **Nouvelles** des maisons, avec images et statut visible/invisible ; **Documentation** (import DOCX/XLSX/PDF converti en HTML).
- **Admin** :
  - utilisateurs (plans, statut de paiement, validité) ;
  - import VNI en masse (CSV `ISIN,Date,VNI`) ;
  - activité : jours depuis la dernière mise à jour de chaque fonds et email de relance à la maison.
- **LAW** : arbre décisionnel de planification (contrats A à H) ; « Simulation Taxe » est une page vide.
- **Outils intégrés** :
  - Agenda : lien vers un Google Sheet ;
  - Portfolio Builder et Analyzer : application externe pb.invest-law.eu, authentifiée par un code échangé en `postMessage`.

## 3. Comment il est construit

- **Front-end** : HTML et JavaScript natif, sans framework ni librairie (graphiques SVG faits main, éditeur `contenteditable`).
- **Serveur** : Node/Express derrière nginx (ETag Express). Le code serveur n'est pas visible.
- **Base de données** : relationnelle. Les noms de colonnes (`FundId`, `MaisonId`…) et les journaux en SQL brut le suggèrent.
- **Fichiers** : PDF des rapports et documents sur DigitalOcean Spaces (Francfort), à des **URL publiques non signées** : quiconque a le lien lit le PDF.
- **Images** (logos, avatars, photos) : stockées en base64 dans la base.
- **Authentification** : mot de passe puis code à 6 chiffres envoyé par email depuis info@invest-law.eu, valable 10 minutes. Session par cookie (7 jours).
- **Sécurité HTTP** : bons en-têtes (CSP stricte, HSTS, X-Frame-Options).
- **Traductions** : `/i18n/{fr,en,nl}.json`.
- **Volumes (19/10/2026)** :
  - 488 fonds, dont 16 internes (FID), et 7 classifications ;
  - 120 maisons, 80 banques, 226 benchmarks ;
  - environ 620 000 VNI, réparties sur 166 fonds ;
  - environ 440 rapports PDF ;
  - 1 nouvelle et 2 documents de documentation.

## 4. Dépendances au développeur constatées (raison d'être du projet)

| Constat | Source |
|---|---|
| Publication des nouvelles et gestion de la documentation réservées à l'email du développeur, codé en dur | `documentation.js`, `frais-fiscalite.js`, `utilisateurs.js`, `simulation.js` |
| Modifier ou supprimer une VNI renvoie toujours une erreur 500 (`PUT /vl?month=`) : aucun moyen de corriger | `docs/sessions/2026-10-14-diagnostic-dates-vni.md` |
| Historique VNI décalé d'un jour sur 122 fiches (environ 532 000 valeurs), probablement à cause d'un fuseau horaire | idem |
| Pas de renommage de rapport ; la date affichée est la date d'upload, pas le mois couvert | `docs/2026-10-12-guide-invest-law.md` |
| `PUT /api/funds/{id}` remplace toute la fiche ; `last_update` est remis à la date du jour à chaque enregistrement | idem |
| Pas d'export des utilisateurs pour l'équipe Data (403) ; journaux en SQL brut | `docs/sessions/2026-10-19-connexion-zimbra.md` |
| Paramètres (URL de l'agenda, Portfolio Builder, modification d'email) fixés côté serveur, sans écran d'administration | `/api/settings/config`, `/api/agenda-url` |
| Pas d'accès programmatique sans code email à chaque session : les routines Claude doivent lire Gmail | skill `invest-law` |
| Portfolio Builder et Analyzer : application séparée, hors de notre contrôle | pb.invest-law.eu |

## 5. Défauts fonctionnels à corriger dans la nouvelle version

- **Formules** :
  - la « performance annualisée » n'est pas calculée de la même façon dans la sélection, la fiche et le simulateur ;
  - l'« Alpha » est en fait la performance du fonds, et le Sharpe ne tient pas compte d'un taux sans risque ;
  - la courbe de sélection additionne des VNI pondérées au lieu de rendements, ce qui est faux dès que les VNI n'ont pas le même ordre de grandeur.
- **Droits** : contrôlés surtout côté navigateur (le Courtier peut modifier la pondération, par exemple), à refaire entièrement côté serveur.
- **Données** :
  - pondération stockée sur le fonds : un seul jeu de pondérations pour tout le monde ;
  - devise « E » au lieu d'« EUR » sur 19 fonds ;
  - catégories en texte libre (56 fonds sans catégorie).
- **Écrans** :
  - comparateur : la conclusion n'est pas enregistrée ;
  - arbre décisionnel : textes non traduits ;
  - simulation taxe : page vide.

## 6. Avant de reconstruire : point juridique et contractuel (à faire en premier)

L'indépendance tient d'abord à la propriété, avant la technique. À vérifier dans le contrat avec le développeur, ou à lui demander par écrit :

1. **Nom de domaine** invest-law.eu : titulaire au registre (EURid) et compte du registrar. Il doit être au nom de la société.
2. **Hébergement, base de données, stockage DigitalOcean et boîte info@** : quel compte, quel titulaire, qui paie.
3. **Propriété du code** source du site et de pb.invest-law.eu (cession de droits ou licence).
4. **Export complet des données** : dump de la base, fichiers et utilisateurs. Ce sont les données de la société.

Si le contrat le permet, **récupérer le code et le dump** peut suffire à devenir autonome plus vite qu'une reconstruction. Le prompt reste utile dans les deux cas : reconstruction propre, ou reprise d'un code existant selon les mêmes exigences.
