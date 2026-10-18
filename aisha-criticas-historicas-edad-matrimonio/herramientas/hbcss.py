# -*- coding: utf-8 -*-
# CSS y utilidades comunes del pack «Hebreos 10:28 y los Padres de la Iglesia»
import re, html, os
HBD = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb'
src = open('/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/caps/genv.py', encoding='utf-8').read()
BASE = re.search(r'CSS = """(.*?)"""', src, re.S).group(1)
CSS = BASE + """
.hd.alt{background:linear-gradient(120deg,#14213d,#26365c)}
h2.g{font-size:20px;margin:20px 0 9px;color:#14213d;border-bottom:2px solid #fca311;padding-bottom:3px}
p.l{font-size:19.5px;line-height:1.55;margin:6px 0}
ul.l{margin:6px 0 0 22px;font-size:19px;line-height:1.5}
ul.l li{margin:3px 0}
.ans{border-left:6px solid #14213d;background:#eef1f8;padding:16px 22px;border-radius:0 8px 8px 0;font-size:20.5px;line-height:1.55;margin-bottom:18px}
.ans b{color:#14213d}
table.v{width:100%;border-collapse:collapse;font-size:17px;line-height:1.4}
table.v th{background:#eef1f6;text-align:left;padding:8px 10px;font-size:12.5px;text-transform:uppercase;letter-spacing:.05em;color:#3b4660}
table.v td{border-top:1px solid #e3e7ee;padding:8px 10px;vertical-align:top}
.ok{color:#1d7a4f;font-weight:700}.no{color:#b44a2f;font-weight:700}.mid{color:#9a6a00;font-weight:700}
.gr{font-family:'FreeSerif','DejaVu Serif',serif;font-size:21px;line-height:1.55;color:#1b2333}
.es2{font-size:19.5px;line-height:1.55}
.two{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.pn{border:1px solid #d6dbe4;border-radius:10px;padding:14px 18px;background:#fbfaf6}
.pn h4{font-size:13px;letter-spacing:.07em;text-transform:uppercase;color:#3b4660;margin-bottom:6px}
.sy{border:1px solid #d6dbe4;border-radius:10px;margin:0 0 14px;overflow:hidden}
.sy .t{background:#14213d;color:#fff;font-weight:700;font-size:18px;padding:7px 14px;display:flex;justify-content:space-between}
.sy .t span{color:#ffd77a;font-weight:600;font-size:15px}
.sy .b{padding:10px 16px;font-size:18.5px;line-height:1.5;background:#fff}
.sy .b p{margin:4px 0}
.sy .b b.p{color:#14213d}
.sy .b .c{border-top:1px dashed #cfd6e2;margin-top:6px;padding-top:6px;font-weight:600;color:#14213d}
.sy .b .n{font-size:15.5px;color:#566079;margin-top:4px}
.vid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.vid figure{border:1px solid #d6dbe4;border-radius:8px;overflow:hidden;background:#000}
.vid img{display:block;width:100%}
.vid figcaption{background:#14213d;color:#fff;font-size:14.5px;padding:5px 10px;line-height:1.35}
.tg{display:inline-block;border-radius:999px;padding:2px 11px;font-weight:700;font-size:14px;margin-right:4px}
.tgH,.tgP{background:#cfe3f7;color:#14213d}.tgD{background:#ffe8b0;color:#14213d}.tgN{background:#cdeedd;color:#14213d}.tgX{background:#f6d0c6;color:#14213d}
.av{width:46px;height:46px;border-radius:50%;object-fit:cover;object-position:50% 20%;border:2px solid #fca311;vertical-align:middle;margin-right:10px;background:#ddd}
table.v td.who{white-space:nowrap;font-weight:700;color:#14213d}
.lat{font-family:'Bitstream Charter','DejaVu Serif',serif;font-style:italic;font-size:18px;line-height:1.5;color:#2f3a52}
"""
E = lambda s: html.escape(s, quote=False)
def marks(s):
    s = E(s).replace('&lt;br&gt;', '<br>')
    s = re.sub(r'\[\[k:(.+?)\]\]', r'<mark class="k">\1</mark>', s)
    s = re.sub(r'\[\[a:(.+?)\]\]', r'<mark class="a">\1</mark>', s)
    s = re.sub(r'\[\[g:(.+?)\]\]', r'<span class="gr">\1</span>', s)
    return s
TAGNAME = {'H': 'Hebreos', 'P': 'Razonamiento paralelo a Hebreos', 'D': 'Evangelio frente al AT', 'N': 'No matar a herejes', 'X': 'Matiz en contra'}
def tags(ts):
    return ''.join(f'<span class="tg tg{t}">{TAGNAME[t]}</span>' for t in ts)
def page(out, fname, cid, tag, kind, title, ref, body, foot, kind_cls='es', head_cls='alt', arref=''):
    h = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="card">
<div class="hd {head_cls}"><div class="row"><div class="badge"><b>{cid}</b>{E(tag)}</div><span class="kind {kind_cls}">{E(kind)}</span></div>
<h1>{E(title)}</h1>
<div class="row"><div class="ref">{E(ref)}</div><div class="arref">{arref}</div></div></div>
<div class="bd">{body}</div>
<div class="ft"><div class="u">{foot}</div></div>
</div></body></html>'''
    os.makedirs(out, exist_ok=True)
    open(f'{out}/{fname}.html', 'w', encoding='utf-8').write(h)
PACK = 'Pack «Hebreos 10:28, Aquino y los Padres de la Iglesia: respuesta al vídeo de @antibulos1»'
