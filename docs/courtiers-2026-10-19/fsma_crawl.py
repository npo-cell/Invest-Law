import re, html, json, os, sys, time, http.cookiejar, urllib.request
from concurrent.futures import ThreadPoolExecutor
D = sys.argv[1]
B = 'https://www.fsma.be'
Q = '/fr/data-portal?f%5B0%5D=fa_active%3A1&f%5B1%5D=fa_activity%3A106702&f%5B2%5D=fa_content_type%3Actparty&f%5B3%5D=fa_sector%3A105110'
cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (research; invest-law)')]
def get(u, tries=4):
    for k in range(tries):
        try:
            t = op.open(urllib.request.Request(B + u, headers={'Referer': B + u}), timeout=40).read().decode('utf-8', 'ignore')
            if len(t) < 2000 and 'click here to continue' in t:
                continue
            return t
        except Exception as e:
            time.sleep(2 * (k + 1))
    return ''
def page(p):
    f = f'{D}/list-{p}.json'
    if os.path.exists(f): return json.load(open(f))
    t = get(Q + (f'&page={p}' if p else ''))
    out = []
    for m in re.finditer(r'href="(/fr/party/[^"]+)" class="search-result-teaser__link">\s*<div class="search-result-teaser__title">\s*(.*?)\s*</div>.*?Statut actif</div>.*?<div class="field__item">(.*?)</div>', t, re.S):
        out.append([m.group(1), html.unescape(m.group(2)).strip(), html.unescape(m.group(3)).strip()])
    if out: json.dump(out, open(f, 'w'))
    return out
with ThreadPoolExecutor(4) as ex:
    pages = list(ex.map(page, range(690)))
rows = [r for p in pages for r in p]
print('liste', len(rows), 'pages vides', sum(1 for p in pages if not p), flush=True)
brok = [r for r in rows if "Courtiers d'assurances" in r[2]]
print('courtiers', len(brok), flush=True)
def detail(r):
    slug = r[0].rsplit('/', 1)[1]
    f = f'{D}/p-{slug}.json'
    if os.path.exists(f): return
    t = get(r[0])
    m = re.search(r'href="/fr/export/party/(\d+)"', t)
    if not m: return
    j = get(f'/fr/export/party/{m.group(1)}')
    try: d = json.loads(j)
    except Exception: return
    d['_slug'], d['_nom'], d['_statuts'] = slug, r[1], r[2]
    json.dump(d, open(f, 'w'), ensure_ascii=False)
with ThreadPoolExecutor(4) as ex:
    list(ex.map(detail, brok))
print('détails', len([x for x in os.listdir(D) if x.startswith('p-')]), flush=True)
