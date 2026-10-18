# -*- coding: utf-8 -*-
# Empaqueta el pack «Las críticas históricas al matrimonio de Mahoma con Aisha por su edad» en el repositorio
import sys, os, shutil, json, glob
AY = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ay'
HB = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb'
sys.path.insert(0, AY)
from PIL import Image
from ayfigs import FIGS
import aystatic as S
R = '/home/user/Pruebas/aisha-criticas-historicas-edad-matrimonio'
os.chdir(AY)
for d in ('', '/imagenes', '/herramientas', '/herramientas/briefs_agentes', '/herramientas/datos_agentes'):
    os.makedirs(R + d, exist_ok=True)
TN = {'E': 'Edad de Aisha', 'L': 'Esposas y lujuria', 'N': 'Aisha nombrada', 'M': 'Fuente musulmana'}
order = ['AE00_es']
for f in FIGS: order += [f['id'] + '_cita', f['id'] + '_info']
order += ['AE13_es', 'AE14_es', 'AE15_es', 'AE99_es']
files = [o + '.png' for o in order]
for f in files:
    assert os.path.exists('aycards/' + f), f
    shutil.copy('aycards/' + f, R + '/' + f)
for f in glob.glob('aycards/img/*.jpg'):
    shutil.copy(f, R + '/imagenes/' + os.path.basename(f))
for t in ['gen.py', 'gen2.py', 'oilib.py', 'aydata.py', 'ayfigs.py', 'aypad.py', 'aystatic.py', 'ayrun.py', 'aychk.py', 'packay.py', 'renderhb.js']:
    if os.path.exists(t): shutil.copy(t, R + '/herramientas/' + t)
for t in glob.glob('V/*.json'):
    shutil.copy(t, R + '/herramientas/' + os.path.basename(t))
for t in ('hbcss.py', 'genpad.py'):
    shutil.copy(f'{HB}/{t}', R + '/herramientas/' + t)
for y in [f'A{i}' for i in range(1, 12)] + ['B1', 'B2']:
    if os.path.exists(f'{y}.txt'): shutil.copy(f'{y}.txt', R + f'/herramientas/briefs_agentes/{y}.txt')
    for n in ('figures.json', 'works.json', 'passages.json', 'excluded.json', 'notes.md'):
        if os.path.exists(f'{y}/{n}'): shutil.copy(f'{y}/{n}', R + f'/herramientas/datos_agentes/{y}_{n}')
def pdf(name, w, q):
    ims = []
    for f in files:
        im = Image.open('aycards/' + f).convert('RGB')
        if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        ims.append(im)
    ims[0].save(R + '/' + name, save_all=True, append_images=ims[1:], resolution=120, quality=q)
    return os.path.getsize(R + '/' + name) / 1e6
PDF = 'aisha_criticas_historicas_edad_matrimonio.pdf'
mb = pdf(PDF, 1200, 72)
print('pdf MB', mb, 'pages', len(files))
assert mb < 30

