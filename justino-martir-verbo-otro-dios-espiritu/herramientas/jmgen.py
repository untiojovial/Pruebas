# -*- coding: utf-8 -*-
import sys, os, shutil
B = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad'
UG = B + '/jm'; UQ = B + '/jq'
sys.path.insert(0, B + '/hb'); sys.path.insert(0, UG)
import hbcss, genpad
from hbcss import E
from jmdata import S
OUT = UG + '/jmcards'; os.makedirs(OUT + '/img', exist_ok=True)
PACK = 'Pack «Justino Mártir, ¿trinitario? El Verbo, el «otro Dios» y el Espíritu profético»'
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
    return f'<div class="lq"><div class="{cls}"><span class="lg {lc}">{nm}</span>{E(q["txt"])}</div><div class="es"><span class="lg" style="color:#1d7a4f">Español</span> {E(q["es"])}</div><div class="rf"><b>{E(q["ref"])}</b> · {E(q["src"])} · <span style="color:#8a93a6">{q["id"]}</span></div></div>'
FOOT = PACK + '<br>Traducciones al español mías. Griego/latín/inglés tal como se indica en cada cita; entre corchetes […] lo omitido. Lo no verificado se dice.'
TABLE = [
 ('A · «lo tenemos en segundo lugar… el Espíritu en tercer orden» (1 Apol. 13)', 'Se explica, con límite', 'Orden de origen y adoración al Hijo, no rango de naturaleza; Justino no dice «consustancial».', 'JM03'),
 ('B · «otro Dios… subordinado… en número, no en voluntad» (Dial. 56)', 'Parcial', 'Cada cláusula se corrige (misma voluntad; único «Dios sobre quien no hay otro»); persona vs. naturaleza es vocabulario posterior (Bull, Aquino, Hilario). No se resuelve por sí solo.', 'JM09 · JM17'),
 ('C · «ángel», «ministro» del Padre (Dial. 58, 116, 126-127)', 'Se explica, con límite', 'Función de mensajero; el Hijo es «Dios, Hijo del único Dios» y las teofanías son suyas porque el Padre no se mueve. Newman concede vocabulario subordinacionista.', 'JM10'),
 ('D · «Dios engendró antes de todas las criaturas un poder racional» (Dial. 61-62)', 'Parcial', '«Racional», «de sí mismo», «junto al Padre antes de toda criatura», «este mismo Dios engendrado»; pero «antes de las criaturas» no es «eterno».', 'JM11'),
 ('E · «por su poder y voluntad, no por abscisión» (Dial. 128; 2 Apol. 6)', 'Se explica, con límite', 'Justino rechaza la división de la esencia; «voluntad» se matiza con «por naturaleza» (Atanasio) y «como concomitancia» (Aquino). La luz del sol es de los adversarios.', 'JM12 · JM16'),
 ('F · «primogénito de toda la creación» (Dial. 84, 100, 125)', 'Parcial', '«Antes de todas las criaturas», «unigénito… de modo propio»; Novaciano lo lee así; sentido literal temporal innegable (Newman).', 'JM13'),
 ('G · «el Espíritu y el poder… son el Verbo» (1 Apol. 33.6)', 'Parcial', 'Exégesis de Lc 1:35, no teoría; el Espíritu aparece aparte en 6, 13, 60, 61, 65, 67; pneumatología poco desarrollada.', 'JM05'),
 ('H · «era engendrado cuando creó todo» (2 Apol. 6)', 'No del todo', 'Participios unidos («estaba con él y era engendrado»); pero Newman: el sentido literal es temporal y «requiere acomodación».', 'JM07 · JM15'),
 ('I · Hijo Dios, adorado, distinto del Padre, fórmula trinitaria', 'Sí', '«es también Dios» (1 Apol. 63.15), «Dios, Hijo del único Dios» (Dial. 126), adoración al Verbo (2 Apol. 13), bautismo trino (1 Apol. 61).', 'JM04 · JM06 · JM08'),
]
def cls(v): return 'v1' if v.startswith('Sí') or v == 'Se explica' else ('v3' if v.startswith('No') else 'v2')
CONC = '<div class="rs2"><b>Conclusión.</b> Justino afirma <b>distinción real</b> entre Padre, Hijo y Espíritu profético, <b>adoración</b> del Hijo, que el Verbo «es también Dios», engendrado «de sí mismo» y antes de toda criatura, y la fórmula bautismal trina; y rechaza expresamente la división de la esencia y el modalismo. <b>No es arriano ni nicenista formulado</b>: la distinción «en número, no en voluntad», la subordinación de origen y misión, la generación ligada a la creación y un Espíritu poco desarrollado son rasgos preniceños que la tradición posterior explica, y que estudiosos como Newman y Kono toman en su sentido literal. Defenderlo honestamente es decir esto.</div>'
for s in S:
    if s['id'] == 'JM19':
        rh = ''.join(f'<tr><td style="font-weight:700;font-size:14px">{a}</td><td class="{cls(b)}" style="font-weight:700;white-space:normal">{b}</td><td style="font-size:13.5px">{c}</td><td style="font-weight:700;white-space:nowrap;font-size:13px">{d}</td></tr>' for a, b, c, d in TABLE)
        body = f'<table class="v" style="table-layout:fixed"><tr><th style="width:310px">Pasaje difícil</th><th style="width:130px">¿Se resuelve?</th><th>Cómo</th><th style="width:130px">Diapositivas</th></tr>{rh}</table>{CONC}'
        card('JM19', hdr('JM19', 'Justino · mapa', 'Resumen', s['title'], s['sub']), body, FOOT); continue
    body = ''.join(qhtml(q) for q in s['quotes']) + f'<div class="rs2">{s["res"]}</div>'
    card(s['id'], hdr(s['id'], 'Justino', 'Cita y resolución', s['title'], s['sub']), body, FOOT)
