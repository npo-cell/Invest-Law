import json, os, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
D = sys.argv[1]
def get(u, tries=3):
    for k in range(tries):
        try:
            return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=40).read())
        except Exception:
            time.sleep(2 * (k + 1))
    return None
cps = {}
for p in [str(x) for x in range(10, 15)] + [str(x) for x in range(40, 80)]:
    for c in get(f'https://contact.baloise.be/api/address/cities?filter={p}') or []:
        cp = c['postalCode']
        if cp.startswith(p) and cp not in cps:
            cps[cp] = (c['coordinates']['latitude'], c['coordinates']['longitude'], c['mainNames'].get('FRA', ''))
json.dump(cps, open(f'{D}/cps.json', 'w'))
print('CP', len(cps), flush=True)
KEEP_AL = ['OfficeId', 'OfficeName', 'Telephone', 'Email', 'Website', 'Street', 'ZipCode', 'City', 'CityName', 'Brocom']
def bal(cp):
    la, lo, _ = cps[cp]
    return get(f'https://contact.baloise.be/api/brokersearch/brokers?latitude={la}&longitude={lo}&registered=false') or []
def al(cp):
    r = get(f'https://apps.allianz.be/GSERest/api/GetBrokerDetails?postal_code={cp}&broker_id=NULL&product_code=11&search_type=Broker&lang_code=FR&country_code=BE') or []
    return [{k: v for k, v in x.items() if k in KEEP_AL} for x in r]  # champs publics uniquement
for name, fn in (('baloise', bal), ('allianz', al)):
    out = {}
    with ThreadPoolExecutor(3) as ex:
        for res in ex.map(fn, sorted(cps)):
            for x in res:
                out[str(x.get('brokerId') or x.get('OfficeId'))] = x
    json.dump(list(out.values()), open(f'{D}/{name}.json', 'w'), ensure_ascii=False)
    print(name, len(out), flush=True)
