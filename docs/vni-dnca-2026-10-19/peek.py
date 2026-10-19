import json,sys,os,datetime as dt
for f in sorted(sys.argv[1:]):
  d=json.load(open(f)); k=d['items']['share']['id']; data=[r for r in d['data'] if r.get(k) is not None]
  we=sum(dt.date.fromisoformat(r['date']).weekday()>=5 for r in data)
  print(os.path.basename(f),d['items']['share']['legend'],len(data),data[0]['date'],data[0][k],data[-1]['date'],data[-1][k],'weekend',we, 'nulls',len(d['data'])-len(data))
