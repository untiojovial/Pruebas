# -*- coding: utf-8 -*-
# Dos diapositivas por tema: <id>_cita (citas en español) y <id>_info (obra, texto árabe, aclaración y contraste con fuentes cristianas).
import sys, os, re, html
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb')
import hbcss
from hbcss import E, marks, page
import genpad
OUT = 'itcards'
PACK = 'Pack «Ibn Taymiyya: tawhid, epistemología, tawatur y su refutación de los cristianos»'
hbcss.TAGNAME.update({'T': 'Tawhid', 'E': 'Epistemología', 'W': 'Tawatur', 'C': 'Cristianos'})
hbcss.CSS += """
.tgT{background:#d9ecdf;color:#14213d}.tgE{background:#e4dcf5;color:#14213d}.tgW{background:#ffe8b0;color:#14213d}.tgC{background:#f9d5d9;color:#14213d}
.vd{display:inline-block;font-family:'Inter',sans-serif;font-size:13px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;padding:3px 10px;border-radius:6px}
.vd.fiel{background:#2a9d8f;color:#fff}.vd.parcial{background:#f4b942;color:#14213d}.vd.paja{background:#d64550;color:#fff}.vd.algunos{background:#4f7cc9;color:#fff}.vd.nov{background:#8a93a8;color:#fff}.vd.valido{background:#2a9d8f;color:#fff}.vd.debil{background:#d64550;color:#fff}
.work td.ar{font-family:'Amiri','Noto Naskh Arabic',serif;direction:rtl;text-align:right;font-size:22px;line-height:1.85;color:#14213d;background:#fbfaf5}
.work .ct{padding:8px 14px 10px;font-size:16px;line-height:1.5;background:#f1f5fc;border-top:3px solid #4f7cc9}
.work .ct b{color:#2e5aa3;font-size:12.5px;letter-spacing:.07em;text-transform:uppercase;display:block;margin-bottom:2px}
.work .ct mark{background:none;color:#14213d;text-decoration:underline;text-decoration-color:#4f7cc9;text-decoration-thickness:3px;text-underline-offset:4px;padding:0;font-weight:600}
.work .vv mark{background:none;color:#14213d;text-decoration:underline;text-decoration-color:#e76f51;text-decoration-thickness:3px;text-underline-offset:4px;padding:0;font-weight:600}
.work .ct q{font-family:'Bitstream Charter','DejaVu Serif',serif;font-style:italic;quotes:'«' '»';color:#26334f}
.work .vv{padding:8px 14px 10px;font-size:17px;line-height:1.5;background:#fff7f1;border-top:3px solid #e76f51}
.work .vv b.h{font-size:12.5px;letter-spacing:.07em;text-transform:uppercase;display:block;margin-bottom:4px;color:#b44a2f}
.bk{border:1px solid #cfd6e2;border-radius:12px;background:linear-gradient(160deg,#14213d,#26365c);color:#f4efe2;padding:26px 22px 20px;box-shadow:0 6px 22px rgba(20,33,61,.18);text-align:center}
.bk .a{font-family:'Amiri','Noto Naskh Arabic',serif;font-size:34px;line-height:1.7;direction:rtl;color:#ffe3a1;margin:4px 0 8px}
.bk .l{font-family:'Inter',sans-serif;font-size:15px;color:#d7c9a3;letter-spacing:.02em;line-height:1.4;margin-bottom:12px}
.bk .e{font-family:'Inter',sans-serif;font-size:12.5px;color:#aab6d6;line-height:1.45;border-top:1px solid rgba(215,201,163,.3);padding-top:10px;margin-top:10px}
.bk hr{border:0;border-top:1px solid rgba(215,201,163,.3);margin:16px 0}
"""
tags = hbcss.tags
VERD = {'fiel': 'Fiel a sus fuentes cristianas', 'parcial': 'Parcialmente fiel', 'paja': 'Hombre de paja', 'algunos': 'Acierta contra algunos cristianos, no contra todos', 'nov': 'No verificable', 'valido': 'Argumento coherente', 'debil': 'Argumento débil o inconsistente'}
def vd(k): return f'<span class="vd {k}">{E(VERD[k])}</span>' if k else ''
def cita_slide(f):
    qs = ''
    for q in f['quotes']:
        qs += f'<div class="qq"><div class="n"><span class="chips">{tags(q["theme"])}{(" " + vd(q.get("verdict"))) if q.get("verdict") else ""}</span></div><blockquote>{marks(q["es"])}</blockquote></div>'
    h = f'''<!doctype html><html><head><meta charset="utf-8"><style>{hbcss.CSS}{genpad.CQ}</style></head><body><div class="qs">
<div class="top"><div class="who"><b>{f["id"]}</b>{E(f["name"])}<i>{E(f["dates"])}</i></div></div>
<div class="mid">{qs}</div>
<div class="ft2"><span>Cita traducida al español por mí (fuente, texto árabe y aclaración en la diapositiva siguiente)</span><span>{E(f["id"])} · 1/2</span></div></div></body></html>'''
    open(f'{OUT}/{f["id"]}_cita.html', 'w', encoding='utf-8').write(h)
