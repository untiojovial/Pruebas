# -*- coding: utf-8 -*-
# Dos diapositivas por figura: <id>_cita (citas en español) y <id>_info (imagen o portada, obra, texto original, aclaración).
import sys, os, re, html
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb')
import hbcss
from hbcss import E, marks, page
import genpad
OUT = 'aycards'
PACK = 'Pack «Las críticas históricas al matrimonio de Mahoma con Aisha por su edad: de las fuentes más tempranas a 1700»'
hbcss.TAGNAME.update({'E': 'Edad de Aisha', 'L': 'Esposas y lujuria', 'N': 'Aisha nombrada', 'M': 'Musulmana'})
hbcss.CSS += """
.tgE{background:#f9d5d9;color:#14213d}.tgL{background:#ffe8b0;color:#14213d}.tgN{background:#d9ecdf;color:#14213d}.tgM{background:#cfe3f7;color:#14213d}
.work td.ar{font-family:'Amiri','Noto Naskh Arabic',serif;direction:rtl;text-align:right;font-size:22px;line-height:1.85;color:#14213d;background:#fbfaf5}
.work td.or2{font-family:'Bitstream Charter','DejaVu Serif',serif;font-size:16px;line-height:1.5;color:#2f3a52;background:#fbfaf5}
.bk{border:1px solid #cfd6e2;border-radius:12px;background:linear-gradient(160deg,#14213d,#26365c);color:#f4efe2;padding:26px 22px 20px;box-shadow:0 6px 22px rgba(20,33,61,.18);text-align:center}
.bk .a{font-family:'Amiri','Noto Naskh Arabic',serif;font-size:34px;line-height:1.7;direction:rtl;color:#ffe3a1;margin:4px 0 8px}
.bk .l{font-family:'Inter',sans-serif;font-size:15px;color:#d7c9a3;letter-spacing:.02em;line-height:1.4;margin-bottom:12px}
.bk .e{font-family:'Inter',sans-serif;font-size:12.5px;color:#aab6d6;line-height:1.45;border-top:1px solid rgba(215,201,163,.3);padding-top:10px;margin-top:10px}
.bk hr{border:0;border-top:1px solid rgba(215,201,163,.3);margin:16px 0}
.fig .ph.pg{height:auto;background:#f3efe3}
.fig .ph.pg img{height:auto;object-fit:contain;display:block}
"""
tags = hbcss.tags
def cita_slide(f):
    qs = ''
    for q in f['quotes']:
        if not q.get('es'): continue
        qs += f'<div class="qq"><div class="n"><span class="chips">{tags(q["theme"])}</span></div><blockquote>{marks(q["es"])}</blockquote></div>'
    h = f'''<!doctype html><html><head><meta charset="utf-8"><style>{hbcss.CSS}{genpad.CQ}</style></head><body><div class="qs">
<div class="top"><div class="who"><b>{f["id"]}</b>{E(f["name"])}<i>{E(f["dates"])}</i></div></div>
<div class="mid">{qs}</div>
<div class="ft2"><span>{E(f.get("citafoot", "Cita traducida al español por mí (fuente y aclaración en la diapositiva siguiente)"))}</span><span>{E(f["id"])} · 1/2</span></div></div></body></html>'''
    open(f'{OUT}/{f["id"]}_cita.html', 'w', encoding='utf-8').write(h)
def info_slide(f):
    works = ''
    for q in f['quotes']:
        if q.get('ar'):
            orig = f'<tr><td>Original árabe</td><td class="ar">{E(q["ar"])}</td></tr>'
        elif q.get('orig'):
            orig = f'<tr><td>Original</td><td class="or2">{E(q["orig"])}</td></tr>'
        else: orig = ''
        works += f'''<div class="work"><div class="wt">{tags(q["theme"])} {E(q["work"])}</div><table>
<tr><td>Fecha y lengua</td><td>{E(q["date"])}</td></tr>
<tr><td>Referencia</td><td>{E(q["ref"])}</td></tr>
<tr><td>Texto de partida</td><td>{E(q["trans"])}{(" · <span style='word-break:break-all'>" + E(q["url"]) + "</span>") if q.get("url") else ""}</td></tr>{orig}</table>
<div class="cl"><b>Aclaración de la cita</b>{marks(q["clar"])}</div></div>'''
    if f.get('imgs'):
        ph = ''.join(f'<div class="ph pg" style="margin-bottom:10px"><img src="img/{i}"></div>' for i in f['imgs'])
        fig = f'<div class="fig">{ph}<div class="cap">{E(f["credit"])}<br><i>{E(f.get("img_note", ""))}</i></div></div>'
    else:
        bk = ''
        for i, w in enumerate(f['works']):
            if i: bk += '<hr>'
            bk += f'<div class="a">{E(w["ar"])}</div><div class="l">{E(w["lat"])}</div><div class="e">{E(w["ed"])}</div>'
        fig = f'<div class="fig"><div class="bk">{bk}</div><div class="cap">{E(f.get("credit", ""))}</div></div>'
    h = f'''<!doctype html><html><head><meta charset="utf-8"><style>{hbcss.CSS}{genpad.CQ}</style></head><body><div class="card">
<div class="hd alt"><div class="row"><div class="badge"><b>{f["id"]}</b>{E(f["block"])} · obra e información</div><span class="kind">{f["id"]} · 2/2</span></div>
<h1>{E(f["name"])}: la obra, la fuente y qué quiere decir la cita</h1>
<div class="ref">{E(f["role"])}</div></div>
<div class="bd"><div class="info">{fig}
<div class="rt"><div class="nm">{E(f["name"])}<span>{E(f["why"])}</span></div><div style="height:14px"></div>{works}</div></div></div>
<div class="ft"><div class="u">{E(f["foot"])}<br>{PACK}</div></div></div></body></html>'''
    open(f'{OUT}/{f["id"]}_info.html', 'w', encoding='utf-8').write(h)
def run(FIGS):
    os.makedirs(OUT + '/img', exist_ok=True)
    for f in FIGS:
        cita_slide(f); info_slide(f)
    print('figuras ok', len(FIGS))
