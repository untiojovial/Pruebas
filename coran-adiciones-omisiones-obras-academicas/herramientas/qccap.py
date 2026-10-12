# -*- coding: utf-8 -*-
# Capturas robustas para el pack QC: localiza la página por votación de k-gramas, usa la capa de texto del PDF (pdfhl2) y, si falla, OCR + búsqueda aproximada (scanhl).
import subprocess, json, os, re, functools
import pdfhl2, scanhl
letters = pdfhl2.letters
@functools.lru_cache(maxsize=None)
def page_texts(pdf):
    raw = subprocess.run(['pdftotext', '-raw', pdf, '-'], capture_output=True, text=True).stdout
    return [letters(p) for p in raw.split('\f')]
def find_page(pdf, text, hint=None, window=6):
    """página (1-based) con más coincidencias de k-gramas del texto; si hay pista, solo ±window."""
    P = page_texts(pdf); q = letters(text); k = 14
    grams = [q[i:i + k] for i in range(0, max(1, len(q) - k), 7)]
    rng = range(max(1, hint - window), min(len(P), hint + window) + 1) if hint else range(1, len(P) + 1)
    best = (0, None)
    for p in rng:
        n = sum(1 for g in grams if g in P[p - 1])
        if n > best[0]: best = (n, p)
    if not best[1] or best[0] < max(2, len(grams) // 4): return None
    return best[1]
def seg(d, out):
    d = dict(d)
    if not d.get('page'):
        d['page'] = find_page(d['pdf'], d['from_'] + ' ' + d['to'])
        if not d['page']: raise ValueError('página no encontrada: ' + d['from_'][:50])
    try:
        if d.get('ocr'): raise ValueError('ocr forzado')
        pdfhl2.seg(d, out); return 'texto'
    except Exception as e:
        scanhl.seg(d, out); return 'ocr'
def run(SPECS, man='rawt/manifest.json'):
    M = json.load(open(man)) if os.path.exists(man) else {}
    for sid, parts in SPECS.items():
        files = []; how = []
        for k, d in enumerate(parts, 1):
            f = f'rawt/{sid}_seg{k}.png'
            try: how.append(seg(d, f)); files.append(f)
            except Exception as e: print('  FALLO', sid, k, str(e)[:100]); how.append('FALLO')
        M[sid] = {'segs': files, 'title': None, 'errors': [h for h in how if h == 'FALLO']}
        print(sid, 'ok', len(files), how)
    json.dump(M, open(man, 'w'), ensure_ascii=False, indent=1)
