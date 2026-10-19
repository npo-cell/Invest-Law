"""Fusionne registre FSMA (courtiers ILP actifs) + annuaires des compagnies -> courtiers Bruxelles/Wallonie.
Usage : python3 -I fusion.py <scratchpad> <sortie.csv>"""
import csv, glob, html, json, re, sys, unicodedata
S, OUT = sys.argv[1], sys.argv[2]
L = S + '/locators/'

def region(z):
    z = int(z) if z and z.isdigit() else 0
    if 1000 <= z <= 1299: return 'Bruxelles'
    if 1300 <= z <= 1499: return 'Brabant wallon'
    if 4000 <= z <= 4999: return 'Liège'
    if 5000 <= z <= 5999: return 'Namur'
    if 6600 <= z <= 6999: return 'Luxembourg'
    if 6000 <= z <= 6599 or 7000 <= z <= 7999: return 'Hainaut'
    return ''

def bce(x):
    d = re.sub(r'\D', '', x or '')
    return d.zfill(10) if d else ''

FORMES = r'\b(srl|sprl|sa|nv|bv|bvba|scrl|scs|snc|sc|comm ?v|cvba|vof|sprlu|asbl|s ?r ?l|s ?a|sca)\b'
STOP = {'assurances', 'assurance', 'verzekeringen', 'verzekering', 'bureau', 'cabinet', 'kantoor', 'et', 'de', 'des', 'du', 'la', 'le', 'les', 'and', 'en', 'fils', 'group', 'groupe', 'insurance', 'insurances', 'courtage', 'courtier', 'courtiers', 'finance', 'finances'}

def toks(n):
    n = unicodedata.normalize('NFKD', html.unescape(n or '')).encode('ascii', 'ignore').decode().lower()
    n = n.split('|')[0]
    n = re.sub(FORMES, ' ', re.sub(r'[^a-z0-9 ]', ' ', n.replace('.', '')))
    return {t for t in n.split() if len(t) > 1 and t not in STOP}

def dom(x):
    x = (x or '').lower().strip()
    if '@' in x: x = x.split('@')[1]
    x = re.sub(r'^https?://', '', x).split('/')[0]
    x = re.sub(r'^www\.', '', x)
    generic = ('gmail', 'hotmail', 'outlook', 'skynet', 'yahoo', 'live.', 'msn', 'proximus', 'telenet', 'voo.be', 'scarlet', 'icloud')
    return '' if not x or '.' not in x or any(g in x for g in generic) else x

# --- FSMA
B = {}
for f in glob.glob(S + '/fsma/p-*.json'):
    d = json.load(open(f))
    ad = [a for a in d.get('address', []) if not a.get('valid_to_date')] or d.get('address', [])
    if not ad: continue
    a = ad[-1]
    if (a.get('country_code') or 'BE') != 'BE' or not region(a.get('zip', '')): continue
    k = bce(d.get('enterprise_number')) or d['_slug']
    B[k] = {'nom': d['_nom'], 'bce': bce(d.get('enterprise_number')), 'fsma': d.get('cbfa_code', ''),
            'rue': f"{a.get('street', '')} {a.get('house_number', '')}".strip(), 'cp': a.get('zip', ''), 'ville': a.get('city', ''),
            'region': region(a.get('zip', '')), 'statuts': d['_statuts'], 'cies': {}, 'tel': '', 'email': '', 'site': '',
            'fiche': 'https://www.fsma.be/fr/party/' + d['_slug'], 'brocom': False}
idx_zip = {}
for k, b in B.items():
    b['t'] = toks(b['nom'])
    idx_zip.setdefault(b['cp'], []).append(k)
idx_dom = {}

def attach(cie, nom, cp, ville, num, tel, email, site, brocom=False):
    k = bce(num) if num else ''
    if k not in B:
        k = ''
        d = dom(site) or dom(email)
        if d and d in idx_dom and toks(nom) & B[idx_dom[d]]['t']: k = idx_dom[d]  # domaine + au moins un mot commun
        else:
            t, best = toks(nom), 0
            cands = idx_zip.get(cp, []) if cp else [x for x, b in B.items() if ville and b['ville'].lower() == ville.lower()]
            for c in cands:
                bt = B[c]['t']
                if t and bt:
                    j = len(t & bt) / len(t | bt)
                    if j > best: best, k = j, c
            if best < 0.5: k = ''
            if not k and not cp:  # commune non reconnue (ex. BRUSSEL) : nom quasi identique, toute la zone
                for c, b in B.items():
                    if t and b['t'] and len(t & b['t']) / len(t | b['t']) >= 0.8 and len(t) >= 2: k = c; break
    if not k: return False
    b = B[k]
    b['cies'][cie] = 1
    b['tel'] = b['tel'] or (tel or '').strip()
    b['email'] = b['email'] or (email or '').strip()
    b['site'] = b['site'] or (site or '').strip()
    b['brocom'] = b['brocom'] or str(brocom).lower() == 'true'
    for d in (dom(site), dom(email)):
        if d: idx_dom.setdefault(d, k)
    return True

