import xlrd, glob, csv, sys, json, re, os
from datetime import date, timedelta, datetime
root = sys.argv[1]; rows = []
for f in sorted(glob.glob(root + '/zmail/*/*.XLS')):
    sh = xlrd.open_workbook(f).sheet_by_index(0)
    hd = sh.row_values(0)
    for r in range(1, sh.nrows):
        v = dict(zip(hd, sh.row_values(r)))
        d = (date(1899, 12, 30) + timedelta(days=int(v['NAV Date']))).isoformat()
        rows.append(dict(src='CACEIS', mail=f.split('/')[-2], isin=v['ISIN Code'], name=v['Share Name'], date=d,
                         vni=v['Subscription Price'], red=v['Redemption Price'], ccy=v['Sub Fund Currency']))
for f in sorted(glob.glob(root + '/zmail/*/*.csv')):
    for v in csv.DictReader(open(f, encoding='utf-8-sig', errors='replace'), delimiter=';'):
        num = lambda s: float(s.replace('\xa0', '').replace(' ', '').replace(',', '.'))
        rows.append(dict(src='DNCA', mail=f.split('/')[-2], isin=v['ISIN'].strip(), name=v['Fonds'].strip(),
                         date=datetime.strptime(v['Date cotation'], '%d/%m/%Y').date().isoformat(), vni=num(v['VL']), red=None, ccy=v['Devise']))
json.dump(rows, open(root + '/work/mail_vni.json', 'w'), indent=0)
print(len(rows), 'lignes;', len({r['isin'] for r in rows}), 'ISIN;', sorted({r['date'] for r in rows}))
print('CACEIS sub!=red:', [r for r in rows if r['red'] is not None and r['red'] != r['vni']][:3])
