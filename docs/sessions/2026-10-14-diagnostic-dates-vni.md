# 2026-10-14 — Diagnostic : dates des VNI décalées d'un jour

- **Demande** : diagnostiquer le décalage d'un jour des VNI constaté avec le fichier Funds For Good et produire un tableau à envoyer à Omar (développeur).
- **Méthode** : lecture des 622 583 VNI des 488 fiches (166 en ont) ; pour chaque fiche, répartition par jour de la semaine, part de valeurs identiques au jour précédent, dernière date de week-end. Preuve sur Funds For Good (fichier officiel) : la VNI du site au jour J = VNI officielle du jour ouvré suivant, sur 100 % des dates communes.
- **Résultat** : 122 fiches touchées (~532 000 VNI) — 76 « décalé d'un jour », 6 « en grande partie », 29 « décalé + doublons », 11 « dates de week-end » ; 44 fiches correctes. Le décalage concerne l'historique chargé jusqu'à début juin 2026 ; les VNI ajoutées depuis (y compris l'import du 14/10) sont à la bonne date.
- **Livrables** : `docs/2026-10-14-diagnostic-dates-vni.xlsx` (onglets « À lire », « Par fiche », « Preuve ») ; sauvegarde complète des VNI avant toute correction : `docs/vni-diagnostic-2026-10-14/sauvegarde_vni_2026-10-14.csv.gz`.
- Rien modifié sur le site.
