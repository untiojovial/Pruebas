# -*- coding: utf-8 -*-
# Diapositivas generales: AE00 (resumen), AE13 (mapa de lo que dijo cada fuente), AE14 y AE15 (conclusiones para TikTok) y AE99 (fuentes y límites)
import sys, os
AY = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ay'
sys.path.insert(0, AY)
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb')
import aypad
import hbcss
from hbcss import E, marks, page
import genpad
from ayfigs import FIGS
OUT = aypad.OUT; PACK = aypad.PACK; tags = aypad.tags
os.makedirs(OUT, exist_ok=True)
ID = {f['slug']: f['id'] for f in FIGS}

# ---------------------------------------------------------------- AE00
ROWS = {
 'ibn-shubruma': ('Al-Muhalla, vol. 9, pp. 38–40 (opinión del s. VIII, texto del s. XI)', 'Un jurista musulmán no admite que un padre case a su hija pequeña hasta la pubertad y ve el caso de Aisha como una excepción del Profeta; Ibn Hazm lo rechaza. Crítica jurídica, no moral.'),
 'kindi': ('Respuesta de al-Kindi (siglo IX; fecha dudosa)', 'Mahoma pasó por alto el escándalo del collar porque ella era la única virgen y la más joven de sus mujeres. No da edad.'),
 'riccoldo': ('Confutatio (c. 1300; texto impreso en 1550)', 'Ante el reproche de Alí, Mahoma responde que la quiere porque la tomó «virgen y todavía jovencita». No da edad.'),
 'pascual': ('Sobre la seta mahometana, cap. II (atribuido a c. 1300; copia del s. XVI)', 'Axa «no tenía más de siete años» al casarse y «aún no tenía sino diez» al consumar el matrimonio. Atribución y fecha discutidas.'),
 'juan-andres': ('Confusión de la secta mahomética (Valencia, 1515)', 'Seis años al contrato y ocho a la consumación, «casi homicida»; y Mahoma tenía ya «siete mujeres juntamente». La crítica explícita más antigua con fecha segura.'),
 'prideaux': ('The True Nature of Imposture (Londres, 1697)', 'Da seis y ocho años y los explica por la costumbre de los «países cálidos»; lo que critica es la «lujuria» de Mahoma, no la edad.'),
}
tr = ''
for f in FIGS:
    th = []
    for q in f['quotes']:
        for t in q['theme']:
            if t not in th: th.append(t)
    obra, dice = ROWS[f['slug']]
    tr += (f'<tr><td class="who" style="white-space:normal"><div>{E(f["name"])}<br><span style="font-weight:500;color:#566079;font-size:13.5px">{E(f["dates"])} · {f["id"]}</span></div></td>'
           f'<td style="font-size:15px">{E(obra)}</td><td>{E(dice)}</td><td style="line-height:2">{tags(th)}</td></tr>')
body = f'''<table class="v" style="table-layout:fixed"><tr><th style="width:270px">Figura</th><th style="width:210px">Obra</th><th>Qué dice de Aisha</th><th style="width:170px">Tema</th></tr>{tr}</table>
<div class="ans" style="margin-top:16px"><b>Qué hay y qué no hay.</b> Un jurista musulmán del siglo VIII, un texto cristiano árabe anónimo del IX, un dominico (c. 1300), un tratado castellano atribuido a un obispo, un converso antiguo alfaquí (1515) y un deán anglicano (1697). <b>Antes de 1515, con fecha segura, no encontré a ningún cristiano que critique expresamente la edad de Aisha</b>; lo anterior ataca las esposas y la «lujuria», y a Aisha solo la nombra como la más joven o la única virgen. El tratado atribuido a Pedro Pascual da una edad (siete y diez años), pero su fecha es dudosa. Las edades vienen de las propias fuentes musulmanas (diapositiva AE13).</div>'''
page(OUT, 'AE00_es', 'AE00', 'Las críticas históricas al matrimonio de Mahoma con Aisha', 'Resumen en español',
     'La edad de Aisha: quién la criticó por escrito, de las fuentes más tempranas a 1700',
     'Citas traducidas al español, con su obra, su fuente y qué quiere decir cada una. Imágenes de las páginas leídas, con el subrayado mío.', body,
     'Las citas entre comillas son de mi traducción al español; el texto de partida y la aclaración de cada una están en las diapositivas AExx. Fechas aproximadas.<br>' + PACK, head_cls='alt')

