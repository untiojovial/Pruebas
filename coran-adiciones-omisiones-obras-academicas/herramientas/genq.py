import sys as _s; _s.path.insert(0, ".")
# -*- coding: utf-8 -*-
# Generador de diapositivas del pack QC (adiciones / interpolaciones / supresiones en el Corán, según obras académicas).
# Por obra, tres láminas: <id>_or (texto original: captura subrayada o transcripción), <id>_es (traducción al español), <id>_pt (portada).
# Uso: CARDMOD=qccards_data CARDVAR=QCCARDS CARDOUT=qccards python3 genq.py [ids]
import json, re, html, os, sys, importlib
from PIL import Image, ImageChops
MOD = os.environ.get('CARDMOD', 'qccards_data'); VAR = os.environ.get('CARDVAR', 'QCCARDS'); OUT = os.environ.get('CARDOUT', 'qccards')
CARDS = getattr(importlib.import_module(MOD), VAR)
ONLY = sys.argv[1:]
os.makedirs(OUT, exist_ok=True)
src = open('genv.py', encoding='utf-8').read()
CSS = re.search(r'CSS = """(.*?)"""', src, re.S).group(1)
CSS += """
.tx{background:#fbfaf6;border:1px solid #d6dbe4;border-radius:8px;padding:24px 30px;font-family:'DejaVu Serif',Georgia,serif;font-size:22px;line-height:1.7;color:#1b2333}
.tx.rtl{direction:rtl;font-family:'Amiri',serif;font-size:30px;line-height:2.1}
.tx p+p{margin-top:12px}
.txn{margin:8px 0 14px;font-size:15px;color:#566079}
.cv{display:flex;gap:36px;align-items:flex-start}
.cv img{display:block;max-width:560px;max-height:820px;border:1px solid #cfd6e2;box-shadow:0 4px 18px rgba(20,33,61,.18);border-radius:3px}
.bib{flex:1;font-size:20px;line-height:1.5}
.bib table{width:100%;border-collapse:collapse}
.bib td{border-top:1px solid #e3e7ee;padding:8px 10px;vertical-align:top}
.bib td:first-child{width:150px;font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:#3b4660;font-weight:700}
.stance{display:inline-block;margin-top:10px;background:#eef1f8;border-radius:6px;padding:3px 10px;font-size:16px;color:#14213d;font-weight:600}
"""
man = json.load(open('rawt/manifest.json'))
ESC = lambda s: html.escape(s, quote=False)
AR = re.compile(r'([؀-ۿﭐ-ﷹﹰ-﻿][؀-ۿﭐ-ﷹﹰ-﻿ ]*)')

def marks(s, ar=True):
    s = ESC(s).replace('&lt;br&gt;', '<br>')
    s = re.sub(r'\[\[k:(.+?)\]\]', r'<mark class="k">\1</mark>', s)
    s = re.sub(r'\[\[a:(.+?)\]\]', r'<mark class="a">\1</mark>', s)
    if ar: s = AR.sub(r'<bdi dir="rtl" lang="ar">\1</bdi>', s)
    return s

def legend(has_alt, es=False, orig=True):
    items = []
    if not es and orig: items.append('<span><i style="background:#fff0a0"></i>pasaje citado</span>')
    items.append('<span><i style="background:#ffb000"></i>frase clave</span>')
    if has_alt: items.append('<span><i style="background:#9fd3f5"></i>matiz / en contra</span>')
    return '<div class="lg">' + ''.join(items) + '</div>'

def header(c, kind):
    k = {'or': f'<span class="kind">Texto original · {ESC(c.get("lang_name", ""))}</span>', 'es': '<span class="kind es">Traducción al español</span>', 'pt': '<span class="kind">Portada de la obra</span>'}[kind]
    sec = ' <span class="sec">transcripción</span>' if (kind == 'or' and c.get('transcript')) else ''
    ref = c['ref_pt'] if kind == 'pt' else c['ref']
    return f'''<div class="hd"><div class="row"><div class="badge"><b>{c["id"]}</b>{ESC(c["tag"])}{sec}</div>{k}</div>
<h1>{ESC(c["title"])}</h1>
<div class="row"><div class="ref">{ESC(ref)}</div><div class="arref">{c.get("orig_ref", "")}</div></div></div>'''

