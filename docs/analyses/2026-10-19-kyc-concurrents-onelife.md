# Méthodes KYC des concurrents de OneLife

Date : 19/10/2026. Sources : sites publics, notices de confidentialité, formulaires, décisions des régulateurs, presse. Aucun accès aux portails courtiers.

Notation : **[F]** fait lu sur la source citée · **[S]** fait relevé en presse ou dans un résumé, source primaire non lue · **[I]** inférence.

Constat général : aucun des sept concurrents ne publie de politique LBC/FT détaillée, de politique d'acceptation client ni de questionnaire Wolfsberg. L'analyse repose donc sur des indices : outils, formulaires, notices de confidentialité et sanctions.

## 1. Synthèse

| Assureur | Canal | Identification à l'entrée | Outil numérique | Origine des fonds | Sanction LBC connue |
|---|---|---|---|---|---|
| **OneLife** (réf.) | Conseillers / partenaires, 9 marchés | Par le partenaire, pièces chargées en ligne | youroffice + outil « Connaissance client », criblage KYCTech [S] | Non publié | Aucune trouvée |
| **Wealins** (Foyer, LU) | Partenaires, gestionnaires d'actifs, courtiers | Non publié | e-Wealins ; e-signature eIDAS Namirial (OTP SMS) | Non publié | Aucune trouvée |
| **Utmost** (LU, IE, IOM, GG) | Conseillers, banques privées | **Le conseiller vérifie et certifie** (formulaire IOM) | Connect ; e-signature eIDAS | Formulaire SoF systématique ; questionnaire SoW si risque élevé/PEP | **CAA 2024 : 1,682 M€** (Lombard) ; **GFSC 2026 : 1,96 M£** |
| **Vitis Life** (Monceau, LU) | 100 % distributeurs (banques privées, gérants) | Non publié | MY VITISLIFE, Web API, outil VIPP | Non publié | Aucune trouvée |
| **Athora Belgium** | 100 % courtiers indépendants | Par le courtier | Athora.Site, signature itsme/eID (rachats), intégration Brio | Non publié | Aucune trouvée |
| **NN Belgium** | Courtiers + bancassurance ING | Par courtier / ING [I] | Broker portal NN | Non publié | Aucune trouvée |
| **Vivium** (P&V) | 100 % courtiers | Par le courtier | MyVivium (itsme/eID, gestion seulement) | **Formulaire PEP 8.871N avec preuve objective** | Aucune trouvée |
| **Allianz Benelux** | Surtout courtiers | Non publié | Non publié | Non publié | Aucune trouvée (BE) |

« Aucune trouvée » : recherche web et avis CAA 2022-2026 ; les listes de sanctions BNB et FSMA n'ont pas pu être ouvertes (erreur 404). À confirmer manuellement.

## 2. Fiches par concurrent

### Wealins (groupe Foyer, Luxembourg)
- Canal : partenaires de référence, courtiers, gestionnaires d'actifs [F] https://www.wealins.com/ ; données partagées avec le réseau Foyer et les courtiers [F] https://www.wealins.com/privacy-information/
- Plateforme e-Wealins pour partenaires et clients, connexion commune Foyer [F] https://www.e-wealins.com/
- Signature électronique avancée eIDAS par **Namirial** : identification par mobile + OTP, lien par e-mail, piste d'audit, scellement, IP enregistrée [F] https://www.wealins.com/esignature/
- e-Wealins aide à recueillir les préférences de durabilité (IDD) [F] https://paperjam.lu/article/innovation-regulation-go-hand-
- Pièces exigées, criblage PEP/sanctions, recours aux tiers, revue périodique : rien de publié.

