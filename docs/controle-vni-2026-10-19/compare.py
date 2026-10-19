import json, sys
from collections import defaultdict
S = sys.argv[1]
mail = json.load(open(S + '/work/mail_vni.json')); funds = json.load(open(S + '/work/funds.json'))
vl = json.load(open(S + '/work/site_vl.json'))
m = defaultdict(dict)  # isin -> date -> set(vni)
names = {}
for r in mail:
    m[r['isin'].upper()].setdefault(r['date'], set()).add(round(r['vni'], 4)); names[r['isin'].upper()] = (r['src'], r['name'], r['ccy'])
out = []
for f in funds:
    i = (f.get('ISIN') or '').strip().upper()
    if i not in m: continue
    site = {e['VLDate']: float(e['VL']) for e in vl[str(f['FundId'])]}
    last = max(site) if site else None
    ok = diff = miss = 0; diffs = []
    for d, vs in sorted(m[i].items()):
        if len(vs) > 1: diffs.append((d, 'mails contradictoires', sorted(vs)))
        v = next(iter(vs))
        if d not in site: miss += 1
        elif abs(site[d] - v) < 0.005: ok += 1
        else: diff += 1; diffs.append((d, site[d], v))
    out.append(dict(id=f['FundId'], isin=i, site_name=f['Name'], src=names[i][0], mail_name=names[i][1], ccy=names[i][2], site_ccy=f.get('Currency'),
                    active=f.get('IsActive'), last=last, last_vl=site.get(last), n_site=len(site), mail_dates=len(m[i]), ok=ok, diff=diff, miss=miss, diffs=diffs,
                    mail_last=max(m[i]), mail_last_vl=sorted(m[i][max(m[i])])))
json.dump(out, open(S + '/work/result.json', 'w'), indent=1)
for o in sorted(out, key=lambda o: (o['src'], o['site_name'])):
    print(f"{o['id']:>4} {o['isin']} {o['src']:6} {o['site_name'][:42]:42} {o['ccy']}/{o['site_ccy']} act={o['active']} site_last={o['last']} ({o['last_vl']}) n={o['n_site']} | mail {o['mail_dates']}j ok={o['ok']} diff={o['diff']} absent={o['miss']} mail_last={o['mail_last']} {o['mail_last_vl']}")
    for d in o['diffs']: print('      DIFF', d)
