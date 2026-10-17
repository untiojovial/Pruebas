# -*- coding: utf-8 -*-
# Diapositivas generales: OI00 (resumen con fotos), OI11 e OI12 (conclusiones para TikTok) y OI99 (fuentes y límites)
import sys, os
OX = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ox'
sys.path.insert(0, OX)
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb')
import oxpad
import hbcss
from hbcss import E, marks, page
import genpad
from oxfigs import FIGS
OUT = oxpad.OUT; PACK = oxpad.PACK; tags = oxpad.tags
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- OI00
ROWS = {
 'OI01': ('Panoplia dogmática, tít. 28 «Contra los sarracenos» (c. 1100–1118)', 'Mahoma, «falso profeta»; su Corán son «fabulillas» que equivalen a «sacar el estiércol de Augías»; el Corán haría que Cristo «mintió ante Dios».'),
 'OI02': ('Epítome de historias XIV, 17 (c. 1118–1140)', 'Un hombre pobre y «malvado» al que un monje desterrado enseñó a fingir revelaciones: «aquel hombre abominable se ganó entre los suyos el nombre de profeta»; impuso su ley «blandiendo la espada».'),
 'OI03': ('Anales, parte IV (c. 1150–1165)', '«El falso profeta Mahoma», avalado por «un monje arriano que daba falso testimonio»; de judíos, arrianos y nestorianos tomó «una religión propia».'),
 'OI04': ('Historia, libro VII (c. 1206–1217)', 'Defiende el «anatema contra el Dios de Mahoma» en la fórmula de bautismo: «el delirante y demoníaco Mahoma», «los desechables desvaríos de Mahoma»; lo suyo, «no diría teología».'),
 'OI05': ('Cuatro discursos contra Mahoma, I y IV (c. 1355–1370)', 'Su ley viene de «su padre, el diablo»; lo que inventó sobre su nombre es «una mentira clarísima»; «el diablo es homicida, y Mahoma condenó a muerte a quienes no obedecían sus leyes».'),
 'OI06': ('Carta desde el cautiverio a su Iglesia (1354)', 'Sin testimonio de los profetas: «no creemos en él, ni en el libro que dejó»; conquistó «con guerra, espada, saqueo, esclavización y matanzas», voluntad «del homicida desde el principio».'),
 'OI07': ('Diálogo con un persa, VII (c. 1391–1392)', 'De todas las leyes, «la de Mahoma es la peor»; «solo encontrarás cosas malas o inhumanas», como mandar que su fe «se propague por la espada».'),
 'OI08': ('Diálogo contra todas las herejías, cap. 14 (c. 1400–1429)', 'Mahoma «se llamó a sí mismo apóstol de Dios»; dijo haber visto a Dios «de cristal»; sus seguidores son «del todo ateos» porque «rechazan al Hijo y Verbo de Dios».'),
 'OI09': ('Dos discursos contra Mahoma (antes de 1525)', '«El abominable Mahoma es precisamente el falso profeta» del Apocalipsis y «el precursor del anticristo»; en «su maldito libro» introduce «por todas partes leyes contrarias» al Evangelio.'),
 'OI10': ('Crónica mayor III, 10 y IV, 3 (c. 1573–75)', '«Falso profeta y anticristo», «iluminado en las cosas de las tinieblas por su padre Satanás»; sin testimonio de la Escritura, «no ha sido enviado por Dios».'),
}
tr = ''
for f in FIGS:
    th = []
    for q in f['quotes']:
        for t in q['theme']:
            if t not in th: th.append(t)
    obra, dice = ROWS[f['id']]
    tr += (f'<tr><td class="who" style="white-space:normal"><div style="display:flex;align-items:center;gap:2px"><img class="av" src="img/{f["slug"]}.jpg" style="flex:none"><div>{E(f["name"])}<br><span style="font-weight:500;color:#566079;font-size:13.5px">{E(f["dates"])} · {f["id"]}</span></div></div></td>'
           f'<td style="font-size:15px">{E(obra)}</td><td>{E(dice)}</td><td style="line-height:2">{tags(th)}</td></tr>')
