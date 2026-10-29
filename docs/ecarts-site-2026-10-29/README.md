# Écarts entre invest-law.eu et le classeur « Gamme One Life complète » (29/10/2026)

- **Site** : lu le 29/10/2026 par `GET /api/funds` (lecture seule, rien modifié). **Classeur** : onglet Fiches (CSV `docs/gamme-complete-2026-10-16/sheet/`, identiques au Google Sheet).
- Fichier : `ecarts-site-classeur.xlsx` (onglets Synthèse, Écarts, Autres points). Script : `comparer.py`.
- Colonnes : « Avant (site) » → « Après (classeur) », **Type** (à corriger / à remplir / à vider) et **Nature** :
  - *Valeur* : un chiffre ou une valeur courte change (encours, frais, SRI, classification, SFDR, indice, dates…) ;
  - *Texte* : texte rédigé différent (type de fonds, compartiment, disclaimer, politiques) — le site a souvent des textes reformulés, le classeur des copies exactes des documents ;
  - *Forme* : même contenu écrit autrement (ordre des gérants, « 0.52 » / « 0.52 ans »…).

## Chiffres
- 463 fiches du site comparées (présentes dans le classeur) : **78 identiques, 385 avec au moins un écart**.
- 2 984 écarts : 1 853 à corriger, 556 à remplir (vide sur le site), 575 à vider (le site a une valeur que les documents ne donnent pas). Par nature : 1 507 Valeur, 1 428 Texte, 49 Forme.
- Champs les plus touchés : type de fonds (281), politique FR (271), compartiment (268), encours (244), disclaimer (202), indice (162), classification (87 à corriger + 97 à remplir), frais courants (73), duration (69).

## Autres points (onglet « Autres points »)
- 25 fiches du site absentes du classeur (hors gamme One Life : mandats/profils FID, portefeuilles modèles Leleux, fonds retirés de la gamme, Carmignac Grandchildren à l'ISIN tronqué).
- 16 ISIN invalides (dont « LU196663100 » tronqué, « KER--- », « LU373 », zéros des mandats FID, codes internes OneLife « XFCS… » des fonds FIC).
- 167 fiches externes sans classification, 74 sans SRI.
- 3 classifications contraires au risque : Lazard Patrimoine SRI (Dynamique, SRI 2), Allianz Securicash (Dynamique, SRI 1), Fid-keren-gestion-défensif (Sécuritaire, SRI 4).

## À décider avant tout report sur le site
- **Textes** (politique, disclaimer, compartiment, type de fonds) : remplacer les textes reformulés du site par les textes exacts des documents, ou ne reporter que les valeurs ?
- **« À vider »** : le classeur vide ce que les documents ne donnent pas (règle « mieux vaut incomplet que faux »). Cas sensibles : 105 politiques EN du site (traductions ?), 103 frais de gestion, 81 indices, 17 dates de création.
- Le report se fait fiche par fiche avec `tools/investlaw.py set` (ancien → nouveau montré avant `--apply`).
