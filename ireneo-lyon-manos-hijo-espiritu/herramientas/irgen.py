# -*- coding: utf-8 -*-
import sys, os, shutil, re
B = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad'
UG = B + '/ir'; UQ = B + '/iq'
sys.path.insert(0, B + '/hb'); sys.path.insert(0, UG)
import hbcss, genpad
from hbcss import E
from irdata import S
OUT = UG + '/ircards'; os.makedirs(OUT + '/img', exist_ok=True)
PACK = 'Pack «Ireneo de Lyon, ¿trinitario? Las dos manos de Dios, el Hijo y el Espíritu»'
CSS = hbcss.CSS + genpad.CQ + """
.lq{border:1px solid #d6dbe4;border-radius:10px;margin:0 0 10px;background:#fff;overflow:hidden}
.lq .la{font-family:'Gentium Plus','Gentium Book Plus','DejaVu Serif','Bitstream Charter',serif;font-size:17px;line-height:1.5;color:#2f3a52;background:#f6f4ec;padding:9px 16px;border-bottom:1px solid #e3e7ee}
.lq .la.lat{font-style:italic}
.lq .la.en{font-family:'Inter',sans-serif;font-size:15px}
.lq .es{font-size:17.5px;line-height:1.5;padding:9px 16px;color:#1b2333}
.lq .rf{font-size:12.5px;color:#566079;padding:5px 16px;background:#eef1f8;line-height:1.4}
.lq .rf b{color:#14213d}
.lq .lg{font-size:11px;letter-spacing:.08em;text-transform:uppercase;font-weight:700;color:#8a6d00;margin-right:6px;font-family:'Inter',sans-serif;font-style:normal}
.lq .lg.en{color:#1d5f9a}
.rs2{border-left:6px solid #14213d;background:#eef1f8;padding:12px 20px;border-radius:0 8px 8px 0;font-size:15.5px;line-height:1.52;margin-top:8px}
.rs2 b{color:#14213d}
.capg{display:flex;gap:14px;align-items:flex-start}
.capg .c{flex:1;min-width:0;border:1px solid #cfd6e2;border-radius:8px;overflow:hidden;background:#fff}
.capg img{width:100%;display:block}
.capg .t{font-size:12.5px;line-height:1.4;color:#2f3a52;padding:6px 10px;background:#f4f5f8}
.v1{color:#1d7a4f}.v2{color:#9a6a00}.v3{color:#b44a2f}
"""
LANG = {'gr': ('Griego', 'la', ''), 'en': ('Inglés', 'la en', 'en'), 'la': ('Latín', 'la lat', '')}
def hdr(cid, tag, kind, title, ref):
    return f'<div class="hd alt"><div class="row"><div class="badge"><b>{cid}</b>{tag}</div><span class="kind es">{kind}</span></div><h1>{title}</h1><div class="row"><div class="ref">{ref}</div></div></div>'
def card(fname, head, body, foot):
    h = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="card">{head}<div class="bd">{body}</div><div class="ft"><div class="u">{foot}</div></div></div></body></html>'
    open(f'{OUT}/{fname}.html', 'w', encoding='utf-8').write(h)
def qhtml(q):
    nm, cls, lc = LANG[q['lang']]
    return f'<div class="lq"><div class="{cls}"><span class="lg {lc}">{nm}</span>{E(q["txt"])}</div><div class="es"><span class="lg" style="color:#1d7a4f">Español</span> {E(re.sub(r"<[^>]+>","",q["es"]))}</div><div class="rf"><b>{E(q["ref"])}</b> · {E(q["src"])} · <span style="color:#8a93a6">{q["id"]}</span></div></div>'
