import json,sys,os,csv
nav_dir,out=sys.argv[1],sys.argv[2]
A=('2026-06-01','2026-10-05'); E=('2026-02-20','2026-10-05'); F=('0000','2026-10-05')
R={**{i:A for i in 'LU1694789451 LU1907594748 LU1907595398 LU0284393930 LU0284394235 LU2254337392 LU0284396016'.split()},'LU0284394664':E,
   **{i:F for i in 'LU1515062757 LU3077228958 LU1490785091 LU1490785505 LU0870553020 LU2707622630 LU1515062674'.split()}}
w=csv.writer(open(out,'w',newline='')); w.writerow(['ISIN','Date','VNI'])
for isin,(a,b) in R.items():
  d=json.load(open(os.path.join(nav_dir,isin+'.json'))); k=d['items']['share']['id']; assert isin.lower() in k
  rows=[(r['date'],r[k]) for r in d['data'] if r.get(k) is not None and a<=r['date']<=b]
  for dte,v in rows: w.writerow([isin,dte,repr(float(v))])
  print(isin,len(rows),rows[0][0],rows[-1][0])
ab=json.load(open(os.path.join(nav_dir,'LU1694789451.json')))
print('check',[(r['date'],r['a-lu1694789451']) for r in ab['data'] if '2026-10-06'<=r['date']<='2026-10-15'])
