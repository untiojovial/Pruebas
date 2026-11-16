# -*- coding: utf-8 -*-
# Núcleo de evidencia directa, clasificado por el orquestador: PMID -> (grupo, área, grado, nota crítica)
# Grado: A = validación externa en cohorte de la enfermedad; B = prueba independiente o cohorte >=50 con validación interna;
#        C = prueba de concepto (muestra pequeña, sin validación o no consta); D = in silico o preclínico.
AREAS = {'4.1': 'Sospecha y diagnóstico precoz (historia clínica, lenguaje natural, cribado)', '4.2': 'Genética e interpretación de variantes', '4.3': 'Biomarcadores y ómicas',
         '4.4': 'Imagen y patología digital', '4.5': 'Pronóstico y estratificación', '4.6': 'Tratamiento y monitorización', '4.7': 'IA generativa y modelos de lenguaje', '4.8': 'Investigación clínica y fármacos'}
CORE = {
 # Gaucher
 '39245415': ('Gaucher', '4.1', 'B', 'Caso-control en una sola aseguradora (264 casos, 3.429 controles). Prueba interna con el 25 % de los datos; sin validación externa ni prospectiva. Una carta posterior (PMID 39617306) discute sesgos en la importancia de las variables.'),
 '37689674': ('Gaucher', '4.1', 'B', 'Datos de reclamaciones de EE. UU. Mide eficiencia (pacientes a revisar para encontrar 28 diagnosticados), no AUC. Hay un estudio de implementación registrado (NCT05908656).'),
 '34663554': ('Gaucher', '4.1', 'C', 'Reconocimiento facial en Gaucher tipos 2 y 3 con una plataforma comercial; fotos, no pacientes consecutivos. Utilidad clínica no evaluada.'),
 '32962737': ('Gaucher', '4.5', 'C', 'Registro español (358 pacientes). Árbol de decisión exploratorio: describe factores asociados, no da rendimiento predictivo ni validación.'),
 '37250646': ('Gaucher', '4.5', 'C', '441 resonancias de 131 pacientes. El bosque aleatorio ordena variables por importancia; el resumen no da métricas de predicción.'),
 '37629403': ('Gaucher', '4.4', 'C', 'Volumen esplénico por aprendizaje profundo; conjunto de prueba de 20 pacientes. Mejora el error frente a la fórmula habitual.'),
 '38834102': ('Gaucher', '4.4', 'C', 'Segmentación de osteonecrosis (cohorte Gaucherite). Sin métricas de segmentación en el resumen y sin correlación fuerte con la puntuación de carga medular.'),
 '27109052': ('Gaucher', '4.4', 'C', '20 pacientes y 10 controles; AUC 0,79. Estudio antiguo (2016) y pequeño.'),
 '39201273': ('Gaucher', '4.3', 'D', 'Modelización in silico de candidatos a biomarcador óseo; sin validación en pacientes.'),
 '34529671': ('Gaucher, Fabry y Pompe', '4.2', 'D', 'Predice la respuesta a chaperonas farmacológicas a partir de la estructura proteica; entrenado sobre todo con variantes de Fabry. Trabajo computacional.'),
 # Fabry
 '34930374': ('Fabry', '4.1', 'B', 'Calibrado con casi 5.000 pacientes; AUROC 0,82 fuera de muestra. Datos estructurados de EE. UU.; sin evaluación prospectiva ni confirmación diagnóstica de los señalados.'),
 '38187171': ('Fabry', '4.1', 'B', 'Prueba con muestras independientes (30 casos, 167 controles). Es un modelo estadístico de riesgo: está en la frontera de lo que se llama IA.'),
 '37240705': ('Fabry', '4.1', 'C', 'El lenguaje natural extrae rasgos, pero la puntuación es por reglas de expertos. El AUC de 0,998 no se acompaña de la descripción de la cohorte en el resumen; un paciente confirmado.'),
 '38424111': ('Fabry', '4.1', 'C', 'Agrupamiento no supervisado en 1,28 millones de historias; parte de 4 pacientes y propone 2 más. Prueba de concepto.'),
 '40587431': ('Fabry', '4.1', 'C', 'Cuestionario con IA; 33 pacientes; validación cruzada interna.'),
 '40874831': ('Fabry', '4.1', 'C', 'Verificador de síntomas; piloto prospectivo con 6 pacientes (2 de 6 frente a 1 de 6).'),
 '38982319': ('Fabry', '4.1', 'C', 'Regresión logística sobre datos de una aseguradora alemana: frontera de la IA. Sin confirmación diagnóstica.'),
 '37061786': ('Fabry', '4.5', 'C', 'Agrupamiento de trayectorias de filtrado glomerular en 234 varones; descriptivo, no predictivo.'),
 '32806627': ('Fabry', '4.6', 'B', '120 varones de tres centros. El bosque aleatorio no superó a una regresión logística de tres variables (AUC 0,77 ambos): ejemplo útil de que más complejidad no implica más rendimiento.'),
 '36186840': ('Fabry', '4.4', 'C', 'Sedimento urinario con red profunda (AUC 0,968 en validación). El resumen no da el número de pacientes; riesgo de que varias imágenes del mismo paciente estén en entrenamiento y validación.'),
 '41526641': ('Fabry', '4.4', 'C', 'Podocitos espumosos en biopsia renal: exactitud 79 % y solapamiento (Dice) de 0,46, modesto. Tamaño muestral no consta en el resumen.'),
 '37774924': ('Fabry', '4.4', 'B', 'Anchura de los pedicelos en microscopía electrónica: concordancia con técnicos expertos en 56 pacientes con Fabry y otros grupos. Automatiza una medida, no diagnostica.'),
 '38706878': ('Fabry', '4.4', 'A', 'Distingue miocardiopatía de Fabry de miocardiopatía hipertrófica en cine de resonancia; prueba externa en un segundo hospital (AUC 0,918). El resumen no da el número de pacientes con Fabry.'),
 '33304928': ('Fabry', '4.4', 'C', '163 pacientes con hipertrofia (30 con Fabry). El AUC de 0,94 es para separar la miocardiopatía hipertrófica de sus imitadores en conjunto, no Fabry en concreto.'),
 '42787413': ('Fabry', '4.5', 'C', '38 pacientes, retrospectivo, sin grupo control. La IA mide el ecocardiograma; no hay un modelo predictivo validado.'),
 '38520360': ('Fabry', '4.4', 'B', '«Edad cerebral» por aprendizaje profundo: 52 pacientes y 58 controles de un centro; modelo entrenado con 2.160 sanos. Biomarcador de investigación.'),
 '40181436': ('Fabry', '4.4', 'C', 'Microvasculatura retiniana: 27 pacientes y 27 controles; asociación con lesión de pequeño vaso cerebral.'),
 '34575675': ('Fabry', '4.3', 'C', 'Metabolómica: 66 pacientes y 60 controles; AUC 0,992 con 13 metabolitos, sin validación externa (riesgo de sobreajuste).'),
 '39808991': ('Fabry', '4.3', 'C', 'Espectroscopia infrarroja con aprendizaje automático; el resumen no da tamaño ni cifras.'),
 '39390597': ('Fabry', '4.3', 'C', 'Espectroscopia y análisis discriminante (PLS-DA): 100 % de sensibilidad y especificidad en 47 pacientes clásicos y 52 controles. Cifra perfecta en estudio piloto: probable sobreajuste. Frontera de la IA.'),
 '40565264': ('Fabry', '4.2', 'D', 'Variantes de GLA con AlphaMissense, EVE y FoldX; análisis computacional de la «amenabilidad» a chaperonas.'),
 # Pompe
 '37153672': ('Pompe', '4.1', 'C', '350.116 historias de 5 hospitales; 104 señalados y 19 plausibles tras revisión. Los autores llaman «especificidad» (18,27 %) a lo que es un valor predictivo positivo. Sin confirmación enzimática o genética en el resumen.'),
 '41756255': ('Pompe', '4.4', 'C', 'Resonancia en tiempo real del diafragma con segmentación automática: 11 pacientes y 11 controles, prospectivo.'),
 '35829785': ('Pompe', '4.4', 'C', '30 pacientes y 10 controles, prospectivo, un año. La red convolucional mide movilidad y curvatura del diafragma.'),
 '33267428': ('Pompe', '4.4', 'C', 'Ecografía muscular con textura y análisis discriminante: 22 niños y 6 controles (AUC 0,98). Muestra pequeña y desequilibrada.'),
 '41803906': ('Pompe', '4.5', 'C', 'Índice de marcha en 24 pacientes de inicio tardío (AUC 0,95 frente a 0,84 de la prueba de marcha). Selección de variables y análisis discriminante: frontera de la IA.'),
 # Otras enfermedades lisosomales
 '40770294': ('Mucopolisacaridosis', '4.1', 'C', '115 pacientes de un sistema sanitario; mejor modelo Naive Bayes (AUC 0,96), validación interna.'),
 '30903511': ('Mucopolisacaridosis', '4.3', 'C', 'Árbol de clasificación sobre glucosaminoglucanos en 60 casos; sin validación descrita.'),
 '38802532': ('Mucopolisacaridosis III', '4.2', 'D', 'Predictor de patogenicidad específico de gen (AUC 0,908 frente a 0,885 de AlphaMissense en NAGLU). Computacional.'),
 '42764280': ('Mucopolisacaridosis IIIA', '4.8', 'D', 'Cribado de fármacos en neuronas derivadas de pacientes con apoyo de aprendizaje automático; preclínico.'),
 '41727682': ('Varias (MPS, alfa-manosidosis)', '4.4', 'A', 'Validación externa de una herramienta general de edad ósea en una cohorte lisosomal: error medio de 7,13 meses.'),
 '42012644': ('Leucodistrofia metacromática', '4.4', 'B', 'Segmentación de la desmielinización; prueba independiente con 130 estudios de 49 pacientes (Dice 0,82).'),
 '42410243': ('Gangliosidosis GM1', '4.4', 'C', '«Edad cerebral» en 41 pacientes; biomarcador de investigación.'),
 '36358448': ('Aspartilglucosaminuria', '4.4', 'C', '22 pacientes y 24 controles; bosque aleatorio sobre resonancia.'),
 '33728252': ('CLN3', '4.4', 'C', 'Recuento automático de vacuolas en linfocitos (r = 0,98 con el manual, n = 40).'),
}
# Transferible: herramientas neuromusculares cuyo resumen no menciona Pompe
TRANSFER_NM = {'40275674': 'Myo-Guide (2.961 resonancias, 20 enfermedades neuromusculares). El resumen no dice si incluye Pompe: comprobar en el texto completo.',
               '32029545': 'Patrones de resonancia muscular en 10 distrofias (976 resonancias). El resumen no menciona Pompe.'}
