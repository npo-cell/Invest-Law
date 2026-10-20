import csv, json, os, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
S = sys.argv[1]; D = S + '/nbb'
B = 'https://consult.cbso.nbb.be/api'
CODES = {'70': 'ca', '9900': 'marge_brute', '10/49': 'total_bilan', '9087': 'etp', '10/15': 'fonds_propres', '9905': 'resultat', '9901': 'res_exploit', '1003': 'etp_1003'}
def get(u, js=True):
    for k in range(4):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers=({'Accept': 'application/json'} if js else {}) | {'User-Agent': 'Mozilla/5.0'}), timeout=40).read()
            return json.loads(r) if js else r.decode('utf-8', 'ignore')
        except urllib.error.HTTPError as e:
            if e.code in (404, 400): return None
            time.sleep(3 * (k + 1))
        except Exception:
            time.sleep(3 * (k + 1))
    return None
def one(bce):
    f = f'{D}/{bce}.json'
    if os.path.exists(f): return
    out = {'bce': bce}
    lst = get(f'{B}/rs-consult/published-deposits?page=0&size=10&enterpriseNumber={bce}&sort=periodEndDate,desc&sort=depositDate,desc')
    deps = (lst or {}).get('content') or []
    if deps:
        d = deps[0]  # dernier exercice, dépôt le plus récent (rectificatif éventuel)
        out.update(annee=d.get('periodEndDateYear'), modele=d.get('modelName'), ref=d.get('reference'))
        t = get(f"{B}/external/broker/public/deposits/consult/csv/{d['id']}", js=False) or ''
        for row in csv.reader(t.splitlines()):
            if len(row) >= 2 and row[0] in CODES: out[CODES[row[0]]] = row[1]
    json.dump(out, open(f, 'w'))
rows = json.load(open(S + '/sheet_rows.json'))
bces = sorted({r[1] for r in rows if r[1]})
with ThreadPoolExecutor(4) as ex: list(ex.map(one, bces))
print('fini', len(bces), len([x for x in os.listdir(D) if x[0].isdigit()]))
