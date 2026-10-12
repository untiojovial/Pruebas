# -*- coding: utf-8 -*-
# Empaqueta el pack «Hebreos 10:28, Aquino y los Padres de la Iglesia» en el repositorio
import sys, os, shutil, re, json, glob
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb')
from PIL import Image
import hbpadres
HB = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb'
CAPS = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/caps'
R = '/home/user/Pruebas/hebreos-10-28-padres-de-la-iglesia'
os.chdir(HB)
for d in ('', '/herramientas', '/herramientas/briefs_agentes', '/herramientas/datos_agentes', '/herramientas/lectura_directa', '/imagenes'):
    os.makedirs(R + d, exist_ok=True)

P = {f['id']: f for f in hbpadres.PADRES}
order = ['HB00_es', 'HB01_es', 'HB02_es', 'HB02b_es', 'HB03_es', 'HB04_es']
for i in sorted(P): order += [f'{i}_cita', f'{i}_info']
order += ['AQ01_es', 'AQ02_es', 'CV01_es', 'CV02_es', 'HB09_es']
files = [f'{o}.png' for o in order]
for f in files:
    assert os.path.exists('hbcards/' + f), f
    shutil.copy('hbcards/' + f, R + '/' + f)

# imágenes de los Padres
for f in hbpadres.PADRES:
    shutil.copy(f'hbcards/img/{f["slug"]}.jpg', R + f'/imagenes/{f["id"]}_{f["slug"]}.jpg')

# herramientas
for t in ['hbcss.py', 'hbstatic.py', 'hbstatic2.py', 'genpad.py', 'hbpadres.py', 'runpad.py', 'renderhb.js', 'hbverify.py', 'hbverify_orig.py', 'packhb.py', 'showp.py']:
    shutil.copy(t, R + '/herramientas/' + t)
shutil.copy('Hb/gen.py', R + '/herramientas/briefs_agentes/gen_briefs.py')
shutil.copy('V/greek.py', R + '/herramientas/lectura_directa/greek.py')
shutil.copy('vid/transcript.txt', R + '/herramientas/lectura_directa/transcripcion_video.txt')
shutil.copy(CAPS + '/genv.py', R + '/herramientas/genv.py')
for i in range(1, 9):
    shutil.copy(f'H{i}.txt', R + f'/herramientas/briefs_agentes/H{i}.txt')
    for n in ('father.json', 'works.json', 'passages.json'):
        if os.path.exists(f'H{i}/{n}'):
            shutil.copy(f'H{i}/{n}', R + f'/herramientas/datos_agentes/H{i}_{n}')

def pdf(name, w, q):
    ims = []
    for f in files:
        im = Image.open('hbcards/' + f).convert('RGB')
        if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        ims.append(im)
    ims[0].save(R + '/' + name, save_all=True, append_images=ims[1:], resolution=120, quality=q)
    return os.path.getsize(R + '/' + name) / 1e6
mb = pdf('hebreos_10_28_padres_de_la_iglesia.pdf', 1200, 72)
print('pdf MB', mb, 'pages', len(files))

def cell(s): return s.replace('|', '\\|').replace('\n', ' ')
def link(u):
    m = re.match(r'(https?://\S+)', u)
    if not m: return u
    host = re.sub(r'^https?://(www[.])?', '', m.group(1)).split('/')[0]
    return f'[{host}]({m.group(1)})'
TAG = {'H': 'Hebreos', 'P': 'Razonamiento paralelo', 'D': 'Evangelio frente al AT', 'N': 'No matar a herejes', 'X': 'Matiz en contra'}

