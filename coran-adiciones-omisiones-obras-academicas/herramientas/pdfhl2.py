# -*- coding: utf-8 -*-
# Resalta pasajes sobre la imagen de una página de PDF (variante tolerante de pdfhl.py): compara solo letras (sin espacios, sin dígitos ni
# puntuación) para que no estorben los números de nota ni las palabras pegadas de algunas capas de texto.
# PDFS = {id: [dict(pdf, page, from_, to, keys=[], alts=[], clip=None), ...]}  -> rawt/<id>_segN.png + rawt/manifest.json
import subprocess, re, json, os, html, unicodedata
from PIL import Image, ImageDraw, ImageChops
COL = {'ctx': (255, 240, 160), 'key': (255, 176, 0), 'alt': (159, 211, 245)}
DPI = 170
def letters(s):
    s = unicodedata.normalize('NFKD', s).casefold()
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('ʿ', '').replace('ʾ', '')
    return ''.join(c for c in s if c.isalpha())
def words(pdf, page):
    x = subprocess.run(['pdftotext', '-f', str(page), '-l', str(page), '-bbox-layout', pdf, '-'], capture_output=True, text=True).stdout
    W = []
    for li, line in enumerate(re.findall(r'<line[^>]*>(.*?)</line>', x, re.S)):
        for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', line):
            W.append(dict(box=tuple(float(v) for v in m.groups()[:4]), text=html.unescape(m.group(5)), line=li))
    S = []; owner = []
    for i, w in enumerate(W):
        t = letters(w['text']); S.append(t); owner += [i] * len(t)
    return W, ''.join(S), owner
def find(S, owner, phrase, start_char=0):
    q = letters(phrase)
    k = S.find(q, start_char)
    if k < 0: raise ValueError('no encontrado: ' + phrase[:60])
    return owner[k], owner[k + len(q) - 1], k + len(q)
def boxes(W, a, b):
    lines = {}
    for i in range(a, b + 1):
        x0, y0, x1, y1 = W[i]['box']; L = lines.setdefault(W[i]['line'], [x0, y0, x1, y1])
        L[0] = min(L[0], x0); L[1] = min(L[1], y0); L[2] = max(L[2], x1); L[3] = max(L[3], y1)
    return list(lines.values())
def seg(d, out):
    W, S, owner = words(d['pdf'], d['page'])
    a, _, ca = find(S, owner, d['from_'])
    _, b, cb = find(S, owner, d['to'], ca - len(letters(d['from_'])) + 1)
    # el comienzo de 'from_' debe ser anterior al final de 'to'
    tmp = out + '.page'
    subprocess.run(['pdftoppm', '-f', str(d['page']), '-l', str(d['page']), '-r', str(DPI), '-png', '-singlefile', d['pdf'], tmp], check=True)
    im = Image.open(tmp + '.png').convert('RGB'); os.remove(tmp + '.png')
    s = DPI / 72; ov = Image.new('RGB', im.size, (255, 255, 255)); dr = ImageDraw.Draw(ov)
    ctx = boxes(W, a, b)
    def rect(B, kind):
        for x0, y0, x1, y1 in B: dr.rectangle([x0 * s - 3, y0 * s - 3, x1 * s + 3, y1 * s + 3], fill=COL[kind])
    rect(ctx, 'ctx')
    base = 0
    for kind in ('key', 'alt'):
        for k in d.get(kind + 's', []):
            q = letters(k); c0 = S.find(q, 0)
            # localizar la ocurrencia dentro del intervalo [a, b]
            pos = -1; st = 0
            while True:
                p = S.find(q, st)
                if p < 0: break
                if a <= owner[p] <= b: pos = p; break
                st = p + 1
            if pos < 0: raise ValueError('ancla no encontrada: ' + k[:60])
            rect(boxes(W, owner[pos], owner[pos + len(q) - 1]), kind)
    im = ImageChops.multiply(im, ov)
    # recorte: columna(s) que contienen el pasaje (evita incluir la otra columna de páginas a dos columnas)
    cy0 = min(v[1] for v in ctx); cy1 = max(v[3] for v in ctx)
    cx0 = min(v[0] for v in ctx); cx1 = max(v[2] for v in ctx)
    for _ in range(2):
        for w in W:
            x0, y0, x1, y1 = w['box']
            if y1 >= cy0 - 2 and y0 <= cy1 + 2 and x1 >= cx0 and x0 <= cx1: cx0 = min(cx0, x0); cx1 = max(cx1, x1)
    X0 = cx0 * s - 25; X1 = cx1 * s + 25; Y0 = cy0 * s - 9; Y1 = cy1 * s + 9
    im.crop((int(max(0, X0)), int(max(0, Y0)), int(min(im.width, X1)), int(min(im.height, Y1)))).save(out)
def run(PDFS, man='rawt/manifest.json'):
    M = json.load(open(man)) if os.path.exists(man) else {}
    for sid, parts in PDFS.items():
        files = []
        for k, d in enumerate(parts, 1):
            f = f'rawt/{sid}_seg{k}.png'; seg(d, f); files.append(f)
        M[sid] = {'segs': files, 'title': None, 'errors': []}
        print(sid, 'ok', len(files))
    json.dump(M, open(man, 'w'), ensure_ascii=False, indent=1)
