# -*- coding: utf-8 -*-
# Empaqueta el pack «La Iglesia Ortodoxa ante el Islam, 1084–1700» en el repositorio
import sys, os, shutil, json, glob
OX = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ox'
HB = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb'
sys.path.insert(0, OX)
from PIL import Image
from oxfigs import FIGS
R = '/home/user/Pruebas/iglesia-ortodoxa-islam-1084-1700'
os.chdir(OX)
for d in ('', '/imagenes', '/herramientas', '/herramientas/briefs_agentes', '/herramientas/datos_agentes'):
    os.makedirs(R + d, exist_ok=True)
CRED = json.load(open('credits.json', encoding='utf-8'))
TN = {'M': 'Mahoma', 'Q': 'Corán y doctrina', 'S': 'Cómo se extendió', 'H': 'El Islam como religión'}
order = ['OI00_es']
for f in FIGS: order += [f['id'] + '_cita', f['id'] + '_info']
order += ['OI11_es', 'OI12_es', 'OI99_es']
files = [o + '.png' for o in order]
for f in files:
    assert os.path.exists('oxcards/' + f), f
    shutil.copy('oxcards/' + f, R + '/' + f)
for f in FIGS:
    shutil.copy(f'IMG/small/{f["slug"]}.jpg', R + f'/imagenes/{f["slug"]}.jpg')
for t in ['gen.py', 'oxdata.py', 'oxdata_extra.py', 'oxdata_extra2.py', 'oxfigs.py', 'oxpad.py', 'oxstatic.py', 'oxrun.py', 'oxchk.py', 'imgs.py', 'imgs3.py', 'imgs4.sh', 'imgs5.sh', 'imgs6.sh', 'imgs7.sh', 'lic.py', 'cv.py', 'renderhb.js', 'packox.py', 'credits.json']:
    if os.path.exists(t): shutil.copy(t, R + '/herramientas/' + t)
shutil.copy('IMG/lic.json', R + '/herramientas/lic.json')
for t in ('hbcss.py', 'genpad.py'):
    shutil.copy(f'{HB}/{t}', R + '/herramientas/' + t)
for i in range(1, 12):
    shutil.copy(f'O{i}.txt', R + f'/herramientas/briefs_agentes/O{i}.txt')
    for n in ('figures.json', 'works.json', 'passages.json', 'excluded.json'):
        if os.path.exists(f'O{i}/{n}'): shutil.copy(f'O{i}/{n}', R + f'/herramientas/datos_agentes/O{i}_{n}')
def pdf(name, w, q):
    ims = []
    for f in files:
        im = Image.open('oxcards/' + f).convert('RGB')
        if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        ims.append(im)
    ims[0].save(R + '/' + name, save_all=True, append_images=ims[1:], resolution=120, quality=q)
    return os.path.getsize(R + '/' + name) / 1e6
mb = pdf('iglesia_ortodoxa_islam_1084_1700.pdf', 1200, 72)
print('pdf MB', mb, 'pages', len(files))

