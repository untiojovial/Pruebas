---
title: "Revisión del mapa de evidencia, de la estructura y crítica del manuscrito"
subtitle: "Inteligencia artificial en las enfermedades de depósito lisosomal (en-LISOS)"
lang: es
---

# 1. Qué se ha hecho en esta ronda

Se han aplicado las seis decisiones de tus instrucciones de continuación:

- título definitivo;
- todas las enfermedades lisosomales;
- dos figuras y dos tablas;
- trabajos de frontera incluidos y diferenciados;
- solo fuentes gratuitas;
- prioridad a los textos completos en acceso abierto.

Seis documentalistas (Haiku, razonamiento medio) trabajaron en paralelo:

| Documentalista | Encargo | Resultado |
|---|---|---|
| E1 | Mucopolisacaridosis, mucolipidosis y glucoproteinosis | 33 registros (21 nuevos) |
| E2 | Leucodistrofia metacromática, Krabbe, gangliosidosis, Niemann-Pick y esfingomielinasa ácida, lipofuscinosis ceroideas (CLN) y otras | 41 registros (27 nuevos) |
| E3 | Bibliografía sobre muestra pequeña, desequilibrio de clases y validación | 33 referencias |
| E4 | Bibliografía sobre heterogeneidad, geografía, fragmentación y calidad de datos | 38 referencias |
| E5 | Lectura de textos completos: Gaucher y Fabry | 24 estudios (19 con texto completo) |
| E6 | Lectura de textos completos: imagen de Fabry, Pompe y evidencia complementaria | 23 estudios (16 con texto completo) |

**Verificación:**

- Los 186 registros de esta ronda con PMID se volvieron a pedir a PubMed. Todos existen y coinciden en título, primer autor y año. Los otros 6 son preprints o registros de ensayos sin PMID.
- Para cada cita literal se comprobó que aparece en el resumen o en el texto completo. Dos no aparecían tal cual (38706878 y 33267428); la cifra de 38706878 se comprobó a mano en el texto completo y 33267428 no se usa en el manuscrito.
- Yo mismo comprobé en los textos completos las cifras que entran en el manuscrito.

**Búsqueda:** se usaron PubMed, Europe PMC (incluidos preprints) y ClinicalTrials.gov, hasta el 16 de noviembre de 2026.

**Fuentes no consultadas:**

- Embase, Scopus y Web of Science, por falta de acceso.
- Google Scholar, porque no permite búsquedas automatizadas fiables.
- Otros registros de ensayos.

# 2. El mapa de evidencia ampliado

**Evidencia directa: 59 estudios originales en enfermedades lisosomales** (45 de la primera ronda y 14 nuevos).

| Enfermedad | Estudios | Lo más sólido |
|---|---|---|
| Fabry | 21 | Resonancia cardíaca con prueba en otro hospital; patología digital renal con prueba en otro centro |
| Gaucher | 9 | Búsqueda de casos en historias clínicas y datos de aseguradoras; volumen del bazo |
| Pompe | 6 (y 3 compartidos con otras enfermedades) | Myo-Guide: 116 pacientes con Pompe en un modelo de 34 centros; movimiento del diafragma |
| Mucopolisacaridosis y mucolipidosis | 12 | Edad ósea con herramienta externa; reconocimiento facial; perfiles de glucosaminoglucanos |
| Leucodistrofia metacromática | 3 | Desmielinización con cohorte de prueba independiente; función motora a partir de vídeo |
| Otras: GM1, CLN3, aspartilglucosaminuria, sialidosis y un panel de varias EDL | 5 | Estudios pequeños, sin validación externa |
| Estudios que abarcan varias enfermedades | 3 | Respuesta a chaperonas (Gaucher, Fabry y Pompe); cribado neonatal con herramientas posanalíticas (Krabbe y Pompe; Pompe y MPS I), que no son aprendizaje automático en sentido estricto |

**Validación:** solo cuatro estudios se probaron con datos externos:

