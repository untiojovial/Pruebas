# -*- coding: utf-8 -*-
# HB04 (resumen de los ocho Padres con foto) y HB09 (fuentes, límites y avisos)
import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb')
from hbcss import *
OUT = 'hbcards'

ROWS = [
 ('P01', 'crisostomo', 'Juan Crisóstomo', 'c. 347–407',
  'Comenta 10:28 como pasado («sufrían el castigo»); el v. 29, para los bautizados que pecan: «excomunión y fuego».',
  'La Ley, «de gran utilidad», no perfecciona (Heb 7:19).',
  '«No es justo dar muerte a un hereje» (Mt, hom. 46).',
  'Admite frenarlos, silenciarlos y disolver sus asambleas.'),
 ('P02', 'agustin', 'Agustín de Hipona', '354–430',
  'Sin pasaje sobre 10:28 en lo reunido.',
  'Un solo Dios: preceptos «menores» (temor) y «mayores» (amor).',
  'Pide que no se ejecute ni mutile a donatistas violentos (Cartas 133 y 139).',
  'Defiende multas, destierro y presión legal; cambió de opinión (Ep. 93 §17); elogia la pena de muerte contra los sacrificios paganos (Ep. 93 §10).'),
 ('P03', 'origenes', 'Orígenes', 'c. 185–c. 253',
  'Cita Heb 10:29 en sentido moral: honrar al Hijo es vivir rectamente.',
  'A la letra, la ley penal de Moisés no rige para la Iglesia: los cristianos «no podrían» apedrear ni quemar.',
  'El Legislador cristiano no enseña violencia contra nadie; al hereje se le rechaza (Tit 3:10) sin odiarlo.',
  'Ninguno hallado.'),
 ('P04', 'ireneo', 'Ireneo de Lyon', 'c. 130–c. 202',
  'Sin citar 10:26-31, razona igual: la venganza es «típica y moderada» en el AT y «real y eterna» en el NT (IV.28.1).',
  'El Evangelio «cumple, extiende y da mayor amplitud» a la Ley; las leyes «de servidumbre» fueron canceladas.',
  '«En Dios no hay coacción» (principio, no norma civil).',
  '«Justamente apedreado» (IV.8.3); herejes quemados por fuego del cielo (IV.26.2): castigo divino.'),
 ('P05', 'tertuliano', 'Tertuliano de Cartago', 'c. 155–c. 220',
  'Cita Heb 6:4-6 («de Bernabé»); no 10:26-31.',
  'La ley antigua frenaba la violencia (talión); la nueva apunta a la clemencia.',
  '«No forma parte de la religión obligar a la religión» (A Escápula 2).',
  'Cita Dt 13 y los 23.000 muertos del AT sin reproche (Scorpiace 2-3).'),
 ('P06', 'lactancio', 'Lactancio', 'c. 250–c. 320',
  'No cita Hebreos en lo leído.',
  'El antiguo testamento «no era perfecto»; el de Cristo, «completo» (IV.20).',
  '«La religión no puede imponerse por la fuerza»; matar «siempre es ilícito» (V.20, VI.20).',
  'Presenta la derrota de un perseguidor como castigo de Dios (Muertes 47).'),
 ('P07', 'atanasio', 'Atanasio de Alejandría', 'c. 296–373',
  'Comenta Heb 3:1-2 (Disc. II §9); no 10:26-31.',
  '«¿Qué necesidad había ya de la sombra?» (Encarnación §40).',
  '«La verdad no se predica con espadas… sino con persuasión» (Hist. arianos §33).',
  '«¿Quién no apedrearía a tales locos?» (retórico, Decretos §28).'),
 ('P08', 'jeronimo', 'Jerónimo', 'c. 347–420',
  'No cita 10:26-31 en las cartas leídas.',
  'De la espada de la ley antigua (Dt 17) a la «espada espiritual»: la expulsión de la Iglesia (Ep. 14 §8).',
  '—',
  '«No hay crueldad en el celo por el honor de Dios»: Dt 13 (Ep. 109 §3).'),
]
tr = ''
for code, slug, name, dates, h, d, n, x in ROWS:
    tr += (f'<tr><td class="who"><img class="av" src="img/{slug}.jpg">{E(name)}<br><span style="font-weight:500;color:#566079;font-size:14px;margin-left:56px">{E(dates)} · {code}</span></td>'
           f'<td>{E(h)}</td><td>{E(d)}</td><td>{E(n)}</td><td>{E(x)}</td></tr>')