def cell(s): return str(s).replace('|', '\\|').replace('\n', ' ')
B1_NOTE = open(AY + '/B1_note.txt', encoding='utf-8').read().strip() if os.path.exists(AY + '/B1_note.txt') else ''
out = ['# Las críticas históricas al matrimonio de Mahoma con Aisha por su edad: de las fuentes más tempranas a 1700', '',
 'Documentación, en diapositivas, de **quién criticó por escrito, lo más pronto posible, el matrimonio de Mahoma con Aisha por su corta edad o por la diferencia de edad**: textos siriacos, griegos, armenios, latinos, árabes cristianos, castellanos y modernos, y también fuentes musulmanas que registran objeciones. El punto de partida fue una página de la traducción francesa (1574) de Juan Andrés que me pasaron; el pack busca su origen y a quienes vinieron antes y después. Hay **%d figuras o textos**, cada uno con **dos diapositivas**: `AExx_cita.png` (las citas traducidas al español, con la frase clave subrayada) y `AExx_info.png` (imagen de la página o portada, obra, texto original, fuente y «aclaración de la cita»). Además: un resumen (`AE00`), un **mapa de lo que dijo cada fuente, con los resultados negativos** (`AE13`), dos diapositivas de **conclusiones para un post** (`AE14`, `AE15`) y una de fuentes y límites (`AE99`).' % len(FIGS), '',
 f'Todo junto en un PDF ({mb:.0f} MB): [`{PDF}`]({PDF}). Orden de las páginas: `AE00`; `AExx_cita` y `AExx_info` por cada figura; `AE13_es`; `AE14_es`; `AE15_es`; `AE99_es`.', '',
 '**Resultado en pocas palabras** (el detalle y los textos están en las diapositivas):', '',
 '- **Antes de 1515, con fecha segura, no encontré a ningún cristiano que critique expresamente la edad de Aisha.** Lo anterior que leí ataca las cuatro esposas, las concubinas y la «lujuria» de Mahoma (Juan Damasceno, c. 740; Zigabeno; Coniates; Cusa) y a Aisha solo la nombra como la más joven y la única virgen: la *Apología de al-Kindi* (s. IX, autoría y fecha discutidas) y Riccoldo da Monte di Croce (c. 1300: «virgen y todavía jovencita»). Los textos siriacos, griegos y armenios del s. VII–VIII que leí no hablan de sus esposas.',
 '- Un **tratado castellano atribuido a Pedro Pascual** (obispo de Jaén, m. 1300), *Sobre la seta mahometana*, dice que Axa «no avia mas de siete años» al casarse y «no avie aun sino diez años» al consumar. Sería el texto cristiano con edad más temprano, **pero la atribución y la fecha se discuten** y el único manuscrito es una copia del siglo XVI.',
 '- **Juan Andrés** (Valencia, 1515): seis años al contrato y ocho a la consumación; «casi homicida»; Mahoma tenía «siete mujeres juntamente». Es la **crítica explícita más antigua con fecha segura** que encontré, y su página 99 en francés (1574) es la de tu captura. Dice ocho, no nueve, y cita un «libro de Acear» que no pude identificar.',
 '- **Prideaux** (1697): seis y ocho años (cita a Juan Andrés en el margen); los explica por la costumbre de los «países cálidos» y **no condena la edad**: critica la «lujuria» de Mahoma.',
 '- **Las edades vienen de las fuentes musulmanas**: Ibn Ishaq (m. 151 H), Ibn Saʿd y al-Tabari dan seis o siete años al contrato y nueve a la consumación. En el siglo VIII, **Ibn Shubruma** ya no admitía que un padre casara a su hija pequeña y trataba el caso de Aisha como excepción del Profeta (opinión que conocemos por Ibn Hazm, que la rechaza).',
 '- **Lo que no se puede decir**: que los cristianos criticaran la edad de Aisha desde el siglo VII (no hay textos), ni que Prideaux la condene, ni que Juan Andrés diga lo mismo que las fuentes musulmanas (dice ocho, no nueve).', '',
 '**Qué no muestra.** Que la edad sea o no históricamente correcta (las fuentes musulmanas dan cifras distintas y hay cronologías alternativas, ver `AE15`), ni que no existan críticas anteriores en textos que no pude leer. Un resultado negativo («no la nombra») es lo que leyó cada investigador en los pasajes que abrió, no una búsqueda exhaustiva de cada obra.', '',
 '## Las figuras', '', '| Código | Figura | Obra y referencia | Temas | Texto de partida | Diapositivas |', '|---|---|---|---|---|---|']
for f in FIGS:
    th = []
    for q in f['quotes']:
        for t in q['theme']:
            if TN[t] not in th: th.append(TN[t])
    works = ' / '.join(dict.fromkeys(q['work'] for q in f['quotes']))
    refs = '; '.join(dict.fromkeys(q['ref'] for q in f['quotes']))
    srcs = '; '.join(dict.fromkeys((q['trans'] + (' · ' + q['url'] if q.get('url') else '')) for q in f['quotes']))
    out.append(f"| {f['id']} | {cell(f['name'])} ({cell(f['dates'])}) | {cell(works)} — {cell(refs)} | {', '.join(th)} | {cell(srcs)} | [cita]({f['id']}_cita.png) · [obra]({f['id']}_info.png) |")
