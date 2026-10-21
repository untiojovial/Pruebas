# -*- coding: utf-8 -*-
# Genera, por cada Padre, dos diapositivas: <id>_cita (solo la cita en español) y <id>_info (foto, obra, datos y aclaración)
import sys, os, re, shutil, html
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb')
from hbcss import *
from PIL import Image
OUT = 'hbcards'
CQ = """
body{background:#dfe4ec}
.qs{width:1280px;margin:0 auto;background:linear-gradient(165deg,#0d172d 0%,#1a2a50 62%,#22345f 100%);color:#f4efe2;padding:54px 78px 40px;position:relative;display:flex;flex-direction:column;min-height:780px}
.qs .mid{flex:1;display:flex;flex-direction:column;justify-content:center}
.qs .top{display:flex;justify-content:space-between;align-items:center;margin-bottom:34px}
.qs .who{font-family:'Inter',sans-serif;font-size:19px;letter-spacing:.09em;text-transform:uppercase;color:#d7c9a3;font-weight:600}
.qs .who b{background:#fca311;color:#14213d;padding:3px 11px;border-radius:6px;margin-right:12px;letter-spacing:.02em}
.qs .who i{font-style:normal;color:#9fb0d4;margin-left:12px;text-transform:none;letter-spacing:.02em}
.qs .chips{display:flex;gap:8px;flex-wrap:wrap}
.qs .tg{font-family:'Inter',sans-serif}
.qq{position:relative;padding:12px 0 22px 62px;margin-bottom:12px}
.qq:before{content:'«';position:absolute;left:-4px;top:-14px;font-family:'Bitstream Charter','DejaVu Serif',serif;font-size:118px;line-height:1;color:#fca311;opacity:.9}
.qq + .qq{border-top:1px solid rgba(215,201,163,.28);padding-top:30px}
.qq + .qq:before{top:10px}
.qq .n{font-family:'Inter',sans-serif;font-size:13px;letter-spacing:.14em;color:#9fb0d4;text-transform:uppercase;margin-bottom:10px;display:flex;gap:10px;align-items:center}
.qq blockquote{font-family:'Bitstream Charter','DejaVu Serif',serif;font-size:31px;line-height:1.52;color:#f8f4e8}
.qq blockquote mark{background:none;color:#ffcf6b;text-decoration:underline;text-decoration-color:rgba(252,163,17,.75);text-decoration-thickness:3px;text-underline-offset:6px;padding:0}
.qq blockquote mark.a{color:#a9d8f7;text-decoration-color:rgba(159,211,245,.7)}
.qq blockquote .ac{display:block;margin-top:12px;font-size:22px;color:#c9d3ea;font-style:italic}
.qs .ft2{margin-top:26px;font-family:'Inter',sans-serif;font-size:14px;color:#8f9dc0;display:flex;justify-content:space-between}
.fig{width:372px;flex:none}
.fig .ph{width:372px;height:470px;border-radius:12px;overflow:hidden;background:#e9edf4;border:1px solid #cfd6e2;box-shadow:0 6px 22px rgba(20,33,61,.18)}
.fig .ph img{width:100%;height:100%;object-fit:cover}
.fig .cap{font-size:13.5px;color:#566079;line-height:1.4;margin-top:8px}
.nm{font-size:29px;font-weight:750;color:#14213d;line-height:1.2}
.nm span{display:block;font-size:17px;font-weight:500;color:#566079;margin-top:4px}
.work{border:1px solid #d6dbe4;border-radius:10px;margin:0 0 12px;background:#fff;overflow:hidden}
.work .wt{background:#eef1f6;padding:8px 14px;font-weight:700;font-size:17.5px;color:#14213d;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.work table{width:100%;border-collapse:collapse;font-size:15.5px;line-height:1.4}
.work td{padding:5px 14px;vertical-align:top;border-top:1px solid #edf0f5}
.work td:first-child{width:128px;font-size:12.5px;text-transform:uppercase;letter-spacing:.05em;color:#3b4660;font-weight:700}
.work .or{font-family:'Bitstream Charter','DejaVu Serif',serif;font-style:italic;font-size:15.5px;color:#2f3a52}
.work .cl{padding:8px 14px 10px;font-size:17px;line-height:1.5;background:#f4faf8;border-top:3px solid #2a9d8f}
.work .cl b{color:#2a6f67;font-size:12.5px;letter-spacing:.07em;text-transform:uppercase;display:block;margin-bottom:2px}
.work .oj{padding:8px 14px 10px;font-size:17px;line-height:1.5;background:#fdf1ec;border-top:3px solid #e76f51}
.work .oj b{color:#b44a2f;font-size:12.5px;letter-spacing:.07em;text-transform:uppercase;display:block;margin-bottom:2px}
.info{display:flex;gap:28px;align-items:flex-start}
.info .rt{flex:1;min-width:0}
"""
def img_prep(src, dst, pos='50% 20%'):
    im = Image.open(src).convert('RGB')
    if im.width < 600:
        k = 2 if im.width >= 300 else 3
        im = im.resize((im.width * k, im.height * k), Image.LANCZOS)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    im.save(dst, quality=92)
