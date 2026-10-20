# Veille « Nouvelles » : consigne de la routine quotidienne

~~Deux boîtes à relever (demande du 20/10/2026)~~ (consigne d'une autre session du 20/10/2026, remplacée par la suivante)

> **Changement du 20/10/2026 (demande de Louis)** : la veille lit **uniquement la boîte data@invest-law.eu** (Zimbra, `tools/zimbra_mail.py`, lecture seule ; réglage : `docs/2026-10-19-guide-zimbra.md`). La boîte Gmail npo@lifeb2b.com n'est plus utilisée. Les articles Gmail déjà rédigés restent dans `articles/` (`"boite": "npo@lifeb2b.com"`) mais ne sont plus affichés ; l'ancienne page « Nouvelles à valider » (VvpoPNQ86DzBFLrqiXjP1b), ainsi que `ecartes.txt`, `etat.json` et `tools/nouvelles_apercu.py`, ne sont plus mis à jour. La page de suivi est désormais la page « Gestion des nouvelles » : https://claude.ai/artifact/E3iZyR26aZ5UxhvSoqVn6c

Demande de l'utilisatrice (14/10/2026) : chaque jour, relever dans sa boîte Gmail (npo@lifeb2b.com) les nouvelles newsletters et communications des maisons de gestion (point sur un fonds, vue macro / marchés, étude, événement à venir), en faire de petits articles, et garder à jour la page « Nouvelles à valider » :
https://claude.ai/artifact/VvpoPNQ86DzBFLrqiXjP1b

**Rien n'est publié sur invest-law.eu** (la publication des nouvelles attend un réglage côté développeur, voir `docs/sessions/2026-10-14-nouvelles.md`). Aucun mail n'est envoyé, déplacé ni supprimé (sauf le mail du code de connexion invest-law si une connexion a été nécessaire).

## Fichiers
- `articles/<thread_id>.json` : un article par fil retenu — `{"thread", "date_source" (AAAA-MM-JJ), "maison_id" (id invest-law ou null), "maison", "type" ("Marchés"|"Fonds"|"Événement"|"Étude"), "titre", "html", "notes"}`, "origine"}`.
- `"origine"` (consigne du 20/10/2026, la page de gestion affiche une étiquette différente pour chacune) :
  - `"veille"` : mail reçu dans la boîte, relevé par la routine ;
  - `"document"` : rédigé à partir d'un document donné par un membre de l'équipe dans une conversation (PDF, texte, lien, mail désigné) ; fichier `articles/d-AAAAMMJJ-<sujet>.json`, `"thread"` = ce même identifiant (ou l'id du fil Gmail si le document est un mail), `"date_source"` = date du document ; ajouter `"demande_par"` (prénom de la personne qui a donné le document) et `"demande_le"` (AAAA-MM-JJ, date de la demande), affichés sur la page pour distinguer ces articles de ceux de la veille ;
  - `"recherche"` : rédigé par Claude à partir de ses propres recherches ; uniquement des informations exactes et vérifiables auprès de sources fiables (site de la maison, communiqué officiel, presse financière reconnue), recoupées si possible ; fichier `articles/r-AAAAMMJJ-<sujet>.json` ; ajouter `"sources": [{"titre", "url"}]` (obligatoire) ; dernière ligne « Source : … » avec ces sources.
- Champ `"boite"` : `"data@invest-law.eu"` pour la veille (obligatoire, sinon l'article n'est pas affiché) ; `"thread"` = `z-<id du message>` ; fichier `articles/z-<id>.json`.
- `ecartes-data.txt` : une ligne par mail écarté — `thread | sujet | raison`.
- `etat-data.json` : `derniere_verification` (date) et `fils_traites` (ids Zimbra déjà examinés, retenus ou écartés).
- Anciens fichiers de la veille Gmail (plus mis à jour) : `ecartes.txt`, `etat.json`.
- `apercu.html` : généré par `python3 tools/nouvelles_apercu.py` (ne pas l'éditer à la main ; le modèle est `tools/nouvelles_apercu_modele.html`).
- `gestion.html` : page « Gestion des nouvelles » (https://claude.ai/artifact/E3iZyR26aZ5UxhvSoqVn6c, créée le 20/10/2026), générée par `python3 tools/nouvelles_gestion.py` (modèle `tools/nouvelles_gestion_modele.html`). L'équipe y règle le statut de chaque article (À valider, À corriger, Validée, Publiée sur le site, Refusée) avec commentaire et historique ; ces statuts sont dans la base partagée de l'artéfact (collection `statuts`, une fiche par `thread`), pas dans le dépôt. Elle montre aussi un aperçu au format de la page Actualités du site et la liste des mails non retenus.

## Information de l'utilisatrice (15/10/2026)
Il arrive qu'elle voie un mail sans l'avoir pour autant traité : un mail lu, ouvert ou répondu n'est pas un mail déjà transformé en article. Il faut donc analyser sérieusement la boîte ET l'artefact, et relever ce qui n'a réellement pas été fait : ne pas se fier à l'état lu/non lu, ni seulement à `fils_traites` ; comparer les fils de la boîte avec les articles de l'artefact en ligne (le lire d'abord) et avec `articles/` et `ecartes.txt`. Un fil absent de l'artefact et jugeable à retenir doit être traité, même s'il est ancien ou déjà lu. Inversement, l'artefact en ligne peut contenir des articles absents du dépôt : éviter les doublons.

## Étapes
1. Intégrer la branche par défaut, lire `AGENTS.md` et les dernières notes de `docs/sessions/`.
2. Zimbra : `python3 tools/zimbra_mail.py list 200 --query "after:MM/JJ/AAAA"` (date = `derniere_verification` de `etat-data.json` moins 1 jour), en ignorant les ids déjà dans `fils_traites`. Ignorer les envois de VNI (DNCA « Valeurs Liquidatives » / « Sub Fund NAV », CACEIS « Autoreport »…), traités par la routine VNI. Lire chaque candidat : `python3 tools/zimbra_mail.py get <id> --save <dossier du scratchpad>` (texte + pièces jointes ; lire les PDF joints, ils contiennent souvent l'essentiel). Les newsletters arrivent souvent transférées (« Fwd: … ») par lla@lifeb2b.com : c'est l'émetteur d'origine qui compte.
3. Retenir : commentaire de marché ou macro, vue d'un gérant, reporting / mise à jour d'un fonds, nouveau fonds, lettre ou étude d'une maison, événement À VENIR annoncé par la maison.
   Écarter : tout ce qui est marqué confidentiel / usage interne / ne pas diffuser ; communications internes OneLife ; échanges personnels ou commerciaux privés, confirmations d'inscription nominatives, relances de rendez-vous ; données clients ; factures, livraisons, outils ; événements déjà passés ; doublons (un seul article par sujet) ; contenu uniquement dans une pièce jointe illisible.
4. Rédiger en français : titre ≤ 90 caractères ; corps 120–250 mots, en ses propres mots (courtes citations attribuées seulement) ; chiffres, dates, noms de fonds et de gérants exactement comme dans le mail, rien d'inventé, pas d'avis ni de recommandation, chiffre ambigu = on ne le met pas ; événement : quoi, qui, quand, format (pas de lien d'inscription personnel) ; dernière ligne « Source : <maison>, <type de document>, <date> » ; HTML simple (`<p>`, `<ul><li>`, `<strong>`). Mettre dans "notes" tout doute (diffusion restreinte, maison absente du site, pièce jointe non lue…).
5. Maison : `maison_id` d'après `GET /api/maisons` d'invest-law (connexion : skill invest-law) ; si aucune correspondance claire, `null` et le nom dans "maison". Si la connexion échoue, laisser `maison_id` comme dans les articles existants de la même maison, ou `null`.
6. Mettre à jour `etat-data.json` (date du jour, ajouter tous les ids examinés), `ecartes-data.txt`, puis `python3 tools/nouvelles_gestion.py`.
7. Republier la page de gestion au même lien : outil Artifact, `url` = https://claude.ai/artifact/E3iZyR26aZ5UxhvSoqVn6c (la lire d'abord avec `action: "read"`, puis publier `docs/nouvelles/gestion.html` avec ce `url`, **sans** paramètre `capabilities` pour garder la base des statuts). Ne jamais créer une nouvelle page ; si le compte n'a pas l'accès en modification, le signaler dans la note de session.
8. Note de session `docs/sessions/AAAA-MM-JJ-veille-nouvelles.md` (nombre de fils vus, articles ajoutés avec titres, écartés), commit, push, demande de fusion vers la branche par défaut et fusion (méthode « merge »), comme le prévoit `AGENTS.md`.
9. S'il n'y a aucun nouveau fil : mettre seulement à jour `derniere_verification`, régénérer et republier la page (date de vérification), courte note de session, fusion.

## Statuts posés par l'équipe (20/10/2026)
Avant de rédiger, lire la collection `statuts` de la page de gestion (outil ArtifactData, `list`) : un article « À corriger » se corrige d'après le commentaire laissé, puis on remet son statut à « À valider » ; ne jamais changer soi-même un statut « Validée », « Publiée » ou « Refusée ».
