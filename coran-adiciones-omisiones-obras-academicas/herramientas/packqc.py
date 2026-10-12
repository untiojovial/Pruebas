# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
import os, shutil, re, glob, json
from PIL import Image
import qccards_data
R = '/home/user/Pruebas/coran-adiciones-omisiones-obras-academicas'
SP = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/'
os.makedirs(R + '/herramientas/briefs_agentes', exist_ok=True)
os.makedirs(R + '/herramientas/datos_agentes', exist_ok=True)
os.makedirs(R + '/herramientas/lectura_directa', exist_ok=True)
QC = {c['id']: c for c in qccards_data.QCCARDS}
SECS = [
 ('A', 'A. Obras recientes sobre la formación del texto y los manuscritos (inglés, alemán, francés)', ['QC01', 'QC02', 'QC03', 'QC04', 'QC05', 'QC06', 'QC07', 'QC08', 'QC09', 'QC10']),
 ('B', 'B. Clásicos de la crítica textual (1844–1938) y obras en neerlandés', ['QC11', 'QC12', 'QC13', 'QC14', 'QC15', 'QC16', 'QC17', 'QC18']),
 ('C', 'C. Obras en árabe: clásicos (al-Suyūṭī, al-Zarkashī, Abū ʿUbayd, Ibn Abī Dāwūd) y modernos (Ṣubḥī al-Ṣāliḥ, al-Zurqānī)', ['QC19', 'QC20', 'QC21', 'QC22', 'QC23', 'QC24', 'QC25']),
]
order = []
for _, _, ids in SECS: order += ids
assert sorted(order) == sorted(QC), set(QC) ^ set(order)
files = ['QC00_es.png', 'QC00b_es.png', 'QC00c_es.png', 'QC00d_es.png']
for i in order:
    for l in ('or', 'es', 'pt'): files.append(f'{i}_{l}.png')
for f in files:
    assert os.path.exists('qccards/' + f), f
    shutil.copy('qccards/' + f, R + '/' + f)
for t in ['capt.js', 'fetchroute.js', 'genv.py', 'genq.py', 'renderqc.js', 'pdfhl2.py', 'scanhl.py', 'qccap.py', 'qcpdfs.py', 'qcfix.py', 'qcspecs_build.py', 'qcshamela.json', 'qcweb.json',
          'qcc_a.py', 'qcc_b.py', 'qcc_c.py', 'qcc_d.py', 'qccards_data.py', 'qc00.py', 'packqc.py']:
    shutil.copy(t, R + '/herramientas')
for i in range(1, 9):
    shutil.copy(f'{SP}qc/Q{i}.txt', R + f'/herramientas/briefs_agentes/Q{i}.txt')
    for n in ('works.json', 'passages.json'):
        shutil.copy(f'{SP}qc/Q{i}/{n}', R + f'/herramientas/datos_agentes/Q{i}_{n}')
for t in ['qcverify.py', 'qcverify2.py']: shutil.copy(f'{SP}qc/V/{t}', R + '/herramientas/lectura_directa/' + t)
def pdf(name, w, q):
    ims = []
    for f in files:
        im = Image.open('qccards/' + f).convert('RGB')
        if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        ims.append(im)
    ims[0].save(R + '/' + name, save_all=True, append_images=ims[1:], resolution=120, quality=q)
    return os.path.getsize(R + '/' + name) / 1e6
