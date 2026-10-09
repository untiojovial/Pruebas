# -*- coding: utf-8 -*-
import re, html
src = open('genv.py', encoding='utf-8').read()
CSS = re.search(r'CSS = """(.*?)"""', src, re.S).group(1)
CSS += """
table.v{width:100%;border-collapse:collapse;font-size:19px;line-height:1.45}
table.v th{background:#eef1f6;text-align:left;padding:10px 12px;font-size:15px;text-transform:uppercase;letter-spacing:.05em;color:#3b4660}
table.v td{border-top:1px solid #e3e7ee;padding:11px 12px;vertical-align:top}
.ok{color:#1d7a4f;font-weight:700}.no{color:#b44a2f;font-weight:700}.mid{color:#9a6a00;font-weight:700}
"""
R = [
 ("al-Yaʿqubi cuenta la conversión de Pablo con una voz, ceguera y Ḥananiyā, sin ángel", "ok", "Confirmado", "Idéntico en las 3 digitalizaciones de OpenITI. Dar Sadir, vol. 1, pp. 79–80 (marcadores «conforme al impreso»). W01"),
 ("La «p. 31» del foro", "mid", "Explicado", "Es la paginación automática de ketabonline (p. 31), no la del libro impreso. W01"),
 ("Ibn ʿAsakir, entrada 1825 «Ḥanīnā», con cadena hasta Wahb", "ok", "Confirmado", "Cadena tal cual: Ibn Sabir ← Abu l-Husayn al-Hafiz ← al-Jawlani ← ʿUmara ← Wathima ← ʿAmr ibn al-Azhari ← Idris ← Wahb. W02"),
 ("Páginas de Ibn ʿAsakir: vol. 15, «hacia pp. 332–333»", "mid", "Corregido", "Son las pp. 333–334 (Dar al-Fikr, 1995). W02"),
 ("En Ibn ʿAsakir falta el sobrino paseado y apedreado", "no", "Incorrecto", "El sobrino rapado, pregonado y apedreado sí está. Lo que falta es «ظالما غاشما» y «lo paseó por la ciudad». W02"),
 ("Ibn Manzur, Mujtasar, vol. 7, pp. 283–284", "ok", "Confirmado", "Mismo texto, sin la cadena: «dijo Wahb ibn Munabbih». W03"),
 ("Ibn ʿAsakir escribe «حنينا»; Ibn Kathir, «ضينا»", "ok", "Confirmado", "Las dos formas parecen deformaciones de Ḥananiyā (Ananías). W02, W04"),
 ("La «buena fe» de Pablo y la «iglesia de Pablo» no están en Ibn ʿAsakir", "ok", "Confirmado", "Cero apariciones en dos digitalizaciones de Ibn ʿAsakir y en Ibn Manzur. Sí están en todas las ediciones de Ibn Kathir (Shiri 2/119; Saʿada 2/100–101; Dar Hayar 2/529–530). W04"),
 ("Nota de manuscrito de Saʿada, vol. 2, p. 100", "mid", "Sin verificar", "En la p. 100 hay una nota [1], pero va en «los compañeros de sus compañeros» (Marcos y Lucas), no en Pablo, y su texto no está digitalizado. W04"),
]
rows = ''.join(f'<tr><td>{html.escape(a)}</td><td class="{c}">{html.escape(b)}</td><td>{html.escape(d)}</td></tr>' for a, c, b, d in R)
page = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="card">
<div class="hd"><div class="row"><div class="badge"><b>W00</b>Verificación · Pablo en Damasco</div><span class="kind es">Resumen en español</span></div>
<h1>Qué se ha confirmado del análisis que me pasaste, y qué no</h1>
<div class="row"><div class="ref">Comprobado en el corpus OpenITI (GitHub) y en las páginas impresas de shamela.ws; capturas en W01–W04.</div><div class="arref">التحقق</div></div></div>
<div class="bd"><table class="v"><tr><th style="width:38%">Afirmación</th><th style="width:14%">Resultado</th><th>Detalle y tarjeta</th></tr>{rows}</table></div>
<div class="ft"><div class="u">Fuentes: github.com/OpenITI (0300AH, 0575AH, 0725AH, 0775AH) · shamela.ws libros 71, 3118, 8376 y 4445<br>Mini-pack «Pablo en Damasco»</div></div>
</div></body></html>'''
open('wcards/W00_es.html', 'w').write(page)
