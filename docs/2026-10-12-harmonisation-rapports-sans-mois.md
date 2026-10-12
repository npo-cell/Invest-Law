# 2026-10-12 — Harmonisation des rapports sans mois (invest-law.eu)

Rapports intitulés « Rapport de gestion » (ou équivalent) sans mois. Le mois a été lu dans le PDF. Comme le site ne permet pas de renommer, chaque rapport est redéposé sous le nouveau nom et le nouveau fichier, puis l'ancien est supprimé (`tools/investlaw.py rename-report`).

- 82 rapports : 78 renommés « Rapport de gestion <Mois> <Année> », datés de la factsheet ; 4 sont en fait des DIC, renommés « DIC (Document d'informations clés) ».
- Aucun conflit : aucun fonds n'a déjà un rapport du même mois.
- Fiche 129 traitée en test le 12/10/2026 (OK). Les autres attendent la validation de l'utilisateur.

| Fiche | ISIN (nouveau fichier) | Ancien nom | Ancien fichier | Nouveau nom | Date | Source de la date |
|---|---|---|---|---|---|---|
| 207 | DE000A0X7541__KID_2026-09-28.pdf | rapport de gestion | t_l_chargement.pdf | DIC (Document d'informations clés) | 2026-09-28 | KID |
| 210 | FR00140144O8__Factsheet_2026-02-05.pdf | Fiche produit | Fiche_Produit_AHD.pdf | Rapport de gestion Février 2026 | 2026-02-05 | donnees au txt « 47 Données au 05 février 2026. Le » |
| 82 | FR0013261765__Factsheet_2026-08-31.pdf | Rapport de gestion 2026 | Rapport_de_gestion_Athymis_Better_Life_P_2026-08.pdf | Rapport de gestion Août 2026 | 2026-08-31 | titre « meilleur. REPORTING MENSUEL - Août 2026 » |
| 82 | FR0013261765__Factsheet_2022-10-31.pdf | Rapport de gestion | Fiche_F00000ZHNL_52.pdf | Rapport de gestion Octobre 2022 | 2022-10-31 | image |
| 72 | FR0013358793__Factsheet_2026-08-31.pdf | Rapport de gestion 2026 | Rapport_de_gestion_Athymis_Industrie_4.0_P_2026-08.pdf | Rapport de gestion Août 2026 | 2026-08-31 | titre « industrielle. REPORTING MENSUEL - Août 2026 » |
| 220 | FR0013173374__Factsheet_2026-08-31.pdf | Rapport de gestion 2026 | Rapport_de_gestion_Athymis_Millennial_P_2026-08.pdf | Rapport de gestion Août 2026 | 2026-08-31 | titre «llénaire qui commence. REPORTING MENSUEL - Août 2026 » |
| 83 | FR0010149302__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F0GBR04F8J_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | donnees au «CUMULÉES ET ANNUALISÉES (au 29/05/2026 - Ne» |
| 84 | LU0099161993__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F0GBR04NSH_52__1_.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | donnees au «CUMULÉES ET ANNUALISÉES (au 29/05/2026 - Ne» |
| 85 | FR0010148981__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F0GBR04F8Y_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | donnees au «CUMULÉES ET ANNUALISÉES (au 29/05/2026 - Ne» |
| 86 | FR0010147603__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F0GBR05TLP_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | donnees au «CUMULÉES ET ANNUALISÉES (au 29/05/2026 - Ne» |
| 87 | FR0010135103__Factsheet_2026-04-30.pdf | Rapport de gestion | Fiche_F0GBR04F90_52.pdf | Rapport de gestion Avril 2026 | 2026-04-30 | donnees au «CUMULÉES ET ANNUALISÉES (au 30/04/2026 - Ne» |
| 165 | LU196663100__Factsheet_2026-07-31.pdf | Rapport de gestion | Monthly-Factsheet-PRO_Carmignac-Portfolio-Grandchildren-A-EUR-Acc_LU1966631001_BE_fr.pdf | Rapport de gestion Juillet 2026 | 2026-07-31 | donnees au «CUMULÉES ET ANNUALISÉES (au 31/07/2026 - Ne» |
| 88 | LU0336083497__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F000001EWI_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | donnees au «CUMULÉES ET ANNUALISÉES (au 29/05/2026 - Ne» |
| 49 | LU1966631001__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F000013PCZ_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | donnees au «CUMULÉES ET ANNUALISÉES (au 29/05/2026 - Ne» |
| 44 | LU1694789451__Factsheet_2026-04-30.pdf | Rapport de gestion | Fiche_F00000ZY7L_52.pdf | Rapport de gestion Avril 2026 | 2026-04-30 | donnees au « base 100 (du 14/12/2017 au 30/04/2026) Val» |
| 89 | LU1907594748__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F000011TTX_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | donnees au « base 100 (du 17/12/2018 au 29/05/2026) Val» |
| 91 | LU1907595398__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F000011SU3_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | donnees au « base 100 (du 17/12/2018 au 29/05/2026) Val» |
| 92 | LU0284393930__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F000002HSV_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | donnees au « base 100 (du 31/05/2016 au 29/05/2026) Val» |
| 93 | LU1515062757__Factsheet_2026-05-29.pdf | Rapport de gestion | monthly-reporting_dnca-invest-sri-europe-growth_lu1515062757_int.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | donnees au txt «ainability risk Data as of 29 May 2026 » |
| 5 | LU0284394235__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F000001AI5_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | donnees au « Données au 29/05/2026 » |
| 8 | LU0284394664__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F000001A88_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | donnees au « Données au 29/05/2026 » |
| 94 | LU0870553020__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F00000PBLM_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | donnees au « base 100 (du 31/05/2016 au 29/05/2026) Val» |
| 90 | LU2254337392__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F000016GNF_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | donnees au « base 100 (du 09/02/2021 au 29/05/2026) Le » |
| 71 | LU0284396016__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F000002IKE_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | donnees au « Données au 29/05/2026 » |
| 95 | FR0010321810__Factsheet_2026-07-31.pdf | Rapport mensuel | Rapport_Mensuel_Echiquier_Agenor_Mid_Cap_Europe_A_FR0010321810.pdf | Rapport de gestion Juillet 2026 | 2026-07-31 | donnees au « JUILLET 2026 (données au 31/07/2026) » |
| 95 | FR0010321810__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F0GBR04VT4_52__2_.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au « MAI 2026 (données au 31/05/2026) » |
| 96 | FR0010321802__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F0GBR04QCF_52__2_.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au « MAI 2026 (données au 31/05/2026) » |
| 97 | FR0012870657__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F00000WES1_52__2_.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au « MAI 2026 (données au 31/05/2026) » |
| 98 | LU1819480192__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F000010S65_52__1_.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au « MAI 2026 (données au 31/05/2026) » |
| 99 | FR0010611293__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F000002180_52__1_.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au « MAI 2026 (données au 31/05/2026) » |
| 100 | FR001400BE31__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F00001EGKL_52__3_.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au « MAI 2026 (données au 31/05/2026) » |
| 101 | FR0013277571__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F00000ZIFJ_52__1_.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au « MAI 2026 (données au 31/05/2026) » |
| 102 | FR0010321828__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F0GBR05V7K_52__2_.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au « MAI 2026 (données au 31/05/2026) » |
| 103 | FR0010863688__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F00000HHCF_52__2_.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au « MAI 2026 (données au 31/05/2026) » |
| 104 | LU2466448532__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F00001EUKX_52__2_.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au « MAI 2026 (données au 31/05/2026) » |
| 105 | FR0010547067__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F0GBR04QL5_52__2_.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au « MAI 2026 (données au 31/05/2026) » |
| 56 | FR0010859769__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F00000H6EA_52__2_.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au « MAI 2026 (données au 31/05/2026) » |
| 16 | LU1038809395__Factsheet_2026-05-31.pdf | Rapport de gestion | Factsheet_F00000T4KE_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au txt « Informations au 31 mai 2026 F» |
| 109 | LU1481583711__Factsheet_2026-05-31.pdf | Rapport de gestion | Factsheet_F00000XXY3_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | lecture manuelle |
| 110 | LU2473801830__Factsheet_2026-05-31.pdf | Rapport de gestion | Factsheet_F00001DXKW_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au txt « Informations au 31 mai 2026 F» |
| 111 | LU2673417882__Factsheet_2026-05-31.pdf | Rapport de gestion | Factsheet_F00001HH7Y_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au txt « Informations au 31 mai 2026 F» |
| 112 | FR0010697532__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F000002LI1_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | lecture manuelle |
| 113 | FR0014000W38__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F000016IXX_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | lecture manuelle |
| 114 | FR0011271550__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F00000OLXV_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | lecture manuelle |
| 115 | FR0000980427__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F0GBR068MN_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | lecture manuelle |
| 117 | BE6202762975__KID_2026-01-01.pdf | Rapport de gestion | PRIIP_KID_F00000JRDW_299__2_.pdf | DIC (Document d'informations clés) | 2026-01-01 | KID |
| 118 | BE6327306930__KID_2026-01-01.pdf | Rapport de gestion | PRIIP_KID_F0000196S0_299.pdf | DIC (Document d'informations clés) | 2026-01-01 | KID |
| 119 | BE6327307946__KID_2026-01-01.pdf | Rapport de gestion | PRIIP_KID_F0000196ST_299.pdf | DIC (Document d'informations clés) | 2026-01-01 | KID |
| 73 | LU1670618187__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F000010L96_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au txt « Reporting mensuel au 31 mai 2026 » |
| 74 | LU1582988058__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F00000ZY64_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au txt « Reporting mensuel au 31 mai 2026 » |
| 43 | LU1670631016__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F000010L7P_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au txt « Reporting mensuel au 31 mai 2026 » |
| 76 | LU1670707527__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F000010L79_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au txt « Reporting mensuel au 31 mai 2026 » |
| 77 | LU1670713335__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F000010L5V_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au txt « Reporting mensuel au 31 mai 2026 » |
| 78 | LU1670618690__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F000010L92_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au txt « Reporting mensuel au 31 mai 2026 » |
| 79 | LU1665237704__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F00000ZQ29_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au txt « Reporting mensuel au 31 mai 2026 » |
| 80 | LU1670715207__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F000010L5E_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au txt « Reporting mensuel au 31 mai 2026 » |
| 81 | LU1670628491__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F000010KYI_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au txt « Reporting mensuel au 31 mai 2026 » |
| 120 | LU1582984818__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F00000ZY5F_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au txt « Reporting mensuel au 31 mai 2026 » |
| 121 | LU1670724373__Factsheet_2026-04-30.pdf | Rapport de gestion | Fiche_F000010L39_52.pdf | Rapport de gestion Avril 2026 | 2026-04-30 | donnees au txt « Reporting mensuel au 30 avril 2026 » |
| 122 | LU1900799617__Factsheet_2026-05-31.pdf | Rapport de gestion | Fiche_F000011FHJ_52.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | donnees au txt « Reporting mensuel au 31 mai 2026 » |
| 123 | LU2415445837__Factsheet_2026-05-31.pdf | Rapport de gestion | Factsheet_F00001D3QA_52__1_.pdf | Rapport de gestion Mai 2026 | 2026-05-31 | lecture manuelle |
| 124 | LU0864714000__Factsheet_2026-02-27.pdf | Rapport de gestion | Fiche_F00000P8QG_52.pdf | Rapport de gestion Février 2026 | 2026-02-27 | lecture manuelle |
| 125 | LU0390221256__Factsheet_2026-02-27.pdf | Rapport de gestion | Fiche_F000002JCW_52.pdf | Rapport de gestion Février 2026 | 2026-02-27 | lecture manuelle |
| 31 | LU0864709349__Factsheet_2026-02-27.pdf | Rapport de gestion | Fiche_F00000P8Q8_52.pdf | Rapport de gestion Février 2026 | 2026-02-27 | lecture manuelle |
| 126 | LU1856130205__Factsheet_2026-02-27.pdf | Rapport de gestion | Fiche_F000013COP_52__1_.pdf | Rapport de gestion Février 2026 | 2026-02-27 | lecture manuelle |
| 127 | LU2381585830__Factsheet_2026-02-27.pdf | Rapport de gestion | Fiche_F00001CXFD_52.pdf | Rapport de gestion Février 2026 | 2026-02-27 | lecture manuelle |
| 128 | LU0308864023__Factsheet_2026-02-27.pdf | Rapport de gestion | Fiche_F000000NT5_52.pdf | Rapport de gestion Février 2026 | 2026-02-27 | lecture manuelle |
| 131 | LU1919842267__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F00001273T_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | ligne date « Artificial Intelligence 29 MAI 2026 CR-E» |
| 132 | FR0000989899__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F0GBR04RBR_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | ligne date «ODDO BHF Avenir 29 MAI 2026 CR-E» |
| 133 | FR0000990095__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F0GBR04ZW9_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | ligne date «ODDO BHF Avenir Euro 29 MAI 2026 CR-E» |
| 134 | FR0000974149__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F0GBR04RBZ_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | ligne date «ODDO BHF Avenir Europe 29 MAI 2026 CR-E» |
| 135 | LU1493433004__Factsheet_2026-04-30.pdf | Rapport de gestion | Fiche_F00000YCUI_52__1_.pdf | Rapport de gestion Avril 2026 | 2026-04-30 | ligne date « 30 avril 2026 ODD» |
| 129 | DE0009772988__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F0GBR04HQ2_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | ligne date « BHF Global Equity Trend 29 MAI 2026 CRw-» |
| 136 | LU1864504425__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F000011NPN_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | ligne date «DDO BHF Polaris Balanced 29 MAI 2026 CRw-» |
| 30 | LU1849528234__Factsheet_2026-04-30.pdf | Rapport de gestion | Fiche_F000013B2E_52.pdf | Rapport de gestion Avril 2026 | 2026-04-30 | ligne date «ODDO BHF Polaris Dynamic 30 AVRIL 2026 CR-E» |
| 20 | LU1874836890__Factsheet_2026-04-30.pdf | Rapport de gestion | Fiche_F000013B2C_52.pdf | Rapport de gestion Avril 2026 | 2026-04-30 | ligne date «DDO BHF Polaris Flexible 30 AVRIL 2026 CR-E» |
| 4 | DE000A2JJ1W5__Factsheet_2026-04-30.pdf | Rapport de gestion | Fiche_F000011OG4_52.pdf | Rapport de gestion Avril 2026 | 2026-04-30 | ligne date «DDO BHF Polaris Moderate 30 AVRIL 2026 CR-E» |
| 137 | FR0010109165__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F0GBR05T1R_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | ligne date «ODDO BHF ProActif Europe 29 MAI 2026 CR-E» |
| 130 | LU1833929729__Factsheet_2026-04-30.pdf | Rapport de gestion | Fiche_F000010UH2_52.pdf | Rapport de gestion Avril 2026 | 2026-04-30 | ligne date «ODDO BHF Algo Trend US 30 AVRIL 2026 CR-E» |
| 23 | DE000A1JCWX9__Factsheet_2026-05-29.pdf | Rapport de gestion | Factsheet_F00000N723_52.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | status US «M Global Allocation R Status: 05/29/2026 M» |
| 138 | LU0260464168__Factsheet_2026-06-19.pdf | Rapport de gestion | Factsheet_FOGBR05U62_52__1_.pdf | Rapport de gestion Juin 2026 | 2026-06-19 | image |
| 29 | FR0011261197__Factsheet_2026-05-29.pdf | Rapport de gestion | Fiche_F00000X34O_52__1_.pdf | Rapport de gestion Mai 2026 | 2026-05-29 | donnees au « AU 29/05/2026 » |
