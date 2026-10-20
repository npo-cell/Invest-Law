# 2026-10-20 — Contrôle des VNI (fonds avec / sans VNI, cohérence avec la date de création)

- **Objectif** : lister les fonds avec et sans VNI sur invest-law.eu et comparer la date de création de chaque fiche à sa première VNI. Tolérance : 7 jours avant, 3 mois après.
- **Résultat** (488 fiches) : 121 OK, 2 aux VNI fausses (DNCA Alpha Bonds, Echiquier Agressor), 31 avec des VNI avant la création, 17 au début d'historique manquant, 3 sans date de création, 314 sans aucune VNI (dont 17 actifs).
- **Autres anomalies** : 122 fonds avec des VNI datées un week-end (décalage probable d'un jour à l'import), 61 fonds plus mis à jour depuis plus de 45 jours (surtout depuis le 7–8/06/2026), 7 historiques en francs avant l'euro.
- **Rien n'a été modifié sur le site** (lecture seule).
- **Tableau de bord** (artéfact privé, à partager depuis la page) : https://claude.ai/artifact/E3kwtSBzrF4KKKR5XSu8R6
- **Fichiers** : `docs/2026-10-20-controle-vni.md` (rapport), `docs/controle-vni/controle-vni-2026-10-20.json` (données), `tools/controle_vni.py` (script).
- **Connexion** : les identifiants de l'environnement de cette session étaient périmés (401). Le nouveau mot de passe a été fourni dans le chat et passé à la commande, sans être écrit dans le dépôt. Code de connexion mis à la corbeille.
- **Pour reprendre (ex. Noa)** : tout est résumé dans `docs/controle-vni/README.md` (règles, bilan, anomalies, pistes, mise à jour du tableau de bord), lien ajouté dans le skill invest-law et dans `docs/zimbra-vni/CONSIGNE.md`. `tools/controle_vni.py` lit désormais le site lui-même : vérifié, il redonne exactement le JSON du 20/10.
