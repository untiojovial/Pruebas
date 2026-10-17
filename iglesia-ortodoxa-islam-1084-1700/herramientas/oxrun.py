# -*- coding: utf-8 -*-
import sys, os, json
OX = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ox'
sys.path.insert(0, OX)
from PIL import Image
import oxpad
from oxfigs import FIGS
os.chdir(OX)
CRED = json.load(open('credits.json', encoding='utf-8')) if os.path.exists('credits.json') else {}
os.makedirs('IMG/small', exist_ok=True)
for f in FIGS:
    src = f['img']; dst = f'IMG/small/{f["slug"]}.jpg'
    if os.path.exists(src) and os.path.getsize(src) > 5000:
        im = Image.open(src).convert('RGB')
        cr = CRED.get(f['slug'], {}).get('crop')
        if cr: im = im.crop(tuple(cr))
        im.thumbnail((1100, 1100)); im.save(dst, quality=90)
    else:
        Image.new('RGB', (400, 480), '#c9d1e0').save(dst); print('SIN IMAGEN', f['id'])
    f['img'] = dst
    c = CRED.get(f['slug'], {})
    f['credit'] = c.get('credit', 'Imagen pendiente de crédito.')
    f['img_note'] = c.get('note', '')
    if c.get('pos'): f['pos'] = c['pos']
oxpad.run(FIGS)
import oxstatic
