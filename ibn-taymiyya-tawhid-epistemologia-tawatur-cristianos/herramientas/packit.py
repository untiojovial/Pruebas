# -*- coding: utf-8 -*-
# Empaqueta el pack «Ibn Taymiyya: tawhid, epistemología, tawatur y su refutación de los cristianos» en el repositorio
import sys, os, shutil, json
IT = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/it'
HB = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb'
sys.path.insert(0, IT)
from PIL import Image
import itfigs, itstatic
from itfigs import FIGS
R = '/home/user/Pruebas/ibn-taymiyya-tawhid-epistemologia-tawatur-cristianos'
os.chdir(IT)
for d in ('', '/herramientas', '/herramientas/briefs_agentes', '/herramientas/datos_agentes'):
    os.makedirs(R + d, exist_ok=True)
TN = {'T': 'Tawhid', 'E': 'Epistemología', 'W': 'Tawatur', 'C': 'Cristianos'}
order = ['IT00_es']
for f in FIGS: order += [f['id'] + '_cita', f['id'] + '_info']
order += ['IT13_bal', 'IT14_es', 'IT15_es', 'IT99_es']
files = [o + '.png' for o in order]
for f in files:
    assert os.path.exists('itcards/' + f), f
    shutil.copy('itcards/' + f, R + '/' + f)
for t in ['gen.py', 'itlib.py', 'itsrc.py', 'itpages.py', 'itbase.py', 'itdata1.py', 'itdata2.py', 'itfigs.py', 'itpad.py', 'itstatic.py', 'itrun.py', 'itchk.py',
          'renderhb.js', 'packit.py', 'ibntaymiyya_openiti.tsv', 'oimeta.csv']:
    if os.path.exists(t): shutil.copy(t, R + '/herramientas/' + t)
for t in ('hbcss.py', 'genpad.py'):
    shutil.copy(f'{HB}/{t}', R + '/herramientas/' + t)
for i in range(1, 12):
    shutil.copy(f'T{i}.txt', R + f'/herramientas/briefs_agentes/T{i}.txt')
    for n in ('works.json', 'passages.json', 'excluded.json', 'notes.md'):
        if os.path.exists(f'T{i}/{n}'): shutil.copy(f'T{i}/{n}', R + f'/herramientas/datos_agentes/T{i}_{n}')
def pdf(name, w, q):
    ims = []
    for f in files:
        im = Image.open('itcards/' + f).convert('RGB')
        if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        ims.append(im)
    ims[0].save(R + '/' + name, save_all=True, append_images=ims[1:], resolution=120, quality=q)
    return os.path.getsize(R + '/' + name) / 1e6
PDF = 'ibn_taymiyya_tawhid_epistemologia_tawatur_cristianos.pdf'
mb = pdf(PDF, 1200, 72)
print('pdf MB', mb, 'pages', len(files))
assert mb < 30

def cell(s): return str(s).replace('|', '\\|').replace('\n', ' ')
nq = sum(len(f['quotes']) for f in FIGS)
assert nq == 36 and len(FIGS) == 12
bal = itstatic.BAL
cnt = {k: sum(1 for b in bal if b[2] == k) for k in ('fiel', 'parcial', 'paja', 'nov')}
jawab_checked = sum(1 for f in FIGS for q in f['quotes'] if 'Al-Jawab' in q['ref'])
works_all = []
for f in FIGS:
    for q in f['quotes']:
        w = q['ref'].split(', ')[0]
        if w not in works_all: works_all.append(w)
