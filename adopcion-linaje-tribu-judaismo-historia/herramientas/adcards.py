# -*- coding: utf-8 -*-
# Generador de diapositivas del pack «Adopción, linaje y tribu»: por cada prueba, AD<nn>_or (texto original) y AD<nn>_es (traducción y qué demuestra)
import sys, os, re, html
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb')
import hbcss
from hbcss import E, marks, page

AD = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ad'
OUT = 'adcards'
PACK = 'Pack «Adopción, linaje y tribu: lo que dicen el judaísmo y la historia»'
TAGNAME = {'A': 'Adopción y herencia tribal', 'B': 'Principio rabínico', 'C': 'Incorporación a una tribu o linaje', 'E': 'Levirato y filiación legal', 'G': 'Historia: derecho antiguo', 'J': 'Jesús, José y David'}
SCOPE = {'DIRECT': 'Texto directo', 'ANALOGY': 'Institución análoga', 'BACKGROUND': 'Contexto histórico'}
LANG = {'he': 'Hebreo / arameo', 'arc': 'Arameo', 'el': 'Griego', 'la': 'Latín', 'en': 'Traducción inglesa de dominio público (texto base)'}
hbcss.CSS += """
.tgA{background:#ffe8b0;color:#14213d}.tgB{background:#e3d4f7;color:#14213d}.tgC{background:#cdeedd;color:#14213d}.tgE{background:#cfe3f7;color:#14213d}.tgG{background:#e9e1cf;color:#14213d}.tgJ{background:#f9d5d9;color:#14213d}
.sc{display:inline-block;border:1.5px solid #14213d;border-radius:999px;padding:1px 10px;font-weight:700;font-size:13px;margin-left:4px;color:#14213d;background:#fff}
.src{border:1px solid #d6dbe4;border-radius:10px;background:#fbfaf6;padding:6px 6px 14px}
.src .lab{font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;color:#566079;font-weight:700;padding:6px 16px}
.txt{padding:14px 26px;background:#fff8d6;border-radius:8px;margin:0 8px;border-left:6px solid #f2c94c}
.txt.he{direction:rtl;text-align:right;font-family:'FreeSerif','DejaVu Serif',serif;font-size:31px;line-height:1.95;color:#14213d}
.txt.el{font-family:'FreeSerif','DejaVu Serif',serif;font-size:27px;line-height:1.7;color:#14213d}
.txt.la,.txt.en{font-family:'Bitstream Charter','DejaVu Serif',serif;font-size:25px;line-height:1.6;color:#14213d}
.txt mark.k{background:none;border-bottom:4px solid #fca311;background:rgba(252,163,17,.28);padding:0 2px;border-radius:2px}
.refl{padding:10px 16px 0;font-size:16px;color:#2f3a52;line-height:1.5}
.refl b{color:#14213d}
.trad{font-family:'Bitstream Charter','DejaVu Serif',serif;font-size:25px;line-height:1.62;color:#14213d;background:#fff8d6;border-left:6px solid #f2c94c;border-radius:0 8px 8px 0;padding:16px 24px;margin-bottom:14px}
.trad mark.k{background:rgba(252,163,17,.28);border-bottom:4px solid #fca311;padding:0 2px;border-radius:2px}
.dem{border-left:6px solid #2a9d8f;background:#f1faf8;border-radius:0 8px 8px 0;padding:12px 20px;font-size:20px;line-height:1.55;margin-bottom:14px}
.dem b.h{display:block;color:#2a6f67;font-size:13px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:3px}
table.m{width:100%;border-collapse:collapse;font-size:15.5px;line-height:1.4}
table.m td{border-top:1px solid #e3e7ee;padding:5px 8px;vertical-align:top}
table.m td:first-child{width:150px;font-size:12.5px;text-transform:uppercase;letter-spacing:.05em;color:#3b4660;font-weight:700}
"""
def chips(c):
    t = ''.join(f'<span class="tg tg{x}">{E(TAGNAME[x])}</span>' for x in c['tags'])
    return t + f'<span class="sc">{E(SCOPE[c["scope"]])}</span>'
def card_or(c):
    lang = c['lang']; cls = 'he' if lang in ('he', 'arc') else lang
    body = f'''<div style="margin-bottom:10px">{chips(c)}</div>
<div class="src"><div class="lab">{"Texto original · " if lang != "en" else ""}{E(LANG[lang])} · {E(c["ref"])}</div>
<div class="txt {cls}">{marks(c["orig"])}</div>
<div class="refl"><b>Obra:</b> {E(c["work"])} · <b>Autor:</b> {E(c["author"])} · <b>Fecha:</b> {E(c["date"])}<br><b>Edición:</b> {E(c["edition"])}<br><b>Fuente leída:</b> <span style="word-break:break-all">{E(c["orig_url"])}</span></div></div>'''
    page(OUT, f'{c["id"]}_or', c['id'], 'Prueba · texto original', 'Original', c['title'], c['ref'], body,
         f'{E(c["licence"])}<br>{PACK}', kind_cls='or', head_cls='alt')
def card_es(c):
    body = f'''<div style="margin-bottom:10px">{chips(c)}</div>
<div class="trad">{marks(c["es"])}</div>
<div class="dem"><b class="h">Qué demuestra</b>{marks(c["shows"])}</div>
<table class="m"><tr><td>Obra</td><td>{E(c["work"])} ({E(c["author"])}, {E(c["date"])})</td></tr>
<tr><td>Referencia</td><td>{E(c["ref"])}</td></tr>
<tr><td>Texto de partida</td><td>{E(c["base"])}</td></tr>
<tr><td>Fuente</td><td style="word-break:break-all">{E(c["url"])}</td></tr></table>'''
    page(OUT, f'{c["id"]}_es', c['id'], 'Prueba · traducción al español', 'Español', c['title'], c['ref'], body,
         f'Traducción al español mía a partir del texto indicado. {E(c["licence"])}<br>{PACK}', kind_cls='es', head_cls='alt')
def run(CARDS):
    os.makedirs(OUT, exist_ok=True)
    for c in CARDS:
        card_or(c); card_es(c)
    print('tarjetas', len(CARDS))
