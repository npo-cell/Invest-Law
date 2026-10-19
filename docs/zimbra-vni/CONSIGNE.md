# Routine quotidienne : VNI Zimbra → invest-law.eu

Décidée le 19/10/2026 : du lundi au vendredi vers 17h (Bruxelles), une session cloud lit la boîte Zimbra « data » et importe les nouvelles VNI sur invest-law.eu.

## Règles (choix de l'équipe)
- **Import automatique des VNI seulement**, et seulement pour les fiches qui existent déjà. On ne crée jamais de fiche ; les parts sans fiche sont ignorées.
- **Les VNI suspectes sont signalées, pas importées** : date future, mails contradictoires, variation de plus de 10 % par rapport à la VNI précédente. Une VNI déjà présente sur le site n'est jamais modifiée : si elle diffère du mail, elle est seulement signalée.
- Les autres mails (factsheets, nouvelles, mails inconnus) sont seulement signalés dans le compte rendu.
- **Compte rendu** : notification et email en fin de passage (import fait, anomalie ou échec). Le passage ajoute aussi une ligne dans `docs/sessions/AAAA-MM-JJ-vni-zimbra.md`, puis commit et fusion selon `AGENTS.md`.

## Étapes
1. `pip install -q xlrd`.
2. Connexion à invest-law : `python3 tools/investlaw_upload.py login`. Lire le **dernier** code dans Gmail (`from:info@invest-law.eu newer_than:15m`, **avec la corbeille incluse**, car le fil peut être à la corbeille), puis `verify <code>` et mettre le fil à la corbeille. En cas de 401, recommencer une fois : une connexion depuis un autre poste invalide la session.
3. Simulation : `cd tools && python3 zimbra_vni_sync.py --days 10`. Lire `a_importer` et `ecartees`.
4. Import : `python3 zimbra_vni_sync.py --days 10 --apply`. L'outil relit le site après l'import : `ecarts_relecture` doit être vide.
5. Signaler les mails reçus depuis la veille qui ne sont ni CACEIS ni DNCA : `python3 tools/zimbra_mail.py list 30 --query "after:MM/JJ/AAAA"`.
6. Compte rendu : nombre de VNI importées par fiche, VNI écartées avec la raison, autres mails, erreurs.

## Sources connues
- **CACEIS (OLIS)**, `Olis@caceis.com` : Excel « Fund Prices Providers » pour les fonds Leleux Invest, avec un décalage de quelques jours sur la date de VNI.
- **DNCA**, `opcvm@dncafinance.fr` et `opcvm@dncafinance.lu` : CSV `cotation_mailing_dnca_*.csv` avec toute la gamme.
- Pour une nouvelle source (autre format), le compte rendu la signale, puis on étend `tools/zimbra_vni_sync.py` après accord.
