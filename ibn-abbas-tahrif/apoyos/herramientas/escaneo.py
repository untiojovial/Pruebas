# -*- coding: utf-8 -*-
# Escaneo de comentarios coránicos descargados de quran-tafsir.net (lista en urls_escaneo.txt: «URL nombre_de_fichero»).
# Uso: python3 -I escaneo.py <carpeta_con_las_paginas_descargadas>
# Marca las páginas donde «ابن عباس» aparece a ≤300 caracteres de términos de interpretación/texto. Es un filtro: hay que leer cada hallazgo.
import re, html, glob, os, sys
DIA = re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ]')
MAP = {'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا', 'ى': 'ي', 'ة': 'ه', 'ؤ': 'و', 'ئ': 'ي'}
KW = re.compile(r'التاويل|يتاول|تاويل|يزيل لفظ|بقاء لفظ|لفظ التوراه باق|بالمعني لا باللفظ|لا يمكن تغيير|تحريف المعني|المعني دون اللفظ|باللفظ')
def norm(t): return ''.join(MAP.get(c, c) for c in DIA.sub('', t))
def text(f):
    t = open(f, encoding='utf-8', errors='replace').read()
    t = re.sub(r'<script.*?</script>|<style.*?</style>', '', t, flags=re.S)
    t = norm(html.unescape(re.sub(r'<[^>]+>', ' ', t))); t = re.sub(r'\s+', ' ', t)
    i = t.find('الاية السابقة'); return t[:i] if i > 0 else t   # corta la lista de otros comentarios
d = sys.argv[1]
for f in sorted(glob.glob(os.path.join(d, '*.html'))):
    t = text(f)
    for m in re.finditer('ابن عباس', t):
        c = t[max(0, m.start() - 300):m.end() + 300]
        if KW.search(c): print(os.path.basename(f)); print('   ', c); break
