# -*- coding: utf-8 -*-
import sys, os, re, shutil, html
TQ = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/tq'
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb')
sys.path.insert(0, TQ)
import hbcss, genpad
from hbcss import E
from tqdata import S
OUT = TQ + '/tqcards'
os.makedirs(OUT + '/img', exist_ok=True)
PACK = 'Pack «Tertuliano, trinitario: una sustancia, tres personas»'
CSS = hbcss.CSS + genpad.CQ + """
.lq{border:1px solid #d6dbe4;border-radius:10px;margin:0 0 12px;background:#fff;overflow:hidden}
.lq .la{font-family:'Bitstream Charter','DejaVu Serif',serif;font-style:italic;font-size:16.5px;line-height:1.5;color:#2f3a52;background:#f6f4ec;padding:10px 16px;border-bottom:1px solid #e3e7ee}
.lq .la.en{font-style:normal;font-family:'Inter',sans-serif;font-size:15.5px}
.lq .es{font-size:18px;line-height:1.52;padding:10px 16px;color:#1b2333}
.lq .rf{font-size:13px;color:#566079;padding:6px 16px;background:#eef1f8;line-height:1.4}
.lq .rf b{color:#14213d}
.lq .lg{font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;font-weight:700;color:#8a6d00;margin-right:6px}
.lq .lg.en{color:#1d5f9a}
.rs2{border-left:6px solid #14213d;background:#eef1f8;padding:13px 20px;border-radius:0 8px 8px 0;font-size:16.5px;line-height:1.55;margin-top:8px}
.rs2 b{color:#14213d}
.capg{display:flex;gap:14px;align-items:flex-start}
.capg .c{flex:1;min-width:0;border:1px solid #cfd6e2;border-radius:8px;overflow:hidden;background:#fff}
.capg img{width:100%;display:block}
.capg .t{font-size:12.5px;line-height:1.4;color:#2f3a52;padding:6px 10px;background:#f4f5f8}
"""
def hdr(cid, tag, kind, title, ref):
    return f'''<div class="hd alt"><div class="row"><div class="badge"><b>{cid}</b>{tag}</div><span class="kind es">{kind}</span></div><h1>{title}</h1><div class="row"><div class="ref">{ref}</div></div></div>'''
def card(fname, head, body, foot):
    h = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="card">{head}<div class="bd">{body}</div><div class="ft"><div class="u">{foot}</div></div></div></body></html>'
    open(f'{OUT}/{fname}.html', 'w', encoding='utf-8').write(h)
def qhtml(q):
    lg = 'Inglés (original)' if q['lang'] == 'en' else 'Latín'
    cls = 'la en' if q['lang'] == 'en' else 'la'
    return f'''<div class="lq"><div class="{cls}"><span class="lg {'en' if q['lang']=='en' else ''}">{lg}</span>{E(q["lat"])}</div><div class="es"><span class="lg" style="color:#1d7a4f">Español</span> {E(q["es"])}</div><div class="rf"><b>{E(q["ref"])}</b> · {E(q["src"])} · <span style="color:#8a93a6">{q["id"]}</span></div></div>'''
def ri(t):
    return t
for s in S:
    body = ''.join(qhtml(q) for q in s['quotes']) + f'<div class="rs2">{s["res"]}</div>'
    card(s['id'], hdr(s['id'], 'Tertuliano', 'Cita y resolución', s['title'], s['sub']), body,
         PACK + '<br>Latín tomado de Kroymann (CSEL 47), Migne o la Latin Library, según se indica; traducciones al español mías. Itálicas en el latín = original; donde se cita en inglés se dice.')

# ---- capturas
def cap_slide(fn, cid, title, items):
    g = ''
    for i, (img, t) in enumerate(items):
        dst = f'{OUT}/img/{cid}_{i}.png'; shutil.copy(TQ + '/cap/' + img, dst)
        g += f'<div class="c"><img src="img/{cid}_{i}.png"><div class="t">{t}</div></div>'
    card(fn, hdr(cid, 'Páginas reales', 'Capturas', title, 'Edición crítica de Kroymann (CSEL 47, Viena 1906), escaneo abierto de archive.org; subrayado mío'),
         f'<div class="capg">{g}</div><div class="rs2">Las páginas son las del escaneo de Kroymann (OCR con errores, p. ej. «graclu» por «gradu»): el texto subrayado se identifica con la imagen, no con el OCR. La numeración es la impresa en la página (CSEL 47).</div>',
         PACK)
