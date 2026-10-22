import os, shutil, glob, json
from PIL import Image
B='/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad'
AT=B+'/ir'; AQ=B+'/iq'
R='/home/user/Pruebas/ireneo-lyon-manos-hijo-espiritu'
os.chdir(AT)
for d in ('','/herramientas','/herramientas/briefs_agentes','/herramientas/datos_agentes','/paginas'):
    os.makedirs(R+d,exist_ok=True)
order=['IR18']+[f'IR{i:02d}' for i in range(1,18)]+['IR20','IR21','IR22']
files=[o+'.png' for o in order]
for f in files: shutil.copy('ircards/'+f,R+'/'+f)
for f in glob.glob(AQ+'/pg/*.png'): shutil.copy(f,R+'/paginas/'+os.path.basename(f))
for t in ('irdata.py','irgen.py','packir.py'): shutil.copy(t,R+'/herramientas/'+t)
for t in ('hlz2.py',): shutil.copy(f'{AQ}/{t}',R+'/herramientas/resaltar_'+t)
shutil.copy(B+'/ay/renderhb.js',R+'/herramientas/renderhb.js'); shutil.copy(B+'/tq/hlz.py',R+'/herramientas/hlz.py'); shutil.copy(B+'/jd/hlpage.py',R+'/herramientas/hlpage.py')
for t in ('hbcss.py','genpad.py'): shutil.copy(f'{B}/hb/{t}',R+'/herramientas/'+t)
shutil.copy(AQ+'/gen.py',R+'/herramientas/gen_briefs.py')
for k in range(1,12):
    shutil.copy(f'{AQ}/I{k}.txt',R+f'/herramientas/briefs_agentes/I{k}.txt')
    for n in ('passages.json','notes.md'):
        p=f'{AQ}/I{k}/{n}'
        if os.path.exists(p): shutil.copy(p,R+f'/herramientas/datos_agentes/I{k}_{n}')
ims=[]
for f in files:
    im=Image.open('ircards/'+f).convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    ims.append(im)
PDF='ireneo_lyon_manos_hijo_espiritu.pdf'
ims[0].save(R+'/'+PDF,save_all=True,append_images=ims[1:],resolution=120,quality=72)
mb=os.path.getsize(R+'/'+PDF)/1e6; print('pdf MB',mb); assert mb<30
n=0
for p in glob.glob(AQ+'/I*/passages.json'):
    d=json.load(open(p)); n+=len(d['items'] if isinstance(d,dict) else d)
open(R+'/README.md','w',encoding='utf-8').write(f'''# Ireneo de Lyon, ¿trinitario? Las dos manos de Dios, el Hijo y el Espíritu

Pack de diapositivas en español sobre *Contra las herejías* y la *Demostración de la predicación apostólica* de Ireneo (hacia 180-190): **latín (y griego donde sobrevive) con traducción mía**, los **pasajes difíciles** (Dios «todo mente», Mc 13:32 «ni el Hijo», generación inenarrable, «sólo el Padre es Dios», «medida» e «invisible del Hijo», Sabiduría = Espíritu en 4.20.3, «Padre sobre todos» y subordinación) y su **resolución** con metafísica posterior (Atanasio, Agustín, Aquino, Gregorio Nacianceno, Tertuliano), **páginas reales** con texto subrayado (Harvey 1857 en latín; ANF en inglés) y lo que dicen los estudiosos (Bull, Newman, Bethune-Baker). Todo en un PDF ({mb:.0f} MB): [`{PDF}`]({PDF}).

## Veredicto honesto
Ireneo es el testigo más fuerte del siglo II y es **trinitario en estructura, con lenguaje preniceno**, no un trinitario niceno formulado. Tiene regla de fe de tres miembros (1.10.1; 4.33.7; Dem. 6), el Hijo y el Espíritu «siempre con» el Padre y como sus «manos» (4.20.1; 5.6.1; 5.28.4), «lo engendrado de Dios es Dios» (Dem. 47) y la generación «inenarrable». Pero no usa «consustancial» ni «Trinidad», el Padre es «sobre todos» y «sólo ingénito», la Sabiduría = Espíritu choca con Justino y Tertuliano, y Mc 13:32, «medida» e «invisible del Hijo» sólo se resuelven con la metafísica posterior, que es una **relectura**.

| Diapositiva | Contenido |
|---|---|
| IR18 | Mapa: veredicto y tabla de pasajes difíciles |
| IR01-IR03 | Quién es y qué se conserva; regla de fe; creación por Verbo, Espíritu y Sabiduría |
| IR04-IR08 | Pasajes A-E: 2.13/2.28.5; Mc 13:32; generación inenarrable; 3.6.1/3.9.1; «medida» e invisible |
| IR09-IR12 | Las «manos»; Sabiduría = Espíritu (4.20.3); subordinación; el Espíritu |
| IR13 | Lo que Ireneo no dice y correcciones |
| IR14-IR15 | Estudiosos a favor y objeciones |
| IR16-IR17 | Metafísica posterior |
| IR20-IR21 | **Páginas reales**: Harvey pp. 213-214; ANF pp. 330, 401, 488 |
| IR22 | Fuentes, correcciones y límites |

## Lo que se leyó y lo que no
- **Visto por mí en imagen:** Harvey vol. 2 pp. 213-214; ANF vol. 1 pp. 330, 401, 488.
- **Resto del latín:** leído por los investigadores en Harvey, casi todo sin capa de texto (OCR; marcado en cada cita).
- **Demostración:** sólo existe en armenio; no lo leí; uso Robinson 1920 (inglés). Fragmentos de Pfaff excluidos (espurios o dudosos).
- **No leídos:** Kelly, Lawson, Briggman, Behr, Osborn, Steenberg (restringidos).

## Correcciones
«Por el Verbo y el Espíritu» es 1.22.1; «manos = Hijo y Espíritu» está en 5.6.1, 5.28.4 y el prefacio del libro 4, no en 4.20.1; «Padre de todos» es 3.6.5; la *Demostración* dice «tres puntos»; Atanasio (NPNF2) no nombra a Ireneo; Aquino: I q.42 a.5; ANF y Harvey numeran distinto (ANF 3.16.6 = Harvey 3.17.6).

## Cómo se hizo
Orquestador (yo) y 11 investigadores (Haiku, nivel alto): I1 Haer. 1 y 2.1-27; I2 2.28-35; I3 3.1-15; I4 3.16-25; I5 4.1-19; I6 4.20-41; I7 libro 5; I8 *Demostración*; I9 escaneos y latín; I10 estudiosos; I11 metafísica. Encargos y datos ({n} registros) en `herramientas/`. Incidentes: un agente mató procesos de otro y el disco se llenó; se resolvió sin perder datos.
''')
print('ok')
