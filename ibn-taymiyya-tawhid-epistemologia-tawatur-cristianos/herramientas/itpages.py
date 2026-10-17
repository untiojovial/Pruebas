# -*- coding: utf-8 -*-
# Página impresa de un pasaje según los marcadores de OpenITI.
# Convención comprobada contra los escaneos de Dar al-'Asima: el marcador PageV<v>P<n> va AL FINAL de la página n,
# de modo que el texto que sigue al marcador n está en la página n+1.
import re, bisect, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import itlib, itsrc
TOK = re.compile(r'\s?(\d+),(\d+)\s?')
_cache = {}
def build(work):
    key = itsrc.BOOK[work]
    if key in _cache: return _cache[key]
    t = itlib.get(key)
    t2 = itlib.PAGE.sub(lambda m: f'{m.group(1)},{m.group(2)}', t)
    c = itsrc.tidy(itlib.clean(t2))
    parts = TOK.split(c)
    final = parts[0]; marks = []
    for k in range(1, len(parts), 3):
        v, p, nxt = int(parts[k]), int(parts[k + 1]), parts[k + 2]
        if nxt:
            final += ' '; marks.append((len(final), v, p + 1)); final += nxt
    # (en Majmu' difiere 1 carácter de book_text por un espacio tras ك/ب junto a un marcador; no afecta a las páginas)
    pos = [m[0] for m in marks]
    _cache[key] = (final, marks, pos)
    return _cache[key]
def page_of(work, off):
    final, marks, pos = build(work)
    i = bisect.bisect_right(pos, off) - 1
    return (marks[i][1], marks[i][2]) if i >= 0 else None
def pages(work, text, k=40):
    """[(vol_ini, pág_ini, vol_fin, pág_fin)] por cada aparición del pasaje (se buscan sus primeras y últimas k letras)."""
    final, marks, pos = build(work)
    a_key, b_key = text[:k], text[-k:]
    out = []; i = final.find(a_key)
    while i >= 0:
        j = final.find(b_key, i)
        if j >= 0 and j + len(b_key) - i < len(text) + 60:
            a = page_of(work, i); b = page_of(work, j + len(b_key) - 1)
            out.append((a[0], a[1], b[0], b[1]) if a and b else None)
        i = final.find(a_key, i + 1)
    return out
def fmt(hit):
    v1, p1, v2, p2 = hit
    return f'vol. {v1}, p. {p1}' + (f'–{p2}' if p2 != p1 and v2 == v1 else '')
