# -*- coding: utf-8 -*-
# Cobertura de 8-gramas de letras de cada cita en los textos (OCR/HTML/TXT) que descargaron los agentes. Indica si la cita existe en esas fuentes.
import sys, os, re, glob, json, html, unicodedata
IG = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ig'
def L(s):
    s = unicodedata.normalize('NFKD', s).casefold()
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('æ','ae').replace('œ','oe').replace('ſ','s').replace('j','i').replace('v','u').replace('ǽ','ae')
    return ''.join(c for c in s if c.isalnum())
K = 8
def grams(t): return {t[i:i+K] for i in range(max(0, len(t)-K+1))}
cache = {}
def load(f):
    if f in cache: return cache[f]
    try:
        raw = open(f, encoding='utf-8', errors='ignore').read()
    except Exception: raw = ''
    if f.endswith(('.html', '.htm')):
        raw = html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', raw, flags=re.S)))
    cache[f] = L(raw); return cache[f]
def best(quote, files):
    q = L(quote); g = grams(q)
    if not g: return 0, None
    bestc, bf = 0, None
    for f in files:
        t = load(f)
        if not t: continue
        # cobertura por presencia (rápida): muestreo cada 4 gramas
        sample = list(g)[::3] or list(g)
        c = sum(1 for x in sample if x in t) / len(sample)
        if c > bestc: bestc, bf = c, f
    return bestc, bf
if __name__ == '__main__':
    ids = sys.argv[1:]
    for m in sorted(glob.glob(IG + '/M[1-8]')):
        P = json.load(open(m + '/passages.json', encoding='utf-8'))
        sel = [p for p in P if p['id'] in ids]
        if not sel: continue
        files = [f for f in glob.glob(m + '/dl/**/*', recursive=True) if f.endswith(('.txt', '.out', '.html', '.htm', '.json')) and os.path.getsize(f) < 80e6]
        for p in sel:
            for fld in ('quote_orig', 'quote_en'):
                v = p.get(fld) or ''
                if len(L(v)) < 20: continue
                c, f = best(v, files)
                print(p['id'], fld, f'{c:.2f}', os.path.basename(f or '-'))
