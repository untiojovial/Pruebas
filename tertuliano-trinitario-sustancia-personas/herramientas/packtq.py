import os, shutil, glob
from PIL import Image
TQ='/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/tq'
HB='/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb'
AY='/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ay'
JD='/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/jd'
R='/home/user/Pruebas/tertuliano-trinitario-sustancia-personas'
os.chdir(TQ)
for d in ('','/herramientas','/herramientas/briefs_agentes','/herramientas/datos_agentes','/paginas'):
    os.makedirs(R+d,exist_ok=True)
order=['TQ00']+[f'TQ{i:02d}' for i in range(1,16)]+['TQ99']
files=[o+'.png' for o in order]
for f in files: shutil.copy('tqcards/'+f,R+'/'+f)
for f in glob.glob('cap/k*.png'): shutil.copy(f,R+'/paginas/kroymann_csel47_'+os.path.basename(f))
for t in ('gen.py','lib.py','tqdata.py','tqgen.py','chk.py','hlz.py','packtq.py'): shutil.copy(t,R+'/herramientas/'+t)
shutil.copy(AY+'/renderhb.js',R+'/herramientas/renderhb.js'); shutil.copy(JD+'/hlpage.py',R+'/herramientas/hlpage.py')
for t in ('hbcss.py','genpad.py'): shutil.copy(f'{HB}/{t}',R+'/herramientas/'+t)
for k in range(1,12):
    shutil.copy(f'T{k}.txt',R+f'/herramientas/briefs_agentes/T{k}.txt')
    for n in ('passages.json','notes.md'):
        if os.path.exists(f'T{k}/{n}'): shutil.copy(f'T{k}/{n}',R+f'/herramientas/datos_agentes/T{k}_{n}')
ims=[]
for f in files:
    im=Image.open('tqcards/'+f).convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    ims.append(im)
PDF='tertuliano_trinitario_sustancia_personas.pdf'
ims[0].save(R+'/'+PDF,save_all=True,append_images=ims[1:],resolution=120,quality=72)
mb=os.path.getsize(R+'/'+PDF)/1e6; print('pdf MB',mb); assert mb<30
open(R+'/README.md','w',encoding='utf-8').write(f'''# Tertuliano, trinitario: una sustancia, tres personas

Pack de diapositivas en español con **latín de Tertuliano + traducción**, los **pasajes difíciles** que usan arrianos y antitrinitarios y su **resolución** con metafísica (Bull, Hilario, Atanasio, Tomás de Aquino), y **páginas reales** de la edición crítica de Kroymann con el latín subrayado. Todo en un PDF ({mb:.0f} MB): [`{PDF}`]({PDF}).

## Veredicto honesto
Tertuliano es **trinitario en sustancia**: una sola sustancia (*unius substantiae*), tres que se distinguen realmente, divinidad del Hijo y del Espíritu (*tertium nomen divinitatis*, *trinitas unius divinitatis*), regla de fe y fórmula bautismal trinitarias. **No es arriano.** Pero su lenguaje sobre *cómo* procede el Hijo (*derivatio et portio*, «natividad perfecta» en la creación, «hubo un tiempo en que no existían el pecado ni el Hijo», Adv. Herm. 3.4) es **preniceno**: «portio» se explica y se corrige con la tradición posterior; «hubo un tiempo…» **no se resuelve del todo** y es lo que Nicea precisó (generación eterna). Lo dicen sus propios defensores (Bull según Kaye; Kaye).

| Diapositiva | Contenido |
|---|---|
| TQ00 | Mapa: veredicto y tabla de pasajes difíciles |
| TQ01-TQ06 | Evidencia trinitaria: vocabulario, una sustancia, tres distintos, divinidad del Hijo, el Espíritu, reglas de fe |
| TQ07-TQ08 | Pasaje 1 («hubo un tiempo…», Adv. Herm. 3) y su resolución |
| TQ09-TQ10 | Pasaje 2 («derivatio totius et portio», Adv. Prax. 9) y su resolución |
| TQ11 | «El Padre es mayor», «segundo», «vicario» |
| TQ12 | «Natividad perfecta» del Verbo |
| TQ13 | Qué dicen los estudiosos (Bull, Kaye) |
| TQ14-TQ15 | **Páginas reales** de Kroymann (CSEL 47) con el latín subrayado |
| TQ99 | Fuentes, correcciones y límites |

## Lo que se leyó y lo que no
- **Visto en imagen de página:** Kroymann, CSEL 47 (1906), pp. 129, 230, 239, 246, 248, 276, 288 (escaneo abierto de archive.org; subrayado mío). Bull, *Defensio*, pp. 193 y 200 (PDF abierto).
- **Latín** de cada cita mostrada, comprobado por programa contra Kroymann (OCR), Migne y la Latin Library (`herramientas/chk.py`); *De Pudicitia* 21.16 comprobado en la Latin Library y en Migne.
- **Inglés** (ANF, Bull, Kaye, Atanasio, Hilario, Aquino): de versiones públicas en inglés; no leí el griego de Atanasio ni el latín de Hilario y Aquino.
- **No leídos (sin texto abierto):** Kelly, Evans, Osborn, Barnes, Daniélou, Moingt, Hanson: no los cito.

## Correcciones a lo que se pidió o se suponía
«Deum de Deo» no está en *Apol.* 21 (solo en *Ad Nat.* 2.3); «alius, non aliud» no aparece en *Adv. Prax.* 13-25 ni en el latín leído; «tertius» del Espíritu está en *Prax.* 8.7, no en 25; bautismo trino en *De Baptismo* 13.3 (no 6 y 8); *Scorpiace* 9.3 (no 10); Kroymann marca como posible interpolación el final del cap. 3 de *Adv. Prax.* y corchetea «oportebat et patrem crucifigi» (cap. 10): no los uso. En *Adv. Herm.* 3.4 la Latin Library lee «cum ei delictum» y Kroymann «cum et delictum».

## Cómo se hizo
Orquestador (yo) y 11 investigadores (Haiku, nivel alto): T1-T5 *Adv. Prax.* por capítulos, T6 Espíritu y «trinitas», T7 *Adv. Herm.*, T8 otras obras y reglas de fe, T9 estudiosos, T10 metafísica, T11 escaneos. Sus encargos y datos (209 pasajes) están en `herramientas/briefs_agentes/` y `herramientas/datos_agentes/`. Las traducciones al español son mías.

## Límites
Las páginas impresas de la ANF no las vi (la ANF digital tiene otra paginación); cito capítulo y sección. El OCR de Kroymann tiene errores; el texto subrayado se corresponde con la imagen. La metafísica posterior (Atanasio, Hilario, Aquino) es una explicación, no una prueba de qué pensaba Tertuliano.
''')
print('ok')
