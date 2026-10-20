# 2026-10-20 — Page « Gestion des nouvelles »

- **Objectif** : une page commune pour gérer les nouvelles d'invest-law (en attente, validées, publiées…) et voir à quoi elles ressembleraient sur le site.
- **Page** : https://claude.ai/artifact/E3iZyR26aZ5UxhvSoqVn6c (privée tant que la propriétaire ne la partage pas via « Partager »).
  - Compteurs par statut : À valider, À corriger, Validée, Publiée sur le site, Refusée (cliquables pour filtrer).
  - Onglet Gestion : chaque article (texte, points à vérifier), changement de statut, commentaire, historique avec le nom de la personne. Statuts enregistrés dans la base partagée de l'artéfact (collection `statuts`) : tout le monde voit la même chose.
  - Onglet Aperçu sur le site : reprise de la mise en page de la page Actualités d'invest-law.eu (liste à gauche, lecture à droite, mêmes couleurs) ; par défaut seulement les articles validés ou publiés.
  - Onglet Mails non retenus : contenu de `ecartes.txt`.
- **Fichiers** : `tools/nouvelles_gestion.py`, `tools/nouvelles_gestion_modele.html`, `docs/nouvelles/gestion.html` ; consigne de veille mise à jour (`docs/nouvelles/CONSIGNE.md` : régénérer et republier aussi cette page, sans `capabilities` ; tenir compte des statuts).
- **Limites** : l'ancienne page « Nouvelles à valider » (VvpoPNQ86DzBFLrqiXjP1b) n'est pas accessible depuis ce compte, d'où une nouvelle page. Connexion à invest-law.eu refusée (401, identifiants de l'environnement) : nouvelles déjà en ligne non vérifiées ; logos des maisons inaccessibles (réseau), remplacés par les initiales. Tous les articles démarrent « À valider ».

## Origine des articles (demande du 20/10/2026)
- Chaque article porte une étiquette d'origine sur la page de gestion, avec un filtre : **Recherche Claude** (rédigé à partir de recherches de Claude, sources listées sur l'article), **Document fourni** (à partir d'un document donné par l'équipe), **Veille mails** (mails relevés par la routine).
- Champ `"origine"` ajouté aux 33 articles existants (`"veille"`) ; règles et nommage des fichiers dans `docs/nouvelles/CONSIGNE.md`.
- Mise à jour : l'origine devient un sélecteur en tête de page (Veille mails / Document fourni / Recherche Claude, avec le nombre d'articles et une explication) ; les compteurs de statut et l'aperçu suivent l'origine choisie ; les articles « Document fourni » affichent « Demandée par … le … » (champs `demande_par`, `demande_le`).
