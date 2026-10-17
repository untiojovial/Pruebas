# -*- coding: utf-8 -*-
# Diapositivas generales: IT00 (resumen), IT13 (balance de «hombres de paja»), IT14 e IT15 (conclusiones para TikTok) e IT99 (fuentes y límites)
import sys, os
IT = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/it'
sys.path.insert(0, IT)
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb')
import itpad
import hbcss
from hbcss import E, marks, page
import genpad
from itfigs import FIGS
OUT = itpad.OUT; PACK = itpad.PACK; tags = itpad.tags; vd = itpad.vd
os.makedirs(OUT, exist_ok=True)
BYID = {f['id']: f for f in FIGS}

# ---------------------------------------------------------------- IT00
ROWS = {
 'IT01': 'Reconocer a Dios como creador (rububiyya) no basta: lo hacían los politeístas árabes; lo decisivo es adorarlo solo (uluhiyya). Sus tres «clases» de tawhid no llevan, como tal, los tres nombres que se le atribuyen.',
 'IT02': 'Afirma los atributos de Dios «sin distorsión ni negación, sin “cómo” ni comparación»; el habla de Dios es un atributo eterno, con «sus letras y sus significados».',
 'IT03': 'Rechaza la simplicidad divina de los filósofos: tener atributos distintos no es «una composición imposible». Por eso no puede objetar a la Trinidad que Dios sea simple.',
 'IT04': '«Los textos establecidos del Mensajero nunca fueron contradichos por una razón clara»; si chocan, prevalece lo concluyente. Compara el método de los teólogos con el credo cristiano.',
 'IT05': 'La fitra (conocimiento innato de Dios): la reflexión «no es la primera obligación»; la prueba de la creación es «innata y necesaria», pero la versión de los teólogos está corrompida.',
 'IT06': 'Contra la lógica griega: es imposible concebir «las cosas definidas por la mera definición»; la analogía puede dar certeza; Dios y los profetas se conocen por «signos», no por silogismos.',
 'IT07': 'El tawatur «no tiene un número limitado»: es el conocimiento que produce el informe, y puede ser tawatur «para unos y no para otros»; la aceptación de la comunidad da certeza.',
 'IT08': 'Aplica el tawatur a los cristianos: los Evangelios no se transmitieron como el Corán; los apóstoles «estaban asustados y ausentes» en la crucifixión. Al Corán le exige lecturas «establecidas».',
 'IT09': 'Responde a una carta de Pablo de Antioquía y dice que la citará «con sus palabras exactas». Cita bien la sección que se pudo comprobar.',
 'IT10': 'Explica la Trinidad como tres atributos (esencia, habla, vida): es lo que dice una carta cristiana árabe, no los credos ni los Padres.',
 'IT11': 'Argumenta que «una sola sustancia» en tres es «tres sustancias, tres dioses»; reconoce que ellos no lo dicen. Los credos lo prohíben.',
 'IT12': 'Fórmula melquita bien resumida; «Dios murió» jacobita, parcial; «ellos adoran a María» y le dicen «perdónanos y ten misericordia de nosotros»: hombre de paja.',
}
tr = ''
for f in FIGS:
    th = []; vs = []
    for q in f['quotes']:
        for t in q['theme']:
            if t not in th: th.append(t)
        if q.get('verdict') and q['verdict'] not in vs: vs.append(q['verdict'])
    vch = ' '.join(vd(v) for v in vs) if vs else '<span style="color:#8a93a8;font-size:13px">—</span>'
    tr += (f'<tr><td class="who" style="white-space:normal">{E(f["name"])}<br><span style="font-weight:500;color:#566079;font-size:13.5px">{f["id"]} · {E(f["block"])}</span></td>'
           f'<td style="font-size:14.5px">{E(f["works"][0]["lat"])}{(" y " + E(f["works"][1]["lat"])) if len(f["works"]) > 1 else ""}</td><td style="font-size:15.5px">{E(ROWS[f["id"]])}</td><td style="line-height:2">{tags(th)}</td><td style="line-height:2.1">{vch}</td></tr>')
