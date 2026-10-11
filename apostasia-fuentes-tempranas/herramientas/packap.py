# -*- coding: utf-8 -*-
import os, shutil, re
from PIL import Image
import acards_data
R = '/home/user/Pruebas/apostasia-fuentes-tempranas'
os.makedirs(R + '/herramientas/briefs_agentes', exist_ok=True)
AP = {c['id']: c for c in acards_data.APCARDS}
SECS = [
 ('A', 'A. Hadices: «quien cambie su religión, matadlo» y «no es lícita la sangre de un musulmán salvo por una de tres»', ['AP01', 'AP02', 'AP05', 'AP03', 'AP04', 'AP06']),
 ('B', 'B. Compañeros y casos tempranos (con las cadenas que los editores califican de débiles o cortadas): Muʿadh, ʿUmar y Tustar, ʿAli, Ibn Masʿud', ['AP07', 'AP08', 'AP09', 'AP34', 'AP24', 'AP31', 'AP32', 'AP25', 'AP26', 'AP10', 'AP27', 'AP11', 'AP23']),
 ('B2', 'B2. Sucesores: al-Nakhaʿi, al-Thawri y ʿUmar ibn ʿAbd al-ʿAziz (disidencias y contrarios)', ['AP28', 'AP29', 'AP30']),
 ('C', 'C. Juristas, por orden cronológico: Malik (Muwatta\' y Mudawwana), al-Shafiʿi, Ibn al-Mundhir, Ibn ʿAbd al-Barr, al-Sarakhsi, Ibn Rushd, Ibn Qudama, al-Qurtubi e Ibn Taymiyya', ['AP33', 'AP12', 'AP35', 'AP36', 'AP37', 'AP38', 'AP13', 'AP14', 'AP15', 'AP16', 'AP42', 'AP43', 'AP44', 'AP45', 'AP47', 'AP46', 'AP39', 'AP40', 'AP41', 'AP19', 'AP17', 'AP18']),
 ('D', 'D. Corán y exégesis: lo que los comentaristas dicen sobre el arrepentimiento del apóstata', ['AP20', 'AP21']),
 ('E', 'E. Estudio académico (fuente secundaria)', ['AP22']),
]
files = ['AP00_es.png', 'AP00b_es.png', 'AP00c_es.png', 'AP00d_es.png']
order = []
for _, _, ids in SECS: order += ids
for i in order:
    for l in ('ar', 'es'): files.append(f'{i}_{l}.png')
for f in files:
    assert os.path.exists('apcards/' + f), f
    shutil.copy('apcards/' + f, R + '/' + f)
for t in ['capt.js', 'fetchroute.js', 'genv.py', 'renderap.js', 'aspecs_build.py', 'aspecs_defs.py', 'aspecs.json', 'apdfs.py', 'pdfhl.py', 'acards_data.py', 'acards_ext.py', 'ap00.py', 'packap.py']:
    shutil.copy(t, R + '/herramientas')
