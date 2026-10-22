# -*- coding: utf-8 -*-
import sys, os, shutil, re
B = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad'
UG = B + '/at'; UQ = B + '/aq'
sys.path.insert(0, B + '/hb'); sys.path.insert(0, UG)
import hbcss, genpad
from hbcss import E
from atdata import S
OUT = UG + '/atcards'; os.makedirs(OUT + '/img', exist_ok=True)
PACK = 'Pack «Atenágoras de Atenas, ¿trinitario? El Hijo «en idea y operación», la «efusión» y el orden»'
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
 ('A · «el Hijo es el Verbo del Padre en idea y en operación» (Leg. 10.2)', 'Se explica, con límite', 'Ejemplar y eficacia en el Verbo (Aquino q.34 a.3); «Hijo», «uno el Padre y el Hijo» e inhabitación mutua en el mismo texto; Newman advierte riesgo sabeliano.', 'AT04 · AT15'),
 ('B · «primer engendrado… no como hecho», pero «salió» para crear (Leg. 10.3)', 'Se explica, con límite', '«Mente eterna… eternamente racional»; «salida» = hacia la materia; Atanasio I.17; Newman y Dorner reconocen la lectura temporal posible.', 'AT05 · AT15'),
 ('C · el Espíritu como «efusión» (apórroia) que vuelve como rayo (Leg. 10.4)', 'Parcial', 'Bull y Bethune-Baker lo leen como procesión esencial; Loofs duda de la personalidad; Atanasio sustituye la imagen por «resplandor»; Gregorio: ¿sustancia o accidente?', 'AT06 · AT16'),
 ('D · «unión en poder y distinción en orden» (Leg. 10, 12), sin «Tríada»', 'Parcial', 'Enumeración con estructura, retomada por Basilio y Tertuliano; la unidad es en «poder»; Loofs: no es doctrina trinitaria.', 'AT07 · AT16'),
 ('E · «unidos en esencia» (ANF, Leg. 24) / «unidad y poder de espíritu» (10.2)', 'No (corrección)', 'El griego dice «unidos en poder»; «en esencia» es conjetura de Gesner rechazada por Otto; «pneûma» en 10.2 puede ser la esencia divina. No es testigo de homoousios.', 'AT08'),
 ('F · ángeles y «ministros» (Leg. 10, 24)', 'Se explica', 'El Verbo es quien los ordena; los ángeles son criaturas con providencia particular; no se dice nada de la generación.', 'AT09'),
 ('G · «sólo eterno el Dios ingénito» (Leg. 30) y Espíritu-flautista (Leg. 9)', 'Parcial', 'Contexto contra dioses míticos; el Verbo «eterno» en 10.3; el flautista es analogía de inspiración; el Espíritu es la parte más débil del caso.', 'AT10 · AT03'),
 ('H · Hijo, Verbo, «no hecho», mente eterna, inhabitación Padre-Hijo', 'Sí', '«Νοοῦμεν… υἱὸν τοῦ θεοῦ», «πρῶτον γέννημα… οὐχ ὡς γενόμενον», «ἐν πατρὶ… πατρὸς ἐν υἱῷ»: leídos en la página de Otto.', 'AT04 · AT05'),
]
def cls(v): return 'v1' if v.startswith('Sí') or v == 'Se explica' else ('v3' if v.startswith('No') else 'v2')
CONC = '<div class="rs2"><b>Conclusión.</b> Atenágoras afirma que el Hijo es el Verbo del Padre, «no hecho», engendrado de una «mente eterna», «en» el Padre y «uno» con él, y enumera Padre, Hijo y Espíritu Santo con «unión» y «distinción en el orden». <b>No es arriano ni modalista, pero tampoco un trinitario formulado</b>: el Espíritu es una «efusión» de personalidad discutida, la unidad se dice «en poder» (no «en esencia»), el «salió» para crear admite una lectura temporal, y la obra no habla de Jesucristo. Defenderlo honestamente es decir esto, y explicar el vocabulario del siglo II con la metafísica posterior.</div>'
for s in S:
    if s['id'] == 'AT18':
        rh = ''.join(f'<tr><td style="font-weight:700;font-size:14px">{a}</td><td class="{cls(b)}" style="font-weight:700;white-space:normal">{b}</td><td style="font-size:13.5px">{c}</td><td style="font-weight:700;white-space:nowrap;font-size:13px">{d}</td></tr>' for a, b, c, d in TABLE)
        body = f'<table class="v" style="table-layout:fixed"><tr><th style="width:310px">Pasaje difícil</th><th style="width:130px">¿Se resuelve?</th><th>Cómo</th><th style="width:130px">Diapositivas</th></tr>{rh}</table>{CONC}'
        card('AT18', hdr('AT18', 'Atenágoras · mapa', 'Resumen', s['title'], s['sub']), body, FOOT); continue
    body = ''.join(qhtml(q) for q in s['quotes']) + f'<div class="rs2">{s["res"]}</div>'
    card(s['id'], hdr(s['id'], 'Atenágoras', 'Cita y resolución', s['title'], s['sub']), body, FOOT)
def cap(fn, cid, title, items, note, ref):
    g = ''
    for i, (img, t) in enumerate(items):
        shutil.copy(UQ + '/pg/' + img, f'{OUT}/img/{cid}_{i}.png')
        g += f'<div class="c"><img src="img/{cid}_{i}.png"><div class="t">{t}</div></div>'
    card(fn, hdr(cid, 'Páginas reales', 'Capturas', title, ref), f'<div class="capg">{g}</div><div class="rs2">{note}</div>', PACK)
