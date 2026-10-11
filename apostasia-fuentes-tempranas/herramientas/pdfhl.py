# Resalta un pasaje sobre la imagen de una página de PDF, con las coordenadas de las palabras (pdftotext -bbox-layout).
# PDFS = {id: [dict(pdf, page, from_, to, keys=[], alts=[]), ...]}  -> rawt/<id>_segN.png + rawt/manifest.json
import subprocess, re, json, os, html, unicodedata
from PIL import Image, ImageDraw, ImageChops
COL = {'ctx': (255, 240, 160), 'key': (255, 176, 0), 'alt': (159, 211, 245)}
DPI = 170
def tok(s):
    s = unicodedata.normalize('NFKC', s).replace('’', "'").replace('‘', "'").lower()
    return [t for t in re.split(r"[^\w]+", s) if t]
def words(pdf, page):
    x = subprocess.run(['pdftotext', '-f', str(page), '-l', str(page), '-bbox-layout', pdf, '-'], capture_output=True, text=True).stdout
    W = []
    for li, line in enumerate(re.findall(r'<line[^>]*>(.*?)</line>', x, re.S)):
        for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', line):
            W.append(dict(box=tuple(float(v) for v in m.groups()[:4]), text=html.unescape(m.group(5)), line=li))
    # tokens con referencia a la palabra; une guiones de fin de línea
    T = []
    i = 0
    while i < len(W):
        w = W[i]; t = w['text']
        if t.endswith('-') and i + 1 < len(W) and W[i + 1]['line'] != w['line']:
            for k in tok(t[:-1] + W[i + 1]['text']): T.append((k, [i, i + 1]))
            i += 2; continue
        for k in tok(t): T.append((k, [i]))
        i += 1
    return W, T
def find(T, phrase, start=0):
    q = tok(phrase)
    for i in range(start, len(T) - len(q) + 1):
        if all(T[i + j][0] == q[j] for j in range(len(q))): return i, i + len(q) - 1
    raise ValueError('no encontrado: ' + phrase[:60])
def boxes(W, T, a, b):
    idx = sorted({w for k in range(a, b + 1) for w in T[k][1]})
    lines = {}
    for i in idx:
        x0, y0, x1, y1 = W[i]['box']; L = lines.setdefault(W[i]['line'], [x0, y0, x1, y1])
        L[0] = min(L[0], x0); L[1] = min(L[1], y0); L[2] = max(L[2], x1); L[3] = max(L[3], y1)
    return list(lines.values())
def seg(d, out):
    W, T = words(d['pdf'], d['page'])
    a, _ = find(T, d['from_']); _, b = find(T, d['to'], a)
    tmp = out + '.page'
    subprocess.run(['pdftoppm', '-f', str(d['page']), '-l', str(d['page']), '-r', str(DPI), '-png', '-singlefile', d['pdf'], tmp], check=True)
    im = Image.open(tmp + '.png').convert('RGB'); os.remove(tmp + '.png')
    s = DPI / 72; ov = Image.new('RGB', im.size, (255, 255, 255)); dr = ImageDraw.Draw(ov)
    ctx = boxes(W, T, a, b)
    def rect(B, kind):
        for x0, y0, x1, y1 in B: dr.rectangle([x0 * s - 3, y0 * s - 3, x1 * s + 3, y1 * s + 3], fill=COL[kind])
    rect(ctx, 'ctx')
    for kind in ('key', 'alt'):
        for k in d.get(kind + 's', []):
            i, j = find(T, k, a); rect(boxes(W, T, i, j), kind)
    im = ImageChops.multiply(im, ov)
    allx = [w['box'] for w in W]
    X0 = min(v[0] for v in allx) * s - 25; X1 = max(v[2] for v in allx) * s + 25
    Y0 = min(v[1] for v in ctx) * s - 25; Y1 = max(v[3] for v in ctx) * s + 25
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
