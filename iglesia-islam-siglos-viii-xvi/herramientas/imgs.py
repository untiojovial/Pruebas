import json, subprocess, time, urllib.parse, os, sys
UA = 'Mozilla/5.0 (research; contact via claude.ai)'
T = [('juan-damasceno','John_of_Damascus'),('pedro-venerable','Peter_the_Venerable'),('inocencio-iii','Pope_Innocent_III'),('aquino','Thomas_Aquinas'),
     ('riccoldo','Riccoldo_da_Monte_di_Croce'),('dante','Dante_Alighieri'),('cusa','Nicholas_of_Cusa'),('pio-ii','Pope_Pius_II'),('savonarola','Girolamo_Savonarola'),('vives','Juan_Luis_Vives')]
out = {}
def curl(u, f=None):
    a = ['curl','-sS','-m','90','-L','-A',UA,'-w','\n%{http_code}']
    if f: a += ['-o', f]
    r = subprocess.run(a + [u], capture_output=True, text=True)
    return r.stdout
for slug, title in T:
    if os.path.exists(f'IMG/{slug}.jpg') and os.path.getsize(f'IMG/{slug}.jpg') > 5000: continue
    for attempt in range(4):
        r = curl(f'https://en.wikipedia.org/api/rest_v1/page/summary/{title}')
        body, code = r.rsplit('\n', 1)
        if code.strip() == '200': break
        time.sleep(40)
    try:
        d = json.loads(body); oi = d.get('originalimage') or {}; src = oi.get('source', '')
    except Exception as e:
        out[slug] = {'err': 'summary ' + code}; print(slug, 'ERR summary', code, flush=True); time.sleep(20); continue
    src = src.split('?')[0]
    cands = []
    if '/wikipedia/commons/' in src and '/thumb/' not in src:
        fn = src.rsplit('/', 1)[-1]
        cands.append(src.replace('/commons/', '/commons/thumb/') + f'/900px-{fn}')
    cands.append(src)
    ok = False
    for u in cands:
        for attempt in range(3):
            r = curl(u, f'IMG/{slug}.jpg'); code = r.strip().rsplit('\n', 1)[-1]
            if code == '200' and os.path.getsize(f'IMG/{slug}.jpg') > 5000: ok = True; break
            time.sleep(45)
        if ok: break
    out[slug] = {'title': title, 'src': src, 'w': oi.get('width'), 'h': oi.get('height'), 'ok': ok, 'desc': d.get('description')}
    print(slug, ok, src, oi.get('width'), oi.get('height'), flush=True)
    json.dump(out, open('IMG/meta.json', 'w'), ensure_ascii=False, indent=1)
    time.sleep(25)
print('DONE', flush=True)