body = f'''<table class="v" style="table-layout:fixed"><tr><th style="width:230px">Tema</th><th style="width:175px">Obra</th><th>Qué dice</th><th style="width:165px">Bloque</th><th style="width:195px">Veredicto</th></tr>{tr}</table>
<div class="ans" style="margin-top:14px"><b>Qué es este pack.</b> Doce temas de Ibn Taymiyya (661–728 H / 1263–1328): <b>tawhid</b> (IT01–03), <b>epistemología</b> (IT04–06), <b>tawatur</b> (IT07–08) y su <b>refutación de los cristianos</b> (IT08–12), con el texto árabe original, mi traducción y, en los pasajes sobre cristianos, un contraste con lo que dicen las fuentes cristianas: <b>¿hace hombres de paja?</b> El veredicto está en cada tema y se resume en IT13. No se conserva un retrato suyo: la columna de la izquierda de cada tema muestra la portada tipográfica de la obra.</div>'''
page(OUT, 'IT00_es', 'IT00', 'Ibn Taymiyya', 'Resumen en español',
     'Ibn Taymiyya sobre tawhid, epistemología, tawatur y los cristianos: ¿hombres de paja?',
     'Citas del árabe traducidas al español, con su obra, su edición y el contraste con las fuentes cristianas.', body,
     'Las citas entre comillas son de mi traducción al español; el árabe, la fuente y la aclaración de cada una están en las diapositivas ITxx. Lecturas críticas mías marcadas como «Lectura (mía)».<br>' + PACK, head_cls='alt')

# ---------------------------------------------------------------- IT13 balance
BAL = [
 ('IT09', 'La carta que responde es de Pablo de Antioquía (melquita, obispo de Sidón)', 'fiel', 'Datos exactos; es una carta, no «la» doctrina'),
 ('IT09', 'Citará la carta «con sus palabras exactas», sección por sección', 'nov', 'Solo comprobado en la sección 1'),
 ('IT10', 'Cita la fórmula esencia–habla–vida de la carta cristiana', 'fiel', 'Cita real; no es lo que dicen los credos'),
 ('IT10', '«Muchos de ellos» dicen Padre = existencia, Hijo = Palabra, Espíritu = vida', 'parcial', 'Real en esa carta; sin fuentes; los credos dicen «personas»'),
 ('IT10', '«Hipóstasis» no está en sus libros y se explica de varias maneras', 'parcial', 'Las glosas varían; pero está en Hebreos 1:3'),
 ('IT11', 'Una sustancia en tres = tres sustancias = tres dioses', 'parcial', 'Cita exacta; conclusión suya; los credos lo prohíben'),
 ('IT11', 'Reconoce que los cristianos «no dicen tres dioses»', 'fiel', 'Es una concesión; lo suyo es una acusación de contradicción'),
 ('IT11', 'Ningún trinitario afirma un «asociado» igual a Dios', 'parcial', 'Los credos dicen tres personas coiguales, y no asociados'),
 ('IT12', 'Los melquitas: una persona, dos naturalezas', 'fiel', 'Es la fórmula de Calcedonia'),
 ('IT12', 'Los jacobitas: «Dios murió, padeció y fue crucificado»', 'parcial', 'Cirilo dice «sufrió en la carne»; los credos matizan'),
 ('IT12', 'Los cristianos «adoran a María» y le piden «perdónanos»', 'paja', 'La oración pide «ruega por nosotros»; Nicea II separa veneración y adoración'),
 ('IT08', 'Los Evangelios no se transmitieron como el Corán (letra y sentido)', 'parcial', 'Cierto en el método; no responde a Lc 1:1-4'),
 ('IT08', 'Ningún discípulo ni cristiano presenció la crucifixión', 'parcial', 'Contradice a Jn 19:25-27 y 19:35'),
]
tr = ''
for code, claim, v, why in BAL:
    tr += f'<tr><td class="who" style="white-space:normal">{code}</td><td style="font-size:16px">{E(claim)}</td><td>{vd(v)}</td><td style="font-size:15px">{E(why)}</td></tr>'
cnt = {k: sum(1 for b in BAL if b[2] == k) for k in ('fiel', 'parcial', 'paja', 'nov')}
body = f'''<table class="v" style="table-layout:fixed"><tr><th style="width:80px">Tema</th><th>Lo que dice sobre los cristianos</th><th style="width:240px">Veredicto</th><th style="width:360px">Por qué</th></tr>{tr}</table>
<div class="ans" style="margin-top:14px"><b>Marcador.</b> De {len(BAL)} afirmaciones contrastadas: <b>{cnt["fiel"]} fieles</b>, <b>{cnt["parcial"]} parcialmente fieles</b>, <b>{cnt["paja"]} hombre de paja</b> y {cnt["nov"]} no verificable. No es un hombre de paja sistemático —cita sus fuentes y reconoce lo que los cristianos niegan—, pero <b>toma por «la doctrina» lo que dice una carta cristiana árabe</b>, saca de ahí contradicciones que los credos rechazan expresamente, y en María y la crucifixión afirma lo que los textos cristianos desmienten.</div>'''
page(OUT, 'IT13_bal', 'IT13', 'Balance', 'Resumen en español',
     'Balance: ¿hombres de paja? Trece afirmaciones sobre los cristianos, contrastadas',
     'Cada fila remite al tema donde están el árabe, la traducción y las fuentes cristianas.', body,
     'Veredictos míos, apoyados en las fuentes cristianas citadas en cada tema (credos, Padres, Tomás de Aquino, concilios, Evangelios). «Parcialmente fiel»: describe algo real pero lo generaliza, lo interpreta mal o lo presenta sin fuentes.<br>' + PACK, head_cls='alt')

