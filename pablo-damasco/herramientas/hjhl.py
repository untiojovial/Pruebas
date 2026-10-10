# Resalta la p. 35 de la introducción de la ed. Dar Hajar (al-Turki) a al-Bidaya wa-l-Nihaya (archive.org bn21_20190727, PDF p. 35).
import json, sys
sys.path.insert(0, '.')
from scanhl import seg
from PIL import Image
def bands(path, x0=120, y0=60):
    im = Image.open(path).convert('L'); px = im.load(); W, H = im.size; out = []; inb = False
    for y in range(y0, H - 120):
        r = sum(1 for x in range(x0, W - 120, 2) if px[x, y] < 128)
        if r > 3 and not inb: s = y; inb = True
        elif r <= 3 and inb:
            inb = False
            if y - s > 8: out.append((s, y))
    return out
P = '../hp/V2img/hj-035.png'
B = bands(P)
f = 'rawt/X-hj35_seg1.png'
seg(P, 0, 4, [(0, 170, 1105, 'key'), (1, 170, 1105, 'key'), (2, 775, 1105, 'key')], f, 165, 1110, B)
M = json.load(open('rawt/manifest.json')); M['X-hj35'] = {'segs': [f], 'title': None, 'errors': []}
json.dump(M, open('rawt/manifest.json', 'w'), ensure_ascii=False, indent=1)
print(Image.open(f).size)
