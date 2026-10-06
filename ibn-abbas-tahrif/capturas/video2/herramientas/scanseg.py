# Recortes subrayados de páginas escaneadas (Irwaʾ al-Ghalil, PDF de usul.ai).
# Coordenadas medidas a 200 ppp; las imágenes se generan a 300 ppp (x1,5).
# Uso: python3 scanseg.py <carpeta con x-<pág>.png> irwaspecs.json
import json, sys
from PIL import Image, ImageChops
S = 1.5
COL = {'ctx': (255, 236, 120), 'key': (255, 176, 0)}
def hl(im, box, kind):
    x0, y0, x1, y1 = [int(v * S) for v in box]
    reg = im.crop((x0, y0, x1, y1))
    tint = Image.new('RGB', reg.size, COL[kind])
    im.paste(ImageChops.multiply(reg, tint), (x0, y0))
def piece(src, p):
    im = Image.open(f"{src}/x-{p['pdfpage']}.png").convert('RGB')
    for kind in ('ctx', 'key'):
        for b in p.get(kind, []): hl(im, b, kind)
    x0, y0, x1, y1 = [int(v * S) for v in p['crop']]
    return im.crop((x0, y0, x1, y1))
def build(src, specs, out_dir='rawv', manifest='rawv/manifest.json'):
    man = json.load(open(manifest))
    for sp in specs:
        segs = []
        for i, seg in enumerate(sp['segments']):
            ims = [piece(src, p) for p in seg]
            W = max(i.width for i in ims); H = sum(i.height for i in ims) + 30 * (len(ims) - 1)
            o = Image.new('RGB', (W, H), 'white'); y = 0
            for k, im in enumerate(ims):
                if k:
                    for x in range(0, W, 24): o.paste((190, 190, 190), (x, y + 14, min(W, x + 12), y + 16))
                    y += 30
                o.paste(im, (W - im.width, y)); y += im.height
            f = f"{out_dir}/{sp['id']}_seg{i + 1}.png"; o.save(f); segs.append(f)
        man[sp['id']] = {'segs': segs, 'title': None, 'errors': []}
        print(sp['id'], segs)
    json.dump(man, open(manifest, 'w'), indent=1)
if __name__ == '__main__':
    build(sys.argv[1], json.load(open(sys.argv[2])))
