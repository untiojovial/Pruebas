# -*- coding: utf-8 -*-
# Utilidades para leer cualquier texto de OpenITI (metadatos completos en it/oimeta.csv) con página impresa corregida.
# Uso:
#   import sys; sys.path.insert(0, '<esta carpeta>'); import oilib
#   oilib.find('IbnHisham')                      # lista de dicts (versionUri, title_lat, author_lat, date, chars, url) cuyo versionUri/título/autor contiene el texto (sin distinguir mayúsculas)
#   t = oilib.get('0213IbnHisham.SiraNabawiyya.Shamela0023833-ara1')   # texto crudo (con caché); también acepta un fragmento único del versionUri
#   print(oilib.header(t))                       # líneas #META# (edición impresa)
#   idx = oilib.Index(t); hits = idx.find('عائشه')   # búsqueda sin vocales ni distinción alef/ya/ta marbuta; hits = [(ini, fin)] crudos; admite regex ya normalizada
#   oilib.page(t, hits[0][0])                    # (vol, pág.) IMPRESA: el marcador PageV..P.. cierra la página, así que es marcador+1 (comprobado en Shamela/Al-Jawab al-Sahih; en otras versiones es una suposición)
#   oilib.snippet(t, hits[0][0], 300)            # contexto limpio
#   p = oilib.extract(t, ini, fin)               # dict: ar (literal y limpio), vol_page, offset_start, offset_end
#   oilib.verify(t, p['ar'])                     # debe dar True antes de guardar el pasaje
import os, re, csv, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
IT = os.path.join(os.path.dirname(HERE), 'it')
sys.path.insert(0, IT)
import itlib, itsrc
CACHE = os.path.join(HERE, 'oicache'); os.makedirs(CACHE, exist_ok=True)
_rows = None
def _load():
    global _rows
    if _rows is None:
        with open(os.path.join(IT, 'oimeta.csv'), encoding='utf-8', newline='') as f:
            _rows = list(csv.DictReader(f, delimiter='\t'))
    return _rows
def find(q, limit=60):
    q = q.lower(); out = []
    for r in _load():
        if q in (r['versionUri'] + ' ' + r['title_lat'] + ' ' + r['author_lat'] + ' ' + r['title_ar'] + ' ' + r['author_ar']).lower():
            out.append(dict(versionUri=r['versionUri'], title_lat=r['title_lat'], author_lat=r['author_lat'], date=r['date'], chars=int(r['char_length'] or 0), url=r['url'], ed_info=r['ed_info'][:120]))
    out.sort(key=lambda d: (d['date'], d['versionUri']))
    return out[:limit]
def get(vu):
    rows = [r for r in _load() if r['versionUri'] == vu] or [r for r in _load() if vu in r['versionUri']]
    if not rows: raise KeyError(vu)
    if len(rows) > 1: raise KeyError(f'ambiguo ({len(rows)}): ' + ', '.join(r['versionUri'] for r in rows[:6]))
    r = rows[0]; fn = os.path.join(CACHE, r['versionUri'] + '.txt')
    if not os.path.exists(fn) or os.path.getsize(fn) < 500:
        subprocess.run(['curl', '-sS', '-L', '-m', '600', '-o', fn, r['url']], check=True)
    return open(fn, encoding='utf-8').read()
header = itlib.header
Index = itlib.Index
def page(t, off):
    a = itlib.page_at(t, off)
    return (a[0], a[1] + 1) if a else None
def snippet(t, off, w=200): return itlib.clean(t[max(0, off - w): off + w])
def extract(t, s, e):
    a, b = page(t, s), page(t, e)
    vp = f'vol. {a[0]}, p. {a[1]}' + (f'–{b[1]}' if b and b != a and b[0] == a[0] else '') if a else None
    return {'ar': itsrc.tidy(itlib.clean(t[s:e])), 'vol_page': vp, 'offset_start': s, 'offset_end': e}
def verify(t, ar): return itsrc.tidy(ar) in itsrc.tidy(itlib.clean(t))