stats = {}
def run(cie, rows):
    n = sum(attach(cie, *r) for r in rows)
    stats[cie] = (n, len(rows))

ag = [x for x in json.load(open(L + 'aglist.json')) if region(x['address']['zip'])]
run('AG Insurance', [(x['brokerName'], x['address']['zip'], x['address']['city'], x['bce'], (x.get('contactDataB2C') or {}).get('phone'), (x.get('contactDataB2C') or {}).get('email'), x.get('siteUrl'), x.get('isBrocom')) for x in ag])
ax = json.load(open(L + 'axa100.json'))
ax = ax['features'] if isinstance(ax, dict) else ax
rows = []
for f in ax:
    p = f.get('properties', f); c = p.get('contactMethods') or {}
    pa = (c.get('postAddressContact') or [{}])[0]
    if not region(pa.get('postCode', '')): continue
    rows.append((p.get('nameFr') or p.get('nameDu'), pa.get('postCode'), pa.get('municipality'), p.get('neon'),
                 ((c.get('phoneContact') or [{}])[0]).get('phoneNumber'), (c.get('emailContact') or {}).get('url'),
                 (c.get('webPageContact') or {}).get('url') if isinstance(c.get('webPageContact'), dict) else '', p.get('hasBrocom')))
run('AXA', rows)
nn = [x for x in json.load(open(L + 'nnlist.json'))['data'] if region((x.get('address') or {}).get('zip', ''))]
run('NN', [(x['name'], x['address']['zip'], x['address']['city'], '', x.get('phone'), x.get('email'), x.get('website')) for x in nn])
try:
    bal = [x for x in json.load(open(S + '/loc2/baloise.json')) if region((x.get('address') or {}).get('postalCode', ''))]
    run('Baloise', [(x['name'], x['address']['postalCode'], x['address']['cityName'], x.get('kboNumber'), x.get('phoneNumber'), x.get('emailAddress'), x.get('website'), x.get('brocom')) for x in bal])
except FileNotFoundError: pass
try:
    al = [x for x in json.load(open(S + '/loc2/allianz.json')) if region(str(x.get('ZipCode', '')))]
    run('Allianz', [(x['OfficeName'], str(x['ZipCode']), '', '', x.get('Telephone'), x.get('Email'), x.get('Website'), x.get('Brocom')) for x in al])
except FileNotFoundError: pass
t = open(L + 'patfr.html', encoding='utf-8').read()
pat = []
for m in re.finditer(r'"popup":"(.*?)","cssClass"', t):
    p = json.loads('"' + m.group(1) + '"')
    nm = re.search(r'>(.*?)</a>', p); parts = p.split('<br />')
    if nm and len(parts) >= 3: pat.append((html.unescape(nm.group(1)), '', html.unescape(parts[-1]).strip(), '', '', '', ''))
pat = list({r[0] + r[2]: r for r in pat}.values())
run('Patronale Life', pat)

CIES = ['AG Insurance', 'AXA', 'Allianz', 'Baloise', 'NN', 'Patronale Life']
rows = sorted(B.values(), key=lambda b: (-len(b['cies']), b['region'], b['nom'].lower()))
with open(OUT, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['Courtier', 'N° BCE', 'N° FSMA', 'Adresse', 'Code postal', 'Commune', 'Région / province', 'Nb de compagnies identifiées', 'Compagnies identifiées'] + CIES + ['Courtier crédit hypothécaire', 'Téléphone', 'Email', 'Site web', 'Fiche FSMA'])
    for b in rows:
        w.writerow([b['nom'], b['bce'], b['fsma'], b['rue'], b['cp'], b['ville'].title(), b['region'], len(b['cies']), ', '.join(c for c in CIES if c in b['cies'])]
                   + ['oui' if c in b['cies'] else '' for c in CIES]
                   + ['oui' if 'crédit hypothécaire' in b['statuts'] else '', b['tel'], b['email'], b['site'], b['fiche']])
print('courtiers B+W', len(B), 'rattachés', stats)
import collections
print(collections.Counter(len(b['cies']) for b in B.values()), collections.Counter(b['region'] for b in B.values()))