mb = pdf('coran_adiciones_omisiones_obras_academicas.pdf', 1200, 72)
print('pdf MB', mb, 'pages', len(files))
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
out = ["# ¿Adiciones, interpolaciones o supresiones en el Corán? Lo que dicen obras académicas (inglés, alemán, neerlandés, francés y árabe)", "",
 "Documentación, **con la captura del texto original subrayado, su traducción al español y la portada de cada obra**, sobre lo que dicen obras académicas acerca de adiciones, interpolaciones o supresiones en el Corán (Sinai, Shoemaker, Neuwirth, Corpus Coranicum, Nöldeke–Schwally, Jeffery, Déroche, Dye, Bouali, van Koningsveld y fuentes árabes clásicas y modernas, entre otras). Incluye lo que cada obra matiza, informa de otros o rechaza, porque una cita sin su contexto sería engañosa. Es documentación de lo que dicen las obras; no es una opinión ni una recomendación.", "",
 "**Respuesta corta.** Sí hay obras académicas que proponen **adiciones o interpolaciones**, pero casi todas dentro de la **formación del texto en vida de Muhammad** (ampliaciones «medinenses» de suras mequíes: Nöldeke, Neuwirth, Sinai, Corpus Coranicum) y con lenguaje condicional («no descarto», «podría», «dürfte»). Las tesis de **fijación o redacción posterior** (Shoemaker, hacia el 700; Wansbrough, hacia el 800, que cita van Koningsveld para rechazarla) son **minoritarias y discutidas**. Sobre **supresiones**, ninguna obra leída muestra suras o versículos perdidos del texto actual: hay **informes** (Ubayy, Ibn Masʿūd, ʿUmar, ʿĀʾisha) que las propias fuentes árabes registran y clasifican como «abrogación de la recitación» o rechazan (al-Nawawī, Ibn Ḥazm, al-Zurqānī, Ṣubḥī al-Ṣāliḥ). El palimpsesto de Ṣanʿāʾ I (Déroche) omite 9:85 y tiene variantes, pero **los manuscritos tempranos estudiados siguen el texto ʿuthmánico** (Bergsträsser–Pretzl; van Putten). Ver QC00b y QC00c.", "",
 f"Todo junto en un PDF ({mb:.0f} MB): [`coran_adiciones_omisiones_obras_academicas.pdf`](coran_adiciones_omisiones_obras_academicas.pdf). Páginas: QC00, QC00b, QC00c y QC00d (resumen, obras clásicas, lecturas y qué se puede afirmar, fuentes leídas y no leídas) y, por cada una de las 25 obras, **tres diapositivas**: `QCxx_or.png` (texto original, con subrayado sobre la página digital o una transcripción cuando no hay copia digital), `QCxx_es.png` (traducción al español, «qué dice el autor» y «ojo») y `QCxx_pt.png` (portada o página de título con autor y título).", "",
 "Colores: amarillo = pasaje citado · naranja = frase clave · azul = matiz, concesión o lo que juega en contra. En la tabla de las páginas de resumen: **A** adición o interpolación · **B** redacción o fijación posterior · **C** supresión, pérdida u omisión · **D** códices alternativos y variantes · **E** contraevidencia o rechazo.", "",
 "**Cómo se hizo.** Un orquestador y 8 agentes de búsqueda (modelo pequeño) buscaron obras y pasajes en toda la web (sus encargos están en `herramientas/briefs_agentes/` y lo que devolvieron, en `herramientas/datos_agentes/`). Luego **abrí yo cada obra en una copia digital** (PDF abierto, escaneos de archive.org, Project Gutenberg, texto web de Shamela, API del Corpus Coranicum) y comprobé cada pasaje en la página; los subrayados se dibujaron sobre la imagen de la página (con las coordenadas de las palabras de la capa de texto del PDF o, en escaneos, con reconocimiento óptico de caracteres; en Shamela, sobre la página web). Cuando una pista del agente no cuadraba con la página la corregí o la descarté (p. ej., el versículo perdido de Zayd está en la p. 89 de Ibn Abī Dāwūd y no en la 88; en Hirschfeld (seg. 3) y Muir (seg. 5) la capa de texto del PDF tiene el orden de palabras alterado y el subrayado se hizo con OCR, aproximado en los bordes). Lo que solo dicen los agentes y yo no pude abrir **no tiene tarjeta**: está listado como pista sin verificar en QC00d.", "",
 "**Avisos.** (1) Las traducciones son mías y literales; las aclaraciones van entre corchetes; las citas de Shamela y del Corpus Coranicum son de páginas web, no de ediciones impresas (la página que da Shamela no la comprobé contra la edición impresa). (2) **Obras sin copia legal accesible** (Sinai 2017, Wansbrough, Crone, Cook, Reynolds, Powers, Donner, Motzki, Sadeghi y otros): los agentes solo hallaron fichas o copias subidas por terceros, que no usé; no tienen tarjeta. (3) **van Koningsveld 2009 (QC18)** es una copia en un servidor de terceros (la del repositorio de Leiden estaba bloqueada), y su licencia no se verificó. (4) **Neuwirth 2007 (QC03)**: solo leí la vista previa gratuita del editor; el apartado «Spätere Zusätze» no está en ella. (5) **«De Koran» (QC17)** es una introducción divulgativa neerlandesa de hacia 1916 de autor no identificado en el texto; la incluyo por ser de dominio público, no por ser académica en sentido estricto. (6) **Derechos**: Sinai, Shoemaker y van Putten son de acceso abierto; Déroche (OAPEN), Dye, Bouali, Chahdi (Archimède), Bergsträsser–Pretzl (1938), Ṣubḥī al-Ṣāliḥ y al-Zurqānī: licencia no confirmada o «todos los derechos reservados», por lo que muestro solo fragmentos breves con cita. (7) **Cubiertas**: las de al-Suyūṭī, al-Zarkashī, Ṣubḥī y al-Zurqānī son miniaturas de baja resolución; la de «De Koran» es una cubierta generada por Project Gutenberg (sin autores); el Corpus Coranicum no tiene portada; la de Abū ʿUbayd es la ficha de Shamela; la de Ibn Abī Dāwūd, la portada de la edición de Jeffery; la de Sinai, la página de título del PDF abierto. (8) Resultados negativos y dudas están en QC00d y en el «Ojo» de cada obra.", ""]
for k, name, ids in SECS:
    out += ["", f"## {name}", "", "| Código | Autor / obra | Título | Fuente | Diapositivas |", "|---|---|---|---|---|"]
    for i in ids:
        c = QC[i]; who = c['tag'].split(' · ', 1)[1] if ' · ' in c['tag'] else c['tag']
        out.append(f"| {i} | {cell(who)} | {cell(c['title'])} | {cell(c['ref'])} · {link(c['url'])} | [original]({i}_or.png) · [español]({i}_es.png) · [portada]({i}_pt.png) |")
out += ["", "## Resúmenes", "", "| Código | Tema |", "|---|---|",
 "| [QC00](QC00_es.png) | ¿Dice la erudición que el Corán sufrió adiciones, interpolaciones o supresiones? Obras recientes (tabla) |",
 "| [QC00b](QC00b_es.png) | Clásicos, obras en neerlandés y fuentes árabes (tabla) |",
 "| [QC00c](QC00c_es.png) | Cuatro clases de afirmaciones; qué se puede y no se puede afirmar |",
 "| [QC00d](QC00d_es.png) | Obras leídas por mí, obras no leídas, resultados negativos y avisos |", "",
 "Herramientas de captura y generación de diapositivas en `herramientas/` (`capt.js` captura web con resaltado; `pdfhl2.py` y `scanhl.py` resaltan sobre PDF y escaneos; `genq.py` genera las diapositivas)."]
open(R + '/README.md', 'w').write('\n'.join(out) + '\n')
print(len(files), 'files')
