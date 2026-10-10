# Resalta las pp. 85–86 de la ed. Dar Ibn Kathir 2010 (juz' 1, «Descripción de los manuscritos»; archive.org 2_20200225_20200225, PDF pp. 89–90).
import json, sys
sys.path.insert(0, '.')
from scanhl import seg
from PIL import Image
def bands(path, x0=140, x1=1370, y0=130, y1=1990):
    im = Image.open(path).convert('L'); px = im.load(); out = []; inb = False
    for y in range(y0, y1):
        r = sum(1 for x in range(x0, x1, 2) if px[x, y] < 128)
        if r > 3 and not inb: s = y; inb = True
        elif r <= 3 and inb:
            inb = False
            if y - s > 8: out.append((s, y))
    return out
H = '../hp/V2img/'
P89, P90 = H + 'ms-089.png', H + 'ms-090.png'
B89, B90 = bands(P89), bands(P90)
S = [
 (P89, B89, 4, 7, [(5, 150, 1100, 'key'), (6, 880, 1470, 'key')]),
 (P90, B90, 5, 8, [(5, 700, 1470, 'key'), (6, 140, 960, 'alt'), (7, 140, 595, 'key'), (8, 1260, 1365, 'key')]),
 (P90, B90, 12, 15, [(12, 415, 1470, 'key')]),
 (P90, B90, 21, 25, [(23, 110, 975, 'key'), (24, 880, 1320, 'alt')]),
]
files = []
for k, (p, B, a, b, hl) in enumerate(S, 1):
    f = f'rawt/X-dar85_seg{k}.png'
    seg(p, a, b, hl, f, 150, 1350, B)
    files.append(f)
M = json.load(open('rawt/manifest.json')); M['X-dar85'] = {'segs': files, 'title': None, 'errors': []}
json.dump(M, open('rawt/manifest.json', 'w'), ensure_ascii=False, indent=1)
print(files)
