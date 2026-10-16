import json,csv,openpyxl,collections,sys
S=sys.argv[1]
t=open(S+'/funds.json').read();site=json.loads(t[t.index(' ')+1:])
siteI={f['ISIN'].strip().upper():f for f in site if f.get('ISIN')}
wb=openpyxl.load_workbook(sys.argv[2],read_only=True);rows=list(wb.active.iter_rows(values_only=True))[1:]
rng=[r for r in rows if r[1]]
I=[r[1].strip().upper() for r in rng]
print('lignes',len(rng),'ISIN uniques',len(set(I)))
wb_=list(csv.DictReader(open('docs/wealth-belgium-2026-10-15/fonds-isin.csv')))
k=[c for c in wb_[0] if 'ISIN' in c.upper()][0]
wbI={r[k].strip().upper() for r in wb_}
R=set(I)
a=R&set(siteI); b=(R&wbI)-set(siteI); c=R-set(siteI)-wbI
print('sur le site',len(a),'| WB seulement',len(b),'| WB et site',len(R&wbI&set(siteI)),'| ni l un ni l autre',len(c))
print('site hors gamme',len(set(siteI)-R),'| WB hors gamme',len(wbI-R))
act=collections.Counter(siteI[i].get('IsActive') for i in a);print('actifs site dans gamme',act)
byI={r[1].strip().upper():r for r in rng}
for name,s in [('reste',c)]:
  print(name,collections.Counter(byI[i][0] for i in s).most_common())
  print(collections.Counter(byI[i][6] for i in s).most_common(15))
print('avail',collections.Counter(r[5] for r in rng))
print('types gamme',collections.Counter(r[0] for r in rng))
with open(S+'/reste.csv','w') as f:
  w=csv.writer(f);w.writerow(['Type','ISIN','Nom','Maison'])
  for r in rng:
    if r[1].strip().upper() in c: w.writerow([r[0],r[1],r[2],r[6]])
