# Resalta la p. 302 (juz' 2) de al-Bidāya wa-l-Nihāya, ed. Dār Ibn Kathīr 2010 (archive.org 2_20200225_20200225, PDF p. 742).
import json, sys
sys.path.insert(0, '.')
from scanhl import bands, seg
P = '../hp/V2img/pg-742.png'
B = bands(P)
segs = [
 dict(first=2, last=3, hl=[(2, 380, 1085, 'key'), (2, 160, 320, 'alt'), (3, 1065, 1525, 'alt')]),
 dict(first=8, last=20, hl=[(14, 515, 690, 'alt'), (18, 165, 985, 'key'), (19, 735, 1525, 'key'), (19, 160, 222, 'key'), (20, 1100, 1528, 'key')]),
 dict(first=21, last=23, hl=[(21, 1240, 1540, 'alt'), (23, 1150, 1540, 'alt')]),
]
files = []
for k, s in enumerate(segs, 1):
    f = f'rawt/X-dar302_seg{k}.png'
    seg(P, s['first'], s['last'], s['hl'], f, 120, 1545, B)
    files.append(f)
M = json.load(open('rawt/manifest.json')); M['X-dar302'] = {'segs': files, 'title': None, 'errors': []}
json.dump(M, open('rawt/manifest.json', 'w'), ensure_ascii=False, indent=1)
print(files)
