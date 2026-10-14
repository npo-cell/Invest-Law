import sys,json,os,hashlib,urllib.request,urllib.parse,subprocess
sys.path.insert(0,'/home/user/Invest-Law/tools')
from investlaw import get
from concurrent.futures import ThreadPoolExecutor
F=get('/api/funds'); json.dump(F,open('funds.json','w'),ensure_ascii=False)
ids=[z['FundId'] for z in F]
with ThreadPoolExecutor(8) as ex: R=dict(zip(map(str,ids),ex.map(lambda i:get(f'/api/funds/{i}/reports'),ids)))
json.dump(R,open('reports.json','w'),ensure_ascii=False)
os.makedirs('pdf',exist_ok=True); os.makedirs('txt',exist_ok=True)
jobs=[(i,k,r) for i,rs in R.items() for k,r in enumerate(rs)]
def go(j):
  i,k,r=j; p=f'pdf/{i}_{k}.pdf'
  try:
    if not os.path.exists(p):
      d=urllib.request.urlopen(urllib.parse.quote(r['file_url'],safe=':/%'),timeout=120).read(); open(p,'wb').write(d)
    t=subprocess.run(['pdftotext','-l','8',p,'-'],capture_output=True,text=True,timeout=120).stdout
    open(f'txt/{i}_{k}.txt','w').write(t); return 'ok'
  except Exception as e: return 'err '+str(e)[:60]
with ThreadPoolExecutor(10) as ex: out=list(ex.map(go,jobs))
print(len(F),len(jobs),{x:out.count(x) for x in set(out)})
