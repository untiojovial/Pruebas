# -*- coding: utf-8 -*-
import json, re, html, os, glob
from PIL import Image, ImageChops
import importlib, os as _os
MOD=_os.environ.get('CARDMOD','vcards_data'); VAR=_os.environ.get('CARDVAR','VCARDS'); OUT=_os.environ.get('CARDOUT','vcards')
CARDS=getattr(importlib.import_module(MOD),VAR)
import sys
ONLY=sys.argv[1:]
specs = {}
man = {}
for sf, mf in [('specs.json','raw/manifest.json'),('hspecs.json','rawh/manifest.json'),('vspecs.json','rawv/manifest.json'),('zspecs.json','rawz/manifest.json'),('v1specs.json','rawv/manifest.json'),('kspecs.json','rawv/manifest.json'),('mspecs.json','rawm/manifest.json')]:
    if os.path.exists(sf): specs.update({s['id']: s for s in json.load(open(sf))})
    if os.path.exists(mf): man.update(json.load(open(mf)))

def trim(src, dst, pad=12):
    im = Image.open(src).convert('RGB')
    bg = Image.new('RGB', im.size, (255, 255, 255))
    diff = ImageChops.difference(im, bg).convert('L').point(lambda p: 255 if p > 18 else 0)
    bb = diff.getbbox()
    if bb:
        im = im.crop((max(0, bb[0]-pad), max(0, bb[1]-pad), min(im.width, bb[2]+pad), min(im.height, bb[3]+pad)))
    im.save(dst)
    return im.size

