import json, subprocess, time, os, sys
UA = 'Mozilla/5.0 (research; contact via claude.ai)'
T = [('cantacuzeno','John_VI_Kantakouzenos'),('maximo-griego','Maximus_the_Greek'),('simeon-tesalonica','Symeon_of_Thessalonica'),('zigabeno','Euthymios_Zigabenos'),('zonaras','John_Zonaras'),('glykas','Michael_Glykas'),('choniates','Niketas_Choniates')]
if len(sys.argv) > 1: T = [t for t in T if t[0] in sys.argv[1:]]
meta = json.load(open('IMG/meta.json')) if os.path.exists('IMG/meta.json') else {}
def curl(u, f=None):
    a = ['curl','-sS','-m','90','-L','-A',UA,'-w','\n%{http_code}']
    if f: a += ['-o', f]
    r = subprocess.run(a + [u], capture_output=True, text=True)
    return r.stdout
for slug, title in T:
    if os.path.exists(f'IMG/{slug}.jpg') and os.path.getsize(f'IMG/{slug}.jpg') > 5000: continue
    d = None
    for attempt in range(4):
        r = curl(f'https://en.wikipedia.org/api/rest_v1/page/summary/{title}')
        body, code = r.rsplit('\n', 1)
        if code.strip() == '200':
            try: d = json.loads(body); break
            except Exception: pass
        time.sleep(60)
    if not d: print(slug, 'ERR summary', flush=True); continue
    oi = d.get('originalimage') or {}; src = oi.get('source', '').split('?')[0]
    if not src: print(slug, 'NO IMAGE', d.get('title'), flush=True); meta[slug] = {'title': title, 'ok': False}; continue
    w = oi.get('width') or 0
    cands = []
    if '/thumb/' not in src and w > 960:
        fn = src.rsplit('/', 1)[-1]
        for proj in ('commons', 'en'):
            if f'/wikipedia/{proj}/' in src:
                cands.append(src.replace(f'/wikipedia/{proj}/', f'/wikipedia/{proj}/thumb/') + f'/960px-{fn}')
    cands.append(src)
    ok = False
    for u in cands:
        for attempt in range(3):
            r = curl(u, f'IMG/{slug}.jpg'); code = r.strip().rsplit('\n', 1)[-1]
            if code == '200' and os.path.getsize(f'IMG/{slug}.jpg') > 5000: ok = True; break
            time.sleep(45)
        if ok: break
    meta[slug] = {'title': title, 'src': src, 'w': w, 'h': oi.get('height'), 'ok': ok, 'desc': d.get('description')}
    print(slug, ok, src, w, oi.get('height'), flush=True)
    json.dump(meta, open('IMG/meta.json', 'w'), ensure_ascii=False, indent=1)
    time.sleep(15)
print('DONE', flush=True)