out += ['', '## Cómo se hizo', '',
 'Un orquestador (yo) y **13 investigadores** (modelo Haiku, nivel alto) en dos tandas. **Primera tanda (11)**: A1 y A2, fuentes musulmanas primitivas (objeciones y cronología de la edad); A3, polémica y teología musulmana que registra o responde a objeciones; A4, textos siriacos, griegos y armenios (630–800); A5, siriacos, árabes cristianos, coptos y judíos (800–1300); A6, bizantinos (800–1500); A7, latinos (700–1200); A8, latinos y románicos (1200–1500); A9, Juan Andrés y la tradición ibérica; A10, Reforma y siglo XVII; A11, bibliografía académica y pistas. **Segunda tanda (2)**, dirigida a los huecos: B1, Lutero y el latín original de Riccoldo; B2, autores ibéricos medievales (Espina, Martí, Pascual, Pérez de Chinchón) y otros pasajes de Juan Andrés. Sus encargos están en `herramientas/briefs_agentes/` y lo que devolvieron (autores, obras, pasajes, exclusiones y notas), en `herramientas/datos_agentes/`.', '',
 '**Yo elegí las figuras y las citas** de entre lo que reunieron, traduje al español y redacté las aclaraciones y las conclusiones. **Comprobé yo mismo en la imagen de la página**: Juan Andrés (ejemplar de 1515 de la Biblioteca del Congreso, imágenes 182–183), Riccoldo (Basilea, 1550, p. 7 de su sección), Pascual (ed. de Armengol, 1908, pp. 30–31) y Prideaux (1698, pp. 53, 54 y 158). El árabe de al-Kindi y de Ibn Hazm lo corté por programa del texto de OpenITI (`herramientas/oilib.py`) y comprobé que aparece literal en la obra. `herramientas/aychk.py` verifica que cada frase entre « » de las diapositivas de resumen figura, tal cual, en las citas traducidas.', '',
 '## Lo que dejé fuera y por qué', '',
 '- **Pasajes sexualmente explícitos o violentos**, y los tramos de Riccoldo, Pascual y otros que acusan a Aisha de adulterio (el Corán, 24:11-20, la declara inocente y las propias fuentes cristianas lo recogen después). Citarlos sin ese contexto habría sido engañoso.',
 '- **Textos que nombran a Aisha sin edad ni crítica** (por ejemplo, la *Chronica mendosa* del círculo de Pedro el Venerable, hacia 1143, que la llama «Ayska»; Bartolomé de Edesa, que la llama «Aise»; Vives; Reland): están en el mapa `AE13`, no tienen diapositiva propia.',
 '- **Críticas generales a las esposas sin Aisha** (Juan Damasceno, Zigabeno, Coniates, Jacques de Vitry, Cusa, Torquemada): aparecen en el mapa como contexto, no como críticas a su edad.',
 '- **Pistas sin comprobar**: Espina (*Fortalitium fidei*, 1459–60) nombra a una esposa «Ayosse, hija de Hebeboz» (la identifico con Aisha por el nombre del padre y la pareja con Hafsa, pero el texto no dice «Aisha» ni da edad); Lutero y Bibliander (ver nota abajo); Ramón Martí, Pérez de Chinchón, Obregón y otros no pudieron leerse (sin texto accesible).',
 '- **Posterior a 1700**: Reland (1705, «única virgen»), Boulainvilliers (1730, «muy joven», solo OCR) y Gagnier (1732, siete y nueve, narración neutra) están en el mapa, sin diapositiva.']