body = f'''<table class="v" style="table-layout:fixed"><tr><th style="width:250px">Figura</th><th style="width:185px">Obra</th><th>Qué dice de Mahoma y del Islam</th><th style="width:205px">Tema</th></tr>{tr}</table>
<div class="ans" style="margin-top:16px"><b>Quién habla.</b> Dos emperadores (Juan VI Cantacuceno, Manuel II Paleólogo), tres santos de la Iglesia Ortodoxa (Gregorio Palamás, Simeón de Tesalónica, Máximo el Griego), un monje teólogo (Eutimio Zigabeno), un monje y canonista (Zonaras), un secretario imperial (Glicas), un alto funcionario (Coniates) y un metropolitano (Macario Melisseno): <b>diez figuras ortodoxas, de c. 1100 a 1585</b>, todas posteriores al Cisma de 1054 y sin Juan Damasceno. Cada una tiene su diapositiva de cita (OIxx 1/2) y su diapositiva de obra y fuente (OIxx 2/2).</div>'''
page(OUT, 'OI00_es', 'OI00', 'La Iglesia Ortodoxa ante el Islam', 'Resumen en español',
     'La Iglesia Ortodoxa ante el Islam, 1084–1700: lo que dijeron diez figuras',
     'Citas traducidas al español, con su obra, su fuente y qué quiere decir cada una. Retratos y miniaturas de dominio público (iconografía, no retratos en vida).', body,
     'Las citas entre comillas son de mi traducción al español; el texto de partida y la aclaración de cada una están en las diapositivas OIxx. Fechas aproximadas.<br>' + PACK, head_cls='alt')

# ---------------------------------------------------------------- OI11 / OI12 (conclusiones)
CC = """
.cc{display:flex;gap:28px;padding:22px 0 24px;border-top:1px solid rgba(215,201,163,.28)}
.cc:first-child{border-top:none;padding-top:6px}
.cc .nn{font-family:'Inter',sans-serif;font-size:76px;font-weight:800;color:#fca311;line-height:.95;min-width:64px}
.cc .tx{flex:1}
.cc h3{font-family:'Inter',sans-serif;font-size:37px;line-height:1.16;font-weight:800;color:#fff;margin:0 0 10px;letter-spacing:-.01em}
.cc p{font-family:'Bitstream Charter','DejaVu Serif',serif;font-size:21.5px;line-height:1.5;color:#d9e0f2;margin:0}
.cc p b{color:#ffcf6b;font-weight:700}
.cc p mark{background:none;color:#ffcf6b;text-decoration:underline;text-decoration-color:rgba(252,163,17,.75);text-decoration-thickness:3px;text-underline-offset:5px;padding:0}
.cc .by{font-family:'Inter',sans-serif;font-size:13.5px;letter-spacing:.06em;text-transform:uppercase;color:#9fb0d4;margin-top:9px}
.cc .by span{background:#fca311;color:#14213d;border-radius:5px;padding:1px 7px;margin-right:5px;font-weight:700;letter-spacing:.02em}
.qs .nota{margin-top:16px;font-family:'Inter',sans-serif;font-size:14.5px;line-height:1.45;color:#aab6d6;border-top:1px solid rgba(215,201,163,.28);padding-top:12px}
"""
def concl(fname, n, items):
    blocks = ''
    for num, head, txt, codes in items:
        cd = ''.join(f'<span>{c}</span>' for c in codes)
        blocks += f'<div class="cc"><div class="nn">{num}</div><div class="tx"><h3>{E(head)}</h3><p>{marks(txt)}</p><div class="by">Lo dijeron {cd}</div></div></div>'
    h = f'''<!doctype html><html><head><meta charset="utf-8"><style>{hbcss.CSS}{genpad.CQ}{CC}</style></head><body><div class="qs">
<div class="top"><div class="who"><b>{fname[:4]}</b>Veredicto de la Iglesia Ortodoxa<i>{n}/2 · diez figuras, casi cinco siglos</i></div></div>
<div class="mid">{blocks}</div>
<div class="nota">Cada punto resume lo que dijo cada autor (códigos OI01–OI10). Son juicios de monjes, emperadores, historiadores y obispos bizantinos y postbizantinos, no hallazgos de la historiografía actual; parte de lo que cuentan (el monje, la epilepsia) es leyenda polémica. Traducciones al español mías.</div>
<div class="ft2"><span>{PACK}</span><span>{fname[:4]} · {n}/2</span></div></div></body></html>'''
    open(f'{OUT}/{fname}.html', 'w', encoding='utf-8').write(h)

