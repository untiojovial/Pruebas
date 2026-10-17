# Retratos vía HTML de Wikipedia (la API REST sigue limitada): extrae la imagen del infobox y baja una miniatura estándar.
import re, json, subprocess, sys, os, time, html, urllib.parse
UA='Mozilla/5.0 (research; contact via claude.ai)'
T=[('maximo-griego','Maximus_the_Greek'),('simeon-tesalonica','Symeon_of_Thessalonica'),('zigabeno','Euthymios_Zigabenos'),('zonaras','John_Zonaras'),('glykas','Michael_Glykas'),('choniates','Niketas_Choniates')]
if len(sys.argv)>1: T=[t for t in T if t[0] in sys.argv[1:]]
def curl(u,f=None):
    a=['curl','-sS','-m','90','-L','-A',UA,'-w','\n%{http_code}']
    if f: a+=['-o',f]
    r=subprocess.run(a+[u],capture_output=True,text=True); return r.stdout
meta=json.load(open('IMG/meta.json')) if os.path.exists('IMG/meta.json') else {}
for slug,title in T:
    r=curl(f'https://en.wikipedia.org/wiki/{title}'); body,code=r.rsplit('\n',1)
    if code.strip()!='200': print(slug,'page',code,flush=True); time.sleep(20); continue
    i=body.find('infobox-image')
    im=re.search(r'<img[^>]*?src="//(?:thumb|upload)\.wikimedia\.org/wikipedia/([a-z]+)/(?:thumb/)?([0-9a-f]/[0-9a-f]{2})/([^/"?]+)[^"]*"[^>]*?data-file-width="(\d+)"',body[i:]) if i>=0 else None
    if not im: print(slug,'NO IMG',flush=True); meta[slug]={'title':title,'ok':False}; continue
    proj,hh,fn,w=im.group(1),im.group(2),im.group(3),int(im.group(4))
    u=(f'https://upload.wikimedia.org/wikipedia/{proj}/thumb/{hh}/{fn}/960px-{fn}' if w>960 else f'https://upload.wikimedia.org/wikipedia/{proj}/{hh}/{fn}')
    print(slug,proj,urllib.parse.unquote(fn),w,u,flush=True)
    ok=False
    for k in range(3):
        r=curl(u,f'IMG/{slug}.jpg'); c=r.strip().rsplit('\n',1)[-1]
        if c=='200' and os.path.getsize(f'IMG/{slug}.jpg')>3000: ok=True; break
        print(slug,'dl',c,flush=True); time.sleep(30)
    meta[slug]={'title':title,'src':u,'file':urllib.parse.unquote(fn),'proj':proj,'w':w,'ok':ok}
    json.dump(meta,open('IMG/meta.json','w'),ensure_ascii=False,indent=1)
    time.sleep(8)
print('DONE',flush=True)