def marks(s):
    s = html.escape(s, quote=False).replace('&lt;br&gt;', '<br>')
    s = re.sub(r'\[\[k:(.+?)\]\]', r'<mark class="k">\1</mark>', s)
    s = re.sub(r'\[\[a:(.+?)\]\]', r'<mark class="a">\1</mark>', s)
    s = re.sub(r'([\u0600-\u06FF\uFB50-\uFDF9\uFE70-\uFEFF][\u0600-\u06FF\uFB50-\uFDF9\uFE70-\uFEFF ]*)', r'<bdi dir="rtl" lang="ar">\1</bdi>', s)
    return s

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#dfe4ec;font-family:'Inter',sans-serif;color:#1b2333;-webkit-font-smoothing:antialiased}
.card{width:1280px;background:#fff;margin:0 auto}
.hd{background:#14213d;color:#fff;padding:22px 32px 20px}
.row{display:flex;justify-content:space-between;align-items:center;gap:20px}
.badge{display:inline-flex;gap:10px;align-items:center;font-size:15px;letter-spacing:.06em;text-transform:uppercase;color:#b9c6e4;font-weight:600}
.sec{background:#e76f51;color:#fff;padding:2px 8px;border-radius:5px;letter-spacing:.02em;text-transform:none}
.pos{display:inline-block;margin-top:8px;background:#26365c;color:#ffd77a;padding:3px 10px;border-radius:6px;font-size:16px}
.badge b{background:#fca311;color:#14213d;padding:3px 10px;border-radius:6px;letter-spacing:.02em}
.kind{font-size:15px;font-weight:700;color:#14213d;background:#e5ecf8;padding:4px 12px;border-radius:999px}
.kind.es{background:#fca311}
h1{font-size:30px;line-height:1.25;font-weight:750;margin:14px 0 10px}
.ref{font-size:18px;color:#d5dcec}
.arref{font-family:'Amiri',serif;font-size:27px;direction:rtl;color:#fff;white-space:nowrap}
.bd{padding:26px 32px 18px}
.strip{display:flex;justify-content:flex-end;margin-bottom:14px}
.strip img{max-height:86px;border:1px solid #e3e7ee;border-radius:6px}
.seg{border:1px solid #d6dbe4;border-radius:8px;overflow:hidden;background:#fff}
.seg img{display:block;width:100%}
.gap{text-align:center;color:#8a93a6;font-size:22px;margin:8px 0;letter-spacing:.2em}
.tr{background:#fff8d6;border-radius:8px;padding:22px 26px;font-size:22px;line-height:1.62}
.tr p+p{margin-top:12px}
mark{border-radius:4px;padding:1px 3px;color:#111;-webkit-box-decoration-break:clone;box-decoration-break:clone}
mark.k{background:#ffb000}
mark.a{background:#9fd3f5}
bdi[lang=ar]{font-family:'Amiri',serif;font-size:1.12em}
.box{margin-top:18px;border-left:6px solid #2a9d8f;background:#eef8f6;padding:14px 20px;border-radius:0 8px 8px 0;font-size:19px;line-height:1.5}
.box.ojo{border-color:#e76f51;background:#fdf1ec}
.box h3{font-size:14px;text-transform:uppercase;letter-spacing:.08em;margin-bottom:4px;color:#2a6f67}
.box.ojo h3{color:#b44a2f}
.ft{padding:14px 32px 20px;border-top:1px solid #e6e9ef;font-size:15px;color:#566079;display:flex;justify-content:space-between;gap:24px;align-items:flex-start}
.ft .u{max-width:900px;overflow-wrap:anywhere}
.lg{display:flex;gap:12px;flex-wrap:wrap;justify-content:flex-end;white-space:nowrap}
.lg span{display:inline-flex;align-items:center;gap:6px}
.lg i{display:inline-block;width:18px;height:14px;border-radius:3px}
"""

def legend(has_alt, es=False):
    items = []
    if not es: items.append('<span><i style="background:#fff0a0"></i>pasaje citado</span>')
    items.append('<span><i style="background:#ffb000"></i>frase clave</span>')
    if has_alt: items.append('<span><i style="background:#9fd3f5"></i>matiz / en contra</span>')
    return '<div class="lg">' + ''.join(items) + '</div>'

def header(c, kind):
    k = '<span class="kind es">Traducción al español</span>' if kind == 'es' else f'<span class="kind">Texto original en {c.get("lang","árabe")}</span>'
    sec = ' <span class="sec">fuente secundaria</span>' if c.get('secondary') else ''
    return f'''<div class="hd"><div class="row"><div class="badge"><b>{c["id"]}</b>{html.escape(c.get("tag") or (c["year"] + " · " + c["who"]) if c.get("year") else c.get("tag",""))}{sec}</div>{k}</div>
<h1>{html.escape(c["title"])}</h1>
<div class="row"><div class="ref">{html.escape(c["ref"])}{('<br><span class="pos">' + html.escape(c['chip']) + '</span>') if c.get('chip') else ''}</div><div class="arref">{c["ar_ref"]}</div></div></div>'''

def footer(c, has_alt, es=False):
    note = 'Traducción literal propia; entre corchetes, aclaraciones. ' if es else ''
    return f'''<div class="ft"><div class="u">{note}Fuente: {html.escape(c["site"])}<br>{html.escape(c["url"])}<br>{html.escape(c.get('uso',''))}</div>{legend(has_alt, es)}</div>'''

for c in CARDS:
    if ONLY and c['id'] not in ONLY: continue
    sids = c.get('specs', [c['id']])
    if any(s not in man for s in sids): print('missing capture', c['id']); continue
    m = {'segs': sum((man[s]['segs'] for s in sids), []), 'title': man[sids[0]].get('title')}
    sp = {'segments': sum((specs[s]['segments'] for s in sids if s in specs), [])}
    assert len(c['es']) == len(m['segs']), (c['id'], len(c['es']), len(m['segs']))
    has_alt = any(s.get('alts') for s in sp['segments']) or '[[a:' in ''.join(c['es'])
    # Arabic card
    parts = []
    if m.get('title'):
        t = f'{OUT}/{c["id"]}_strip.png'; trim(m['title'], t)
        parts.append(f'<div class="strip"><img src="{os.path.basename(t)}"></div>')
    for i, f in enumerate(m['segs']):
        if i: parts.append('<div class="gap">[ … ]</div>')
        wpx = Image.open(f).width
        wcss = min(1216, int(wpx / 2 * 1.6))
        parts.append(f'<div class="seg" style="max-width:{wcss+2}px;margin:0 auto"><img src="../{f}"></div>')
    ar = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="card">{header(c,"ar")}<div class="bd">{"".join(parts)}</div>{footer(c,has_alt)}</div></body></html>'
    open(f'{OUT}/{c["id"]}_ar.html', 'w').write(ar)
    # Spanish card
    segs = '<div class="gap">[ … ]</div>'.join(f'<div class="tr"><p>{marks(s)}</p></div>' for s in c['es'])
    boxes = f'<div class="box"><h3>Qué demuestra</h3>{marks(c["prueba"])}</div>'
    if c.get('ojo'): boxes += f'<div class="box ojo"><h3>Ojo</h3>{marks(c["ojo"])}</div>'
    es = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="card">{header(c,"es")}<div class="bd">{segs}{boxes}</div>{footer(c,has_alt,True)}</div></body></html>'
    open(f'{OUT}/{c["id"]}_es.html', 'w').write(es)
print('ok', len(CARDS))