cap_slide('TQ14', 'TQ14', 'Las páginas: unidad de sustancia y «portio»', [
 ('k230.png', '<b>CSEL 47, p. 230</b> · Adv. Prax. 2.4: «tres autem non statu, sed gradu… unius autem substantiae»'),
 ('k239.png', '<b>p. 239</b> · Adv. Prax. 8.7 (azul) y 9.2 (oro): «secundus… tertius…» y «pater enim tota substantia est, filius uero deriuatio totius et portio»'),
 ('k246.png', '<b>p. 246</b> · Adv. Prax. 12.3: «personae, non substantiae nomine, ad distinctionem, non ad diuisionem»')])
cap_slide('TQ15', 'TQ15', 'Las páginas: «dos dioses», «unidad de sustancia», el Espíritu y Hermógenes', [
 ('k248.png', '<b>CSEL 47, p. 248</b> · Adv. Prax. 13.6: «duos tamen deos et duos dominos nunquam ex ore nostro proferimus»'),
 ('k276.png', '<b>p. 276</b> · Adv. Prax. 25.1: «ad substantiae unitatem non ad numeri singularitatem»'),
 ('k288.png', '<b>p. 288</b> · Adv. Prax. 30: «tertium nomen diuinitatis et tertium gradum maiestatis»'),
 ('k129.png', '<b>p. 129</b> · Adv. Herm. 3.4: «fuit autem tempus cum et delictum et filius non fuit» (pasaje duro)')])

# ---- TQ00
rows = [
 ('«Hubo un tiempo en que no existían el pecado ni el Hijo» (Adv. Herm. 3.4)', 'No se resuelve del todo', 'Lenguaje pre-niceno; relativo («Padre/Juez» son nombres de relación). El Verbo está en Dios antes (Prax. 5), pero Tertuliano fecha el nacimiento perfecto del Hijo en la creación. Nicea lo corrige (generación eterna).', 'TQ07 · TQ08 · TQ13'),
 ('«El Hijo, derivación y porción del todo» (Prax. 9.2)', 'Se explica, con imprecisión', 'En el mismo texto: «no por división sino por distinción»; «no se separa la sustancia sino que se extiende» (Apol. 21.12). Bull, Hilario, Atanasio y Aquino: Dios no tiene partes.', 'TQ09 · TQ10'),
 ('«El Padre es mayor», «segundo», «vicario» (Prax. 9, 19, 24)', 'Se explica', 'Subordinación económica y de origen («nec statu sed gradu», 19.7), no de naturaleza; sigue sonando subordinacionista.', 'TQ11'),
 ('«Natividad perfecta» del Verbo en la creación (Prax. 7.1)', 'Parcial', 'Distingue Razón eterna y Verbo proferido; Nicea separa generación eterna y manifestación.', 'TQ12'),
 ('Tres personas, una sustancia, Hijo y Espíritu divinos', 'Sí, claramente', '«unius substantiae», «tres… non statu sed gradu», «tertium nomen divinitatis», «trinitas unius divinitatis».', 'TQ01–TQ06'),
]
rh = ''.join(f'<tr><td style="font-weight:700">{a}</td><td class="{"v1" if "Sí" in b or "Se explica" == b else ("v3" if "No se" in b else "v2")}" style="font-weight:700;white-space:normal">{b}</td><td style="font-size:15px">{c}</td><td style="font-weight:700;white-space:nowrap;font-size:14px">{d}</td></tr>' for a, b, c, d in rows)
body = f'''<style>.v1{{color:#1d7a4f}}.v2{{color:#9a6a00}}.v3{{color:#b44a2f}}</style>
<div class="ans"><b>Veredicto honesto.</b> Tertuliano es <b>trinitario en sustancia</b>: afirma una sola sustancia (<i>unius substantiae</i>), tres que se distinguen realmente (Padre, Hijo, Espíritu), la divinidad de los tres y la fórmula bautismal; usa <i>trinitas</i> y <i>persona</i> con este sentido (en <i>Adv. Prax.</i> 2 aparece por primera vez «trinitas» en ese tratado). <b>No es arriano</b>: el Hijo no es criatura. Pero su lenguaje sobre <b>cómo</b> el Hijo procede del Padre (derivación, porción, nacimiento en la creación, «hubo un tiempo…») es <b>preniceno</b> y la tradición posterior lo precisó. Defenderlo no exige negar ese lenguaje: exige explicarlo.</div>
<table class="v" style="table-layout:fixed;margin-top:8px"><tr><th style="width:290px">Pasaje difícil</th><th style="width:150px">¿Se resuelve?</th><th>Cómo</th><th style="width:130px">Diapositivas</th></tr>{rh}</table>
<div class="two" style="margin-top:12px"><div class="pn"><h4>Qué se leyó</h4><ul class="l" style="font-size:15px;line-height:1.45"><li>Latín de <i>Adv. Prax.</i> y <i>Adv. Herm.</i> en las páginas de Kroymann (CSEL 47) y en Migne; inglés de la ANF.</li><li>Bull (<i>Defensio</i>, p. 193 y 200) y Kaye (nota de la ANF), en PDF abierto.</li></ul></div>
<div class="pn"><h4>Qué no se leyó</h4><ul class="l" style="font-size:15px;line-height:1.45"><li>Kelly, Evans, Osborn, Barnes, Daniélou, Moingt, Hanson: sin texto abierto; no los cito.</li><li>Los griegos (Atanasio) y el latín de Hilario y Aquino: solo la versión inglesa (newadvent).</li></ul></div></div>'''
card('TQ00', hdr('TQ00', 'Tertuliano · mapa', 'Resumen', '¿Era trinitario Tertuliano? Qué dice, qué es difícil y qué se resuelve', 'Obras: Adversus Praxean, Adversus Hermogenem, Apologeticum, De Praescriptione, De Pudicitia, De Baptismo'), body, PACK)