### Utmost (ex-Lombard International au Luxembourg)
- Canal : conseillers et banques privées [S] https://www.privatebankerinternational.com/news/lombard-international-assurance-enhances-online-servicing-platform/
- Portail Connect (connect.utmostgroup.lu), guides de souscription digitale Belgique/France [S] ; e-signature eIDAS, fournisseur non nommé [F] https://www.utmostgroup.com/electronic-signature-notice
- Formulaire « KYC – Source of Funding and Verification of Identity » (IOM/PanEurope, 05/2025) : ID et justificatif de domicile **certifiés**, déclaration PEP (famille, proches), compte bancaire d'origine des fonds ; **le conseiller vérifie l'identité et signe des déclarations** [F] https://www.utmostwealthdocs.com/mb/CLYrhM
- Questionnaire « Source of Wealth » réservé aux clients à risque élevé, PEP ou EDD : approche par les risques [F] https://www.utmostwealthdocs.com/mb/Bvf9Kl
- Notice de confidentialité Luxembourg : collecte en registres publics, bases de données spécialisées, presse et internet (criblage [I]) ; prestataires LBC/KYC au Royaume-Uni et aux États-Unis ; décision partiellement automatisée [F] https://www.utmostwealthdocs.com/mb/DbkCPU
- **CAA, 10/01/2024, 1 682 000 € contre Lombard International Assurance** [F] https://www.caa.lu/uploads/documents/files/Sanction_administrative_20240320.pdf. Manquements :
  - pas d'évaluation globale des risques, notation client inadéquate ;
  - définitions erronées (bénéficiaire effectif, PEP) ;
  - **intermédiaires non contrôlés au titre de l'art. 3-3** ;
  - origine des fonds, conformité fiscale et bénéficiaire effectif sans pièces probantes ;
  - vigilance renforcée insuffisante sur le risque fiscal ; surveillance défaillante ; déclarations à la CRF tardives.
- **GFSC Guernesey, 12/03/2026, 1,96 M£ contre Utmost Worldwide** : dépendance à des courtiers non régulés, revue annuelle de moins de 3,5 % des ~22 500 clients à risque élevé, falsification de dossiers par un intermédiaire non remédiée ; amendes personnelles CEO et MLRO adjoint [S] https://guernseypress.com/news/2026/03/13/utmost-fined-almost-pound2m-for-decade-long-regulatory-failings

### Vitis Life (groupe Monceau, Luxembourg + succursale belge)
- Pas de canal direct : banques privées et gestionnaires de fortune [F] https://www.vitislife.com/partenaires/
- Portail MY VITISLIFE : souscription en ligne, suivi des demandes, ajout de « documents manquants », Web API, logiciel dédié au contrat belge VIPP [F] https://www.vitislife.com/my-vitislife/
- Notice de confidentialité : carte d'identité, passeport, titre de séjour, nationalité, données fiscales, données « fraude et blanchiment » ; destinataires LBC au sein du groupe Monceau [F] https://www.vitislife.com/disclaimer/ (la notice renvoie vers des liens groupama.fr et macif.fr et n'indique pas de DPO : anomalie).
- [I] Identification déléguée au distributeur (art. 3-3 loi du 12/11/2004), non confirmé.

### Athora Belgium
- Exclusivement courtiers indépendants ; le courtier met à jour les données client [F] https://www.athora.com/be/nl/bibliotheek/faq
- Extranet Athora.Site : profil de risque, devis, souscription, rachats, pré-remplissage ; « 100% elektronische processen » ; **signature itsme ou eID** (rachats) ; consultation des contrats via MyBroker dans **Brio** [F] https://www.athora.com/be/nl/broker-zone
- Paiement : copie recto/verso de la carte d'identité du bénéficiaire et attestation bancaire « pour réduire le risque de fraude » [F] FAQ ci-dessus.
- Préférences de durabilité recueillies par le courtier (catégories A/B/C, % minimum), « periodieke geschiktheidsbeoordeling » [F] https://marketing.be.athora.site/documents_online/public/Pdf/Common/SFDR/ATH_718_NOTE_SFDR_NL.pdf
- [I] Reprise des portefeuilles NN (2025) et Aviva (2026) : remédiation KYC probable des contrats transférés.

