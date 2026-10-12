#!/usr/bin/env python3
"""Client invest-law.eu (API JSON du site). Session partagée avec investlaw_upload.py (login / verify).
Carte complète du site et de l'API : docs/2026-10-12-guide-invest-law.md

  fund <ISIN|FundId>                    fiche + allocations + rapports + commentaires
  set <ISIN|FundId> champ=valeur… [--json f.json] [--apply]
                                        modifie la fiche (PUT complet reconstruit depuis l'état actuel) ;
                                        sans --apply : affiche seulement ancien -> nouveau
  delete-report <ISIN|FundId> <file_name> [--apply]
                                        supprime un rapport de gestion (la « croix »)
  call <METHODE> <chemin> [corps.json]  appel brut, ex. call GET /api/benchmarks
"""
import json, sys
from investlaw_upload import api

# champ du PUT /api/funds/{id} <- clé renvoyée par GET /api/funds
FIELDS = {
    'classification_id': 'ClassificationId', 'category': 'Category', 'fid': 'FID', 'is_active': 'IsActive',
    'maison_id': 'MaisonId', 'banque_id': 'BanqueId', 'name': 'Name', 'isin': 'ISIN', 'fund_code': 'FundCode',
    'creation_date': 'CreationDate', 'currency': 'Currency', 'fund_type': 'FundType',
    'fund_manager': 'fund_manager', 'fund_analyst': 'fund_analyst', 'compartment': 'Compartment',
    'total_assets': 'TotalAssets', 'fees': 'Fees', 'ter': 'TER', 'benchmark_id': 'BenchmarkId',
    'disclaimer': 'Disclaimer', 'investment_policy_fr': 'InvestmentPolicy',
    'investment_policy_en': 'InvestmentPolicyEN', 'investment_policy_nl': 'InvestmentPolicyNL',
    'duration': 'Duration', 'issuer_quality': 'IssuerQuality', 'esg': 'ESG', 'esg_code': 'ESG_code',
    'last_update': 'last_update', 'risque': 'Risque',
}
ALLOC = ('positions', 'sectors', 'assets', 'geographies')


def get(path):
    st, d = api('GET', path)
    if st != 200:
        sys.exit('GET %s -> %s : relancer investlaw_upload.py login/verify si 401' % (path, st))
    return d


def find_fund(key):
    funds = get('/api/funds')
    hit = [f for f in funds if str(f['FundId']) == key or (f.get('ISIN') or '').strip().upper() == key.upper()]
    if len(hit) != 1:
        sys.exit('%d fiche(s) pour %s' % (len(hit), key))
    return hit[0]


def body_from(f):
    b = {k: f.get(src) for k, src in FIELDS.items()}
    b['investment_policy'] = b['investment_policy_fr']
    if b['fid'] != 1:
        b['banque_id'] = None  # le formulaire n'envoie la banque que pour les fonds internes (FID=1)
    al = get('/api/funds/%s/allocations' % f['FundId'])
    for k in ALLOC:
        b[k] = [{'name': x['name'], 'percentage': x['percentage']} for x in al.get(k, [])]
    return b


def cmd_fund(key):
    f = find_fund(key); fid = f['FundId']
    print(json.dumps({'fiche': f, 'allocations': get('/api/funds/%s/allocations' % fid),
                      'rapports': get('/api/funds/%s/reports' % fid),
                      'commentaires': get('/api/funds/%s/comments' % fid)}, ensure_ascii=False, indent=1))


def cmd_set(key, pairs, json_file, apply):
    f = find_fund(key); old = body_from(f); new = dict(old)
    if json_file:
        new.update(json.load(open(json_file)))
    for p in pairs:
        k, v = p.split('=', 1)
        if k not in new:
            sys.exit('champ inconnu : %s (valides : %s)' % (k, ', '.join(new)))
        new[k] = None if v == '' else v
    new['investment_policy'] = new['investment_policy_fr']
    diff = {k: (old[k], new[k]) for k in new if old[k] != new[k]}
    for k, (a, b) in diff.items():
        print('%s : %r -> %r' % (k, a, b))
    if not diff or not apply:
        print('aucun changement' if not diff else '(simulation : ajouter --apply pour enregistrer)')
        return
    st, d = api('PUT', '/api/funds/%s' % f['FundId'], new)
    after = body_from(find_fund(str(f['FundId'])))
    bad = [k for k in diff if str(after[k]) != str(new[k])]
    print('PUT', st, d.get('error') or 'OK', '| écarts après relecture :', bad or 'aucun')


def cmd_delete_report(key, file_name, apply):
    f = find_fund(key)
    reps = [r for r in get('/api/funds/%s/reports' % f['FundId']) if r.get('file_name') == file_name]
    if len(reps) != 1:
        sys.exit('%d rapport(s) %s sur la fiche %s' % (len(reps), file_name, f['FundId']))
    r = reps[0]
    body = {'report_name': r.get('report_name') or '', 'file_name': r['file_name'],
            'report_date': str(r.get('report_date') or '')[:10]}
    print('fiche %s (%s) :' % (f['FundId'], f['Name']), body)
    if not apply:
        print('(simulation : ajouter --apply pour supprimer)')
        return
    st, d = api('DELETE', '/api/funds/%s/reports' % f['FundId'], body)
    print('DELETE', st, d.get('error') or 'OK')


if __name__ == '__main__':
    a = sys.argv[1:]
    apply = '--apply' in a
    a = [x for x in a if x != '--apply']
    jf = a[a.index('--json') + 1] if '--json' in a else None
    if jf:
        i = a.index('--json'); del a[i:i + 2]
    if a[:1] == ['fund'] and len(a) == 2: cmd_fund(a[1])
    elif a[:1] == ['set'] and len(a) >= 2: cmd_set(a[1], a[2:], jf, apply)
    elif a[:1] == ['delete-report'] and len(a) == 3: cmd_delete_report(a[1], a[2], apply)
    elif a[:1] == ['call'] and len(a) in (3, 4):
        st, d = api(a[1].upper(), a[2], json.load(open(a[3])) if len(a) == 4 else None)
        print(st, json.dumps(d, ensure_ascii=False, indent=1))
    else:
        sys.exit(__doc__)
