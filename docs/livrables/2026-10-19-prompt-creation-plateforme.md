# Prompt de création de la plateforme (version « page blanche »)

Copier tout ce qui suit la ligne, et remplacer `[NOM]` par le nom de la plateforme.

---

Je veux créer **[NOM]**, une plateforme web professionnelle (B2B) de **sélection de fonds d'investissement et d'accompagnement patrimonial**, destinée au marché belge. Ce document décrit tout ce que la plateforme doit faire et à quoi elle doit ressembler. Construis-la entièrement, de zéro.

Le code est hébergé sur **GitHub** : c'est par là que passe toute mise en ligne. L'application est hébergée sur **Vercel** et la base de données sur **Supabase**. Je suis propriétaire de ces trois comptes.

Avant de commencer :
- pose-moi les questions dont tu as besoin ;
- propose-moi un plan par étapes ;
- tiens-moi informée à la fin de chaque étape.

Je dois pouvoir tester chaque partie au fur et à mesure.

## 1. Vision

[NOM] réunit en un seul endroit tout ce dont un courtier ou un conseiller financier a besoin pour choisir des fonds et conseiller ses clients :
- une base de fonds complète et fiable ;
- les historiques de valeur et les performances ;
- les documents officiels des fonds ;
- les avis des analystes ;
- les maisons de gestion et les banques dépositaires ;
- des outils pour composer une sélection, la simuler et la comparer ;
- un volet juridique et fiscal (« LAW ») : documentation fiscale belge et outil d'aide à la planification successorale.

La plateforme a deux grands volets, visibles dans le menu : **INVEST** et **LAW**.

Elle est disponible en **français** (langue par défaut), **anglais** et **néerlandais**. Chaque utilisateur choisit sa langue, et tous les écrans, messages et emails suivent ce choix. Les nombres s'affichent au format belge (virgule décimale) et les dates en jj/mm/aaaa.

L'accès est **privé** : rien n'est visible sans être connecté.

## 2. Utilisateurs, rôles et accès

### 2.1 Les rôles

| Rôle | Qui | Ce qu'il peut faire |
|---|---|---|
| **Administrateur** | moi et un suppléant | Absolument tout : tous les utilisateurs et tous les rôles, droits de chaque rôle, paramètres, modèles d'emails, journal de toutes les actions, export complet des données, publication de tous les contenus |
| **Responsable** | direction, équipe commerciale | Gérer les utilisateurs Courtier et Maison, suivre l'activité des maisons et les relancer, importer des valeurs, gérer tout le contenu |
| **Data** | équipe chargée des données | Créer et tenir à jour les fonds, valeurs, documents, indices de référence, maisons, banques, commentaires, actualités et documentation |
| **Maison** | une maison de gestion partenaire | Voir et modifier **sa** fiche maison et **ses** fonds ; proposer des actualités, publiées après validation |
| **Courtier** | clients de la plateforme | Consulter tout le contenu publié, composer sa propre sélection de fonds, simuler, comparer. Aucune modification de données |

### 2.2 Exigences sur les droits

- L'Administrateur peut modifier en quelques clics, depuis un écran, quels droits a chaque rôle : par exemple donner à un Responsable le droit de publier les actualités.
- Un Administrateur peut **voir la plateforme comme un autre utilisateur ou un autre rôle**, en lecture seule. Cela lui permet de vérifier ce qu'ils voient.
- Il doit toujours rester au moins un Administrateur : on ne peut pas supprimer ni désactiver le dernier.
- Chaque compte de l'équipe interne (Administrateur, Responsable) se protège avec une double authentification.
- Une Maison ne voit jamais les données d'une autre maison en modification. Un Courtier ne peut rien modifier d'autre que sa sélection et ses paramètres. Ces règles doivent être garanties partout, pas seulement dans l'affichage.
- Toute modification de données est enregistrée dans un **journal** : qui, quand, quoi, avant et après. Les Administrateurs peuvent le consulter et le filtrer.
- Dès la première version utilisable, crée-moi trois comptes : un **Administrateur**, un **Responsable** et un **Data**. Je dois pouvoir me connecter avec chacun et voir la différence.

### 2.3 Connexion et compte

