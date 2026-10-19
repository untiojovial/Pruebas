# -*- coding: utf-8 -*-
# Empaqueta el pack «¿Dijo Jesús que era Dios?» en el repositorio
import os, shutil, glob
from PIL import Image
JD = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/jd'
TT = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/tt'
AY = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ay'
HB = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb'
R = '/home/user/Pruebas/jesus-divinidad-respuesta-video-isa-rojas'
os.chdir(JD)
for d in ('', '/herramientas', '/herramientas/briefs_agentes', '/herramientas/datos_agentes', '/herramientas/paginas_usadas', '/herramientas/video', '/evidencia'):
    os.makedirs(R + d, exist_ok=True)
order = ['JD00', 'JDG1', 'JDG2', 'JDG3', 'JDG4'] + [f'JD0{i}' for i in range(1, 9)]
for f in ['BK', 'BR', 'WR', 'HU', 'SC', 'BO', 'PI', 'BI']:
    order += [f + '_cita', f + '_info']
order += ['JD90', 'JD99']
files = [o + '.png' for o in order]
for f in files:
    assert os.path.exists('jdcards/' + f), f
    shutil.copy('jdcards/' + f, R + '/' + f)
shutil.copy('guion.md', R + '/guion_video.md')
for t in ('gen.py', 'jdpoints.py', 'jdsch.py', 'jdgen.py', 'hlpage.py', 'mkpages.py', 'webshot.js', 'packjd.py', 'cfg2.json', 'cfg3.json', 'cfg4.json'):
    shutil.copy(t, R + '/herramientas/' + t)
shutil.copy(AY + '/renderhb.js', R + '/herramientas/renderhb.js')
for t in ('hbcss.py', 'genpad.py'):
    shutil.copy(f'{HB}/{t}', R + '/herramientas/' + t)
for j in range(1, 12):
    shutil.copy(f'J{j}.txt', R + f'/herramientas/briefs_agentes/J{j}.txt')
    for n in ('passages.json', 'notes.md', 'works.json'):
        if os.path.exists(f'J{j}/{n}'):
            shutil.copy(f'J{j}/{n}', R + f'/herramientas/datos_agentes/J{j}_{n}')
for f in glob.glob('pg/*.png'):
    b = os.path.basename(f)
    if b.startswith(('clj_test', 'test_')) or b.endswith('.tmp.png'): continue
    shutil.copy(f, R + '/herramientas/paginas_usadas/' + b)
shutil.copy(TT + '/analisis_video.md', R + '/herramientas/video/analisis_video.md')
shutil.copy(TT + '/transcripcion.txt' if os.path.exists(TT + '/transcripcion.txt') else TT + '/transcripcion.txt', R + '/herramientas/video/transcripcion_whisper_large-v3.txt')
shutil.copy(TT + '/sub_spa.txt', R + '/herramientas/video/subtitulos_tiktok_spa-ES.vtt')
shutil.copy(TT + '/tr.py', R + '/herramientas/video/transcribir.py')
shutil.copy(JD + '/J11/dl/page_platner_pdf101.png', R + '/evidencia/plinio_epist_X96_platner_1894_p91.png')
for src, dst in (('full/dunn_crop.png', 'dunn_fotograma_4m32s.png'), ('full/verm_crop.png', 'vermes_resena_fotograma_4m39s.png'), ('full/bcrop168.png', 'brown_p84_fotograma_2m48s.png')):
    shutil.copy(TT + '/' + src, R + '/evidencia/' + dst)

def pdf(name, w, q):
    ims = []
    for f in files:
        im = Image.open('jdcards/' + f).convert('RGB')
        if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        ims.append(im)
    ims[0].save(R + '/' + name, save_all=True, append_images=ims[1:], resolution=120, quality=q)
    return os.path.getsize(R + '/' + name) / 1e6
PDF = 'jesus_divinidad_respuesta_video_isa_rojas.pdf'
mb = pdf(PDF, 1200, 72)
print('pdf MB', mb, 'paginas', len(files))
assert mb < 30

