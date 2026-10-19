#!/usr/bin/env python3
"""Synchronise les VNI reçues sur Zimbra (Excel CACEIS, CSV DNCA) avec invest-law.eu.

Prérequis : `pip install -q xlrd`, session invest-law ouverte (investlaw_upload.py login/verify),
variables ZIMBRA_USER / ZIMBRA_PASSWORD. Procédure de la routine : docs/zimbra-vni/CONSIGNE.md

  python3 tools/zimbra_vni_sync.py [--days 10] [--dir DOSSIER]           # simulation : ce qui serait importé
  python3 tools/zimbra_vni_sync.py [--days 10] [--dir DOSSIER] --apply   # import + relecture

Seules les fiches existantes sont mises à jour. Une VNI est écartée (signalée, pas importée) si :
date dans le futur, mails contradictoires, ou variation > 10 % par rapport à la VNI précédente.
"""
import csv, glob, json, os, sys, tempfile
from collections import defaultdict
from datetime import date, datetime, timedelta
import xlrd
import zimbra_mail
from investlaw_upload import api

MAX_VAR = 0.10


def opt(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def download(days, out):
    since = (date.today() - timedelta(days=days)).strftime('%m/%d/%Y')
    for m in zimbra_mail.messages(f'after:{since}'):
        d = os.path.join(out, m['id'])
        if not os.path.isdir(d):
            msg = zimbra_mail.email.message_from_bytes(zimbra_mail.rest('', id=m['id']))
            os.makedirs(d)
            for part in msg.walk():
                if part.get_filename():
                    with open(os.path.join(d, os.path.basename(zimbra_mail.h(part.get_filename()))), 'wb') as f:
                        f.write(part.get_payload(decode=True))


def num(s):
    return float(s.replace('\xa0', '').replace(' ', '').replace(',', '.'))


def parse(out):
    rows = []  # (isin, date, vni, source)
    for f in glob.glob(out + '/*/*.[xX][lL][sS]'):
        sh = xlrd.open_workbook(f).sheet_by_index(0)
        hd = sh.row_values(0)
        if 'ISIN Code' not in hd:
            continue
        for r in range(1, sh.nrows):
            v = dict(zip(hd, sh.row_values(r)))
            d = (date(1899, 12, 30) + timedelta(days=int(v['NAV Date']))).isoformat()
            rows.append((v['ISIN Code'].strip().upper(), d, round(float(v['Subscription Price']), 4), 'CACEIS'))
    for f in glob.glob(out + '/*/*.csv'):
        for v in csv.DictReader(open(f, encoding='utf-8-sig', errors='replace'), delimiter=';'):
            if v.get('ISIN') and v.get('VL') and v.get('Date cotation'):
                d = datetime.strptime(v['Date cotation'].strip(), '%d/%m/%Y').date().isoformat()
                rows.append((v['ISIN'].strip().upper(), d, round(num(v['VL']), 4), 'DNCA'))
    return rows


def main():
    apply = '--apply' in sys.argv
    out = opt('--dir') or tempfile.mkdtemp(prefix='zimbra_vni_')
    download(int(opt('--days', 10)), out)
    mail = defaultdict(lambda: defaultdict(set))
    for i, d, v, src in parse(out):
        mail[i][d].add(v)
    st, funds = api('GET', '/api/funds')
    if st != 200:
        sys.exit(f'GET /api/funds -> {st} : relancer investlaw_upload.py login/verify')
    ids = {(f.get('ISIN') or '').strip().upper(): f for f in funds}
    today = date.today().isoformat()
    todo, rejected, sites = [], [], {}
    for i in sorted(set(mail) & set(ids)):
        fid = ids[i]['FundId']
        site = sites[fid] = {e['VLDate']: float(e['VL']) for e in api('GET', f'/api/funds/{fid}/vl')[1]}
        known = dict(site)
        for d in sorted(mail[i]):
            vs = mail[i][d]
            v = next(iter(vs))
            if d in site:
                if len(vs) == 1 and abs(site[d] - v) >= 0.005:
                    rejected.append((fid, i, d, v, f'différente du site ({site[d]}), non modifiée'))
                continue
            prev = max((k for k in known if k < d), default=None)
            if d > today:
                rejected.append((fid, i, d, v, 'date future'))
            elif len(vs) > 1:
                rejected.append((fid, i, d, sorted(vs), 'mails contradictoires'))
            elif prev and abs(v / known[prev] - 1) > MAX_VAR:
                rejected.append((fid, i, d, v, f'variation {v / known[prev] - 1:+.1%} vs {prev} ({known[prev]})'))
            else:
                todo.append((fid, i, d, v))
                known[d] = v
    report = {'dossier': out, 'isin_mails': len(mail), 'fiches': len(set(mail) & set(ids)), 'a_importer': len(todo),
              'ecartees': rejected, 'importees': 0, 'ecarts_relecture': []}
    if apply and todo:
        body = 'ISIN,Date,VNI\n' + ''.join(f'{i},{d},{v:g}\n' for _, i, d, v in todo)
        st, r = api('POST', '/api/funds/vl/upload-by-isin', {'csv': body})
        report['reponse_import'] = [st, r]
        for fid in {t[0] for t in todo}:
            sites[fid] = {e['VLDate']: float(e['VL']) for e in api('GET', f'/api/funds/{fid}/vl')[1]}
        bad = [t for t in todo if abs(sites[t[0]].get(t[2], -1) - t[3]) >= 0.005]
        report['importees'] = len(todo) - len(bad)
        report['ecarts_relecture'] = bad
    report['detail'] = defaultdict(list)
    for fid, i, d, v in todo:
        report['detail'][f"{fid} {ids[i]['Name']}"].append(d)
    print(json.dumps(report, ensure_ascii=False, indent=1, default=str))


if __name__ == '__main__':
    main()
