# 2026-10-15 — Fiches des maisons de la page d'accueil

## Objectif
Compléter les fiches générales des 10 maisons « Sponsor » affichées sur la page d'accueil d'invest-law.eu (clic sur le logo InvestLaw), à partir de leurs sites officiels, sans toucher aux champs déjà remplis.

## Fait (sur le site, 15/10/2026)
- 49 champs vides remplis sur 9 maisons : Carmignac, DNCA, Funds For Good, Keren Finance, LFDE, Lazard, M&G Investments, ODDO BHF, PTAM. Leleux était déjà complète.
  - 34 champs « prêts » enregistrés vers 09:05 UTC, puis 15 champs « à valider / non vérifiés » vers 09:22 UTC, sur accord explicite de l'utilisatrice.
  - Slogan LFDE : version du site belge (« La proximité d’une boutique, les standards d’une grande maison »), choix de l'utilisatrice.
- Vérification après chaque enregistrement : valeurs identiques aux propositions (le site encode `'` et `&` en entités HTML), aucun autre champ, logo ou contact modifié.
- Rien d'enregistré pour les contacts ni pour le seuil FID d'ODDO BHF.

## Décisions et points d'attention
- Champs laissés vides faute de source officielle : FID de Carmignac, DNCA et Funds For Good ; slogans de Keren Finance, Lazard et M&G.
- Chiffres retirés à la relecture : encours Carmignac (source moteur de recherche seulement), sous-totaux M&G (somme ≠ total), « 7 Md€ » Lazard (non daté).
- Carmignac : site illisible en automatique ; adresse, points forts et partie « fonds externes » viennent de LinkedIn et du moteur de recherche. À relire sur carmignac.com.
- LFDE : champs FID remplis (gestion sous mandat, gestion pilotée), mais le site ne mentionne pas de FID belge ou luxembourgeois.
- Lazard propose des mandats en assurance-vie luxembourgeoise mais n'est pas cochée FID sur le site.
- PTAM = PT Asset Management GmbH (nom de la fiche inchangé).
- Doublon probable : « Altum » (0 fonds) et « Altum Management Company » (1 fonds) ; 4 maisons sans nom (id 83, 97, 102, 111, 0 fonds).

## Fichiers
- `docs/maisons-2026-10-15/propositions.json` : textes, sources, extraits, statut de chaque champ.
- `docs/maisons-2026-10-15/avant-2026-10-15.json`, `avant-2-2026-10-15.json` : état complet des maisons avant chaque enregistrement (pour annuler).
- `docs/maisons-2026-10-15/fiches-maisons-a-valider.html` : page de relecture.
- `tools/maisons_apply.py` : remplit uniquement des champs vides depuis un fichier de propositions (simulation sans `--apply`).

## Liens
- Page de relecture (artefact) : https://claude.ai/artifact/FkxB9bet8thgpvYfyJ3bqe
