# 2026-10-17 — Authentification du classeur « Gamme One Life complète »

- **Demande** : vérifier que chaque information du Google Sheet vient de la factsheet la plus récente ou du KID du fonds, et rendre le verdict dans un artefact.
- **Méthode** (`docs/authentification-2026-10-17/`) :
  1. `authentifier.py` : chaque case remplie de l'onglet Fiches et chaque ligne d'Allocations cherchée dans le texte de la factsheet utilisée (440 PDF du site retéléchargés, PDF du dépôt) et du KID. 11 120 cases : 7 853 retrouvées automatiquement.
  2. Relecture des 1 685 cases et 384 blocs d'allocations non retrouvés, PDF et images des pages, en 8 lots de 71 fonds (`CONSIGNE-relecture.md`, verdicts dans `relecture/`).
  3. `consolider.py` : second contrôle dans le KID publié sur fundinfo (416 KID téléchargés pour les fiches du site), fraîcheur comparée à la liste fundinfo des rapports mensuels et KID FR/EN.
- **Résultat** : 9 018 cases conformes (93 % des cases vérifiables), 160 contredisent le document, 452 absentes de la factsheet et du KID, 116 catégories du site hors fichier One Life, 1 374 synthèses (type, classification).
  - Fiches préparées par nos soins (Wealth Belgium 336, fiches du 16/10 28) : **toutes authentifiées**.
  - Fiches invest-law.eu (463) : 179 authentifiées, 146 à corriger (au moins une valeur contredit le document), 138 source incomplète.
  - Causes principales sur le site : encours d'une autre date (75 cases), factsheet d'une autre part (14 fonds), dernier document publié = KID et non factsheet (86 fonds), textes rédigés ou résumés (politiques, disclaimers), gérants absents des documents.
  - Fraîcheur : 177 fonds ont une factsheet plus récente sur fundinfo (134 du site, 42 Wealth Belgium, 1 du 16/10), en général celle de fin septembre parue depuis.
- **Fichiers** : `resultat.json` (verdict par case), `ecarts.csv` (tous les écarts, avec valeur du document et note), `passage-automatique.json`, page `authentification-gamme-one-life.html`.
- **Artefact** : https://claude.ai/artifact/7GsXisc2YK4wPHHni72WLx (privé tant qu'il n'est pas partagé).
- Rien modifié sur invest-law.eu ni dans le Google Sheet.