# ---------------------------------------------------------------- IT14 / IT15 (conclusiones)
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
def concl(fname, n, items, title, nota):
    blocks = ''
    for num, head, txt, codes in items:
        cd = ''.join(f'<span>{c}</span>' for c in codes)
        blocks += f'<div class="cc"><div class="nn">{num}</div><div class="tx"><h3>{E(head)}</h3><p>{marks(txt)}</p><div class="by">Véase {cd}</div></div></div>'
    h = f'''<!doctype html><html><head><meta charset="utf-8"><style>{hbcss.CSS}{genpad.CQ}{CC}</style></head><body><div class="qs">
<div class="top"><div class="who"><b>{fname[:4]}</b>{E(title)}<i>{n}/2 · doce temas</i></div></div>
<div class="mid">{blocks}</div>
<div class="nota">{E(nota)}</div>
<div class="ft2"><span>{PACK}</span><span>{fname[:4]} · {n}/2</span></div></div></body></html>'''
    open(f'{OUT}/{fname}.html', 'w', encoding='utf-8').write(h)

CONCL1 = [
 ('1', 'Sabe citar a los cristianos: cuando cita, cita bien.',
  'Cita la carta de Pablo de Antioquía y resume con fidelidad la fórmula melquita: [[k:una sola persona y dos naturalezas]], que es la de Calcedonia. Y reconoce que los cristianos [[k:no dicen tres dioses]].',
  ['IT09', 'IT12', 'IT11']),
 ('2', 'Pero toma una glosa por «la doctrina».',
  'Que Padre, Hijo y Espíritu sean esencia, habla y vida lo dice una carta cristiana árabe; los credos y los Padres hablan de personas, no de atributos: «[[k:no son tres Dioses, sino un solo Dios]]». Y su «muchos de ellos dicen» no nombra ni un libro.',
  ['IT10', 'IT11']),
 ('3', 'La contradicción «tres dioses» es suya, no de ellos.',
  '«Una sola sustancia» no significa «tres sustancias»: el credo de Atanasio [[k:prohíbe decir que hay tres Dioses]]. Él mismo admite que no lo dicen: lo que hace es acusarlos de contradecirse.',
  ['IT11']),
 ('4', 'Con María y con la cruz se equivoca.',
  'Su «ellos adoran a María», con el «perdónanos» que les atribuye, es un hombre de paja: la oración dice [[k:«ruega por nosotros»]] y Nicea II separa veneración y adoración. Y que «ninguno de ellos presenció la crucifixión» lo desmiente [[k:Juan 19:25-27 y 19:35]].',
  ['IT12', 'IT08']),
]
CONCL2 = [
 ('5', 'Su tawhid: lo central es adorar a Dios solo.',
  'Reconocer a Dios como creador [[k:no basta]]: los politeístas árabes lo hacían. Pero la fórmula de tres «tawhid» con exactamente los nombres rububiyya, uluhiyya y atributos no aparece como tal en los textos que se revisaron: lo suyo es la insistencia en la uluhiyya.',
  ['IT01']),
 ('6', 'Sus atributos: acepta distinciones reales en Dios.',
  'Para él la esencia con atributos distintos [[k:no es composición]]; el habla de Dios es un atributo eterno. Lectura (mía): con esa teología no puede objetar a la Trinidad que Dios sea simple; solo le quedan otros argumentos.',
  ['IT02', 'IT03']),
 ('7', 'Su tawatur: lo define el conocimiento que produce.',
  'No tiene [[k:un número limitado]] y puede ser tawatur «para unos y no para otros». A los Evangelios les exige tawatur de la letra; al Corán, lecturas [[k:«establecidas»]]. Lectura (mía): el criterio es relativo al oyente, y por eso la certeza cristiana sobre la cruz no cuenta para él.',
  ['IT07', 'IT08']),
 ('8', 'Su epistemología: critica la lógica y usa la lógica.',
  'Rechaza el silogismo, pero argumenta con dilemas y reducciones. Y su regla [[k:«los textos establecidos del Mensajero nunca fueron contradichos por una razón clara»]], lectura (mía), se protege sola: si hay choque, uno de los dos no era claro o no estaba establecido.',
  ['IT04', 'IT05', 'IT06']),
]
concl('IT14_es', 1, CONCL1, '¿Hombres de paja? Lo que hace con los cristianos',
      'Veredictos míos, apoyados en los textos de cada tema (árabe de OpenITI y fuentes cristianas de dominio público). Cada punto resume lo que dijo Ibn Taymiyya y lo que dicen las fuentes cristianas; no es una valoración de la fe musulmana. Traducciones mías.')
