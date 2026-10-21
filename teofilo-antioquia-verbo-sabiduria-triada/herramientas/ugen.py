# -*- coding: utf-8 -*-
import sys, os, shutil
B = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad'
UG = B + '/ug'; UQ = B + '/uq'
sys.path.insert(0, B + '/hb'); sys.path.insert(0, UG)
import hbcss, genpad
from hbcss import E
from ugdata import S
OUT = UG + '/ugcards'; os.makedirs(OUT + '/img', exist_ok=True)
PACK = 'Pack «Teófilo de Antioquia, ¿trinitario? Verbo, Sabiduría y la primera «Tríada»»'
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
 ('A · «lo engendró… antes de todas las cosas» (2.10, 2.22)', 'Se explica, con límite', 'El texto da «siempre» (aei, dià pantós) al Verbo inmanente; lo que ocurre al crear es la proferencia (manifestación). Nicea: generación eterna. Teófilo no dice «eterna».', 'UG03 · UG09 · UG13'),
 ('B · «Tríada» sin el Espíritu y con un «cuarto» (2.15)', 'Parcial', 'Dios, Verbo, Sabiduría ≈ Padre, Hijo, Espíritu (Ireneo 4.20.3); el cuarto es la criatura. Pero el Espíritu no se nombra y los estudiosos lo anotan.', 'UG05 · UG15'),
 ('C · Verbo = «Espíritu de Dios», «sabiduría» (2.10)', 'Se explica, con límite', 'Títulos del Verbo como agente; en 2.33 el «Espíritu Santo» habla en los profetas. La separación precisa llega en Atanasio y Basilio.', 'UG04 · UG12 · UG15'),
 ('D · «prósōpon del Padre» (2.22)', 'Se explica', 'Sentido teatral (máscara), no modalismo: el Padre es «inabarcable» y el Verbo es «enviado» y «Hijo».', 'UG07 · UG08'),
 ('E · «Dios estaba solo y el Verbo en él» (2.22)', 'Se explica', '«Solo» se opone a criaturas; el Verbo «era Dios» y «estaba junto a Dios».', 'UG10 · UG11'),
 ('F · «como necesitando ayuda» (2.18) y «auxiliar» (2.10)', 'Se explica', 'La «ayuda» es su propio Verbo y su propia Sabiduría («su propia mente y reflexión», 2.22); no un ser ajeno.', 'UG06'),
 ('G · Verbo Hijo, Dios por naturaleza, no criatura', 'Sí', '«ὅς ἐστιν καὶ υἱὸς αὐτοῦ», «Θεὸς… ὁ λόγος καὶ ἐκ θεοῦ πεφυκώς» (2.22): leídos en la imagen de la página de Otto.', 'UG07 · UG10 · UG20'),
]
def cls(v): return 'v1' if v.startswith('Sí') or v == 'Se explica' else ('v3' if v.startswith('No') else 'v2')
for s in S:
    if s['id'] == 'UG19':
        rh = ''.join(f'<tr><td style="font-weight:700;font-size:14.5px">{a}</td><td class="{cls(b)}" style="font-weight:700;white-space:normal">{b}</td><td style="font-size:14px">{c}</td><td style="font-weight:700;white-space:nowrap;font-size:13px">{d}</td></tr>' for a, b, c, d in TABLE)
        body = f'<table class="v" style="table-layout:fixed"><tr><th style="width:300px">Pasaje difícil</th><th style="width:130px">¿Se resuelve?</th><th>Cómo</th><th style="width:140px">Diapositivas</th></tr>{rh}</table><div class="rs2"><b>Conclusión.</b> Teófilo es <b>trinitario «en intención»</b>: habla de tres realidades en Dios (Dios, Verbo, Sabiduría), llama «Tríada» a la tríada, dice que el Verbo es Dios, Hijo y no criatura, y que el Espíritu Santo habló en los profetas. <b>No es un trinitario formulado como Nicea</b>: el Espíritu no está nítido y la generación va ligada a la creación. Defenderlo honestamente es decir esto y explicar el vocabulario del siglo II con la metafísica posterior, no negarlo.</div>'
        card('UG19', hdr('UG19', 'Teófilo · mapa', 'Resumen', s['title'], s['sub']), body, FOOT); continue
    body = ''.join(qhtml(q) for q in s['quotes']) + f'<div class="rs2">{s["res"]}</div>'
    card(s['id'], hdr(s['id'], 'Teófilo', 'Cita y resolución', s['title'], s['sub']), body, FOOT)
def cap(fn, cid, title, items, note, ref):
    g = ''
    for i, (img, t) in enumerate(items):
        shutil.copy(UQ + '/pg/' + img, f'{OUT}/img/{cid}_{i}.png')
        g += f'<div class="c" style="{"flex:0 0 60%" if len(items)==1 else ""}"><img src="img/{cid}_{i}.png"><div class="t">{t}</div></div>'
    card(fn, hdr(cid, 'Páginas reales', 'Capturas', title, ref), f'<div class="capg" style="{"justify-content:center" if len(items)==1 else ""}">{g}</div><div class="rs2">{note}</div>', PACK)
