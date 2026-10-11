# -*- coding: utf-8 -*-
import os, shutil, re, glob
from PIL import Image
import nqcards_data
R = '/home/user/Pruebas/naqisat-aql-mujer'
os.makedirs(R + '/herramientas/briefs_agentes', exist_ok=True)
NQ = {c['id']: c for c in nqcards_data.NQCARDS}
SECS = [
 ('A', 'A. El hadiz «nāqiṣāt ʿaql wa-dīn» y sus variantes (Bujari, Muslim, Abu Dawud, Tirmidhi, Ahmad, Ibn Hibban, Ibn Abi Shayba)', ['NQ01', 'NQ02', 'NQ03', 'NQ04', 'NQ05', 'NQ06', 'NQ07', 'NQ08', 'NQ09']),
 ('B', 'B. Textos parecidos o relacionados: «ʿaql» = diya, «kamala», «lan yuflih qawm», «shaqaʾiq», Umm Salama y ʿAʾisha', ['NQ10', 'NQ11', 'NQ12', 'NQ13', 'NQ14', 'NQ15', 'NQ16']),
 ('C', 'C. Reportes tempranos sobre el testimonio de la mujer: ʿAli, ʿUmar, Tawus, ʿAtaʾ, Malik, Wahb ibn Munabbih, y el sermón 80 del Nahj al-balagha (fuente débil)', ['NQ17', 'NQ18', 'NQ19', 'NQ20', 'NQ21', 'NQ22', 'NQ23', 'NQ53']),
 ('D', 'D. Exégesis de Corán 2:282 y 4:34: al-Tabari, al-Qurtubi, al-Maturidi, al-Baydawi, al-Razi, Ibn Kathir, al-Alusi, al-Shawkani, Siddiq Hasan Jan', ['NQ24', 'NQ25', 'NQ26', 'NQ27', 'NQ28', 'NQ29', 'NQ30', 'NQ31', 'NQ32', 'NQ33', 'NQ34', 'NQ35']),
 ('E', 'E. Comentaristas del hadiz: al-Jattabi, Ibn Hayar, al-Nawawi (con al-Mazari), al-ʿAyni', ['NQ36', 'NQ37', 'NQ38', 'NQ39', 'NQ40', 'NQ41']),
 ('F', 'F. Juristas y pensadores: Ibn Qudama, Ibn Hazm, al-Qurtubi, Ibn al-Qayyim e Ibn Taymiyya', ['NQ42', 'NQ43', 'NQ44', 'NQ45', 'NQ46', 'NQ47', 'NQ48', 'NQ49']),
 ('G', 'G. Siglos XIX–XX: ʿAbduh y Rida (Manar), Tahtawi y Qasim Amin (páginas escaneadas)', ['NQ50', 'NQ51', 'NQ52']),
]
files = ['NQ00_es.png', 'NQ00b_es.png', 'NQ00c_es.png', 'NQ00d_es.png']
order = []
for _, _, ids in SECS: order += ids
assert sorted(order) == sorted(NQ), set(NQ) ^ set(order)
for i in order:
    for l in ('ar', 'es'): files.append(f'{i}_{l}.png')
for f in files:
    assert os.path.exists('nqcards/' + f), f
    shutil.copy('nqcards/' + f, R + '/' + f)
for t in ['capt.js', 'fetchroute.js', 'genv.py', 'rendernq.js', 'nqspecs_build.py', 'nqspecs_defs.py', 'nqspecs.json', 'imgcap.py', 'imgwords.py',
          'nqcards_a.py', 'nqcards_b.py', 'nqcards_d.py', 'nqcards_f.py', 'nqcards_h.py', 'nqcards_data.py', 'nq00.py', 'packnq.py']:
    shutil.copy(t, R + '/herramientas')