out = ["# Hebreos 10:28, Aquino y los Padres de la Iglesia: respuesta a un vídeo de TikTok (@antibulos1)", "",
 "Documentación, en diapositivas, que responde a un vídeo de TikTok (@antibulos1, 90 s) que cita **Hebreos 10:28** y **Tomás de Aquino** para decir que «la brutalidad» de la pena por apostasía también está en los textos cristianos. Está construida con el texto de Hebreos, silogismos, ocho Padres de la Iglesia (**dos diapositivas por Padre**: la cita en español, y la foto, la obra, los datos y una aclaración de la cita) y la respuesta al cierre del vídeo. Es documentación de lo que dicen las fuentes; no valora ninguna religión ni es una guía para actuar contra nadie.", "",
 "**Respuesta corta.** (1) **Hebreos 10:28 no manda nada**: describe lo que pasaba bajo la ley de Moisés («muere sin compasión, por dos o tres testigos») y lo usa en un argumento «cuánto más» que termina en el **juicio de Dios** (10:29-31, «Mía es la venganza»); en 10:26-31 no hay ningún imperativo. (2) De los **ocho Padres** que leí, **ninguno** usa Hebreos 10:28 como orden de ejecutar a nadie; solo Crisóstomo lo comenta, como un hecho del pasado. Crisóstomo, Orígenes, Tertuliano, Lactancio y Atanasio dicen expresamente que no se debe matar o forzar en materia de fe. **No hay unanimidad, y no hay que fingirla**: Agustín defendió la coerción legal (sin pedir la muerte de los donatistas), Crisóstomo admite frenar y silenciar a los herejes y Jerónimo invoca Dt 13 en una carta. (3) **Aquino** (s. XIII) es teólogo y no jurista, y no es tradición apostólica; su opinión sobre los herejes es «residual» frente a los Padres, no frente a la Edad Media latina. (4) El cierre del vídeo es un «tú también» y la comparación con la traición castiga **actos, no creencias**.", "",
 f"Todo junto en un PDF ({mb:.0f} MB): [`hebreos_10_28_padres_de_la_iglesia.pdf`](hebreos_10_28_padres_de_la_iglesia.pdf).", "",
 "## Diapositivas", "", "| Código | Contenido |", "|---|---|",
 "| [HB00](HB00_es.png) | Qué dice el vídeo (capturas) y cómo se responde |",
 "| [HB01](HB01_es.png) | El propio texto de Hebreos 10:26-31 (griego SBLGNT y traducción literal) |",
 "| [HB02](HB02_es.png) · [HB02b](HB02b_es.png) | Silogismos (descripción y prescripción; quién ejecuta; «cuánto más»; los dos pactos) y pasajes del NT |",
 "| [HB03](HB03_es.png) | El Evangelio como moral plena y el Antiguo Testamento como moral contextualizada y aún no plena |",
 "| [HB04](HB04_es.png) | Los ocho Padres de un vistazo (con foto) |"]
for i in sorted(P):
    f = P[i]
    out.append(f"| [{i}_cita]({i}_cita.png) · [{i}_info]({i}_info.png) | **{f['name']}** ({f['dates']}): la cita en español / foto, obra, datos y aclaración |")
out += ["| [AQ01](AQ01_es.png) · [AQ02](AQ02_es.png) | Aquino: qué dice y de dónde lo toma; tardío, teólogo, no jurista, no tradición apostólica |",
 "| [CV01](CV01_es.png) · [CV02](CV02_es.png) | El cierre del vídeo (el «tú también», la distinción y la traición) |",
 "| [HB09](HB09_es.png) | Fuentes leídas, resultados negativos, límites y avisos |", "",
 "Colores en las diapositivas de los Padres: amarillo = frase clave · azul = matiz o lo que juega en contra. Etiquetas: **Hebreos** · **Razonamiento paralelo** · **Evangelio frente al AT** · **No matar a herejes** · **Matiz en contra**.", "",
 "## Padres, obras citadas y fuentes", ""]
for i in sorted(P):
    f = P[i]
    out += [f"### {i} · {f['name']} ({f['dates']})", "", f"{f['role']}", "",
            "| Etiqueta | Obra | Referencia | Texto de partida |", "|---|---|---|---|"]
    for q in f['quotes']:
        out.append(f"| {', '.join(TAG[t] for t in q['theme'])} | {cell(q['work'])} | {cell(q['ref'])} | {link(q['url'])} |")
    out += ["", f"*Imagen:* {f['credit']} {f['img_note']} ([archivo](imagenes/{i}_{f['slug']}.jpg))", ""]
    if f.get('ojo'): out += [f"*Ojo:* {f['ojo']}", ""]