def cell(s): return s.replace('|', '\\|').replace('\n', ' ')
out = ['# La Iglesia Ortodoxa ante el Islam, 1084–1700: lo que dijeron sus grandes figuras', '',
 'Documentación, en diapositivas, de lo que dijeron sobre Mahoma, el Corán y el Islam **diez figuras de la Iglesia Ortodoxa posteriores al Cisma de 1054** (entre c. 1100 y 1585): dos emperadores (Juan VI Cantacuceno, Manuel II Paleólogo), tres santos de la Iglesia Ortodoxa (Gregorio Palamás, Simeón de Tesalónica, Máximo el Griego), un monje teólogo (Eutimio Zigabeno), un monje y canonista (Juan Zonaras), un secretario imperial (Miguel Glicas), un alto funcionario (Nicetas Coniates) y un metropolitano (Macario Melisseno). **Sin Juan Damasceno** (ya está en el pack católico) y sin nadie anterior al Cisma, católicos convertidos, protestantes ni Cirilo Lúcaris. Se buscó a los más relevantes y a los que hablan con más dureza **que tienen texto de dominio público accesible**. Cada figura tiene **dos diapositivas**: `OIxx_cita.png` (solo las citas, traducidas al español, con la frase clave subrayada) y `OIxx_info.png` (retrato, obra, fecha, referencia, texto de partida y «aclaración de la cita»). Al final hay dos diapositivas de **conclusiones para un post** (`OI11`, `OI12`), pensadas para exponerlas al público, y una de fuentes y límites (`OI99`).', '',
 f'Todo junto en un PDF ({mb:.0f} MB): [`iglesia_ortodoxa_islam_1084_1700.pdf`](iglesia_ortodoxa_islam_1084_1700.pdf). Páginas: `OI00` (resumen con retratos), `OIxx_cita` y `OIxx_info` por cada figura (OI01–OI10), `OI11` y `OI12` (conclusiones) y `OI99` (fuentes, límites y avisos).', '',
 '**Qué muestran.** Que, en casi cinco siglos, las figuras citadas coinciden en lo esencial: no reconocen a Mahoma como profeta (falso profeta, a veces «anticristo»), le atribuyen una inspiración diabólica o de un monje hereje, tachan su ley y su libro de fábulas y desvaríos, explican su éxito por la espada más que por milagros y le niegan la Trinidad y la divinidad de Cristo. Las conclusiones de `OI11` y `OI12` resumen eso, cada punto con las frases de cada autor y su código.', '',
 '**Qué no muestran.** Que esas afirmaciones sean ciertas: son juicios y polémica de monjes, emperadores, historiadores y obispos bizantinos y postbizantinos, casi siempre sin fuentes árabes; varias (el monje desterrado, la epilepsia, el «monje arriano») pertenecen a una tradición polémica que la investigación actual no da por establecida. Tampoco son la **posición actual de las Iglesias Ortodoxas**: no revisé declaraciones actuales; las conclusiones están formuladas como «lo que dijeron» y no como veredicto histórico.', '',
 '**Aviso sobre la fuerza del conjunto.** El corpus ortodoxo de dominio público sobre el Islam posterior al Cisma es más escaso que el católico. **Las primeras nueve figuras son sólidas** (tienen pasajes duros y claros, comprobados contra la página donde hay griego o latín de dominio público; con las salvedades de traducción de más abajo). **La décima, Macario Melisseno, es la más débil**: su «Crónica mayor» incluye una polémica contra Mahoma cuyo autor no está identificado (es una interpolación) y es una obra compilada, no un tratado suyo; está marcada así en su diapositiva. Prefiero decirlo a rellenar el hueco con una figura que no dice nada duro (por ejemplo, Genadio Escolario).', '',
 '## Las diez figuras', '', '| Código | Figura | Obras y referencias | Temas | Texto de partida y fuente | Diapositivas |', '|---|---|---|---|---|---|']
for f in FIGS:
    th = []
    for q in f['quotes']:
        for t in q['theme']:
            if TN[t] not in th: th.append(TN[t])
    works = ' / '.join(dict.fromkeys(q['work'] for q in f['quotes']))
    refs = works + ' — ' + '; '.join(dict.fromkeys(q['ref'] for q in f['quotes']))
    srcs = '; '.join(dict.fromkeys(f"{q['trans']} · {q['url']}" for q in f['quotes']))
    out.append(f"| {f['id']} | {cell(f['name'])} ({f['dates']}) — {cell(f['role'])} | {cell(refs)} | {', '.join(th)} | {cell(srcs)} | [cita]({f['id']}_cita.png) · [obra]({f['id']}_info.png) |")