- **Connexion** : email, mot de passe, puis code de vérification (double authentification).
- **Récupération** : mot de passe oublié.
- **Arrivée d'un nouvel utilisateur** : il reçoit une invitation par email et choisit lui-même son mot de passe.
- **Page « Paramètres »** de chaque utilisateur :
  - photo de profil (recadrée en carré), nom et mobile ;
  - langue de l'interface, qui s'applique immédiatement ;
  - changement d'email et de mot de passe, confirmés par un code envoyé par email ; mot de passe de 12 caractères au moins ;
  - bouton de déconnexion.
- **Pastille ronde** avec la photo de l'utilisateur, en haut à droite de chaque page, qui mène à ses paramètres.
- **Accès automatisé** : l'Administrateur peut créer des **clés d'accès** pour des outils automatisés (par exemple un assistant qui importe chaque jour les valeurs des fonds). Chaque clé a des droits limités et une date d'expiration, et l'Administrateur peut la révoquer à tout moment.

## 3. Navigation et apparence

### 3.1 Menu latéral fixe à gauche

- Logo en haut.
- Pour l'équipe interne : **Admin** (Administrateur et Responsable), **Importer les valeurs** (Data).
- **Actualités**.
- Section **INVEST** : Liste des fonds ; Maisons de gestion ; Banques dépositaires ; Agenda ; Construire un portefeuille ; Analyser ma sélection.
- Section **LAW** : Simulation fiscale ; Planification (arbre décisionnel).
- **Documentation**.
- **Paramètres**.

L'élément de menu actif est mis en évidence par une bordure épaisse à gauche et un fond légèrement teinté.

Une **Maison** a un menu réduit : Actualités, Liste des fonds (ses fonds), Fiche maison (la sienne), Paramètres. En se connectant, elle arrive directement sur la liste de ses fonds.

### 3.2 Style visuel

Sobre, professionnel, lumineux : un outil de travail sérieux pour la finance.