def info_slide(f):
    works = ''
    for q in f['quotes']:
        ar = f'<tr><td>Original árabe</td><td class="ar">{E(q["ar"])}</td></tr>' if q.get('ar') else ''
        ct = ''
        if q.get('christian'):
            c = q['christian']
            og = f'<br><span style="font-size:14px;color:#3b4a6b;font-style:italic">{E(c["orig"])}</span>' if c.get('orig') else ''
            ct = f'<div class="ct"><b>{E(c.get("head", "Lo que dicen las fuentes cristianas"))}</b>{marks(c["txt"])}{og}<br><span style="font-size:13.5px;color:#4a5878">{E(c["src"])}</span></div>'
        vv = ''
        if q.get('verdict'):
            vv = f'<div class="vv"><b class="h">¿Hombre de paja?</b>{vd(q["verdict"])} {marks(q.get("vtxt", ""))}</div>'
        works += f'''<div class="work"><div class="wt">{tags(q["theme"])} {E(q["work"])}</div><table>
<tr><td>Fecha y lengua</td><td>{E(q["date"])}</td></tr>
<tr><td>Referencia</td><td>{E(q["ref"])}</td></tr>
<tr><td>Texto de partida</td><td>{E(q["trans"])} · <span style="word-break:break-all">OpenITI {E(q["url"].rsplit("/",1)[-1])}</span></td></tr>{ar}</table>
<div class="cl"><b>Aclaración de la cita</b>{marks(q["clar"])}</div>{ct}{vv}</div>'''
    bk = ''
    for i, w in enumerate(f['works']):
        if i: bk += '<hr>'
        bk += f'<div class="a">{E(w["ar"])}</div><div class="l">{E(w["lat"])}</div><div class="e">{E(w["ed"])}</div>'
    h = f'''<!doctype html><html><head><meta charset="utf-8"><style>{hbcss.CSS}{genpad.CQ}</style></head><body><div class="card">
<div class="hd alt"><div class="row"><div class="badge"><b>{f["id"]}</b>Ibn Taymiyya · {E(f["block"])} · obra e información</div><span class="kind">{f["id"]} · 2/2</span></div>
<h1>{E(f["name"])}: la obra, la fuente y qué quiere decir la cita</h1>
<div class="ref">{E(f["role"])}</div></div>
<div class="bd"><div class="info"><div class="fig"><div class="bk">{bk}</div><div class="cap">{E(f.get("cap", "Ibn Taymiyya (661–728 H / 1263–1328). No se conserva un retrato; se muestra la portada tipográfica de la obra citada."))}</div></div>
<div class="rt"><div class="nm">{E(f["name"])}<span>{E(f["why"])}</span></div><div style="height:14px"></div>{works}</div></div></div>
<div class="ft"><div class="u">{E(f["foot"])}<br>{PACK}</div></div></div></body></html>'''
    open(f'{OUT}/{f["id"]}_info.html', 'w', encoding='utf-8').write(h)
def run(FIGS):
    os.makedirs(OUT, exist_ok=True)
    for f in FIGS:
        cita_slide(f); info_slide(f)
    print('temas ok', len(FIGS))