def cap(fn, cid, title, items, note, ref):
    g = ''
    for i, (img, t) in enumerate(items):
        shutil.copy(UQ + '/pg/' + img, f'{OUT}/img/{cid}_{i}.png')
        g += f'<div class="c"><img src="img/{cid}_{i}.png"><div class="t">{t}</div></div>'
    card(fn, hdr(cid, 'Páginas reales', 'Capturas', title, ref), f'<div class="capg">{g}</div><div class="rs2">{note}</div>', PACK)
cap('JM20', 'JM20', 'Páginas reales del griego: Otto 1842 (1 Apol. 13) y Trollope 1846 (Diálogo 61)', [('otto164.png', '<b>Otto, <i>S. Justini… opera</i> vol. 1 (Jena 1842), p. 164</b> · 1 Apol. 13: oro «lo tenemos en segundo lugar, y al Espíritu profético en tercer orden»; azul «nos acusan de locura… dar el segundo lugar… después del Dios inmutable y siempre existente… a un hombre crucificado». Abajo, el aparato de Otto.'), ('trollope124.png', '<b>Trollope (Cambridge 1846), p. 124</b> (recorte) · Diálogo 61: oro «Dios engendró… un poder racional de sí mismo, que el Espíritu Santo llama gloria del Señor, Hijo, Sabiduría, Ángel, Dios, Señor y Verbo…»; azul «al proferir una palabra, engendramos una palabra, no por abscisión… y lo mismo en el fuego».')],
    'Son las páginas de los escaneos abiertos de archive.org; el griego se identifica con la imagen. El subrayado es mío.', 'Otto 1842 y Trollope 1846, escaneos abiertos; subrayado mío')
cap('JM21', 'JM21', 'Páginas reales (ANF vol. 1): 1 Apol. 13, Diálogo 56 y 61', [('anf185.png', '<b>ANF vol. 1, p. 167</b> · 1 Apol. 13: «lo tenemos en segundo lugar y al Espíritu profético en el tercero».'), ('anf241.png', '<b>p. 223</b> · Diálogo 56: «otro Dios y Señor subordinado al Hacedor de todas las cosas» y «numéricamente, quiero decir, no [distinto] en voluntad».'), ('anf245.png', '<b>p. 227</b> · Diálogo 61: «Dios engendró antes de todas las criaturas un Principio… un poder racional» y «no por abscisión, para no disminuir la palabra». Notas: «el acto de voluntad es por parte del Padre»; «logos» es a la vez razón y palabra.')],
    'Inglés de Dods y Reith (ANF vol. 1, escaneo de archive.org con capa de texto). Las notas al pie son de los editores del siglo XIX; sus lecturas son opiniones editoriales.', 'ANF vol. 1 (Buffalo 1885), escaneo abierto; subrayado mío')
