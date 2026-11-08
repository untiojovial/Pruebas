# -*- coding: utf-8 -*-
# Guion: N = narrador, D = defensor (objeción), F = fuente leída (cita de las fuentes islámicas o bíblicas)
VOICES = {'N': ('es-ES-AlvaroNeural', '+12%', '+0Hz'), 'D': ('es-MX-JorgeNeural', '+8%', '+0Hz'), 'F': ('es-CO-GonzaloNeural', '-2%', '-4Hz')}
SCENES = [
 dict(id='hook', title='¿Solo luchó en defensa propia?', vis='hook', segs=[
  ('D', 'Mahoma solo luchó en defensa propia. Nunca atacó a nadie primero.'),
  ('N', 'En el vídeo anterior vimos qué pasó con los poetas que lo criticaron: Ka\'b ibn al-Ashraf, Asma bint Marwán y Abu Afak. Hoy seguimos con las guerras.'),
  ('N', 'Y solo con fuentes musulmanas: el Corán, los grandes comentarios del Corán, los hadices de Bujari y Muslim, y la biografía más antigua, la de Ibn Ishaq. Con las páginas en pantalla.'),
 ]),
 dict(id='medina', title='Medina, año 622', vis='medina', segs=[
  ('N', 'Año seiscientos veintidós. Mahoma y los suyos emigran de La Meca a Medina. Hay que decirlo: en La Meca habían sufrido persecución, y perdieron sus casas.'),
  ('N', 'Pero, según Ibn Ishaq, en pocos meses empiezan a salir expediciones contra las caravanas de los comerciantes de La Meca. Varias no llegaron a combatir. Pero el objetivo era siempre la caravana.'),
 ]),
 dict(id='nakhla', title='La caravana de Najla', vis='nakhla', segs=[
  ('N', 'La primera sangre llega en Najla, entre La Meca y Taif. Mahoma envía un grupo con una carta sellada: id a Najla y acechad allí a Quraysh.'),
  ('F', 'Si los matáis, los mataréis en el mes sagrado. Y dudaron. Luego se animaron unos a otros, y decidieron matar a cuantos pudieran, y quedarse con lo que llevaban.'),
  ('N', 'Era el mes sagrado, cuando los árabes no hacían la guerra. Mahoma primero lo desaprueba. Pero luego baja el versículo dos, doscientos diecisiete: luchar en el mes sagrado es grave, pero la persecución es peor que matar. Y Mahoma toma la caravana.'),
 ]),
 dict(id='badr', title='Badr empezó por una caravana', vis='badr', segs=[
  ('N', 'Y llega Badr, la batalla más famosa. ¿Empezó porque La Meca atacara Medina? Ibn Ishaq cuenta que Mahoma supo que Abu Sufyán volvía de Siria con una gran caravana, y dijo:'),
  ('F', 'Esta es la caravana de Quraysh, que lleva sus bienes. Salid contra ella. Quizá Dios os la dé como botín.'),
  ('N', 'Los de La Meca salieron a proteger su caravana. La batalla vino después.'),
 ]),
 dict(id='kab', title='Los críticos, otra vez', vis='kab', segs=[
  ('N', 'Después de Badr llegan los críticos, como en el vídeo anterior. Bujari, cuatro mil treinta y siete:'),
  ('F', '¿Quién matará a Ka\'b ibn al-Ashraf, que ha ofendido a Dios y a su mensajero? Muhammad ibn Maslama dijo: ¿quieres que lo mate? Dijo: sí. Entonces permíteme decir algo para engañarlo.'),
  ('N', 'Y según Ibn Ishaq, a la mañana siguiente el Profeta dijo: matad a cualquier judío que caiga en vuestro poder.'),
  ('N', 'Y al conquistar La Meca, unos pocos quedaron excluidos del perdón: debían morir aunque los encontraran bajo las cortinas de la Kaaba.'),
 ]),
 dict(id='mustaliq', title='Banu al-Mustaliq: sin aviso', vis='mustaliq', segs=[
  ('N', 'Bujari, dos mil quinientos cuarenta y uno. La tribu de Banu al-Mustaliq.'),
  ('F', 'El Profeta atacó de repente a Banu al-Mustaliq, sin aviso, mientras estaban desprevenidos y su ganado bebía en el agua. Sus combatientes fueron muertos, y sus mujeres y niños tomados cautivos.'),
  ('N', 'Ibn Ishaq da un motivo: le llegó la noticia de que se estaban reuniendo contra él. Aun así, el ataque fue por sorpresa, junto al agua. Y en Muslim, el narrador añade algo revelador: invitar al islam antes de atacar era cosa de los primeros tiempos.'),
 ]),
 dict(id='qurayza', title='Banu Qurayza', vis='qurayza', segs=[
  ('N', 'Banu Qurayza, una tribu judía de Medina. Las fuentes musulmanas la acusan de traición durante el asedio de la Trinchera. Concedámoslo. ¿Cuál fue la sentencia?'),
  ('F', 'Que los hombres sean muertos, los bienes repartidos, y las mujeres y los niños tomados cautivos.'),
  ('N', 'Ibn Ishaq dice que cavaron zanjas en el mercado de Medina, y los decapitaron por grupos. Seiscientos o setecientos. Algunos dicen ochocientos o novecientos.'),
 ]),
 dict(id='khaybar', title='Jaybar: el criterio', vis='khaybar', segs=[
  ('N', 'Jaybar, un oasis judío a ciento cincuenta kilómetros al norte de Medina. No estaba sitiando Medina. Ibn Ishaq describe el método:'),
  ('F', 'Cuando el apóstol atacaba a un pueblo, esperaba a la mañana. Si oía la llamada a la oración, se detenía. Si no la oía, atacaba.'),
  ('N', 'El criterio para atacar no era si te habían atacado, sino si eran musulmanes. Y al ver Jaybar, gritó: Dios es grande, Jaybar está destruida.'),
 ]),
 dict(id='tabuk', title='Contra Bizancio', vis='tabuk', segs=[
  ('N', 'Año nueve de la Hégira. Tabuk. Mahoma reúne un ejército de treinta mil contra los bizantinos, a unos setecientos kilómetros de Medina. Y el Corán, nueve, veintinueve, dice:'),
  ('F', 'Combatid a quienes no creen en Dios ni en el Último Día, de entre los que recibieron la Escritura, hasta que paguen el tributo de su mano, y humillados.'),
  ('N', 'Ibn Kathir, el comentario del Corán más leído, explica: este versículo bajó con la orden de combatir a judíos y cristianos. Y Mahoma preparó su ejército para combatir a los romanos.'),
 ]),
 dict(id='hadith', title='No es solo historia: es doctrina', vis='hadith', segs=[
  ('N', 'Y no es solo historia. Es doctrina. Bujari, veinticinco:'),
  ('F', 'Se me ha ordenado combatir a la gente, hasta que atestigüen que no hay más dios que Dios, y que Mahoma es el mensajero de Dios.'),
  ('N', 'Y Muslim, mil setecientos treinta y uno, las instrucciones a los ejércitos: cuando encuentres a tus enemigos, invítalos al islam. Si se niegan, exígeles el tributo. Si se niegan, pide ayuda a Dios, y combátelos.'),
  ('N', 'Fíjate en el orden: el combate no depende de que te ataquen. Depende de que acepten el islam, o el tributo.'),
 ]),
 dict(id='sword', title='El versículo de la espada', vis='sword', segs=[
  ('N', 'Corán, nueve, cinco: matad a los politeístas dondequiera que los encontréis. Ibn Kathir lo llama el versículo de la espada, y cita que abrogó todo pacto de paz.'),
  ('N', 'Y explica: no esperes a encontrarlos. Búscalos y sítialos en sus fortalezas, para que no les quede más opción que morir o abrazar el islam.'),
  ('N', 'Al-Qurtubi va más lejos. Sobre el versículo dos, ciento noventa y tres, escribe: es una orden de combatir sin la condición de que empiecen los incrédulos. La causa del combate es la incredulidad.'),
 ]),
 dict(id='fiqh', title='El derecho islámico clásico', vis='fiqh', segs=[
  ('N', 'Y así lo resumen los manuales clásicos de derecho. El manual shafií Reliance of the Traveller dice:'),
  ('F', 'El califa hace la guerra a judíos, cristianos y zoroastrianos, hasta que se hagan musulmanes o paguen el tributo. Y combate a todos los demás pueblos, hasta que se hagan musulmanes.'),
  ('N', 'Ibn Qudama, hanbalí: la yihad, como mínimo, una vez al año. Ibn Rushd: los juristas están de acuerdo en que se combate a todos los politeístas.'),
 ]),
 dict(id='counter', title='«Pero el Corán dice…»', vis='counter', segs=[
  ('D', '¡Pero el Corán dice: combatid a los que os combaten, y no os excedáis! ¡Y se les permitió luchar porque habían sido oprimidos!'),
  ('N', 'Es verdad, y hay que reconocerlo. Dos, ciento noventa, y veintidós, treinta y nueve, hablan de defensa. Y el propio Ibn Kathir prohíbe matar a mujeres, niños, ancianos y monjes.'),
  ('N', 'Pero algunos comentaristas clásicos dicen que eso fue solo el principio, y que quedó superado. Ibn Kathir no lo cree así. Pero él mismo llama al nueve, cinco, el versículo de la espada, y explica el nueve, veintinueve, como orden de combatir a judíos y cristianos. Y la práctica de Mahoma, en Najla, Badr, Mustaliq, Jaybar y Tabuk, no fue solo defensa.'),
  ('N', 'Hasta el historiador W. Montgomery Watt, nada hostil al islam, lo escribió en mil novecientos cincuenta y seis: el juramento hablaba solo de defensa, pero las primeras expediciones fueron ofensivas, para emboscar caravanas de La Meca. Incluso Badr fue una razia.'),
  ('N', 'Ibn Sa\'d cuenta veintisiete expediciones dirigidas por él, y cuarenta y siete enviadas. ¿Todas en defensa propia?'),
 ]),
 dict(id='jesus', title='¿Y Jesús?', vis='jesus', segs=[
  ('N', 'Compáralo con Jesús. Cuando Pedro sacó la espada para defenderlo, le dijo:'),
  ('F', 'Vuelve tu espada a su sitio, porque todos los que tomen espada, a espada perecerán.'),
  ('N', 'Y ante Pilato: mi reino no es de este mundo. Si lo fuera, mis servidores pelearían. Y cuando sus discípulos quisieron hacer bajar fuego sobre una aldea que lo rechazó, los reprendió: el Hijo del Hombre no ha venido a destruir vidas, sino a salvarlas.'),
 ]),
 dict(id='end', title='Resumen', vis='end', segs=[
  ('N', 'Resumen. Uno: las primeras expediciones iban contra caravanas. Dos: hubo ataques por sorpresa, como Banu al-Mustaliq y Jaybar.'),
  ('N', 'Tres: el Corán y los hadices mandan combatir hasta el islam o el tributo. Cuatro: los comentaristas y los juristas clásicos lo entendieron así.'),
  ('N', 'Esto no va contra los musulmanes, a quienes respetamos. Va de lo que dicen sus propias fuentes. Si te ha servido, compártelo. Y si quieres las fuentes con sus páginas, pídelas en comentarios.'),
 ]),
]
