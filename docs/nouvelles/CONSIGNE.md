# Veille « Nouvelles » : consigne de la routine quotidienne

Demande de l'utilisatrice (14/10/2026) : chaque jour, relever dans sa boîte Gmail (npo@lifeb2b.com) les nouvelles newsletters et communications des maisons de gestion (point sur un fonds, vue macro / marchés, étude, événement à venir), en faire de petits articles, et garder à jour la page « Nouvelles à valider » :
https://claude.ai/artifact/VvpoPNQ86DzBFLrqiXjP1b

**Rien n'est publié sur invest-law.eu** (la publication des nouvelles attend un réglage côté développeur, voir `docs/sessions/2026-10-14-nouvelles.md`). Aucun mail n'est envoyé, déplacé ni supprimé (sauf le mail du code de connexion invest-law si une connexion a été nécessaire).

## Fichiers
- `articles/<thread_id>.json` : un article par fil retenu — `{"thread", "date_source" (AAAA-MM-JJ), "maison_id" (id invest-law ou null), "maison", "type" ("Marchés"|"Fonds"|"Événement"|"Étude"), "titre", "html", "notes"}`.
- `ecartes.txt` : une ligne par fil écarté — `thread | sujet | raison`.
- `etat.json` : `derniere_verification` (date) et `fils_traites` (tous les thread id déjà examinés, retenus ou écartés).
- `apercu.html` : généré par `python3 tools/nouvelles_apercu.py` (ne pas l'éditer à la main ; le modèle est `tools/nouvelles_apercu_modele.html`).

## Information de l'utilisatrice (15/10/2026)
Il arrive qu'elle voie un mail sans l'avoir pour autant traité : un mail lu, ouvert ou répondu n'est pas un mail déjà transformé en article. Il faut donc analyser sérieusement la boîte ET l'artefact, et relever ce qui n'a réellement pas été fait : ne pas se fier à l'état lu/non lu, ni seulement à `fils_traites` ; comparer les fils de la boîte avec les articles de l'artefact en ligne (le lire d'abord) et avec `articles/` et `ecartes.txt`. Un fil absent de l'artefact et jugeable à retenir doit être traité, même s'il est ancien ou déjà lu. Inversement, l'artefact en ligne peut contenir des articles absents du dépôt : éviter les doublons.

## Étapes
1. Intégrer la branche par défaut, lire `AGENTS.md` et les dernières notes de `docs/sessions/`.
2. Gmail : chercher les fils reçus depuis `derniere_verification` moins 1 jour (`after:AAAA/MM/JJ -in:sent -from:info@invest-law.eu`), en ignorant ceux déjà dans `fils_traites`. Lire chaque candidat (get_thread, PLAIN_TEXT). Les newsletters arrivent souvent transférées par lla@lifeb2b.com ou tli@lifeb2b.com (« Fwd: … ») : c'est l'émetteur d'origine qui compte.
3. Retenir : commentaire de marché ou macro, vue d'un gérant, reporting / mise à jour d'un fonds, nouveau fonds, lettre ou étude d'une maison, événement À VENIR annoncé par la maison.
   Écarter : tout ce qui est marqué confidentiel / usage interne / ne pas diffuser ; communications internes OneLife ; échanges personnels ou commerciaux privés, confirmations d'inscription nominatives, relances de rendez-vous ; données clients ; factures, livraisons, outils ; événements déjà passés ; doublons (un seul article par sujet) ; contenu uniquement dans une pièce jointe illisible.
4. Rédiger en français : titre ≤ 90 caractères ; corps 120–250 mots, en ses propres mots (courtes citations attribuées seulement) ; chiffres, dates, noms de fonds et de gérants exactement comme dans le mail, rien d'inventé, pas d'avis ni de recommandation, chiffre ambigu = on ne le met pas ; événement : quoi, qui, quand, format (pas de lien d'inscription personnel) ; dernière ligne « Source : <maison>, <type de document>, <date> » ; HTML simple (`<p>`, `<ul><li>`, `<strong>`). Mettre dans "notes" tout doute (diffusion restreinte, maison absente du site, pièce jointe non lue…).
5. Maison : `maison_id` d'après `GET /api/maisons` d'invest-law (connexion : skill invest-law) ; si aucune correspondance claire, `null` et le nom dans "maison". Si la connexion échoue, laisser `maison_id` comme dans les articles existants de la même maison, ou `null`.
6. Mettre à jour `etat.json` (date du jour, ajouter tous les fils examinés), `ecartes.txt`, puis `python3 tools/nouvelles_apercu.py`.
7. Republier la page au même lien : outil Artifact, `url` = https://claude.ai/artifact/VvpoPNQ86DzBFLrqiXjP1b (la lire d'abord avec `action: "read"`, puis publier `docs/nouvelles/apercu.html` avec ce `url`). Ne jamais créer une nouvelle page.
8. Note de session `docs/sessions/AAAA-MM-JJ-veille-nouvelles.md` (nombre de fils vus, articles ajoutés avec titres, écartés), commit, push, demande de fusion vers la branche par défaut et fusion (méthode « merge »), comme le prévoit `AGENTS.md`.
9. S'il n'y a aucun nouveau fil : mettre seulement à jour `derniere_verification`, régénérer et republier la page (date de vérification), courte note de session, fusion.
