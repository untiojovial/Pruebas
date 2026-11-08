# -*- coding: utf-8 -*-
# Guion del vídeo: escenas con segmentos (hablante, texto). N = narrador, E = escéptico, P = Padre citado.
VOICES = {'N': ('es-ES-AlvaroNeural', '+11%', '+0Hz'), 'E': ('es-MX-JorgeNeural', '+9%', '+0Hz'), 'P': ('es-CO-GonzaloNeural', '-4%', '-4Hz')}
SCENES = [
 dict(id='hook', title='¿José tenía DOS padres?', vis='hook', segs=[
  ('E', '¡Las genealogías de Jesús se contradicen! Mateo dice que el padre de José es Jacob. Lucas dice que es Elí. ¡Un hombre no puede tener dos padres!'),
  ('N', 'Esta objeción tiene casi dos mil años. Hoy la vamos a desmontar con las fuentes en la mano: griego, hebreo, latín, y páginas reales de los libros.'),
  ('N', 'Y también la otra: que decir que Lucas da la línea de María es un invento del año mil quinientos. Quédate, porque ahí hay sorpresa.'),
 ]),
 dict(id='tree', title='Dos listas, un David', vis='tree', segs=[
  ('N', 'Primero, los hechos. Mateo baja desde Abrahán hasta Jesús. Lucas sube desde Jesús hasta Adán. Hasta el rey David, las dos coinciden.'),
  ('N', 'Pero desde David se separan. Mateo sigue la línea de los reyes, por Salomón. Lucas va por Natán, otro hijo de David.'),
  ('N', 'Se vuelven a cruzar en dos nombres, Salatiel y Zorobabel, y terminan en José. Con dos padres distintos: Jacob en Mateo, Elí en Lucas.'),
 ]),
 dict(id='logic', title='¿Qué es una contradicción?', vis='logic', segs=[
  ('N', 'Ahora, lógica. Dos frases se contradicen solo si es imposible que las dos sean verdad a la vez.'),
  ('N', 'Basta con encontrar una forma coherente en que ambas sean verdad, y la contradicción desaparece.'),
  ('E', '¿Y qué forma va a haber? ¡Un hombre tiene un solo padre!'),
  ('N', 'En el Israel antiguo, no siempre. Mira esto.'),
 ]),
 dict(id='levir', title='La ley del levirato', vis='levir', segs=[
  ('N', 'Hacia el año doscientos veinte, Julio Africano lo explicó así. Una mujer, Esta, se casa con Matán, de la línea de Salomón. Tienen a Jacob.'),
  ('N', 'Matán muere. Ella se casa con Melquí, de la línea de Natán. Tienen a Elí. Jacob y Elí son hermanos de madre.'),
  ('N', 'Elí se casa, y muere sin hijos. La ley de Moisés, en Deuteronomio veinticinco, manda que el hermano tome a la viuda, para darle descendencia al muerto.'),
  ('N', 'Jacob lo hace. Y nace José: hijo de Jacob por naturaleza, e hijo de Elí por ley. Dos padres. Cero contradicción.'),
 ]),
 dict(id='euseb', title='Eusebio lo conserva', vis='scan_euseb', segs=[
  ('P', 'Jacob engendró a José, hijo suyo por naturaleza; pero según la ley, era hijo de Elí.'),
  ('N', 'Lo cuenta Eusebio de Cesarea, en su Historia de la Iglesia. Y ojo: Africano es honesto. Admite que no tiene documentos que lo prueben. Pero no hace falta probar cada eslabón. Basta con mostrar que es posible.'),
 ]),
 dict(id='zoro', title='La Biblia hebrea hace lo mismo', vis='zoro', segs=[
  ('N', '¿Te parece raro un hombre con dos padres? La propia Biblia hebrea lo hace. Esdras y Ageo llaman a Zorobabel hijo de Salatiel. Primero de Crónicas lo llama hijo de Pedaías.'),
  ('N', 'Nadie dice que la Biblia hebrea se contradiga ahí. Pues con la misma vara hay que medir a Mateo y a Lucas.'),
 ]),
 dict(id='greek', title='Los evangelistas te avisan', vis='greek', segs=[
  ('N', 'Además, los dos evangelistas te avisan. Lucas escribe que Jesús era hijo de José, según se pensaba.'),
  ('N', 'Y Mateo rompe su propia fórmula. No dice: José engendró a Jesús. Dice: José, el esposo de María, de la cual nació Jesús. En griego, de la cual va en femenino.'),
  ('N', 'Ninguno pretende que José sea el padre biológico. La supuesta contradicción les atribuye una intención que ellos mismos niegan.'),
 ]),
 dict(id='roads', title='¿Solo José viene de David?', vis='roads', segs=[
  ('E', 'Vale. Pero entonces Jesús no tiene sangre de José. ¡Y sin sangre de José, no es hijo de David!'),
  ('N', 'Dos respuestas. La primera: la ley. En la Misná, quien dice este es mi hijo, es creído. Y el Talmud enseña que quien cría a un huérfano, la Escritura lo cuenta como si lo hubiera engendrado.'),
  ('N', 'José le pone el nombre al niño. Es su hijo legal, y heredero de sus derechos. Por eso el ángel lo llama: José, hijo de David.'),
  ('N', 'La segunda: la carne. San Pablo dice que Jesús es del linaje de David según la carne. Si no tuvo padre humano, esa carne solo puede venir de María.'),
  ('N', 'Por eso el ángel le promete a María, sin varón de por medio, el trono de David, su padre. Dos títulos: uno por ley, por José. Otro por sangre, por María.'),
 ]),
 dict(id='aaron', title='¿María era levita?', vis='aaron', segs=[
  ('E', '¡Pero María era levita! Su pariente Isabel era de las hijas de Aarón.'),
  ('N', 'Esa objeción ya la hizo un maniqueo, Fausto, hacia el año cuatrocientos. Pero ser pariente no te dice la tribu: la tribu va por el padre.'),
  ('N', 'Y el mejor ejemplo es el propio Aarón: se casó con Eliseba, hermana de Naasón, el príncipe de Judá. Todos los sacerdotes descendían de una madre de Judá.'),
 ]),
 dict(id='jecon', title='La maldición de Jeconías', vis='jecon', segs=[
  ('E', '¿Y la maldición de Jeconías? Jeremías dijo que ninguno de su semilla se sentaría en el trono de David. ¡Y Mateo pone a Jesús en esa línea!'),
  ('N', 'Aquí la objeción cae en un dilema. Opción uno: la maldición se levantó. Dios le dice a Zorobabel, nieto de Jeconías: te pondré como anillo de sello. Justo la imagen de la maldición, pero al revés.'),
  ('N', 'Y los rabinos, en Levítico Rabá, dicen que el arrepentimiento anuló el juramento y el decreto.'),
  ('N', 'Opción dos: la maldición sigue en pie. Pero cae sobre su semilla. Y Jesús no es semilla de José. Hereda el derecho legal, sin la sangre maldita.'),
 ]),
 dict(id='ireneo', title='Ireneo, año 180', vis='scan_ireneo', segs=[
  ('P', 'No nacerá de su semilla, es decir, de José; sino que, según la promesa de Dios, del vientre de David se levanta el Rey eterno.'),
  ('N', 'Lo escribió Ireneo de Lyon hacia el año ciento ochenta. Elijas la opción que elijas, la objeción no llega.'),
 ]),
 dict(id='y1500', title='¿Un invento del año 1500?', vis='y1500', segs=[
  ('E', 'Bueno, ¿y lo de que Lucas da la línea de María? ¡Eso se lo inventaron hacia el mil quinientos!'),
  ('N', 'Vamos a ser honestos. La frase exacta, la lista de Lucas es la de María, y Elí es su padre, no la he encontrado antes de Annio de Viterbo, hacia el mil cuatrocientos noventa. Eso es verdad.'),
  ('N', 'Pero la conclusión no se sigue. Primero: que una idea se formule tarde no la hace falsa. Eso es una falacia genética. Segundo: las piezas de esa idea son antiquísimas.'),
 ]),
 dict(id='justino', title='Justino Mártir, año 155', vis='justino', segs=[
  ('N', 'Hacia el año ciento cincuenta y cinco, Justino Mártir dice que la Virgen es del linaje de David, Jacob, Isaac y Abrahán. Habla de los antepasados enumerados de los que María trae su linaje. Y añade:'),
  ('P', 'Sabemos que los padres de las mujeres son también padres de los hijos que dan a luz sus hijas.'),
  ('N', 'Hasta el crítico alemán Strauss, nada sospechoso, reconoce que Justino aplicaba a María una de las genealogías.'),
 ]),
 dict(id='timeline', title='Siglos II al VIII', vis='timeline', segs=[
  ('N', 'Hacia el ciento ochenta, Ireneo: María es del linaje de David. Hacia el doscientos diez, Tertuliano, lo mismo.'),
  ('N', 'En el siglo cuarto, Eusebio, Jerónimo y Crisóstomo explican que la genealogía de José muestra también el origen de María, porque la ley mandaba casarse dentro de la tribu.'),
  ('N', 'Y en el siglo octavo, Juan Damasceno hace descender a María de Natán, la rama de Lucas, y la pone en la misma familia que Elí.'),
  ('N', 'Lo que aparece hacia el mil quinientos es solo la combinación explícita. Y la explicación cristiana más antigua, la de Africano, ni siquiera la necesita.'),
 ]),
 dict(id='omis', title='¿Mateo se salta reyes?', vis='omis', segs=[
  ('E', '¡Mateo se salta reyes! Ocozías, Joás, Amasías... ¡y luego dice catorce, catorce y catorce!'),
  ('N', 'Los omite, es verdad. Pero en las genealogías bíblicas, hijo de significa descendiente de. Esdras se llama hijo de Seraías, que murió más de un siglo antes. Y la lista de Esdras se salta seis generaciones de la de Crónicas.'),
  ('N', 'Mateo hace tres bloques de catorce para memorizar. Y catorce es el valor de David en hebreo: dálet, vav, dálet. Cuatro, seis, cuatro.'),
  ('N', 'Un detalle honesto: contando, salen cuarenta y un nombres, no cuarenta y dos. Cómo contaba Mateo exactamente se sigue discutiendo.'),
 ]),
 dict(id='cainan', title='¿Y Cainán?', vis='cainan', segs=[
  ('E', '¿Y Cainán? Lucas mete un Cainán que no está en el Génesis.'),
  ('N', 'No está en el Génesis hebreo. Pero sí en la Biblia griega de los Setenta, la que leían sus lectores: Arfaxad engendró a Cainán. Lucas cita fielmente su Biblia.'),
 ]),
 dict(id='talmud', title='Cuidado con este mito', vis='talmud', segs=[
  ('N', 'Y un aviso para los nuestros. Muchos apologistas dicen que el Talmud llama a María hija de Elí. Lo he comprobado.'),
  ('N', 'El texto dice: Miriam, hija de Ali Betzalim. Algo así como hoja de cebolla. No habla de Jesús. Es una conjetura del siglo diecisiete. No la uses.'),
 ]),
 dict(id='end', title='Resumen', vis='end', segs=[
  ('N', 'Resumen. Uno: no hay contradicción lógica. Hay paternidad natural y legal.'),
  ('N', 'Dos: Jesús es hijo de David por la ley, a través de José, y por la carne, a través de María.'),
  ('N', 'Tres: la maldición de Jeconías cae en un dilema. Cuatro: lo del mil quinientos es solo la fórmula. Sus piezas son de los siglos segundo al octavo.'),
  ('N', 'Si te ha servido, compártelo con quien te ponga esta objeción. Y si quieres las fuentes, con sus páginas, pídelas en comentarios.'),
 ]),
]
