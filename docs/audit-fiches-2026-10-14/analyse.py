import json,re,unicodedata,collections
F={str(z['FundId']):z for z in json.load(open('funds.json'))}
R=json.load(open('reports.json'))
s=open('/home/user/Invest-Law/docs/2026-10-12-audit-fiches-investlaw.html').read()
D=json.loads(re.search(r'const D = (\{.*?\});\n',s,flags=re.S).group(1))
EXT={str(x['id']):x for x in D['funds']}
M={'janvier':1,'fevrier':2,'mars':3,'avril':4,'mai':5,'juin':6,'juillet':7,'aout':8,'septembre':9,'octobre':10,'novembre':11,'decembre':12}
def nrm(x): return unicodedata.normalize('NFKD',x).encode('ascii','ignore').decode().lower()
def mth(n):
  q=re.search(r'('+'|'.join(M)+r')\s+(\d{4})',nrm(n)); return f"{q.group(2)}-{M[q.group(1)]:02d}" if q else None
W={'FR':' le la les des est du une pour dans sur fonds '.split(),'EN':' the and of to is in fund for with '.split(),'DE':' der die und das ist mit für von '.split(),'IT':' il di che della per con fondo gli '.split(),'NL':' het van een en voor met '.split(),'SV':' och att för som av med fonden är '.split(),'ES':' el los las del que para con fondo '.split()}
def lang(t):
  c=collections.Counter(re.findall(r"[a-zàâäéèêëïîôöùûüçå]+",t.lower())); sc={k:sum(c[w] for w in v) for k,v in W.items()}
  return max(sc,key=sc.get) if sum(sc.values())>30 else '?'
def kind(r):
  n=nrm(r['report_name']+' '+r['file_name'])
  if 'dic' in n.split() or 'kid' in n or 'kiid' in n or "informations cles" in n: return 'DIC'
  if 'annuel' in n or 'annual' in n: return 'Rapport annuel'
  if 'semestriel' in n or 'semi' in n: return 'Rapport semestriel'
  return 'Factsheet'
docs=[];rows=[]
for i in EXT:
  z=F[i]; isin=z['ISIN']; rs=R.get(i,[])
  L=[]
  for k,r in enumerate(rs):
    t=open(f'txt/{i}_{k}.txt').read()
    tt=re.sub(r'\s','',t).upper()
    d=dict(id=int(i),nom=z['Name'],isin=isin,doc=r['report_name'],fichier=r['file_name'],type=kind(r),mois=mth(r['report_name']),
      langue=lang(t),isin_ok=isin.upper() in tt,lisible=len(t.strip())>200)
    L.append(d); docs.append(d)
  fs=[d for d in L if d['type']=='Factsheet']
  last=max(fs,key=lambda d:d['mois'] or '') if fs else None
  dup=[m for m,c in collections.Counter(d['mois'] for d in fs if d['mois']).items() if c>1]
  sans_mois=[d['fichier'] for d in fs if not d['mois']]
  pb=[]
  if not fs: pb.append('Aucune factsheet')
  else:
    if (last['mois'] or '')<'2026-08': pb.append(f"Factsheet ancienne ({last['mois']})")
    if not last['isin_ok']: pb.append("Factsheet sans l'ISIN de la part")
    if last['langue'] not in('FR','EN'): pb.append(f"Factsheet en {last['langue']}")
    if not last['lisible']: pb.append('Factsheet illisible (texte non extractible)')
  if dup: pb.append('Doublon de mois : '+', '.join(dup))
  if sans_mois: pb.append('Rapport sans mois dans le nom')
  rows.append(dict(id=int(i),nom=z['Name'],isin=isin,maison=EXT[i]['maison'],n_docs=len(L),n_fs=len(fs),
    dernier=last['mois'] if last else None,langue=last['langue'] if last else None,isin_ok=last['isin_ok'] if last else None,
    dic=any(d['type']=='DIC' for d in L),pol_fr=bool((z.get('InvestmentPolicy') or '').strip()),pol_en=bool((z.get('InvestmentPolicyEN') or '').strip()),pb=pb))
json.dump({'docs':docs,'rows':rows},open('audit_docs.json','w'),ensure_ascii=False)
C=collections.Counter
print('fiches',len(rows),'docs',len(docs),C(d['type'] for d in docs))
print('derniere fs mois',C(r['dernier'] for r in rows).most_common(8))
print('langue',C(r['langue'] for r in rows))
print('isin_ok',C(r['isin_ok'] for r in rows))
print('pb',C(p.split(' (')[0].split(' :')[0] for r in rows for p in r['pb']))
print('sans pb',sum(1 for r in rows if not r['pb']))
print('docs illisibles',sum(1 for d in docs if not d['lisible'])),'docs isin ko',sum(1 for d in docs if not d['isin_ok'])
for r in rows:
  if any('ISIN' in p or 'illisible' in p or 'Doublon' in p or 'sans mois' in p for p in r['pb']): print(r['id'],r['nom'][:40],r['pb'])