HPD = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hp'
for i in range(1, 9): shutil.copy(f'{HPD}/X{i}.txt', R + f'/herramientas/briefs_agentes/X{i}.txt')
os.makedirs(R + '/herramientas/lectura_directa', exist_ok=True)
for t in ['toc.py', 'scan.sh', 'hits.py', 'mkpass2.py']: shutil.copy(f'{HPD}/R2/tools/{t}', R + '/herramientas/lectura_directa/' + t)
def pdf(name, w, q):
    ims = []
    for f in files:
        im = Image.open('nqcards/' + f).convert('RGB')
        if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        ims.append(im)
    ims[0].save(R + '/' + name, save_all=True, append_images=ims[1:], resolution=120, quality=q)
    return os.path.getsize(R + '/' + name) / 1e6
print('pdf MB', pdf('naqisat_aql_mujer.pdf', 1200, 72), 'pages', len(files))
def cell(s): return s.replace('|', '\\|')
def link(u):
    out = []
    for p in re.split(r' · ', u):
        m = re.match(r'(https?://\S+)(.*)', p)
        if m:
            host = re.sub(r'^https?://(www[.])?', '', m.group(1)).split('/')[0]
            out.append(f"[{host}]({m.group(1)}){m.group(2)}")
        else: out.append(p)
    return ' · '.join(out)
out = ["# La mujer «deficiente en razón y religión»: el hadiz, sus variantes y lo que dijeron los sabios tempranos, medievales y del siglo XIX", "",
 "Documentación, **con la captura del original en árabe subrayado y su traducción**, sobre el hadiz de las «nāqiṣāt ʿaql wa-dīn» (la mujer «deficiente en razón y religión»), sus variantes, los textos parecidos y lo que dijeron sobre él juristas, comentaristas y exégetas, de los Compañeros y sucesores hasta el siglo XIX. Se incluye lo que los mismos textos matizan, discuten o contradicen, porque una cita sin sus condiciones sería engañosa. Es documentación de lo que dicen las fuentes; no es una opinión ni una recomendación.", "",
 "**Respuesta corta.** El hadiz existe (Bujari 304, 1462, 2658; Muslim 79; Abu Dawud 4679; Tirmidhi 2613; Ahmad 8862…), pero **no dice «la mitad de inteligencia»**: dice que las mujeres son «deficientes en razón y religión» y **el propio Profeta lo explica**: la «deficiencia de razón» es que el testimonio de dos mujeres equivale al de un hombre (Corán 2:282); la «deficiencia de religión» es que no rezan ni ayunan cuando menstrúan. Busqué «نصف عقل» («mitad de razón») en todos los textos leídos: **resultado negativo**. La fórmula más parecida es de derecho penal («el ʿaql de la mujer es la mitad del ʿaql del hombre», Bayhaqi 16407, atribuido a ʿAli, cadena cortada), y ahí **ʿaql significa diya** (precio de sangre). **Pero no basta con eso**: el texto sí dice «deficientes en razón», y exégetas y juristas de primer orden —al-Razi, al-Baydawi, Ibn Kathir, Ibn Qudama, al-Alusi— lo generalizaron a una superioridad intelectual del hombre; otros —al-Mazari, al-Nawawi, Ibn Taymiyya, Ibn al-Qayyim— lo limitan a la **precisión al retener (dabt) en el testimonio** (Ibn Taymiyya: la mitad es por la razón, «no por la religión»; la rectitud de la mujer es igual a la del hombre; donde no se teme el olvido no hay «mitad»); Ibn Hayar lo ve «de la creación original» pero «sin censura»; Ibn Hazm niega que sea por psicología y sostiene que hubo profetisas; y en el siglo XIX Tahtawi, ʿAbduh y Qasim Amin lo atribuyen a la ignorancia y la falta de educación (Siddiq Hasan Jan, en cambio, lo refuerza). Ver NQ00b y NQ00c.", "",
 "Todo junto en un PDF: [`naqisat_aql_mujer.pdf`](naqisat_aql_mujer.pdf). Páginas: NQ00, NQ00b, NQ00c y NQ00d (resumen, sabios por época, lecturas y qué se puede afirmar, fuentes leídas y no leídas) y las tarjetas NQ01–NQ53 (`NQxx_ar.png` = original con subrayado, `NQxx_es.png` = traducción, «qué demuestra» y «ojo»).", "",
 "Colores: amarillo = pasaje citado · naranja = frase clave · azul = matiz, concesión o lo que juega en contra.", "",
 "**Cómo se hizo.** Un orquestador y 8 agentes de búsqueda (modelo pequeño) buscaron fuentes en paralelo (sus encargos están en `herramientas/briefs_agentes/`; devolvieron unas 275 pistas). Luego **verifiqué yo cada pista**: descargué las páginas originales (hadithunlocked.com, Shamela, comentarios coránicos en línea) y las busqué con palabras clave; **todo lo que está en una tarjeta lo leí yo en la página original**, y pasó una comprobación automática de que cada resaltado cae en el texto de la página. Dos fuentes del siglo XIX (Tahtawi, Qasim Amin) solo estaban en escaneos de archive.org: descargué las imágenes de página, comprobé que son legibles y dibujé el resaltado con las coordenadas del OCR (`herramientas/imgcap.py`); son las tarjetas NQ51–NQ52. Lo que solo dicen los agentes **no tiene tarjeta**: está listado como pista sin verificar en NQ00d. Algunas citas de página de los agentes eran incorrectas (p. ej., el Manar) y se corrigieron.", "",
 "**Avisos.** (1) Las calificaciones de cadenas («débil», «ṣaḥīḥ», «cortada») son las que imprimen los sitios, no las mías; hadithunlocked muestra a veces notas de crítica bajo otro número de edición. (2) Los textos de Shamela, hadithunlocked y los comentarios en línea son transcripciones web; la página impresa va en el título de las páginas de Shamela. (3) Las traducciones son mías y literales; las aclaraciones van entre corchetes. (4) Las fechas de muerte de los autores son de memoria (dato general) salvo donde la página las muestra. (5) **NQ53** (Nahj al-balagha, sermón 80) es solo una transcripción en un foro, no una edición: fuente débil, marcada como secundaria. (6) Segunda mano: lo que atribuyo a Ibn Abi Shayba, la Mudawwana, Abu ʿUbayd, Ibn Taymiyya y a los salaf en NQ20–NQ22, NQ25 y NQ49 viene a través de Ibn al-Qayyim o al-Qurtubi; no leí los originales. (7) Pistas sin verificar (Qadi ʿIyad, Ibn Battal, al-Kirmani, ʿAli al-Qari, al-Mubarakfuri, al-Shafiʿi, al-Sarakhsi, al-Mawardi, Ibn Rushd–Averroes, Ibn ʿAbd Rabbih, etc.): listadas en NQ00d.", ""]
