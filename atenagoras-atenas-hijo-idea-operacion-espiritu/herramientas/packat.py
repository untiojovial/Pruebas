import os, shutil, glob, json
from PIL import Image
B='/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad'
AT=B+'/at'; AQ=B+'/aq'
R='/home/user/Pruebas/atenagoras-atenas-hijo-idea-operacion-espiritu'
os.chdir(AT)
for d in ('','/herramientas','/herramientas/briefs_agentes','/herramientas/datos_agentes','/paginas'):
    os.makedirs(R+d,exist_ok=True)
order=['AT18']+[f'AT{i:02d}' for i in range(1,18)]+['AT19','AT20','AT21']
files=[o+'.png' for o in order]
for f in files: shutil.copy('atcards/'+f,R+'/'+f)
for f in glob.glob(AQ+'/pg/*.png'): shutil.copy(f,R+'/paginas/'+os.path.basename(f))
for t in ('atdata.py','atgen.py','packat.py'): shutil.copy(t,R+'/herramientas/'+t)
for t in ('V_o46.py','V_o48.py','V_o124.py','bands.py','hlz2.py'): shutil.copy(f'{AQ}/{t}',R+'/herramientas/resaltar_'+t)
shutil.copy(B+'/ay/renderhb.js',R+'/herramientas/renderhb.js'); shutil.copy(B+'/tq/hlz.py',R+'/herramientas/hlz.py'); shutil.copy(B+'/jd/hlpage.py',R+'/herramientas/hlpage.py')
for t in ('hbcss.py','genpad.py'): shutil.copy(f'{B}/hb/{t}',R+'/herramientas/'+t)
shutil.copy(AQ+'/gen.py',R+'/herramientas/gen_briefs.py')
for k in range(1,12):
    shutil.copy(f'{AQ}/A{k}.txt',R+f'/herramientas/briefs_agentes/A{k}.txt')
    for n in ('passages.json','notes.md'):
        p=f'{AQ}/A{k}/{n}'
        if os.path.exists(p): shutil.copy(p,R+f'/herramientas/datos_agentes/A{k}_{n}')
ims=[]
for f in files:
    im=Image.open('atcards/'+f).convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    ims.append(im)
PDF='atenagoras_atenas_hijo_idea_operacion_espiritu.pdf'
ims[0].save(R+'/'+PDF,save_all=True,append_images=ims[1:],resolution=120,quality=72)
mb=os.path.getsize(R+'/'+PDF)/1e6; print('pdf MB',mb); assert mb<30
n=0
for p in glob.glob(AQ+'/A*/passages.json'):
    d=json.load(open(p)); n+=len(d['items'] if isinstance(d,dict) else d)
open(R+'/README.md','w',encoding='utf-8').write(f'''# Atenágoras de Atenas, ¿trinitario? El Hijo «en idea y operación», la «efusión» y el orden

Pack de diapositivas en español sobre la *Legación en favor de los cristianos* y *Sobre la resurrección de los muertos* de Atenágoras (hacia 176-180): **griego con traducción**, los **pasajes difíciles** («el Hijo… Verbo del Padre en idea y en operación», «primer engendrado… no como hecho» pero «salió» para crear, el Espíritu como «efusión» que vuelve como rayo, «su poder en la unión y su distinción en el orden», el «unidos en poder» de Leg. 24, ángeles, «sólo eterno el Dios ingénito») y su **resolución** con metafísica posterior (Atanasio, Agustín, Aquino, Basilio, Gregorio de Nacianzo, Tertuliano), **páginas reales** con el texto subrayado (Otto 1857 en griego; ANF en inglés) y lo que dicen los estudiosos. Todo en un PDF ({mb:.0f} MB): [`{PDF}`]({PDF}).

## Veredicto honesto
Atenágoras es **trinitario «en intención»**, no un trinitario formulado. Llama «Hijo» al Verbo, lo hace «no hecho» y engendrado de una «mente eterna», lo pone «en» el Padre y «uno» con él, y enumera «Dios Padre, Dios Hijo y Espíritu Santo» con «unión» y «distinción en el orden». Pero: el Espíritu es una «efusión» de personalidad discutida (Loofs, Dorner), la unidad se dice **«en poder»** y no «en esencia» (el «unidos en esencia» de la traducción ANF **no está en el griego**), el «salió» para crear admite una lectura temporal (Newman p. 198), y la *Legación* no habla de Jesucristo. La resolución nicena es una **relectura**, no lo que él formuló.

| Diapositiva | Contenido |
|---|---|
| AT18 | Mapa: veredicto y tabla de pasajes difíciles |
| AT01 | Quién es; testimonios (Felipe de Side, Metodio) y silencio de Eusebio |
| AT02-AT03 | Leg. 4, 6, 8, 9: Verbo, Espíritu, «indivisible», el flautista |
| AT04-AT08 | Leg. 10, 12, 24: «idea y operación», «primer engendrado», «efusión», «unión y distinción», «unidos en poder» |
| AT09-AT10 | Ángeles; Leg. 12 y 30 («conocer a Dios y a su Verbo», «sólo eterno») |
| AT11-AT12 | *Sobre la resurrección* (sin doctrina trinitaria; autoría discutida) y lo que no dice |
| AT13-AT14 | Estudiosos: a favor (Bull, Bethune-Baker, Dorner) y objeciones (Newman, Loofs) |
| AT15-AT16 | Metafísica posterior (Atanasio, Agustín, Aquino, Basilio, Gregorio, Tertuliano) |
| AT17 | Paralelos: Justino, Taciano, Teófilo, Ireneo |
| AT19-AT20 | **Páginas reales**: Otto pp. 46, 48 y 124; ANF pp. 133 y 141 |
| AT21 | Fuentes, correcciones y límites |

## Lo que se leyó y lo que no
- **Visto por mí en imagen de página:** Otto 1857 pp. 46, 48 y 124; ANF vol. 2 pp. 133 y 141.
- **Griego** del resto: leído por los investigadores en el escaneo de Otto (algunos solo por OCR; marcado en cada cita).
- **Inglés/alemán** (ANF, NPNF, Bull, Newman, Bethune-Baker, Dorner, Loofs): PDFs abiertos; Loofs en alemán con traducción de un investigador.
- **No leídos:** Prestige, Kelly, Barnard, Grant, Behr, Schoedel (restringidos); Migne PG 6 (700 MB); Focio cód. 234 y Epifanio (Haer. 64).

## Correcciones
«Unidos en esencia» (Leg. 24) es la traducción inglesa y la conjetura de Gesner (rechazada por Otto), no el griego impreso; «Verbo que procede de él» (Leg. 18) en la ANF corresponde sólo a *par’ autoû*, «de él»; no hay «Jesús», «Cristo» (sólo «cristianos»), «tríada» ni «consustancial»; Eusebio no nombra a Atenágoras; *Sobre la resurrección* no tiene doctrina trinitaria y su autoría la discute Grant (1954).

## Cómo se hizo
Orquestador (yo) y 11 investigadores (Haiku, nivel alto): A1 Leg. 1-9; A2 Leg. 10; A3 Leg. 10-12; A4 Leg. 13-23; A5 Leg. 24-27; A6 Leg. 28-37; A7 *Sobre la resurrección*; A8 escaneos y griego; A9 estudiosos; A10 metafísica; A11 recepción y paralelos. Un límite de uso cortó a ocho de ellos y los retomé. Encargos y datos ({n} registros) en `herramientas/`. Traducciones al español mías.
''')
print('ok')
