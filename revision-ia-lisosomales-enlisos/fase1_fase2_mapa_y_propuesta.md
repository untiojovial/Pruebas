# Inteligencia artificial en las enfermedades de depósito lisosomal

Documento de trabajo para la revisión destinada a en-LISOS. Fase 1 (mapa de evidencia) y Fase 2 (propuesta editorial). Fecha de la búsqueda: 16 de noviembre de 2026. Pendiente de validación antes de redactar el manuscrito.


## 1. Resumen

- La evidencia directa existe, pero es joven y pequeña: 45 estudios originales nucleares en enfermedades lisosomales (9 en Gaucher, 21 en Fabry, 5 en Pompe, 9 en otras y 1 que abarca las tres principales), casi todos retrospectivos y con decenas de pacientes.
- Solo dos estudios tienen validación externa en una cohorte de la enfermedad: un clasificador de resonancia cardíaca en Fabry y una herramienta de edad ósea validada en mucopolisacaridosis y alfa-manosidosis.
- Donde hay más trabajo: cribado en historias clínicas electrónicas (Gaucher, Fabry, Pompe, mucopolisacaridosis) e imagen o patología digital (corazón, riñón, cerebro y retina en Fabry; bazo y hueso en Gaucher; diafragma y músculo en Pompe).
- Donde casi no hay nada: predicción de respuesta al tratamiento, modelos de lenguaje (ChatGPT y similares) aplicados a pacientes lisosomales, ensayos clínicos con IA y biomarcadores clásicos (lyso-Gb1, lyso-Gb3) integrados en modelos validados.
- Ninguna herramienta ha demostrado mejorar resultados clínicos, y no hemos encontrado ninguna autorizada como producto sanitario para una enfermedad lisosomal.
- Recomendación editorial: una revisión narrativa crítica con búsqueda estructurada, ordenada por el recorrido del paciente y con tres niveles de evidencia (directa, otras enfermedades raras, extrapolación). Unas 2.500 palabras, 2 figuras y 2 tablas.


## 2. Cómo se hizo la búsqueda

Seis documentalistas automáticos (modelo Haiku, razonamiento medio) trabajaron en paralelo, cada uno con un ámbito: Gaucher; Fabry (corazón e imagen); Fabry (resto); Pompe y otras lisosomales; otras enfermedades raras (evidencia transferible); marcos metodológicos, registros y preprints. Después verifiqué cada referencia contra PubMed.

| Fuente | Estado | Detalle |
|---|---|---|
| PubMed/MEDLINE | Consultada | Más de 90 consultas con términos libres y MeSH por enfermedad y por técnica (16/11/2026). |
| Europe PMC (preprints) | Consultada | medRxiv, bioRxiv, Research Square y Preprints.org. Identificados como no revisados por pares. |
| ClinicalTrials.gov | Consultada | Diez consultas por enfermedad y técnica. |
| Embase, Scopus, Web of Science, Cochrane Library | NO consultadas | Requieren suscripción institucional y no tengo acceso. Conviene que alguien con acceso repita las consultas principales. |
| Google Scholar | NO consultada | No admite búsqueda automatizada. El encargo la preveía solo como complemento. |
| Otros registros de ensayos (EU CTR, ISRCTN) | NO consultados | Pendiente si se quiere exhaustividad en el apartado de estudios en marcha. |

Verificación. Se recogieron 190 registros: 162 con PMID (146 distintos) y 28 preprints o registros de ensayos. Los 146 PMID existen en PubMed y coinciden en título, primer autor y año con lo que anotaron los documentalistas. Cada estudio lleva una cita literal del resumen, y comprobé por programa que esa cita aparece en el resumen de PubMed. Leí yo mismo los resúmenes completos de los cinco estudios más influyentes. Una consulta amplia sobre Fabry devolvió 98 resultados y el documentalista solo revisó 60; revisé los restantes y todos eran de óptica (interferómetros de Fabry-Pérot), sin relación con la enfermedad.

Límites de la verificación. Los datos proceden de los resúmenes, no de los textos completos. Antes de redactar hay que leer el texto completo de los estudios que entren en las tablas, sobre todo donde el resumen no da el tamaño de muestra o el tipo de validación. La búsqueda llega al 16 de noviembre de 2026, no al 31 de diciembre; habrá que repetirla antes del envío.


## 3. Mapa de evidencia: qué hay en cada enfermedad

Cada casilla indica el número de estudios originales nucleares y el mejor grado alcanzado. Grados: A, validación externa en una cohorte de la enfermedad; B, prueba independiente o cohorte de al menos 50 pacientes con validación interna; C, prueba de concepto; D, in silico o preclínico. Los grados los he asignado yo a partir de los resúmenes y son provisionales.

| Aplicación | Gaucher | Fabry | Pompe | Otras lisosomales |
|---|---|---|---|---|
| Sospecha y diagnóstico precoz (historia clínica, lenguaje natural, cribado) | 3 (mejor: B) | 7 (mejor: B) | 1 (mejor: C) | 1 (mejor: C) |
| Genética e interpretación de variantes | 1 (mejor: D) | 2 (mejor: D) | 1 (mejor: D) | 1 (mejor: D) |
| Biomarcadores y ómicas | 1 (mejor: D) | 3 (mejor: C) | — | 1 (mejor: C) |
| Imagen y patología digital | 3 (mejor: C) | 7 (mejor: A) | 3 (mejor: C) | 5 (mejor: A) |
| Pronóstico y estratificación | 2 (mejor: C) | 2 (mejor: C) | 1 (mejor: C) | — |
| Tratamiento y monitorización | — | 1 (mejor: B) | — | — |
| IA generativa y modelos de lenguaje | — | — | — | — |
| Investigación clínica y fármacos | — | — | — | 1 (mejor: D) |

El estudio de respuesta a chaperonas (PMID 34529671) cuenta en las tres enfermedades. En IA generativa no hay ningún estudio original con pacientes lisosomales: solo una demostración de una plataforma de modelización farmacológica con un modelo de lenguaje (PMID 41159846) y un editorial sobre «alucinaciones» de ChatGPT con Pompe como ejemplo (PMID 36811129).


## 4. Estudios nucleares (evidencia directa)

Tabla de trabajo, base de la futura Tabla 1 del artículo (que será más corta). «No consta» significa que el resumen no da el dato.


### Enfermedad de Gaucher

| Estudio | Aplicación | Datos y muestra | Modelo | Resultado principal | Grado | Lectura crítica |
|---|---|---|---|---|---|---|
| Cebolla et al., Int J Mol Sci 2024 (PMID 39201273) | Biomarcadores y ómicas | Estudio in silico; tamaño de cohorte de pacientes no consta en el resumen. | Modelos matemáticos en el sistema Therapeutic Performance Mapping System (TPMS) más una estrategia de… | 18 candidatos; se destacan PDGFB, IL1R2, PTH y CCL3 (MIP-1α). Métricas de rendimiento no consta en el resumen. | D | Modelización in silico de candidatos a biomarcador óseo; sin validación en pacientes. |
| Azuri et al., J Clin Med 2023 (PMID 37629403) | Imagen y patología digital | Conjunto de prueba de 20 pacientes con GD; tamaño de entrenamiento no consta en el resumen. | Deep learning para segmentación esplénica (el resumen no especifica arquitectura). | Error medio 3,6 ± 2,7% con deep learning frente a 13,9 ± 9,6% con la fórmula. | C | Volumen esplénico por aprendizaje profundo; conjunto de prueba de 20 pacientes. Mejora el error frente a la fórmula habitual. |
| Yu et al., Bone 2024 (PMID 38834102) | Imagen y patología digital | 364 imágenes T1w anotadas manualmente para entrenamiento (176 columna, 188 fémur); modelos aplicados a 917 imágenes T1w de la base del estudio Gaucherite (Reino Unido). | Dos modelos U-Net independientes (columna y fémur) para segmentar osteonecrosis y médula no afectada. | No se encontró correlación fuerte entre los parámetros y el bone marrow burden score; la esplenectomía se asocia con la fracción de osteonecrosis y el retraso de tratamiento con los valores cuantificados.… | C | Segmentación de osteonecrosis (cohorte Gaucherite). Sin métricas de segmentación en el resumen y sin correlación fuerte con la puntuación de carga medular. |
| Sharma et al., J Biomech 2016 (PMID 27109052) | Imagen y patología digital | 20 pacientes con GD1 y 10 controles sanos; micro-RM del radio distal. | PCA y SVM (análisis predictivo), junto a modelos lineales generales. | Discriminación GD vs. controles: precisión máxima 73%; AUC 0,79. | C | 20 pacientes y 10 controles; AUC 0,79. Estudio antiguo (2016) y pequeño. |
| Andrade-Campos et al., Orphanet J Rare Dis 2020 (PMID 32962737) | Pronóstico y estratificación | 358 pacientes del registro español (340 GD1, 18 GD3). | Redes de correlación y análisis con árboles de decisión. | La esplenectomía previa se correlaciona con complicaciones óseas (p = 0,005); IgG > 1750 mg/dL y edad > 60 años con cáncer. En el árbol de decisión, los pacientes con diagnóstico y terapia tardíos son los más… | C | Registro español (358 pacientes). Árbol de decisión exploratorio: describe factores asociados, no da rendimiento predictivo ni validación. |
| Valero-Tena et al., Front Med (Lausanne) 2023 (PMID 37250646) | Pronóstico y estratificación | 441 estudios de RM digitalizados de 131 pacientes (69 varones, 62 mujeres), con reevaluación por radiólogo experto cegado. | Random forest. | El random forest identificó como factores más importantes el grado de infiltración medular, la edad al inicio de la terapia y la infiltración femoral. Métricas de rendimiento no consta en el resumen. | C | 441 resonancias de 131 pacientes. El bosque aleatorio ordena variables por importancia; el resumen no da métricas de predicción. |
| Tenenbaum et al., J Clin Epidemiol 2024 (PMID 39245415) | Sospecha y diagnóstico precoz | Base Maccabi Healthcare Services (1998-2022, ~2,6 millones de pacientes): 264 pacientes con GD y 3.429 controles emparejados (1:13) por año de nacimiento, sexo y nivel… | Modelo de machine learning (el algoritmo concreto no consta en el resumen). | AUROC 0,95 ± 0,03; AUPRC 0,80 ± 0,08 en prueba; detección mediana 2,78 años antes del diagnóstico clínico (P25-P75: 1,29-4,53). | B | Caso-control en una sola aseguradora (264 casos, 3.429 controles). Prueba interna con el 25 % de los datos; sin validación externa ni prospectiva. Una carta posterior (PMID 39617306) discute sesgos en la importancia de las variables. |
| Wilson et al., Orphanet J Rare Dis 2023 (PMID 37689674) | Sospecha y diagnóstico precoz | Base Optum Integrated Claims-Clinical (2007-2019); tamaño de cohorte no consta en el resumen. | Dos algoritmos de ML: uno basado en la edad de aparición de rasgos (age-based) y otro en la prevalencia de… | Para identificar 28 pacientes diagnosticados con GD: 1.204 (edad) y 2.862 (prevalencia) pacientes a evaluar frente a 20.743 con el algoritmo clínico; eficiencia 10-20 veces mayor. AUC/sensibilidad no consta… | B | Datos de reclamaciones de EE. UU. Mide eficiencia (pacientes a revisar para encontrar 28 diagnosticados), no AUC. Hay un estudio de implementación registrado (NCT05908656). |
| Daykin et al., Mol Genet Metab 2021 (PMID 34663554) | Sospecha y diagnóstico precoz | Más de 100 fotos por cohorte (GD2, GD3 y controles sanos). | Plataforma de reconocimiento facial con IA (algoritmo propietario no detallado en el resumen). | Comparaciones binarias: correctas al menos en 89% de los casos. Multiclase GD2/GD3/controles: precisión media 76,6% frente a 37,7% por azar. | C | Reconocimiento facial en Gaucher tipos 2 y 3 con una plataforma comercial; fotos, no pacientes consecutivos. Utilidad clínica no evaluada. |