for k, name, ids in SECS:
    out += ["", f"## {name}", "", "| Código | Autor / fuente | Título | Fuente | Tarjetas |", "|---|---|---|---|---|"]
    for i in ids:
        c = NQ[i]; who = c['tag'].split(' · ', 1)[1] if ' · ' in c['tag'] else c['tag']
        out.append(f"| {i} | {cell(who)} | {cell(c['title'])} | {cell(c['ref'])} · {link(c['url'])} | [original]({i}_ar.png) · [español]({i}_es.png) |")
out += ["", "## Resúmenes", "", "| Código | Tema |", "|---|---|",
 "| [NQ00](NQ00_es.png) | ¿Dice el islam que la mujer tiene «la mitad de inteligencia»? El hadiz y sus variantes (tabla) |", "| [NQ00b](NQ00b_es.png) | Lo que dijeron los sabios, por época (tabla) |", "| [NQ00c](NQ00c_es.png) | Cuatro lecturas del hadiz; qué se puede y no se puede afirmar |", "| [NQ00d](NQ00d_es.png) | Fuentes leídas por mí, pistas sin verificar, resultados negativos y correcciones |", "",
 "Herramientas de captura y generación de tarjetas en `herramientas/`."]
open(R + '/README.md', 'w').write('\n'.join(out) + '\n')
print(len(files), 'files')
