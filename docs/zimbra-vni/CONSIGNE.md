# Routine quotidienne : VNI Zimbra → invest-law.eu

État des lieux des VNI du site (fonds sans VNI, VNI fausses, dates décalées, fonds plus mis à jour) : `docs/controle-vni/README.md`.

Décidée le 19/10/2026 : du lundi au vendredi vers 17h (Bruxelles), une session cloud lit la boîte Zimbra « data » et importe les nouvelles VNI sur invest-law.eu.

## Règles (choix de l'équipe)
- **Import automatique des VNI seulement**, et seulement pour les fiches qui existent déjà. On ne crée jamais de fiche ; les parts sans fiche sont ignorées.
- **Les VNI suspectes sont signalées, pas importées** : date future, mails contradictoires, variation de plus de 10 % par rapport à la VNI précédente. Une VNI déjà présente sur le site n'est jamais modifiée : si elle diffère du mail, elle est seulement signalée.
- Les autres mails (factsheets, nouvelles, mails inconnus) sont seulement signalés dans le compte rendu.
- **Compte rendu** : notification et email en fin de passage (import fait, anomalie ou échec). Le passage ajoute aussi une ligne dans `docs/sessions/AAAA-MM-JJ-vni-zimbra.md`, puis commit et fusion selon `AGENTS.md`.

## Mémoire de la routine (track record)
Les sessions cloud repartent de zéro : la mémoire est dans le dépôt, à committer à chaque passage.
- `docs/zimbra-vni/journal.csv` : chaque VNI importée (`importee`), écartée (`ecartee` + raison) ou en échec de relecture (`erreur`), avec l'horodatage.
- `docs/zimbra-vni/mails.csv` : chaque mail Zimbra déjà vu (`VNI` ou `à traiter à la main`). Un mail n'est signalé qu'une fois.
- Double sécurité contre les doublons : l'outil compare aussi avec les VNI déjà présentes sur le site et ne réimporte jamais une date existante.
- Une VNI écartée déjà au journal est marquée « déjà signalée » : ne la rappeler que dans une ligne de synthèse.

## Étapes
1. `pip install -q xlrd`.
2. Connexion à invest-law : `python3 tools/investlaw_upload.py login`. Lire le **dernier** code dans Gmail (`from:info@invest-law.eu newer_than:15m`, **avec la corbeille incluse**, car le fil peut être à la corbeille), puis `verify <code>` et mettre le fil à la corbeille. En cas de 401, recommencer une fois : une connexion depuis un autre poste invalide la session.
3. Simulation : `cd tools && python3 zimbra_vni_sync.py --days 10`. Lire `a_importer` et `ecartees`.
4. Import : `python3 zimbra_vni_sync.py --days 10 --apply`. L'outil relit le site après l'import : `ecarts_relecture` doit être vide.
5. Signaler les nouveaux mails à traiter à la main : liste `mails_a_traiter` de la sortie.
6. Committer `docs/zimbra-vni/journal.csv` et `mails.csv` avec la note de session (étape obligatoire : c'est la mémoire).
7. Compte rendu : nombre de VNI importées par fiche, VNI écartées avec la raison, autres mails, erreurs.

## Sources connues
- **CACEIS (OLIS)**, `Olis@caceis.com` : Excel « Fund Prices Providers » pour les fonds Leleux Invest, avec un décalage de quelques jours sur la date de VNI.
- **DNCA**, `opcvm@dncafinance.fr` et `opcvm@dncafinance.lu` : CSV `cotation_mailing_dnca_*.csv` avec toute la gamme.
- Pour une nouvelle source (autre format), le compte rendu la signale, puis on étend `tools/zimbra_vni_sync.py` après accord.