- dos modelos propios probados en otro hospital, con 31 y 15 casos;
- dos herramientas desarrolladas con otros datos y evaluadas en pacientes lisosomales.

Ninguno midió su efecto sobre la atención.

**Sin ningún estudio de IA encontrado:**

- Krabbe fuera del cribado neonatal, Farber, déficit de lipasa ácida lisosomal, picnodisostosis, Danon y cistinosis;
- MPS IVB, VII y IX;
- fucosidosis y galactosialidosis.

**Lagunas transversales:**

- predicción de respuesta al tratamiento;
- grandes modelos de lenguaje en pacientes;
- aprendizaje federado en enfermedades lisosomales;
- electrocardiograma con IA en Fabry;
- ensayos registrados de herramientas de IA en Fabry o Pompe.

**Evidencia complementaria y metodológica:** 71 referencias reunidas (33 de E3 y 38 de E4). Entran en el manuscrito 27, elegidas por apoyar una afirmación concreta.

**Cambios de clasificación al leer los textos completos:**

- Myo-Guide (40275674) pasa de evidencia complementaria a directa: incluye 116 pacientes con Pompe, con un 70 % a 80 % de aciertos.
- Las dos publicaciones de mucopolisacaridosis de Abu Dabi (40770294 y 41593722) usan los mismos 37 pacientes; se presentan como una sola evidencia.

# 3. Discrepancias encontradas entre resumen y texto completo

Se corrigieron en el manuscrito o se evitaron.

| Estudio | Problema | Cómo queda en el manuscrito |
|---|---|---|
| Wilson 2023, Gaucher (37689674) | El resumen dice «10-20 veces más eficiente»; con las cifras del artículo sale entre 7,2 y 17,2 veces | Se dan las cifras absolutas (1.204 frente a 20.743) |
| Jefferies 2021, Fabry (34930374) | El «23,9 veces» se refiere a una prevalencia supuesta de 1 por 50.000 | Se da la prevalencia proyectada: 1 por 2.090 |
| Hahn 2025, Fabry (40587431) | El 88,12 % que los autores llaman sensibilidad es un AUC; el resumen dice 33 pacientes y el texto 46 | No se cita en el manuscrito |
| Lobel 2024, Fabry (38187171) | El título dice «validated», pero solo hay validación interna | Figura como interna |
| van der Veen 2020, Fabry (32806627) | La cohorte de Münster no pudo validar el modelo por diferencias en la medición de lyso-Gb3 | Se usa como ejemplo de falta de armonización |
| Valero-Tena 2023, Gaucher (37250646) | El documentalista dio por mejor el modelo B; el texto completo dice que fue el A | Se describen solo los predictores, sin AUC |
| Lin 2023, Pompe (37153672) | La «especificidad» del 18,27 % es un valor predictivo (19 de 104) | Se dan las cifras absolutas |
| Uryu 2022, Fabry (36186840) | Solo hay 3 pacientes; los 125.000 fragmentos de entrenamiento salen de uno solo | Se usa como ejemplo de imágenes frente a pacientes |
| Chen 2024, Fabry (38706878) | F1 de 0,846 en el resumen y de 0,861 en el texto | Se usa el AUC, que coincide en ambos |

# 4. Síntesis de las barreras metodológicas

La desarrollan la sección «Los retos de entrenar modelos de IA en enfermedades raras» (632 palabras, la más larga del artículo) y la tabla 2.

