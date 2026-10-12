# -*- coding: utf-8 -*-
# Resalta pasajes sobre la imagen de una página ESCANEADA (PDF de imágenes o PNG/JPG) usando las cajas de palabras de Tesseract
# y una búsqueda aproximada por letras (tolera errores de OCR).
# SPECS = {id: [dict(pdf=..., page=N | img=..., lang='eng', from_=..., to=..., keys=[...], alts=[...], psm=3, dpi=170), ...]}
# Salida: rawt/<id>_segN.png + rawt/manifest.json. Uso: from scanhl import run
import subprocess, re, json, os, csv, io, unicodedata, tempfile
from difflib import SequenceMatcher
from PIL import Image, ImageDraw, ImageChops
COL = {'ctx': (255, 240, 160), 'key': (255, 176, 0), 'alt': (159, 211, 245)}
TESSDATA = '/tmp/claude-0/tessdata'
def letters(s):
    s = unicodedata.normalize('NFKD', s).casefold()
    s = ''.join(c for c in s if not unicodedata.combining(c)).replace('ʿ', '').replace('ʾ', '').replace('ß', 'ss')
    return ''.join(c for c in s if c.isalpha())
def page_image(d, dpi):
    if d.get('img'): return Image.open(d['img']).convert('RGB')
    tmp = tempfile.mktemp(prefix='scanhl_')
    subprocess.run(['pdftoppm', '-f', str(d['page']), '-l', str(d['page']), '-r', str(dpi), '-png', '-singlefile', d['pdf'], tmp], check=True)
    im = Image.open(tmp + '.png').convert('RGB'); os.remove(tmp + '.png'); return im
def ocr_words(im, lang, psm):
    tmp = tempfile.mktemp(prefix='scanhl_', suffix='.png'); im.save(tmp)
    env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
    out = subprocess.run(['tesseract', tmp, 'stdout', '-l', lang, '--psm', str(psm), 'tsv'], capture_output=True, text=True, env=env).stdout
    os.remove(tmp)
    W = []
    for r in csv.DictReader(io.StringIO(out), delimiter='\t', quoting=csv.QUOTE_NONE):
        t = (r.get('text') or '').strip()
        if r['level'] != '5' or not t: continue
        try: l, tp, w, h = int(r['left']), int(r['top']), int(r['width']), int(r['height'])
        except ValueError: continue
        W.append(dict(box=(l, tp, l + w, tp + h), text=t, line=(r['block_num'], r['par_num'], r['line_num'])))
    return W
def stream(W):
    S = []; owner = []
    for i, w in enumerate(W):
        t = letters(w['text']); S.append(t); owner += [i] * len(t)
    return ''.join(S), owner
def fuzzy(S, q, start=0, thr=0.72):
    """(inicio, fin) en S de la mejor coincidencia aproximada de q; ajusta los bordes con los bloques coincidentes."""
    L = len(q); best = (0.0, -1)
    for p in range(max(0, start), len(S) - L + 1):
        sm = SequenceMatcher(None, S[p:p + L], q, autojunk=False)
        if sm.real_quick_ratio() < thr or sm.quick_ratio() < thr: continue
        r = sm.ratio()
        if r > best[0]: best = (r, p)
        if r >= 0.97: break
    if best[1] < 0 or best[0] < thr: raise ValueError('no encontrado (mejor %.2f): %s' % (best[0], q[:50]))
    p = best[1]
    blocks = [b for b in SequenceMatcher(None, S[p:p + L], q, autojunk=False).get_matching_blocks() if b.size >= 3]
    if not blocks: return p, p + L
    b0, b1 = blocks[0], blocks[-1]
    st = max(start, p + b0.a - b0.b)
    en = min(len(S), p + b1.a + b1.size + (L - (b1.b + b1.size)))
    return st, max(en, st + 1)
def boxes(W, a, b):
    lines = {}
    for i in range(a, b + 1):
        x0, y0, x1, y1 = W[i]['box']; L = lines.setdefault(W[i]['line'], [x0, y0, x1, y1])
        L[0] = min(L[0], x0); L[1] = min(L[1], y0); L[2] = max(L[2], x1); L[3] = max(L[3], y1)
    return list(lines.values())
def seg(d, out):
    dpi = d.get('dpi', 170)
    im = page_image(d, dpi)
    W = ocr_words(im, d.get('lang', 'eng'), d.get('psm', 3))
    S, owner = stream(W)
    qf, qt = letters(d['from_']), letters(d['to'])
    pf, _e = fuzzy(S, qf)
    _s, pe = fuzzy(S, qt, pf + 1)
    a, b = owner[pf], owner[min(pe, len(owner)) - 1]
    ov = Image.new('RGB', im.size, (255, 255, 255)); dr = ImageDraw.Draw(ov)
    ctx = boxes(W, a, b)
    def rect(B, kind):
        for x0, y0, x1, y1 in B: dr.rectangle([x0 - 3, y0 - 3, x1 + 3, y1 + 3], fill=COL[kind])
    rect(ctx, 'ctx')
    for kind in ('key', 'alt'):
        for k in d.get(kind + 's', []):
            q = letters(k)
            ks, ke = fuzzy(S[pf:pe], q); ks += pf; ke += pf
            rect(boxes(W, owner[ks], owner[min(ke, len(owner)) - 1]), kind)
    im2 = ImageChops.multiply(im, ov)
    cy0 = min(v[1] for v in ctx); cy1 = max(v[3] for v in ctx)
    cx0 = min(v[0] for v in ctx); cx1 = max(v[2] for v in ctx)
    for _ in range(2):
        for w in W:
            x0, y0, x1, y1 = w['box']
            if y1 >= cy0 - 2 and y0 <= cy1 + 2 and x1 >= cx0 and x0 <= cx1: cx0 = min(cx0, x0); cx1 = max(cx1, x1)
    X0 = cx0 - 25; X1 = cx1 + 25; Y0 = cy0 - 7; Y1 = cy1 + 7
    im2.crop((int(max(0, X0)), int(max(0, Y0)), int(min(im.width, X1)), int(min(im.height, Y1)))).save(out)
def run(SPECS, man='rawt/manifest.json'):
    M = json.load(open(man)) if os.path.exists(man) else {}
    for sid, parts in SPECS.items():
        files = []
        for k, d in enumerate(parts, 1):
            f = f'rawt/{sid}_seg{k}.png'; seg(d, f); files.append(f)
        M[sid] = {'segs': files, 'title': None, 'errors': []}
        print(sid, 'ok', len(files))
    json.dump(M, open(man, 'w'), ensure_ascii=False, indent=1)