# ---------------------------------------------------------------- AE13: mapa
MAP = [
 ('ss. VII–VIII', 'Cristianos siriacos, griegos y armenios (Sofronio, Sebeos, Ghewond, Crónica de 724…)', 'No', 'No', 'No hablan de sus esposas.'),
 ('c. 740', 'Juan Damasceno, <i>De haeresibus</i> 101', 'No', 'No', 'Critica el caso de la mujer de Zayd y las cuatro esposas y mil concubinas que dice permitir el Corán.'),
 ('s. VIII', 'Ibn Shubruma, según Ibn Hazm (AE01)', 'Sí', 'No en esta cita', 'Para él el matrimonio con Aisha fue una excepción del Profeta (crítica jurídica).'),
 ('ss. VIII–IX', 'Ibn Ishaq, Ibn Saʿd, al-Tabari (fuentes musulmanas)', 'Sí', 'Sí: 6 o 7 al contrato, 9 a la consumación', 'Dan la edad ellos mismos; ninguno critica el matrimonio por su edad.'),
 ('s. IX', 'Teófanes (c. 814)', 'No', 'No', 'Cuenta su boda con Jadiya, una viuda; no habla de otras esposas.'),
 ('s. IX', 'Apología de al-Kindi (AE02)', 'Sí', 'Solo «la más joven»', 'La presenta como escándalo y como la favorita por ser la única virgen y la más joven.'),
 ('ss. IX–XII', 'Bartolomé de Edesa (fecha incierta)', 'Sí (“Aise”)', 'No', 'La nombra en una lista de esposas; critica las cuatro esposas y las concubinas.'),
 ('ss. XI–XIII', 'Zigabeno, Coniates, Jacques de Vitry', 'No', 'No', 'Critican las cuatro esposas, las concubinas y la «lujuria»; no la nombran.'),
 ('ss. XII–XIII', 'Cronistas siriacos: Miguel el Sirio, Bar Hebreo', 'No', 'No', 'Hablan de la poligamia en general o nombran solo a Jadiya.'),
 ('c. 1143', 'Dosier latino de Pedro el Venerable (<i>Chronica mendosa</i>)', 'Sí (“Ayska”)', 'No', 'La nombra en un relato político, no en el de su boda.'),
 ('c. 1300', 'Riccoldo da Monte di Croce (AE03)', 'Sí (“Ayssa”)', 'Solo «todavía jovencita»', 'Relata el episodio del collar y la presenta como adúltera; la edad no figura.'),
 ('c. 1300 (¿?)', 'Tratado atribuido a Pedro Pascual (AE04)', 'Sí («Axa»)', 'Sí: 7 y 10', 'Fecha y autoría discutidas; único manuscrito del s. XVI.'),
 ('1461', 'Nicolás de Cusa', 'No', 'No', 'Critica el permiso de muchas esposas.'),
 ('1515', 'Juan Andrés (AE05)', 'Sí («Axa»)', 'Sí: 6 y 8', 'La crítica explícita más antigua con fecha segura.'),
 ('1697', 'Prideaux (AE06)', 'Sí', 'Sí: 6 y 8', 'No condena la edad; critica la «lujuria». Cita a Juan Andrés.'),
 ('1705–1732', 'Reland, Boulainvilliers, Gagnier', 'Sí', 'Reland no; Boulainvilliers “muy joven”; Gagnier 7 y 9', 'Narran sin condenar.'),
]
rows = ''
for fecha, quien, nombra, edad, que in MAP:
    cls = ' style="background:#fff7e6"' if ('AE0' in quien and ('Sí: ' in edad or 'Sí: 6' in edad)) else ''
    rows += f'<tr{cls}><td style="font-size:14px;white-space:nowrap">{E(fecha)}</td><td style="font-size:14.5px">{quien}</td><td style="font-size:14.5px">{E(nombra)}</td><td style="font-size:14.5px">{E(edad)}</td><td style="font-size:14.5px">{E(que)}</td></tr>'
