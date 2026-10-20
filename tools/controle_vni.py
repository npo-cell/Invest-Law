#!/usr/bin/env python3
"""Contrôle des VNI : python3 tools/controle_vni.py DOSSIER (DOSSIER contient data.json = {funds, vl} extrait de /api/funds et /api/funds/{id}/vl)."""
import json, collections, sys, calendar
from datetime import date
S=sys.argv[1]; d=json.load(open(S+'/data.json')); today=date(2026,10,20)
D=lambda s: date.fromisoformat(s[:10])
def add3m(x):
    m=x.month+3; y=x.year+(m-1)//12; m=(m-1)%12+1
    return date(y,m,min(x.day,calendar.monthrange(y,m)[1]))
rows=[]
for f in d['funds']:
    v=sorted(((D(e['VLDate']),float(e['VL'])) for e in d['vl'][str(f['FundId'])] if e.get('VL') not in (None,'')))
    c=D(f['CreationDate']) if f['CreationDate'] else None
    r=dict(id=f['FundId'],nom=f['Name'].strip(),isin=f['ISIN'],maison=(f.get('MaisonName') or '').strip(),actif=bool(f['IsActive']),
           creation=f['CreationDate'] or '',n=len(v),premiere=v[0][0].isoformat() if v else '',
           derniere=v[-1][0].isoformat() if v else '',ecart=None,flags=[],statut='')
    jumps=[(d1,a,b) for (d0,a),(d1,b) in zip(v,v[1:]) if a>0 and abs(b/a-1)>0.2]
    franc=[j for j in jumps if j[0].year<=2002 and 6.3<j[1]/j[2]<6.8]
    other=[j for j in jumps if j not in franc]
    if v and c: r['ecart']=(v[0][0]-c).days
    if not v: r['statut']='sans_vni'
    elif len(other)>=3: r['statut']='fausses'
    elif not c: r['statut']='creation_absente'
    elif r['ecart']<-7: r['statut']='avant_creation'
    elif v[0][0]>add3m(c): r['statut']='incomplet'
    else: r['statut']='ok'
    if r['statut']=='fausses': r['flags'].append(f'{len(other)} sauts de plus de 20 % (ex. {other[0][0]} : {other[0][1]:g} → {other[0][2]:g})')
    if franc: r['flags'].append(f'historique en francs avant {franc[-1][0]} (÷ 6,56 au passage à l\'euro)')
    if other and r['statut']!='fausses': r['flags'].append('; '.join(f'saut {(b/a-1)*100:+.0f} % le {x} ({a:g} → {b:g})' for x,a,b in other))
    if v:
        we=sum(1 for x,_ in v if x.weekday()>=5)
        if we/len(v)>0.03: r['flags'].append(f'{we} VNI datées un week-end ({we*100//len(v)} %) : dates probablement décalées d\'un jour')
        if any(x<=0 for _,x in v): r['flags'].append('VNI nulle ou négative')
        if v[-1][0]>today: r['flags'].append(f'date future {v[-1][0]}')
        if (today-v[-1][0]).days>45: r['flags'].append(f'plus mise à jour depuis le {v[-1][0].strftime("%d/%m/%Y")}')
    if r['statut']=='ok' and r['ecart'] is not None and r['ecart']<0: r['flags'].append(f'1re VNI {-r["ecart"]} j avant la création (décalage de date)')
    rows.append(r)
json.dump(rows,open(S+'/rows.json','w'),ensure_ascii=False,indent=0)
print(collections.Counter(r['statut'] for r in rows))
print(collections.Counter((r['statut'],r['actif']) for r in rows))
print('flags',sum(1 for r in rows if r['flags']), 'fausses:',[ (r['nom'],r['flags'][0]) for r in rows if r['statut']=='fausses'])
print('weekend',sum(1 for r in rows if any('week-end' in x for x in r['flags'])),'stale',sum(1 for r in rows if any('plus mise' in x for x in r['flags'])),'franc',sum(1 for r in rows if any('francs' in x for x in r['flags'])))
for r in rows:
  if any('saut' in x and 'sauts' not in x for x in r['flags']): print(r['nom'],r['flags'])
