# -*- coding: utf-8 -*-
# Especificaciones de captura del pack «taʿlīq de Ibn ʿAbbās» (TA). Uso: python3 -I yspecs_build.py
import json, re, sys, os, unicodedata
HP = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hp'
DIA = re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ‌-‏]')
MAP = {'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا', 'ى': 'ي', 'ة': 'ه', 'ؤ': 'و', 'ئ': 'ي', 'ی': 'ي', 'ک': 'ك', 'ے': 'ي'}
SH = "#bu_load_prev{display:none!important} div.nomargin:has(#bu_tashkeel){display:none!important} .heading-title.heading-border{display:none!important} html,body,*{scroll-behavior:auto!important}"
S = "https://shamela.ws/book/"
QT = "html.dark-mode, html.dark-mode body, html.dark-mode body *{background:#fff!important;color:#000!important;text-shadow:none!important} html,body,*{scroll-behavior:auto!important}"
def norm(s):
    o = []
    for c in DIA.sub('', s):
        c = MAP.get(c, c)
        if unicodedata.category(c)[0] in 'LN': o.append(c)
        elif o and o[-1] != ' ': o.append(' ')
    return ''.join(o).strip()
PASS = {}
for d in ['Yloc', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8']:
    f = f'{HP}/{d}/passages.json'
    if os.path.exists(f):
        for p in json.load(open(f)):
            PASS.setdefault(p['url'], []).append(norm(p['passage']))
def sh(i, u, segs, **kw): return dict(id=i, url=S + u, css=SH, minW=400, segments=segs, **kw)
def web(i, u, segs, css='html,body,*{scroll-behavior:auto!important}', minW=300, **kw): return dict(id=i, url=u, css=css, minW=minW, segments=segs, **kw)
def sg(f, t, keys=(), alts=(), nth=None):
    d = {"from": f, "to": t, "keys": list(keys)}
    if alts: d["alts"] = list(alts)
    if nth: d["nth"] = nth
    return d
SPECS = []
def add(*specs): SPECS.extend(specs)
exec(open('yspecs_defs.py').read())
def check():
    bad = 0
    for s in SPECS:
        texts = PASS.get(s['url'])
        if not texts: print('· sin texto de referencia:', s['id'], s['url']); continue
        T = ' || '.join(texts)
        for g in s['segments']:
            a = T.find(norm(g['from'])); b = T.find(norm(g['to']), max(a, 0))
            if a < 0: print('✗', s['id'], 'from', g['from']); bad += 1
            if b < 0: print('✗', s['id'], 'to', g['to']); bad += 1
            for k in g['keys'] + g.get('alts', []):
                kk = T.find(norm(k), max(a, 0))
                if kk < 0 or (b >= 0 and kk > b + len(norm(g['to']))): print('✗', s['id'], 'key', k); bad += 1
    return bad
if __name__ == '__main__':
    ids = [s['id'] for s in SPECS]; assert len(ids) == len(set(ids)), 'ids repetidos'
    n = check(); json.dump(SPECS, open('yspecs.json', 'w'), ensure_ascii=False, indent=1)
    print(len(SPECS), 'specs;', n, 'errores')
