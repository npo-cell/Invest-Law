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

## Suite : correction du classeur (19/10/2026)
- **Demande** : « corrige tout ce qu'il faut pour avoir un document des plus véridiques possibles ».
- **Méthode** (`docs/correction-2026-10-19/`, `CONSIGNE.md`) : 417 fonds repris (374 fiches du site à écarts / autre part / KID seul / factsheet dépassée, 43 fiches préparées dont la factsheet a été remplacée). Pour chacun : dernière factsheet et dernier KID de la part exacte (fundinfo, 740 PDF rangés dans `INVESTLAW/`, plus quelques-uns trouvés chez les gestionnaires), fiche refaite selon `CONSIGNE-fiches.md`, contrôle `verif_fiche.py`. 8 lots parallèles.
- **État à l'arrêt** : fiches refaites dans `docs/correction-2026-10-19/fiches/` (lots 1, 3, 6, 7 terminés ; 2, 4, 5, 8 interrompus). Liste des fonds restants : `docs/correction-2026-10-19/reste-a-faire.txt` (17 fonds). 400 fiches écrites ; 47 ont encore un écart au contrôle `verif_fiche.py` : la plupart sont expliqués en remarque (noms en majuscules, indice « Aucun »), mais celles des lots interrompus sont à revérifier à la reprise.
- Générateur du classeur déjà adapté (`docs/gamme-complete-2026-10-16/construire.py` : les fiches de `correction-2026-10-19/fiches` sont prioritaires, origine « Corrigée le 19/10 »).
- **Reste à faire pour reprendre** : 1) terminer les fonds de `reste-a-faire.txt` (même consigne, entrées dans `lots/lot-K-entree.json`) ; 2) remplir la catégorie (fichier OneLife Fund Classification sur le Drive, même ISIN ou autre part du même fonds ; catégorie du site gardée avec remarque sinon) ; 3) `construire.py` puis réimport dans le Google Sheet (IMPORTDATA, voir note du 16/10) et contrôle cellule par cellule ; 4) relancer `authentifier.py` / `consolider.py` et republier l'artefact (même lien).
- Décisions à valider : CPR Hydrogen A2 (seule factsheet de la part datée de 2024, non retenue, fiche sur le KID) ; M&G Sustainable Macro Flexible Credit P (factsheet de la part W dont le tableau donne la ligne de la part P) ; fiches vides faute de document de la part (Leleux parts P et PA, Conviction Patrimoine B).
- Ni le Google Sheet ni invest-law.eu n'ont encore été modifiés par cette correction.

### Reprise et fin de la correction (19/10/2026, 13h30)
- 17 fonds restants faits (5 BL / BlackRock, 11 JPM, TC New Horizon), 20 fiches des lots interrompus relues et corrigées si besoin ; indice BL harmonisé (« Aucun », KID « sans utiliser une valeur de référence ») ; 3 politiques nettoyées (MainFirst Germany et Top European Ideas, PTAM Defensiv : tableaux et mentions copiés par erreur).
- Catégories (`docs/correction-2026-10-19/categories.py`, fichier OneLife non versionné) : 279 même ISIN, 33 autre part du même fonds, 70 catégorie du site gardée avec remarque, 35 vides.
- **Google Sheet mis à jour** (même lien) : 417 fiches refaites (origine « Corrigée le 19/10 »), Allocations 20 217 lignes, Documents 2 478 PDF ; import IMPORTDATA du commit dbb0ea7 ; contrôle cellule par cellule : 0 écart (37 libellés de maturité remis en texte). Lisez-moi daté du 19/10.
- **Authentification refaite** : passage automatique (format de date « 04-janv.-1999 » ajouté), relecture des 160 cases et 16 blocs d'allocations non retrouvés (`relecture2/`, 3 lots + compléments). **Résultat : 10 294 cases conformes, 0 qui contredit son document, 0 absente ; 719 blocs d'allocations conformes** ; 110 catégories reprises du site (hors fichier One Life) ; 1 479 synthèses (type, classification). 7 fonds ont une factsheet plus récente en anglais seulement (règle « français d'abord ») ou une factsheet d'une autre part.
- Fichiers : `resultat-apres-correction.json`, `passage-automatique-apres-correction.json`. Artefact republié au même lien : https://claude.ai/artifact/7GsXisc2YK4wPHHni72WLx
- **invest-law.eu non modifié** : les corrections des 374 fiches du site restent à reporter sur le site, avec l'accord de l'utilisatrice.
- Décisions toujours ouvertes : CPR Hydrogen A2 (factsheet de la part datée de 2024, non retenue) ; M&G Sustainable Macro Flexible Credit P (factsheet de la part W, ligne de la part P) ; Waterloo (factsheet « Internal use only », publiée par le gestionnaire) ; fiches vides faute de document de la part (Leleux P et PA, Conviction Patrimoine B).
