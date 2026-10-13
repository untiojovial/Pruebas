# -*- coding: utf-8 -*-
# Dos diapositivas por figura: <id>_cita (solo la cita en español) y <id>_info (foto, obra, datos y aclaración). Sin «Ojo».
import sys, os, re, shutil, html
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb')
import hbcss
from hbcss import E, marks, page
import genpad
from PIL import Image
OUT = 'igcards'
PACK = 'Pack «La Iglesia ante el Islam, siglos VIII–XVI: lo que dijeron sus grandes autoridades»'
hbcss.TAGNAME.update({'M': 'Mahoma', 'Q': 'Corán y doctrina', 'S': 'Cómo se extendió', 'H': 'El Islam como religión'})
hbcss.CSS += """
.tgM{background:#f9d5d9;color:#14213d}.tgQ{background:#cfe3f7;color:#14213d}.tgS{background:#ffe8b0;color:#14213d}
"""
tags = hbcss.tags
def cita_slide(f):
    qs = ''
    for q in f['quotes']:
        qs += f'<div class="qq"><div class="n"><span class="chips">{tags(q["theme"])}</span></div><blockquote>{marks(q["es"])}</blockquote></div>'
    h = f'''<!doctype html><html><head><meta charset="utf-8"><style>{hbcss.CSS}{genpad.CQ}</style></head><body><div class="qs">
<div class="top"><div class="who"><b>{f["id"]}</b>{E(f["name"])}<i>{E(f["dates"])}</i></div></div>
<div class="mid">{qs}</div>
<div class="ft2"><span>Cita traducida al español por mí (fuente y aclaración en la diapositiva siguiente)</span><span>{E(f["id"])} · 1/2</span></div></div></body></html>'''
    open(f'{OUT}/{f["id"]}_cita.html', 'w', encoding='utf-8').write(h)
def info_slide(f):
    dst = f'{OUT}/img/{f["slug"]}.jpg'; genpad.img_prep(f['img'], dst)
    works = ''
    for q in f['quotes']:
        orig = f'<tr><td>Original</td><td class="or">{E(q["orig"])}</td></tr>' if q.get('orig') else ''
        works += f'''<div class="work"><div class="wt">{tags(q["theme"])} {E(q["work"])}</div><table>
<tr><td>Fecha y lengua</td><td>{E(q["date"])}</td></tr>
<tr><td>Referencia</td><td>{E(q["ref"])}</td></tr>
<tr><td>Texto de partida</td><td>{E(q["trans"])} · <span style="word-break:break-all">{E(q["url"])}</span></td></tr>{orig}</table>
<div class="cl"><b>Aclaración de la cita</b>{marks(q["clar"])}</div></div>'''
    h = f'''<!doctype html><html><head><meta charset="utf-8"><style>{hbcss.CSS}{genpad.CQ}</style></head><body><div class="card">
<div class="hd alt"><div class="row"><div class="badge"><b>{f["id"]}</b>Figura de la Iglesia · obra e información</div><span class="kind">{f["id"]} · 2/2</span></div>
<h1>{E(f["name"])} ({E(f["dates"])}): la obra, la fuente y qué quiere decir la cita</h1>
<div class="ref">{E(f["role"])}</div></div>
<div class="bd"><div class="info"><div class="fig"><div class="ph"><img src="img/{f["slug"]}.jpg" style="object-position:{f.get("pos","50% 20%")}"></div><div class="cap">{E(f["credit"])}<br><i>{E(f["img_note"])}</i></div></div>
<div class="rt"><div class="nm">{E(f["name"])}<span>{E(f["why"])}</span></div><div style="height:14px"></div>{works}</div></div></div>
<div class="ft"><div class="u">{E(f["foot"])}<br>{PACK}</div></div></div></body></html>'''
    open(f'{OUT}/{f["id"]}_info.html', 'w', encoding='utf-8').write(h)
def run(FIGS):
    os.makedirs(OUT + '/img', exist_ok=True)
    for f in FIGS:
        cita_slide(f); info_slide(f)
    print('figuras ok', len(FIGS))
