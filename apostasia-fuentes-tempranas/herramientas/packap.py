# -*- coding: utf-8 -*-
import os, shutil, re
from PIL import Image
import acards_data
R = '/home/user/Pruebas/apostasia-fuentes-tempranas'
os.makedirs(R + '/herramientas/briefs_agentes', exist_ok=True)
AP = {c['id']: c for c in acards_data.APCARDS}
SECS = [
 ('A', 'A. Hadices: «quien cambie su religión, matadlo» y «no es lícita la sangre de un musulmán salvo por una de tres»', ['AP01', 'AP02', 'AP05', 'AP03', 'AP04', 'AP06']),
 ('B', 'B. Compañeros, tabiʿun y casos tempranos (con las cadenas que los editores califican de débiles o cortadas)', ['AP07', 'AP08', 'AP09', 'AP10', 'AP23', 'AP11']),
 ('C', 'C. Juristas: Malik, al-Shafiʿi, la escuela hanafí, al-Qurtubi e Ibn Taymiyya', ['AP12', 'AP13', 'AP14', 'AP15', 'AP16', 'AP17', 'AP18', 'AP19']),
 ('D', 'D. Corán y exégesis: lo que los comentaristas dicen sobre el arrepentimiento del apóstata', ['AP20', 'AP21']),
 ('E', 'E. Estudio académico (fuente secundaria)', ['AP22']),
]
files = ['AP00_es.png', 'AP00b_es.png', 'AP00c_es.png']
order = []
for _, _, ids in SECS: order += ids
for i in order:
    for l in ('ar', 'es'): files.append(f'{i}_{l}.png')
for f in files:
    assert os.path.exists('apcards/' + f), f
    shutil.copy('apcards/' + f, R + '/' + f)
for t in ['capt.js', 'fetchroute.js', 'genv.py', 'renderap.js', 'aspecs_build.py', 'aspecs_defs.py', 'aspecs.json', 'apdfs.py', 'pdfhl.py', 'acards_data.py', 'ap00.py', 'packap.py']:
    shutil.copy(t, R + '/herramientas')
HPD = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hp'
for i in range(1, 9): shutil.copy(f'{HPD}/Z{i}.txt', R + f'/herramientas/briefs_agentes/Z{i}.txt')
def pdf(name, w, q):
    ims = []
    for f in files:
        im = Image.open('apcards/' + f).convert('RGB')
        if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        ims.append(im)
    ims[0].save(R + '/' + name, save_all=True, append_images=ims[1:], resolution=120, quality=q)
    return os.path.getsize(R + '/' + name) / 1e6
