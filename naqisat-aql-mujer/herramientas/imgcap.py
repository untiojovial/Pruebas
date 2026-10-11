# -*- coding: utf-8 -*-
# Recortes de páginas escaneadas de archive.org con resaltado (amarillo = contexto, naranja = frase clave, azul = matiz).
# Uso: python3 -I imgcap.py   (lee R3/*.xml y R3/*.jpg; escribe rawt/NQ-*_segN.png y actualiza rawt/manifest.json)
import json, sys
from PIL import Image, ImageChops, ImageDraw
sys.path.insert(0, '.')
from imgwords import page_words
R3 = '../hp/R3/'
YEL, ORA, BLU = (255, 240, 160), (255, 176, 0), (159, 211, 245)
JOBS = [
 # id, xml, jpg, n, segmentos
 ('NQ-qa55', 'qa.xml', 'qa_n58.jpg', 58, [
   dict(lines=(15, 25), orange=[(22, 0, 10), (23, 0, 1), (23, 3, 12), (24, 0, 5), (24, 7, 9), (25, 0, 4)], blue=[(16, 0, 9), (17, 0, 8)])]),
 ('NQ-th143', 'th.xml', 'th_n242.jpg', 242, [
   dict(lines=(6, 7), orange=[(6, 5, 11), (7, 0, 7)], blue=[]),
   dict(lines=(14, 16), orange=[(16, 6, 12)], blue=[])]),
 ('NQ-th144', 'th.xml', 'th_n243.jpg', 243, [
   dict(lines=(2, 8), orange=[(7, 2, 12), (8, 0, 5)], blue=[(2, 0, 10), (3, 0, 3), (5, 5, 13), (6, 0, 11)])]),
]
def union(ws): return (min(w['l'] for w in ws), min(w['tp'] for w in ws), max(w['r'] for w in ws), max(w['b'] for w in ws))
def build(job, man):
    id_, xml, jpg, n, segs = job
    W, H, lines = page_words(R3 + xml, n)
    base = Image.open(R3 + jpg).convert('RGB'); assert base.size == (W, H), (base.size, W, H)
    out = []
    for si, sg in enumerate(segs, 1):
        mask = Image.new('RGB', base.size, (255, 255, 255)); d = ImageDraw.Draw(mask)
        l0, l1 = sg['lines']
        padv = 6
        for li in range(l0, l1 + 1):
            x0, y0, x1, y1 = union(lines[li]); d.rectangle((x0 - 6, y0 - padv, x1 + 6, y1 + padv), fill=YEL)
        for col, key in ((ORA, 'orange'), (BLU, 'blue')):
            for li, a, b in sg[key]:
                x0, y0, x1, y1 = union(lines[li][a:b + 1]); d.rectangle((x0 - 4, y0 - padv, x1 + 4, y1 + padv), fill=col)
        im = ImageChops.multiply(base, mask)
        xs = [union(lines[li]) for li in range(l0, l1 + 1)]
        box = (max(0, min(x[0] for x in xs) - 40), max(0, min(x[1] for x in xs) - 14), min(W, max(x[2] for x in xs) + 40), min(H, max(x[3] for x in xs) + 14))
        fn = f'rawt/{id_}_seg{si}.png'; im.crop(box).save(fn); out.append(fn)
    man[id_] = {'segs': out, 'title': None, 'errors': []}
if __name__ == '__main__':
    man = json.load(open('rawt/manifest.json'))
    for j in JOBS: build(j, man)
    json.dump(man, open('rawt/manifest.json', 'w'), ensure_ascii=False, indent=1)
    print('ok', [j[0] for j in JOBS])
