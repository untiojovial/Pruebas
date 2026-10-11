import re,html,json,subprocess,os,sys
R2='/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hp/R2'
OUT='/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hp/Xloc'
os.makedirs(OUT,exist_ok=True)
sh_pages={'1673':[891,892,893],'1711':[310,311,312],'5756':[896,897],'16946':[218,219],'23790':[1292,1293],'767':[3690,3695,3696,3697,3736,3737],'8463':[4569],'11495':[124,125,126,127,128,129],'12304':[897,898],'6521':[629,630,631]}
web=[]
for c,n in [('bukhari',304),('bukhari',1462),('bukhari',2658),('bukhari',2731),('bukhari',4425),('muslim',79),('abudawud',4679),('abudawud',236),('tirmidhi',2613),('tirmidhi',3883),('ahmad',8862),('ibnhibban',3323),('ibnabishaybah',31048),('nasai',4805),('bayhaqi',16407),('abdalrazzaq',15478),('abdalrazzaq',15486),('abdalrazzaq',15487)]:
    web.append(f'https://hadithunlocked.com/{c}:{n}')
web+=['https://quran.ksu.edu.sa/tafseer/tabary/sura2-aya282.html','https://quran.ksu.edu.sa/tafseer/katheer/sura2-aya282.html','https://quran.ksu.edu.sa/tafseer/qortobi/sura3-aya42.html',
'https://quran-tafsir.net/baidawy/sura2-aya282.html','https://quran-tafsir.net/alrazy/sura2-aya282.html','https://quran-tafsir.net/alrazy/sura4-aya34.html','https://quran-tafsir.net/maturidy/sura2-aya282.html','https://quran-tafsir.net/alusy/sura4-aya34.html','https://quran.ksu.edu.sa/tafseer/katheer/sura4-aya34.html','https://quran-tafsir.net/baidawy/sura4-aya34.html','https://quran.ksu.edu.sa/tafseer/qortobi/sura2-aya282.html','https://quran-tafsir.net/seddiq/sura2-aya282.html','https://quran-tafsir.net/seddiq/sura4-aya34.html','https://quran-tafsir.net/shawkany/sura2-aya282.html','https://quran-tafsir.net/shawkany/sura4-aya34.html','https://hadithunlocked.com/bukhari:3411','https://forums.alkafeel.net/archive/index.php/t-39824.html']
res=[]
def nass(t):
    m=re.search(r'<div class="nass[^"]*"[^>]*>(.*?)</div>\s*</div>',t,re.S)
    return html.unescape(re.sub(r'<[^>]+>','',m.group(1) if m else t))
for b,ps in sh_pages.items():
    for p in ps:
        fn=f'{R2}/dl/{b}/p{p}.html'
        if not os.path.exists(fn): print('missing',b,p); continue
        res.append(dict(id=f'sh_{b}_{p}',url=f'https://shamela.ws/book/{b}/{p}',passage=nass(open(fn,encoding='utf-8',errors='ignore').read())))
for u in web:
    t=subprocess.run(['curl','-sS','-m','90','-L',u],capture_output=True,text=True).stdout
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    s=html.unescape(re.sub(r'<[^>]+>',' ',t)); s=re.sub(r'\s+',' ',s)
    res.append(dict(id='w_'+u[-40:],url=u,passage=s)); print(u[-50:],len(s))
json.dump(res,open(OUT+'/passages.json','w'),ensure_ascii=False,indent=1)
print(len(res))
