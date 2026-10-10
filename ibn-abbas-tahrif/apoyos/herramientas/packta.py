# -*- coding: utf-8 -*-
import os, shutil, re
from PIL import Image
import ycards_data
R = '/home/user/Pruebas/ibn-abbas-tahrif/apoyos'
H = '/home/user/Pruebas/ibn-abbas-tahrif/capturas/historia'
os.makedirs(R + '/herramientas', exist_ok=True)
TA = {c['id']: c for c in ycards_data.TACARDS}
exec(open('hcards_data.py', encoding='utf-8').read(), g := {})
HC = {c['id']: c for c in g['HCARDS']}
SECS = [
 ('0', 'Base: el texto de al-Bujari y lo que dice Ibn Hajar', ['H09']),
 ('A', 'A. Quién atribuye a Ibn Abbas la lectura «el tahrif es de significado» (orden cronológico)', ['H02a', 'H15', 'TA01', 'TA14', 'TA02', 'H20a', 'H20b', 'H21', 'TA15', 'TA03', 'TA16', 'TA05', 'TA04', 'TA09']),
 ('B', 'B. Quién la atribuye a al-Bujari o la comenta (y lo que dicen de ella)', ['TA06', 'TA17', 'H19a', 'H19b', 'H17', 'H16', 'TA07', 'TA08', 'TA18']),
 ('C', 'C. Lo que hay que decir en contra: Ibn Abbas también aparece en la otra dirección', ['TA10', 'TA11', 'TA12', 'TA19', 'TA13', 'H02b', 'H18']),
]
files = ['TA00_es.png', 'TA00b_es.png', 'TA00c_es.png']
order = []
for _, _, ids in SECS: order += ids
for i in order:
    for l in ('ar', 'es'): files.append(f'{i}_{l}.png')
files += [f'S{i}_es.png' for i in (1, 2, 3)]
def src(f): return f'tacards/{f}' if f.startswith(('TA', 'S')) else f'{H}/{f}'
for f in files:
    assert os.path.exists(src(f)), f
    shutil.copy(src(f), R + '/' + f)
for t in ['capt.js', 'genv.py', 'rendera.js', 'scanhl.py', 'pdfhl.py', 'textcap.js', 'yspecs_build.py', 'yspecs_defs.py', 'yspecs.json', 'ycards_data.py', 'hcards_data.py', 'ta00.py', 'packta.py', 'escaneo.py', 'urls_escaneo.txt']:
    shutil.copy(t, R + '/herramientas')
os.makedirs(R + '/herramientas/briefs_agentes', exist_ok=True)
HPD = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hp'
for i in range(1, 9): shutil.copy(f'{HPD}/Y{i}.txt', R + f'/herramientas/briefs_agentes/Y{i}.txt')
def pdf(name, w, q):
    ims = []
    for f in files:
        im = Image.open(src(f)).convert('RGB')
        if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        ims.append(im)
    ims[0].save(R + '/' + name, save_all=True, append_images=ims[1:], resolution=120, quality=q)
    return os.path.getsize(R + '/' + name) / 1e6
