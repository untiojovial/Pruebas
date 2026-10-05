# -*- coding: utf-8 -*-
# Tarjetas del Vídeo 2 (Umar). [[k:...]] naranja = frase clave; [[a:...]] azul = matiz o lo que juega en contra.
# Campos: cap (n.º de captura en la tabla del Vídeo 2), bloque, specs (capturas que se juntan), es (una entrada por segmento).
from cards_data import CARDS as IH
from hcards_data import HCARDS as HC

ih = {c['id']: c for c in IH}
hc = {c['id']: c for c in HC}
HU = "hadithunlocked.com"
KSU = "quran.ksu.edu.sa (Universidad Rey Saúd)"

VCARDS = [
 dict(id="U05", cap="5", bloque="bloque 1", specs=["IH14"],
  title=ih['IH14']['title'], ref=ih['IH14']['ref'], ar_ref=ih['IH14']['ar_ref'], site=ih['IH14']['site'], url=ih['IH14']['url'],
  es=ih['IH14']['es'], prueba=ih['IH14']['prueba'], ojo="Es la misma captura que IH14 de la serie de Ibn Hajar."),

 dict(id="U06", cap="6", bloque="bloque 3", specs=["H18"],
  title=hc['H18']['title'], ref=hc['H18']['ref'], ar_ref=hc['H18']['ar_ref'], site=hc['H18']['site'], url=hc['H18']['url'],
  es=hc['H18']['es'], prueba="Ibn Kathir, el autor que cita Tibyanan, dice que las traducciones al árabe que circulaban estaban llenas de errores, añadidos y supresiones. Lo que Umar llevó era una copia en árabe.",
  ojo="Ibn Kathir también cree que los ejemplares de su época tenían cambios; muestra la frase entera (es H18 de la serie de Historia)."),

 dict(id="U07", cap="7", bloque="bloque 4", specs=["U07a","U07b"],
  title="«No creáis a la Gente del Libro ni la desmintáis»",
  ref="Sahih al-Bujari 4485 (Tafsir) y 7542 (Tawhid)", ar_ref="صحيح البخاري ٤٤٨٥ و٧٥٤٢", site=HU, url="https://hadithunlocked.com/bukhari:4485",
  es=["La Gente del Libro [[k:leía la Torá en hebreo y la explicaba en árabe a los musulmanes]]. Y el Mensajero de Dios ﷺ dijo: «[[k:No creáis a la Gente del Libro ni la desmintáis]], y decid: “Creemos en Dios y en lo que se nos ha revelado…”» (2:136). [Bujari 4485]",
      "La Gente del Libro [[k:leía la Torá en hebreo y la explicaba en árabe a los musulmanes]]. Y el Mensajero de Dios ﷺ dijo: «[[k:No creáis a la Gente del Libro ni la desmintáis]], y decid: “Creemos en Dios y en lo que se nos ha revelado…”» (3:84). [Bujari 7542]"],
  prueba="Lo que llegaba a los musulmanes era una explicación oral en árabe de un texto hebreo. Ante eso, el Profeta manda no creer ni desmentir: lo contrario de «es falso». Es el mismo criterio que «desmentiréis una verdad» en el hadiz de Umar.",
  ojo="Página de 7542: https://hadithunlocked.com/bukhari:7542"),

 dict(id="U09a", cap="9", bloque="bloque 7", specs=["U09a"],
  title="«Transmitid de los hijos de Israel, no hay problema»",
  ref="Sahih al-Bujari 3461", ar_ref="صحيح البخاري ٣٤٦١", site=HU, url="https://hadithunlocked.com/bukhari:3461",
  es=["[El Profeta ﷺ dijo:] «Transmitid de mí aunque sea un versículo; [[k:y transmitid de los hijos de Israel, no hay problema]]; y quien mienta sobre mí a sabiendas, que ocupe su asiento en el Fuego»."],
  prueba="El Profeta permite transmitir lo que cuentan los hijos de Israel; no tendría sentido si todo lo que tenían fuera falso.",
  ojo="Los comentaristas lo entienden sobre todo de relatos de los israelitas, no de un texto concreto de la Torá: úsalo como apoyo, no como prueba principal."),

 dict(id="U09b", cap="9", bloque="bloque 7", specs=["U09b"],
  title="Pide la Torá, la pone sobre el cojín y dice: «Creo en ti y en Quien te reveló»",
  ref="Sunan Abi Dawud 4449, con las calificaciones que recoge la página", ar_ref="سنن أبي داود ٤٤٤٩", site=HU, url="https://hadithunlocked.com/abudawud:4449",
  es=["Vino un grupo de judíos e invitaron al Mensajero de Dios ﷺ a al-Quff; fue a verlos a la casa de estudio (midrás) y dijeron: «Abu al-Qasim, un hombre de los nuestros ha fornicado con una mujer: juzga entre ellos». Pusieron al Mensajero de Dios ﷺ un cojín y se sentó en él. Luego dijo: «[[k:Traedme la Torá]]». Se la trajeron, [[k:quitó el cojín de debajo de él, puso la Torá encima y dijo: «Creo en ti y en Quien te reveló»]]. Luego dijo: «Traedme al más sabio de vosotros», y le trajeron a un joven. Y luego menciona la historia de la lapidación, como el hadiz de Malik de Nafiʿ.",
      "[[k:Bueno (ḥasan): al-Albani]] · [[k:auténtico y firme: al-Zaylaʿi]] · [[a:débil con esta redacción: Shuʿayb al-Arnaʾut]]"],
  prueba="Según este relato, el Profeta pidió la Torá que tenían en Medina, la puso en alto y dijo «creo en ti y en Quien te reveló».",
  ojo="Las calificaciones no coinciden (en azul): al-Arnaʾut la considera débil con esta redacción. En el guion di «hasan según al-Albani» y no la presentes como indiscutible. El núcleo de la lapidación sí está en Bujari (U09c) y Muslim (U09d)."),

 dict(id="U09c", cap="9", bloque="bloque 7", specs=["U09c"],
  title="El versículo de la lapidación estaba en la Torá: «uno puso la mano encima»",
  ref="Sahih al-Bujari 3635", ar_ref="صحيح البخاري ٣٦٣٥", site=HU, url="https://hadithunlocked.com/bukhari:3635",
  es=["Los judíos vinieron al Mensajero de Dios ﷺ y le contaron que un hombre y una mujer de entre ellos habían fornicado. El Mensajero de Dios ﷺ les dijo: «¿Qué encontráis en la Torá sobre la lapidación?». Dijeron: «Los exponemos a la vergüenza y son azotados». ʿAbdallah ibn Salam dijo: «Mentís: en ella está la lapidación». Trajeron la Torá y la abrieron, [[k:y uno de ellos puso la mano sobre el versículo de la lapidación]] y leyó lo que había antes y después. ʿAbdallah ibn Salam le dijo: «Levanta la mano». La levantó, [[k:y allí estaba el versículo de la lapidación]]. Dijeron: «Ha dicho la verdad, Muhammad: en ella está el versículo de la lapidación». El Mensajero de Dios ﷺ ordenó que fueran lapidados. Dijo ʿAbdallah [ibn ʿUmar]: «Vi al hombre inclinarse sobre la mujer para protegerla de las piedras»."],
  prueba="El versículo estaba en la Torá que trajeron: lo taparon con la mano, no lo habían borrado."),

 dict(id="U09d", cap="9", bloque="bloque 7", specs=["U09d"],
  title="Un sabio judío lo admite: «encontramos la lapidación, pero se extendió entre nuestros nobles»",
  ref="Sahih Muslim 1700", ar_ref="صحيح مسلم ١٧٠٠", site=HU, url="https://hadithunlocked.com/muslim:1700",
  es=["Pasaron junto al Profeta ﷺ con un judío ennegrecido [con carbón] y azotado. Los llamó y dijo: «¿Así encontráis el castigo del fornicador en vuestro Libro?». Dijeron: «Sí». Llamó a uno de sus sabios y dijo: «Te conjuro por Dios, que reveló la Torá a Moisés: ¿así encontráis el castigo del fornicador en vuestro Libro?». Dijo: «No; y si no me hubieras conjurado así, no te lo habría dicho. [[k:Encontramos la lapidación, pero [el delito] se extendió entre nuestros nobles]]: cuando cogíamos a un noble lo dejábamos, y cuando cogíamos a un débil le aplicábamos el castigo. Dijimos: “Pongámonos de acuerdo en algo que apliquemos al noble y al humilde”, [[k:y pusimos el ennegrecimiento y los azotes en lugar de la lapidación]]»."],
  prueba="Lo admite un sabio judío ante el Profeta: el texto decía lapidación; lo que cambiaron fue la práctica, no el Libro."),

 dict(id="U10a", cap="10", bloque="bloque 8", specs=["H01"],
  title=hc['H01']['title'], ref=hc['H01']['ref'], ar_ref=hc['H01']['ar_ref'], site=hc['H01']['site'], url=hc['H01']['url'],
  es=hc['H01']['es'], prueba=hc['H01']['prueba'], ojo=hc['H01']['ojo']),

 dict(id="U10b", cap="10", bloque="bloque 8", specs=["U10a"],
  title="Las otras vías: «he venido a escucharos», «cada vez que entraba, los escuchaba», «lo encontramos escrito»",
  ref="al-Tabari, Tafsir, sobre el Corán 2:97, n.º 1610 (Qatada), 1613 (al-Suddi) y 1614 (Mujalid, de al-Shaʿbi)", ar_ref="تفسير الطبري، البقرة ٩٧، رقم ١٦١٠ و١٦١٣ و١٦١٤", site=KSU, url="https://quran.ksu.edu.sa/tafseer/tabary/sura2-aya97.html",
  es=["1610 — Nos contó Bishr ibn Muʿadh: nos contó Yazid ibn Zurayʿ: nos contó Saʿid, de Qatada, que dijo: Se nos ha contado que Umar ibn al-Jattab fue un día a ver a los judíos; cuando lo vieron, le dieron la bienvenida. Umar les dijo: «Por Dios, no he venido por amor a vosotros ni por interés en vosotros, [[k:sino que he venido a escucharos]]». Les preguntó y le preguntaron, y dijeron:…",
      "1613 — Me contó Musa ibn Harun: nos contó ʿAmr ibn Hammad: nos contó Asbat, de al-Suddi, sobre «Di: quien sea enemigo de Gabriel… Él lo hizo descender sobre tu corazón con permiso de Dios, confirmando lo que había antes»: dijo: Umar ibn al-Jattab tenía una tierra en la parte alta de Medina e iba a ella; su camino pasaba por la casa de estudio de los judíos, [[k:y cada vez que entraba con ellos, los escuchaba]]. Un día entró y le dijeron: «Umar, no hay entre los compañeros de Muhammad ﷺ nadie a quien queramos más que a ti: ellos pasan junto a nosotros y nos molestan, y tú pasas y no nos molestas; tenemos esperanzas contigo». Umar les dijo: «¿Cuál es vuestro juramento más grande?». Dijeron: «El Misericordioso, que reveló la Torá a Moisés en el monte Sinaí». Les dijo Umar: «Os conjuro por el Misericordioso, que reveló la Torá a Moisés en el monte Sinaí: ¿encontráis a Muhammad ﷺ entre vosotros?». Se callaron. Dijo: «Hablad, ¿qué os pasa? Por Dios, no os lo pregunto porque dude de nada de mi religión». Se miraron unos a otros, y se levantó uno de ellos y dijo: «Decídselo al hombre, o se lo digo yo». Dijeron: «Sí, [[k:lo encontramos escrito entre nosotros]]; pero…",
      "1614 — Me contó al-Muthanna: nos contó Ishaq ibn al-Hajjaj al-Razi: nos contó ʿAbd al-Rahman ibn Maghraʾ Abu Zuhayr, [[k:de Mujalid, de al-Shaʿbi]], que dijo: Umar fue a los judíos y dijo: «Os conjuro por Quien reveló la Torá a Moisés: ¿encontráis a Muhammad en vuestro Libro?». [[k:Dijeron: «Sí»]]. Dijo: «¿Y qué os impide seguirle?»…"],
  prueba="Las otras vías del relato de Umar en la escuela judía: Qatada («he venido a escucharos»), al-Suddi («cada vez que entraba, los escuchaba» y «lo encontramos escrito entre nosotros») y Mujalid, de al-Shaʿbi.",
  ojo="Ninguna llega conectada a Umar: Qatada dice «se nos ha contado», y al-Suddi y al-Shaʿbi no lo conocieron. La de Mujalid pasa por un transmisor débil."),

 dict(id="U10c", cap="10", bloque="bloque 8", specs=["U10b"],
  title="La vía de Ibn Abi Layla: el versículo «se reveló tal como lo dijo Umar»",
  ref="al-Tabari, Tafsir, sobre el Corán 2:98, n.º 1635", ar_ref="تفسير الطبري، البقرة ٩٨، رقم ١٦٣٥", site=KSU, url="https://quran.ksu.edu.sa/tafseer/tabary/sura2-aya98.html",
  es=["1635 — Se me contó de ʿAmmar: nos contó Ibn Abi Jaʿfar, de su padre, de Husayn ibn ʿAbd al-Rahman, [[k:de ʿAbd al-Rahman ibn Abi Layla]], que dijo: Un judío encontró a Umar y le dijo: «Ese Gabriel del que habla tu compañero es enemigo nuestro». Umar le dijo: «Quien sea enemigo de Dios, de Sus ángeles, de Sus mensajeros, de Gabriel y de Miguel… Dios es enemigo de los incrédulos». Dijo: [[k:y se reveló [el versículo] tal como lo dijo Umar]]."],
  prueba="La vía de Ibn Abi Layla trae el encuentro de Umar con los judíos y el versículo de Gabriel, sin el detalle de la escuela.",
  ojo="La cadena empieza con «se me contó» (sin nombre) y se discute si Ibn Abi Layla oyó a Umar (IH17)."),

 dict(id="U11", cap="11", bloque="bloque 8", specs=["IH16"],
  title=ih['IH16']['title'], ref=ih['IH16']['ref'], ar_ref=ih['IH16']['ar_ref'], site=ih['IH16']['site'], url=ih['IH16']['url'],
  es=ih['IH16']['es'], prueba=ih['IH16']['prueba'], ojo=ih['IH16']['ojo']),
]

from vcards_extra import EXTRA
_order = ['U01','U02','U03a','U03b','U04','U05','U06','U07','U08','U09a','U09b','U09c','U09d','U10a','U10b','U10c','U11','U12','U13']
VCARDS = sorted(VCARDS + EXTRA, key=lambda c: _order.index(c['id']))

def _finish(cards):
    for c in cards:
        c.setdefault('tag', f"Vídeo 2 · captura {c['cap']} · {c['bloque']}")
        c.setdefault('uso', f"Vídeo 2 (Umar) · captura {c['cap']} ({c['bloque']})")
        c.setdefault('ojo', None)
        if c['ojo'] is None: c.pop('ojo')
_finish(VCARDS)