out += ['', '## Cómo se hizo', '',
 'Un orquestador y **11 investigadores** (modelo pequeño, nivel alto; la petición era de 8, pero hizo falta cubrir más autores y repetir dos encargos): O1 Zigabeno y Coniates; O2 Palamás; O3 Cantacuceno; O4 Manuel II; O5 Brienio y panorama general; O6 Escolario, Ducas y Sfrantzes; O7 Máximo el Griego y fuentes eslavas y georgianas; O8 postbizantinos de 1500–1700; O9 Palamás (segunda pasada) y Simeón de Tesalónica; O10 cronistas bizantinos (Zonaras, Glicas, Coniates, Gregoras, Calcocondilas…); O11 ortodoxos de 1453–1700, neomártires y Nicusio. Dos de los primeros encargos (O1, O3) fallaron por el límite semanal de la herramienta y se relanzaron. Sus encargos están en `herramientas/briefs_agentes/` y lo que devolvieron (autores, obras, pasajes, exclusiones), en `herramientas/datos_agentes/`.', '',
 'Yo **elegí las diez figuras y las citas** de entre los pasajes que reunieron (los más conocidos y los de juicio más duro), traduje al español y redacté las aclaraciones. El griego de los investigadores se lee mal en los textos digitalizados, así que lo comprobé **mirando yo mismo la imagen de la página**: Zigabeno (Migne PG 130, cols. 1333–1334 y 1339–1342), Zonaras (Dindorf, pp. 311–312), Glicas (Bekker, pp. 513–514), Coniates (Bekker, pp. 278–279), Cantacuceno (ed. de Basilea 1543, pp. 78, 79 y 107), Palamás (*Neos Hellenomnemon* 16, 1922, pp. 17 y 19) y Melisseno (Bekker, pp. 295 y 343–344). Donde incluyo el griego (`Original` en la diapositiva `info`) es el que leí en la imagen. Simeón de Tesalónica lo cito desde el latín que Migne imprime junto al griego, leído en el texto digitalizado y no en la imagen (el griego del OCR no era legible); Manuel II, desde la traducción inglesa de Roger Pearse (2009); Máximo el Griego, desde la traducción rusa de 1910. Los retratos se bajaron de Wikimedia Commons (y, el de Zigabeno, de Wikipedia en inglés) por las páginas HTML de cada figura, a tamaño de miniatura estándar, y de las fichas de Commons comprobé la licencia de cada uno (`herramientas/lic.json`).', '',
 '## Lo que dejé fuera y por qué', '',
 '- **Autores y obras fuera de los diez**:',
 '  - *Juan Damasceno* (a petición, ya está en el pack católico) y los pasajes de la *Thesaurus* de Coniates que reproducen a Damasceno.',
 '  - *Gregorio Escolario / Genadio II*: su «Confesión de fe» a Mehmed II es serena (dureza baja); la «Confesión I» tiene autoría discutida y el griego de Migne no era legible.',
 '  - *Miguel Ducas*: historiador con pasajes duros, pero ardiente unionista (partidario de la unión con Roma); no lo tomé por voz ortodoxa fiable.',
 '  - *Jorge Sfrantzes*: el pasaje de la *Crónica mayor* no es suyo (es de la compilación de Melisseno); por eso lo uso como Melisseno y no como Sfrantzes.',
 '  - *Nicéforo Grégoras*, *Juan Calecas*: pasajes descriptivos o de tono histórico, no de doctrina contra el Islam.',
 '  - *José Brienio*, *Macario Macris*, *Pacomio Rusano*, *Pseudo-Doroteo*, *Teófilo Coridaleo*, *Zacarías Gergano*: sus textos sobre el Islam solo están en manuscrito o en ediciones con derechos, o no pude comprobarlos.',
 '  - *Panagiotis Nikusios* (Diálogo de 1662, Pandora 1868): obra anónima o de su círculo, casi toda en la voz de su interlocutor musulmán; las líneas suyas son de dureza baja.',
 '  - *Sinaxarista* (Nicodemo, 1868): las vidas de neomártires que mencionan a Mahoma se limitan a confesiones breves o a insultos; no hay doctrina.',
 '- **Pasajes que piden matar o hacer la guerra** (se registran en los `excluded.json` de `datos_agentes/`): por ejemplo, el discurso de guerra de Coniates, la cláusula de pena de muerte que la *Crónica mayor* pone en boca de Mahoma (la cita OI10 se corta antes) y los exhortos de Ducas.',
 '- **Insultos a pueblos enteros o a la persona**: Simeón sobre «inmundo y bárbaro» y las acusaciones de sodomía, Máximo el Griego («perro», «pueblo impío»), los epítetos «necio» e «impudente» de Cantacuceno.',
 '- **Leyendas**: el «monje arriano» y la epilepsia de Mahoma aparecen en Zonaras, Glicas y Melisseno; se citan como lo que dijeron y están marcadas como polémica.', '',
 '## Límites y avisos', '',
 '1. **Traducciones al español mías**, desde el griego, el latín y el ruso; en Manuel II, desde el inglés de Pearse (autodeclarado de dominio público, 2009). El griego del *Diálogo VII* de Manuel II solo está en ediciones con derechos (Trapp, 1966; Khoury), así que no muestro el griego. Solo Pearse tiene traducción inglesa libre; en el resto no hay otra que haya leído.',
 '2. **Dos autorías discutidas.** Los *Cuatro discursos contra Mahoma* se atribuyen a Cantacuceno, pero su autoría se debate; el libro IV de la *Crónica mayor* contiene una polémica interpolada de autor no identificado, dentro de una obra compilada por Melisseno (Pseudo-Sfrantzes, hacia 1573–75, en Nápoles). Por eso la última figura es la más débil (ver más arriba).',
 '3. **Cantacuceno (OI05)**: traduzco del latín de Gwalther (1543) cotejado con la imagen del griego (el tipo de imprenta de la época, con ligaduras, es poco legible, por eso no muestro el griego); la cita 3 (el diablo homicida) está en la p. 107.',
 '4. **Simeón de Tesalónica (OI08)**: solo el latín de Migne, del texto digitalizado (con errores de OCR que cotejé entre sí) y no de la imagen de la página. Omito el comienzo («hombre inmundo y bárbaro») y el resto de insultos del capítulo.',
 '5. **Máximo el Griego (OI09)**: traducción rusa de 1910 de textos que se conservan en eslavo eclesiástico; no leí el original eslavo ni griego alguno.',
 '6. **Coniates (OI04)**: lo que dice sobre el «Dios de Mahoma» es su relato de la polémica sobre la fórmula de bautismo (c. 1180); su opinión («delirante y demoníaco», «no diría teología») va en su propia voz.',
 '7. **Zonaras y Glicas (OI02, OI03)** repiten la tradición bizantina sobre el origen de Mahoma (un monje herético, la epilepsia); no la respaldan fuentes árabes.',
 '8. **Fechas aproximadas** (convencionales); no las verifiqué una a una. **Retratos**: iconografía y miniaturas de dominio público; ninguno es un retrato en vida salvo, quizá, la miniatura de Cantacuceno (hecha en sus últimos años). Donde no hay retrato libre se muestra la portada de la edición (Glicas, Melisseno) o una página de un manuscrito (Zigabeno). Ver los créditos más abajo.',
 '9. Las conclusiones de `OI11` y `OI12` resumen lo que dijo cada autor y llevan la nota correspondiente al pie. Cada frase entre comillas del resumen figura, traducida, en la diapositiva de la figura (la comprueba `herramientas/oxchk.py`).', '',
 '## Retratos y créditos', '', '| Figura | Crédito | Nota |', '|---|---|---|']