CONCL1 = [
 ('1', 'Ninguno de los diez lo reconoce como profeta.',
  '«Falso profeta» (Zigabeno, Glicas). «Falso profeta y anticristo» (Melisseno). «El abominable Mahoma es precisamente el falso profeta» del Apocalipsis (Máximo el Griego). Ni los profetas lo atestiguan: «no creemos en él, ni en el libro que dejó» (Palamás).',
  ['OI01', 'OI03', 'OI10', 'OI09', 'OI06']),
 ('2', 'No lo inspiró Dios: lo inspiró el diablo.',
  '«Su padre, el diablo» (Cantacuceno). «Iluminado en las cosas de las tinieblas por su padre Satanás» (Melisseno). Avalado por «un monje arriano que daba falso testimonio» (Glicas) y por «aquel monje embustero» (Zonaras). Su pretendido nombre en la Escritura: «una mentira clarísima» (Cantacuceno).',
  ['OI05', 'OI10', 'OI03', 'OI02']),
 ('3', 'Su ley y su Corán: lo peor.',
  '«La de Mahoma es la peor» de todas las leyes (Manuel II): «solo encontrarás cosas malas o inhumanas». Un libro de «fabulillas» que es como «sacar el estiércol de Augías» (Zigabeno), «su maldito libro» (Máximo el Griego), «los desechables desvaríos de Mahoma» (Coniates).',
  ['OI07', 'OI01', 'OI09', 'OI04']),
 ('4', 'Se impuso con espada, no con milagros.',
  '«Con guerra, espada, saqueo, esclavización y matanzas» (Palamás). «Blandiendo la espada contra quienes no le obedecían con facilidad» (Zonaras). Una fe que «se propague por la espada» (Manuel II). Y en la crónica de Melisseno, la frase que se pone en boca de Mahoma: «no he venido a dar la ley por medio de milagros, sino por medio de la espada».',
  ['OI06', 'OI02', 'OI07', 'OI10']),
]
CONCL2 = [
 ('5', 'Niega a Cristo y a la Trinidad.',
  'Zigabeno: según el Corán, Cristo, que es Dios, «mintió ante Dios». Simeón de Tesalónica: los musulmanes «rechazan al Hijo y Verbo de Dios» y son «del todo ateos». Máximo el Griego: «¿Por qué rechazas su divinidad?». Coniates: el «Dios de Mahoma» que «ni engendró ni fue engendrado».',
  ['OI01', 'OI08', 'OI09', 'OI04']),
 ('6', '«Precursor del anticristo».',
  'Máximo el Griego: Mahoma es «el falso profeta» del Apocalipsis y «el precursor del anticristo». Melisseno lo llama «falso profeta y anticristo». Cantacuceno: «el diablo es homicida, y Mahoma condenó a muerte a quienes no obedecían sus leyes».',
  ['OI09', 'OI10', 'OI05']),
 ('7', 'Lo conocían de primera mano.',
  'Palamás escribió su carta siendo prisionero de los turcos (1354). Manuel II compuso sus diálogos en Ankara, al servicio del sultán Bayaceto, con un docto musulmán (1391). Coniates cuenta cómo se bautizaba a los musulmanes convertidos y qué anatema pronunciaban contra el «Dios de Mahoma».',
  ['OI06', 'OI07', 'OI04']),
 ('8', 'Tres santos, dos emperadores y un metropolitano.',
  'Gregorio Palamás, Simeón de Tesalónica y Máximo el Griego (santos de la Iglesia Ortodoxa); Juan VI Cantacuceno y Manuel II Paleólogo (emperadores); Macario Melisseno (metropolitano); Zigabeno, Zonaras, Glicas y Coniates (monjes, secretario y alto funcionario imperial). [[k:Diez voces ortodoxas, casi cinco siglos.]]',
  ['OI06', 'OI08', 'OI09', 'OI05', 'OI07']),
]
concl('OI11_es', 1, CONCL1)
concl('OI12_es', 2, CONCL2)