cap('JM22', 'JM22', 'Páginas reales (ANF vol. 1): Diálogo 128 y 2 Apología 6', [('anf282.png', '<b>ANF vol. 1, p. 264</b> · Diálogo 128: «por su poder y voluntad, pero no por abscisión, como si se dividiera la esencia del Padre» y «numéricamente distinto de aquel que engendra». En la misma página aparece la imagen de la luz del sol: es la de los adversarios.'), ('anf208.png', '<b>p. 190</b> · 2 Apol. 6: «el Verbo que estaba con Él y era engendrado antes de las obras».')],
    'En 128 el pasaje de la luz del sol («dicen ellos») lo rechaza Justino; no es suyo.', 'ANF vol. 1 (Buffalo 1885), escaneo abierto; subrayado mío')
body = '''<div class="two"><div class="pn"><h4>Método</h4><ul class="l" style="font-size:15px;line-height:1.45">
<li>Once investigadores (modelo pequeño): J1 1 Apol. 1-30; J2 1 Apol. 31-68; J3 2 Apol.; J4 Diálogo 1-55; J5 Diálogo 56-60 y 126-127; J6 Diálogo 61-62 y 128-129; J7 resto del Diálogo; J8 escaneos y griego; J9 estudiosos; J10 metafísica; J11 recepción. Encargos y datos en <code>herramientas/</code>.</li>
<li><b>Yo comprobé</b> en imagen de página: Otto 1842 p. 164 (1 Apol. 13), Trollope 1846 p. 124 (Diálogo 61) y las páginas impresas de la ANF 167, 190, 223, 227 y 264 (inglés). El resto del griego lo leyeron los investigadores: Otto 1842, Rauschen 1911 y Trollope en imagen; Migne y Otto vol. 2 sólo en OCR (marcado en cada cita).</li>
<li>Traducciones al español mías, desde el griego cuando se muestra, desde el inglés cuando sólo hay inglés.</li></ul></div>
<div class="pn"><h4>Correcciones y negativos</h4><ul class="l" style="font-size:14.5px;line-height:1.42">
<li>Dial. 56: no aparece «<i>héteros theós</i>» ni «<i>arithmô héteros</i>» con los números de sección del encargo; el texto es «Θεὸς καὶ Κύριος ἕτερος ὑπὸ τὸν ποιητὴν τῶν ὅλων… ἀριθμῷ… ἀλλ’ οὐ γνώμῃ» (sin numeración de sección fiable).</li>
<li>Dial. 128: la imagen de la luz del sol es de los <b>adversarios</b>, no de Justino.</li>
<li>1 Apol. 63: no dice «llamado Dios» de Jesús; dice que el Verbo, primogénito, «es también Dios».</li>
<li>Dial. 48.2 es <b>condicional</b>, no una renuncia a la preexistencia.</li>
<li>Atanasio: el «no por voluntad» está en De Syn. 26.7 y 42 y en Contra los arrianos III.59-66, no en De Decr. 20-24.</li>
<li>Escritos espurios (Exposición de la fe, Preguntas…) <b>no usados</b>.</li>
<li>No pude abrir Barnard, Prestige, Kelly, Bethune-Baker (restringidos) ni leer Semisch (gótico). Capturas del griego de Migne y Otto vol. 2: no hay (PDF de más de 60 MB).</li></ul></div></div>'''
card('JM23', hdr('JM23', 'Fuentes y límites', 'Resumen', 'Qué se leyó, qué se corrigió y qué no se pudo comprobar', 'Resumen honesto del método y sus límites'), body, FOOT)
print('jmgen ok', len(S))
