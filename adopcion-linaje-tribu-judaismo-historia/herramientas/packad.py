# -*- coding: utf-8 -*-
# Empaqueta el pack «Adopción, linaje y tribu» en el repositorio
import sys, os, shutil, re, glob
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ad')
from PIL import Image
import adspec
from adcards import TAGNAME, SCOPE
AD = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ad'
R = '/home/user/Pruebas/adopcion-linaje-tribu-judaismo-historia'
os.chdir(AD)
for d in ('', '/herramientas', '/herramientas/briefs_agentes', '/herramientas/datos_agentes'):
    os.makedirs(R + d, exist_ok=True)
CARDS = adspec.CARDS
order = ['AD00_es', 'AD00b_es', 'AD00c_es']
for c in CARDS: order += [f'{c["id"]}_or', f'{c["id"]}_es']
order += ['AD99_es']
files = [o + '.png' for o in order]
for f in files:
    assert os.path.exists('adcards/' + f), f
    shutil.copy('adcards/' + f, R + '/' + f)
for t in ['gen.py', 'adverify.py', 'adcheck.py', 'adspec.py', 'adcards.py', 'adstatic.py', 'runad.py', 'showa.py', 'renderhb.js', 'extra_he.json', 'packad.py']:
    shutil.copy(t, R + '/herramientas/' + t)
for i in range(1, 9):
    shutil.copy(f'A{i}.txt', R + f'/herramientas/briefs_agentes/A{i}.txt')
    for n in ('works.json', 'passages.json', 'image.json'):
        if os.path.exists(f'A{i}/{n}'): shutil.copy(f'A{i}/{n}', R + f'/herramientas/datos_agentes/A{i}_{n}')
def pdf(name, w, q):
    ims = []
    for f in files:
        im = Image.open('adcards/' + f).convert('RGB')
        if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        ims.append(im)
    ims[0].save(R + '/' + name, save_all=True, append_images=ims[1:], resolution=120, quality=q)
    return os.path.getsize(R + '/' + name) / 1e6
mb = pdf('adopcion_linaje_tribu_judaismo_historia.pdf', 1200, 72)
print('pdf MB', mb, 'pages', len(files))

def cell(s): return s.replace('|', '\\|').replace('\n', ' ')
out = ["# Adopción, linaje y tribu: lo que dicen el judaísmo y la historia", "",
 "Documentación, en diapositivas, de **34 pruebas** de obras judaicas, de la historia del derecho antiguo y de dos textos cristianos antiguos en las que la adopción, el nombre o la filiación legal asignan familia, nombre, herencia, linaje o tribu. Cada prueba tiene **dos diapositivas**: el **texto original** (hebreo, arameo, griego o latín; en inglés de dominio público cuando no leí el original) con la frase clave resaltada, y la **traducción al español** con «qué demuestra». Es una **selección de textos favorables**: los textos en sentido contrario que encontraron los investigadores están en el apartado «Textos en contra y límites» de este README, no en las diapositivas.", "",
 "**Qué muestran las pruebas.** (1) En Gn 48:5-6 Jacob declara suyos a Efraín y Manasés «como Rubén y Simeón» y la tradición judía (Targumim, Rashi, Midrás Tanjumá) y Josefo lo entienden como contarlos entre los hijos de Jacob, con porción en la tierra o como tribus; Josefo usa la palabra «adopción» (AD01–AD08). (2) El Talmud enuncia que quien cría o enseña al hijo de otro es tenido por la Escritura «como si lo hubiera engendrado» y que los hijos así criados «se llaman por su nombre» (AD10–AD12). (3) El levirato asigna al hijo el nombre y la heredad del muerto (AD16–AD20). (4) En la historia del derecho, la adopción crea familia, nombre y parentesco legal: Hammurabi, Atenas (fratría, demo y «tribu», Iseo) y Roma (Gelio, Justiniano, Suetonio, Tácito) (AD24–AD31). (5) Agustín defiende expresamente que José pudo tener un padre por adopción y cita a Jacob y los hijos de José (AD34); Africano usa el levirato para explicar las genealogías de Jesús (AD33).", "",
 "**Qué no muestran** (ver «Textos en contra y límites»): ninguna prueba reunida muestra que la adopción transmita **la condición davídica, real o sacerdotal**, ni que **cambie de tribu** salvo el caso de Efraín y Manasés, que ya eran nietos de Jacob por sangre; el derecho judío no reconoce formalmente la adopción y los Padres más antiguos sitúan la descendencia davídica de Jesús en María. Por eso estas pruebas apoyan que la adopción atribuía **nombre, familia y herencia**, y dejan abierta la transmisión de la condición davídica por esa vía.", "",
 f"Todo junto en un PDF ({mb:.0f} MB): [`adopcion_linaje_tribu_judaismo_historia.pdf`](adopcion_linaje_tribu_judaismo_historia.pdf). Páginas: AD00 (presentación), AD00b y AD00c (índice de las 34 pruebas), `ADxx_or.png` y `ADxx_es.png` por cada prueba, y AD99 (fuentes, licencias y límites).", "",
 "Colores: amarillo = pasaje citado · naranja = frase clave. Etiquetas de grupo: " + ' · '.join(f'**{v}**' for v in TAGNAME.values()) + ". Etiquetas de alcance: **Texto directo** (el texto mismo habla de un adoptado o hijo legal), **Institución análoga** (levirato, crianza, incorporación) y **Contexto histórico**.", "",
 "## Las 34 pruebas", "", "| Código | Fuente y qué dice | Grupo | Alcance | Obra y fuente leída | Diapositivas |", "|---|---|---|---|---|---|"]