# ---------------------------------------------------------------- OI99
body = '''<div class="two">
<div class="pn"><h4>Qué leí y cómo se comprobó</h4><ul class="l" style="font-size:17px">
<li>Once investigadores (modelo pequeño) buscaron los textos. <b>Yo elegí las diez figuras y las citas</b> y comprobé las frases clave contra la imagen de la página: Zigabeno (Migne PG 130), Zonaras (Dindorf), Glicas, Coniates y Melisseno (Bekker, Bonn), Cantacuceno (Basilea, 1543) y Palamás (revista <i>Neos Hellenomnemon</i>, 1922).</li>
<li>Simeón de Tesalónica lo cito desde el latín que Migne imprime junto al griego (texto digitalizado, no la imagen), y Manuel II desde la traducción inglesa de Roger Pearse (2009); Máximo el Griego, desde la traducción rusa de 1910.</li>
<li>Los códigos de página y las direcciones están en la diapositiva «obra» (OIxx 2/2) de cada figura.</li>
<li>Retratos de Wikimedia Commons: iconografía y miniaturas, no retratos en vida; donde no hay retrato libre, la portada de la edición.</li>
</ul></div>
<div class="pn"><h4>Límites y qué quedó fuera</h4><ul class="l" style="font-size:17px">
<li><b>Traducciones al español mías.</b> Del texto de Manuel II no hay griego de dominio público: el griego del diálogo VII solo está en ediciones con derechos (Trapp, Khoury).</li>
<li><b>Fuera</b>: los pasajes que piden matar o hacer la guerra, y los insultos a pueblos enteros. Los cortes dentro de una cita van marcados con […] y la aclaración dice qué omito.</li>
<li><b>Solo figuras ortodoxas posteriores al Cisma</b>: sin Juan Damasceno (ya está en el pack católico), sin católicos convertidos y sin protestantes ni Lucaris.</li>
<li>Las autorías se discuten en dos casos: el texto de Cantacuceno y el libro IV de la <i>Crónica mayor</i> (compilada por Melisseno, con polémica interpolada de autor desconocido); por eso Melisseno es la figura más débil del conjunto.</li>
<li>Muchas de estas afirmaciones son <b>polémica sin fuentes árabes</b> (el monje, la epilepsia); aquí se citan como lo que dijo cada autor.</li>
<li>Son juicios históricos de cada autor, <b>no la posición actual de la Iglesia Ortodoxa</b>.</li>
</ul></div></div>'''
page(OUT, 'OI99_es', 'OI99', 'Fuentes, límites y avisos', 'Resumen en español',
     'Qué leí, qué dejé fuera y qué hay que tener en cuenta',
     'Resumen honesto del método y de sus límites.', body,
     'Fuentes: archive.org (Migne PG 130, 154–155; Bekker, CSHB, Bonn; Dindorf; impreso de Basilea de 1543), <i>Neos Hellenomnemon</i> 16 (1922), azbyka.ru, Roger Pearse (2009), Wikimedia Commons.<br>' + PACK, head_cls='alt')
print('oxstatic ok')