def cita_slide(f):
    qs = ''
    for i, q in enumerate(f['quotes'], 1):
        qs += f'<div class="qq"><div class="n"><span class="chips">{tags(q["theme"])}</span></div><blockquote>{marks(q["es"])}{("<span class=ac>"+E(q["ac"])+"</span>") if q.get("ac") else ""}</blockquote></div>'
    h = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{CQ}</style></head><body><div class="qs">
<div class="top"><div class="who"><b>{f["id"]}</b>{E(f["name"])}<i>{E(f["dates"])}</i></div></div>
<div class="mid">{qs}</div>
<div class="ft2"><span>Cita traducida al español por mí (fuente y aclaración en la diapositiva siguiente)</span><span>{E(f["id"])} · 1/2</span></div></div></body></html>'''
    open(f'{OUT}/{f["id"]}_cita.html', 'w', encoding='utf-8').write(h)
def info_slide(f):
    img = f['img']; dst = f'{OUT}/img/{f["slug"]}.jpg'; img_prep(img, dst)
    works = ''
    for q in f['quotes']:
        orig = f'<tr><td>Original</td><td class="or">{E(q["orig"])}</td></tr>' if q.get('orig') else ''
        ojo = f'<div class="oj"><b>Ojo</b>{marks(q["ojo"])}</div>' if q.get('ojo') else ''
        works += f'''<div class="work"><div class="wt">{tags(q["theme"])} {E(q["work"])}</div><table>
<tr><td>Fecha y lengua</td><td>{E(q["date"])}</td></tr>
<tr><td>Referencia</td><td>{E(q["ref"])}</td></tr>
<tr><td>Texto de partida</td><td>{E(q["trans"])} · <span style="word-break:break-all">{E(q["url"])}</span></td></tr>{orig}</table>
<div class="cl"><b>Aclaración de la cita</b>{marks(q["clar"])}</div>{ojo}</div>'''
    gen = f'<div class="box ojo" style="margin-top:12px"><h3>Ojo</h3>{marks(f["ojo"])}</div>' if f.get('ojo') else ''
    h = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{CQ}</style></head><body><div class="card">
<div class="hd alt"><div class="row"><div class="badge"><b>{f["id"]}</b>Padre de la Iglesia · obra e información</div><span class="kind">{f["id"]} · 2/2</span></div>
<h1>{E(f["name"])} ({E(f["dates"])}): la obra, la fuente y qué quiere decir la cita</h1>
<div class="ref">{E(f["role"])}</div></div>
<div class="bd"><div class="info"><div class="fig"><div class="ph"><img src="img/{f["slug"]}.jpg" style="object-position:{f.get("pos","50% 20%")}"></div><div class="cap">{E(f["credit"])}<br><i>{E(f["img_note"])}</i></div></div>
<div class="rt"><div class="nm">{E(f["name"])}<span>{E(f["why"])}</span></div><div style="height:14px"></div>{works}{gen}</div></div></div>
<div class="ft"><div class="u">{E(f["foot"])}<br>{PACK}</div></div></div></body></html>'''
    open(f'{OUT}/{f["id"]}_info.html', 'w', encoding='utf-8').write(h)
def run(PADRES):
    os.makedirs(OUT + '/img', exist_ok=True)
    for f in PADRES:
        cita_slide(f); info_slide(f)
    print('padres ok', len(PADRES))