cap('UG20', 'UG20', 'Página real del griego (Otto, 1861): A Autólico 2.22', [('otto118.png', '<b>Otto, <i>Corpus apologetarum</i> vol. 8 (Jena 1861), p. 118</b> · oro: «asumiendo el prósōpon del Padre… en el prósōpon de Dios» · azul: «¿qué otra cosa es la voz sino el Verbo de Dios, que es también su Hijo?» · rojo: «engendró a este Verbo proferido, primogénito de toda la creación, sin quedar vacío del Verbo». Al pie, la nota de Humphry sobre el sentido teatral de prósōpon.')],
    'Es la página del escaneo de archive.org (reimpresión Sändig 1969): el griego se identifica con la imagen, no con el OCR (que falla en griego). El subrayado lo he puesto yo sobre la imagen.', 'Otto 1861, escaneo abierto; subrayado mío')
cap('UG21', 'UG21', 'Páginas reales (ANF vol. 2): 2.10 y 2.22', [('anf225.png', '<b>ANF vol. 2, p. 204</b> · 2.10: «teniendo su propio Verbo interno… lo engendró, emitiéndolo con su sabiduría antes de todas las cosas»; abajo, notas 46 («ἐνδιάθετον») y 47 («literalmente, eructar»).'), ('anf240.png', '<b>p. 219</b> · 2.22: «prosopon», «que es también su Hijo», «engendró este Verbo… proferido» y notas 74-77 (la 74 advierte contra leer «persona» en sentido trinitario posterior).')],
    'Traducción inglesa de Dods tal como está impresa en la ANF (CCEL, PDF abierto, con capa de texto). Las notas al pie son de los editores del siglo XIX (p. ej. Coxe): sus afirmaciones («primer uso», «el espíritu del Concilio de Nicea») son <b>opiniones editoriales</b>, no del texto.', 'ANF vol. 2 (Buffalo 1885), PDF de ccel.org; subrayado mío')
cap('UG22', 'UG22', 'Páginas reales (ANF vol. 2): 1.7, 2.15 y 2.18', [('anf203.png', '<b>p. 182</b> · 1.7: «Dios… por su Verbo y su Sabiduría hizo todas las cosas».'), ('anf233.png', '<b>p. 212</b> · 2.15: «tipos de la Tríada (Trinity)…»; nota 64: «el primer uso de esta palabra».'), ('anf236.png', '<b>p. 215</b> · 2.18: «a ningún otro… sino a su propio Verbo y Sabiduría».')],
    'La nota 64 y la 65 (Kaye) son comentarios editoriales; la tesis «primera vez que se usa Tríada» es de los editores y de estudiosos posteriores (Bethune-Baker, Swete, Robertson).', 'ANF vol. 2 (Buffalo 1885), PDF de ccel.org; subrayado mío')
body = '''<div class="two"><div class="pn"><h4>Método</h4><ul class="l" style="font-size:15px;line-height:1.45">
<li>Once investigadores (modelo pequeño): U1 libro 1; U2 libro 2.1-9; U3 2.10-12; U4 2.13-18; U5 2.19-27; U6 2.28-38 y libro 3; U7 escaneos y griego; U8 estudiosos; U9 metafísica nicena y tomista; U10 paralelos en apologistas; U11 recepción de Teófilo. Sus encargos y datos están en <code>herramientas/</code>.</li>
<li><b>Yo comprobé</b> en la imagen de la página (a) el griego de 2.22 en Otto 1861 y (b) el inglés de 1.7, 2.10, 2.15, 2.18 y 2.22 en la ANF impresa. El griego de 1.7, 2.10, 2.15 y 2.18 viene de la BKV (texto de Grant) y, donde pude, coincide con el OCR de Migne leído por los investigadores; <b>no lo cotejé con imagen</b>.</li>
<li>Las traducciones al español son mías, desde el griego o el latín cuando se muestra, o desde el inglés cuando solo había inglés.</li></ul></div>
<div class="pn"><h4>Correcciones y negativos que importa saber</h4><ul class="l" style="font-size:14.5px;line-height:1.42">
<li>«Primer uso de Tríada»: lo dicen los editores de la ANF, Robertson, Bethune-Baker y Swete; no es un dato que Teófilo diga de sí.</li>
<li>El griego de Teófilo es <i>prósōpon</i>, no «persona»; <i>endiáthetos</i> y <i>prophorikós</i> son de 2.10 y 2.22 (no solo 2.10).</li>
<li>En el libro 2 «Hijo» aparece una vez (2.22).</li>
<li>Atanasio, Basilio, Agustín y Aquino <b>no comentan a Teófilo</b>: son el marco metafísico. Atanasio no usa <i>endiáthetos/prophorikós</i>. Aquino ST I q.27 a.1: solo en inglés.</li>
<li>Los investigadores <b>no hallaron</b> condenas antiguas de Teófilo por herejía (Fócio, Gennadio, decreto Gelasiano: «no encontrado»; Marcelo de Ancira, arrianos y De Synodis: «no hallado»). Es un negativo de búsqueda, no una prueba.</li>
<li>No pude leer Kelly, Prestige, Grant, Behr, Rankin ni Hanson; Migne PG 6 y Otto vol. 8 completo solo como OCR; el PDF de Migne no tiene capa de texto utilizable en griego.</li>
<li>Jerónimo, Ep. 121 (Diatessaron) solo vía enciclopedia: no lo uso.</li></ul></div></div>'''
card('UG23', hdr('UG23', 'Fuentes y límites', 'Resumen', 'Qué se leyó, qué se corrigió y qué no se pudo comprobar', 'Resumen honesto del método y sus límites'), body, FOOT)
print('ugen ok', len(S))