# ---- TQ99
body = '''<div class="two"><div class="pn"><h4>Método</h4><ul class="l" style="font-size:15.5px;line-height:1.45">
<li>Once investigadores (modelo pequeño): T1-T5 recorrieron <i>Adversus Praxean</i> por capítulos; T6 el Espíritu y «trinitas»; T7 <i>Adversus Hermogenem</i>; T8 otras obras y reglas de fe; T9 estudiosos; T10 metafísica nicena y tomista; T11 escaneos y páginas. Sus encargos y datos están en <code>herramientas/</code>.</li>
<li><b>Yo comprobé</b> el latín de cada cita mostrada contra los textos (Kroymann, Migne, Latin Library) con un programa, y vi en la imagen de la página los pasajes de las capturas TQ14-TQ15.</li>
<li>El latín está en la ortografía de su fuente; los términos griegos (<i>oikonomía</i>, <i>probolḗ</i>) los restituyo. Las traducciones al español son mías, hechas desde el latín o, donde se dice, desde el inglés.</li></ul></div>
<div class="pn"><h4>Correcciones y negativos que importa saber</h4><ul class="l" style="font-size:15px;line-height:1.45">
<li>El «Deum de Deo» no está en <i>Apol.</i> 21 (solo en <i>Ad Nat.</i> 2.3); el «alius, non aliud» no aparece en <i>Adv. Prax.</i> 13-25 ni en el latín que pude leer; «Spiritus tertius» está en <i>Prax.</i> 8.7, no en el 25.</li>
<li>Bautismo trino: <i>De Baptismo</i> 13.3 (no 6 y 8); triple inmersión: <i>De Corona</i> 3.3; Espíritu en <i>Scorp.</i> 9.3 (no 10).</li>
<li>Kroymann marca como posible interpolación el final del cap. 3 de <i>Adv. Prax.</i> y corchetea «oportebat et patrem crucifigi» (cap. 10): no los uso.</li>
<li>«Cum et delictum» (Kroymann) frente a «cum ei delictum» (Latin Library) en <i>Adv. Herm.</i> 3.4: el sentido no cambia.</li>
<li>Páginas de la ANF impresa: no las vi; la ANF digital tiene otra paginación. Cito capítulo y sección.</li>
<li>No pude leer Kelly, Evans, Osborn, Barnes, Daniélou, Moingt ni Hanson.</li></ul></div></div>'''
card('TQ99', hdr('TQ99', 'Fuentes y límites', 'Resumen', 'Qué se leyó, qué se corrigió y qué no se pudo comprobar', 'Resumen honesto del método y de sus límites'), body, PACK)
print('tqgen ok')
