# 2026-10-14 — Nouvelles rédigées à partir des emails

- **Demande** : relever les news reçues par email depuis le 1/09/2026 et en faire de petits articles pour la page « Nouvelles » d'invest-law.
- **Page Nouvelles** : `GET/POST /api/nouvelles` ; un article = maison (logo affiché), auteur, langue, statut, date, titre, texte HTML (images possibles). Une seule nouvelle existante (test Eleva, id 1).
- **Tri** : 110 fils Gmail depuis le 1/09 ; 58 venant de maisons de gestion ; écartés : confidentiel/interne (stats OneLife, intégration Mandarine), échanges privés, inscriptions nominatives, événements passés, doublons, contenus seulement en PDF joint.
- **Résultat** : 25 brouillons (FR, 120–250 mots, chaque article cite sa source) : marchés, fonds, études, événements à venir. Fichiers : `docs/nouvelles/articles/` ; écartés : `docs/nouvelles/ecartes.txt`. Aperçu : https://claude.ai/artifact/VvpoPNQ86DzBFLrqiXjP1b
- **Rien publié sur le site** — en attente de validation. Points ouverts : mentions de diffusion restreinte (LFDE, DNCA, Robeco, Nordea), maisons absentes du site (Probus Pleion, BNP Paribas AM, Patrimonial Advice), événements du 15/10 (Athymis, Nordea).
- **Veille quotidienne** (demande de l'utilisatrice) : dossier rendu autonome (`docs/nouvelles/` : articles, ecartes.txt, etat.json, CONSIGNE.md ; page générée par `tools/nouvelles_apercu.py`), routine quotidienne créée pour garder la page à jour.
- **Publication des nouvelles** : le bouton « Ajouter » de la page Nouvelles n'apparaît que pour omar@xsreturn.com ou le rôle Maison (code `documentation.js`) ; l'utilisatrice en parlera à Omar.
- **VNI Funds For Good** (mail de Maxime Desaive, 14/10) : fichier VNIs.xlsx récupéré depuis Gmail et analysé (`docs/2026-10-14-vni-funds-for-good.md`) : 10 parts, valeurs réelles et reconstituées (backtest GD, extension GEC, début GELC) ; 7 parts sans VNI sur le site ; décalage d'un jour constaté sur les VNI existantes du site (bug probable). Rien importé.
