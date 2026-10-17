# -*- coding: utf-8 -*-
# Utilidades para leer los textos de OpenITI de Ibn Taymiyya y extraer pasajes literales con su página.
# Uso (desde Python):  import sys; sys.path.insert(0, '<carpeta de este fichero>'); import itlib
#   t = itlib.get('JawabSahih')            # descarga (con caché) y devuelve el texto crudo
#   idx = itlib.Index(t)                   # índice de búsqueda sin vocalización
#   for s, e in idx.find('الأقانيم'): print(idx.where(s), idx.snippet(s, 200))
#   p = itlib.extract(t, s-100, e+400)     # dict con 'ar' (texto limpio), 'page_start', 'page_end', 'vol_page'
import os, re, csv, subprocess, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'cache'); os.makedirs(CACHE, exist_ok=True)
TSV = os.path.join(HERE, 'ibntaymiyya_openiti.tsv')
def _rows():
    with open(TSV, encoding='utf-8') as f:
        next(f)
        for line in f:
            b, tl, vu, cl, url = line.rstrip('\n').split('\t')
            yield b.split('.')[1], vu, int(cl or 0), url
def versions(book):
    """Lista (versionUri, longitud, url) de los ficheros de un libro (clave corta, p. ej. 'JawabSahih')."""
    return [(vu, cl, url) for b, vu, cl, url in _rows() if b == book]
def get(book_or_uri, version=None):
    """Devuelve el texto crudo. book_or_uri: clave corta ('JawabSahih') -> usa la versión más larga, o versionUri completo."""
    url = None
    for b, vu, cl, u in sorted(_rows(), key=lambda r: -r[2]):
        if vu == book_or_uri or (b == book_or_uri and (version is None or version in vu)):
            url, vuri = u, vu; break
    if not url: raise KeyError(book_or_uri)
    fn = os.path.join(CACHE, vuri + '.txt')
    if not os.path.exists(fn) or os.path.getsize(fn) < 1000:
        subprocess.run(['curl', '-sS', '-L', '-m', '600', '-o', fn, url], check=True)
    t = open(fn, encoding='utf-8').read()
    return t
def header(t, n=40):
    """Las primeras líneas (#META#) con datos de la edición impresa que sigue el texto."""
    return '\n'.join(t.split('\n')[:n])
PAGE = re.compile(r'PageV(\d+)P(\d+)')
def page_at(t, off):
    """Marca de página (vol, pág.) vigente en el desplazamiento 'off' del texto crudo."""
    last = None
    for m in PAGE.finditer(t, 0, off):
        last = m
    return (int(last.group(1)), int(last.group(2))) if last else None
_TASH = re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ]')
def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = _TASH.sub('', s)
    return (s.replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا').replace('ٱ', 'ا')
             .replace('ى', 'ي').replace('ة', 'ه').replace('ؤ', 'و').replace('ئ', 'ي'))
class Index:
    """Búsqueda en texto normalizado (sin vocales, alef/yaa unificadas) con vuelta a los desplazamientos crudos."""
    def __init__(self, t):
        self.t = t; chars = []; m = []
        for i, c in enumerate(t):
            n = norm(c)
            for d in n:
                chars.append(d); m.append(i)
        self.n = ''.join(chars); self.map = m
    def find(self, q, flags=0):
        """Devuelve [(inicio, fin)] crudos de cada aparición de q (cadena o regex ya normalizada)."""
        q = norm(q); out = []
        for mt in re.finditer(q, self.n, flags):
            out.append((self.map[mt.start()], self.map[min(mt.end(), len(self.map)) - 1] + 1))
        return out
    def where(self, off): return page_at(self.t, off)
    def snippet(self, off, w=200): return clean(self.t[max(0, off - w): off + w])
_MARK = re.compile(r'PageV\d+P\d+|ms\d+|~~|%~%|\n#+ ?|\n(?=[^\n])|\n')
def clean(s):
    s = re.sub(r'PageV\d+P\d+', ' ', s)
    s = re.sub(r'\bms\d+\b', ' ', s)
    s = s.replace('%~%', ' ').replace('~~', ' ')
    s = re.sub(r'(?m)^#+\s*', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()
def extract(t, start, end):
    """Pasaje literal t[start:end] limpio de marcas, con páginas inicial y final."""
    a = page_at(t, start); b = page_at(t, end)
    return {'ar': clean(t[start:end]), 'page_start': a, 'page_end': b,
            'vol_page': (f'vol. {a[0]}, p. {a[1]}' + (f'–{b[1]}' if b and b != a and b[0] == a[0] else '') if a else None),
            'offset_start': start, 'offset_end': end}
def verify(t, ar):
    """Comprueba que 'ar' (limpio) aparece literal en el texto limpio de t; devuelve True/False."""
    return clean(ar) in clean(t)