body = f'''<table class="v"><tr><th style="width:230px">Padre</th><th><span class="tg tgH">Hebreos</span></th><th><span class="tg tgD">Evangelio frente al AT</span></th><th><span class="tg tgN">No matar a herejes</span></th><th><span class="tg tgX">Matiz en contra</span></th></tr>{tr}</table>
<div class="ans" style="margin-top:16px"><b>Lectura de conjunto.</b> En lo que leí, <b>ninguno de los ocho usa Hebreos 10:28 como orden de ejecutar a nadie</b>; solo Crisóstomo lo comenta (como un hecho del pasado) y Orígenes cita el v. 29 en sentido moral. Crisóstomo, Orígenes, Tertuliano, Lactancio y Atanasio dicen expresamente que no se debe matar o forzar en materia de fe, e Ireneo lo implica como principio. <b>No hay unanimidad, y no hay que fingirla</b>: Agustín defendió la coerción legal (sin pedir la muerte de los donatistas), Crisóstomo admite frenar y silenciar a los herejes, y Jerónimo invoca Dt 13 en una carta.</div>'''
page(OUT, 'HB04_es', 'HB04', 'Los ocho Padres · resumen', 'Resumen en español',
     'Ocho Padres: ninguno usa Hebreos 10:28 como orden de matar, pero tampoco son unánimes',
     'Fotos: grabados, mosaicos, iconos y pinturas de dominio público (iconografía tradicional, no retratos en vida). Detalle y citas en P01–P08.', body,
     'Cada celda resume pasajes de las diapositivas P01–P08 (citas verificadas contra la página de origen en la traducción inglesa de dominio público). «Lo reunido» y «lo leído» se refiere a lo que encontraron los investigadores y comprobé yo; no es un rastreo exhaustivo de cada autor.<br>' + PACK)

# ---------------------------------------------------------------- HB09
body = f'''<div class="two">
<div class="pn"><h4>Lo que sí hice</h4><ul class="l" style="font-size:17.5px">
<li>Vi el vídeo entero (90 s): transcripción con Whisper large-v3 y revisión fotograma a fotograma.</li>
<li>Leí el griego de Hebreos 10 y de los pasajes paralelos (SBLGNT, CC BY 4.0).</li>
<li>Abrí el artículo de Coetsee (<i>Verbum et Ecclesia</i> 45/1, 2024, acceso abierto) para el argumento «cuánto más».</li>
<li>Aquino: latín del Corpus Thomisticum e inglés de la edición dominica de 1920 (II-II, q. 10 y q. 11).</li>
<li>Ocho investigadores (modelo pequeño, uno por Padre) buscaron los pasajes. <b>Comprobé yo</b> que cada cita inglesa está, letra por letra, en la página que indican (82 de 83 pasajes; el que no coincide, la carta de Ireneo a Víctor, no lo uso) y que los fragmentos latinos y griegos mostrados están en su fuente.</li>
</ul></div>
<div class="pn"><h4>Resultados negativos</h4><ul class="l" style="font-size:17.5px">
<li>De los ocho Padres, <b>ninguno cita Hebreos 10:28 como orden</b>. Solo Crisóstomo lo comenta; Orígenes cita 10:29 (moral); Tertuliano cita Heb 6:4-6.</li>
<li>Sobre Agustín no se buscó Hebreos 10:26-31; solo coerción y Antiguo Testamento.</li>
<li>Lactancio, Ireneo, Atanasio y Jerónimo: ninguna cita de Heb 10:26-31 en lo leído.</li>
<li>No he podido verificar en la edición crítica la frase «resecandae sunt putridae carnes» que Aquino atribuye a Jerónimo (el Manipulus florum la sitúa en In Gal. III, CCSL 77A p. 163): no la uso como cita.</li>
</ul></div></div>
<div class="two" style="margin-top:14px">
<div class="pn"><h4>Límites</h4><ul class="l" style="font-size:17.5px">
<li><b>Traducciones al español mías</b>, desde ediciones inglesas del s. XIX de dominio público (ANF y NPNF); no he leído el griego ni el latín completos, solo los fragmentos citados donde pude comprobarlos.</li>
<li><b>Fechas de vida y de obras aproximadas</b> (convencionales; no verificadas una a una).</li>
<li><b>Imágenes</b>: iconografía tradicional; ninguna es un retrato en vida. La de Ireneo es de baja resolución.</li>
<li>Los investigadores cometieron errores que corregí (numeración de homilías, «hachas y martillos» en lugar de «espadas»…).</li>
</ul></div>
<div class="pn"><h4>Avisos</h4><ul class="l" style="font-size:17.5px">
<li>«Residual» respecto de Aquino vale <b>frente a los Padres y la tradición apostólica</b>, no frente a la Edad Media latina: allí la ejecución de herejes se contempló y practicó.</li>
<li>Los Padres <b>no son unánimes</b>; los matices están en cada ficha (azul).</li>
<li>La parte islámica del cierre (CV01-CV02) remite a las tarjetas del pack de apostasía (AP); no la he vuelto a verificar aquí.</li>
<li>Es documentación de lo que dicen las fuentes, no una valoración de ninguna religión ni una guía para actuar contra nadie.</li>
</ul></div></div>'''
page(OUT, 'HB09_es', 'HB09', 'Fuentes, límites y avisos', 'Resumen en español',
     'Qué leí, qué no, qué salió negativo y qué hay que tener en cuenta',
     'Resumen honesto del método y de sus límites.', body,
     'Fuentes: SBLGNT (CC BY 4.0), newadvent.org (ANF/NPNF), CCEL, The Latin Library, Wikisource, Corpus Thomisticum, Patrologia Graeca 25 (archive.org), Wikimedia Commons (imágenes de dominio público).<br>' + PACK)
print('hbstatic2 ok')