HPD = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hp'
for i in range(1, 9): shutil.copy(f'{HPD}/Z{i}.txt', R + f'/herramientas/briefs_agentes/Z{i}.txt')
os.makedirs(R + '/herramientas/lectura_directa', exist_ok=True)
for t in ['toc.py', 'scan.sh', 'hits.py', 'mkpass.py']: shutil.copy(f'{HPD}/R2/tools/{t}', R + '/herramientas/lectura_directa/' + t)
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
 "**Respuesta corta.** Sí: hay textos tempranos y abundantes. (1) **Hadices**: «Quien cambie su religión, matadlo» (Ibn Abbas, Bujari 6922 y 3017, Tirmidhi 1458) y «no es lícita la sangre de un musulmán salvo por una de tres… el que deja su religión» (Ibn Masʿud en Bujari 6878 y Muslim 1676; ʿUthman en Abu Dawud 4502). (2) **Casos y prácticas de los Compañeros**: Muʿadh y Abu Musa en Yemen (Bujari 6923), ʿAli y Mustawrid, ʿUmar a ʿAmr ibn al-ʿAs, Ibn Masʿud e Ibn al-Nawwaha. (3) **Juristas** desde el siglo II H: Malik (según Ibn ʿAbd al-Barr), al-Shafiʿi (al-Umm), la escuela hanafí (al-Sarakhsi), al-Qurtubi, Ibn Taymiyya. **Ampliación con lectura directa:** el Muwatta' mismo (Malik: «quien cambie su religión…» y su explicación), ʿAbd al-Razzaq, Saʿid ibn Mansur, la Mudawwana, Ibn al-Mundhir (consenso: «no conozco desacuerdo»), Ibn Qudama («los sabios convinieron en la obligatoriedad de matar al apóstata… y no se rechazó») e Ibn Rushd (abuelo y nieto). **Pero no es un bloque sin matices**: casi todos piden primero el arrepentimiento (de una hora a tres días, veinte noches, dos meses…); los hanafíes no matan a las mujeres; los hanafíes razonan la pena como «repeler el combate», no como castigo por creer; la pena no alcanza al dhimmi que cambia entre religiones; el Corán, según al-Tabari y al-Qurtubi, no fija una pena mundana (y un ansari que apostató y se arrepintió fue aceptado: AP20); y varios relatos tienen cadena débil o cortada según sus editores. Ver AP00b y AP00c.", "",
 "Todo junto en un PDF: [`apostasia_fuentes_tempranas.pdf`](apostasia_fuentes_tempranas.pdf). Páginas: AP00, AP00b, AP00c y AP00d (resumen, matices, límites y lectura directa) y las tarjetas AP01–AP47 (`APxx_ar.png` = original con subrayado, `APxx_es.png` = traducción, «qué demuestra» y «ojo»).", "",
 "Colores: amarillo = pasaje citado · naranja = frase clave · azul = matiz, concesión o lo que juega en contra.", "",
 "**Cómo se hizo.** Primera parte (AP01–AP23): un orquestador y 8 agentes de búsqueda (modelo pequeño) buscaron fuentes en paralelo (sus encargos están en `herramientas/briefs_agentes/`). **Ampliación (AP24–AP47, AP00d): sin agentes**: descargué yo las páginas originales de ʿAbd al-Razzaq, Saʿid ibn Mansur, el Muwatta', la Mudawwana, Ibn al-Mundhir, Ibn Qudama e Ibn Rushd, las busqué con palabras clave y leí los pasajes (scripts en `herramientas/lectura_directa/`). **Todo lo que está en una tarjeta lo leí yo en la página original** (Shamela, hadithunlocked.com, Wikisource, quran-tafsir.net, quran.ksu.edu.sa y un PDF académico) y pasó una comprobación automática de que cada resaltado cae en el texto de la página; lo que solo dicen los agentes **no tiene tarjeta** y se señala como tal en AP00c. Varias pistas que me dieron (o que yo apunté de memoria) **resultaron inexactas** y se corrigieron: está listado en AP00c.", "",
 "**Avisos.** (1) Las calificaciones de cadenas («débil», «ṣaḥīḥ», «cortada») son las que imprimen los editores o los sitios web, no las mías. (2) Los textos de Shamela y de los comentarios en línea son transcripciones web, sin comprobar contra la edición impresa; la página impresa va en el título de cada página de Shamela. (3) Las traducciones son mías y literales; las aclaraciones van entre corchetes. (4) Sigue sin leer: al-Khiraqi, Ibn al-Qayyim (Ahkam ahl al-dhimma), Ibn al-Mundhir fuera de al-Ijmaʿ, y otros volúmenes de Saʿid ibn Mansur: la lista está en AP00c. (5) Corrección tras la lectura directa: la opinión de al-Nakhaʿi «se le pide arrepentimiento siempre [abadan]» sí existe (AP28, AP41), y Mustawrid está también en ʿAbd al-Razzaq (AP26).", ""]
for k, name, ids in SECS:
    out += ["", f"## {name}", "", "| Código | Autor / fuente | Título | Fuente | Tarjetas |", "|---|---|---|---|---|"]
    for i in ids:
        c = AP[i]; who = c['tag'].split(' · ', 1)[1] if ' · ' in c['tag'] else c['tag']
        out.append(f"| {i} | {cell(who)} | {cell(c['title'])} | {cell(c['ref'])} · {link(c['url'])} | [original]({i}_ar.png) · [español]({i}_es.png) |")
out += ["", "## Resúmenes", "", "| Código | Tema |", "|---|---|",
 "| [AP00](AP00_es.png) | Qué dicen los textos tempranos (tabla de fuentes) |", "| [AP00b](AP00b_es.png) | Matices, disidencia y contrarios |", "| [AP00c](AP00c_es.png) | Correcciones, lo que no salió, lo que sigue sin leer y qué no se puede afirmar |", "| [AP00d](AP00d_es.png) | Lo que ahora he leído yo mismo: fuente, página y qué aporta |", "",
 "Herramientas de captura y generación de tarjetas en `herramientas/`."]
open(R + '/README.md', 'w').write('\n'.join(out) + '\n')
print(len(files), 'files')
