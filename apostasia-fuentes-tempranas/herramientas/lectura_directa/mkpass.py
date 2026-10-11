import re,html,json,subprocess,os,sys
R2='/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hp/R2'
OUT='/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hp/Zloc2'
os.makedirs(OUT,exist_ok=True)
sh_pages={'8463':[3917,3918,3919,3920],'151100':[128,129],'13122':[2639,2640],'587':[558,730,731],'21751':[7806,7807,7808,7819,7820],'21735':[134],'21739':[929]}
hu=['malik:36-25','malik:36-26']+[f'abdalrazzaq:{n}' for n in (18773,18775,18786,18787,18788,18791,18792)]
res=[]
def nass(t):
    m=re.search(r'<div class="nass[^"]*"[^>]*>(.*?)</div>\s*</div>',t,re.S)
    return html.unescape(re.sub(r'<[^>]+>','',m.group(1) if m else t))
for b,ps in sh_pages.items():
    for p in ps:
        t=open(f'{R2}/dl/{b}/p{p}.html',encoding='utf-8',errors='ignore').read()
        res.append(dict(id=f'sh_{b}_{p}',url=f'https://shamela.ws/book/{b}/{p}',passage=nass(t)))
for u in hu:
    t=subprocess.run(['curl','-sS','-m','60','-L',f'https://hadithunlocked.com/{u}'],capture_output=True,text=True).stdout
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    s=html.unescape(re.sub(r'<[^>]+>',' ',t)); s=re.sub(r'\s+',' ',s)
    res.append(dict(id='hu_'+u,url=f'https://hadithunlocked.com/{u}',passage=s))
    print(u,len(s))
json.dump(res,open(OUT+'/passages.json','w'),ensure_ascii=False,indent=1)
print(len(res))