out += ["## Cómo se hizo", "",
 "Un orquestador y **8 agentes de búsqueda** (modelo pequeño, uno por Padre: Crisóstomo, Agustín, Orígenes, Ireneo, Tertuliano, Lactancio, Atanasio y Jerónimo) buscaron pasajes y una imagen de dominio público de cada uno (sus encargos están en `herramientas/briefs_agentes/` y lo que devolvieron, en `herramientas/datos_agentes/`). Después **comprobé yo** con un script (`herramientas/hbverify.py`) que cada cita inglesa está, letra por letra, en la página que el agente indicaba (82 de 83 pasajes; el único que no coincide, la carta de Ireneo a Víctor citada por Eusebio, no se usa) y que los fragmentos latinos y griegos mostrados están en su fuente (`hbverify_orig.py`). El texto griego de Hebreos lo leí en el SBLGNT (MorphGNT; `herramientas/lectura_directa/greek.py`); el vídeo, con Whisper large-v3 (transcripción en `herramientas/lectura_directa/transcripcion_video.txt`) y fotograma a fotograma; Aquino, en el latín del Corpus Thomisticum y en el inglés de la edición dominica de 1920; el artículo de Coetsee (2024), en su PDF de acceso abierto.", "",
 "## Avisos y límites", "",
 "1. **Las traducciones al español son mías**, hechas desde ediciones inglesas del siglo XIX de dominio público (ANF y NPNF); no he leído el griego ni el latín completos de las obras, solo los fragmentos mostrados donde pude comprobarlos. Pueden contener errores.",
 "2. **Resultados negativos**: ninguno de los ocho Padres usa Hebreos 10:28 como orden; Crisóstomo lo comenta, Orígenes cita 10:29 (sentido moral) y Tertuliano cita Heb 6:4-6; en Agustín no se buscó Hebreos 10:26-31 (solo coerción y Antiguo Testamento); en Ireneo, Lactancio, Atanasio y Jerónimo no hay cita de Heb 10:26-31 en lo leído. El Padre más adverso es Jerónimo (Carta 109 §3); Agustín defendió la coerción legal (Cartas 93 y 185).",
 "3. **«Residual» respecto de Aquino** vale frente a los Padres y la tradición apostólica, no frente a la Edad Media latina (allí la ejecución de herejes se contempló y practicó).",
 "4. **La frase «resecandae sunt putridae carnes»** que Aquino atribuye a Jerónimo (Comentario a Gálatas 5:9, según el Decreto de Graciano) no la pude verificar en la edición crítica: un agente no la halló en una edición de 1616 y el *Manipulus florum* la sitúa en *In Gal.* III (CCSL 77A, p. 163). No la uso como cita.",
 "5. **Fechas de vida y de obras**: aproximadas, convencionales; no las verifiqué una a una.",
 "6. **Imágenes**: grabados, mosaicos, iconos y pinturas de dominio público de Wikimedia Commons; ninguna es un retrato en vida. La de Ireneo es de baja resolución (245 × 325 px).",
 "7. **Errores de los agentes** que corregí: numeración de homilías (la Hom. 19 sobre Hebreos es sobre 10:19-25; 10:26-31 es la Hom. 20), Tito 3:10 en Crisóstomo (Hom. 6, no 3), «hachas y martillos» (Atanasio §33), «Dios sabe» (no «solo Dios sabe») en Eusebio sobre Orígenes, etc. Un agente de Tertuliano creó por error una sesión de Claude Code (archivada, sin trabajo) y el agente de Agustín quedó detenido por mí mientras reintentaba una imagen secundaria; sus datos ya estaban en disco.",
 "8. **La parte islámica del cierre (CV01-CV02)** remite a las tarjetas AP del pack [`apostasia-fuentes-tempranas`](../apostasia-fuentes-tempranas); no la he vuelto a verificar aquí.",
 "9. **Derechos**: las traducciones inglesas citadas son de dominio público; el texto griego es el SBLGNT (CC BY 4.0, Society of Biblical Literature y Faithlife). El artículo de Coetsee se cita brevemente. La versión JPS 2023 de Sefaria (CC BY-NC) no se cita.", "",
 "Herramientas de generación en `herramientas/` (`hbstatic.py`, `hbstatic2.py` y `genpad.py` generan las diapositivas; `renderhb.js` las convierte en PNG; `hbpadres.py` contiene los datos de los Padres)."]
open(R + '/README.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(files), 'diapositivas')