print('pdf MB', pdf('apostasia_fuentes_tempranas.pdf', 1200, 72), 'pages', len(files))
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
out = ["# La pena para el apóstata en los textos islámicos tempranos: lo que dicen, con sus condiciones y sus contrarios", "",
 "Textos tempranos (hadices, Compañeros y tabiʿun, los fundadores de las escuelas jurídicas y sus herederos) que respaldan la idea de matar al apóstata del islam, **con la captura del original en árabe subrayado y su traducción**, y —porque una cita sin sus condiciones sería engañosa— lo que los mismos textos matizan, discuten o contradicen. Esto es documentación de doctrina clásica; no es una opinión ni una recomendación.", "",
 "**Respuesta corta.** Sí: hay textos tempranos y abundantes. (1) **Hadices**: «Quien cambie su religión, matadlo» (Ibn Abbas, Bujari 6922 y 3017, Tirmidhi 1458) y «no es lícita la sangre de un musulmán salvo por una de tres… el que deja su religión» (Ibn Masʿud en Bujari 6878 y Muslim 1676; ʿUthman en Abu Dawud 4502). (2) **Casos y prácticas de los Compañeros**: Muʿadh y Abu Musa en Yemen (Bujari 6923), ʿAli y Mustawrid, ʿUmar a ʿAmr ibn al-ʿAs, Ibn Masʿud e Ibn al-Nawwaha. (3) **Juristas** desde el siglo II H: Malik (según Ibn ʿAbd al-Barr), al-Shafiʿi (al-Umm), la escuela hanafí (al-Sarakhsi), al-Qurtubi, Ibn Taymiyya. **Pero no es un bloque sin matices**: casi todos piden primero el arrepentimiento (de una hora a tres días, veinte noches, dos meses…); los hanafíes no matan a las mujeres; los hanafíes razonan la pena como «repeler el combate», no como castigo por creer; la pena no alcanza al dhimmi que cambia entre religiones; el Corán, según al-Tabari y al-Qurtubi, no fija una pena mundana (y un ansari que apostató y se arrepintió fue aceptado: AP20); y varios relatos tienen cadena débil o cortada según sus editores. Ver AP00b y AP00c.", "",
 "Todo junto en un PDF: [`apostasia_fuentes_tempranas.pdf`](apostasia_fuentes_tempranas.pdf). Páginas: AP00, AP00b y AP00c (resumen, matices y límites) y las tarjetas AP01–AP23 (`APxx_ar.png` = original con subrayado, `APxx_es.png` = traducción, «qué demuestra» y «ojo»).", "",
 "Colores: amarillo = pasaje citado · naranja = frase clave · azul = matiz, concesión o lo que juega en contra.", "",
 "**Cómo se hizo.** Un orquestador y 8 agentes de búsqueda (modelo pequeño) buscaron fuentes en paralelo (sus encargos están en `herramientas/briefs_agentes/`). **Todo lo que está en una tarjeta lo leí yo en la página original** (Shamela, hadithunlocked.com, Wikisource, quran-tafsir.net, quran.ksu.edu.sa y un PDF académico) y pasó una comprobación automática de que cada resaltado cae en el texto de la página; lo que solo dicen los agentes **no tiene tarjeta** y se señala como tal en AP00c. Varias pistas que me dieron (o que yo apunté de memoria) **resultaron inexactas** y se corrigieron: está listado en AP00c.", "",
 "**Avisos.** (1) Las calificaciones de cadenas («débil», «ṣaḥīḥ», «cortada») son las que imprimen los editores o los sitios web, no las mías. (2) Los textos de Shamela y de los comentarios en línea son transcripciones web, sin comprobar contra la edición impresa; la página impresa va en el título de cada página de Shamela. (3) Las traducciones son mías y literales; las aclaraciones van entre corchetes. (4) No he leído el Muwatta' mismo ni las colecciones de ʿAbd al-Razzaq o Saʿid ibn Mansur, ni la Mudawwana, Ibn Rushd o Ibn al-Mundhir: la lista está en AP00c.", ""]
for k, name, ids in SECS:
    out += ["", f"## {name}", "", "| Código | Autor / fuente | Título | Fuente | Tarjetas |", "|---|---|---|---|---|"]
    for i in ids:
        c = AP[i]; who = c['tag'].split(' · ', 1)[1] if ' · ' in c['tag'] else c['tag']
        out.append(f"| {i} | {cell(who)} | {cell(c['title'])} | {cell(c['ref'])} · {link(c['url'])} | [original]({i}_ar.png) · [español]({i}_es.png) |")
out += ["", "## Resúmenes", "", "| Código | Tema |", "|---|---|",
 "| [AP00](AP00_es.png) | Qué dicen los textos tempranos (tabla de fuentes) |", "| [AP00b](AP00b_es.png) | Matices, disidencia y contrarios |", "| [AP00c](AP00c_es.png) | Lo que se comprobó y no salió, qué no se pudo leer, y qué no se puede afirmar |", "",
 "Herramientas de captura y generación de tarjetas en `herramientas/`."]
open(R + '/README.md', 'w').write('\n'.join(out) + '\n')
print(len(files), 'files')