body = f'''<table class="v" style="table-layout:fixed"><tr><th style="width:110px">Fecha</th><th style="width:330px">Quién y qué obra</th><th style="width:130px">¿Nombra a Aisha?</th><th style="width:190px">¿Da su edad?</th><th>Qué hace</th></tr>{rows}</table>
<div class="ans" style="margin-top:14px"><b>Cómo leerlo.</b> Cada fila es lo que <b>leí</b> en esa fuente, no todo lo que escribió el autor. «No» significa que en los pasajes leídos no aparece (véase «Límites» en AE99). Las filas con ítem AExx tienen su propia diapositiva; las demás son resultados negativos o contexto.</div>'''
page(OUT, 'AE13_es', 'AE13', 'Qué dijo cada fuente', 'Resumen en español',
     'Dónde busqué y qué encontré: de los siglos VII a XVIII',
     'Mapa de resultados, incluidos los negativos.', body,
     'Fuentes leídas por investigadores (modelo pequeño) y comprobadas por mí en las diapositivas AE01–AE06; el resto, solo por los investigadores.<br>' + PACK, head_cls='alt')

# ---------------------------------------------------------------- AE14 / AE15 (conclusiones)
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
        blocks += f'<div class="cc"><div class="nn">{num}</div><div class="tx"><h3>{E(head)}</h3><p>{marks(txt)}</p><div class="by">{"Lo dijeron" if codes else ""} {cd}</div></div></div>'
    h = f'''<!doctype html><html><head><meta charset="utf-8"><style>{hbcss.CSS}{genpad.CQ}{CC}</style></head><body><div class="qs">
<div class="top"><div class="who"><b>{fname[:4]}</b>Lo que se puede decir, y lo que no<i>{n}/2 · de los siglos VII a XVIII</i></div></div>
<div class="mid">{blocks}</div>
<div class="nota">Cada punto resume lo que dijo cada autor (códigos AE01–AE06) o lo que no se encontró en las fuentes leídas. No es una valoración de si Aisha era o no una niña ni un juicio sobre la tradición musulmana, sino de qué se dijo y cuándo. Traducciones al español mías.</div>
<div class="ft2"><span>{PACK}</span><span>{fname[:4]} · {n}/2</span></div></div></body></html>'''
    open(f'{OUT}/{fname}.html', 'w', encoding='utf-8').write(h)

CONCL1 = [
 ('1', 'Antes de 1515, con fecha segura, ningún cristiano critica expresamente la edad de Aisha.',
  'En lo que pude leer (siriaco, griego, armenio, latín), las críticas medievales atacan [[k:las cuatro esposas y la «lujuria»]] de Mahoma. Aisha aparece solo como la más joven y la única virgen (al-Kindi, s. IX) o como «virgen y todavía jovencita» (Riccoldo, c. 1300): una alusión, no una edad.',
  ['AE02', 'AE03']),
 ('2', 'La edad aparece por escrito en textos cristianos con Pascual (¿c. 1300?) y Juan Andrés (1515).',
  'Un tratado castellano atribuido a Pedro Pascual dice que no tenía [[k:más de siete años]] al casarse y aún no diez al consumar; su fecha es dudosa. Juan Andrés (1515, fecha segura) da [[k:seis y ocho]] y lo llama «casi homicida». Prideaux (1697) repite seis y ocho y cita a Juan Andrés en el margen.',
  ['AE04', 'AE05', 'AE06']),
 ('3', 'Las edades no las inventan los críticos: las toman de las fuentes musulmanas.',
  'Los textos musulmanes dan [[k:seis o siete años al contrato y nueve a la consumación]] desde el siglo VIII (Ibn Ishaq, Ibn Saʿd, al-Tabari). El tratado atribuido a Pascual los cita como «los libros de los moros»; Juan Andrés dice probarlo con el «libro de Acear», que no he podido identificar.',
  ['AE04', 'AE05']),
 ('4', 'Un jurista musulmán ya lo trató como excepción.',
  'Ibn Shubruma (s. VIII, por Ibn Hazm) no admite que un padre case a su hija pequeña y [[k:considera el caso de Aisha una excepción propia del Profeta]]. Ibn Hazm (s. XI) responde que a quien alegue que fue exclusivo suyo no se le hace caso. La discusión es interna y jurídica.',
  ['AE01']),
]
CONCL2 = [
 ('5', 'Lo que no se puede decir: «los cristianos criticaban la edad de Aisha desde el siglo VII».',
  'Los [[k:textos siriacos, griegos y armenios que leí no la nombran]]. Lo más temprano que critica el matrimonio de Mahoma es general (la mujer de Zayd, las cuatro esposas y las concubinas), y la primera edad en un texto de fecha segura es de 1515.',
  ['AE02']),
 ('6', 'Cuidado con Juan Andrés.',
  'Da [[k:ocho años a la consumación, no nueve]]; cita un «libro de Acear» que no sé identificar; y escribe como converso polemista, no como fuente neutral. Prideaux lo cita en el margen y repite sus cifras (seis y ocho).',
  ['AE05', 'AE06']),
 ('7', 'Prideaux no condena la edad.',
  'Explica los seis y los ocho años por [[k:la costumbre de los países cálidos]] y critica otra cosa: cómo Mahoma hizo servir su impostura a su lujuria. Quien lo cite como “crítico de la edad” le atribuye algo que no dice.',
  ['AE06']),
 ('8', 'Las fuentes musulmanas tampoco son unánimes en la cronología.',
  'Seis o siete años al contrato, nueve o diez a la consumación. Las cronologías basadas en la edad de su hermana Asma (unos cien años al morir en 73 H, diez más que Aisha) apuntan a una Aisha mayor, pero [[k:no encajan con las fechas de Ibn Saʿd]]: no son una cronología acordada. Conviene conocerlas para responder.',
  []),
]
concl('AE14_es', 1, CONCL1)
concl('AE15_es', 2, CONCL2)