README = f'''# ¿Dijo Jesús que era Dios? Respuesta al vídeo de @isarojasmx (Cap. 8 de «El Nuevo Testamento a examen»)

Pack de diapositivas con **guion, silogismos por punto y ocho académicos con la página subrayada** para responder a un vídeo de TikTok que sostiene que Jesús nunca se presentó como Dios y que hay «amplio consenso académico» en ello. Todo junto en un PDF ({mb:.0f} MB): [`{PDF}`]({PDF}).

**El vídeo**: [@isarojasmx (Isa Rojas), «El Nuevo Testamento a examen, Cap. 8: ¿Jesús dijo que era Dios?»](https://vm.tiktok.com/ZGdCXHYdB/) (7 min 21 s). Lo analicé con los subtítulos automáticos de TikTok, una transcripción de Whisper large-v3 y 74 fotogramas; la transcripción y el análisis están en `herramientas/video/`. Cita a Raymond Brown, James Dunn, Géza Vermes, Bart Ehrman y Brant Pitre. **Sobre quién es «él»**: no me lo dijeron al pedir el pack y trabajé desde las objeciones que contestan los dossiers del blog «Defendiendo la Fe»; después me pasaron este vídeo y rehíce los puntos sobre él. Si hay otros vídeos del mismo autor, habría que añadirlos.

## Diapositivas

| Código | Contenido |
|---|---|
| [JD00](JD00.png) | Mapa: los ocho puntos del vídeo, qué hay que conceder y respuesta en una línea |
| [JDG1](JDG1.png)–[JDG3](JDG3.png), [JDG4](JDG4.png) | **Guion** (≈8 min, con la diapositiva que va en pantalla y los silogismos) y versión corta para TikTok (≈75 s). También en [`guion_video.md`](guion_video.md) |
| [JD01](JD01.png)–[JD08](JD08.png) | Un punto del vídeo por diapositiva: lo que dice, lo que se puede conceder, respuesta, **silogismo** y fuentes |
| BK, BR, WR, HU, SC, BO, PI, BI (`_cita` y `_info`) | Ocho académicos, **dos diapositivas cada uno**: la cita en español (oro = lo que afirma, azul = lo que concede) y la obra con la **captura de la página y el texto subrayado** |
| [JD90](JD90.png), [JD99](JD99.png) | Aviso sobre el blog «Defendiendo la Fe»; fuentes, método y límites |

Académicos: **BK** Richard Bauckham · **BR** Raymond E. Brown · **WR** N. T. Wright · **HU** Larry Hurtado · **SC** Peter Schäfer · **BO** Daniel Boyarin · **PI** Brant Pitre · **BI** Michael Bird y Craig Evans.

## Resultado en pocas líneas

- **El vídeo acierta** en que en los Sinópticos Jesús no dice «soy Dios, adórenme», en que el título «Dios» aplicado a Jesús es tardío y en que Ap 1:11 («Alfa y Omega») falta en el Sinaítico. Lo digo en las diapositivas sin rodeos.
- **No demuestra lo que concluye.** (1) La página de Dunn que enseña tiene la frase subrayada solo hasta el punto y coma: sigue «pero podemos afirmar que la enseñanza en ese sentido […] fue una reflexión adecuada y elaboración del propio sentido de filiación […] de Jesús», y la frase anterior habla de «conciencia de autoridad divina» en el estrato más antiguo. (2) La frase «no deja rastro en los sinópticos» es de **Renan** (1863), no de Vermes; lo que se enseña de Vermes es una reseña. (3) Brown habla del *título* «Dios»; en su artículo de 1965 responde «afirmativamente» a si el NT llama Dios a Jesús (tres casos claros, cinco probables) y dice que *kyrios* es la traducción estándar de YHWH. (4) El «rotundo no» de Pitre es la descripción de la opinión que su artículo (Church Life Journal, 4-2-2025) va a discutir; su tesis es que Jesús sí habló y actuó como divino, «de una manera muy judía». (5) Ehrman niega que Jesús lo dijera, pero admite que los primeros cristianos lo creyeron muy pronto.
- **Los académicos están divididos** y las diapositivas lo muestran con sus límites: Wright, Pitre, Bird y Evans defienden una pretensión implícita; Hurtado, Dunn, Ehrman y Brown (para el título) no ven evidencia de una pretensión explícita; Bauckham, Schäfer y Hurtado muestran una cristología alta muy temprana y judía.
- **Huecos del blog** «Defendiendo la Fe»: no responde a Jn 9:9, Jer 1:5, Dn 2:37, Ap 3:12, la frase de Brown, Mt 9:8, Jn 20:23 ni «Hijo del hombre» = Ezequiel, ni a los puntos 7 y 8 del vídeo; además tiene varios errores (JD90). Este pack cubre esos huecos.

## Qué se leyó de verdad (y qué no)

- **Páginas reales vistas y reproducidas con subrayado mío**: Bauckham 2018, pp. 12-13 (PDF abierto de la editorial); Brown 1965, pp. 565-566 (PDF abierto de *Theological Studies*); Schäfer 2020, p. 5 (muestra de la editorial); Hurtado, «Christology» (*NIDB*, versión del autor, sin paginación impresa); y páginas web de Pitre (CLJ), Wright (ntwrightpage.com), Hurtado (blog) y el extracto de Bird y Evans (Zondervan). Plinio, *Epist.* X 96, p. 91 de Platner (1894): leída en la imagen de la página.
- **De segunda mano o parcial**: Boyarin (epígrafe de Pitre y un ensayo reproducido en un blog), Segal (blog), la continuación de la frase de Dunn (leída en el fotograma del vídeo; no localicé la edición ni la página: Pitre cita la 2.ª ed., p. 254), Vermes (solo la reseña citada), Brown 1994 (fragmentos; la p. 84 castellana, solo en el fotograma).
- **No leídos**: los libros principales de Bauckham (2008), Hurtado (2003), Wright (1996), Pitre (2024), Evans, Bock y Gathercole (Google Books bloqueado; archive.org solo presta). Tampoco el apéndice «Ego eimi» del comentario de Brown a Juan, ni su «Did Jesus Know He Was God?» (1985): **no los cito**.
- **Apocalipsis**: el Sinaítico, por la transcripción de codexsinaiticus.org (no el facsímil); el Alejandrino, NA28 y Metzger no los obtuve.
- Los textos bíblicos están en traducción mía; todas las traducciones del inglés son mías.

## Cómo se hizo

Un orquestador (yo) y **once investigadores** (modelo Haiku, nivel alto): J1-J3 leyeron los 36 dossiers del blog (objeciones, argumentos, silogismos y errores); J4 Bauckham; J5 Hurtado y Tilling; J6 Wright y Hays; J7 Boyarin, Segal y Schäfer; J8 Brown, Hengel, Moule y Ratzinger; J9 Bock, Gathercole, Evans, Witherington y Bird; J10 los que niegan o matizan (Dunn, Vermes, Ehrman, Casey, Sanders, Fredriksen, Pitre); J11 culto temprano a Cristo y fuentes primarias (Plinio, Ignatio, Didaché, Justino, Apocalipsis en el Sinaítico). Sus encargos, hallazgos y notas están en `herramientas/briefs_agentes/` y `herramientas/datos_agentes/`. Después de que me pasaran el vídeo, mandé a J1-J11 los puntos exactos y las páginas que enseña. **Yo comprobé en la página** las citas de Bauckham, Brown, Schäfer, Hurtado (*NIDB*), el artículo de Pitre, el ensayo de Wright, el extracto de Bird y Evans y Plinio; y en los fotogramas, Dunn, Vermes y Brown (castellano).

`herramientas/hlpage.py` convierte una página de PDF en imagen y subraya las frases (con `pdftotext -bbox`); `webshot.js` hace lo mismo con páginas web (Playwright); `jdgen.py`, `jdpoints.py` y `jdsch.py` generan las diapositivas.

## Límites y avisos

1. El pack responde **a este vídeo**; no sé si «él» ha dicho más cosas en otros.
2. Muchas citas de libros modernos son de PDFs o webs abiertos y no de los libros completos; las diapositivas marcan lo que es página real y lo que es texto de segunda mano.
3. **Hurtado** y **Brown** conceden cosas que el vídeo puede usar (la historia crítica no da evidencia de una afirmación explícita; Jesús no se llama «Dios» en los Sinópticos); están dichas en sus diapositivas.
4. Bird, Pitre y Evans son evangélicos o católicos que defienden una tesis; no son un «consenso».
5. Los silogismos son válidos en su forma; sus premisas históricas (que Jesús dijera Jn 8:58, que Mc 14:62 sea histórico) son las que discuten Hurtado, Dunn y Ehrman. Las diapositivas lo indican.
6. Las capturas de las páginas llevan la atribución a su fuente y son recortes para cita; no se incluyen los PDF completos.
7. Los errores del blog («Policarpo 14», Ap 19:10, Hch 12:7, 1QIsa<sup>a</sup>, etc.) los señalaron los investigadores; no todos los recomprobé yo (JD90 lo dice).
'''
open(R + '/README.md', 'w', encoding='utf-8').write(README)
print('ok')
