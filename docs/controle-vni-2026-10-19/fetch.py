import json, sys
sys.path.insert(0, '/home/user/Invest-Law/tools')
from investlaw_upload import api
S = sys.argv[1]
mail = json.load(open(S + '/work/mail_vni.json'))
isins = {r['isin'].upper() for r in mail}
st, funds = api('GET', '/api/funds'); assert st == 200, st
json.dump(funds, open(S + '/work/funds.json', 'w'))
hit = [f for f in funds if (f.get('ISIN') or '').strip().upper() in isins]
print(len(funds), 'fiches ;', len(hit), 'fiches dont l ISIN est dans les mails')
st, latest = api('GET', '/api/funds/latest-vl'); print('latest-vl', st, type(latest).__name__, str(latest)[:300])
json.dump(latest, open(S + '/work/latest.json', 'w'))
vl = {}
for f in hit:
    st, d = api('GET', '/api/funds/%s/vl' % f['FundId']); vl[f['FundId']] = d if st == 200 else {'err': st}
json.dump(vl, open(S + '/work/site_vl.json', 'w'))
f = hit[0]; print(f['FundId'], f['ISIN'], str(vl[f['FundId']])[:400])