- **Police** : sans empattement, élégante (style Avenir).
- **Couleurs** :
  - texte bleu-gris foncé (#2c3e50) ; titres bleu ardoise (#3d5263) ;
  - couleur d'accent bleu-vert (#48a1c1), utilisée pour la section INVEST, les sous-titres et l'élément de menu actif ; bleu ardoise (#3e5263) pour la section LAW ;
  - boutons principaux bleus (#1a88d4) ; vert pour les succès et les valeurs positives (#27ae60) ; rouge pour les erreurs, les suppressions et les valeurs négatives (#e74c3c) ;
  - menu latéral sur fond gris très clair (#eef1f4).
- **Éléments** :
  - contenu présenté dans des **cartes blanches** aux coins arrondis, avec une ombre très douce ;
  - tableaux avec un en-tête gris clair et le survol des lignes ;
  - fenêtres modales sur un voile sombre semi-transparent.
- **Titres de page** : un grand titre, sous lequel figure un sous-titre en gras couleur accent.
- **Mobile et tablette** : le site doit être parfaitement utilisable. En dessous d'une largeur de tablette, le menu devient un bouton « hamburger » qui ouvre un tiroir, et les tableaux défilent horizontalement.
- **Ergonomie** : la touche Échap ferme les fenêtres et revient à la liste. Les formulaires de fiche s'enregistrent automatiquement, sans bouton « Enregistrer », avec un discret « Enregistré » qui confirme.

## 4. Accueil

Page de bienvenue titrée « **Les maisons prestigieuses qui nous distinguent** ». Elle présente une grille de cartes (logo et nom) des maisons de gestion marquées comme **partenaires mises en avant**. Chaque carte ouvre la fiche de la maison.

## 5. Liste des fonds (cœur de la plateforme)

### 5.1 Tableau

- **Colonnes** : statut actif/inactif (pastille verte ou rouge, visible par l'équipe interne uniquement) ; nom ; ISIN (ou la mention « FID » pour un fonds interne dédié) ; maison de gestion ; classification ; **pondération** ; niveau de risque.
- **Filtres** : une ligne de filtres au-dessus des en-têtes, avec un champ de recherche par colonne. La recherche porte sur « contient », ignore les majuscules, et les filtres se combinent. Sur mobile, un seul champ de recherche (nom, ISIN, maison).
- **Tri** : par clic sur un en-tête, avec les flèches ▲ ▼. Les valeurs vides vont à la fin. Tri par défaut : pondération décroissante.
- **Export** de la liste filtrée en Excel.
- Un clic sur une ligne ouvre la fiche du fonds.

### 5.2 Onglets « Tous les fonds (N) » et « Ma sélection (M) »

- Chaque utilisateur attribue un **pourcentage de pondération** aux fonds de son choix, directement dans la colonne Pondération. La valeur s'affiche avec 2 décimales.
- Le **total** est affiché dans l'en-tête de la colonne : en vert s'il fait exactement 100 %, en rouge sinon.
- Les fonds pondérés forment **sa sélection**, propre à chaque utilisateur.
- L'onglet « Ma sélection » ne montre que ces fonds, avec le total en bas.

### 5.3 Courbe et simulateur de la sélection

Sous la liste de l'onglet « Ma sélection » :
- **Courbe** de l'évolution du portefeuille composé selon les pondérations, en base 100, sur la période commune aux fonds.
- **Choix de période** : « depuis la date d'investissement » ou « depuis l'origine ».
- **Indicateurs** : performance annualisée et valeur actuelle.
- **Simulateur d'investissement** :
  - montant initial (€) ;
  - date d'investissement (par défaut le 1er janvier de l'année en cours) ;
  - versement périodique et sa fréquence (mensuel, trimestriel, annuel) ;
  - retrait périodique et sa fréquence ;
  - frais de contrat annuels (%) ;
  - taxe sur chaque versement (%).
- **Règles du calcul** :
  - les versements achètent des parts à la valeur du jour, et les retraits en revendent ;
  - les frais de contrat courent chaque jour sur le montant net investi ;
  - la taxe est prélevée sur chaque versement.
- **Résultats**, recalculés en direct : valeur finale en euros, performance totale, performance annualisée, en vert ou en rouge selon le signe.
- **Mention légale** en bas : les simulations ne constituent pas un conseil en investissement et les performances passées ne préjugent pas des performances futures.

## 6. Fiche d'un fonds

Titre de la page = nom du fonds, avec un bouton retour vers la liste. Cinq onglets : **Fiche**, **Historique des valeurs**, **Commentaires analystes**, **Comparateur**, **Rapport détaillé**.

### 6.1 Onglet Fiche

Deux colonnes.

**Colonne de gauche** :
- nom ; ISIN (obligatoire et unique pour un fonds externe) ; code interne ;
- type de fonds ; indice de référence (benchmark) ; compartiment ;
- maison de gestion ; gérant ; analyste ;
- banque dépositaire (pour les fonds internes) ;
- **politique d'investissement** en trois onglets FR / EN / NL, avec un bouton « Traduire depuis… » qui remplit automatiquement une langue vide à partir d'une autre ;
- duration et qualité des émetteurs (fonds obligataires) ;
- avertissement légal ;
- **documents du fonds**.

**Colonne de droite, « Données clés »** :
- statut actif/inactif ;
- type : FID (fonds interne dédié d'assurance) ou fonds externe ;
- date de création ; date de dernière mise à jour des données ;
- classification ; catégorie ;
- **niveau de risque de 1 à 7**, affiché comme 7 cases dont une est sélectionnée ;
- devise ; actifs sous gestion (en millions, avec leur date) ;
- frais de gestion (%) ; frais courants (TER, %) ;
- **score ESG de 0 à 100** sur un curseur coloré (rouge sous 50, jaune jusqu'à 70, vert au-delà) ; code ESG ;
- **quatre tableaux d'allocation** : principales positions, répartition par secteur, par classe d'actifs et par zone géographique. Chaque ligne a un nom et un pourcentage ; on ajoute et retire des lignes facilement ; le total est affiché. Les secteurs et les zones sont traduits dans les trois langues.

**Classifications**, choisies selon le type de fonds :
- fonds externes : Défensif, Équilibré, Dynamique, Agressif ;
- fonds internes : Sécuritaire, Équilibré, Dynamique.

Les catégories (« Actions Monde », « Obligations Europe », « Mixte flexible »…) viennent d'une liste gérée par l'équipe, traduite en trois langues.

**Documents du fonds** :
- liste : nom, type (fiche mensuelle, document d'informations clés, rapport annuel…), **mois couvert**, langue, date d'ajout, lien pour ouvrir le PDF ;
- l'équipe peut ajouter, renommer, changer le mois couvert et supprimer un document, avec confirmation ;
- les documents ne sont accessibles qu'aux utilisateurs connectés.

**Droits sur cet onglet** :
- **Courtier** : tout est en lecture seule, et la politique d'investissement s'affiche dans sa langue (en français si la traduction manque) ;
- **Maison** : elle modifie les fonds de sa maison uniquement.

**Création d'un fonds** : bouton « Ajouter un fonds » dans la liste. Le formulaire est vérifié avant enregistrement : champs obligatoires, ISIN unique, dates et nombres valides.

### 6.2 Onglet Historique des valeurs

**Bandeau de synthèse** :
- une jauge (rouge, jaune ou verte) indique si la performance annualisée est négative, inférieure ou supérieure à l'objectif de la classification. Objectifs : Défensif 4 %, Équilibré 6 %, Dynamique 8 %, Agressif 10 %, modifiables par l'Administrateur ;
- performance annualisée, volatilité, ratio de Sharpe, perte maximale (max drawdown), alpha par rapport à l'indice de référence, dernière valeur.

**Graphique** de l'évolution de la valeur liquidative.

**Tableau des performances** : depuis le début de l'année, 1 an, 3 ans, 5 ans, 10 ans. Chaque performance est en vert ou en rouge selon son signe, et n'est affichée que si l'historique est assez long.

**Gestion des valeurs (équipe)** :
- consultation par mois ;
- ajout, modification et suppression d'une valeur à la fois ;
- import d'un fichier CSV (date, valeur), suivi d'un compte rendu : lignes importées, ignorées et pourquoi.

**Définitions** (à expliquer aussi dans une info-bulle sur chaque indicateur) :
- performance annualisée = (valeur finale / valeur initiale) ^ (365 / nombre de jours) − 1 ; sous un an, on affiche la performance cumulée, avec la mention « non annualisée » ;
- volatilité = écart-type des rendements périodiques, annualisé selon la fréquence des valeurs (quotidienne, hebdomadaire, mensuelle) ;
- Sharpe = (performance annualisée − taux sans risque) / volatilité ; taux sans risque réglable par l'Administrateur ;
- perte maximale = plus forte baisse entre un sommet et un creux ultérieur ;
- alpha = performance annualisée du fonds − celle de son indice de référence sur la même période.

### 6.3 Onglet Commentaires analystes

- Fil de commentaires, du plus récent au plus ancien. Chacun a une date, le nom de l'analyste et un texte mis en forme (gras, italique, listes).
- L'équipe ajoute, modifie et supprime des commentaires.

### 6.4 Onglet Comparateur

- Choix d'un second fonds par une recherche (« Nom (ISIN) »), parmi les fonds actifs.
- Tableau côte à côte : date de création, classification, catégorie, risque, actifs sous gestion, frais, TER, performance annualisée, volatilité, Sharpe, perte maximale, alpha.
- Graphique des deux fonds **en base 100** depuis leur première date commune : le fonds de la fiche en bleu, le fonds comparé en orange, avec une ligne pointillée à 100.
- Zone de **conclusion** rédigée par l'analyste, enregistrée.

### 6.5 Onglet Rapport détaillé

Emplacement réservé à un rapport d'analyse avancée du fonds (fiche d'évaluation), qui pourra être fourni plus tard par un outil complémentaire. En attendant, une carte « Bientôt disponible ».

### 6.6 Indices de référence (benchmarks)

- Accessibles depuis la fiche, par un petit crayon à côté du champ.
- Liste avec recherche. Chaque indice a un code unique et un nom.
- L'équipe crée et modifie les indices et gère leur historique de valeurs, comme pour un fonds. Ces valeurs servent au calcul de l'alpha.

## 7. Importer les valeurs (équipe Data)

- **Tableau de tous les fonds** : nom, ISIN, date et montant de la dernière valeur. Filtres et tri.
- **Signal** sur les fonds dont la dernière valeur date de plus de X jours ; X est réglable.
- **Import en masse** d'un fichier CSV à trois colonnes (ISIN, date, valeur) pour de nombreux fonds à la fois. Exemple d'aide affiché : `LU0524465548,2025-11-01,99.34`. Le compte rendu indique les lignes importées, les lignes ignorées et leur raison.
- Un clic sur un fonds ouvre directement son historique de valeurs.

## 8. Maisons de gestion

### 8.1 Liste

- **Deux onglets** avec compteur : « Fonds internes dédiés (FID) » et « Fonds externes ». Une maison qui propose les deux apparaît dans les deux.
- **Recherche** par nom (sans tenir compte des accents).
- **Tableau** : logo, nom, adresse, site web.
- **Pour l'équipe** :
  - ajout ;
  - suppression, avec un avertissement indiquant le nombre de fonds liés.

### 8.2 Fiche maison

- **Informations** : logo, nom, site (cliquable), adresse, slogan.
- **Interrupteurs** : propose des FID oui/non, propose des fonds externes oui/non, partenaire mis en avant sur l'accueil oui/non.
- **Contacts** : photo, nom, email, téléphone, langue préférée. On peut ajouter et retirer des contacts.
- **Deux panneaux côte à côte, alignés** :
  - « FID » : liste de ses fonds internes (cliquables), description, spécialités, type de gestion, seuil d'accès ;
  - « Fonds externes » : liste de ses fonds externes (cliquables), description, spécialités, type de gestion.
- Les textes longs sont mis en forme : gras, italique, souligné, listes.

**Accès** :
- la **Maison** arrive directement sur sa propre fiche et peut la modifier ;
- le **Courtier** la consulte en lecture seule.

## 9. Banques dépositaires

- **Mise en page** : liste à gauche (recherche, ajout, suppression) et fiche à droite.
- **Fiche** : logo, nom, site, statut actif/inactif, adresse, pays, personne de contact, email, téléphone, description, crédit lombard oui/non, frais de transaction, frais lombard.
- **Documents PDF** de la banque : ajout et suppression par l'équipe.
- **« Maisons de gestion partenaires »** : cartes cliquables vers les fiches maisons.
- **Courtier** : il ne voit que les banques actives.

## 10. Actualités

- **Page** titrée « **Les actualités récentes de vos partenaires de gestion** ».
- **Liste à gauche** : recherche ; chaque carte montre le logo de la maison, le titre, « maison · date » et la langue.
- **Article complet à droite**.
- **Rédaction** :
  - champs : maison, auteur, date, langue (FR/EN/NL), titre, texte mis en forme avec des images ;
  - une **Maison** rédige ses actualités, qui partent **en validation** ;
  - l'équipe autorisée les **publie**, les refuse ou les archive. Le statut se voit d'un coup d'œil (pastille) ;
  - les Courtiers ne voient que les actualités publiées ;
  - un email prévient les validateurs quand une actualité est soumise, et l'auteur quand elle est publiée.

## 11. Documentation

- **Présentation** : même mise en page que les actualités. Chaque document a un badge **Invest** ou **Law**, un auteur, une date et un statut (visible ou masqué).
- **Ajout** : l'équipe peut téléverser un document Word, Excel ou PDF, qui est converti en page lisible, puis le retoucher.
- **Contenus fournis dès le départ** (à rédiger, avec les sources) :
  1. « **Les frais et la fiscalité des investissements en Belgique** » :
     - les frais : courtage, droits de garde, frais courants des fonds et des ETF, frais d'entrée et de sortie, spread, change ;
     - la taxe sur les opérations de bourse : taux et plafonds par type de titre (actions, obligations, ETF et SICAV de distribution ou de capitalisation) ;
     - le précompte mobilier et l'exonération sur les premiers euros de dividendes ;
     - l'épargne réglementée ;
     - la taxe sur les plus-values en vigueur depuis 2026 (taux, exonération annuelle et son report, compensation des pertes) ;
     - la taxe Reynders ;
     - la taxe annuelle sur les comptes-titres ;
     - un tableau récapitulatif.
  2. « **Fiscalité des principaux actifs financiers en Belgique** » : un grand tableau comparatif par type d'actif. Lignes : compte d'épargne, actions cotées et non cotées, épargne-pension, assurances branche 21 et 23, ETF et fonds belges et étrangers, SICAV de capitalisation. Colonnes : précompte, exonération, réduction d'impôt, Reynders, TOB, taxe sur les primes, taxe à 60 ans, taxe sur les comptes-titres, plus-values.
- Chaque chiffre fiscal est daté, avec sa source officielle (SPF Finances, Wikifin/FSMA…). **Signale-moi** tout chiffre que tu n'as pas pu vérifier.

## 12. Volet LAW

### 12.1 Planification : arbre décisionnel

Un **assistant** guide le conseiller, question par question, vers la structure de contrats d'assurance-vie adaptée à la transmission du patrimoine de ses clients.

**Interface** :
- barre de progression ;
- « Question n », avec le thème de la question ;
- grandes cartes-réponses ;
- fil des réponses déjà données ;
- boutons Retour et Recommencer.

**Résultat** : la solution recommandée, illustrée par des **cartes de contrats**. Chaque carte indique le preneur, le ou les assurés et le bénéficiaire en cas de décès, en notation M / Mme / Enfant, avec UF (usufruit), NP (nue-propriété) et PP (pleine propriété). Le résultat est exportable en PDF.

**Logique de départ** (à faire valider par notre juriste) :
1. **Profil** : cohabitants de fait, ou cohabitants légaux / mariés. Dans le second cas, on demande si le patrimoine est fait de biens propres ou de biens communs. Pour les cohabitants de fait, il s'agit toujours de biens propres.
2. **Orientation** :
   - **transmission horizontale** (entre conjoints) ;
   - **transmission verticale** (vers les enfants) ;
   - **simple investissement financier** : le résultat signale qu'il s'agit d'une protection financière et fiscale, sans montage successoral.
3. **Verticale** : « Y a-t-il dépouillement ? »
   - **Oui** : donation préalable de fonds (étapes : contrôle, rente financière).
   - **Non** : « Le dépouillement porte-t-il sur le capital au premier décès ? »
     - **Non** : contrat à la souscription, suivi d'une cession de la nue-propriété.
     - **Oui** : « La règle des 4 % est-elle acceptable ? » Si oui, cession de tous les droits ; sinon, cession de la nue-propriété.
4. **Horizontale avec biens communs** : « La génération suivante est-elle impliquée ? »
   - **Non** : modification du régime matrimonial.
   - **Oui** : « Y a-t-il dépouillement du capital à la souscription ? » Si oui, souscription démembrée avec accroissement ; sinon, contrat classique à la souscription.
5. **Horizontale avec biens propres** : « Les chances de survie sont-elles équivalentes ? »
   - **Non** :
     - si la génération suivante est impliquée : démembrement de propriété ;
     - sinon : donations réciproques (deux contrats croisés), avec une mention sur le pacte d'accroissement (« verblijvingsbeding ») en Flandre pour les couples mariés ou cohabitants légaux.
   - **Oui** : « L'équivalence des montants en euros est-elle respectée ? »
     - si elle ne l'est pas et qu'aucun rééquilibrage par donations n'est prévu : avertissement « à analyser avant de poursuivre » ;
     - sinon : contrat incluant les enfants si la génération suivante est impliquée, contrat entre conjoints sinon.

L'arbre (questions, réponses, résultats, cartes) doit pouvoir être **modifié par un Administrateur sans programmeur**, avec un aperçu avant publication. Il est disponible en trois langues.

### 12.2 Simulation fiscale

Un calculateur qui estime, pour une opération ou un portefeuille donné, les principales taxes belges : taxe sur les opérations de bourse, précompte mobilier, taxe sur les plus-values, Reynders, taxe sur les comptes-titres. Les taux et plafonds sont **modifiables par l'Administrateur** et datés : ils changent chaque année.

## 13. Outils intégrés

- **Agenda** : agenda des événements à venir (conférences des maisons de gestion, webinaires…). Il est tenu dans un tableur en ligne dont l'adresse est réglable par l'Administrateur. Un bouton ouvre l'agenda, et un aperçu est intégré à la page.
- **Construire un portefeuille** et **Analyser ma sélection** : emplacements prévus pour un outil d'analyse de portefeuille complémentaire. Celui-ci calculera les ratios clés, comparera aux fonds de même catégorie, fera des simulations et générera une conclusion par IA.
  - « Analyser ma sélection » n'est accessible que si la sélection de l'utilisateur totalise 100 %. Sinon, un message explique comment pondérer ses fonds.
  - Tant que l'outil n'est pas branché, une carte « Bientôt disponible » s'affiche. Son adresse et son activation sont réglables par l'Administrateur.

## 14. Administration

Une page **Admin** organisée en onglets.

**Utilisateurs** :
- tableau : nom (avec la maison pour les comptes Maison), email, téléphone, mobile, rôle, statut (inactif en rouge), date de fin de validité ;
- fiche utilisateur : statut actif/inactif (on désactive, on ne supprime pas), nom, email, téléphone, mobile, rôle, maison (obligatoire pour une Maison), langue, formule d'abonnement, statut de paiement (« En attente », « Payée », « Aucun plan payant actif »), date de validité ;
- la création d'un utilisateur envoie une invitation ;
- l'historique des actions de chaque utilisateur est accessible depuis sa ligne.

**Rôles et droits** : la matrice rôles × permissions, modifiable (Administrateur).

**Importer les valeurs** : voir la section 7.

**Activité des maisons** :
- tableau de tous les fonds : statut, nom, maison, date de dernière mise à jour des données, date du dernier rappel, **nombre de jours écoulés** (du plus ancien au plus récent) ;
- bouton « Écrire » en vert si la fiche a été mise à jour il y a moins de 30 jours, en rouge sinon (seuil réglable) ;
- ce bouton ouvre un email de relance prérempli : destinataire = contact de la maison, langue = langue du contact (FR/EN/NL, modifiable) ; le texte rappelle la date de dernière mise à jour du fonds et invite la maison à vérifier ses données ;
- l'envoi est enregistré et met à jour « dernier rappel ».

**Paramètres** : tous les réglages de la plateforme, sans programmeur :
- adresse de l'agenda ;
- outil de portefeuille (adresse, activation) ;
- objectifs de performance par classification ;
- taux sans risque ;
- seuils de fraîcheur et de relance ;
- mentions légales ;
- taux fiscaux ;
- expéditeur des emails ;
- autorisation de changer son email.

**Modèles d'emails** : invitation, code, relance, actualités. Chacun est modifiable dans les trois langues.

**Listes de référence** : classifications, catégories, libellés des secteurs et zones, devises, formules d'abonnement.

**Journal** : toutes les actions, filtrables et exportables.

**Export** : un bouton « Exporter toutes les données » produit une archive complète : tableaux et documents. Les données de la plateforme ne doivent jamais être prisonnières.

## 15. Qualité attendue

- **Fiabilité des données** : la plateforme ne doit jamais afficher une valeur inventée ou approximative. Un champ inconnu reste vide et s'affiche « – ».
- **Calculs** : ils doivent être exacts et vérifiés sur des exemples calculés à la main. Explique-les dans une page d'aide accessible aux utilisateurs.
- **Rapidité** : la liste de 500 fonds et un historique de 10 ans de valeurs quotidiennes s'affichent en moins d'une seconde.
- **Sécurité** : documents et données accessibles uniquement aux personnes autorisées ; sauvegardes automatiques quotidiennes.
- **Mise en ligne** :
  - d'abord sur une **version de test**, que je valide ;
  - ensuite en **production** ;
  - je dois pouvoir revenir à la version précédente en cas de problème.
- **Autonomie** : rédige pour moi, en langage simple :
  - un **guide d'administration** : chaque écran et chaque réglage ;
  - un **guide des accès** : qui détient quoi, comment ajouter ou retirer une personne, que faire si on perd l'accès ;
  - un **guide pour faire évoluer la plateforme** avec Claude.
- **Jeu de démonstration** : une vingtaine de fonds fictifs, mais réalistes, avec leurs historiques, leurs maisons et leurs documents d'exemple, pour que je puisse tout tester avant d'y mettre nos vraies données.

Commence par me poser tes questions, puis propose-moi ton plan.