print('pdf MB', pdf('apoyos_taliq_ibn_abbas.pdf', 1200, 72), 'pages', len(files))
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
out = ["# Ibn Abbas y el tahrif: ¿quién más atribuye a Ibn Abbas que el «cambio» es de significado? — repaso completo", "",
 "El taʿliq de al-Bujari (Sahih, Kitab al-Tawhid): «Y dijo Ibn Abbas: *yuharrifun*: *yuzilun* [quitan]; y nadie quita el texto de un libro de Dios, pero lo tergiversan: lo interpretan en un sentido que no es el suyo». Ya teníamos a Ibn ʿAtiyya e Ibn Jaldun. Aquí se busca, con las páginas originales delante, **quién más lo atribuye a Ibn Abbas**, qué dice cada uno de verdad y qué hay en contra.", "",
 "**Respuesta corta.** Sí, hay más: **Abu Hayyan (745 H, en 2:75 y en 5:13), Ibn Kathir (774), al-Thaʿalibi (875), al-Alusi (1270), Siddiq Hasan Khan (1307), al-Qasimi (1332) e Ibn ʿAshur (1393)**, además de Ibn Hajar (852), que lo recoge como atribución que no ve conectada, y de Sirry (Oxford, 2014). Con Ibn ʿAtiyya e Ibn Jaldun, **diez autores de 541 a 1393 H**. **Pero** (1) no son testimonios independientes: al-Thaʿalibi copia a Ibn ʿAtiyya, al-Qasimi a Ibn Kathir, Siddiq a Ibn Jaldun e Ibn al-Qayyim; (2) casi ninguno la adopta como única postura (Ibn Jaldun es quien más se inclina por ella; Abu Hayyan, al-Alusi, Ibn ʿAshur e Ibn Kathir dan también el cambio de texto como cierto); (3) no hay cadena conectada (Ibn Hajar no la ve «por un camino firme»; en al-Tabari no hay ninguna coincidencia y mis agentes tampoco la hallan en Ibn Abi Hatim); y (4) de Ibn Abbas se transmiten también relatos de «añadieron», «quitaron» o «escribieron un libro» (al-Tabari, Ibn Kathir, al-Alusi, al-Razi). Hay además quien la atribuye a al-Bujari y no a Ibn Abbas (Ibn al-Qayyim, Ibn al-Mulaqqin, al-Rayihi).", "",
 f"Todo junto en un PDF: [`apoyos_taliq_ibn_abbas.pdf`](apoyos_taliq_ibn_abbas.pdf). Páginas: TA00, TA00b y TA00c (resumen, matices y límites), las tarjetas (`xx_ar.png` = original con subrayado, `xx_es.png` = traducción, «qué demuestra» y «ojo») y tres silogismos (S1–S3) con sus puntos débiles. Las tarjetas `Hxx` ya estaban comprobadas en el paquete anterior (`../capturas/historia/`) y se repiten aquí para que el PDF esté completo.", "",
 "Colores: amarillo = pasaje citado · naranja = frase clave · azul = matiz, concesión o lo que juega en contra.", "",
 "**Cómo se hizo.** Un orquestador y 8 agentes de búsqueda (modelo pequeño) buscaron fuentes en paralelo (sus encargos están en `herramientas/briefs_agentes/`). Además hice **mi propio escaneo de 55 comentarios coránicos × 6 versículos** (2:75, 2:79, 3:78, 4:46, 5:13, 5:41; 324 páginas; `herramientas/escaneo.py` y `urls_escaneo.txt`). **Todo lo que está en una tarjeta TA lo leí yo en la página original** (texto en línea de quran-tafsir.net, quran.ksu.edu.sa o Wikisource, que no traen paginación impresa; lo indico en cada tarjeta). Lo que solo dicen los agentes (p. ej. al-Qastallani en OCR, Rashid Rida en al-Manar) **no tiene tarjeta y se marca como tal** en TA00b/TA00c. Los resultados negativos (Ibn Hazm, Ibn Taymiyya, al-Tabari, Ibn Abi Hatim…) están en TA00c.", "",
 "**Avisos.** (1) No se ha hallado cadena conectada de la frase «nadie quita…» a Ibn Abbas; puede ser de al-Bujari. (2) El texto en línea de algunos comentarios puede tener erratas respecto a la edición impresa (p. ej. Ibn Kathir en esta edición imprime «يزيدون» en lugar de «يزيلون»). (3) No he evaluado a los transmisores de las cadenas citadas.", ""]
for k, name, ids in SECS:
    out += ["", f"## {name}", "", "| Código | Autor | Título | Fuente | Tarjetas |", "|---|---|---|---|---|"]
    for i in ids:
        if i in TA:
            c = TA[i]; who = c['tag'].split(' · ', 1)[1] if ' · ' in c['tag'] else c['tag']
            out.append(f"| {i} | {cell(who)} | {cell(c['title'])} | {cell(c['ref'])} · {link(c['url'])} | [original]({i}_ar.png) · [español]({i}_es.png) |")
        else:
            c = HC[i]
            out.append(f"| {i} (ya verificada) | {cell(c['who'])} | {cell(c['title'])} | {cell(c['ref'])} · {link(c['url'])} | [original]({i}_ar.png) · [español]({i}_es.png) |")
out += ["", "## Resúmenes y silogismos", "", "| Código | Tema |", "|---|---|",
 "| [TA00](TA00_es.png) | Quién más lo atribuye a Ibn Abbas (tabla cronológica) |", "| [TA00b](TA00b_es.png) | Quién lo atribuye a al-Bujari, y qué hay en contra |", "| [TA00c](TA00c_es.png) | Resultados negativos y lo que no se puede afirmar |",
 "| [S1](S1_es.png) | La lectura «tahrif sobre todo de significado» no es un invento moderno |", "| [S2](S2_es.png) | No hay consenso musulmán de que el texto de la Biblia esté simplemente «corrompido» |", "| [S3](S3_es.png) | Si Ibn Abbas es testigo, hay que citarlo entero |", "",
 "Herramientas de captura, generación de tarjetas y escaneo en `herramientas/`."]
open(R + '/README.md', 'w').write('\n'.join(out) + '\n')
print(len(files), 'files')
