# -*- coding: utf-8 -*-
# Comprueba que cada trozo del texto «original» mostrado en cada tarjeta está en alguna de las páginas leídas (caché Vc) o en el SBLGNT local.
import sys, re, glob, html, json, unicodedata
sys.path.insert(0, '.')
import adverify as V
from adspec import CARDS
T = ''
for f in glob.glob(V.AD + '/Vc/*.dat'):
    raw = open(f, encoding='utf-8', errors='ignore').read()
    s = raw.lstrip()
    if s[:1] in '{[':
        try: raw = ' '.join(V.flat(json.loads(s)))
        except Exception: pass
    t = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', raw, flags=re.S); t = html.unescape(re.sub(r'<[^>]+>', ' ', t))
    T += ' ' + V.L(html.unescape(t))
# SBLGNT Mateo local
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb/V')
import greek
T += ' ' + V.L(greek.g('Mt', 1, 20, 21) + ' ' + greek.g('Mt', 1, 25, 25))
print('universo', len(T))
bad = 0
for c in CARDS:
    o = re.sub(r'\[\[k:(.*?)\]\]', r'\1', c['orig'])
    segs = [x for x in re.split(r'…|<br>|\[[^\]]{1,12}\]', o) if len(V.L(x)) > 12]
    res = []
    for sg in segs:
        sg = sg.strip(' “”"«»')
        # (los trozos con corchetes de verso ya se cortaron arriba)
        res.append(V.L(sg) in T)
    ok = all(res)
    if not ok: bad += 1
    print(c['id'], 'OK' if ok else 'REVISAR', res)
print('REVISAR:', bad)
