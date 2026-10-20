# 2026-10-20 — Page « Gestion des nouvelles »

- **Objectif** : une page commune pour gérer les nouvelles d'invest-law (en attente, validées, publiées…) et voir à quoi elles ressembleraient sur le site.
- **Page** : https://claude.ai/artifact/E3iZyR26aZ5UxhvSoqVn6c (privée tant que la propriétaire ne la partage pas via « Partager »).
  - Compteurs par statut : À valider, À corriger, Validée, Publiée sur le site, Refusée (cliquables pour filtrer).
  - Onglet Gestion : chaque article (texte, points à vérifier), changement de statut, commentaire, historique avec le nom de la personne. Statuts enregistrés dans la base partagée de l'artéfact (collection `statuts`) : tout le monde voit la même chose.
  - Onglet Aperçu sur le site : reprise de la mise en page de la page Actualités d'invest-law.eu (liste à gauche, lecture à droite, mêmes couleurs) ; par défaut seulement les articles validés ou publiés.
  - Onglet Mails non retenus : contenu de `ecartes.txt`.
- **Fichiers** : `tools/nouvelles_gestion.py`, `tools/nouvelles_gestion_modele.html`, `docs/nouvelles/gestion.html` ; consigne de veille mise à jour (`docs/nouvelles/CONSIGNE.md` : régénérer et republier aussi cette page, sans `capabilities` ; tenir compte des statuts).
- **Limites** : l'ancienne page « Nouvelles à valider » (VvpoPNQ86DzBFLrqiXjP1b) n'est pas accessible depuis ce compte, d'où une nouvelle page. Connexion à invest-law.eu refusée (401, identifiants de l'environnement) : nouvelles déjà en ligne non vérifiées ; logos des maisons inaccessibles (réseau), remplacés par les initiales. Tous les articles démarrent « À valider ».
