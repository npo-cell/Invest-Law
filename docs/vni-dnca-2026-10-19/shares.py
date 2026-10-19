import json,sys,glob
seen=set()
for f in sys.argv[1:]:
  try:d=json.load(open(f))
  except Exception:continue
  for c in d.get('fund_categories',[]):
    for fu in c['funds']:
      if any(k in fu['fund_slug'] for k in ('europe-growth','value-europe')):
        for s in fu['shares']:
          k=s['share_path']
          if k not in seen: seen.add(k);print(f,k)
