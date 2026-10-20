# Veille « Nouvelles » : consigne de la routine quotidienne

Demande de l'utilisatrice (14/10/2026) : chaque jour, relever dans sa boîte Gmail (npo@lifeb2b.com) les nouvelles newsletters et communications des maisons de gestion (point sur un fonds, vue macro / marchés, étude, événement à venir), en faire de petits articles, et garder à jour la page « Nouvelles à valider » :
https://claude.ai/artifact/VvpoPNQ86DzBFLrqiXjP1b

**Rien n'est publié sur invest-law.eu** (la publication des nouvelles attend un réglage côté développeur, voir `docs/sessions/2026-10-14-nouvelles.md`). Aucun mail n'est envoyé, déplacé ni supprimé (sauf le mail du code de connexion invest-law si une connexion a été nécessaire).

## Fichiers
- `articles/<thread_id>.json` : un article par fil retenu — `{"thread", "date_source" (AAAA-MM-JJ), "maison_id" (id invest-law ou null), "maison", "type" ("Marchés"|"Fonds"|"Événement"|"Étude"), "titre", "html", "notes"}`, "origine"}`.
- `"origine"` (consigne du 20/10/2026, la page de gestion affiche une étiquette différente pour chacune) :
  - `"veille"` : mail reçu dans la boîte, relevé par la routine ;
  - `"document"` : rédigé à partir d'un document donné par un membre de l'équipe dans une conversation (PDF, texte, lien, mail désigné) ; fichier `articles/d-AAAAMMJJ-<sujet>.json`, `"thread"` = ce même identifiant (ou l'id du fil Gmail si le document est un mail), `"date_source"` = date du document ;
  - `"recherche"` : rédigé par Claude à partir de ses propres recherches ; uniquement des informations exactes et vérifiables auprès de sources fiables (site de la maison, communiqué officiel, presse financière reconnue), recoupées si possible ; fichier `articles/r-AAAAMMJJ-<sujet>.json` ; ajouter `"sources": [{"titre", "url"}]` (obligatoire) ; dernière ligne « Source : … » avec ces sources.
- `ecartes.txt` : une ligne par fil écarté — `thread | sujet | raison`.
- `etat.json` : `derniere_verification` (date) et `fils_traites` (tous les thread id déjà examinés, retenus ou écartés).
- `apercu.html` : généré par `python3 tools/nouvelles_apercu.py` (ne pas l'éditer à la main ; le modèle est `tools/nouvelles_apercu_modele.html`).
- `gestion.html` : page « Gestion des nouvelles » (https://claude.ai/artifact/E3iZyR26aZ5UxhvSoqVn6c, créée le 20/10/2026), générée par `python3 tools/nouvelles_gestion.py` (modèle `tools/nouvelles_gestion_modele.html`). L'équipe y règle le statut de chaque article (À valider, À corriger, Validée, Publiée sur le site, Refusée) avec commentaire et historique ; ces statuts sont dans la base partagée de l'artéfact (collection `statuts`, une fiche par `thread`), pas dans le dépôt. Elle montre aussi un aperçu au format de la page Actualités du site et la liste des mails non retenus.

## Information de l'utilisatrice (15/10/2026)
Il arrive qu'elle voie un mail sans l'avoir pour autant traité : un mail lu, ouvert ou répondu n'est pas un mail déjà transformé en article. Il faut donc analyser sérieusement la boîte ET l'artefact, et relever ce qui n'a réellement pas été fait : ne pas se fier à l'état lu/non lu, ni seulement à `fils_traites` ; comparer les fils de la boîte avec les articles de l'artefact en ligne (le lire d'abord) et avec `articles/` et `ecartes.txt`. Un fil absent de l'artefact et jugeable à retenir doit être traité, même s'il est ancien ou déjà lu. Inversement, l'artefact en ligne peut contenir des articles absents du dépôt : éviter les doublons.

## Étapes
1. Intégrer la branche par défaut, lire `AGENTS.md` et les dernières notes de `docs/sessions/`.
2. Gmail : chercher les fils reçus depuis `derniere_verification` moins 1 jour (`after:AAAA/MM/JJ -in:sent -from:info@invest-law.eu`), en ignorant ceux déjà dans `fils_traites`. Lire chaque candidat (get_thread, PLAIN_TEXT). Les newsletters arrivent souvent transférées par lla@lifeb2b.com ou tli@lifeb2b.com (« Fwd: … ») : c'est l'émetteur d'origine qui compte.
3. Retenir : commentaire de marché ou macro, vue d'un gérant, reporting / mise à jour d'un fonds, nouveau fonds, lettre ou étude d'une maison, événement À VENIR annoncé par la maison.
   Écarter : tout ce qui est marqué confidentiel / usage interne / ne pas diffuser ; communications internes OneLife ; échanges personnels ou commerciaux privés, confirmations d'inscription nominatives, relances de rendez-vous ; données clients ; factures, livraisons, outils ; événements déjà passés ; doublons (un seul article par sujet) ; contenu uniquement dans une pièce jointe illisible.
4. Rédiger en français : titre ≤ 90 caractères ; corps 120–250 mots, en ses propres mots (courtes citations attribuées seulement) ; chiffres, dates, noms de fonds et de gérants exactement comme dans le mail, rien d'inventé, pas d'avis ni de recommandation, chiffre ambigu = on ne le met pas ; événement : quoi, qui, quand, format (pas de lien d'inscription personnel) ; dernière ligne « Source : <maison>, <type de document>, <date> » ; HTML simple (`<p>`, `<ul><li>`, `<strong>`). Mettre dans "notes" tout doute (diffusion restreinte, maison absente du site, pièce jointe non lue…).
5. Maison : `maison_id` d'après `GET /api/maisons` d'invest-law (connexion : skill invest-law) ; si aucune correspondance claire, `null` et le nom dans "maison". Si la connexion échoue, laisser `maison_id` comme dans les articles existants de la même maison, ou `null`.
6. Mettre à jour `etat.json` (date du jour, ajouter tous les fils examinés), `ecartes.txt`, puis `python3 tools/nouvelles_apercu.py` et `python3 tools/nouvelles_gestion.py`.
7. Republier la page au même lien : outil Artifact, `url` = https://claude.ai/artifact/VvpoPNQ86DzBFLrqiXjP1b (la lire d'abord avec `action: "read"`, puis publier `docs/nouvelles/apercu.html` avec ce `url`). Ne jamais créer une nouvelle page. Republier aussi `docs/nouvelles/gestion.html` au lien https://claude.ai/artifact/E3iZyR26aZ5UxhvSoqVn6c (lire d'abord, publier avec ce `url`, **sans** paramètre `capabilities` pour garder la base des statuts). Si le compte n'a pas l'accès en modification à l'une des pages, ne pas en créer de copie : le signaler dans la note de session.
8. Note de session `docs/sessions/AAAA-MM-JJ-veille-nouvelles.md` (nombre de fils vus, articles ajoutés avec titres, écartés), commit, push, demande de fusion vers la branche par défaut et fusion (méthode « merge »), comme le prévoit `AGENTS.md`.
9. S'il n'y a aucun nouveau fil : mettre seulement à jour `derniere_verification`, régénérer et republier la page (date de vérification), courte note de session, fusion.

## Statuts posés par l'équipe (20/10/2026)
Avant de rédiger, lire la collection `statuts` de la page de gestion (outil ArtifactData, `list`) : un article « À corriger » se corrige d'après le commentaire laissé, puis on remet son statut à « À valider » ; ne jamais changer soi-même un statut « Validée », « Publiée » ou « Refusée ».
