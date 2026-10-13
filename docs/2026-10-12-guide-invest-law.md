# Guide invest-law.eu (site + API)

Cartographié le 12/10/2026 à partir du code des pages (`*.html`, `*.js`) du site, avec le compte `npo@lifeb2b.com` (rôle **Data**).
Outils : `tools/investlaw_upload.py` (connexion, upload en masse des factsheets) et `tools/investlaw.py` (lecture, modification et suppression sur une fiche, appel brut à l'API).

## 1. Connexion

- Identifiants : variables d'environnement `INVESTLAW_EMAIL` et `INVESTLAW_PASSWORD` (jamais dans le dépôt ni dans le chat).
- `python3 tools/investlaw_upload.py login` envoie un code à 6 chiffres par email, venant de `info@invest-law.eu`. Claude le lit via Gmail (`from:info@invest-law.eu newer_than:15m`). Il faut prendre le **dernier** code reçu, qui expire au bout de 10 minutes.
- `python3 tools/investlaw_upload.py verify <code>` enregistre les cookies dans `~/.investlaw/cookies.txt`, partagés par les deux scripts.
- Une fois connecté, mettre à la corbeille le mail du code utilisé (consigne du 13/10/2026 : le code ne sert plus).
- Si une commande renvoie 401, la session a expiré : refaire `login` puis `verify`. Une connexion depuis un autre poste peut aussi invalider la session.
- `GET /api/session` renvoie l'utilisateur, son rôle et la date d'expiration de la session.

## 2. Rôles

| Rôle | Peut |
|---|---|
| Responsable | tout, plus Administration (`admin.html`), utilisateurs, activité et relances |
| **Data** (notre compte) | modifier les fonds, rapports, commentaires, VNI, benchmarks, contenus (nouvelles, documentation) ; Importer VNI |
| Maison | sa propre maison et ses fonds (documentation, simulation, profil maison) |
| Courtier | lecture |

## 3. Pages (menu)

| Page | Contenu |
|---|---|
| `index.html` | Accueil |
| `documentation.html` | « Nouvelles » des maisons (articles avec images) |
| `simulation.html` | **Liste des Fonds** + fiche fonds (`?fundId=<id>`). Onglets : Fiche Fonds, Historique VNI, Commentaires Analystes, Comparateur, Rapport PB |
| `MaisonsGestion.html` | Maisons de gestion (fiche, contacts, fonds) |
| `banques-depositaires.html` | Banques dépositaires (fiche, documents, maisons partenaires) |
| `agenda.html`, `portfolio-builder.html`, `portfolio-analyzer.html` | Outils embarqués (URL fournie par l'API) |
| `simulation-taxe.html`, `planification-arbre.html` | Partie LAW : simulation fiscale, arbre de décision |
| `frais-fiscalite.html` | Documentation frais et fiscalité (contenus avec fichier) |
| `importer-vni.html` | Import en masse des VNI au format CSV `ISIN,Date,VNI` |
| `setting.html` | Profil : nom, mobile, langue, avatar, email, mot de passe |
| `admin.html`, `utilisateurs.html`, `activity.html` | Réservées au rôle Responsable |

## 4. API (JSON, cookies de session)

Les fichiers s'envoient en JSON, en base64 : `file_name` + `file_data`. Les dates sont au format `AAAA-MM-JJ`.

### Fonds
- `GET /api/funds` : **toutes** les fiches (488), avec tous leurs champs. Il n'existe pas de `GET /api/funds/{id}`.
- `POST /api/funds` crée une fiche ; `PUT /api/funds/{id}` la modifie. **Le PUT remplace toute la fiche**, allocations comprises. Il faut donc toujours repartir de l'état actuel : `tools/investlaw.py set` le fait.
  Correspondance entre le corps du PUT et les clés du GET : `classification_id`←ClassificationId, `category`←Category, `fid`←FID (0 = externe, 1 = interne), `is_active`←IsActive, `maison_id`←MaisonId, `banque_id`←BanqueId (envoyé seulement si FID=1), `name`, `isin`, `fund_code`←FundCode, `creation_date`, `currency`, `fund_type`, `fund_manager`, `fund_analyst`, `compartment`, `total_assets`←TotalAssets (millions), `fees`, `ter`, `benchmark_id`←BenchmarkId, `disclaimer`, `investment_policy` = `investment_policy_fr`←InvestmentPolicy (HTML simple : `<br>`, `<p>`, `<li>`…), `investment_policy_en`, `investment_policy_nl`, `duration`, `issuer_quality`, `esg`, `esg_code`, `last_update`, `risque` (SRI 1–7), et `positions`, `sectors`, `assets`, `geographies`, chacun sous forme de liste `[{name, percentage}]`.
- `GET /api/funds/{id}/allocations` : positions, secteurs, actifs, zones. Le `name` d'un secteur ou d'une zone est une clé en anglais (ex. `Information Technology`) ; le site affiche la traduction.
- `PUT /api/funds/{id}/ponderation` `{ponderation}` modifie la colonne Pondération de la liste.
- `POST /api/funds/{id}/investment-policy/translate` `{source_language, target_language, source_text}` traduit automatiquement la politique d'investissement.
- `GET /api/classifications` donne la liste des classifications ; `GET /api/maisons/options` celle des maisons ; `GET /api/benchmarks` celle des benchmarks.

### Rapports de gestion (section de la fiche)
- `GET /api/funds/{id}/reports` renvoie une liste de `{report_name, file_name, report_date, file_url}`.
- `POST /api/funds/{id}/reports` `{report_name, report_date, file_name, file_data}` ajoute un rapport.
- `DELETE /api/funds/{id}/reports` `{report_name, file_name, report_date}` supprime un rapport (c'est la croix).
- ⚠️ La date affichée pour un rapport existant est souvent sa **date d'upload**, pas le mois couvert. Pour savoir quel mois couvre un rapport, il faut lire son **nom** (« Rapport de gestion Août 2026 »).
- Conventions de nom : « Rapport de Gestion <Mois> <Année> » ou « Rapport hebdomadaire … ».

### Commentaires analystes
- `GET/POST /api/funds/{id}/comments` `{date, analyst_name, analyst_comment}`
- `PUT/DELETE /api/funds/{id}/comments/{cid}`

### VNI (valeurs liquidatives)
- `GET /api/funds/{id}/vl` lit les VNI ; `PUT /api/funds/{id}/vl?month=AAAA-MM` `{entries}` les modifie pour un mois.
- `POST /api/funds/{id}/vl/upload` `{csv}` importe un CSV `date,valeur`.
- `POST /api/funds/{id}/vl/import` lance l'import automatique.
- `POST /api/funds/vl/upload-by-isin` `{csv}` importe pour plusieurs fonds à la fois, au format `ISIN,Date,VNI`. `GET /api/funds/latest-vl` donne la dernière VNI de chaque fonds.
- Benchmarks : `POST /api/benchmarks` et `PUT /api/benchmarks/{id}` `{benchmark_code, benchmark_name}`, `GET /api/benchmarks/{id}/vni`, `PUT …/vni?month=`, `POST …/vni/upload` `{csv}`.

### Maisons de gestion
- `GET /api/maisons`, `POST /api/maisons`, `PUT/DELETE /api/maisons/{id}`, `GET /api/maisons/{id}/contacts|funds|funds/count`.
- Champs : name, adresse, slogan, sponsor, site, fid, fonds_externes, points_forts, fid_specialites, fid_type_gestion, fonds_externes_description, fonds_externes_specialites, fonds_externes_type_gestion, fid_seuil, logo, et les contacts (`contact_id`, name, email, tel, langue, photo).

### Banques dépositaires
- `GET/POST /api/banques-depositaires`, `GET/PUT/DELETE /api/banques-depositaires/{id}`.
- Documents : `GET/POST …/{id}/documents` `{document_name, file_name, file_data}` et `DELETE …/{id}/documents/{doc}`.
- `GET …/{id}/funds/count` et `GET …/{id}/partner-maisons`.

### Contenus
- Nouvelles : `GET/POST /api/nouvelles`, `GET/PUT/DELETE /api/nouvelles/{id}` `{maison_id, auteur, langue, status, creation_date, titre, nouvelle}`. Images : `POST /api/nouvelles/images` `{file_name, content_type, file_data}`.
- Frais et fiscalité : `GET/POST /api/documentation`, `GET/PUT/DELETE /api/documentation/{id}` `{title, author, badge, status, creation_date}`, `PUT /api/documentation/{id}/content` (fichier).

### Compte
- `PUT /api/users/{id}` modifie `{name}`, `{mobile}`, `{langue}` ou `{avatar}`.
- Changement d'email ou de mot de passe : `/api/settings/email|password/request` puis `/verify`, avec un code envoyé par email.
- `POST /api/logout` ferme la session.

## 5. Recettes (`tools/investlaw.py`)

```
python3 tools/investlaw.py fund LU0231459107                 # fiche + allocations + rapports + commentaires
python3 tools/investlaw.py set LU0231459107 fees=1.80 risque=4   # simulation : ancien -> nouveau
python3 tools/investlaw.py set LU0231459107 --json maj.json --apply   # maj.json : {"positions":[{"name":"X","percentage":"4.4"}], ...}
python3 tools/investlaw.py delete-report <ISIN> <file_name> --apply
python3 tools/investlaw.py call GET /api/maisons            # tout autre appel de la section 4
```

- **Upload de factsheets en masse** : suivre `INVESTLAW/LISEZMOI.md` (`plan`, puis `upload --limit 1` à valider, puis `upload`).
- **Mise à jour d'une fiche depuis un PDF** : lire le PDF, préparer les champs, lancer `set` sans `--apply` et montrer le tableau ancien → nouveau à l'utilisateur, puis relancer avec `--apply`. L'outil relit la fiche après l'enregistrement et liste les écarts. `set --apply` est validé (fiche 387, 12/10/2026) : seul le champ visé change, allocations et rapports intacts. ⚠️ Le serveur remet `last_update` (« Mise à jour ») à la date du jour à chaque enregistrement, même si on ne le modifie pas.
- **Prudence** : chaque écriture modifie la base de production, que voient tous les utilisateurs. Avant toute suppression, vérifier qu'il s'agit bien d'un doublon. Ne pas supprimer le travail d'autres personnes sans accord.

## 6. Règles métier (consignes de l'équipe)

- **Fonds internes et mandats sans document public** : fonds FID (FID=1), fonds internes d'assurance (ISIN `XFCS…`), mandats DNCA, Leleux Secu, Keren, Rothschild & Co FID, portefeuilles modèles Leleux FMP. Il est normal qu'ils n'aient pas de factsheet : ne pas les compter comme des manques dans les audits.
- **Recherche d'une factsheet** : d'abord le site du gestionnaire (source d'origine), sinon Morningstar ou fundinfo. Contrôles obligatoires avant de retenir un PDF :
  1. l'ISIN de la part figure dans le PDF ;
  2. la date du document est la plus récente disponible ;
  3. le PDF vient directement de l'émetteur ou d'une base reconnue, pas d'un site tiers qui le recopie ;
  4. la part est exactement celle de la fiche, pas une autre classe du même fonds.
- Les documents trouvés sont ajoutés dans `INVESTLAW/` avant tout upload ou remplissage des fiches.
- **Priorité absolue à l'exactitude** (consigne du 13/10/2026) : si aucun document original et conforme n'est trouvé, on laisse le fonds sans factsheet, tant pis. Jamais de document d'une autre part, recopié par un site tiers ou douteux : mieux vaut une fiche incomplète qu'une information fausse sur invest-law.eu. Même règle pour les champs des fiches : en cas de doute, on ne remplit pas.
- Après chaque connexion, mettre à la corbeille le mail du code utilisé.