FOOT = PACK + '<br>Traducciones al español mías. Griego/latín/inglés tal como se indica en cada cita; entre corchetes […] lo omitido. Lo no verificado se dice.'
TABLE = [
 ('A · Dios «todo mente, todo Verbo»; el Verbo no es una «tercera» emisión (2.13, 2.28.5)', 'Se explica', 'Rechaza la «prolación» gnóstica, no la generación; Tertuliano, en cambio, acepta «prolatio» (Prax. 8). Agustín/Aquino: simplicidad divina y Verbo inmanente.', 'IR04 · IR17'),
 ('B · «ni el Hijo, sino sólo el Padre» (Mc 13:32) y «el Padre es mayor» (2.28.6, 2.28.8)', 'Se explica, con límite', 'Ireneo lo usa como regla de humildad; Agustín (De Trin. I.12) y Aquino (III q.10 a.2) lo leen «no lo da a conocer»; Atanasio, «como hombre». Ireneo no da esa explicación.', 'IR05 · IR16'),
 ('C · generación «inenarrable»; «engendrado antes de toda creación» (2.28.6; 3.18.1; Dem. 30)', 'Se explica', 'Gregorio Nacianceno, Or. 29.8, repite el argumento; no es subordinación sino confesión de misterio.', 'IR06 · IR16'),
 ('D · «sólo el Padre es Dios y Señor» (3.6.1, 3.9.1) frente a Dem. 47: «lo engendrado de Dios es Dios»', 'Se explica', 'Contexto antignóstico (un solo Dios creador); el Hijo y el Espíritu reciben el nombre de Dios y Señor en el mismo libro y en la Demostración.', 'IR07'),
 ('E · «el Hijo es la medida del Padre»; Padre invisible, Hijo visible (4.4.2, 4.6.6)', 'Parcial', 'Aquino I q.42 a.5 (inhabitación mutua); pero «medida» es un juego de palabras del latín y «invisible del Hijo» no es lenguaje niceno formulado.', 'IR08 · IR17'),
 ('F · «el Verbo, el Hijo… la Sabiduría, que es el Espíritu» (4.20.3), distinto de Justino', 'Parcial', 'Identificación propia de Ireneo (Justino, Dial. 61, y Tertuliano leen Sabiduría = Hijo); Prov 8:22 queda tensa.', 'IR10'),
 ('G · «Padre sobre todos», «cabeza de Cristo», «sólo ingénito» (4.20.2, 5.18.2, 5.20.2, 5.36.2)', 'Parcial', 'Orden de la economía (Bull) frente a subordinación de naturaleza (Bethune-Baker, Newman): Ireneo no distingue las dos cosas con vocabulario niceno.', 'IR11 · IR14 · IR15'),
 ('H · Padre, Hijo y Espíritu en la regla de fe; las «dos manos»; Dem. 6, 10, 47', 'Sí', 'Regla de fe trina (1.10.1, 4.33.7, Dem. 6); el Hijo y el Espíritu «siempre con él» (4.20.1) y «manos» (5.6.1, 5.28.4); «lo engendrado de Dios es Dios» (Dem. 47).', 'IR02 · IR09 · IR12'),
]
def cls(v): return 'v1' if v.startswith('Sí') or v == 'Se explica' else ('v3' if v.startswith('No') else 'v2')
CONC = '<div class="rs2"><b>Conclusión.</b> Ireneo es el testigo más fuerte del siglo II: regla de fe de tres miembros, Hijo y Espíritu «siempre con» el Padre y como sus «manos», el Hijo «Dios» (Dem. 47) y la generación «inenarrable». <b>Es trinitario en estructura, con lenguaje preniceno, no un trinitario niceno formulado</b>: no usa «consustancial» ni «Trinidad», el Padre es «sobre todos» y «sólo ingénito», la Sabiduría = Espíritu choca con Justino y Tertuliano, y varias frases (Mc 13:32, «medida», «invisible del Hijo») sólo se resuelven con la metafísica posterior. Defenderlo honestamente es decir esto.</div>'
for s in S:
    if s['id'] == 'IR18':
        rh = ''.join(f'<tr><td style="font-weight:700;font-size:14px">{a}</td><td class="{cls(b)}" style="font-weight:700;white-space:normal">{b}</td><td style="font-size:13.5px">{c}</td><td style="font-weight:700;white-space:nowrap;font-size:13px">{d}</td></tr>' for a, b, c, d in TABLE)
        body = f'<table class="v" style="table-layout:fixed"><tr><th style="width:310px">Pasaje difícil</th><th style="width:130px">¿Se resuelve?</th><th>Cómo</th><th style="width:130px">Diapositivas</th></tr>{rh}</table>{CONC}'
        card('IR18', hdr('IR18', 'Ireneo · mapa', 'Resumen', s['title'], s['sub']), body, FOOT); continue
    body = ''.join(qhtml(q) for q in s['quotes']) + f'<div class="rs2">{s["res"]}</div>'
    card(s['id'], hdr(s['id'], 'Ireneo', 'Cita y resolución', s['title'], s['sub']), body, FOOT)
def cap(fn, cid, title, items, note, ref):
    g = ''
    for i, (img, t) in enumerate(items):
        shutil.copy(UQ + '/pg/' + img, f'{OUT}/img/{cid}_{i}.png')
        g += f'<div class="c"><img src="img/{cid}_{i}.png"><div class="t">{t}</div></div>'
    card(fn, hdr(cid, 'Páginas reales', 'Capturas', title, ref), f'<div class="capg">{g}</div><div class="rs2">{note}</div>', PACK)