| Barrera | Base | Ejemplos del propio mapa |
|---|---|---|
| Pocos pacientes y sobreajuste | van der Ploeg 2014; Vabalas 2019 | Sedimento urinario con un solo paciente de entrenamiento; espectroscopia con 100 % de exactitud en 47 pacientes |
| Heterogeneidad | Grabowski 2015 (Gaucher); Kroos 2007 (Pompe) | Modelo de anticuerpos solo en varones con Fabry clásica |
| Geografía y demografía (desarrollada con especial detalle, como pediste) | Subtipos de MPS por país; variantes de *IDUA* por región; origen de las bases de datos de IA; sesgo europeo de la genética; sesgo por el uso del gasto como indicador de enfermedad | Face2Gene: 0 % de acierto en primera opción para Morquio IVA en Colombia; 80 % frente a 37 % de reconocimiento del síndrome de Down según la ascendencia |
| Desequilibrio de clases | Saito 2015; van den Goorbergh 2022 | Fabry: AUC 0,82 y 1 caso por 2.090 personas; Pompe: 19 de 104 historias señaladas |
| Fragmentación de los datos y aprendizaje federado | Mistry 2022; Aymé 2015; Pati 2022 (71 centros); Rieke 2020 | Ningún estudio federado en enfermedades lisosomales |
| Validación externa y prospectiva | Yu 2022 (81 % pierde rendimiento fuera); Kim 2019 (6 % con validación externa) | 4 de 59 estudios |
| Calidad y armonización | Orlhac 2022 (efecto del equipo de imagen); Monda 2023 (clasificación de variantes de *GLA*) | Medición de lyso-Gb3 en la cohorte de Münster |

# 5. Índice definitivo y palabras

El texto tiene **2.495 palabras**, dentro del margen orientativo de 2.000 a 2.500. El resumen tiene 227 y el abstract 200.

| Sección | Palabras |
|---|---|
| Introducción (incluye un párrafo de método) | 226 |
| Qué es y qué no es la inteligencia artificial | 253 |
| Detección y diagnóstico precoz | 285 |
| Imagen médica y patología digital | 304 |
| Genética, biomarcadores y ómicas | 238 |
| Pronóstico, tratamiento y seguimiento | 187 |
| Los retos de entrenar modelos de IA en enfermedades raras | 632 |
| Otras aplicaciones prometedoras | 177 |
| Conclusiones (qué está demostrado, qué es prometedor y qué falta) | 193 |

# 6. Figuras y tablas finales

- **Figura 1. Cómo aprende y cómo se valida un modelo.**
  - Panel A: los cinco pasos, desde los datos hasta la evaluación clínica, y dónde se detiene la mayoría de los estudios.
  - Panel B: el sobreajuste, con una simulación didáctica reproducible y declarada como tal. El modelo sencillo acierta 21 de 24 casos de entrenamiento y 21 de 24 nuevos; el sobreajustado acierta 24 de 24 y 17 de 24.
- **Figura 2. La IA en el recorrido del paciente.**
  - Seis etapas, de la sospecha al seguimiento, por tres niveles de evidencia: directa, complementaria y potencial.
  - Cada nivel lleva color y, además, textura (relleno liso, rayado o discontinuo), de modo que se distingue sin depender del color. La paleta se comprobó con un validador de daltonismo.
- **Tabla 1. Estudios representativos.**
  - 15 estudios de 8 enfermedades o grupos.
  - Columnas: enfermedad, problema clínico, datos y país, técnica y su tipo (estadística convencional, aprendizaje automático o aprendizaje profundo), tamaño de muestra, resultado y validación.
  - Un estudio solo pudo leerse en resumen y está marcado con asterisco.
- **Tabla 2. Dificultades y estrategias.**
  - Siete filas, cada una con un ejemplo del propio mapa y una estrategia con sus límites.

Las figuras se han dibujado mediante programación, son originales y no se han generado con IA de imágenes. Se entregan en PDF vectorial y en JPG.

# 7. Qué ha entrado y qué se ha dejado fuera

**Entra:**

- estudios con resultado verificable y relevancia clínica;
- todos los que tienen validación externa;
- un ejemplo por enfermedad cuando no hay más;
- los trabajos de frontera que enseñan algo, nombrando el método.

**Queda fuera:**

- estudios sin cifras en el resumen y sin texto abierto (salvo para mencionar que existen);
- preprints con versión publicada;
- estudios in silico sin conexión clínica (varios de variantes de *IDUA*, *GALNS* o *SGSH*);
- trabajos de cribado neonatal sin componente de IA;
- el estudio de 40587431, por la confusión entre AUC y sensibilidad;
- la revisión de radiómica con texto asistido por IA;
- el artículo retractado.

