# -*- coding: utf-8 -*-
# Diapositivas generales: IS00 (resumen con fotos), IS11 e IS12 (conclusiones para TikTok) e IS99 (fuentes y límites)
import sys, os
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ig')
import igpad
import hbcss
from hbcss import E, marks, page
import genpad
from igdata import FIGS
OUT = igpad.OUT; PACK = igpad.PACK; tags = igpad.tags
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- IS00
ROWS = {
 'IS01': ('Sobre las herejías, cap. 101 (c. 743)', 'La religión de los ismaelitas «es precursora del Anticristo»; Mamed «fundó una herejía propia» tras tratar con «un monje arriano».'),
 'IS02': ('Summula y carta sobre su traducción (c. 1143)', 'El «miserabilísimo e impiísimo» Mahoma entregó a casi la tercera parte del género humano «al diablo y a la muerte eterna»; su Corán, hecho de «fábulas judías» y «sandeces de herejes».'),
 'IS03': ('Bula «Quia maior» (1213)', 'Mahoma, «un hijo de perdición, el falso profeta», apartó de la verdad a muchos «por medio de halagos mundanos y placeres carnales».'),
 'IS04': ('Suma contra los Gentiles I, 6 (c. 1259–65) y Super I Cor 15', 'Atrajo con placeres carnales y mezcló verdades con «fábulas y doctrinas falsísimas»; sin milagros, «dijo ser enviado con el poder de las armas»: señal de ladrones y tiranos.'),
 'IS05': ('Contra la ley de los sarracenos (c. 1300)', '«Un dragón diabólico» que compuso «una ley mentirosísima y nefanda»; «precursor del Anticristo»; en él vomitó el diablo «las heces de todos los herejes antiguos».'),
 'IS06': ('Divina Comedia, Infierno XXVIII (c. 1308–21)', 'Lo coloca en el Infierno, mutilado, entre los «sembradores de escándalo y de cisma».'),
 'IS07': ('Cribado del Corán (c. 1460–61)', 'Buscó «el poder de dominar bajo pretexto de religión»; ignora «qué es Cristo»; sugiere que lo engañaron informantes judíos.'),
 'IS08': ('Carta a Mehmed II (c. 1461)', 'Toda su ley es «artificiosa y fraudulenta»; su paraíso, de comida y mujeres; se extendió porque «sus cimientos se echaron en el placer».'),
 'IS09': ('El triunfo de la Cruz IV, 7 (c. 1497)', 'Mahoma «ordenó con astucia que su religión no se defendiera sino con la espada»; «cuán estúpidamente se contradice» en el Corán.'),
 'IS10': ('Sobre la verdad de la fe cristiana IV (1543)', 'Mahoma: «un mero hombre», «muerto y putrefacto»; su religión se apoya en las armas, y Dios no las necesita.'),
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
<div class="ans" style="margin-top:16px"><b>Quién habla.</b> Dos Doctores de la Iglesia (Juan Damasceno, Santo Tomás), dos papas (Inocencio III, Pío II), un cardenal (Nicolás de Cusa), un abad de Cluny, dos dominicos (Riccoldo, Savonarola), el poeta Dante y el humanista Vives: <b>diez figuras católicas, del siglo VIII al XVI</b>, sin ningún protestante. Cada una tiene su diapositiva de cita (ISxx 1/2) y su diapositiva de obra y fuente (ISxx 2/2).</div>'''
page(OUT, 'IS00_es', 'IS00', 'La Iglesia ante el Islam', 'Resumen en español',
     'La Iglesia ante el Islam, siglos VIII–XVI: lo que dijeron diez figuras católicas',
     'Citas traducidas al español, con su obra, su fuente y qué quiere decir cada una. Retratos de dominio público (iconografía, no retratos en vida).', body,
     'Las citas entre comillas son de mi traducción al español; el texto de partida y la aclaración de cada una están en las diapositivas ISxx. Fechas aproximadas.<br>' + PACK, head_cls='alt')

# ---------------------------------------------------------------- IS11 / IS12 (conclusiones)
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
<div class="top"><div class="who"><b>{fname[:4]}</b>Veredicto de la Iglesia medieval<i>{n}/2 · diez figuras, ocho siglos</i></div></div>
<div class="mid">{blocks}</div>
<div class="nota">Cada punto resume lo que dijo cada autor (códigos IS01–IS10). Son juicios de teólogos, papas y poetas medievales, no hallazgos de la historiografía actual. Traducciones al español mías.</div>
<div class="ft2"><span>{PACK}</span><span>{fname[:4]} · {n}/2</span></div></div></body></html>'''
    open(f'{OUT}/{fname}.html', 'w', encoding='utf-8').write(h)

concl('IS11_es', 1, [
 ('1', 'Ninguno de los diez lo reconoce como profeta.',
  'Falso profeta e «hijo de perdición» (Inocencio III). Fundador de «una herejía propia» (Juan Damasceno). Impostor que buscó «dominar bajo pretexto de religión» (Cusa). Cismático mutilado en el Infierno (Dante). «Un mero hombre», «muerto y putrefacto» (Vives).',
  ['IS03', 'IS01', 'IS07', 'IS06', 'IS10']),
 ('2', 'El Corán no vino del cielo: lo armó él.',
  '«Fábulas judías» y «sandeces de herejes» (Pedro el Venerable). «Composiciones dignas de risa» (Juan Damasceno). «Una ley mentirosísima y nefanda» (Riccoldo). Verdades mezcladas con «fábulas y doctrinas falsísimas» (Santo Tomás). «Artificiosa y fraudulenta» (Pío II).',
  ['IS02', 'IS01', 'IS05', 'IS04', 'IS08']),
 ('3', 'Sin milagros: con espada y con placeres.',
  '«Dijo ser enviado con el poder de las armas» (Santo Tomás). «Placeres carnales» (Inocencio III). «Sus cimientos se echaron en el placer» (Pío II). «Lo resuelves todo en la espada» (Cusa). «Con amenazas y con la espada» (Savonarola).',
  ['IS04', 'IS03', 'IS08', 'IS07', 'IS09']),
 ('4', 'Dios no necesita espadas: el éxito no prueba nada.',
  '«¿Qué necesidad tiene de armas?» (Vives). Con ese criterio, dice Savonarola, el diablo sería mejor que Cristo. Los apóstoles convencieron «muriendo»; Mahoma, «por la fuerza de las armas» (Santo Tomás).',
  ['IS10', 'IS09', 'IS04']),
])
concl('IS12_es', 2, [
 ('5', 'Niega lo esencial: Cristo y la Trinidad.',
  'Para Juan Damasceno, Cristo es solo «criatura y siervo». Riccoldo: «niega la Trinidad» con Sabelio y rebaja a Cristo como Arrio. Cusa: «qué es Cristo, lo ignoras por completo».',
  ['IS01', 'IS05', 'IS07']),
 ('6', '«Precursor del Anticristo».',
  'Juan Damasceno (siglo VIII) lo dice de la religión de los ismaelitas; Riccoldo (hacia 1300), de Mahoma: «Este Mahoma fue precursor del Anticristo». Inocencio III lo llama «hijo de perdición», título bíblico del Anticristo (2 Tes 2,3).',
  ['IS01', 'IS05', 'IS03']),
 ('7', 'No hablaban de oídas.',
  'Pedro el Venerable encargó la primera traducción latina del Corán (c. 1143); Riccoldo escribió su refutación, capítulo a capítulo, tras vivir entre musulmanes; Cusa dedicó una obra entera a «cribar» el Corán.',
  ['IS02', 'IS05', 'IS07']),
 ('8', 'Dos Doctores de la Iglesia, dos papas y un cardenal.',
  'Juan Damasceno y Santo Tomás (Doctores de la Iglesia); Inocencio III y Pío II (papas); Nicolás de Cusa (cardenal); Pedro el Venerable (abad de Cluny); Riccoldo y Savonarola (dominicos); Dante y Vives (un poeta y un humanista católicos). [[k:Diez voces católicas, ocho siglos.]]',
  ['IS01', 'IS04', 'IS03', 'IS08', 'IS07']),
])

# ---------------------------------------------------------------- IS99
body = '''<div class="two">
<div class="pn"><h4>Qué leí y cómo se comprobó</h4><ul class="l" style="font-size:17px">
<li>Ocho investigadores (modelo pequeño) buscaron los textos. <b>Yo elegí las diez figuras y las citas</b> y comprobé cada una contra su fuente: texto digitalizado de Migne, Parma, Marietti o Wikisource, y, en Riccoldo, Pío II, Cusa y Savonarola, contra la imagen de la página.</li>
<li>Los códigos de página y las direcciones están en la diapositiva «obra» (ISxx 2/2) de cada figura.</li>
<li>Latín y griego de ediciones antiguas, a veces con errores de digitalización; las dudas están en la aclaración de la cita (por ejemplo, «σκεῖα» en Juan Damasceno).</li>
<li>Retratos de Wikimedia Commons: iconografía, no retratos en vida.</li>
</ul></div>
<div class="pn"><h4>Límites y qué quedó fuera</h4><ul class="l" style="font-size:17px">
<li><b>Traducciones al español mías.</b> Solo Aquino (1923), Dante (Longfellow, 1867) y Savonarola (Procter, 1901, desde el italiano) tienen traducción inglesa de dominio público; no hay otra que haya leído.</li>
<li><b>Fuera</b>: los pasajes que piden matar o hacer la guerra, y los insultos a pueblos enteros. Los cortes dentro de una cita van marcados con […] y la aclaración dice qué omito.</li>
<li><b>Solo figuras católicas</b>, como se pidió: sin protestantes.</li>
<li>Muchas de estas afirmaciones medievales son <b>polémica sin fuentes árabes</b> (la historia del monje arriano, por ejemplo); aquí se citan como lo que dijo cada autor.</li>
<li>Son juicios históricos de cada autor, <b>no la enseñanza actual de la Iglesia</b> (<i>Nostra aetate</i> 3 y Catecismo, n. 841).</li>
</ul></div></div>'''
page(OUT, 'IS99_es', 'IS99', 'Fuentes, límites y avisos', 'Resumen en español',
     'Qué leí, qué dejé fuera y qué hay que tener en cuenta',
     'Resumen honesto del método y de sus límites.', body,
     'Fuentes: archive.org (Migne PL/PG, Parma, Marietti, 1608, 1544, incunable de Florencia), Herzog August Bibliothek Wolfenbüttel, Universitätsbibliothek Paderborn, Wikisource, Project Gutenberg, Wikimedia Commons.<br>' + PACK, head_cls='alt')
print('igstatic ok')
