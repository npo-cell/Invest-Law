# 2026-10-14 — Audit de la page d'audit des fiches (« aucune erreur »)

- **Demande** : refaire l'audit de l'artefact des fiches, très précisément.
- **Méthode** : tout recalculé sur le site le 14/10/2026 à 09h35 UTC (488 fiches, 739 documents téléchargés et relus), puis contrôles indépendants : chaque texte de la page relu contre les données, valeurs bouche-trou, mois de chaque factsheet lu dans le PDF, cohérence devise / dates / frais.
- **Erreurs trouvées et corrigées sur la page** :
  - 19 fiches avaient l'indice « n/a » (benchmark 51) et comptaient comme complètes → comptées comme champ vide (17 « sans objet » : la factsheet dit qu'il n'y a pas d'indice ; 2 « à demander » : 35 Ofi Precious Metals, 265 HMG Rendement). Fiches complètes : 228 → 209.
  - 11 factsheets enregistrées sous le mauvais mois : 495, 338, 339, 341, 342 (Mandarine) sont des factsheets de septembre nommées « Août 2026 » ; 236 (BGF Sustainable Energy), 44 (DNCA Alpha Bonds), 79 et 122 (M&G) sont de juillet mais nommées « Août 2026 » ; 5 et 94 (DNCA) ont un rapport « Août 2026 » qui est celui de juillet. Fiches à corriger : 48 → 59.
  - « 66 maisons » comptait la ligne « maison non renseignée » ; 12 fiches n'ont pas de maison sur le site (65, 46, 60, 47, 52, 67, 6, 45, 53, 35, 34, 18).
  - « 413 fiches conformes : 300 en français, 131 en anglais » additionnait mal (300 + 131 = toutes les factsheets) → reformulé.
  - « factsheet récente : août ou septembre » incluait octobre → « août 2026 ou plus récente ».
- **À vérifier (non modifié sur le site)** : indice S&P 500 sur 18 (Smart Value Investors Patrimoine Flexible), 34 (Ofi Strategic Metals, factsheet sans indice) et 65 (Alken Small Cap Europe). Le S&P 500 de 231 et 348 est correct.
- **Contrôlé sans erreur** : ISIN des factsheets, langues, doublons, devises, dates de création, TER de 139 (5,54 %, conforme à la factsheet).
- **Fichiers** : page `docs/2026-10-12-audit-fiches-investlaw.html` (https://claude.ai/artifact/GfTSsC7oUyEeoruciDXX3J), `docs/2026-10-13-audit-documents.xlsx` et `docs/2026-10-13-champs-vides-a-demander.xlsx` régénérés, scripts dans `docs/audit-fiches-2026-10-14/`, règle ajoutée au guide.
- Rien n'a été modifié sur invest-law.eu.

## Suite : renommage des 11 factsheets (14/10/2026 ~09h40 UTC, accord de l'utilisatrice)
- **Modification du site invest-law.eu** : 11 rapports redéposés sous le bon mois puis l'ancien supprimé (`tools/investlaw.py rename-report`, commandes dans `docs/audit-fiches-2026-10-14/renommage-2026-10-14.sh`) :
  - « Rapport de gestion Juillet 2026 » (31/07/2026) : 236, 44, 79, 122, 5, 94 ;
  - « Rapport de gestion Septembre 2026 » (30/09/2026) : 495, 338, 339, 341, 342.
- Contrôle : nombre de rapports inchangé sur chaque fiche ; les 19 PDF de ces fiches retéléchargés sont identiques (md5) à ceux d'avant.
- Page d'audit recalculée (09h41 UTC) : factsheet de septembre 186, août 239, plus ancienne 12 (dont les 4 de juillet), fiches à corriger 52, conformes 409.

## Suite : maisons de gestion et benchmark 34 (14/10/2026 ~09h50 UTC, demande de l'utilisatrice)
- **Modification du site invest-law.eu** : maison de gestion renseignée sur 11 fiches d'après le Google Sheet « GAMME ONE LIFE CAMELEA » (onglet FundsRange2026-09-22, colonne Fund company, rapprochement par ISIN), rattachée à la maison déjà présente sur le site : 46 → Aphilion (53) ; 60, 47 → COMGEST ASSET MANAGEMENT (108) ; 52 → Guardcap (24) ; 67 → Janus Henderson Investors (39) ; 6 → La Française (45) ; 45 → LBP AM (89, celle déjà utilisée par Tocqueville ; une autre « LBP AM » id 44 existe en double) ; 53 → Morgan Stanley (59) ; 35, 34 → Ofi Asset Management (61) ; 18 → Conventum (75). Relu après enregistrement : aucun écart.
- Fiche 34 Ofi Strategic Metals : indice S&P 500 retiré (champ vide), la factsheet n'affiche aucun indice.
- Non fait : fiche 65 Alken Small Cap Europe, absente du sheet (le seul fonds Alken du sheet, LU0572586591, est géré par AFFM S.A.) → à confirmer par l'utilisatrice.
- Page d'audit recalculée (09h51 UTC) : 208 complètes, 220 presque ; 422 champs vides (310 à demander, 63 à vérifier, 49 sans objet) ; 68 maisons à contacter. Excel liés mis à jour.
