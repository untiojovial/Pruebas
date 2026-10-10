# -*- coding: utf-8 -*-
import os, shutil, re
from PIL import Image
import wcards_data, wcards2_data
R = '/home/user/Pruebas/pablo-damasco'
os.makedirs(R + '/herramientas', exist_ok=True)
cards = wcards_data.WCARDS + wcards2_data.WCARDS2
files = ['wcards/W00_es.png', 'wcards/W00b_es.png']
for c in cards:
    for l in ('ar', 'es'): files.append(f"wcards/{c['id']}_{l}.png")
files += [f'wcards/S{i}_es.png' for i in range(1, 6)]
for f in files:
    assert os.path.exists(f), f
    shutil.copy(f, R)
for t in ['capt.js', 'genv.py', 'renderw.js', 'fetchroute.js', 'scanhl.py', 'pdfhl.py', 'vpdfs.py', 'v2hl.py', 'v2ms.py', 'hjhl.py', 'ahlhl.py', 'textcap.js', 'w00.py',
          'wcards_data.py', 'wcards2_data.py', 'vspecs_build.py', 'vspecs_defs.py', 'vspecs2.json', 'packw2.py']:
    shutil.copy(t, R + '/herramientas')
def pdf(name, w, q):
    ims = []
    for f in files:
        im = Image.open(f).convert('RGB')
        if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        ims.append(im)
    ims[0].save(R + '/' + name, save_all=True, append_images=ims[1:], resolution=120, quality=q)
    return os.path.getsize(R + '/' + name) / 1e6
print('pdf MB', pdf('pablo_damasco_verificacion_ampliada.pdf', 1200, 72), 'pages', len(files))
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
SEC = [('W01', 'A. Lo ya verificado: al-Yaʿqubi, Wahb (Ibn ʿAsakir, Ibn Manzur) e Ibn Kathir'),
       ('W05', 'B. El texto de Ibn Kathir: orden, hadiz, edición crítica y manuscritos'),
       ('W08', 'C. Saʿada, los Qisas, las introducciones y los manuscritos de Berlín'),
       ('W14', 'D. Las iglesias de Damasco y el origen del relato'),
       ('W17', 'E. Otras fuentes musulmanas sobre Pablo'),
       ('W20', 'F. La investigación académica')]
out = ["# Pablo en Damasco: ¿de dónde sale el relato de Ibn Kathir? — verificación ampliada", "",
 "Qué dicen, en el texto original, al-Yaʿqubi, Wahb ibn Munabbih (vía Ibn ʿAsakir e Ibn Manzur) e Ibn Kathir sobre la conversión de Pablo en Damasco; si ese relato «bebe» del hadiz de Abu l-Darda' que lo precede; qué tienen de cierto y de falso los análisis que me pasaron sobre ediciones y manuscritos; qué más dicen las fuentes musulmanas sobre Pablo; y cinco silogismos a favor de la tesis, con sus puntos débiles.", "",
 "**Respuesta corta.** El relato de Pablo **no bebe del hadiz**: en Ibn Kathir (W05) va después de él, sin cadena, y el hadiz no menciona a Pablo; su fuente es Wahb ibn Munabbih (W02). Las frases sobre la «buena fe» de Pablo no están en Ibn ʿAsakir ni en Ibn Manzur; las trae primero Ibn Kathir y la edición crítica de 2010 las confirma (W06). Ibn Kathir fecha «la gran calamidad» 300 años después del Mesías, con Constantino (W09–W10). Pero hay una tradición musulmana abiertamente anti-Pablo (Ibn Hazm, Sayf: W18–W22), y eso hay que decirlo.", "",
 "Todo junto en un PDF: [`pablo_damasco_verificacion_ampliada.pdf`](pablo_damasco_verificacion_ampliada.pdf) (el PDF anterior de W00–W04 sigue en [`pablo_damasco_verificacion.pdf`](pablo_damasco_verificacion.pdf)). Páginas: W00 y W00b (resumen: verdadero / falso / sin verificar), tarjetas W01–W22 (`Wxx_ar.png` = original con subrayado, `Wxx_es.png` = traducción, «qué demuestra» y «ojo») y silogismos S1–S5.", "",
 "Colores: amarillo = pasaje citado · naranja = frase clave · azul = matiz, concesión o lo que juega en contra.", "",
 "**Cómo se hizo.** Un orquestador y 8 agentes de búsqueda (modelo pequeño) buscaron fuentes en paralelo; **yo comprobé las citas que uso leyendo la página o el escaneo**, y donde no pude (p. ej. el artículo completo de Monferrer, el hadiz en Ibn Hibban/Arna'ut, el Majmaʿ de al-Haytami) lo digo. Los hallazgos de los agentes que no tienen captura (OpenITI, OCR) están marcados como tales en W00b.", "",
 "Avisos: W06, W07, W13 y W12 (p. 35) son escaneos con el resaltado dibujado encima; W20–W22 son páginas de PDF de acceso abierto; W16 es un resumen (API de CORE) renderizado en texto.", ""]
cur = None
secs = dict(SEC)
for c in cards:
    if c['id'] in secs:
        out += ["", f"## {secs[c['id']]}", "", "| Código | Autor | Título | Fuente | Tarjetas |", "|---|---|---|---|---|"]
    who = c['tag'].split(' · ', 1)[1] if ' · ' in c['tag'] else c['tag']
    out.append(f"| {c['id']} | {cell(who)} | {cell(c['title'])} | {cell(c['ref'])} · {link(c['url'])} | [original]({c['id']}_ar.png) · [español]({c['id']}_es.png) |")
out += ["", "## Silogismos", "", "| Código | Tema |", "|---|---|",
 "| [S1](S1_es.png) | El dilema del hadiz |", "| [S2](S2_es.png) | Ibn Kathir culpa al concilio de Constantino, no a Pablo |",
 "| [S3](S3_es.png) | Las escenas clásicas de Damasco conservan el relato cristiano |", "| [S4](S4_es.png) | La acusación no está en el Corán ni en el hadiz |",
 "| [S5](S5_es.png) | No hay un islam unánime sobre Pablo |", "",
 "Resumen: [W00](W00_es.png) · [W00b](W00b_es.png). Herramientas de captura en `herramientas/`."]
open(R + '/README.md', 'w').write('\n'.join(out) + '\n')
print(len(files), 'files')