### Enfermedad de Fabry

| Estudio | Aplicación | Datos y muestra | Modelo | Resultado principal | Grado | Lectura crítica |
|---|---|---|---|---|---|---|
| Ducatez et al., J Pers Med 2021 (PMID 34575675) | Biomarcadores y ómicas | 66 plasmas de pacientes con Fabry (FFABRY) y 60 controles | Análisis univariante, de sistemas y aprendizaje automático (algoritmo no especificado); modelo predictivo | 86 metabolitos diferencialmente expresados; modelo predictivo con AUC-ROC 0,992 (IC 0,965-1,000) usando 13 metabolitos de consenso | C | Metabolómica: 66 pacientes y 60 controles; AUC 0,992 con 13 metabolitos, sin validación externa (riesgo de sobreajuste). |
| Mahlovanyi et al., Biosens Bioelectron 2025 (PMID 39808991) | Biomarcadores y ómicas | no consta en el resumen | Espectroscopia de evanescencia en fibra infrarroja (FEWS) con estadística y algoritmos de aprendizaje… | ML con alta selectividad para Fabry en el rango Amida A y Amida I (suero) y en residuos α-D-galactosilo (orina); sin cifras en el resumen | C | Espectroscopia infrarroja con aprendizaje automático; el resumen no da tamaño ni cifras. |
| Barretto et al., Orphanet J Rare Dis 2024 (PMID 39390597) | Biomarcadores y ómicas | 47 pacientes con Fabry (todos fenotipo clásico) y 52 controles sanos, de edad similar | Espectroscopia ATR-FTIR con modelo PLS-DA (quimiometría, reconocimiento de patrones; frontera IA) | PLS-DA independiente del género: sensibilidad, especificidad y exactitud 100% | C | Espectroscopia y análisis discriminante (PLS-DA): 100 % de sensibilidad y especificidad en 47 pacientes clásicos y 52 controles. Cifra perfecta en estudio piloto: probable sobreajuste. Frontera de la IA. |
| Hay et al., Int J Mol Sci 2025 (PMID 40565264) | Genética e interpretación de variantes | no consta en el resumen (n de variantes no indicado) | AlphaMissense (aprendizaje automático), EVE, FoldX y ChimeraX (análisis estructural) | Las variantes amenables tienden a preservar la estabilidad; las no amenables se asocian con desestabilización estructural | D | Variantes de GLA con AlphaMissense, EVE y FoldX; análisis computacional de la «amenabilidad» a chaperonas. |
| Chen et al., Int J Biomed Imaging 2024 (PMID 38706878) | Imagen y patología digital | Numero de pacientes no consta en el resumen. Prueba interna: TVGH; prueba externa: TCVGH; ademas un estudio de lectura a ciegas. | MSLVHC (MRI short-axis view LVH classifier), modelo de IA entrenado con cine SAX; el resumen no especifica… | TVGH: F1 0.846, exactitud 0.909, AUC 0.914. TCVGH (externa): F1 0.727, exactitud 0.806, AUC 0.918. | A | Distingue miocardiopatía de Fabry de miocardiopatía hipertrófica en cine de resonancia; prueba externa en un segundo hospital (AUC 0,918). El resumen no da el número de pacientes con Fabry. |
| Smerkous et al., Kidney Int 2024 (PMID 37774924) | Imagen y patología digital | Biopsias de 56 pacientes con Fabry, 15 con diabetes tipo 2, 10 con enfermedad de cambios mínimos y 17 normales | U-Net (variante) con post-procesado de visión por computador | FPW por DL y por técnicos expertos altamente correlacionados y sin diferencia estadística en ningún grupo; Bland-Altman confirma intercambiabilidad; tiempo por biopsia muy reducido | B | Anchura de los pedicelos en microscopía electrónica: concordancia con técnicos expertos en 56 pacientes con Fabry y otros grupos. Automatiza una medida, no diagnostica. |
| Montella et al., Hum Brain Mapp 2024 (PMID 38520360) | Imagen y patología digital | 52 pacientes con Fabry (40.6 +/- 12.6 anos; 28 mujeres) y 58 controles sanos (38.4 +/- 13.4; 28 mujeres), de una sola institucion. | Modelo DenseNet de prediccion de edad cronologica entrenado con RM T1 de 2160 sujetos sanos de 8 fuentes… | Modelo de edad: MAE 4.01 anos, R2 0.90. Fabry frente a controles: brain-PAD 3.1 frente a -0.1 (p = .01). Asociado con FASTEX (B = 0.10, p = .02). | B | «Edad cerebral» por aprendizaje profundo: 52 pacientes y 58 controles de un centro; modelo entrenado con 2.160 sanos. Biomarcador de investigación. |
| Uryu et al., Mol Genet Metab Rep 2022 (PMID 36186840) | Imagen y patología digital | Numero de muestras y de pacientes: no consta en el resumen. | Red neuronal profunda (arquitectura no nombrada) con metodo de amplificacion de imagenes para construir el… | Conjunto de validacion: sensibilidad 0.902 (IC 95% 0.900-0.903); especificidad 0.977 (0.950-0.980); AUC 0.968 (0.964-0.972). | C | Sedimento urinario con red profunda (AUC 0,968 en validación). El resumen no da el número de pacientes; riesgo de que varias imágenes del mismo paciente estén en entrenamiento y validación. |
| Cazzaniga et al., Sci Rep 2026 (PMID 41526641) | Imagen y patología digital | Numero de biopsias y pacientes: no consta en el resumen. Imagenes de lamina completa de biopsias renales. | EfficientNetB2 (clasificacion a nivel glomerular) y SegFormerB4 (segmentacion a nivel de podocito). | Clasificacion: exactitud 79% (EfficientNetB2). Segmentacion: Dice 0.46, IoU 0.37 (SegFormerB4). ZEBRA frente a controles: p < 0.001; correlacion con puntuacion manual rs = 0.66-0.71. | C | Podocitos espumosos en biopsia renal: exactitud 79 % y solapamiento (Dice) de 0,46, modesto. Tamaño muestral no consta en el resumen. |
| Satriano et al., Front Cardiovasc Med 2020 (PMID 33304928) | Imagen y patología digital | 163 pacientes con HVI de etiologia conocida (85 HCM, 30 HTNcm, 30 AFD, 18 CA); fuente de datos: RMC. Tamano de la cohorte Fabry: 30. | Red neuronal feed-forward totalmente conectada entrenada con datos de arquitectura y deformacion miocardica… | Red neuronal con 3D-MDA: AUC 0.94 (sensibilidad 0.92, especificidad 0.90) para HCM frente a los demas grupos. Mejor AUC de umbrales CMR convencionales: 0.70; strain global: AUC < 0.64. | C | 163 pacientes con hipertrofia (30 con Fabry). El AUC de 0,94 es para separar la miocardiopatía hipertrófica de sus imitadores en conjunto, no Fabry en concreto. |
| Li et al., Orphanet J Rare Dis 2025 (PMID 40181436) | Imagen y patología digital | 27 pacientes con Fabry y 27 controles sanos apareados por edad y sexo; estudio retrospectivo de casos y controles. | Analisis de fondo de ojo asistido por IA (diametro, densidad, simetria, bifurcacion, tortuosidad, dimension… | Fabry frente a controles: menor diametro (p = 0.001 arteria central equivalente), menor densidad de area vascular (p < 0.001), menor dimension fractal (p < 0.001), mayor asimetria arteriolar (p = 0.002) y… | C | Microvasculatura retiniana: 27 pacientes y 27 controles; asociación con lesión de pequeño vaso cerebral. |
| Chiorean et al., Nephrol Dial Transplant 2023 (PMID 37061786) | Pronóstico y estratificación | 234 varones con Fabry con 2 o más valores de eGFR separados ≥6 meses (Optum, 2007-2020); cohorte control sin Fabry | Clustering aglomerativo (no supervisado) | 7 clústeres; cinco mostraron declive natural o rápido; inflexión del eGFR en cada clúster | C | Agrupamiento de trayectorias de filtrado glomerular en 234 varones; descriptivo, no predictivo. |
| Sung et al., Front Artif Intell 2026 (PMID 42787413) | Pronóstico y estratificación | 38 pacientes con Fabry de tres hospitales afiliados (Taipei, Tamsui, Hsinchu); estudio retrospectivo; seguimiento mediano 5.3 anos (RIC 2.8-7.1). | Plataforma de aprendizaje profundo (Us2.ai) para medidas ecocardiograficas (LVMi, LVGLS); duracion QRS del… | QRS: 128.21 +/- 31.18 a 139.63 +/- 37.95 ms (p < 0.001). LVGLS: -14.74 a -16.69% (p = 0.067). LVMi sin cambio significativo. Remodelado adverso concordante en 18/38 (47.4%). Distribucion de fenotipos distinta… | C | 38 pacientes, retrospectivo, sin grupo control. La IA mide el ecocardiograma; no hay un modelo predictivo validado. |
| Jefferies et al., Orphanet J Rare Dis 2021 (PMID 34930374) | Sospecha y diagnóstico precoz | Calibración con casi 5000 pacientes con Fabry de HCE; conjunto de prueba: n no consta en el resumen | Herramienta de IA (aprendizaje automático) que extrae patrones fenotípicos longitudinales; el algoritmo… | AUROC 0.82 en prueba fuera de muestra (0.83 hombres; 0.82 mujeres); el 1% de mayor riesgo tiene 23,9 veces más Fabry que la población | B | Calibrado con casi 5.000 pacientes; AUROC 0,82 fuera de muestra. Datos estructurados de EE. UU.; sin evaluación prospectiva ni confirmación diagnóstica de los señalados. |
| Lobel et al., J Rare Dis (Berlin) 2024 (PMID 38187171) | Sospecha y diagnóstico precoz | Entrenamiento: 260 muestras (130 casos, 130 controles). Prueba: 197 muestras independientes (30 casos, 167 controles) | Modelo estadístico de predicción de riesgo (global y dos modelos por sexo); el tipo de modelo no se… | Modelo global: sensibilidad 80%, especificidad 83,8%, VPP 47,1%. Hombres: 75%, 95,8%, VPP 75%. Mujeres: 83,3%, 81,3%, VPP 45,5% | B | Prueba con muestras independientes (30 casos, 167 controles). Es un modelo estadístico de riesgo: está en la frontera de lo que se llama IA. |
| Michalski et al., J Clin Med 2023 (PMID 37240705) | Sospecha y diagnóstico precoz | no consta en el resumen (estudio retrospectivo; n no indicado) | Procesamiento del lenguaje natural para extraer rasgos de la HCE, combinado con un sistema de puntuación… | AUC 0.998 del sistema de puntuación | C | El lenguaje natural extrae rasgos, pero la puntuación es por reglas de expertos. El AUC de 0,998 no se acompaña de la descripción de la cohorte en el resumen; un paciente confirmado. |
| Moynihan et al., Sci Rep 2024 (PMID 38424111) | Sospecha y diagnóstico precoz | HCE de 1,28 millones de pacientes de 3 hospitales de Singapur; línea base de 4 pacientes con Fabry | Análisis de clústeres y visualización (minería de datos no supervisada) | Se identificaron 2 pacientes adicionales con posible Fabry a partir de 4 de partida | C | Agrupamiento no supervisado en 1,28 millones de historias; parte de 4 pacientes y propone 2 más. Prueba de concepto. |
| Hahn et al., PLoS One 2025 (PMID 40587431) | Sospecha y diagnóstico precoz | 33 conjuntos completos de datos de pacientes con Fabry confirmado | IA basada en cuestionario (tipo de algoritmo no consta en el resumen) | Sensibilidad 88,12% para la presencia de Fabry | C | Cuestionario con IA; 33 pacientes; validación cruzada interna. |
| Pankow et al., JMIR AI 2025 (PMID 40874831) | Sospecha y diagnóstico precoz | 3 expertos (5 viñetas); 6 pacientes con Fabry confirmado | Verificador de síntomas con IA; modelo de Fabry ampliado con 5 viñetas clínicas de expertos | Fabry primera sugerencia: 33% (2/6) con la versión optimizada frente a 17% (1/6) con la original; satisfacción mayor en la optimizada | C | Verificador de síntomas; piloto prospectivo con 6 pacientes (2 de 6 frente a 1 de 6). |
| Hilz et al., Orphanet J Rare Dis 2024 (PMID 38982319) | Sospecha y diagnóstico precoz | Base de datos de una aseguradora alemana; cohorte tratada frente a control sin Fabry (n no consta en el resumen) | Regresión logística (frontera IA: modelo estadístico predictivo) | 284 pacientes en la cohorte potencial; sensibilidad 80,4% y especificidad 79,8% en el punto de corte 0,08 | C | Regresión logística sobre datos de una aseguradora alemana: frontera de la IA. Sin confirmación diagnóstica. |
| van et al., Int J Mol Sci 2020 (PMID 32806627) | Tratamiento y monitorización | 120 varones con Fabry clásico tratados con ERT, de tres centros europeos (datos existentes) | Random forest multivariable frente a regresión logística con 3 variables | AUC-ROC 0,77 para random forest; AUC-ROC 0,77 para regresión logística con 3 variables | B | 120 varones de tres centros. El bosque aleatorio no superó a una regresión logística de tres variables (AUC 0,77 ambos): ejemplo útil de que más complejidad no implica más rendimiento. |


### Enfermedad de Pompe

| Estudio | Aplicación | Datos y muestra | Modelo | Resultado principal | Grado | Lectura crítica |
|---|---|---|---|---|---|---|
| Zeng et al., MedComm (2020) 2026 (PMID 41756255) | Imagen y patología digital | 11 Pompe (media 52,2 años) y 11 controles (50,9 años); estudio prospectivo | Segmentación pulmonar con U-Net sobre RT-MRI (50 ms); T1 mapping para fibrosis grasa | Movilidad diafragmática reducida en Pompe frente a controles; movimiento paradójico en 7 de 11 pacientes; sin AUC ni sensibilidad/especificidad en el resumen | C | Resonancia en tiempo real del diafragma con segmentación automática: 11 pacientes y 11 controles, prospectivo. |
| Harlaar et al., Eur Radiol 2022 (PMID 35829785) | Imagen y patología digital | 30 Pompe y 10 controles sanos; 2 RM con 1 año de intervalo; estudio prospectivo | Algoritmo de aprendizaje automático basado en redes neuronales convolucionales para medir movilidad y… | La curvatura diafragmática aumentó en Pompe frente a controles (p = 0,02 en altura) | C | 30 pacientes y 10 controles, prospectivo, un año. La red convolucional mide movilidad y curvatura del diafragma. |
| Chiou et al., Entropy (Basel) 2019 (PMID 33267428) | Imagen y patología digital | 22 niños con Pompe (0,02-54 meses) y 6 controles sanos (2-12 meses); recto femoral y sartorio | Haralick (GLCM) + selección por regresión escalonada + análisis discriminante lineal de Fisher (clasificador… | Exactitud 94,6%; especificidad 100%; sensibilidad 93,2%; AUC 0,98 ± 0,02 | C | Ecografía muscular con textura y análisis discriminante: 22 niños y 6 controles (AUC 0,98). Muestra pequeña y desequilibrada. |
| Claramunt-Molet et al., J Neuroeng Rehabil 2026 (PMID 41803906) | Pronóstico y estratificación | 24 LOPD y 39 controles sanos; seguimiento de 2 años | Selección de variables (modelo lineal mixto, ElasticNet, bootstrap); clustering jerárquico; análisis… | AUC 0,95 del índice Pompe-MDPI frente a 0,84 de la distancia en 6MWT; 46 variables de marcha significativas | C | Índice de marcha en 24 pacientes de inicio tardío (AUC 0,95 frente a 0,84 de la prueba de marcha). Selección de variables y análisis discriminante: frontera de la IA. |
| Lin et al., Front Neurol 2023 (PMID 37153672) | Sospecha y diagnóstico precoz | 350.116 HCE retrospectivas de 5 hospitales (Salzburgo) en 1 mes; 104 pacientes señalados | Sistema de IA de Symptoma (algoritmo no detallado en el resumen) | 19 pacientes clínicamente plausibles tras revisión; especificidad 18,27%; prevalencia estimada 1 de cada 18.427 | C | 350.116 historias de 5 hospitales; 104 señalados y 19 plausibles tras revisión. Los autores llaman «especificidad» (18,27 %) a lo que es un valor predictivo positivo. Sin confirmación enzimática o genética en el resumen. |


### Otras enfermedades lisosomales y estudios transversales

| Estudio | Aplicación | Datos y muestra | Modelo | Resultado principal | Grado | Lectura crítica |
|---|---|---|---|---|---|---|
| Kadali et al., Mol Cell Biochem 2019 (PMID 30903511) · Mucopolisacaridosis | Biomarcadores y ómicas | 60 casos MPS positivos; GAG por electroforesis 2D y LC-MS/MS | CART (árbol de clasificación y regresión) sobre perfiles de GAG | Exactitud 96,3% (cualitativo) y 98,3% (cuantitativo) en el diagnóstico diferencial | C | Árbol de clasificación sobre glucosaminoglucanos en 60 casos; sin validación descrita. |
| Woodard et al., PLoS Comput Biol 2021 (PMID 34529671) · Gaucher, Fabry y Pompe | Genética e interpretación de variantes | Conjuntos de datos de variantes de Fabry y Pompe; tres variantes de Gaucher para predicción (tamaño total no consta en el resumen). | Un árbol de decisión único y un enfoque de ML avanzado (nombre no consta en el resumen), entrenados con el… | Predicción correcta de la respuesta de tres variantes de GD; predicciones para variantes no probadas. Métricas no consta en el resumen. | D | Predice la respuesta a chaperonas farmacológicas a partir de la estructura proteica; entrenado sobre todo con variantes de Fabry. Trabajo computacional. |
| Mohammed et al., Sci Rep 2024 (PMID 38802532) · Mucopolisacaridosis III | Genética e interpretación de variantes | 415 variantes VUS de NAGLU para entrenamiento; 197 variantes etiquetadas para validación y prueba; 427 para especificidad | Modelo de agrupamiento no supervisado (Bayesian GMM) con características de 8 predictores in silico | Exactitud 0,93; sensibilidad 0,93; especificidad 0,92; AUC 0,908 (frente a 0,885 de AlphaMissense) | D | Predictor de patogenicidad específico de gen (AUC 0,908 frente a 0,885 de AlphaMissense en NAGLU). Computacional. |
| Skaf et al., Front Endocrinol (Lausanne) 2026 (PMID 41727682) · Varias (MPS, alfa-manosidosis) | Imagen y patología digital | 1138 radiografías de mano de varios centros (cohorte 2 = LSD) | Deeplasia (sistema open-source de aprendizaje profundo) frente a 2-5 expertos (método Greulich-Pyle) | Cohorte LSD: MAE 7,13 meses; RMSE 9,56 meses; precisión a 1 año 81,2%; superior a cada experto individual | A | Validación externa de una herramienta general de edad ósea en una cohorte lisosomal: error medio de 7,13 meses. |
| Martin et al., Clin Neuroradiol 2026 (PMID 42012644) · Leucodistrofia metacromática | Imagen y patología digital | 189 escáneres de 35 pacientes para entrenamiento; prueba independiente con 130 escáneres de 49 pacientes | nnU-Net autoconfigurable (CNN) | Dice mediano 0,82 (3D T1) y 0,75 (2D); rS 0,38 con motor; mayor asociación con severidad que el método convencional | B | Segmentación de la desmielinización; prueba independiente con 130 estudios de 49 pacientes (Dice 0,82). |
| Lewis et al., Commun Med (Lond) 2026 (PMID 42410243) · Gangliosidosis GM1 | Imagen y patología digital | 81 RM de 41 pacientes GM1 tipo II y 897 RM de 556 controles | BrainStructuresAges (pipeline de ML) y BSAGE | BSAGE medio 35,50 años (infantil tardío), 21,19 (juvenil), 0,03 (control) | C | «Edad cerebral» en 41 pacientes; biomarcador de investigación. |
| Ruohola et al., Brain Sci 2022 (PMID 36358448) · Aspartilglucosaminuria | Imagen y patología digital | 22 pacientes con AGU y 24 controles sanos | Random forest sobre volumetría de T1, GLSZM de SWI y ratio caudado-tálamo de T2 | Diferenciación con error muy bajo; volúmenes talámicos y varianza de zona talámica con rendimiento excelente (cifras no consta en el resumen) | C | 22 pacientes y 24 controles; bosque aleatorio sobre resonancia. |
| Nonkes et al., JIMD Rep 2021 (PMID 33728252) · CLN3 | Imagen y patología digital | Frotis de sangre periférica de pacientes CLN3 (n = 40 en la validación) | Dos CNN en cascada: segmentación de citoplasma y detección de vacuolas | Correlación con la cuantificación manual r = 0,98 (n = 40) | C | Recuento automático de vacuolas en linfocitos (r = 0,98 con el manual, n = 40). |
| Greenberg et al., Nat Commun 2026 (PMID 42764280) · Mucopolisacaridosis IIIA | Investigación clínica y fármacos | Cultivos corticales derivados de iPSC de niños con MPS IIIA (n no consta en el resumen) | Plataforma multimodal que integra ML, imagen confocal de alto contenido, transcriptómica de núcleo único y… | Al menos nueve compuestos reposicionados que mitigan los efectos adversos en 2 semanas (in vitro) | D | Cribado de fármacos en neuronas derivadas de pacientes con apoyo de aprendizaje automático; preclínico. |
| AlShehhi et al., Sci Rep 2025 (PMID 40770294) · Mucopolisacaridosis | Sospecha y diagnóstico precoz | 115 pacientes ≤19 años (SEHA, 2004-2022) | Varios algoritmos de selección de variables y ML; mejor modelo Naive Bayes; SHAP y LIME | Naive Bayes: exactitud 0,93; AUC 0,96; F1 0,91; MCC 0,86 | C | 115 pacientes de un sistema sanitario; mejor modelo Naive Bayes (AUC 0,96), validación interna. |


## 5. Evidencia en otras enfermedades raras (transferible)

Ninguno de estos resultados se ha demostrado en enfermedades lisosomales. Sirven para ilustrar lo que es técnicamente posible y qué diseño de estudio haría falta.

| Estudio | Tema | Qué aporta y por qué es transferible |
|---|---|---|
| Johnson et al., Sci Transl Med 2024 (PMID 38691621) | Cribado en historias clínicas | Inmunodeficiencia común variable: firma en la historia clínica con validación externa en millones de registros. Modelo de diseño para Gaucher o Fabry. |
| Cohen et al., J Am Med Inform Assoc 2024 (PMID 38134953) | Cribado en historias clínicas | Déficit de AADC: precribado con lenguaje natural; el 22,5 % de los 200 mejor puntuados merecía estudio. |
| Kim et al., J Am Med Inform Assoc 2026 (PMID 41990239) | Lenguaje natural y modelos de lenguaje | Revisión sistemática (27 estudios): casi todo retrospectivo y de un solo centro. |
| Zhao et al., Nature 2026 (PMID 41708847) | Modelos de lenguaje | DeepRare (Nature 2026): sistema con agentes que supera a Exomiser en 168 casos. Aún sin evaluación prospectiva. |
| Reese et al., Eur J Hum Genet 2026 (PMID 41735669) | Modelos de lenguaje | Comparación en 5.213 casos: el mejor modelo de lenguaje acierta el 23,6 %; Exomiser, el 35,5 %. Contrapeso al entusiasmo. |
| Kim et al., Am J Hum Genet 2024 (PMID 39255797) | Modelos de lenguaje | GPT-4 para priorizar genes: por debajo de las herramientas clásicas. |
| Jaech et al., NEJM AI 2026 (PMID 42529462) | Modelos de lenguaje | Reanálisis de genomas no resueltos con apoyo de un modelo de lenguaje: 18 de 376 diagnósticos nuevos. |
| Gurovich et al., Nat Med 2019 (PMID 30617323) | Reconocimiento facial | DeepGestalt: precisión top-10 del 91 % en síndromes genéticos. Relevante para mucopolisacaridosis y Gaucher neuronopático. |
| Reiter et al., J Med Internet Res 2024 (PMID 38477981) | Reconocimiento facial | Validación independiente de tres herramientas faciales. |
| Cheng et al., Science 2023 (PMID 37733863) | Variantes genéticas | AlphaMissense: predicción del efecto de variantes de cambio de aminoácido en todo el proteoma. |
| Lindquist et al., Ophthalmol Sci 2026 (PMID 41492285) | Variantes genéticas | AlphaMissense frente a ClinVar en distrofias de retina: bueno en general, falla en variantes hipomorfas. Aviso para las variantes de inicio tardío de GLA o GAA. |
| Ryan-Phillips et al., Biomedicines 2024 (PMID 39595115) | Estructura de proteínas | ColabFold (AlphaFold) no distinguió de forma fiable variantes patogénicas en síndromes miasténicos. |
| Hostin et al., J Magn Reson Imaging 2023 (PMID 37025028) | Resonancia muscular | Segmentación automática en enfermedades neuromusculares: el rendimiento cae cuando la infiltración grasa supera el 20 %. Directamente relevante para Pompe. |
| Grogan et al., Mayo Clin Proc 2021 (PMID 34218880) | Electrocardiograma | Amiloidosis cardíaca: AUC 0,91 y detección más de 6 meses antes en el 59 %. Referencia para la miocardiopatía de Fabry. |
| Slivnick et al., Eur Heart J 2025 (PMID 40631729) | Ecocardiografía | Amiloidosis a partir de un solo vídeo, con validación externa (AUROC 0,93). |
| Jain et al., JAMA Cardiol 2026 (PMID 41213043) | Implementación | Ensayo no aleatorizado de cribado con IA en amiloidosis por transtiretina: 24 de 50 confirmados. El tipo de estudio que falta en las lisosomales. |
| Lukas et al., BMC Med 2025 (PMID 41137105) | Ensayos clínicos | Controles sintéticos en una enfermedad rara (prueba de concepto). |
| Cortial et al., Front Med (Lausanne) 2024 (PMID 38841574) | Reposicionamiento de fármacos | Revisión: literatura todavía modesta en enfermedades raras. |
| Verdu-Diaz et al., J Cachexia Sarcopenia Muscle 2025 (PMID 40275674) | Resonancia muscular | Myo-Guide (2.961 resonancias, 20 enfermedades neuromusculares). El resumen no dice si incluye Pompe: comprobar en el texto completo. |
| Verdú-Díaz et al., Neurology 2020 (PMID 32029545) | Resonancia muscular | Patrones de resonancia muscular en 10 distrofias (976 resonancias). El resumen no menciona Pompe. |


## 6. Marcos metodológicos y regulatorios

| Guía o norma | Para qué tipo de estudio o herramienta | Referencia verificada |
|---|---|---|
| TRIPOD+AI | Modelos de predicción (diagnósticos o pronósticos): cómo comunicarlos. | Collins et al., BMJ 2024 (PMID 38626948) |
| PROBAST+AI | Modelos de predicción: riesgo de sesgo y aplicabilidad. | Moons et al., BMJ 2025 (PMID 40127903) |
| STARD-AI | Estudios de exactitud diagnóstica con IA. | Sounderajah et al., Nat Med 2025 (PMID 40954311) |
| SPIRIT-AI | Protocolos de ensayos clínicos con una intervención de IA. | Cruz et al., Nat Med 2020 (PMID 32908284) |
| CONSORT-AI | Informes de ensayos clínicos con una intervención de IA. | Liu et al., Nat Med 2020 (PMID 32908283) |
| DECIDE-AI | Evaluación clínica temprana de sistemas de apoyo a la decisión. | Vasey et al., BMJ 2022 (PMID 35584845) |
| CLAIM (actualización de 2024) | IA en imagen médica. | Tejani et al., Radiol Artif Intell 2024 (PMID 38809149) |
| TRIPOD-LLM | Estudios con grandes modelos de lenguaje. | Gallifant et al., Nat Med 2025 (PMID 39779929) |
| FUTURE-AI | Consenso internacional sobre IA fiable y desplegable. | Lekadir et al., BMJ 2025 (PMID 39909534) |
| Reglamento europeo de IA aplicado a la sanidad | Artículo explicativo (NPJ Digit Med 2024). | Busch et al., NPJ Digit Med 2024 (PMID 39134637) |
| Reglamento europeo de IA aplicado a la sanidad | Artículo explicativo (Health Policy 2024). | van et al., Health Policy 2024 (PMID 39244818) |
| Reglamento (UE) 2024/1689 (Reglamento de IA) | Sistemas de IA de alto riesgo, incluidos los que son producto sanitario. | Citar desde EUR-Lex (no verificado aquí). |
| Reglamento (UE) 2017/745 (productos sanitarios) | Software con finalidad médica. | Citar desde EUR-Lex (no verificado aquí). |


## 7. Revisiones previas, preprints y estudios registrados


### Revisiones previas sobre el mismo tema

Ya existen revisiones en inglés. Esto condiciona el enfoque: la aportación de la nuestra sería reunir todas las enfermedades lisosomales, en español, con lectura crítica y para clínicos.

- Spreafico et al., J Med Internet Res 2026 (PMID 41661224): IA y salud digital en enfermedades raras, con las lisosomales como eje.
- Germain et al., Orphanet J Rare Dis 2025 (PMID 40247315): IA en enfermedades raras con Fabry como ejemplo.
- Biddeci et al., Cells 2026 (PMID 42738907): Fabry: fisiopatología, diagnóstico de precisión e IA.
- Moschetti et al., Int J Mol Sci 2025 (PMID 39859472): Pompe: medicina de precisión, genética e IA.
- D'Souza et al., Expert Rev Endocrinol Metab 2022 (PMID 36384353): Rasgos faciales en las enfermedades lisosomales.
- Revisión sobre electrocardiograma con IA en Fabry (PMID 39393622): sin resumen en PubMed; hay que leerla antes de citarla.
- En el número 10 de en-LISOS (octubre de 2026) hay un comentario sobre reposicionamiento de fármacos con IA (sistema ConvAHKG y sebelipasa alfa). Conviene citarlo y no repetirlo.


### Preprints (no revisados por pares)

- Fabry frente a miocardiopatía hipertrófica con datos de electrocardiograma, Holter y ecocardiograma (Research Square 2024, PPR790864): 49 y 100 pacientes, AUC 0,92 en validación cruzada. Sexo y edad figuran entre las variables principales: posible confusión.
- Identificación precoz de ocho enfermedades raras, incluida Fabry, con fenotipado profundo de historias clínicas (medRxiv 2026, PPR1321923).
- Niemann-Pick C1: aprendizaje federado sobre espectros de orina (Research Square 2026, PPR1238314).
- Leucodistrofia metacromática: predicción de actividad enzimática de variantes de ARSA (bioRxiv 2024, PMID 38798479).
- Gangliosidosis GM2 de inicio tardío: segmentación del cerebelo (medRxiv 2025, PMID 40297453).
- CLN3: descubrimiento computacional de biomarcadores (medRxiv 2026, PMID 42145637).


### Estudios registrados

- NCT05908656 (Gaucher): implementación y evaluación de un algoritmo para identificar personas en riesgo en historias clínicas. Falta confirmar en el registro que el algoritmo es de aprendizaje automático.
- NCT07666269 (MOSAIC): IA para clasificar síndromes raros con afectación oral, incluidas mucopolisacaridosis; no iniciado.
- No se encontró ningún ensayo registrado con IA en Fabry ni en Pompe.


## 8. Lagunas de evidencia

- Tratamiento: ningún modelo validado que prediga la respuesta al tratamiento enzimático sustitutivo o a la reducción de sustrato. Lo más cercano: predicción de anticuerpos frente a la enzima en Fabry y de respuesta a chaperonas a partir de la estructura.
- Biomarcadores: ningún modelo validado que integre lyso-Gb1 o CCL18 (Gaucher) o lyso-Gb3 (Fabry). Los estudios ómicos de Fabry son pequeños y sin validación externa.
- Modelos de lenguaje: ningún estudio original en pacientes lisosomales.
- Pompe: sin modelos sobre variantes de GAA, cribado neonatal ni respuesta al tratamiento. Los estudios de marcha, voz y sensores casi no usan IA.
- Fabry: sin estudio original de electrocardiograma con IA, y ecocardiografía con IA solo en una serie de 38 pacientes sin grupo control.
- Gaucher: sin radiómica, sin lenguaje natural sobre notas clínicas y sin variantes de GBA1 enfocadas a Gaucher (la bibliografía de GBA1 está dominada por el párkinson).
- Déficit de lipasa ácida lisosomal, Krabbe y alfa-manosidosis: sin estudios de IA. Déficit de esfingomielinasa ácida: sin modelos propios.
- Validación: casi ningún estudio con validación externa, prospectiva o multicéntrica, y ninguno que mida impacto en resultados clínicos.


## 9. Avisos de calidad para la redacción

- Frontera de la IA: varios trabajos usan regresión logística, análisis discriminante, agrupamiento o puntuaciones por reglas. Propongo incluirlos solo cuando ayuden a explicar un problema clínico, y decir qué son.
- Cifras demasiado buenas en muestras pequeñas (AUC de 0,99 o exactitud del 100 %) deben presentarse como señal de posible sobreajuste, no como rendimiento esperable.
- El estudio de Pompe en historias clínicas llama «especificidad» (18,27 %) a lo que es un valor predictivo positivo (19 de 104). Hay que explicarlo si se cita.
- Las herramientas de resonancia muscular (Myo-Guide y su antecesora) no mencionan Pompe en el resumen: son evidencia transferible salvo que el texto completo diga otra cosa.
- El resumen de una revisión sistemática de radiómica cardíaca (PMID 42793642) contiene la frase «The authors have reviewed and edited the output», propia de un texto preparado con ayuda de IA generativa (es mi interpretación): citar con cautela.
- Un artículo candidato sobre complicaciones renales en Fabry (PMID 37905636, In Vivo 2023) figura como retractado en PubMed y queda excluido.
- Tres registros sin resumen en PubMed no se han podido valorar: una revisión sobre electrocardiograma con IA en Fabry (39393622), una carta sobre detección automática de cuerpos en mora en el sedimento urinario (42066038) y un editorial (36995060).


## 10. Fase 2. Propuesta editorial


### Tres títulos

|  | Título en español | Título en inglés |
|---|---|---|
| 1 (recomendado) | Inteligencia artificial en las enfermedades de depósito lisosomal: qué está demostrado, qué es prometedor y qué falta para llegar a la consulta | Artificial intelligence in lysosomal storage disorders: what is proven, what is promising and what is still missing before clinical use |
| 2 | Aprendizaje automático en las enfermedades de Gaucher, Fabry y Pompe: revisión crítica de la evidencia y de sus limitaciones | Machine learning in Gaucher, Fabry and Pompe disease: a critical review of the evidence and its limitations |
| 3 | Del dato al diagnóstico: aplicaciones de la inteligencia artificial en las enfermedades lisosomales y lecciones de otras enfermedades raras | From data to diagnosis: applications of artificial intelligence in lysosomal diseases and lessons from other rare diseases |

Recomiendo el primero. Responde a la pregunta central, anuncia la clasificación en tres grados de madurez y no promete más de lo que la evidencia permite. El segundo es más clásico, pero deja fuera las mucopolisacaridosis y las leucodistrofias, donde hay estudios sólidos. El tercero es más divulgativo.


### Objetivo y pregunta de revisión

Objetivo: describir y valorar críticamente las aplicaciones de la inteligencia artificial estudiadas en las enfermedades de depósito lisosomal, distinguir lo demostrado de lo extrapolado desde otras enfermedades raras y señalar qué validaciones faltan para su uso asistencial.

Pregunta: ¿cómo contribuyen los modelos de IA y de aprendizaje automático al diagnóstico, la estratificación, el pronóstico y las decisiones terapéuticas en las enfermedades lisosomales, y qué limita su aplicación clínica?


### Enfoque recomendado

- Tipo: revisión narrativa crítica con búsqueda estructurada. No puede presentarse como revisión sistemática: se consultó una sola base bibliográfica principal y la selección no fue por duplicado.
- Hilo conductor: el recorrido del paciente (sospecha, diagnóstico, caracterización, pronóstico, tratamiento y seguimiento), no un catálogo de algoritmos.
- Tres niveles de evidencia visibles en el texto y en las tablas: directa, otras enfermedades raras y extrapolación.
- Cada aplicación se cuenta en el orden problema clínico, herramienta, ejemplo publicado, utilidad y limitación.
- Alcance: Gaucher, Fabry y Pompe como eje, con mucopolisacaridosis, leucodistrofia metacromática y gangliosidosis donde hay estudios sólidos. Pompe tendrá menos peso porque tiene menos evidencia; el texto lo dirá.


### Índice definitivo y palabras por sección

| Sección | Contenido | Palabras |
|---|---|---|
| Resumen y abstract | Estructurados (objetivo, métodos, resultados, conclusiones). No cuentan en el cuerpo. | 250 + 250 |
| 1. Introducción | Enfermedades lisosomales, retraso diagnóstico y dificultad de seguimiento; por qué la IA; objetivo. | 250 |
| 2. Qué es y qué no es la IA | Aprendizaje automático, aprendizaje profundo, lenguaje natural y modelos generativos, con analogías clínicas; entrenar frente a validar. Remite a la Figura 1. | 220 |
| 3. Sospechar antes: historias clínicas y cribado | Gaucher, Fabry, Pompe y mucopolisacaridosis; reconocimiento facial; lecciones de la inmunodeficiencia común variable. | 380 |
| 4. Ver mejor: imagen y patología digital | Corazón, riñón, cerebro y retina en Fabry; bazo y hueso en Gaucher; diafragma y músculo en Pompe; leucodistrofias. | 380 |
| 5. Genes, biomarcadores y ómicas | Variantes y chaperonas; AlphaMissense y sus límites; metabolómica y espectroscopia; lo que falta con lyso-Gb1 y lyso-Gb3. | 260 |
| 6. Pronóstico, tratamiento y seguimiento | Trayectorias renales y óseas; anticuerpos frente a la enzima; marcha y diafragma en Pompe; ausencia de modelos de respuesta. | 260 |
| 7. IA generativa e investigación clínica | Modelos de lenguaje en enfermedades raras (resultados y contrapesos), controles externos y reposicionamiento; todo como evidencia transferible. | 240 |
| 8. Gaucher, Fabry y Pompe frente a frente | Comentario breve de la Tabla 2. | 120 |
| 9. Limitaciones y marco regulatorio | Muestras pequeñas, sobreajuste, falta de validación externa, interoperabilidad y privacidad; guías TRIPOD+AI, STARD-AI, CONSORT-AI y otras; reglamentos europeos. | 260 |
| 10. Conclusiones | Qué está consolidado, qué es prometedor y qué es experimental. | 150 |
| Total del cuerpo |  | ≈ 2.520 |

El total queda en el límite alto del margen orientativo (1.500 a 2.500). Si hay que recortar, las secciones 7 y 8 pueden fundirse.


### Figuras y tablas propuestas

| Elemento | Objetivo | Contenido y estructura | Origen |
|---|---|---|---|
| Figura 1. Cómo aprende y cómo se comprueba un modelo | Que un clínico sin formación técnica entienda entrenamiento, validación interna y validación externa. | Esquema horizontal en tres pasos: datos (historia clínica, analítica, genética, imagen), entrenamiento con casos conocidos, comprobación con pacientes nuevos. Recuadro con los tres errores típicos: muestra pequeña, sobreajuste y falta de validación externa. Sin cifras. | Original, conceptual. |
| Figura 2. La IA en el recorrido del paciente con una enfermedad lisosomal | Mostrar de un vistazo dónde hay evidencia directa y dónde solo extrapolación. | Línea de seis etapas (sospecha, diagnóstico, caracterización, pronóstico, tratamiento, seguimiento). Bajo cada etapa, las aplicaciones estudiadas con un código de tres colores según el nivel de evidencia y las iniciales de la enfermedad. | Original, conceptual. Los colores resumen la Tabla 1; no son resultados experimentales. |
| Tabla 1. Estudios representativos | Dar los datos verificables. | De 12 a 15 filas elegidas del apartado 4: enfermedad, objetivo clínico, datos, modelo, resultado, validación y grado. | Elaboración propia a partir de los estudios citados. |
| Tabla 2. Gaucher, Fabry y Pompe frente a frente | Comparar y señalar lagunas. | Filas: aplicaciones con evidencia, datos usados, mejor nivel de validación, aplicaciones experimentales, lagunas y barreras. Las limitaciones metodológicas y regulatorias (la Tabla 3 del encargo) se integrarían como última fila y en el texto. | Elaboración propia. |

El encargo original pedía tres tablas y dos figuras, y la ampliación pide dos o tres elementos visuales. Las revisiones publicadas en el número 10 de la revista llevan entre dos y cuatro. Propongo cuatro (dos figuras y dos tablas) e integrar la Tabla 3 en la Tabla 2 y en el texto. Si prefieres la Tabla 3 separada, cabe, a costa de texto.


### Normas de la revista: comprobadas

Las instrucciones oficiales están en la página 35 del número 10 (octubre de 2026). Coinciden con las del encargo:

- Revisiones: resumen estructurado, palabras clave, introducción, desarrollo con subtítulos libres y conclusiones.
- Word, Arial 11, doble espacio, cada sección en página nueva. De 3 a 6 palabras clave MeSH o DeCS.
- Citas con números arábigos entre corchetes por orden de aparición; formato ICMJE; seis autores y «et al.».
- Tablas y pies de figura al final, cada una en su página. Figuras en archivos PDF o JPG independientes. Toda la iconografía debe ser original.
- Envío por correo electrónico a la dirección que figura en esas instrucciones.

Diferencias y vacíos respecto al encargo:

- Las normas no fijan número de palabras ni de páginas. Las revisiones del número 10 ocupan de 3 a 5 páginas, así que el objetivo de unas 2.000 a 2.500 palabras es razonable, pero es una estimación.
- El límite de 250 palabras para el resumen aparece solo para los originales. Para las revisiones se pide «resumen estructurado» sin cifra; aplicaré 250.
- El resumen en inglés se exige de forma expresa solo en los originales, pero las revisiones publicadas lo incluyen. Lo incluiré.
- No hay política escrita sobre el uso de IA. En el número 10 hay figuras con la nota «elaborada con asistencia de inteligencia artificial generativa y revisada por los autores». Recomiendo declarar el uso de IA en la preparación del manuscrito, como piden las recomendaciones del ICMJE.


## 11. Lo que necesito que valides antes de redactar

- Título: ¿el 1, el 2 o el 3?
- Alcance: ¿incluimos mucopolisacaridosis, leucodistrofia metacromática y gangliosidosis junto a Gaucher, Fabry y Pompe (mi recomendación), o solo las tres principales?
- Elementos visuales: ¿dos figuras y dos tablas (recomendado), o las tres tablas del encargo original?
- Trabajos en la frontera de la IA (regresión logística, puntuaciones por reglas): ¿los incluimos explicando qué son (recomendado) o los excluimos?
- Bases de datos: ¿alguien con acceso institucional puede repetir la búsqueda en Embase, Scopus y Web of Science? Si no, el manuscrito dirá que la búsqueda se hizo en PubMed, Europe PMC y ClinicalTrials.gov.
- Textos completos: ¿puedes facilitarme los PDF de los estudios de pago que entren en la Tabla 1? Sin ellos, algunos datos quedarán como «no consta».


## Anexo. Referencias verificadas en formato Vancouver

Orden alfabético provisional; la numeración definitiva seguirá el orden de aparición en el manuscrito.

1. AlShehhi A, Alblooshi H, Fadul R, Tumzghi N, Tenaiji AA, Harbi MA, et al. Comparison of machine learning models for mucopolysaccharidosis early diagnosis using UAE medical records. Sci Rep. 2025;15(1):28813. doi:10.1038/s41598-025-13879-3. PMID: 40770294.
2. Andrade-Campos MM, de Frutos LL, Cebolla JJ, Serrano-Gonzalo I, Medrano-Engay B, Roca-Espiau M, et al. Identification of risk features for complication in Gaucher's disease patients: a machine learning analysis of the Spanish registry of Gaucher disease. Orphanet J Rare Dis. 2020;15(1):256. doi:10.1186/s13023-020-01520-7. PMID: 32962737.
3. Azuri I, Wattad A, Peri-Hanania K, Kashti T, Rosen R, Caspi Y, et al. A Deep-Learning Approach to Spleen Volume Estimation in Patients with Gaucher Disease. J Clin Med. 2023;12(16):5361. doi:10.3390/jcm12165361. PMID: 37629403.
4. Barretto CT, Nascimento MHC, Brun BF, da Silva TB, Dias PAC, Silva CAB, et al. Infrared spectroscopy as a new approach for early fabry disease screening: a pilot study. Orphanet J Rare Dis. 2024;19(1):373. doi:10.1186/s13023-024-03380-x. PMID: 39390597.
5. Biddeci G, Spinelli G, Colomba P, Anania M, Duro G, Di Blasi F. Fabry Disease: Integrating Molecular Pathophysiology, Precision Diagnosis, and Artificial Intelligence Toward Precision Medicine. Cells. 2026;15(17):1614. doi:10.3390/cells15171614. PMID: 42738907.
6. Busch F, Kather JN, Johner C, Moser M, Truhn D, Adams LC, et al. Navigating the European Union Artificial Intelligence Act for Healthcare. NPJ Digit Med. 2024;7(1):210. doi:10.1038/s41746-024-01213-6. PMID: 39134637.
7. Cazzaniga G, Carbone M, Barretta R, Casati G, Vatrano S, Gambaro G, et al. Zebra bodies recognition by artificial intelligence (ZEBRA): a computational tool for Fabry nephropathy. Sci Rep. 2026;16(1):5072. doi:10.1038/s41598-026-35466-w. PMID: 41526641.
8. Cebolla JJ, Giraldo P, Gómez J, Montoto C, Gervas-Arruga J. Machine Learning-Driven Biomarker Discovery for Skeletal Complications in Type 1 Gaucher Disease Patients. Int J Mol Sci. 2024;25(16):8586. doi:10.3390/ijms25168586. PMID: 39201273.
9. Chen WW, Kuo L, Lin YX, Yu WC, Tseng CC, Lin YJ, et al. A Deep Learning Approach to Classify Fabry Cardiomyopathy from Hypertrophic Cardiomyopathy Using Cine Imaging on Cardiac Magnetic Resonance. Int J Biomed Imaging. 2024;2024:6114826. doi:10.1155/2024/6114826. PMID: 38706878.
10. Cheng J, Novati G, Pan J, Bycroft C, Žemgulytė A, Applebaum T, et al. Accurate proteome-wide missense variant effect prediction with AlphaMissense. Science. 2023;381(6664):eadg7492. doi:10.1126/science.adg7492. PMID: 37733863.
11. Chiorean A, Lyn N, Kabadi S, Blanchon M, Hayat P, Loustalot P, et al. Cluster analysis of kidney function decline among males with Fabry disease in a large United States electronic health records database. Nephrol Dial Transplant. 2023;38(10):2350-2357. doi:10.1093/ndt/gfad071. PMID: 37061786.
12. Chiou HJ, Yeh CK, Hwang HE, Liao YY. Efficacy of Quantitative Muscle Ultrasound Using Texture-Feature Parametric Imaging in Detecting Pompe Disease in Children. Entropy (Basel). 2019;21(7):714. doi:10.3390/e21070714. PMID: 33267428.
13. Claramunt-Molet M, Pegueroles J, Pi-Cervera A, Rico M, Idelsohn-Zielonka S, Domínguez-González C, et al. Gait analysis reveals new outcome measures for monitoring disease progression in individuals with late-onset Pompe disease. J Neuroeng Rehabil. 2026;23(1):149. doi:10.1186/s12984-026-01898-8. PMID: 41803906.
14. Cohen AM, Kaner J, Miller R, Kopesky JW, Hersh W. Automatically pre-screening patients for the rare disease aromatic l-amino acid decarboxylase deficiency using knowledge engineering, natural language processing, and machine learning on a large EHR population. J Am Med Inform Assoc. 2024;31(3):692-704. doi:10.1093/jamia/ocad244. PMID: 38134953.
15. Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van Calster B, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. BMJ. 2024;385:e078378. doi:10.1136/bmj-2023-078378. PMID: 38626948.
16. Cortial L, Montero V, Tourlet S, Del Bano J, Blin O. Artificial intelligence in drug repurposing for rare diseases: a mini-review. Front Med (Lausanne). 2024;11:1404338. doi:10.3389/fmed.2024.1404338. PMID: 38841574.
17. Cruz Rivera S, Liu X, Chan AW, Denniston AK, Calvert MJ, SPIRIT-AI and CONSORT-AI Working Group, et al. Guidelines for clinical trial protocols for interventions involving artificial intelligence: the SPIRIT-AI extension. Nat Med. 2020;26(9):1351-1363. doi:10.1038/s41591-020-1037-7. PMID: 32908284.
18. D'Souza A, Ryan E, Sidransky E. Facial features of lysosomal storage disorders. Expert Rev Endocrinol Metab. 2022;17(6):467-474. doi:10.1080/17446651.2022.2144229. PMID: 36384353.
19. Daykin E, Fleischer N, Abdelwahab M, Hassib N, Schiffmann R, Ryan E, et al. Investigation of a dysmorphic facial phenotype in patients with Gaucher disease types 2 and 3. Mol Genet Metab. 2021;134(3):274-280. doi:10.1016/j.ymgme.2021.09.008. PMID: 34663554.
20. Ducatez F, Mauhin W, Boullier A, Pilon C, Pereira T, Aubert R, et al. Parsing Fabry Disease Metabolic Plasticity Using Metabolomics. J Pers Med. 2021;11(9):898. doi:10.3390/jpm11090898. PMID: 34575675.
21. Gallifant J, Afshar M, Ameen S, Aphinyanaphongs Y, Chen S, Cacciamani G, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med. 2025;31(1):60-69. doi:10.1038/s41591-024-03425-5. PMID: 39779929.
22. Germain DP, Gruson D, Malcles M, Garcelon N. Applying artificial intelligence to rare diseases: a literature review highlighting lessons from Fabry disease. Orphanet J Rare Dis. 2025;20(1):186. doi:10.1186/s13023-025-03655-x. PMID: 40247315.
23. Greenberg Z, McDonald E, Noreña Puerta A, De Silva MI, Christensen C, Adams R, et al. Drug screen and machine learning predict neuroprotective agents in a preclinical human model of childhood dementia. Nat Commun. 2026;17(1):9980. doi:10.1038/s41467-026-76837-1. PMID: 42764280.
24. Grogan M, Lopez-Jimenez F, Cohen-Shelly M, Dispenzieri A, Attia ZI, Abou Ezzedine OF, et al. Artificial Intelligence-Enhanced Electrocardiogram for the Early Detection of Cardiac Amyloidosis. Mayo Clin Proc. 2021;96(11):2768-2778. doi:10.1016/j.mayocp.2021.04.023. PMID: 34218880.
25. Gurovich Y, Hanani Y, Bar O, Nadav G, Fleischer N, Gelbman D, et al. Identifying facial phenotypes of genetic disorders using deep learning. Nat Med. 2019;25(1):60-64. doi:10.1038/s41591-018-0279-0. PMID: 30617323.
26. Hahn P, Lechner W, Siefen RG, Lampe C, Nordbeck P, Grigull L, et al. Improving a data mining based diagnostic support tool for rare diseases on the example of M. Fabry: Gender differences need to be taken into account. PLoS One. 2025;20(6):e0326372. doi:10.1371/journal.pone.0326372. PMID: 40587431.
27. Harlaar L, Ciet P, van Tulder G, van Kooten HA, van der Beek NAME, Brusse E, et al. MRI changes in diaphragmatic motion and curvature in Pompe disease over time. Eur Radiol. 2022;32(12):8681-8691. doi:10.1007/s00330-022-08940-y. PMID: 35829785.
28. Hay Mele B, Rossetti F, Andreotti G, Cubellis MV, Guerriero S, Monticelli M. Bioinformatics-Driven Multi-Factorial Insight into α-Galactosidase Mutations. Int J Mol Sci. 2025;26(12):5802. doi:10.3390/ijms26125802. PMID: 40565264.
29. Hilz MJ, Lyn N, Marczykowski F, Werner B, Pignot M, Ponce E, et al. Unveiling the untreated: development of a database algorithm to identify potential Fabry disease patients in Germany. Orphanet J Rare Dis. 2024;19(1):259. doi:10.1186/s13023-024-03258-y. PMID: 38982319.
30. Hostin MA, Ogier AC, Michel CP, Le Fur Y, Guye M, Attarian S, et al. The Impact of Fatty Infiltration on MRI Segmentation of Lower Limb Muscles in Neuromuscular Diseases: A Comparative Study of Deep Learning Approaches. J Magn Reson Imaging. 2023;58(6):1826-1835. doi:10.1002/jmri.28708. PMID: 37025028.
31. Jaech A, Cheatham M, Shringarpure SS, Genetti CA, Pradhan P, Bagul A, et al. LLM-Assisted Reanalysis of Unsolved Rare Disease Genomes Increases Diagnostic Yield. NEJM AI. 2026;3(7):10.1056/aics2501343. doi:10.1056/aics2501343. PMID: 42529462.
32. Jain SS, Sun T, Pierson E, Roedan Oliver F, Malta P, Castillo M, et al. Detecting Transthyretin Cardiac Amyloidosis With Artificial Intelligence: A Nonrandomized Clinical Trial. JAMA Cardiol. 2026;11(2):117-124. doi:10.1001/jamacardio.2025.4591. PMID: 41213043.
33. Jefferies JL, Spencer AK, Lau HA, Nelson MW, Giuliano JD, Zabinski JW, et al. A new approach to identifying patients with elevated risk for Fabry disease using a machine learning algorithm. Orphanet J Rare Dis. 2021;16(1):518. doi:10.1186/s13023-021-02150-3. PMID: 34930374.
34. Johnson R, Stephens AV, Mester R, Knyazev S, Kohn LA, Freund MK, et al. Electronic health record signatures identify undiagnosed patients with common variable immunodeficiency disease. Sci Transl Med. 2024;16(745):eade4510. doi:10.1126/scitranslmed.ade4510. PMID: 38691621.
35. Kadali S, Naushad SM, Radha Rama Devi A, Bodiga VL. Biochemical, machine learning and molecular approaches for the differential diagnosis of Mucopolysaccharidoses. Mol Cell Biochem. 2019;458(1-2):27-37. doi:10.1007/s11010-019-03527-6. PMID: 30903511.
36. Kim J, Wang K, Weng C, Liu C. Assessing the utility of large language models for phenotype-driven gene prioritization in the diagnosis of rare genetic disease. Am J Hum Genet. 2024;111(10):2190-2202. doi:10.1016/j.ajhg.2024.08.010. PMID: 39255797.
37. Kim S, Zhou Y, Guo Y, Xiao C, Zheng K. Applying natural language processing and large language models to clinical notes for phenotyping and diagnosing rare diseases: a systematic review. J Am Med Inform Assoc. 2026;33(6):1225-1235. doi:10.1093/jamia/ocag045. PMID: 41990239.
38. Lekadir K, Frangi AF, Porras AR, Glocker B, Cintas C, Langlotz CP, et al. FUTURE-AI: international consensus guideline for trustworthy and deployable artificial intelligence in healthcare. BMJ. 2025;388:e081554. doi:10.1136/bmj-2024-081554. PMID: 39909534.
39. Lewis CJ, Chipman SI, D'Souza P, Johnston JM, Yousef MH, Gahl WA, et al. Brain aging in Type II GM1 gangliosidosis. Commun Med (Lond). 2026;6(1):568. doi:10.1038/s43856-026-01745-w. PMID: 42410243.
40. Li Y, Zhou X, Li J, Zhao Y, Yuan Y, Yang B, et al. Deep learning assisted retinal microvasculature assessment and cerebral small vessel disease in Fabry disease. Orphanet J Rare Dis. 2025;20(1):158. doi:10.1186/s13023-025-03627-1. PMID: 40181436.
41. Lin S, Nateqi J, Weingartner-Ortner R, Gruarin S, Marling H, Pilgram V, et al. An artificial intelligence-based approach for identifying rare disease patients using retrospective electronic health records applied for Pompe disease. Front Neurol. 2023;14:1108222. doi:10.3389/fneur.2023.1108222. PMID: 37153672.
42. Lindquist M, Darrah S, Stafie ST, Mustafi D. Benchmarking AlphaMissense against ClinVar for Diagnostic Interpretation of Missense Variants in Inherited Retinal Diseases. Ophthalmol Sci. 2026;6(2):100997. doi:10.1016/j.xops.2025.100997. PMID: 41492285.
43. Liu X, Cruz Rivera S, Moher D, Calvert MJ, Denniston AK, SPIRIT-AI and CONSORT-AI Working Group. Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension. Nat Med. 2020;26(9):1364-1374. doi:10.1038/s41591-020-1034-x. PMID: 32908283.
44. Lobel CJ, Laney DA, Yang J, Jacob D, Rickheim A, Ogg CZ, et al. FDrisk: development of a validated risk assessment tool for Fabry disease utilizing electronic health record data. J Rare Dis (Berlin). 2024;3(1):2. doi:10.1007/s44162-023-00026-7. PMID: 38187171.
45. Lukas LP, Håkansson S, Tuci M, Torres-Espín A, Rupp R, Taran O, et al. Exploring synthetic controls in rare diseases with a proof of concept in spinal cord injury. BMC Med. 2025;23(1):581. doi:10.1186/s12916-025-04405-3. PMID: 41137105.
46. Mahlovanyi B, Król N, Lopushansky A, Shpotyuk Y, Boussard-Pledel C, Bureau B, et al. Diagnostic and prognostic perspectives of Fabry disease via fiber evanescent wave spectroscopy advanced by machine learning. Biosens Bioelectron. 2025;273:117139. doi:10.1016/j.bios.2025.117139. PMID: 39808991.
47. Martin P, Schaerer J, Cajgfinger T, Delmonte A, Bender B, Whiteman D, et al. Automated Deep Learning-Based Demyelination Load Segmentation in Metachromatic Leukodystrophy. Clin Neuroradiol. 2026;36(3):1009-1021. doi:10.1007/s00062-026-01652-6. PMID: 42012644.
48. Michalski AA, Lis K, Stankiewicz J, Kloska SM, Sycz A, Dudziński M, et al. Supporting the Diagnosis of Fabry Disease Using a Natural Language Processing-Based Approach. J Clin Med. 2023;12(10):3599. doi:10.3390/jcm12103599. PMID: 37240705.
49. Mohammed EEA, Fayez AG, Abdelfattah NM, Fateen E. Novel gene-specific Bayesian Gaussian mixture model to predict the missense variants pathogenicity of Sanfilippo syndrome. Sci Rep. 2024;14(1):12148. doi:10.1038/s41598-024-62352-0. PMID: 38802532.
50. Montella A, Tranfa M, Scaravilli A, Barkhof F, Brunetti A, Cole J, et al. Assessing brain involvement in Fabry disease with deep learning and the brain-age paradigm. Hum Brain Mapp. 2024;45(5):e26599. doi:10.1002/hbm.26599. PMID: 38520360.
51. Moons KGM, Damen JAA, Kaul T, Hooft L, Andaur Navarro C, Dhiman P, et al. PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. BMJ. 2025;388:e082505. doi:10.1136/bmj-2024-082505. PMID: 40127903.
52. Moschetti M, Venezia M, Giacomarra M, Marsana EM, Zizzo C, Duro G, et al. Highlights of Precision Medicine, Genetics, Epigenetics and Artificial Intelligence in Pompe Disease. Int J Mol Sci. 2025;26(2):757. doi:10.3390/ijms26020757. PMID: 39859472.
53. Moynihan D, Monaco S, Ting TW, Narasimhalu K, Hsieh J, Kam S, et al. Cluster analysis and visualisation of electronic health records data to identify undiagnosed patients with rare genetic diseases. Sci Rep. 2024;14(1):5056. doi:10.1038/s41598-024-55424-8. PMID: 38424111.
54. Nonkes LJP, Kuper WFE, Berrens-Hogenbirk K, Musson REA, van Hasselt PM, Huisman A. Automatic quantification of lymphocyte vacuolization in peripheral blood smears of patients with Batten's disease (CLN3 disease). JIMD Rep. 2021;58(1):100-103. doi:10.1002/jmd2.12191. PMID: 33728252.
55. Pankow A, Meißner-Bendzko N, Kaufeld J, Fouquette L, Cotte F, Gilbert S, et al. Medical Expert Knowledge Meets AI to Enhance Symptom Checker Performance for Rare Disease Identification in Fabry Disease: Mixed Methods Study. JMIR AI. 2025;4:e55001. doi:10.2196/55001. PMID: 40874831.
56. Reese JT, Chimirri L, Bridges Y, Danis D, Caufield JH, Gargano MA, et al. Systematic benchmarking demonstrates large language models have not reached the diagnostic accuracy of traditional rare-disease decision support tools. Eur J Hum Genet. 2026;34(4):498-504. doi:10.1038/s41431-026-02054-5. PMID: 41735669.
57. Reiter AMV, Pantel JT, Danyel M, Horn D, Ott CE, Mensah MA. Validation of 3 Computer-Aided Facial Phenotyping Tools (DeepGestalt, GestaltMatcher, and D-Score): Comparative Diagnostic Accuracy Study. J Med Internet Res. 2024;26:e42904. doi:10.2196/42904. PMID: 38477981.
58. Ruohola A, Salli E, Roine T, Tokola A, Laine M, Tikkanen R, et al. Detection of Aspartylglucosaminuria Patients from Magnetic Resonance Images by a Machine-Learning-Based Approach. Brain Sci. 2022;12(11):1522. doi:10.3390/brainsci12111522. PMID: 36358448.
59. Ryan-Phillips F, Henehan L, Ramdas S, Palace J, Beeson D, Dong YY. Assessing the Utility of ColabFold and AlphaMissense in Determining Missense Variant Pathogenicity for Congenital Myasthenic Syndromes. Biomedicines. 2024;12(11):2549. doi:10.3390/biomedicines12112549. PMID: 39595115.
60. Satriano A, Afzal Y, Sarim Afzal M, Fatehi Hassanabad A, Wu C, Dykstra S, et al. Neural-Network-Based Diagnosis Using 3-Dimensional Myocardial Architecture and Deformation: Demonstration for the Differentiation of Hypertrophic Cardiomyopathy. Front Cardiovasc Med. 2020;7:584727. doi:10.3389/fcvm.2020.584727. PMID: 33304928.
61. Sharma GB, Robertson DD, Laney DA, Gambello MJ, Terk M. Machine learning based analytics of micro-MRI trabecular bone microarchitecture and texture in type 1 Gaucher disease. J Biomech. 2016;49(9):1961-1968. doi:10.1016/j.jbiomech.2016.04.010. PMID: 27109052.
62. Skaf K, Fardipour M, Schmidt P, Bolmer E, Keller A, Lampe C, et al. Automated bone age assessment in rare pediatric growth disorders: a comparative study using Deeplasia. Front Endocrinol (Lausanne). 2026;17:1741927. doi:10.3389/fendo.2026.1741927. PMID: 41727682.
63. Slivnick JA, Hawkes W, Oliveira J, Woodward G, Akerman A, Gomez A, et al. Cardiac amyloidosis detection from a single echocardiographic video clip: a novel artificial intelligence-based screening tool. Eur Heart J. 2025;46(40):4090-4101. doi:10.1093/eurheartj/ehaf387. PMID: 40631729.
64. Smerkous D, Mauer M, Tøndel C, Svarstad E, Gubler MC, Nelson RG, et al. Development of an automated estimation of foot process width using deep learning in kidney biopsies from patients with Fabry, minimal change, and diabetic kidney diseases. Kidney Int. 2024;105(1):165-176. doi:10.1016/j.kint.2023.09.011. PMID: 37774924.
65. Sounderajah V, Guni A, Liu X, Collins GS, Karthikesalingam A, Markar SR, et al. The STARD-AI reporting guideline for diagnostic accuracy studies using artificial intelligence. Nat Med. 2025;31(10):3283-3289. doi:10.1038/s41591-025-03953-8. PMID: 40954311.
66. Spreafico AM, Neri L, Angel K, Bellettato CM, Scarpa M. Artificial Intelligence, Connected Care, and Enabling Digital Health Technologies in Rare Diseases With a Focus on Lysosomal Storage Disorders: Scoping Review. J Med Internet Res. 2026;28:e73612. doi:10.2196/73612. PMID: 41661224.
67. Sung KT, Yu WC, Liu ME, Lin PL, Lai YH, Yang HW, et al. AI-assisted longitudinal cardiac phenotyping identifies domain-specific remodeling patterns in Fabry cardiomyopathy. Front Artif Intell. 2026;9:1800355. doi:10.3389/frai.2026.1800355. PMID: 42787413.
68. Takefuji Y. Addressing feature importance biases in machine learning models for early diagnosis of type 1 Gaucher disease. J Clin Epidemiol. 2025;178:111619. doi:10.1016/j.jclinepi.2024.111619. PMID: 39617306.
69. Tejani AS, Klontzas ME, Gatti AA, Mongan JT, Moy L, Park SH, et al. Checklist for Artificial Intelligence in Medical Imaging (CLAIM): 2024 Update. Radiol Artif Intell. 2024;6(4):e240300. doi:10.1148/ryai.240300. PMID: 38809149.
70. Tenenbaum A, Revel-Vilk S, Gazit S, Roimi M, Gill A, Gilboa D, et al. A machine learning model for early diagnosis of type 1 Gaucher disease using real-life data. J Clin Epidemiol. 2024;175:111517. doi:10.1016/j.jclinepi.2024.111517. PMID: 39245415.
71. Uryu H, Migita O, Ozawa M, Kamijo C, Aoto S, Okamura K, et al. Automated urinary sediment detection for Fabry disease using deep-learning algorithms. Mol Genet Metab Rep. 2022;33:100921. doi:10.1016/j.ymgmr.2022.100921. PMID: 36186840.
72. Valero-Tena E, Roca-Espiau M, Verdú-Díaz J, Diaz-Manera J, Andrade-Campos M, Giraldo P. Advantages of digital technology in the assessment of bone marrow involvement in Gaucher's disease. Front Med (Lausanne). 2023;10:1098472. doi:10.3389/fmed.2023.1098472. PMID: 37250646.
73. van der Veen SJ, Vlietstra WJ, van Dussen L, van Kuilenburg ABP, Dijkgraaf MGW, Lenders M, et al. Predicting the Development of Anti-Drug Antibodies against Recombinant alpha-Galactosidase A in Male Patients with Classical Fabry Disease. Int J Mol Sci. 2020;21(16):5784. doi:10.3390/ijms21165784. PMID: 32806627.
74. van Kolfschooten H, van Oirschot J. The EU Artificial Intelligence Act (2024): Implications for healthcare. Health Policy. 2024;149:105152. doi:10.1016/j.healthpol.2024.105152. PMID: 39244818.
75. Vasey B, Nagendran M, Campbell B, Clifton DA, Collins GS, Denaxas S, et al. Reporting guideline for the early stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI. BMJ. 2022;377:e070904. doi:10.1136/bmj-2022-070904. PMID: 35584845.
76. Verdu-Diaz J, Bolano-Díaz C, Gonzalez-Chamorro A, Fitzsimmons S, Warman-Chardon J, Kocak GS, et al. Myo-Guide: A Machine Learning-Based Web Application for Neuromuscular Disease Diagnosis With MRI. J Cachexia Sarcopenia Muscle. 2025;16(3):e13815. doi:10.1002/jcsm.13815. PMID: 40275674.
77. Verdú-Díaz J, Alonso-Pérez J, Nuñez-Peralta C, Tasca G, Vissing J, Straub V, et al. Accuracy of a machine learning muscle MRI-based tool for the diagnosis of muscular dystrophies. Neurology. 2020;94(10):e1094-e1102. doi:10.1212/WNL.0000000000009068. PMID: 32029545.
78. Wilson A, Chiorean A, Aguiar M, Sekulic D, Pavlick P, Shah N, et al. Development of a rare disease algorithm to identify persons at risk of Gaucher disease using electronic health records in the United States. Orphanet J Rare Dis. 2023;18(1):280. doi:10.1186/s13023-023-02868-2. PMID: 37689674.
79. Woodard J, Zheng W, Zhang Y. Protein structural features predict responsiveness to pharmacological chaperone treatment for three lysosomal storage disorders. PLoS Comput Biol. 2021;17(9):e1009370. doi:10.1371/journal.pcbi.1009370. PMID: 34529671.
80. Yu B, Whitmarsh T, Riede P, McDonald S, Kaggie JD, Cox TM, et al. Deep learning-based quantification of osteonecrosis using magnetic resonance images in Gaucher disease. Bone. 2024;186:117142. doi:10.1016/j.bone.2024.117142. PMID: 38834102.
81. Zeng R, Al-Bourini O, Lettermann L, Lettermann L, Olgemöller U, Hofer S, et al. Real-Time MRI With Deep Learning for Efficient Evaluation of Neuromuscular Breathing Impairment. MedComm (2020). 2026;7(3):e70579. doi:10.1002/mco2.70579. PMID: 41756255.
82. Zhao W, Wu C, Fan Y, Qiu P, Zhang X, Sun Y, et al. An agentic system for rare disease diagnosis with traceable reasoning. Nature. 2026;651(8106):775-784. doi:10.1038/s41586-025-10097-9. PMID: 41708847.