for c in CARDS:
    out.append(f"| {c['id']} | {cell(c['title'])} | {', '.join(TAGNAME[t] for t in c['tags'])} | {SCOPE[c['scope']]} | {cell(c['work'])} ({cell(c['author'])}) · {cell(c['edition'])} · {cell(c['url'])} | [original]({c['id']}_or.png) · [español]({c['id']}_es.png) |")
out += ["", "## Cómo se hizo", "",
 "Un orquestador y **8 investigadores** (modelo pequeño, uno por tema) buscaron las fuentes: A1 Tanaj; A2 comentario judío sobre Gn 48:5 (Rashi, Targumim, Midrás); A3 principio rabínico «como si lo hubiera engendrado»; A4 levirato y Rut; A5 Segundo Templo (Josefo, Filón, Enciclopedia Judía); A6 Oriente Próximo antiguo; A7 derecho griego y romano; A8 NT y Padres sobre José y la ascendencia davídica. Sus encargos están en `herramientas/briefs_agentes/` y lo que devolvieron, en `herramientas/datos_agentes/`. Luego **comprobé yo** con scripts (`herramientas/adverify.py` y `adcheck.py`) que el texto mostrado en cada diapositiva aparece letra por letra (sin vocales ni acentos) en la página de la que procede; el texto griego de Mateo lo leí en el SBLGNT (MorphGNT); los versículos de Nm 13:6, Nm 32:12 y 1 Cr 2:34 los obtuve yo directamente de la API de Sefaria. Las traducciones al español son mías.", "",
 "## Textos en contra y límites", "",
 "Esto es lo que encontraron los investigadores o yo y **no** está en las diapositivas:", "",
 "1. **El derecho judío no reconoce formalmente la adopción.** La *Enciclopedia Judía* (Dembitz y Kohler, 1901-1906) dice que la adrogación romana «es desconocida tanto para el derecho bíblico como para el talmúdico» y que el levirato muestra que la adopción en sentido romano no existía entre los antiguos hebreos; que Gn 48:5 implique adopción legal es una inferencia suya. Una responsa reformista (CCAR, 1978; con derechos de autor, citada solo en fragmento) afirma que los dichos de Sanedrín 19b y Meguilá 13a «no son enunciados halájicos» y que el hijo adoptivo no podría compartir los privilegios del sacerdocio aarónico.",
 "2. **Gn 48 no usa la palabra «adopción» y Efraín y Manasés ya eran nietos de Jacob por sangre** (Gn 41:50-52: hijos de José y Asenat, hija de Potifera, sacerdote de On). Rashi, en Gn 48:6, dice que los hijos que José engendre después no tienen nombre de tribu; Rashbam y Jizkuni los llaman «casas paternas»; el Ramban rechaza la lectura de Rashi; Horayot 6b limita la equiparación «a la herencia y no a otra cosa»; 1 Cr 5:1-2 dice que la primogenitura pasó a los hijos de José «aunque no para ser registrado en la genealogía como primogénito» y que el príncipe viene de Judá.",
 "3. **Levirato.** Mishná Yebamot 4:7, Sifré Deuteronomio 289 (en la traducción de Silverstein) y Rashi en Dt 25:6 dan la porción del muerto al cuñado (el *yavam*), no al hijo; Rut 4:21 y Mt 1:5 dicen que «Booz engendró a Obed»; y Africano hace a José hijo «por naturaleza» de Jacob y «por la ley» de Elí.",
 "4. **Oriente Próximo.** Los §§186, 189 y 190 de Hammurabi permiten deshacer la adopción y devolver al hijo a la casa de su padre, y los §§185-191 no dicen nada de tribu, linaje, ni estatus real o sacerdotal. En Nuzi (Speiser, 1930, texto leído en el OCR de archive.org, que no coteja con la imagen de página) los hijos naturales tenían precedencia sobre los adoptados. Ningún texto de Oriente Próximo leído transmite tribu, realeza o sacerdocio por adopción.",
 "5. **Grecia y Roma.** Las *tribus* romanas eran territoriales y ningún texto leído dice que el adoptado tome la tribu del adoptante (Gelio 5.19.16 menciona tribus pero su sentido no se pudo precisar); Iseo 2.42 y 7.17 son afirmaciones de un litigante, no la enunciación de una regla. Justiniano (Inst. 1.11.2) dice que, en la adopción de un hijo sometido a potestad por un extraño, la potestad del padre natural no se extingue; Iseo 6.44 prohíbe el regreso del adoptado a su familia de origen salvo que deje hijo legítimo; Cicerón (De domo sua 35) argumenta contra la validez de la adopción de Clodio.",
 "6. **Registros y reglas del linaje.** Mishná Kidushín 66b: donde el matrimonio es válido el hijo sigue al varón; Bava Batra 109b: «la familia se llama solo por el lado del padre»; Esd 2:61-62: los sacerdotes que tomaron el nombre de Barzilai por su suegro no pudieron probar su linaje; Nm 36:6-9 prohíbe que la herencia pase de una tribu a otra; Josefo (Contra Apión 1.7 y *Vida* 1) fundamenta el linaje sacerdotal en registros de padres y antepasados.",
 "7. **Jesús, José y David.** Mateo no usa ninguna palabra de adopción para José; Lucas 3:23 dice «como se suponía, hijo de José»; Justino (*Diálogo* 43, 100, 120), Ireneo (*Contra las herejías* III.9.1), Tertuliano (*Contra Marción* IV.1) e Ignacio (*Efesios* 18:2) sitúan la ascendencia davídica en María o no mencionan a José; Ireneo (III.21.9) dice que, si Jesús fuera hijo de José, no podría ser rey ni heredero según Jeremías; Crisóstomo (Hom. Mateo 1.14) señala que se traza la genealogía de José, que no fue padre de Cristo; Jerónimo (*Contra Helvidio* §4) tampoco usa la palabra «adopción». Solo Africano (levirato) y Agustín (adopción) describen explícitamente un padre legal en la genealogía de Jesús, y ambos son exégetas cristianos, no fuentes jurídicas judías.",
 "8. **No leí los originales** de Josefo, Filón, Africano y Eusebio (griego), Agustín (latín) ni Hammurabi (acadio); las citas de esos autores están en traducción inglesa de dominio público. No se halló ninguna fuente que diga que la adopción transmita la condición davídica o la tribu, salvo el caso de Efraín y Manasés y la inferencia de Agustín.",
 "9. **Resultados negativos de los investigadores**: Jubileos 34 y 45 no tratan de la adopción de Efraín y Manasés (solo 44:24-25, nacidos de José); Contra Apión 1.30-36 no trata de genealogías sacerdotales (es 1.7); en los papiros de Elefantina (Cowley) no hallaron contratos de adopción; Éxodo Rabá 1:26 no contiene la línea de «hija de Dios» que sugería el encargo; Filón, *Leyes especiales* III, no trata el levirato.", "",
 "## Licencias y derechos", "",
 "Hebreo bíblico: *Miqra according to the Masorah* (Sefaria, CC BY-SA) y *Tanach with Ta'amei Hamikra* (dominio público); Talmud: Wikisource Talmud Bavli (CC BY-SA; el texto de Vilna es de dominio público); Rashi, Targumim y Midrás Tanjumá: dominio público (Sefaria); traducciones inglesas: JPS 1917, Whiston, King, Moyle, Church y Brodribb, Thomson, McGiffert, Schaff (NPNF) y Etheridge, todas de dominio público; Loeb de 1927 (Iseo, Gelio): de dominio público en EE. UU. desde 2023 por su fecha, aunque las páginas de origen no declaran licencia; SBLGNT: © Society of Biblical Literature y Faithlife, CC BY 4.0. El Código de Hammurabi se cita por la traducción de King (1910) del Avalon Project (la página lleva un aviso de copyright de 2008 de la biblioteca, sin licencia para la traducción). Fechas de obras y autores: aproximadas, convencionales.", "",
 "Herramientas en `herramientas/`: `gen.py` (genera los encargos), `adverify.py` y `adcheck.py` (comprobación de citas), `adspec.py` (datos de las 34 pruebas), `adcards.py` y `adstatic.py` (generan las diapositivas) y `renderhb.js` (las convierte en PNG)."]
open(R + '/README.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(files), 'diapositivas')
