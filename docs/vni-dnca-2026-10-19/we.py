import json,sys,os,datetime as dt
for f in sorted(sys.argv[1:]):
  d=json.load(open(f)); k=d['items']['share']['id']
  w=[r['date'] for r in d['data'] if dt.date.fromisoformat(r['date']).weekday()>=5]
  ds={r['date'] for r in d['data']}
  hol=[x for x in ('2026-01-01','2026-04-03','2026-04-06','2026-05-01','2026-05-14','2026-05-25','2026-08-15','2025-12-24','2025-12-25','2025-12-26','2025-12-31') if x in ds]
  print(os.path.basename(f)[:12],w,hol)
