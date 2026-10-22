import os, shutil, glob, json
from PIL import Image
B='/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad'
HR=B+'/hr'; HQ=B+'/hq'
R='/home/user/Pruebas/hipolito-roma-un-poder-dos-personas-tercera-gracia'
os.chdir(HR)
for d in ('','/herramientas','/herramientas/briefs_agentes','/herramientas/datos_agentes','/paginas'):
    os.makedirs(R+d,exist_ok=True)
order=['HP19']+[f'HP{i:02d}' for i in range(1,19)]+['HP20','HP21','HP22','HP23']
files=[o+'.png' for o in order]
for f in files: shutil.copy('hrcards/'+f,R+'/'+f)
for f in glob.glob(HR+'/pg/hp*.png')+glob.glob(HR+'/pg/mil*.png')+glob.glob(HR+'/pg/dun*.png'): shutil.copy(f,R+'/paginas/'+os.path.basename(f))
for t in ('hrdata.py','hrgen.py','packhr.py','mkcap.py','bands.py'): shutil.copy(t,R+'/herramientas/'+t)
shutil.copy(B+'/ay/renderhb.js',R+'/herramientas/renderhb.js')
for t in ('hbcss.py','genpad.py'): shutil.copy(f'{B}/hb/{t}',R+'/herramientas/'+t)
shutil.copy(HQ+'/ctx.txt',R+'/herramientas/briefs_agentes/ctx_comun.txt')
for k in range(1,12):
    shutil.copy(f'{HQ}/H{k}.txt',R+f'/herramientas/briefs_agentes/H{k}.txt')
    for n in ('passages.json','notes.md'):
        p=f'{HQ}/H{k}/{n}'
        if os.path.exists(p): shutil.copy(p,R+f'/herramientas/datos_agentes/H{k}_{n}')
ims=[]
for f in files:
    im=Image.open('hrcards/'+f).convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    ims.append(im)
PDF='hipolito_roma_un_poder_dos_personas_tercera_gracia.pdf'
ims[0].save(R+'/'+PDF,save_all=True,append_images=ims[1:],resolution=120,quality=72)
mb=os.path.getsize(R+'/'+PDF)/1e6; print('pdf MB',mb,len(files)); assert mb<30
n=0
for p in glob.glob(HQ+'/H*/passages.json'):
    d=json.load(open(p)); n+=len(d['items'] if isinstance(d,dict) else d)
open(R+'/README.md','w',encoding='utf-8').write(f'''# Hipólito de Roma, ¿trinitario? «Un solo poder, dos personas, y la tercera la gracia del Espíritu»

Pack de diapositivas en español sobre *Contra Noeto*, la *Refutación de todas las herejías* y otras obras de Hipólito (hacia 200-235): **griego con traducción mía**, los **pasajes difíciles** («el Padre manda, el Hijo obedece», el Verbo «Hijo por lo que iba a ser», el Verbo «concebido» y «engendrado» para crear, «te has hecho Dios», la acusación de «ditheísmo» por Calixto, el Espíritu como «gracia») y su **resolución** con metafísica posterior (Tertuliano, Atanasio, Basilio, Gregorio de Nacianzo, Agustín, Aquino), **páginas reales** con el texto subrayado (Lagarde 1858, Miller 1851, Duncker-Schneidewin 1859) y lo que dicen los estudiosos (Bull, Newman, Harnack, Bethune-Baker, Döllinger). Todo en un PDF ({mb:.0f} MB): [`{PDF}`]({PDF}).

## Veredicto honesto
Hipólito es un testigo temprano de la **estructura** trinitaria y **no es un trinitario niceno formulado**. Tiene «un solo Dios, dos personas (*prosopa*) y la tercera, la gracia del Espíritu Santo» (C. Noet. 14), «uno en poder» (7-8), «estos son verdaderamente tres» (8), «tríada» (14), «el Verbo es Dios, siendo la *ousía* de Dios» (Ref. 10.33) y «Cristo es el Dios sobre todo» (10.34). Pero la unidad se dice «en poder» y «economía», no «en esencia»; el Espíritu es «gracia» y «tercera economía»; el Hijo se «llama» así «por lo que iba a ser» (C. Noet. 15) y el Verbo se «concibe» y «engendra» para crear. La resolución nicena es una **relectura**, no lo que él formuló.

| Diapositiva | Contenido |
|---|---|
| HP19 | Mapa: veredicto y tabla de pasajes difíciles |
| HP01-HP02 | Quién es; Noeto y el modalismo que combate |
| HP03-HP05 | C. Noet. 7-8, 10-11, 14: «un poder, dos personas, tres» |
| HP06-HP08 | Pasajes A-C: «manda/obedece»; «Hijo por lo que iba a ser»; Verbo «engendrado» para crear |
| HP09-HP11 | Ref. 10.33 «ousía»; deificación; Calixto y el «ditheísmo» |
| HP12-HP13 | Daniel y Cristo y Anticristo; textos dudosos y espurios |
| HP14 | Lo que Hipólito NO dice y correcciones |
| HP15-HP16 | Estudiosos a favor y objeciones |
| HP17-HP18 | Metafísica posterior |
| HP20-HP22 | **Páginas reales**: Lagarde pp. 51-54; Miller p. 336; Duncker p. 458 |
| HP23 | Fuentes, correcciones y límites |

## Lo que se leyó y lo que no
- **Visto por mí en imagen de página:** Lagarde 1858 pp. 51-54; Miller 1851 p. 336; Duncker-Schneidewin 1859 p. 458.
- **Resto del griego:** leído por los investigadores en imagen u OCR (marcado en cada cita).
- **No leídos:** Kelly, Prestige, Hanson, Simonetti, Quasten, Nautin, Brent, Cerrato, Butterworth, Dix (restringidos); Wendland GCS 26 (no hallado); Focio cód. 121 sólo en imagen y OCR. No resolví el «problema de Hipólito» (¿uno o dos autores?) ni la variante «λόγος σὰρξ ἦν» de Lagarde. No hallé el texto del Credo Niceno en las fuentes leídas.

## Correcciones
«El Verbo es Dios, sustancia de Dios» es Ref. X.33, no X.32; «cuando quiso creó el mundo» y «serás un dios» no están con esas palabras; «el Padre manda, el Hijo obedece» es C. Noet. 14 (no 12-13) y «dos personas» ya está en el cap. 7; *Contra Noeto* termina en el cap. 18 con una doxología; el horno es Dan 3 (LXX 3:92-93), no «4.11»; el traductor de C. Noet. en ANF vol. 5 es Salmond (no MacMahon); la *Tradición apostólica* no se conserva en griego y su atribución es discutida; el «homoousion» sahídico es tardío; el «Trinity» de *Contra Beron* es glosa de la ANF.

## Cómo se hizo
Orquestador (yo) y 11 investigadores (Haiku, nivel alto): H1 C. Noet. 1-8; H2 C. Noet. 9-18; H3 Ref. IX; H4 Ref. X.28-34; H5 Daniel y Cristo y Anticristo; H6 Tradición apostólica; H7 obras dudosas; H8 identidad; H9 escaneos; H10 estudiosos; H11 metafísica. Un límite de uso los detuvo y los retomé. Encargos y datos ({n} registros) en `herramientas/`. Traducciones al español mías.
''')
print('ok')