cap('AT19', 'AT19', 'Páginas reales del griego (Otto 1857): Legación 10, pp. 46 y 48', [('otto46.png', '<b>Otto, <i>Athenagorae… opera</i> (Jena 1857), p. 46</b> · oro «el Hijo de Dios es el Verbo del Padre en idea y en operación»; azul «el Hijo en el Padre y el Padre en el Hijo, por unidad y poder de espíritu, mente y razón del Padre»; rojo «primer engendrado… no como hecho… mente eterna…»; verde «idea y fuerza operante… habiendo salido». Abajo, la nota 9 de Otto sobre «espíritu» = esencia divina.'), ('otto48.png', '<b>p. 48</b> · oro «el Espíritu Santo… efusión (<i>apórroia</i>) de Dios, que fluye y vuelve como un rayo del sol»; azul «Dios Padre, y Dios Hijo, y Espíritu Santo, mostrando su poder en la unión y su distinción en el orden». Abajo, las notas de Otto (Prov 8:22, Dorner).')],
    'Son las páginas del escaneo abierto de archive.org (reimpresión de Sändig); el griego se identifica con la imagen y no con el OCR. El subrayado es mío.', 'Otto 1857, escaneo abierto; subrayado mío')
cap('AT20', 'AT20', 'Páginas reales: Otto p. 124 (griego de Leg. 24) y ANF pp. 133 y 141 (inglés)', [('otto124.png', '<b>Otto 1857, p. 124</b> · Leg. 24: azul «<i>henoúmena mèn katà dýnamin</i>», «unidos en poder»; oro «Dios, y su Hijo el Verbo, y Espíritu Santo… el Hijo mente, razón, sabiduría del Padre, y el Espíritu efusión como luz del fuego».'), ('anf147.png', '<b>ANF vol. 2, p. 133</b> · Leg. 9-10 en inglés: «en idea y en operación», «el primer producto del Padre», «una efusión de Dios… como un rayo del sol», «su poder en la unión y su distinción en el orden».'), ('anf155.png', '<b>ANF p. 141</b> · Leg. 24: <b>«united in essence»</b> (azul): no está en el griego impreso, que dice «en poder».')],
    'La página 141 de la ANF muestra lo que traduce Pratten («unidos en esencia»); la página 124 de Otto muestra lo que dice el griego («unidos en poder»). Las notas de los editores de la ANF son del siglo XIX. El subrayado es mío.', 'Otto 1857 y ANF vol. 2 (Buffalo 1885), escaneos abiertos; subrayado mío')
body = '''<div class="two"><div class="pn"><h4>Método</h4><ul class="l" style="font-size:15px;line-height:1.45">
<li>Once investigadores (modelo pequeño): A1 Leg. 1-9; A2 Leg. 10; A3 Leg. 10-12; A4 Leg. 13-23; A5 Leg. 24-27 (ángeles); A6 Leg. 28-37; A7 <i>Sobre la resurrección</i>; A8 escaneos y griego; A9 estudiosos; A10 metafísica; A11 recepción y paralelos. Encargos y datos en <code>herramientas/</code>. Un corte por límite de uso detuvo a ocho de ellos; los retomé y terminaron.</li>
<li><b>Yo comprobé</b> en imagen de página: Otto 1857 pp. 46, 48 y 124 (griego) y ANF pp. 133 y 141 (inglés). El resto del griego lo leyeron los investigadores en el escaneo de Otto (marcado en cada cita; algunos sólo por OCR).</li>
<li>Traducciones al español mías, desde el griego cuando se muestra, desde el inglés cuando sólo hay inglés.</li></ul></div>
<div class="pn"><h4>Correcciones y negativos</h4><ul class="l" style="font-size:14.5px;line-height:1.42">
<li>«Unidos en esencia» (Leg. 24, ANF) <b>no está en el griego</b>: es conjetura de Gesner que Otto rechaza.</li>
<li>«Unidad y poder de espíritu» (10.2): Otto, Clerc, Marano y Dorner leen «espíritu» como la esencia divina; Bull, como el Espíritu Santo.</li>
<li>No hay «Jesús», «Cristo» (sólo «cristianos»), «Trinidad/tríada» ni «consustancial» en las dos obras.</li>
<li>Eusebio no nombra a Atenágoras (HE 1-9); la noticia de Felipe de Side es del siglo V; Focio (cód. 234) y Epifanio (Haer. 64), sin leer.</li>
<li><i>Sobre la resurrección</i>: sin doctrina trinitaria; Grant (1954) discute su autoría, según un resumen que sólo leí por WebFetch.</li>
<li>No pude abrir Prestige, Kelly, Barnard, Grant, Behr ni Schoedel (restringidos); Migne PG 6 (700 MB) no se capturó.</li>
<li>Una instrucción de un investigador fue bloqueada por el clasificador del entorno (imprimía la configuración del proxy); la dejó y no la reintentó.</li></ul></div></div>'''
card('AT21', hdr('AT21', 'Fuentes y límites', 'Resumen', 'Qué se leyó, qué se corrigió y qué no se pudo comprobar', 'Resumen honesto del método y sus límites'), body, FOOT)
print('atgen ok', len(S))