### NN Insurance Belgium
- Courtiers (https://www.nn.be/nl/brokers) et bancassurance ING Belgium jusqu'en 2034 [F]
- Notice de confidentialité : numéro de registre national (obligation légale), données reçues du client ou du conseiller, **sources publiques consultées contre terrorisme et blanchiment**, transmission FATCA/CRS et au Point de contact central (PCC) de la BNB, refus possible du contrat [F] https://www.nn.be/nl/de-volledige-privacyverklaring
- Groupe : programme « Financial Economic Crime » avec criblage central et outil KYC sous Salesforce [S, source faible, lien désormais en 404].

### Vivium (groupe P&V)
- Exclusivement courtiers [F] https://my.pv.be/documents/d/guest/vv-privacy-nl
- MyVivium : connexion itsme/eID, consultation des contrats vie ; outil de gestion, pas d'identification à l'entrée [F] https://inform.vivium.be/documents/d/vivium-info/vivium_fiche-cuzo_nl-pdf
- **Formulaire PEP 8.871N (01/2021)** : preneur, représentant, UBO, bénéficiaire ; mandats des 12 derniers mois, famille et proches associés ; **origine des fonds « avec preuve objective »** (extrait de compte, paiement d'assurance groupe, acte notarié, succession) [F] https://vivium.be/politiek-prominent-persoon. C'est le document KYC le plus concret trouvé chez les concurrents belges.
- Criblage embargos et gel des avoirs ; déclaration au PCC de la BNB, conservation 10 ans [F] notice ci-dessus.

### Allianz Benelux
- Surtout courtiers ; distribution « volledig digitaal » envisagée [F] https://allianz.be/content/dam/onemarketing/benelu/allianz-be/nl/documenten/over-allianz/assur-mifid-identiteitsfiche.pdf
- Notice de confidentialité : registre UBO, FATCA/CRS, BNB, FSMA, fichier fraude RSR de Datassur, conservation selon la loi LBC [F] https://allianz.be/content/dam/onemarketing/benelu/allianz-be/other/privacystatement_nl.pdf
- Aucune section KYC détaillée trouvée.

### Commun aux assureurs belges
- Adéquation IDD via la fiche sectorielle Assuralia (connaissances, situation financière, risque, durabilité) depuis le 02/08/2022 [F] https://febelfin.be/nl/publicaties/2022/mifid-idd-waarom-worden-mijn-duurzaamsheidsvoorkeuren-gevraagd

## 3. Référence OneLife
- Portail youroffice : souscription et opérations en ligne, signature électronique simplifiée ; outil **« Connaissance client »** qui signale les dossiers à mettre à jour (données, pièces d'identité) et permet de les compléter en ligne [F] https://www.onelife.com/en/management-tools
- yourassets : signature digitale client avec le conseiller [F] https://www.onelife.com/en/digital-management-your-policy
- Souscription 100 % digitale avec l'outil du groupe APICIL [S] https://paperjam.lu/article/digital-et-reglementation-duo-
- Criblage automatisé via **KYCTech** (« One click, One KYC report ») [S] https://paperjam.lu/article/brand-voice-regtech-insurtech-onelife-a-partage-son-retour-dexperience
- Équipe « Client Review » dédiée à l'analyse LBC [S]

## 4. Lecture pour OneLife [I]
1. **Le modèle dominant est le recours à l'intermédiaire.** Tous les concurrents font collecter les données et souvent vérifier l'identité par le courtier ou la banque. C'est précisément ce que le CAA a sanctionné chez Lombard (intermédiaires non contrôlés, art. 3-3). Le contrôle documenté des apporteurs (due diligence, tests de qualité des dossiers, droit d'audit) est le premier point d'exposition du marché luxembourgeois.
2. **OneLife paraît en avance sur la revue périodique outillée** (outil « Connaissance client » côté partenaire). Aucun concurrent ne décrit publiquement un équivalent. L'affaire Utmost Guernesey (moins de 3,5 % des clients à risque élevé revus) montre l'enjeu.
3. **Origine des fonds et du patrimoine** : Utmost (SoF systématique, SoW si risque élevé) et Vivium (preuves objectives pièce par pièce) sont les plus formalisés. Le CAA reproche l'absence de pièces probantes : point à vérifier dans les formulaires OneLife.
4. **Signature et identité numériques** : Wealins (Namirial, eIDAS) et Athora (itsme/eID) sont les plus avancés publiquement. Personne ne publie d'identification vidéo ni de vérification d'identité automatisée (Onfido, IDnow, etc.) : différenciation possible pour OneLife, surtout sur le marché belge où itsme est la norme.
5. **Transparence** : aucun concurrent ne publie de déclaration LBC ou de questionnaire Wolfsberg. Publier un résumé de politique KYC serait un signal différenciant vis-à-vis des banques privées partenaires.

## 5. Limites
- Portails courtiers non consultés ; procédures internes non publiques.
- Listes de sanctions BNB et FSMA non ouvertes (404) ; absence de sanction non confirmée de façon exhaustive.
- Faits [S] à vérifier sur la source primaire avant diffusion externe.