if B1_NOTE: out += ['- ' + B1_NOTE]
out += ['', '## Límites y avisos', '',
 '1. **Traducciones al español mías**, del árabe, latín, castellano antiguo, francés e inglés.',
 '2. **Pascual (AE04)**: la atribución a Pedro Pascual y la fecha de 1300 vienen de una nota añadida al manuscrito y del editor (Armengol, 1908); el único manuscrito es una copia del siglo XVI cuyo copista, según el editor, modernizó la ortografía. Un investigador encontró referencias (de segunda mano, que no pude comprobar) a un estudio reciente que lo considera de otra mano y de la segunda mitad del siglo XIV. El latín que la edición imprime al lado es una traducción del siglo XVII.',
 '3. **Riccoldo (AE03)**: el latín de Basilea (1550) es una retraducción desde el griego de Demetrio Cidones, que a su vez tradujo el latín de Riccoldo; no es el latín original (que no leí). La edad no figura, solo «todavía jovencita».',
 '4. **Al-Kindi (AE02)**: la autoría y la fecha del texto se discuten; el texto de OpenITI es una transcripción de una web (alkalema.net), sin edición impresa indicada ni paginación. Muir (1882) solo resume el pasaje en inglés.',
 '5. **Juan Andrés (AE05)**: escribe como converso polemista, no como fuente neutral; dice que lo prueba por un «libro de Acear» (Azar en la versión inglesa de 1652) que no pude identificar. Un investigador mencionó, de segunda mano y sin que yo lo comprobara, que algunos estudiosos han discutido su identidad histórica; por eso no lo uso en las diapositivas. La transcripción del francés de 1574 (p. 99) es mía, de la captura que me enviaron, sin otro escaneo para compararla.',
 '6. **Ibn Shubruma (AE01)**: su opinión llega por Ibn Hazm (siglo XI, unos tres siglos después); la fecha de su muerte (144 H) es la de los repertorios biográficos y no la comprobé en esta pasada. Su objeción es jurídica, no moral. La página impresa que figura (marcador + 1) la deduzco de los marcadores de OpenITI: esa regla la comprobé en otra obra (*Al-Jawab al-Sahih*, con escaneos), no en el *Muhalla*, donde puede haber un desfase de una página.',
 '7. **Fuentes musulmanas sobre la edad** (mapa `AE13` y conclusión 3): provienen del trabajo del investigador A2 sobre OpenITI (Ibn Ishaq, recensión de Yunus, 6/9/18; al-Tabari, 6 con variante 7; Ibn Saʿd, 6, 7 y 9; Ibn Hisham, 7 y 9 o 10). Los pasajes están en `datos_agentes/A2_passages.json`; no los cotejé con escaneos. La edad de Asma (unos cien años al morir en 73 H) y la cronología que de ella se deduce no encajan con las fechas de Ibn Saʿd; no se presentan como hecho. Los textos legales y de hadiz sobre el matrimonio de menores están en el pack `matrimonio-infantil`.',
 '8. **Imágenes**: son recortes de las páginas leídas, con el subrayado amarillo mío (salvo el de la captura de 1574, que venía en la imagen recibida). El ejemplar de Riccoldo está en un escaneo de archive.org que lleva un aviso de derechos de la Newberry Library; el libro es de 1550.',
 '9. **Lo anterior no es una valoración** de si la edad es históricamente correcta ni un juicio sobre el islam: solo documenta quién lo dijo, cuándo y con qué texto.', '',
 '## Imágenes y créditos', '', '| Figura | Imagen | Crédito |', '|---|---|---|']
for f in FIGS:
    if f.get('imgs'):
        out.append(f"| {f['id']} {cell(f['name'])} | {', '.join('`imagenes/' + i + '`' for i in f['imgs'])} | {cell(f['credit'])} {cell(f.get('img_note', ''))} |")
    else:
        out.append(f"| {f['id']} {cell(f['name'])} | portada tipográfica | {cell(f['credit'])} |")
out += ['', '## Licencias y derechos', '',
 'Textos citados en extractos breves, con su fuente: OpenITI (Shamela), Biblioteca del Congreso (ejemplar Rosenwald 1275: «The Library of Congress is not aware of any U.S. copyright or any other restrictions»), archive.org (Basilea, 1550; Armengol, 1908, con marca de dominio público; Prideaux, 1698). Las traducciones al español son mías.', '',
 'Herramientas en `herramientas/`: `gen.py` y `gen2.py` (generan los encargos), `oilib.py` (lectura de OpenITI con página impresa corregida), `aydata.py` (datos de las figuras con las traducciones), `ayfigs.py` (orden y códigos), `aypad.py` y `aystatic.py` (generan las diapositivas), `ayrun.py`, `aychk.py` (comprobación de frases), `packay.py` (este empaquetado), `renderhb.js` (convierte en PNG; requiere Playwright y las fuentes Amiri y Noto Naskh Arabic), `hbcss.py` y `genpad.py` (CSS base) y `ibnhazm_q.json`/`kindi_q.json` (el árabe cortado por código).']
open(R + '/README.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(files), 'diapositivas')
