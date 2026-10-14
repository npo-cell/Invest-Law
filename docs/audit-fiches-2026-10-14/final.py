import json,re,collections,datetime
F={str(z['FundId']):z for z in json.load(open('funds.json'))}
A=json.load(open('audit_docs.json'))
# mois lu dans le contenu du PDF quand le nom du rapport sur le site est faux (vérifié à la main le 14/10/2026)
OVR={236:'2026-07',44:'2026-07',79:'2026-07',122:'2026-07',5:'2026-07',94:'2026-07',495:'2026-09',338:'2026-09',339:'2026-09',341:'2026-09',342:'2026-09'}
for d in A['docs']:
  if d['id'] in OVR and d['type']=='Factsheet' and d['mois']=='2026-08': d['mois_site']=d['mois']; d['mois']=OVR[d['id']]
# benchmark « n/a » (id 51) = champ vide ; 17 fiches dont la factsheet dit qu'il n'y a pas d'indice
NA_SANS={25,9,37,224,228,229,202,197,203,198,201,196,205,106,200,204,15}
p='/home/user/Invest-Law/docs/2026-10-12-audit-fiches-investlaw.html'; s=open(p).read()
m=re.search(r'const D = (\{.*?\});\n',s,flags=re.S); D=json.loads(m.group(1))
# --- champs
def vide(v): return v is None or str(v).strip() in ('','0','0.00','E','-')
CH=[('Devise','Currency'),('Encours','TotalAssets'),('Frais de gestion','Fees'),('TER','TER'),('Gérant','fund_manager'),('Date de création','CreationDate'),('Benchmark','BenchmarkId')]
# --- documents par doc
idx=collections.defaultdict(list)
for d in A['docs']: idx[d['id']].append(d)
def statut_doc(d,k):
  if d['type']!='Factsheet': return None
  if d['isin_ok'] or d['id']==448: return 'ok'
  t=open(f"txt/{d['id']}_{k}.txt").read().upper()
  isins={x for x in re.findall(r'\b[A-Z]{2}[0-9A-Z]{9}[0-9]\b',re.sub(r'[  ]','',t)) if re.match(r'(LU|FR|IE|BE|DE|SE|LI|MT|GB|CH|NL|AT)\d',x)}
  return 'autre part' if isins else 'ISIN non mentionné'
docrows=[]
for i,L in idx.items():
  for k,d in enumerate(L): d['statut']=statut_doc(d,k); docrows.append(d)
LANGN={'FR':'français','EN':'anglais','SV':'suédois','NL':'néerlandais','IT':'italien','DE':'allemand','ES':'espagnol'}
for f in D['funds']:
  i=str(f['id']); z=F[i]
  f['maison']=z.get('MaisonName') or None
  f['manque']=[n for n,k in CH if vide(z.get(k)) or (k=='BenchmarkId' and str(z.get(k))=='51')]; f['st']={c:v for c,v in f.get('st',{}).items() if c in f['manque']}
  if str(z.get('BenchmarkId'))=='51': f['st']['Benchmark']='Sans objet' if f['id'] in NA_SANS else 'À demander'
  for c in f['manque']: f['st'].setdefault(c,'À demander')
  L=[d for d in idx.get(f['id'],[]) if d['type']=='Factsheet']
  last=max(L,key=lambda d:d['mois'] or '') if L else None
  f['fs']=last['mois'] if last else None
  pb=[]
  if not L: pb.append('Aucune factsheet' + (' (seulement un rapport annuel ou semestriel)' if idx.get(f['id']) and any(d['type'].startswith('Rapport') for d in idx[f['id']]) else ''))
  else:
    if last['mois']<'2026-08': pb.append('Ancienne ('+last['mois']+')')
    if last['statut']=='autre part': pb.append("Factsheet d'une autre part")
    if last['statut']=='ISIN non mentionné': pb.append('ISIN non mentionné')
    if last['langue'] not in ('FR','EN') and f['id']!=448: pb.append('En '+LANGN.get(last['langue'],last['langue']))
  dup=[m for m,c in collections.Counter(d['mois'] for d in L).items() if c>1]
  if dup: pb.append('Deux rapports pour '+', '.join(dup))
  if any(d.get('mois_site') for d in L): pb.append('Factsheet enregistrée sous le mauvais mois')
  if any(d['statut']=='autre part' and d is not last for d in L): pb.append("Ancien rapport d'une autre part")
  f['doc']=pb
  f['lang']=('FR' if f['id']==448 else last['langue']) if last else None
  f['pol']='FR' if (z.get('InvestmentPolicy') or '').strip() else ('EN' if (z.get('InvestmentPolicyEN') or '').strip() else '')
n=lambda a,b:sum(1 for z in D['funds'] if a<=len(z['manque'])<=b)
D.update(maj=datetime.datetime.now(datetime.UTC).strftime('%d/%m/%Y à %Hh%M UTC'),complete=n(0,0),presque=n(1,2),incomplete=n(3,4),vides=n(5,99))
D['champs']=[[k,v] for k,v in collections.Counter(c for z in D['funds'] for c in z['manque']).most_common()]
cnt=collections.Counter(c for z in D['funds'] for c in z['st'].values())
D['statuts']={k:cnt[k] for k in ['Remplissable','À vérifier','À demander','Sans objet']}
mais=collections.defaultdict(lambda:[set(),0])
for z in D['funds']:
  for c,v in z['st'].items():
    if v=='À demander': mais[z['maison'] or '(maison non renseignée)'][0].add(z['id']); mais[z['maison'] or '(maison non renseignée)'][1]+=1
D['maisons']=sorted([[k,len(v[0]),v[1]] for k,v in mais.items()],key=lambda q:(-q[2],q[0].lower()))
FS=D['funds']; C=collections.Counter
D['docs']={'total':len(docrows),'factsheets':sum(1 for d in docrows if d['type']=='Factsheet'),'dic':sum(1 for d in docrows if d['type']=='DIC'),
 'rapports':sum(1 for d in docrows if d['type'].startswith('Rapport')),
 'sept':sum(1 for f in FS if f['fs']=='2026-09' or f['fs']=='2026-10'),'aout':sum(1 for f in FS if f['fs']=='2026-08'),
 'anciennes':sum(1 for f in FS if f['fs'] and f['fs']<'2026-08'),'aucune':sum(1 for f in FS if not f['fs']),
 'fr':sum(1 for f in FS if f['lang']=='FR'),'en':sum(1 for f in FS if f['lang']=='EN'),'autre_langue':sum(1 for f in FS if f['lang'] and f['lang'] not in('FR','EN')),
 'conformes':sum(1 for f in FS if f['fs'] and not f['doc']),'a_corriger':sum(1 for f in FS if f['doc']),
 'pol_fr':sum(1 for f in FS if f['pol']=='FR'),'pol_en':sum(1 for f in FS if f['pol']=='EN'),'pol_vide':sum(1 for f in FS if not f['pol']),
 'isin_ok_docs':sum(1 for d in docrows if d['statut']=='ok'),'autre_part_docs':sum(1 for d in docrows if d['statut']=='autre part'),'sans_isin_docs':sum(1 for d in docrows if d['statut']=='ISIN non mentionné')}
D['pbdocs']=C(p.split(' (')[0] if not p.startswith('Aucune') else p for f in FS for p in f['doc']).most_common()
json.dump(D,open('D.json','w'),ensure_ascii=False); json.dump(docrows,open('docrows.json','w'),ensure_ascii=False)
print({k:v for k,v in D.items() if k not in('funds','maisons')})