concl('IT15_es', 2, CONCL2, 'Su teoría del conocimiento, puesta a prueba',
      'Los puntos 5 a 8 mezclan lo que dijo con mi lectura crítica; la lectura va marcada «Lectura (mía)» en las diapositivas. Son observaciones de lógica y de coherencia, no un juicio sobre el islam. Traducciones mías.')

# ---------------------------------------------------------------- IT99
body = '''<div class="two">
<div class="pn"><h4>Qué leí y cómo se comprobó</h4><ul class="l" style="font-size:17px">
<li>Once investigadores (modelo pequeño) buscaron los pasajes en el texto digital de OpenITI (copia de Shamela). <b>Yo elegí los doce temas y las citas.</b> El árabe de cada cita lo copió el código del texto de OpenITI, no una persona, y lo comprobé por programa (cada cita aparece literal en la obra).</li>
<li>Quité marcas editoriales de la digitalización (notas, números, marcadores «AUTO»). La página impresa la deduzco de los marcadores de OpenITI (el marcador cierra la página; lo comprobé así en <i>Al-Jawab al-Sahih</i>). <b>Las 14 citas de <i>Al-Jawab al-Sahih</i> las cotejé a ojo con el escaneo de la edición</b> (Dar al-\'Asima): coinciden, con una sola letra corregida (IT11). <b>Las otras 22 solo están verificadas contra OpenITI</b>, con la página por esa misma regla.</li>
<li>Las fuentes cristianas (credos, Padres, Tomás de Aquino, Calcedonia, Nicea II, Biblia del Rey Jacobo) son traducciones inglesas de dominio público; comprobé cada cita por programa contra el texto descargado.</li>
<li>Valoraciones de especialistas (Zwirahn 2018, Rayan y Baraijia 2026, Husseini 2011, Bogataj 2019): las leyó un investigador; las cito como secundarias.</li>
</ul></div>
<div class="pn"><h4>Límites y qué quedó fuera</h4><ul class="l" style="font-size:17px">
<li><b>Traducciones al español mías</b>, desde el árabe. En pasajes sobre cristianos, solo cito lo que él dice; los veredictos son míos.</li>
<li><b>Dos cartas, no toda la tradición cristiana</b>: lo que Ibn Taymiyya conoce son la carta de Pablo de Antioquía y la de al-Hasan ibn Ayyub (un converso). No cotejé el árabe de la carta de Pablo (ed. Khoury, 1964).</li>
<li><b>Fuera</b>: pasajes de insulto o de violencia (por ejemplo, la frase en que dice que quien confunde atributo y sustancia merece el tratamiento de los locos), y el material que repetía lo ya citado.</li>
<li>No juzgo el islam: solo la coherencia de lo que dice sobre los cristianos y su teoría del conocimiento.</li>
<li>Algunos puntos son <b>lecturas mías</b> (marcadas): por ejemplo, la relatividad del tawatur o la simplicidad divina.</li>
</ul></div></div>'''
page(OUT, 'IT99_es', 'IT99', 'Fuentes, límites y avisos', 'Resumen en español',
     'Qué leí, qué dejé fuera y qué hay que tener en cuenta',
     'Resumen honesto del método y de sus límites.', body,
     'Fuentes: OpenITI (Shamela), ediciones de Dar al-\'Asima, Majma\' al-Malik Fahd, Dar al-Kutub al-\'Ilmiyya y otras; CCEL, New Advent, Fordham; Biblia del Rey Jacobo (bible-api).<br>' + PACK, head_cls='alt')
print('itstatic ok')
