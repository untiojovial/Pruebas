# -*- coding: utf-8 -*-
# Guion para el formato «papel recortado»: un solo narrador.
# Cada segmento: (tipo, texto, fuente). tipo 'N' = narración, 'Q' = cita leída (sale en tarjeta).
# *palabra* = palabra clave (roja en el subtítulo, marcada en amarillo en la tarjeta). Los asteriscos no se leen.
VOICE = ('es-ES-AlvaroNeural', '+3%', '-26Hz')
G = 'IBN ISHAQ · SIRA (TRAD. GUILLAUME 1955), '
SCENES = [
 dict(id='hook', segs=[
  ('N', '«Mahoma solo luchó en *defensa* *propia*. Nunca atacó a nadie primero». Eso te dirán.', ''),
  ('N', "En el vídeo anterior vimos qué pasó con los poetas que lo criticaron: Ka'b ibn al-Ashraf, Asma bint Marwán y Abu Afak. Hoy seguimos con las *guerras*.", 'BUJARI 4037 · ' + G + 'PP. 675-676'),
  ('N', 'Y solo con fuentes *musulmanas*: el Corán, los grandes comentarios del Corán, los hadices de Bujari y Muslim, y la biografía más antigua, la de Ibn Ishaq. Con las páginas en pantalla.', 'CORÁN · TAFSIR · BUJARI · MUSLIM · IBN ISHAQ'),
 ]),
 dict(id='medina', segs=[
  ('N', 'Año seiscientos veintidós. Mahoma y los suyos emigran de La Meca a Medina. Hay que decirlo: en La Meca habían sufrido *persecución*, y perdieron sus casas.', G + 'PP. 213-231'),
  ('N', 'Pero, según Ibn Ishaq, en pocos meses empiezan a salir expediciones contra las *caravanas* de los comerciantes de La Meca. Varias no llegaron a combatir. Pero el objetivo era siempre la caravana.', G + 'PP. 281-287'),
 ]),
 dict(id='nakhla', segs=[
  ('N', 'La primera sangre llega en Najla, entre La Meca y Taif. Mahoma envía un grupo con una carta sellada: «Id a Najla y *acechad* allí a Quraysh».', G + 'P. 287'),
  ('Q', 'Si los matáis, los mataréis en el mes sagrado. Y dudaron. Luego se animaron unos a otros, y decidieron *matar* a cuantos pudieran, y quedarse con lo que llevaban.', G + 'P. 287'),
  ('N', 'Era el mes sagrado, cuando los árabes no hacían la guerra. Mahoma primero lo desaprueba. Pero luego baja el versículo dos, doscientos diecisiete: luchar en el mes sagrado es grave, pero la persecución es peor que matar. Y Mahoma toma la *caravana*.', G + 'PP. 287-288 · CORÁN 2:217'),
 ]),
 dict(id='badr', segs=[
  ('N', 'Y llega Badr, la batalla más famosa. ¿Empezó porque La Meca atacara Medina? Ibn Ishaq cuenta que Mahoma supo que Abu Sufyán volvía de Siria con una gran caravana, y dijo:', G + 'P. 289'),
  ('Q', 'Esta es la caravana de Quraysh, que lleva sus bienes. Salid contra ella. Quizá Dios os la dé como *botín*.', G + 'P. 289'),
  ('N', 'Los de La Meca salieron a proteger su caravana. La batalla vino *después*.', G + 'PP. 289-296'),
 ]),
 dict(id='kab', segs=[
  ('N', 'Después de Badr llegan los críticos, como en el vídeo anterior. Bujari, cuatro mil treinta y siete:', 'SAHIH AL-BUJARI 4037'),
  ('Q', "¿Quién *matará* a Ka'b ibn al-Ashraf, que ha ofendido a Dios y a su mensajero? Muhammad ibn Maslama dijo: ¿quieres que lo mate? Dijo: sí. Entonces permíteme decir algo para *engañarlo*.", 'SAHIH AL-BUJARI 4037 (TRAD. MUHSIN KHAN)'),
  ('N', 'Y según Ibn Ishaq, a la mañana siguiente el Profeta dijo: «*Matad* a cualquier judío que caiga en vuestro poder».', G + 'P. 369'),
  ('N', 'Y al conquistar La Meca, unos pocos quedaron excluidos del perdón: debían *morir* aunque los encontraran bajo las cortinas de la Kaaba.', G + 'PP. 550-551'),
 ]),
 dict(id='mustaliq', segs=[
  ('N', 'Bujari, dos mil quinientos cuarenta y uno. La tribu de Banu al-Mustaliq.', 'SAHIH AL-BUJARI 2541'),
  ('Q', 'El Profeta atacó de repente a Banu al-Mustaliq, *sin* *aviso*, mientras estaban desprevenidos y su ganado bebía en el agua. Sus combatientes fueron muertos, y sus mujeres y niños tomados *cautivos*.', 'SAHIH AL-BUJARI 2541 (TRAD. MUHSIN KHAN)'),
  ('N', 'Ibn Ishaq da un motivo: le llegó la noticia de que se estaban reuniendo contra él. Aun así, el ataque fue por *sorpresa*, junto al agua. Y en Muslim, el narrador añade algo revelador: invitar al islam antes de atacar era cosa de los primeros tiempos.', G + 'P. 490 · SAHIH MUSLIM 1730'),
 ]),
 dict(id='qurayza', segs=[
  ('N', 'Banu Qurayza, una tribu judía de Medina. Las fuentes musulmanas la acusan de traición durante el asedio de la Trinchera. Concedámoslo. ¿Cuál fue la *sentencia*?', G + 'PP. 461-464'),
  ('Q', 'Que los hombres sean *muertos*, los bienes repartidos, y las mujeres y los niños tomados cautivos.', G + 'P. 464'),
  ('N', 'Ibn Ishaq dice que cavaron zanjas en el mercado de Medina, y los *decapitaron* por grupos. Seiscientos o setecientos. Algunos dicen ochocientos o novecientos.', G + 'P. 464'),
 ]),
 dict(id='khaybar', segs=[
  ('N', 'Jaybar, un oasis judío a ciento cincuenta kilómetros al norte de Medina. No estaba sitiando Medina. Ibn Ishaq describe el método:', G + 'PP. 510-511'),
  ('Q', 'Cuando el apóstol atacaba a un pueblo, esperaba a la mañana. Si oía la llamada a la oración, se detenía. Si no la oía, *atacaba*.', G + 'P. 511'),
  ('N', 'El criterio para atacar no era si te habían atacado, sino si eran *musulmanes*. Y al ver Jaybar, gritó: «Dios es grande, Jaybar está *destruida*».', G + 'P. 511'),
 ]),
 dict(id='tabuk', segs=[
  ('N', 'Año nueve de la Hégira. Tabuk. Mahoma reúne un ejército de treinta mil contra los bizantinos, a unos setecientos kilómetros de Medina. Y el Corán, nueve, veintinueve, dice:', G + 'P. 602 · TAFSIR IBN KATHIR, VOL. 4'),
  ('Q', '*Combatid* a quienes no creen en Dios ni en el Último Día, de entre los que recibieron la Escritura, hasta que paguen el *tributo* de su mano, y humillados.', 'CORÁN 9:29'),
  ('N', 'Ibn Kathir, el comentario del Corán más leído, explica: este versículo bajó con la orden de combatir a *judíos* y *cristianos*. Y Mahoma preparó su ejército para combatir a los romanos.', 'TAFSIR IBN KATHIR (DARUSSALAM), VOL. 4 · SOBRE 9:29'),
 ]),
 dict(id='hadith', segs=[
  ('N', 'Y no es solo historia. Es *doctrina*. Bujari, veinticinco:', 'SAHIH AL-BUJARI 25'),
  ('Q', 'Se me ha ordenado *combatir* a la gente, hasta que atestigüen que no hay más dios que Dios, y que Mahoma es el mensajero de Dios.', 'SAHIH AL-BUJARI 25 (TRAD. MUHSIN KHAN)'),
  ('N', 'Y Muslim, mil setecientos treinta y uno, las instrucciones a los ejércitos: cuando encuentres a tus enemigos, invítalos al islam. Si se niegan, exígeles el *tributo*. Si se niegan, pide ayuda a Dios, y *combátelos*.', 'SAHIH MUSLIM 1731'),
  ('N', 'Fíjate en el orden: el combate no depende de que te ataquen. Depende de que acepten el islam, o el tributo.', 'SAHIH MUSLIM 1731'),
 ]),
 dict(id='sword', segs=[
  ('N', 'Corán, nueve, cinco: «*Matad* a los politeístas dondequiera que los encontréis». Ibn Kathir lo llama el versículo de la *espada*, y cita que abrogó todo pacto de paz.', 'CORÁN 9:5 · TAFSIR IBN KATHIR, VOL. 4'),
  ('N', 'Y explica: no esperes a encontrarlos. Búscalos y sítialos en sus fortalezas, para que no les quede más opción que *morir* o abrazar el islam.', 'TAFSIR IBN KATHIR (DARUSSALAM), VOL. 4 · SOBRE 9:5'),
  ('N', 'Al-Qurtubi va más lejos. Sobre el versículo dos, ciento noventa y tres, escribe: es una orden de combatir sin la condición de que empiecen los incrédulos. La causa del combate es la *incredulidad*.', "AL-QURTUBI · AL-YAMI' LI-AHKAM AL-QUR'AN, SOBRE 2:193"),
 ]),
 dict(id='fiqh', segs=[
  ('N', 'Y así lo resumen los manuales clásicos de derecho. El manual shafií Reliance of the Traveller dice:', 'RELIANCE OF THE TRAVELLER, O9.8'),
  ('Q', 'El califa hace la *guerra* a judíos, cristianos y zoroastrianos, hasta que se hagan musulmanes o paguen el tributo. Y combate a todos los demás pueblos, hasta que se hagan musulmanes.', 'RELIANCE OF THE TRAVELLER, O9.8-O9.9'),
  ('N', 'Ibn Qudama, hanbalí: la yihad, como mínimo, una vez al año. Ibn Rushd: los juristas están de acuerdo en que se combate a todos los *politeístas*.', 'IBN QUDAMA, AL-MUGHNI · IBN RUSHD, BIDAYAT AL-MUYTAHID'),
 ]),
 dict(id='counter', segs=[
  ('N', 'Te responderán: «Pero el Corán dice: combatid a los que os combaten, y no os excedáis. Y se les permitió luchar porque habían sido *oprimidos*».', 'CORÁN 2:190 · 22:39'),
  ('N', 'Es verdad, y hay que reconocerlo. Dos, ciento noventa, y veintidós, treinta y nueve, hablan de *defensa*. Y el propio Ibn Kathir prohíbe matar a mujeres, niños, ancianos y monjes.', 'CORÁN 2:190 · 22:39 · TAFSIR IBN KATHIR SOBRE 2:190'),
  ('N', 'Pero algunos comentaristas clásicos dicen que eso fue solo el principio, y que quedó superado. Ibn Kathir no lo cree así. Pero él mismo llama al nueve, cinco, el versículo de la *espada*, y explica el nueve, veintinueve, como orden de combatir a judíos y cristianos. Y la práctica de Mahoma, en Najla, Badr, Mustaliq, Jaybar y Tabuk, no fue solo defensa.', 'TAFSIR IBN KATHIR SOBRE 2:190, 9:5 Y 9:29'),
  ('N', 'Hasta el historiador W. Montgomery Watt, nada hostil al islam, lo escribió en mil novecientos cincuenta y seis: el juramento hablaba solo de defensa, pero las primeras expediciones fueron *ofensivas*, para emboscar caravanas de La Meca. Incluso Badr fue una *razia*.', 'W. M. WATT · MUHAMMAD AT MEDINA (OXFORD 1956), P. 231'),
  ('N', "Ibn Sa'd cuenta veintisiete expediciones dirigidas por él, y cuarenta y siete enviadas. ¿Todas en *defensa* *propia*?", "IBN SA'D · TABAQAT, VOL. 2"),
 ]),
 dict(id='jesus', segs=[
  ('N', 'Compáralo con Jesús. Cuando Pedro sacó la espada para defenderlo, le dijo:', 'MATEO 26:51-52'),
  ('Q', 'Vuelve tu *espada* a su sitio, porque todos los que tomen espada, a espada perecerán.', 'MATEO 26:52'),
  ('N', 'Y ante Pilato: «Mi reino no es de este mundo. Si lo fuera, mis servidores pelearían». Y cuando sus discípulos quisieron hacer bajar fuego sobre una aldea que lo rechazó, los reprendió: el Hijo del Hombre no ha venido a destruir vidas, sino a *salvarlas*.', 'JUAN 18:36 · LUCAS 9:54-56'),
 ]),
 dict(id='end', segs=[
  ('N', 'Resumen. Uno: las primeras expediciones iban contra *caravanas*. Dos: hubo ataques por *sorpresa*, como Banu al-Mustaliq y Jaybar.', ''),
  ('N', 'Tres: el Corán y los hadices mandan combatir hasta el islam o el *tributo*. Cuatro: los comentaristas y los juristas clásicos lo entendieron así.', ''),
  ('N', 'Esto no va contra los musulmanes, a quienes respetamos. Va de lo que dicen sus propias fuentes. Así que la pregunta es una sola: ¿de verdad fue todo en *defensa* *propia*? Comenta tu postura. Y si quieres las fuentes con sus páginas, pídelas en comentarios.', ''),
 ]),
]
def clean(t): return t.replace('*', '')