# ---------------------------------------------------------------- AE99
body = '''<div class="two">
<div class="pn"><h4>Qué leí y cómo se comprobó</h4><ul class="l" style="font-size:17px">
<li>Trece investigadores (modelo pequeño) en dos tandas buscaron en textos siriacos, griegos, armenios, latinos, árabes, castellanos y modernos. <b>Yo elegí las figuras y comprobé yo mismo, en la imagen de la página</b>, los pasajes de Juan Andrés (ejemplar de la Biblioteca del Congreso), Riccoldo (Basilea, 1550), Pascual (ed. de 1908) y Prideaux (1698); el árabe de al-Kindi e Ibn Hazm, por programa contra OpenITI.</li>
<li>La página 99 de la traducción francesa de 1574 es la de tu captura: la transcribí de ella y no tengo otro escaneo para compararla.</li>
<li>Los resultados negativos del mapa (AE13) son lo que los investigadores leyeron: no es una búsqueda exhaustiva de cada obra.</li>
</ul></div>
<div class="pn"><h4>Límites y qué quedó fuera</h4><ul class="l" style="font-size:17px">
<li><b>Traducciones al español mías</b>, del árabe, el latín, el castellano antiguo, el francés y el inglés.</li>
<li><b>Pascual</b>: atribución y fecha discutidas; solo existe una copia del siglo XVI. <b>Riccoldo</b>: el latín de 1550 es una retraducción desde el griego. <b>Al-Kindi</b>: autoría y fecha discutidas; el texto de OpenITI es una transcripción web.</li>
<li><b>Fuera</b>: los pasajes sexualmente explícitos o violentos, y los tramos que acusan a Aisha de adulterio (el Corán, 24:11-20, la declara inocente).</li>
<li>La página impresa de las obras árabes la deduzco de los marcadores de OpenITI (el marcador cierra la página; regla comprobada en otra obra, no en estas).</li>
<li>No juzgo la historicidad de la edad ni la tradición musulmana: solo documento <b>quién lo dijo, cuándo y con qué texto</b>.</li>
</ul></div></div>'''
page(OUT, 'AE99_es', 'AE99', 'Fuentes, límites y avisos', 'Resumen en español',
     'Qué leí, qué dejé fuera y qué hay que tener en cuenta',
     'Resumen honesto del método y de sus límites.', body,
     'Fuentes: OpenITI (Shamela), Biblioteca del Congreso (ejemplar Rosenwald 1275), archive.org (Basilea, 1550; Armengol, 1908; Prideaux, 1698).<br>' + PACK, head_cls='alt')
print('aystatic ok')