def footer(c, has_alt, kind):
    note = c.get('trnote', 'Traducción literal propia; entre corchetes, aclaraciones. ') if kind == 'es' else ''
    acc = c.get('acceso', '')
    return f'''<div class="ft"><div class="u">{note}{ESC(acc)}<br>{ESC(c["url"])}<br>{ESC(c.get("uso", ""))}</div>{legend(has_alt, kind == 'es', kind == 'or') if kind != 'pt' else ''}</div>'''

def page(c, kind, body, has_alt):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="card">{header(c, kind)}<div class="bd">{body}</div>{footer(c, has_alt, kind)}</div></body></html>'

def nsegs(c):
    return len(c['transcript']) if c.get('transcript') else sum(len(man[s]['segs']) for s in c['specs'])

for c in CARDS:
    if ONLY and c['id'] not in ONLY: continue
    n = nsegs(c)
    G = c.get('groups') or [1] * n
    assert sum(G) == n and len(c['es']) == len(G), (c['id'], len(c['es']), n, G)
    has_alt = '[[a:' in ''.join(c['es'])
    # ---- 1) original
    parts = []
    if c.get('transcript'):
        rtl = c.get('rtl', False)
        for i, t in enumerate(c['transcript']):
            if i: parts.append('<div class="gap">[ … ]</div>')
            paras = ''.join(f'<p>{marks(p, ar=rtl)}</p>' for p in t.split('\n'))
            parts.append(f'<div class="tx{" rtl" if rtl else ""}">{paras}</div>')
        parts.append(f'<div class="txn">{ESC(c.get("tx_note", "Transcripción literal de la obra (no hay copia digital abierta de la que capturar la imagen); la referencia exacta está arriba."))}</div>')
    else:
        segs = sum((man[s]['segs'] for s in c['specs']), [])
        k = 0
        for gi, g in enumerate(G):
            if gi: parts.append('<div class="gap">[ … ]</div>')
            for j in range(g):
                f = segs[k]; k += 1
                if j: parts.append('<div class="gap" style="font-size:14px;margin:2px 0">↓ el pasaje continúa en la otra columna</div>')
                wpx = Image.open(f).width
                wcss = min(1216, max(int(wpx / c.get('scale', 2) * 1.6), c.get('minw', 0))) if c.get('scale', 2) else 1216
                parts.append(f'<div class="seg" style="max-width:{wcss + 2}px;margin:0 auto"><img src="../{f}"></div>')
    open(f'{OUT}/{c["id"]}_or.html', 'w').write(page(c, 'or', ''.join(parts), has_alt or bool(c.get('has_alt'))))
    # ---- 2) español
    segs = '<div class="gap">[ … ]</div>'.join(f'<div class="tr"><p>{marks(s)}</p></div>' for s in c['es'])
    st = f'<div class="stance">{ESC(c["stance"])}</div>' if c.get('stance') else ''
    boxes = f'<div class="box"><h3>Qué dice el autor</h3>{marks(c["prueba"])}{st}</div>'
    if c.get('ojo'): boxes += f'<div class="box ojo"><h3>Ojo</h3>{marks(c["ojo"])}</div>'
    open(f'{OUT}/{c["id"]}_es.html', 'w').write(page(c, 'es', segs + boxes, has_alt))
    # ---- 3) portada
    cov = c.get('cover')
    if cov and os.path.exists(cov):
        dst = f'{OUT}/{c["id"]}_cover' + os.path.splitext(cov)[1]
        Image.open(cov).convert('RGB').save(dst.rsplit('.', 1)[0] + '.png')
        img = f'<img src="{c["id"]}_cover.png">'
    else:
        img = f'<div class="tx" style="width:420px;text-align:center;font-size:20px">{ESC(c.get("cover_note", "[no se encontró imagen de portada]"))}</div>'
    B = c['biblio']
    rows = ''.join(f'<tr><td>{ESC(k)}</td><td>{ESC(v)}</td></tr>' for k, v in B if v)
    cvb = f'<div class="cv">{img}<div class="bib"><table>{rows}</table></div></div>'
    open(f'{OUT}/{c["id"]}_pt.html', 'w').write(page(c, 'pt', cvb, False))
print('ok', len([c for c in CARDS if not ONLY or c['id'] in ONLY]))