out = ['# Ibn Taymiyya: tawhid, epistemología, tawatur y su refutación de los cristianos', '',
 'Documentación, en diapositivas, de **lo que escribió Ibn Taymiyya (661–728 H / 1263–1328)** sobre el **tawhid**, la **epistemología** (razón y revelación, fitra, lógica griega), el **tawatur** y, sobre todo, **cuando intenta refutar a los cristianos y la Trinidad**, con una pregunta de fondo: **¿hace hombres de paja?** Son **12 temas** (IT01–IT12), con **3 citas cada uno** (%d citas en total, de %d obras), todas en árabe tomadas del texto digital de OpenITI y traducidas al español. Cada tema tiene **dos diapositivas**: `ITxx_cita.png` (las citas, traducidas, con la frase clave subrayada) y `ITxx_info.png` (portada de la obra, árabe original, fuente, aclaración de la cita y, en los temas sobre cristianos, **qué dicen los credos y los Padres y un veredicto «¿hombre de paja?»**). Además: un resumen (`IT00`), un **cuadro de balance** (`IT13`), dos diapositivas de **conclusiones para un post** (`IT14`, `IT15`) y una de fuentes y límites (`IT99`).' % (nq, len(works_all)), '',
 f'Todo junto en un PDF ({mb:.0f} MB): [`{PDF}`]({PDF}). Orden de las páginas: `IT00`; `ITxx_cita` y `ITxx_info` por cada tema (IT01–IT12); `IT13_bal`; `IT14_es`; `IT15_es`; `IT99_es`.', '',
 '**Resultado en pocas palabras** (el detalle y los textos están en las diapositivas):', '',
 f'- Sobre los cristianos se valoraron **{len(bal)} afirmaciones concretas** de Ibn Taymiyya (`IT13`): **{cnt["fiel"]} fieles** a las fuentes cristianas, **{cnt["parcial"]} parcialmente fieles**, **{cnt["paja"]} hombre de paja** y **{cnt["nov"]} no verificable**. Es decir: **no es un hombre de paja sistemático**, pero tiene **fallos concretos**.',
 '- **Donde acierta**: cita con exactitud la carta que responde (de Pablo de Antioquía, obispo melquita de Sidón), resume bien la fórmula melquita («una sola persona y dos naturalezas», Calcedonia) y **reconoce que los cristianos no dicen «tres dioses»**.',
 '- **Donde falla**: (1) toma una **glosa de una carta cristiana árabe** (Padre = existencia, Hijo = Palabra, Espíritu = vida) por «la doctrina», cuando los credos y los Padres hablan de **personas** y no de atributos; (2) de «una sustancia con el Padre» **infiere** «tres sustancias, tres dioses», cosa que el credo de Atanasio y Letrán IV **prohíben decir**; (3) dice que los cristianos **«adoran a María»** y le piden «perdónanos», lo que no cuadra con la oración mariana («ruega por nosotros») ni con Nicea II (adoración solo a Dios): **es el único hombre de paja claro**; (4) afirma que **ningún cristiano presenció la crucifixión**, lo que contradice Juan 19:25-27 y 19:35 (el cuadro lo marca «parcial»: hay base en los sinópticos, donde los discípulos huyen y las mujeres miran de lejos, pero no en Juan).',
 '- En los temas de **tawhid, epistemología y tawatur** (IT01–IT07) no hay «hombres de paja» que valorar: son sus propias ideas y se citan con lo que dicen. Las observaciones críticas que añado ahí van **marcadas «Lectura (mía)»**, para que se distinga la cita de la valoración.', '',
 '**Qué no muestra.** No es una refutación del Islam ni un retrato completo de Ibn Taymiyya. Es un recorte de **12 temas** con citas elegidas por mí; no pretende ser lo único que dijo ni lo más representativo para un musulmán. Tampoco es una valoración teológica de la tesis central (la Trinidad): solo se comprueba **si describe bien lo que los cristianos dicen**.', '',
 '## Los doce temas', '', '| Código | Tema | Obras y referencias (vol., pág. impresa) | Bloque | Veredictos en las citas | Diapositivas |', '|---|---|---|---|---|---|']
VN = {'fiel': 'fiel', 'parcial': 'parcial', 'paja': 'hombre de paja', 'nov': 'no verificable', 'algunos': 'algunos', 'valido': 'válido', 'debil': 'débil'}
for f in FIGS:
    th = []
    for q in f['quotes']:
        for t in q['theme']:
            if TN[t] not in th: th.append(TN[t])
    refs = '; '.join(dict.fromkeys(q['ref'] for q in f['quotes']))
    ver = ', '.join(VN[q['verdict']] for q in f['quotes'] if q['verdict']) or '—'
    out.append(f"| {f['id']} | {cell(f['name'])} | {cell(refs)} | {', '.join(th)} | {ver} | [cita]({f['id']}_cita.png) · [obra]({f['id']}_info.png) |")