cap('IR20', 'IR20', 'Páginas reales del latín (Harvey 1857, vol. 2): 4.20.1 y 4.20.3, pp. 213-214', [('harv213.png', '<b>Harvey, vol. 2, p. 213</b> · 4.20.1: «Semper enim adsunt ei Verbum et Sapientia, Filius et Spiritus, per quos et in quibus omnia libere et sponte fecit» (resaltado).'), ('harv214.png', '<b>p. 214</b> · 4.20.3: «Verbum, hoc est Filium, semper cum Patre fuisse… et Sapientiam, quae est Spiritus, adfuisse ei ante omnem constitutionem» (resaltado).')],
    'Es el escaneo de archive.org de Harvey (Cambridge 1857), con la versión latina antigua del griego perdido; sin capa de texto, así que el latín lo identifiqué en la imagen. El subrayado es mío. El griego sólo se conserva en fragmentos (la p. 213 trae uno, de Eusebio, en el cuerpo de la página).', 'Harvey 1857, vol. 2, escaneo abierto; subrayado mío')
cap('IR21', 'IR21', 'Páginas reales en inglés (ANF vol. 1): 1.10.1, 2.28.6 y 4.20.3', [('anf330.png', '<b>ANF vol. 1, p. 330</b> · 1.10.1: la regla de fe (Padre, Cristo Jesús, Espíritu Santo).'), ('anf401.png', '<b>p. 401</b> · 2.28.6: Mc 13:32 («ni el Hijo, sino el Padre») y «Since therefore His generation is unspeakable». Nota de los editores: Marcos está citado de memoria.'), ('anf488.png', '<b>p. 488</b> · 4.20.3: «the Word, namely the Son… Wisdom, which is the Spirit» (dos columnas resaltadas).')],
    'Traducción inglesa del siglo XIX (Roberts y Rambaut). La numeración ANF difiere de la de Harvey en el libro 3 (ANF 3.16.6 = Harvey 3.17.6). El subrayado es mío.', 'ANF vol. 1 (Buffalo 1885), escaneo abierto; subrayado mío')
body = '''<div class="two"><div class="pn"><h4>Método</h4><ul class="l" style="font-size:15px;line-height:1.45">
<li>Once investigadores (modelo pequeño): I1 Haer. 1 y 2.1-27; I2 2.28-35; I3 3.1-15; I4 3.16-25; I5 4.1-19; I6 4.20-41; I7 libro 5 y fragmentos; I8 <i>Demostración</i>; I9 escaneos y latín; I10 estudiosos y recepción; I11 metafísica y paralelos. Encargos y datos en <code>herramientas/</code>.</li>
<li><b>Yo comprobé</b> en imagen de página: Harvey vol. 2 pp. 213-214 (latín) y ANF vol. 1 pp. 330, 401 y 488 (inglés). El resto lo leyeron los investigadores (marcado en cada cita; el latín de Harvey casi todo sin capa de texto, por OCR).</li>
<li>Traducciones al español mías, desde el latín cuando se muestra, desde Robinson 1920 (inglés) para la <i>Demostración</i>.</li></ul></div>
<div class="pn"><h4>Correcciones y negativos</h4><ul class="l" style="font-size:14.5px;line-height:1.42">
<li>«Por el Verbo y el Espíritu» es 1.22.1; en 2.2.4-5 sólo «Verbo»; 2.30.9 dice «Verbo y Sabiduría».</li>
<li>«Manos = Hijo y Espíritu» está en 5.6.1, 5.28.4 y el prefacio del libro 4, no en 4.20.1 ni 4.7.4.</li>
<li>«Padre de todos» es 3.6.5 (no 3.8.3); «Pater super omnes», 4.20.2; «invisible del Hijo», 4.6.6; «medida», 4.4.2.</li>
<li>La <i>Demostración</i> dice «tres puntos», no «tres artículos»; Atanasio (NPNF2) no nombra a Ireneo, sólo las notas editoriales.</li>
<li>Aquino sobre inhabitación mutua: I q.42 a.5, no a.4. Numeración ANF y Harvey distintas.</li>
<li>La <i>Demostración</i> sólo existe en armenio: no lo leí; uso Robinson. Los fragmentos de Pfaff son espurios o dudosos: excluidos.</li>
<li>No pude abrir Kelly, Lawson, Briggman, Behr, Osborn ni Steenberg (restringidos). Un agente mató procesos de otro (<code>pkill tesseract</code>) y el disco se llenó durante la investigación; libré espacio sin perder datos.</li></ul></div></div>'''
card('IR22', hdr('IR22', 'Fuentes y límites', 'Resumen', 'Qué se leyó, qué se corrigió y qué no se pudo comprobar', 'Resumen honesto del método y sus límites'), body, FOOT)
print('irgen ok', len(S))
