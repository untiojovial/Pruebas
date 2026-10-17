import subprocess, re, html, json, time, urllib.parse, os
UA='Mozilla/5.0 (research; contact via claude.ai)'
F=[('manuel-ii','commons','Manuel_II_Palaiologos_(cropped).jpg'),('palamas','commons','Григорий_Палама_14в.jpg'),('cantacuzeno','commons','John_VI_Kantakouzenos.jpg'),('maximo-griego','commons','Максим_Грек.jpg'),('simeon-tesalonica','commons','Peinture_sainte_sophie_01558.jpg'),('choniates','commons','Niketas_Choniates.jpg'),('zonaras','commons','Jean_Zonare_Historien_Grec._(BM_1879,1213.109).jpg'),('zigabeno','en','Commentary_on_Psalms_by_Euthymios_Zygabenos.jpg')]
out=json.load(open('IMG/lic.json')) if os.path.exists('IMG/lic.json') else {}
for slug,proj,name in F:
    if slug in out and out[slug].get('ok'): continue
    host='commons.wikimedia.org' if proj=='commons' else 'en.wikipedia.org'
    u=f'https://{host}/wiki/File:'+urllib.parse.quote(name)
    body=None
    for k in range(5):
        r=subprocess.run(['curl','-sS','-m','60','-L','-A',UA,'-w','\n%{http_code}',u],capture_output=True,text=True).stdout
        b,c=r.rsplit('\n',1)
        if c.strip()=='200': body=b; break
        print(slug,c.strip(),flush=True); time.sleep(40)
    if not body: out[slug]={'ok':False}; continue
    os.makedirs('IMG/lic_html',exist_ok=True); open(f'IMG/lic_html/{slug}.html','w',encoding='utf-8').write(body)
    def tx(x): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<script.*?</script>|<style.*?</style>','',x,flags=re.S)))).strip()
    fi=re.search(r'<table class="fileinfotpl.*?</table>',body,re.S)
    lic=re.findall(r'<(?:div|table)[^>]*class="[^"]*(?:licensetpl|commons-file-information-table)[^"]*"[^>]*>.*?</(?:div|table)>',body,re.S)
    out[slug]={'ok':True,'file':name,'summary':tx(fi.group(0))[:1200] if fi else '','lic':tx(' '.join(lic))[:900]}
    json.dump(out,open('IMG/lic.json','w'),ensure_ascii=False,indent=1)
    print(slug,'ok',flush=True); time.sleep(10)
print('DONE')