**Por extensión:** no hay un apartado por enfermedad. Las enfermedades sin estudios se nombran solo en el mapa, no en el manuscrito.

# 8. Crítica como revisor externo (fase 5)

## Fortalezas

- Responde a una pregunta útil para el lector de la revista y lo hace con un tono crítico, sin triunfalismo.
- Distingue en todo el texto entre estadística convencional, aprendizaje automático y aprendizaje profundo, y entre evidencia directa, complementaria y potencial.
- La sección de retos tiene peso propio, con ejemplos tomados de la misma literatura lisosomal.
- Cifras absolutas en lugar de solo AUC.
- Transparencia sobre las fuentes no consultadas.

## Problemas mayores

1. **Número de referencias.**
   - Situación: 99 referencias para 2.495 palabras. Las revisiones del número 10 de la revista citan entre 19 y 27.
   - Por qué importa: aunque las normas no fijan un límite, un editor puede pedir recortar.
   - Propuesta: bajar a unas 50-60 trasladando la tabla completa de los 59 estudios a un material suplementario, si la revista lo acepta (hay que preguntarlo a la redacción).
   - Si no lo acepta, candidatos a eliminar: las cinco citas de cuantificación del párrafo de imagen, los estudios pequeños de genética y una de cada pareja de referencias metodológicas que apoyan lo mismo.
2. **No es una revisión sistemática.**
   - Se consultó una sola base bibliográfica principal y la selección no se hizo por duplicado.
   - El texto lo dice, pero un revisor puede pedir el número de registros cribados. Propuesta: añadir esa cifra si lo piden; está en los archivos de datos.
3. **Elaboración asistida por IA.**
   - La búsqueda, la extracción de datos y la redacción se hicieron con un asistente de IA.
   - La revista no tiene política escrita, pero el ICMJE exige declararlo y que los autores respondan de todo el contenido.
   - En la primera parte del Word hay una declaración propuesta.
   - Los autores deberían leer al menos los estudios de la tabla 1 y las cifras citadas.
4. **Fecha de búsqueda.**
   - Se buscó hasta el 16 de noviembre de 2026, no hasta el 31 de diciembre como pedía el encargo.
   - Propuesta: repetirla antes del envío con las mismas herramientas (`herramientas/pm.py`).

## Problemas menores

- La tabla 1 combina estudios con y sin texto completo. Solo uno se leyó únicamente en resumen (39245415, marcado con asterisco).
- Comprobar las palabras clave en DeCS (descriptores en español). Los términos usados son los habituales, pero no se han comprobado en línea.
- Las tablas usan Arial de 9 puntos para que quepan en horizontal. Las normas piden Arial 11 para el documento y doble espacio en las tablas, que sí se aplica. Si la redacción exige 11 puntos también en las tablas, ocuparán más páginas.
- La revisión de Platt et al. (2018), referencia 1, tiene dos correcciones publicadas en PubMed. Las cifras citadas (más de 70 enfermedades; 1 de cada 5.000 nacidos vivos) proceden del resumen, pero conviene comprobar que no las afectan.
- Rellenar los campos de la primera parte: autores, filiación, correspondencia, financiación y conflictos de intereses.

## Lo que se corrigió durante esta revisión

- Recuento de estudios y de validaciones externas: de «tres» a «dos más dos», con la diferencia explicada.
- AUC del estudio óseo de Gaucher, que no correspondía al modelo correcto.
- Afirmación sobre lyso-Gb3, que contradecía el modelo de anticuerpos.
- Formulación sobre AlphaMissense.
- «10 veces más casos» pasa a «más de 10 veces más eventos por variable».
- Abreviatura «[AUC]», que se confundía con una cita.
- Numeración de las referencias de las tablas según el ICMJE.
- Extensión por debajo de 2.500 palabras.
