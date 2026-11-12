# -*- coding: utf-8 -*-
# «El error coránico de los mandeos: ¿salvados o condenados?» — un narrador.
# (tipo, texto, fuente). 'N' narración, 'Q' cita leída (sale en tarjeta). *palabra* = clave (no se lee).
VOICE = ('es-ES-AlvaroNeural', '+14%', '-26Hz')
IR1 = 'ENCYCLOPAEDIA IRANICA, «MANDAEANS i. HISTORY» (E. LUPIERI)'
IR2 = 'ENCYCLOPAEDIA IRANICA, «MANDAEANS ii. RELIGION» (K. RUDOLPH)'
CH = ['EL GANCHO', 'QUIÉNES SON LOS MANDEOS', 'LA PROMESA', '¿SABEOS = MANDEOS?', 'LOS COMENTARISTAS', 'JUAN SÍ, JESÚS NO', 'LA CONDENA', 'EL DILEMA', 'LAS RESPUESTAS', 'LA INVESTIGACIÓN', 'EL VEREDICTO']
SCENES = [
 dict(id='hook', ch=0, segs=[
  ('N', 'Imagina una religión que venera a Juan el Bautista, pero *rechaza* a Jesucristo. Una religión que ya existía antes del islam, y que varios investigadores identifican con los *sabeos* del Corán.', ''),
  ('N', 'Ahora viene el problema. El Corán promete *salvación* a los sabeos. Pero también *condena* a quienes aceptan a unos mensajeros y rechazan a otros.', 'CORÁN 5:69 · CORÁN 4:150-151'),
  ('N', '¿Qué pasa con una religión que acepta a Juan y rechaza a Jesús? ¿Se salva, o se *condena*? Vamos a verlo con sus propios textos.', ''),
 ]),
 dict(id='who', ch=1, segs=[
  ('N', 'Los mandeos. Una pequeña comunidad del sur de Irak y del suroeste de Irán. Se bautizan una y otra vez en *agua* *corriente*, a la que llaman Jordán.', IR2),
  ('N', 'Su lengua sagrada es el mandeo, un arameo oriental. Su dios supremo, la Gran *Vida*. Sus libros: la Ginza y el Libro de Juan.', IR2),
  ('N', '¿Son anteriores al islam? Sí. Los arqueólogos han hallado cuencos de conjuros y amuletos de plomo mandeos, que prueban su presencia en Mesopotamia *antes* *del* *islam*. Los más antiguos se datan en los siglos tres o cuatro.', IR1 + ' · ' + IR2),
  ('N', '¿Vienen de los discípulos de Juan en Palestina? Eso es solo una *hipótesis*. Edmondo Lupieri, por ejemplo, cree más probable que surgieran en Mesopotamia, hacia el siglo dos, de un gnosticismo ya posterior a Cristo.', IR1),
 ]),
 dict(id='promise', ch=2, segs=[
  ('N', 'Ahora, el Corán. La palabra sabeos aparece tres veces. La primera, en la sura dos, versículo sesenta y dos.', 'CORÁN 2:62'),
  ('Q', 'Los que creen, los judíos, los cristianos y los *sabeos*: quien crea en Dios y en el Último Día, y obre el bien, tendrá su *recompensa* junto a su Señor. No temerán, ni estarán tristes.', 'CORÁN 2:62 (TRAD. PROPIA DEL ÁRABE)'),
  ('N', 'La sura cinco, versículo sesenta y nueve, lo repite casi igual. Y fíjate en las condiciones expresas: son *tres*. Creer en Dios. Creer en el Último Día. Y obrar el bien.', 'CORÁN 5:69'),
  ('N', 'Ojo: algunas traducciones añaden entre corchetes «antes del profeta Mahoma». Esas palabras *no* *están* en el árabe. Son interpretación del traductor.', 'CORÁN 2:62 Y 5:69 (SAHEEH INTERNATIONAL)'),
  ('N', 'Veintidós, diecisiete, no promete nada: solo dice que Dios juzgará entre todas esas comunidades. Pero confirma que los sabeos son una *comunidad* *distinta*.', 'CORÁN 22:17'),
 ]),
 dict(id='identity', ch=3, segs=[
  ('N', '¿Quiénes eran esos sabeos? Los primeros comentaristas musulmanes no se ponían de acuerdo. Ibn Kathir lo reconoce: hay *diferencia* *de* *opinión*.', 'TAFSIR IBN KATHIR SOBRE 2:62 (QURAN.COM)'),
  ('N', 'Hoy, varios especialistas apuntan a los mandeos. Sinasi Gündüz lo escribe sin rodeos:', 'Ş. GÜNDÜZ, ARAM 11 (1999-2000), PP. 269-279'),
  ('Q', 'Está bastante claro que los sabeos del Corán descritos por los primeros autores son los *mandeos* del sur de Irak.', 'Ş. GÜNDÜZ, ARAM 11 (1999-2000), PP. 269-279'),
  ('N', 'Y añade que, desde los abasíes, se los confundió con los paganos de *Harrán*. La enciclopedia Iranica confirma la otra mitad: los musulmanes llamaron sabeos a los mandeos, y eso les permitió ser tolerados como gente del Libro.', IR2),
  ('N', 'Pero cuidado: no es un consenso universal. Alena Kulinich muestra que su identidad sigue discutida, y que de ella depende cómo se leen estos versículos sobre la *salvación*.', 'A. KULINICH, JOURNAL OF HUMANITIES (SNU) 75.4 (2018)'),
 ]),
 dict(id='exeg', ch=4, segs=[
  ('N', 'Y la incertidumbre de los primeros comentaristas es muy significativa. El Corán menciona a los sabeos tres veces, pero no explica *quiénes* son. Y las generaciones posteriores dieron descripciones muy distintas.', 'AL-TABARI, TAFSIR SOBRE 2:62'),
  ('N', 'Para Muyahid, no eran judíos ni cristianos, y *no* *tenían* *religión*. Para Ibn Zayd, vivían en la región de Mosul, y no tenían ni *libro* ni *profeta*.', 'AL-TABARI SOBRE 2:62 (MUYAHID, IBN ZAYD)'),
  ('N', 'Para Qatada, adoraban a los *ángeles* y leían los Salmos. Y en Bujari aparece una idea parecida, atribuida a Abu al-Aliya: una secta de la gente del Libro que recita los *Salmos*.', 'AL-TABARI SOBRE 2:62 (QATADA) · SAHIH AL-BUJARI 344'),
  ('N', 'Ojo: eso no lo dice Mahoma. Es un *comentario* que al-Bujari añade al final de un hadiz, citando a un sabio de la generación siguiente.', 'SAHIH AL-BUJARI 344 (TRAD. MUHSIN KHAN)'),
  ('N', 'Y los mandeos reales tienen sacerdotes, liturgia, y una literatura sagrada *extensa*. Esto muestra que los comentaristas no sabían bien de quién hablaban. No demuestra, por sí solo, un error del texto del Corán.', IR2),
 ]),
 dict(id='jesus', ch=5, segs=[
  ('N', 'Ahora mira qué dice el Corán de Juan y de Jesús. Tres, cuarenta y cinco: su nombre será el *Mesías*, Jesús, hijo de María.', 'CORÁN 3:45'),
  ('N', 'Cuatro, ciento setenta y uno: el Mesías es *mensajero* de Dios. Y seis, ochenta y cinco, pone juntos a Zacarías, *Juan* y *Jesús*: todos entre los justos.', 'CORÁN 4:171 · 6:85'),
  ('N', 'Y ahora, el Libro de Juan mandeo. Jesús va al Jordán y le pide a Juan que lo bautice. Esta es la respuesta de Juan:', 'LIBRO DE JUAN MANDEO, § 30'),
  ('Q', 'Has *mentido* a los judíos, y has engañado a los sacerdotes.', 'G. R. S. MEAD, THE GNOSTIC JOHN THE BAPTIZER (1924), P. 49 · LIDZBARSKI (1915), P. 104'),
  ('N', 'Y al final llega una carta del mundo de la luz: «Juan, bautiza al *engañador* en el Jordán».', 'MEAD (1924), P. 51'),
  ('N', 'La Ginza es aún más dura: el enviado de la luz desenmascarará la mentira del *mentiroso* Jesús, el Cristo romano.', 'GINZA, PARTE DERECHA, P. 52 (TRAD. LIDZBARSKI 1925)'),
  ('N', 'Pero seamos rigurosos. Esa parte de la Ginza menciona a «Ahmat, hijo de Bizbat»: según Lidzbarski, *Mahoma*. Así que estos textos se editaron, al menos en parte, en época islámica.', 'GINZA, PARTE DERECHA, P. 30 (LIDZBARSKI 1925)'),
  ('N', 'Kurt Rudolph cree que esta polémica surgió tras el choque con el primer cristianismo. Pero los textos mezclan material antiguo y tardío: *no* *se* *puede* *demostrar* que sea anterior al siglo siete.', IR2),
 ]),
 dict(id='condemn', ch=6, segs=[
  ('N', 'Y ahora, el segundo texto del Corán. Sura cuatro, versículos ciento cincuenta y ciento cincuenta y uno.', 'CORÁN 4:150-151'),
  ('Q', 'Los que no creen en Dios y en sus mensajeros, y quieren separar entre Dios y sus mensajeros, y dicen: creemos en *unos* y rechazamos a *otros*… esos son los *verdaderos* *incrédulos*. Y para los incrédulos hemos preparado un castigo humillante.', 'CORÁN 4:150-151 (TRAD. PROPIA DEL ÁRABE)'),
  ('N', 'El versículo siguiente lo remata: la recompensa es para quien cree en todos sus mensajeros, sin hacer *distinción* entre ninguno. Y dos, doscientos ochenta y cinco, repite: no hacemos distinción entre sus mensajeros.', 'CORÁN 4:152 · 2:285'),
  ('N', 'Ibn Kathir lo aplica sin rodeos: los judíos creen en los profetas, *excepto* en Jesús y en Mahoma. Y quien rechaza a un solo profeta, ha *rechazado* *a* *todos*.', 'TAFSIR IBN KATHIR SOBRE 4:150 (QURAN.COM)'),
  ('N', 'Si los sabeos son los mandeos, encajan justo en esa descripción. Reconocen a Juan. Rechazan a Jesús como Mesías. Entonces, ¿por qué aparecen en la lista de los que se *salvan*?', ''),
 ]),
 dict(id='dilemma', ch=7, segs=[
  ('N', 'Formulemos el argumento con cuidado. Uno: dos, sesenta y dos, y cinco, sesenta y nueve, prometen recompensa a los sabeos que crean en Dios, en el Último Día, y obren el bien.', 'CORÁN 2:62 · 5:69'),
  ('N', 'Dos: cuatro, ciento cincuenta, condena a quien acepta a unos y rechaza a otros. Tres: el Corán reconoce a Juan y a Jesús. Cuatro: los mandeos veneran a Juan y rechazan a Jesús.', 'CORÁN 4:150-151 · 3:45 · 6:85'),
  ('N', 'Y cinco: la identificación entre sabeos y mandeos está defendida por especialistas. Defendida, no *demostrada*.', 'GÜNDÜZ (1999-2000) · KULINICH (2018)'),
  ('N', 'Hay cuatro salidas. Primera: el sabeo se salva sin aceptar a Jesús. Pero entonces choca con cuatro, ciento cincuenta.', ''),
  ('N', 'Segunda: no se salva sin aceptar a Jesús. Pero entonces la promesa exige una condición que *no* *está* *escrita* en esos versículos.', ''),
  ('N', 'Tercera: la promesa fue *abrogada*. Pero entonces, ¿por qué vuelve a aparecer en la sura cinco, que la tradición sitúa entre las últimas?', ''),
  ('N', 'Cuarta: los sabeos no eran los mandeos. Pero entonces hay que demostrar quiénes eran. Cada salida tiene un *coste*. Y para que haya contradicción en sentido estricto, ambas reglas tienen que aplicarse a la misma persona, en el mismo sentido.', ''),
 ]),
 dict(id='answers', ch=8, segs=[
  ('N', 'Veamos las mejores respuestas musulmanas. La primera: cada pueblo se salvaba siguiendo al profeta de su época. Ibn Kathir lo explica así:', 'TAFSIR IBN KATHIR SOBRE 2:62'),
  ('Q', 'Antes de eso, todo el que seguía la guía de *su* *propio* *profeta* estaba en el camino correcto, y se salvaba.', 'TAFSIR IBN KATHIR SOBRE 2:62 (QURAN.COM)'),
  ('N', 'Es coherente. Pero lee las tres condiciones a la luz de *otros* *versículos*. ¿Y qué alcance tiene entonces nombrar a los sabeos?', ''),
  ('N', 'La segunda: tres, ochenta y cinco. A quien busque una religión distinta del islam, no se le aceptará. Al-Tabari recoge que, según Ibn Abbas, ese versículo *abrogó* la promesa.', 'CORÁN 3:85 · AL-TABARI SOBRE 2:62'),
  ('N', 'Problema: cinco, sesenta y nueve, repite la promesa, y según Tirmidhi la sura cinco fue la *última* revelada. Muslim da otra sura, y la fecha de una sura no fija la de cada versículo.', 'TIRMIDHI 3063 · MUSLIM 1618 (AL-BARA)'),
  ('N', 'La tercera respuesta: creer de verdad en Dios ya incluye aceptar a todos sus mensajeros. Es lógicamente *coherente*. Pero convierte una promesa que suena amplia en una promesa para quien acepta toda la revelación islámica.', ''),
  ('N', 'La cuarta: quizá hubo unos sabeos originales fieles a un profeta propio, y el mandeísmo se corrompió después. Es posible en teoría. Pero, ¿qué *fuente* lo muestra?', 'CORÁN 16:36 · 35:24'),
  ('N', 'Y la quinta: Dios no castiga a quien no recibió bien el mensaje. Es justo reconocerlo. Pero la objeción apunta al que rechaza a Jesús *a* *sabiendas*, y cumple las otras tres condiciones.', 'CORÁN 17:15 · 4:165'),
 ]),
 dict(id='scholar', ch=9, segs=[
  ('N', 'Esta dificultad no es una invención de los apologetas cristianos. Es un problema estudiado dentro de la *investigación* *académica* sobre el Corán.', ''),
  ('N', 'Mun\'im Sirry, en Scriptural Polemics, Oxford University Press, dos mil catorce, dedica un capítulo al debate sobre la salvación exclusivista: los versículos que parecen *ampliar* la salvación, frente a los que parecen *restringirla* al islam.', 'M. SIRRY, SCRIPTURAL POLEMICS (OUP 2014), CAP. 3, PP. 65-99'),
  ('N', 'Sirry *no* dice haber demostrado una contradicción insalvable. Analiza un debate. La conclusión apologética es *nuestra*.', 'M. SIRRY, SCRIPTURAL POLEMICS (OUP 2014)'),
  ('N', 'Lo que hacemos en este vídeo es aplicar esa dificultad general a una comunidad concreta: los *mandeos*.', ''),
 ]),
 dict(id='end', ch=10, segs=[
  ('N', 'Volvamos a los dos versículos. Cinco, sesenta y nueve: la *promesa*. Cuatro, ciento cincuenta: la *condena*.', 'CORÁN 5:69 · 4:150-151'),
  ('N', 'El dilema de los mandeos revela una dificultad de fondo en la doctrina coránica de la *salvación*.', ''),
  ('N', 'Si la promesa basta con sus tres condiciones expresas, choca con la condena de quien rechaza a los profetas. Si además exigimos aceptar a todos los mensajeros, la promesa se lee con una condición que el versículo *no* *enuncia*.', 'CORÁN 2:62 · 5:69 · 4:150-151'),
  ('N', 'Y si recurrimos a la abrogación, aún hay que explicar por qué la promesa *reaparece* en una de las últimas suras. La pregunta sigue en pie: ¿cuál era exactamente la situación de los sabeos ante Dios?', 'CORÁN 3:85 · 5:69'),
  ('N', 'El Corán ofrece una promesa que, para ser coherente con otros pasajes, necesita ser *reinterpretada*. El caso de los mandeos hace visible el problema.', ''),
  ('N', 'Esto no va contra los musulmanes, a quienes respetamos. ¿Salvados o condenados? Comenta tu respuesta. Y si quieres las fuentes, pídelas en comentarios.', ''),
 ]),
]
def clean(t): return t.replace('*', '')
