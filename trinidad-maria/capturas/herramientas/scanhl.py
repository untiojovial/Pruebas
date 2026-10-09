# Resalta un escaneo (imagen de página) con los mismos colores que las capturas web.
# SCANS = {id: [ {img, bands:[(y0,y1)...] (detectadas con scanlines.py), first, last, hl:[(band, x0, x1, kind)]} , ...]}
import json, os
from PIL import Image, ImageChops
COL = {'ctx': (255, 240, 160), 'key': (255, 176, 0), 'alt': (159, 211, 245)}
def bands(path):
    im = Image.open(path).convert('L'); W, H = im.size; px = im.load(); out = []; inb = False
    for y in range(H):
        r = sum(1 for x in range(0, W, 2) if px[x, y] < 128)
        if r > 3 and not inb: s = y; inb = True
        elif r <= 3 and inb:
            inb = False
            if y - s > 6: out.append((s, y))
    return out
def seg(path, first, last, hl, out, xl=120, xr=1300, B=None):
    B = B or bands(path); im = Image.open(path).convert('RGB')
    ov = Image.new('RGB', im.size, (255, 255, 255))
    from PIL import ImageDraw
    d = ImageDraw.Draw(ov)
    pad = 9
    for i in range(first, last + 1):
        a, b = B[i]; d.rectangle([xl, a - pad, xr, b + pad], fill=COL['ctx'])
    for (i, x0, x1, kind) in hl:
        a, b = B[i]; d.rectangle([x0, a - pad, x1, b + pad], fill=COL[kind])
    im = ImageChops.multiply(im, ov)
    y0 = B[first][0] - 30; y1 = B[last][1] + 30
    im.crop((xl - 25, y0, xr + 25, y1)).save(out)
def run(SCANS, man='rawt/manifest.json'):
    M = json.load(open(man)) if os.path.exists(man) else {}
    for sid, parts in SCANS.items():
        files = []
        for k, p in enumerate(parts, 1):
            f = f'rawt/{sid}_seg{k}.png'; seg(p['img'], p['first'], p['last'], p.get('hl', []), f, p.get('xl', 120), p.get('xr', 1300), p.get('B')); files.append(f)
        M[sid] = {'segs': files, 'title': None, 'errors': []}
    json.dump(M, open(man, 'w'), ensure_ascii=False, indent=1)
