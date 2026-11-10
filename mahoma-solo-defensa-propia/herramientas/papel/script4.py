# -*- coding: utf-8 -*-
# «¿Qué pasó con los poetas?» — guion corto (≈4 min), un narrador. Misma notación que script3.py.
VOICE = ('es-ES-AlvaroNeural', '+3%', '-26Hz')
G = 'IBN ISHAQ · SIRA (TRAD. GUILLAUME 1955), '
SCENES = [
 dict(id='hook', segs=[
  ('N', 'Tres poetas. Tres poemas. Y tres *muertes*.', ''),
  ('N', 'No lo cuenta un enemigo del islam. Lo cuentan Bujari, la colección de hadices más respetada, e Ibn Ishaq, el biógrafo más antiguo de Mahoma.', 'SAHIH AL-BUJARI · ' + G[:-2]),
 ]),
 dict(id='kab', segs=[
  ('N', "Primero: Ka'b ibn al-Ashraf, un poeta de Medina. Tras la batalla de Badr viaja a La Meca, y llora en verso a los muertos de Quraysh. Luego, dice Ibn Ishaq, compone versos *ofensivos* sobre las mujeres musulmanas.", G + 'PP. 365-367'),
  ('N', 'Era un enemigo declarado, hay que decirlo. Pero su arma eran los *versos*. Y la respuesta está en Bujari, cuatro mil treinta y siete:', 'SAHIH AL-BUJARI 4037'),
  ('Q', "¿Quién *matará* a Ka'b ibn al-Ashraf, que ha ofendido a Dios y a su mensajero? Muhammad ibn Maslama dijo: ¿quieres que lo mate? Dijo: sí. Entonces permíteme decir algo para *engañarlo*.", 'SAHIH AL-BUJARI 4037 (TRAD. MUHSIN KHAN)'),
  ('N', 'Van de noche. Fingen ser amigos. Lo sacan de su fortaleza. Y según Ibn Ishaq, se oye el grito: «¡*Golpead* al enemigo de Dios!».', 'SAHIH AL-BUJARI 4037 · ' + G + 'P. 368'),
  ('N', 'A la mañana siguiente, según Ibn Ishaq, el Profeta dijo: «*Matad* a cualquier judío que caiga en vuestro poder». Y un mercader, Ibn Sunayna, muere a manos de un hombre con quien tenía trato y negocios.', G + 'P. 369'),
 ]),
 dict(id='afak', segs=[
  ('N', 'Segundo: Abu Afak, un anciano. Compuso versos contra Mahoma. Ibn Ishaq cuenta la reacción:', G + 'P. 675'),
  ('Q', '¿Quién se ocupará de este *canalla* por mí? Y Sálim ibn Umayr salió, y lo *mató*.', G + 'P. 675'),
 ]),
 dict(id='asma', segs=[
  ('N', 'Tercera: Asma bint Marwán, una mujer. Tras la muerte de Abu Afak, compone versos contra el islam y sus seguidores.', G + 'PP. 675-676'),
  ('Q', '¿Quién me librará de la hija de Marwán? Umayr ibn Adí lo oyó, y esa misma noche fue a su casa, y la *mató*.', G + 'P. 676'),
  ('N', 'Por la mañana se lo contó al Profeta, que le dijo: «Has *ayudado* a Dios y a su apóstol». Y añadió: «Ni dos cabras se darán de cabezazos por ella».', G + 'P. 676'),
 ]),
 dict(id='more', segs=[
  ('N', 'Y no son casos aislados. Al conquistar La Meca, Ibn Ishaq nombra a dos cantoras que cantaban sátiras sobre él: ordenó *matarlas*. Una murió. La otra pidió inmunidad, y la obtuvo.', G + 'P. 551'),
  ('N', 'Y Abu Dawud recoge el caso de un ciego que mató a su esclava, madre de sus hijos, porque insultaba al Profeta. La respuesta: «Sed testigos: por su *sangre* no se debe nada».', 'SUNAN ABU DAWUD 4361'),
 ]),
 dict(id='fair', segs=[
  ('N', "Ahora, lo justo. Uno: Ka'b no era solo un poeta: animaba al enemigo después de una batalla. Dos: los relatos de Abu Afak y de Asma vienen de Ibn Ishaq sin cadena de transmisores, y muchos estudiosos musulmanes los rechazan por débiles. El de Ka'b, en cambio, está en Bujari y en Muslim.", 'IBN ISHAQ, PP. 365, 675-676 · BUJARI 4037 · MUSLIM (K. AL-YIHAD)'),
  ('N', "Tres: Ibn Ishaq dice también que no mataba a quien acudía a él *arrepentido*. El poeta Ka'b ibn Zuhayr se hizo musulmán, y fue perdonado.", G + 'PP. 597-598'),
  ('N', 'Pero fíjate en la condición. Se salvaba el que se arrepentía. El que seguía con sus versos, *no*.', G + 'P. 597'),
 ]),
 dict(id='jesus', segs=[
  ('N', 'Compáralo con Jesús. A sus discípulos les mandó:', 'MATEO 5:44'),
  ('Q', '*Amad* a vuestros enemigos, y orad por los que os persiguen.', 'MATEO 5:44'),
  ('N', 'Y Pedro, que lo vio morir, lo recordó así: «Cuando lo insultaban, no devolvía el *insulto*».', '1 PEDRO 2:23'),
  ('N', 'Esto no va contra los musulmanes, a quienes respetamos. Va de lo que dicen sus propias fuentes. ¿Qué te parece? Comenta tu postura. Y si quieres las páginas, pídelas en comentarios.', ''),
 ]),
]
def clean(t): return t.replace('*', '')