out += ['', '## Cómo se hizo', '',
 'Un orquestador (yo) y **11 investigadores** (modelo Haiku, nivel alto) que buscaron los pasajes en el texto digital de las obras: T1 y T2, tawhid (clasificación, atributos, simplicidad, la Palabra de Dios); T3 y T4, epistemología (razón y revelación; fitra; crítica de la lógica griega); T5 y T6, tawatur (su teoría; cómo lo aplica a Torá, Evangelios, crucifixión y Corán); T7, estructura de *Al-Jawab al-Sahih* y la carta de Pablo; T8, sus argumentos contra la Trinidad; T9, **qué dicen de verdad las fuentes cristianas** (para el contraste de hombre de paja); T10, encarnación, cruz, Evangelios y concilios; T11, valoraciones de especialistas. Seis de los encargos se interrumpieron por el límite de uso de la herramienta y se reanudaron después. Sus encargos están en `herramientas/briefs_agentes/` y lo que devolvieron (obras, pasajes, exclusiones, notas), en `herramientas/datos_agentes/`.', '',
 '**Yo elegí los 12 temas y las 36 citas**, escribí las traducciones y las aclaraciones y redacté los veredictos. El **árabe de cada cita se copió por programa** del texto de OpenITI (`herramientas/itsrc.py`, `itbase.py`), limpiado de marcas editoriales, y comprobé que cada cita aparece **literal** en la obra. Las citas de los cristianos (credos, Padres, Tomás de Aquino, Calcedonia, Nicea II, Biblia del Rey Jacobo) son **traducciones inglesas de dominio público**; cada una la comprobé por programa contra el texto descargado (Schaff, *Creeds of Christendom*; NPNF; Fordham; CCEL; New Advent; bible-api). `herramientas/itchk.py` verifica que cada frase entre comillas de las diapositivas de resumen figura, tal cual, en las diapositivas de cada tema.', '',
 '**Comprobación con las páginas impresas.** Para *Al-Jawab al-Sahih* conseguí los escaneos de la edición de Dar al-\'Asima (Arabia Saudí, 2.ª ed., 1419 H/1999, 6 vols.), la misma que sigue el texto de OpenITI, y **cotejé a ojo las %d citas de esa obra con la página impresa** (IT03 cita 2; IT08 citas 1–2; IT09 1–3; IT10 1–3; IT11 1–2; IT12 1–3). Resultado: **coinciden las palabras**, con **una sola diferencia**: en IT11 cita 2 el texto de OpenITI trae «يناقضون» y la página impresa «يتناقضون» («se contradicen»); usé la lectura impresa y la diapositiva lo avisa. **Las otras %d citas (las de *Majmu\' al-Fatawa*, *Dar\' ta\'arud*, *Al-Radd*, *Al-Tadmuriyya*, *Al-Isfahaniyya* y *Al-Wasitiyya*) solo están verificadas contra OpenITI**; no encontré escaneos de esas ediciones con la misma paginación.' % (jawab_checked, nq - jawab_checked), '',
 '**Corrección de páginas.** Los investigadores dieron la página que marca el texto de OpenITI (`PageV03P229`). Al cotejar con los escaneos vi que **ese marcador cierra la página** (el texto que lo sigue está en la página siguiente), así que **todas las referencias de las diapositivas son «marcador + 1»**, recalculadas por programa a partir del propio texto (`herramientas/itpages.py`). En *Al-Jawab al-Sahih* lo comprobé con las imágenes; **en las demás obras supongo la misma regla** (el formato de OpenITI es el mismo), pero no lo he comprobado: puede haber desfases de una página. Los JSON de `datos_agentes/` conservan los números originales de los marcadores, así que allí las páginas salen una menos que en las diapositivas.', '',
 '## Lo que dejé fuera y por qué', '',
 '- **Pasajes duplicados**: cada investigador devolvió también los que repetían lo ya recogido (los registraron en sus `excluded.json`).',
 '- **Texto que no es de Ibn Taymiyya** (por ejemplo, notas del editor y reseñas de la cabecera de OpenITI).',
 '- **Insultos o desprecio personal**: por ejemplo, la frase en que dice que quien confunde atributo y sustancia merece el «tratamiento de los locos»; No aportan al argumento.',
 '- **Obras no revisadas**: *Al-Jawab al-Sahih* es enorme (6 vols.); revisé los pasajes que los investigadores encontraron y los que cité, **no la obra entera**. Lo mismo vale para *Majmu\' al-Fatawa* (35 vols. en el texto de OpenITI). Es posible que haya pasajes que maticen o contradigan lo que muestro.', '',
 '## Límites y avisos', '',
 '1. **Traducciones al español mías**, desde el árabe; los textos árabes antiguos tienen giros difíciles. Las marcas `[…]` y los corchetes en las traducciones son aclaraciones mías.',
 '2. **Los veredictos «¿hombre de paja?» son míos**: comparan lo que Ibn Taymiyya dice que creen los cristianos con textos cristianos de referencia (credos, Padres, Calcedonia, Nicea II, Tomás, Biblia). Hay cristianos que dicen cosas muy distintas, y los árabes cristianos medievales que él cita sí hablaban a veces en términos de «atributos». Por eso el veredicto suele ser «parcial» y no «paja».',
 '3. **«Lectura (mía)»**: donde aparece, es una observación crítica mía (por ejemplo, que su definición de tawatur es relativa al oyente, o que su regla sobre la razón se protege sola); **no es una cita de Ibn Taymiyya** y es discutible.',
 '4. **Carta de Pablo de Antioquía**: lo que muestro es lo que Ibn Taymiyya dice citar; **no cotejé el árabe de la carta** (ed. P. Khoury, 1964), que sería lo necesario para decir que la cita «con sus palabras exactas» es literal en todas las secciones (por eso «no verificable» en IT13). Del texto de al-Hasan ibn Ayyub sé solo lo que dice Ibn Taymiyya en *Al-Jawab* (con la nota del editor).',
 '5. **Ediciones**: *Al-Jawab al-Sahih*, Dar al-\'Asima, 2.ª ed., 1419/1999; *Majmu\' al-Fatawa*, ed. Ibn Qasim, Majma\' al-Malik Fahd, 1416/1995; *Dar\' ta\'arud*, Dar al-Kutub al-\'Ilmiyya, 1417/1997; *Al-Tadmuriyya*, ed. \'Ubaykan, 6.ª ed., 2000; *Al-Isfahaniyya*, Dar al-Minhaj, 1430 H; *Al-Wasitiyya*, Maktabat al-Ma\'arif con comentario de Ibn Mani\' (la cita es del credo, no del comentario); *Al-Radd \'ala al-mantiqiyyin*, Dar al-Ma\'rifa (la cabecera de OpenITI no da más datos). Esas son las ediciones que declara la cabecera de OpenITI; solo comprobé la de *Al-Jawab* con escaneos.',
 '6. **Tawhid en tres clases.** En los textos que se revisaron, la fórmula de tres «tawhid» con exactamente los nombres *rububiyya*, *uluhiyya* y *asma\' wa-sifat* **no apareció como tal**; sí aparece la insistencia en la *uluhiyya* y la afirmación de los atributos. No afirmo que no esté en ningún lugar de su obra, solo que no la encontré en lo revisado.',
 '7. **Valoraciones de especialistas** (Zwirahn 2018, Rayan y Baraijia 2026, Husseini 2011, Bogataj 2019): las leyó un investigador y las cito como secundarias; no las leí enteras.',
 '8. **El Corán y la historia no se juzgan aquí**: no digo si la Trinidad es verdadera ni si el Islam lo es. Lo que se comprueba es la coherencia de sus argumentos y su fidelidad a las fuentes cristianas.', '',
 '## Licencias y derechos', '',
 'Textos árabes en extractos breves, con su fuente, tomados de OpenITI (https://github.com/OpenITI, copia de Shamela); textos cristianos de dominio público (Schaff, NPNF, Fordham, CCEL, New Advent, Biblia del Rey Jacobo vía bible-api). Las traducciones al español y los veredictos son míos. No se incluyen imágenes de terceros salvo la tipografía de los títulos de las obras (texto, no escaneos).', '',
 'Herramientas en `herramientas/`: `gen.py` (genera los encargos), `itlib.py`, `itsrc.py`, `itpages.py` y `itbase.py` (lectura de OpenITI, corte del árabe y páginas), `itdata1.py` y `itdata2.py` (datos de los 12 temas con las traducciones y veredictos), `itfigs.py` (orden y códigos), `itpad.py` y `itstatic.py` (generan las diapositivas), `itrun.py`, `itchk.py` (comprobación de frases), `packit.py` (este empaquetado), `renderhb.js` (convierte en PNG; requiere Playwright y las fuentes Amiri y Noto Naskh Arabic) y `hbcss.py` y `genpad.py` (CSS base). `ibntaymiyya_openiti.tsv` es la lista de las versiones de OpenITI de Ibn Taymiyya y `oimeta.csv`, sus metadatos.']
open(R + '/README.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(files), 'diapositivas')