for f in FIGS:
    c = CRED[f['slug']]
    out.append(f"| {f['id']} {f['name']} | {cell(c['credit'])} | {cell(c['note'])} |")
out += ['', '## Licencias y derechos', '',
 'Textos citados en extractos breves, con su fuente: Migne (*Patrologia Graeca*, 130, 154–155), Bekker (*Corpus Scriptorum Historiae Byzantinae*, Bonn, 1835–1838), Dindorf (Bonn, 1868), impreso de Basilea de 1543 (Cantacuceno, Biblioteca Jagellónica), *Neos Hellenomnemon* 16 (1922; digitalización con licencia CC BY 4.0), traducción inglesa de Roger Pearse (2009, autodeclarada de dominio público), traducción rusa de 1910 (azbyka.ru). Las traducciones al español son mías.', '',
 'Herramientas en `herramientas/`: `gen.py` (genera los encargos), `oxdata.py`, `oxdata_extra.py` y `oxdata_extra2.py` (datos de las diez figuras con las traducciones), `oxfigs.py` (orden y códigos), `oxpad.py`, `oxstatic.py` y `oxrun.py` (generan las diapositivas), `oxchk.py` (comprueba que cada frase entre comillas de los resúmenes está en las citas), `imgs*.py`/`imgs*.sh` y `lic.py` (retratos y licencias), `cv.py` (lectura de los datos de los investigadores) y `renderhb.js` (convierte en PNG). Requieren `hbcss.py` y `genpad.py` (incluidos) y, para el CSS base, el fichero `genv.py` del pack de capturas, que no se incluye.']
open(R + '/README.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(files), 'diapositivas')
