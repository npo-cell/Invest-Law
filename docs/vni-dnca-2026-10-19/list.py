import json,sys
want=sys.argv[2].split(',')
d=json.load(open(sys.argv[1]))
for c in d["fund_categories"]:
  for f in c["funds"]:
    for s in f["shares"]:
      if s["isin_code"] in want: print(s["isin_code"],f["fund_slug"],s["share_slug"],s["share_path"])
