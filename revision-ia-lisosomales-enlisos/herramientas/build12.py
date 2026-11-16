# -*- coding: utf-8 -*-
"""Genera el documento de Fase 1 (mapa de evidencia) y Fase 2 (propuesta editorial) en Markdown y Word, y un CSV con todos los registros."""
import json, csv, re, collections, os
from core import CORE, AREAS, TRANSFER_NM
OUT = '/home/user/Pruebas/revision-ia-lisosomales-enlisos'
d = json.load(open('out/verificado.json', encoding='utf8')); by = {}
for s in d: by.setdefault(s['_v']['pmid'], s)
def vanc(p):
    r = by[p]['_v']['pubmed']; au = r['authors']; a = ', '.join(au[:6]) + (', et al' if len(au) > 6 else '')
    t = r['title'].rstrip('.'); s = f"{a}. {t}. {r['journal']}. {r['year']}"
    if r['volume']: s += f";{r['volume']}" + (f"({r['issue']})" if r['issue'] else '')
    if r['pages']: s += f":{r['pages']}"
    s += '.' + (f" doi:{r['doi']}." if r['doi'] else '') + f" PMID: {p}."
    return s
def short(p):
    r = by[p]['_v']['pubmed']; a = r['authors'][0].split(' ')[0] if r['authors'] else '?'
    return f"{a} et al., {r['journal']} {r['year']} (PMID {p})"
def cut(t, n):
    t = re.sub(r'\s+', ' ', (t or '').replace('NO CONSTA EN EL RESUMEN', 'no consta en el resumen')).strip()
    return t if len(t) <= n else t[:n - 1].rsplit(' ', 1)[0] + '…'
GORD = ['Gaucher', 'Fabry', 'Pompe', 'Otras']
def grp(g): return g if g in ('Gaucher', 'Fabry', 'Pompe') else ('Gaucher, Fabry y Pompe' if g.startswith('Gaucher,') else 'Otras')
B = []   # bloques: ('h1'|'h2'|'p'|'ul'|'table', contenido)
H1 = lambda t: B.append(('h1', t)); H2 = lambda t: B.append(('h2', t)); P = lambda t: B.append(('p', t)); UL = lambda l: B.append(('ul', l)); TB = lambda h, rows, w=None: B.append(('table', (h, rows, w)))

B.append(('title', 'Inteligencia artificial en las enfermedades de depósito lisosomal'))
P('Documento de trabajo para la revisión destinada a en-LISOS. Fase 1 (mapa de evidencia) y Fase 2 (propuesta editorial). Fecha de la búsqueda: 16 de noviembre de 2026. Pendiente de validación antes de redactar el manuscrito.')

H1('1. Resumen')
UL(['La evidencia directa existe, pero es joven y pequeña: 45 estudios originales nucleares en enfermedades lisosomales (9 en Gaucher, 21 en Fabry, 5 en Pompe, 9 en otras y 1 que abarca las tres principales), casi todos retrospectivos y con decenas de pacientes.',
    'Solo dos estudios tienen validación externa en una cohorte de la enfermedad: un clasificador de resonancia cardíaca en Fabry y una herramienta de edad ósea validada en mucopolisacaridosis y alfa-manosidosis.',
    'Donde hay más trabajo: cribado en historias clínicas electrónicas (Gaucher, Fabry, Pompe, mucopolisacaridosis) e imagen o patología digital (corazón, riñón, cerebro y retina en Fabry; bazo y hueso en Gaucher; diafragma y músculo en Pompe).',
    'Donde casi no hay nada: predicción de respuesta al tratamiento, modelos de lenguaje (ChatGPT y similares) aplicados a pacientes lisosomales, ensayos clínicos con IA y biomarcadores clásicos (lyso-Gb1, lyso-Gb3) integrados en modelos validados.',
    'Ninguna herramienta ha demostrado mejorar resultados clínicos, y no hemos encontrado ninguna autorizada como producto sanitario para una enfermedad lisosomal.',
    'Recomendación editorial: una revisión narrativa crítica con búsqueda estructurada, ordenada por el recorrido del paciente y con tres niveles de evidencia (directa, otras enfermedades raras, extrapolación). Unas 2.500 palabras, 2 figuras y 2 tablas.'])

H1('2. Cómo se hizo la búsqueda')
P('Seis documentalistas automáticos (modelo Haiku, razonamiento medio) trabajaron en paralelo, cada uno con un ámbito: Gaucher; Fabry (corazón e imagen); Fabry (resto); Pompe y otras lisosomales; otras enfermedades raras (evidencia transferible); marcos metodológicos, registros y preprints. Después verifiqué cada referencia contra PubMed.')
TB(['Fuente', 'Estado', 'Detalle'], [
    ['PubMed/MEDLINE', 'Consultada', 'Más de 90 consultas con términos libres y MeSH por enfermedad y por técnica (16/11/2026).'],
    ['Europe PMC (preprints)', 'Consultada', 'medRxiv, bioRxiv, Research Square y Preprints.org. Identificados como no revisados por pares.'],
    ['ClinicalTrials.gov', 'Consultada', 'Diez consultas por enfermedad y técnica.'],
    ['Embase, Scopus, Web of Science, Cochrane Library', 'NO consultadas', 'Requieren suscripción institucional y no tengo acceso. Conviene que alguien con acceso repita las consultas principales.'],
    ['Google Scholar', 'NO consultada', 'No admite búsqueda automatizada. El encargo la preveía solo como complemento.'],
    ['Otros registros de ensayos (EU CTR, ISRCTN)', 'NO consultados', 'Pendiente si se quiere exhaustividad en el apartado de estudios en marcha.']], [3.2, 2.2, 10.5])
P('Verificación. Se recogieron 190 registros: 162 con PMID (146 distintos) y 28 preprints o registros de ensayos. Los 146 PMID existen en PubMed y coinciden en título, primer autor y año con lo que anotaron los documentalistas. Cada estudio lleva una cita literal del resumen, y comprobé por programa que esa cita aparece en el resumen de PubMed. Leí yo mismo los resúmenes completos de los cinco estudios más influyentes. Una consulta amplia sobre Fabry devolvió 98 resultados y el documentalista solo revisó 60; revisé los restantes y todos eran de óptica (interferómetros de Fabry-Pérot), sin relación con la enfermedad.')
P('Límites de la verificación. Los datos proceden de los resúmenes, no de los textos completos. Antes de redactar hay que leer el texto completo de los estudios que entren en las tablas, sobre todo donde el resumen no da el tamaño de muestra o el tipo de validación. La búsqueda llega al 16 de noviembre de 2026, no al 31 de diciembre; habrá que repetirla antes del envío.')

H1('3. Mapa de evidencia: qué hay en cada enfermedad')
P('Cada casilla indica el número de estudios originales nucleares y el mejor grado alcanzado. Grados: A, validación externa en una cohorte de la enfermedad; B, prueba independiente o cohorte de al menos 50 pacientes con validación interna; C, prueba de concepto; D, in silico o preclínico. Los grados los he asignado yo a partir de los resúmenes y son provisionales.')
cnt = collections.defaultdict(list)
for p, (g, a, gr, n) in CORE.items():
    for gg in (['Gaucher', 'Fabry', 'Pompe'] if g.startswith('Gaucher,') else [grp(g)]): cnt[(gg, a)].append(gr)
rows = []
for a in ['4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '4.7', '4.8']:
    row = [AREAS[a]]
    for g in GORD:
        v = cnt.get((g, a), []); row.append(f"{len(v)} (mejor: {min(v)})" if v else '—')
    rows.append(row)
TB(['Aplicación', 'Gaucher', 'Fabry', 'Pompe', 'Otras lisosomales'], rows, [6.5, 2.3, 2.3, 2.3, 2.6])
P('El estudio de respuesta a chaperonas (PMID 34529671) cuenta en las tres enfermedades. En IA generativa no hay ningún estudio original con pacientes lisosomales: solo una demostración de una plataforma de modelización farmacológica con un modelo de lenguaje (PMID 41159846) y un editorial sobre «alucinaciones» de ChatGPT con Pompe como ejemplo (PMID 36811129).')

H1('4. Estudios nucleares (evidencia directa)')
P('Tabla de trabajo, base de la futura Tabla 1 del artículo (que será más corta). «No consta» significa que el resumen no da el dato.')
for G, name in (('Gaucher', 'Enfermedad de Gaucher'), ('Fabry', 'Enfermedad de Fabry'), ('Pompe', 'Enfermedad de Pompe'), ('Otras', 'Otras enfermedades lisosomales y estudios transversales')):
    H2(name); rows = []
    for p, (g, a, gr, note) in CORE.items():
        if not ((grp(g) == G) or (G == 'Otras' and g.startswith('Gaucher,'))): continue
        s = by[p]
        rows.append([short(p) + ('' if G != 'Otras' else f" · {g}"), AREAS[a].split(' (')[0], cut(s.get('muestra_y_datos'), 170), cut(s.get('algoritmo'), 110), cut(s.get('resultados_metricas'), 210), gr, note])
    rows.sort(key=lambda r: (r[1], r[5]))
    TB(['Estudio', 'Aplicación', 'Datos y muestra', 'Modelo', 'Resultado principal', 'Grado', 'Lectura crítica'], rows, [2.6, 2.0, 3.0, 2.2, 3.2, 1.2, 4.0])

H1('5. Evidencia en otras enfermedades raras (transferible)')
P('Ninguno de estos resultados se ha demostrado en enfermedades lisosomales. Sirven para ilustrar lo que es técnicamente posible y qué diseño de estudio haría falta.')
TR = [('38691621', 'Cribado en historias clínicas', 'Inmunodeficiencia común variable: firma en la historia clínica con validación externa en millones de registros. Modelo de diseño para Gaucher o Fabry.'),
      ('38134953', 'Cribado en historias clínicas', 'Déficit de AADC: precribado con lenguaje natural; el 22,5 % de los 200 mejor puntuados merecía estudio.'),
      ('41990239', 'Lenguaje natural y modelos de lenguaje', 'Revisión sistemática (27 estudios): casi todo retrospectivo y de un solo centro.'),
      ('41708847', 'Modelos de lenguaje', 'DeepRare (Nature 2026): sistema con agentes que supera a Exomiser en 168 casos. Aún sin evaluación prospectiva.'),
      ('41735669', 'Modelos de lenguaje', 'Comparación en 5.213 casos: el mejor modelo de lenguaje acierta el 23,6 %; Exomiser, el 35,5 %. Contrapeso al entusiasmo.'),
      ('39255797', 'Modelos de lenguaje', 'GPT-4 para priorizar genes: por debajo de las herramientas clásicas.'),
      ('42529462', 'Modelos de lenguaje', 'Reanálisis de genomas no resueltos con apoyo de un modelo de lenguaje: 18 de 376 diagnósticos nuevos.'),
      ('30617323', 'Reconocimiento facial', 'DeepGestalt: precisión top-10 del 91 % en síndromes genéticos. Relevante para mucopolisacaridosis y Gaucher neuronopático.'),
      ('38477981', 'Reconocimiento facial', 'Validación independiente de tres herramientas faciales.'),
      ('37733863', 'Variantes genéticas', 'AlphaMissense: predicción del efecto de variantes de cambio de aminoácido en todo el proteoma.'),
      ('41492285', 'Variantes genéticas', 'AlphaMissense frente a ClinVar en distrofias de retina: bueno en general, falla en variantes hipomorfas. Aviso para las variantes de inicio tardío de GLA o GAA.'),
      ('39595115', 'Estructura de proteínas', 'ColabFold (AlphaFold) no distinguió de forma fiable variantes patogénicas en síndromes miasténicos.'),
      ('37025028', 'Resonancia muscular', 'Segmentación automática en enfermedades neuromusculares: el rendimiento cae cuando la infiltración grasa supera el 20 %. Directamente relevante para Pompe.'),
      ('34218880', 'Electrocardiograma', 'Amiloidosis cardíaca: AUC 0,91 y detección más de 6 meses antes en el 59 %. Referencia para la miocardiopatía de Fabry.'),
      ('40631729', 'Ecocardiografía', 'Amiloidosis a partir de un solo vídeo, con validación externa (AUROC 0,93).'),
      ('41213043', 'Implementación', 'Ensayo no aleatorizado de cribado con IA en amiloidosis por transtiretina: 24 de 50 confirmados. El tipo de estudio que falta en las lisosomales.'),
      ('41137105', 'Ensayos clínicos', 'Controles sintéticos en una enfermedad rara (prueba de concepto).'),
      ('38841574', 'Reposicionamiento de fármacos', 'Revisión: literatura todavía modesta en enfermedades raras.')]
rows = [[short(p), a, n] for p, a, n in TR] + [[short(p), 'Resonancia muscular', n] for p, n in TRANSFER_NM.items()]
TB(['Estudio', 'Tema', 'Qué aporta y por qué es transferible'], rows, [4.0, 3.0, 9.0])

H1('6. Marcos metodológicos y regulatorios')
FR = [('38626948', 'TRIPOD+AI', 'Modelos de predicción (diagnósticos o pronósticos): cómo comunicarlos.'), ('40127903', 'PROBAST+AI', 'Modelos de predicción: riesgo de sesgo y aplicabilidad.'),
      ('40954311', 'STARD-AI', 'Estudios de exactitud diagnóstica con IA.'), ('32908284', 'SPIRIT-AI', 'Protocolos de ensayos clínicos con una intervención de IA.'),
      ('32908283', 'CONSORT-AI', 'Informes de ensayos clínicos con una intervención de IA.'), ('35584845', 'DECIDE-AI', 'Evaluación clínica temprana de sistemas de apoyo a la decisión.'),
      ('38809149', 'CLAIM (actualización de 2024)', 'IA en imagen médica.'), ('39779929', 'TRIPOD-LLM', 'Estudios con grandes modelos de lenguaje.'),
      ('39909534', 'FUTURE-AI', 'Consenso internacional sobre IA fiable y desplegable.'), ('39134637', 'Reglamento europeo de IA aplicado a la sanidad', 'Artículo explicativo (NPJ Digit Med 2024).'),
      ('39244818', 'Reglamento europeo de IA aplicado a la sanidad', 'Artículo explicativo (Health Policy 2024).')]
TB(['Guía o norma', 'Para qué tipo de estudio o herramienta', 'Referencia verificada'], [[n, u, short(p)] for p, n, u in FR] +
   [['Reglamento (UE) 2024/1689 (Reglamento de IA)', 'Sistemas de IA de alto riesgo, incluidos los que son producto sanitario.', 'Citar desde EUR-Lex (no verificado aquí).'],
    ['Reglamento (UE) 2017/745 (productos sanitarios)', 'Software con finalidad médica.', 'Citar desde EUR-Lex (no verificado aquí).']], [5.0, 6.5, 4.5])

H1('7. Revisiones previas, preprints y estudios registrados')
H2('Revisiones previas sobre el mismo tema')
P('Ya existen revisiones en inglés. Esto condiciona el enfoque: la aportación de la nuestra sería reunir todas las enfermedades lisosomales, en español, con lectura crítica y para clínicos.')
UL([short(p) + ': ' + t for p, t in (('41661224', 'IA y salud digital en enfermedades raras, con las lisosomales como eje.'), ('40247315', 'IA en enfermedades raras con Fabry como ejemplo.'), ('42738907', 'Fabry: fisiopatología, diagnóstico de precisión e IA.'),
     ('39859472', 'Pompe: medicina de precisión, genética e IA.'), ('36384353', 'Rasgos faciales en las enfermedades lisosomales.'))] +
   ['Revisión sobre electrocardiograma con IA en Fabry (PMID 39393622): sin resumen en PubMed; hay que leerla antes de citarla.',
    'En el número 10 de en-LISOS (octubre de 2026) hay un comentario sobre reposicionamiento de fármacos con IA (sistema ConvAHKG y sebelipasa alfa). Conviene citarlo y no repetirlo.'])
H2('Preprints (no revisados por pares)')
UL(['Fabry frente a miocardiopatía hipertrófica con datos de electrocardiograma, Holter y ecocardiograma (Research Square 2024, PPR790864): 49 y 100 pacientes, AUC 0,92 en validación cruzada. Sexo y edad figuran entre las variables principales: posible confusión.',
    'Identificación precoz de ocho enfermedades raras, incluida Fabry, con fenotipado profundo de historias clínicas (medRxiv 2026, PPR1321923).',
    'Niemann-Pick C1: aprendizaje federado sobre espectros de orina (Research Square 2026, PPR1238314).',
    'Leucodistrofia metacromática: predicción de actividad enzimática de variantes de ARSA (bioRxiv 2024, PMID 38798479).',
    'Gangliosidosis GM2 de inicio tardío: segmentación del cerebelo (medRxiv 2025, PMID 40297453).',
    'CLN3: descubrimiento computacional de biomarcadores (medRxiv 2026, PMID 42145637).'])
H2('Estudios registrados')
UL(['NCT05908656 (Gaucher): implementación y evaluación de un algoritmo para identificar personas en riesgo en historias clínicas. Falta confirmar en el registro que el algoritmo es de aprendizaje automático.',
    'NCT07666269 (MOSAIC): IA para clasificar síndromes raros con afectación oral, incluidas mucopolisacaridosis; no iniciado.',
    'No se encontró ningún ensayo registrado con IA en Fabry ni en Pompe.'])

H1('8. Lagunas de evidencia')
UL(['Tratamiento: ningún modelo validado que prediga la respuesta al tratamiento enzimático sustitutivo o a la reducción de sustrato. Lo más cercano: predicción de anticuerpos frente a la enzima en Fabry y de respuesta a chaperonas a partir de la estructura.',
    'Biomarcadores: ningún modelo validado que integre lyso-Gb1 o CCL18 (Gaucher) o lyso-Gb3 (Fabry). Los estudios ómicos de Fabry son pequeños y sin validación externa.',
    'Modelos de lenguaje: ningún estudio original en pacientes lisosomales.',
    'Pompe: sin modelos sobre variantes de GAA, cribado neonatal ni respuesta al tratamiento. Los estudios de marcha, voz y sensores casi no usan IA.',
    'Fabry: sin estudio original de electrocardiograma con IA, y ecocardiografía con IA solo en una serie de 38 pacientes sin grupo control.',
    'Gaucher: sin radiómica, sin lenguaje natural sobre notas clínicas y sin variantes de GBA1 enfocadas a Gaucher (la bibliografía de GBA1 está dominada por el párkinson).',
    'Déficit de lipasa ácida lisosomal, Krabbe y alfa-manosidosis: sin estudios de IA. Déficit de esfingomielinasa ácida: sin modelos propios.',
    'Validación: casi ningún estudio con validación externa, prospectiva o multicéntrica, y ninguno que mida impacto en resultados clínicos.'])

H1('9. Avisos de calidad para la redacción')
UL(['Frontera de la IA: varios trabajos usan regresión logística, análisis discriminante, agrupamiento o puntuaciones por reglas. Propongo incluirlos solo cuando ayuden a explicar un problema clínico, y decir qué son.',
    'Cifras demasiado buenas en muestras pequeñas (AUC de 0,99 o exactitud del 100 %) deben presentarse como señal de posible sobreajuste, no como rendimiento esperable.',
    'El estudio de Pompe en historias clínicas llama «especificidad» (18,27 %) a lo que es un valor predictivo positivo (19 de 104). Hay que explicarlo si se cita.',
    'Las herramientas de resonancia muscular (Myo-Guide y su antecesora) no mencionan Pompe en el resumen: son evidencia transferible salvo que el texto completo diga otra cosa.',
    'El resumen de una revisión sistemática de radiómica cardíaca (PMID 42793642) contiene la frase «The authors have reviewed and edited the output», propia de un texto preparado con ayuda de IA generativa (es mi interpretación): citar con cautela.',
    'Un artículo candidato sobre complicaciones renales en Fabry (PMID 37905636, In Vivo 2023) figura como retractado en PubMed y queda excluido.',
    'Tres registros sin resumen en PubMed no se han podido valorar: una revisión sobre electrocardiograma con IA en Fabry (39393622), una carta sobre detección automática de cuerpos en mora en el sedimento urinario (42066038) y un editorial (36995060).'])

H1('10. Fase 2. Propuesta editorial')
H2('Tres títulos')
TB(['', 'Título en español', 'Título en inglés'], [
    ['1 (recomendado)', 'Inteligencia artificial en las enfermedades de depósito lisosomal: qué está demostrado, qué es prometedor y qué falta para llegar a la consulta', 'Artificial intelligence in lysosomal storage disorders: what is proven, what is promising and what is still missing before clinical use'],
    ['2', 'Aprendizaje automático en las enfermedades de Gaucher, Fabry y Pompe: revisión crítica de la evidencia y de sus limitaciones', 'Machine learning in Gaucher, Fabry and Pompe disease: a critical review of the evidence and its limitations'],
    ['3', 'Del dato al diagnóstico: aplicaciones de la inteligencia artificial en las enfermedades lisosomales y lecciones de otras enfermedades raras', 'From data to diagnosis: applications of artificial intelligence in lysosomal diseases and lessons from other rare diseases']], [2.2, 7.0, 6.8])
P('Recomiendo el primero. Responde a la pregunta central, anuncia la clasificación en tres grados de madurez y no promete más de lo que la evidencia permite. El segundo es más clásico, pero deja fuera las mucopolisacaridosis y las leucodistrofias, donde hay estudios sólidos. El tercero es más divulgativo.')
H2('Objetivo y pregunta de revisión')
P('Objetivo: describir y valorar críticamente las aplicaciones de la inteligencia artificial estudiadas en las enfermedades de depósito lisosomal, distinguir lo demostrado de lo extrapolado desde otras enfermedades raras y señalar qué validaciones faltan para su uso asistencial.')
P('Pregunta: ¿cómo contribuyen los modelos de IA y de aprendizaje automático al diagnóstico, la estratificación, el pronóstico y las decisiones terapéuticas en las enfermedades lisosomales, y qué limita su aplicación clínica?')
H2('Enfoque recomendado')
UL(['Tipo: revisión narrativa crítica con búsqueda estructurada. No puede presentarse como revisión sistemática: se consultó una sola base bibliográfica principal y la selección no fue por duplicado.',
    'Hilo conductor: el recorrido del paciente (sospecha, diagnóstico, caracterización, pronóstico, tratamiento y seguimiento), no un catálogo de algoritmos.',
    'Tres niveles de evidencia visibles en el texto y en las tablas: directa, otras enfermedades raras y extrapolación.',
    'Cada aplicación se cuenta en el orden problema clínico, herramienta, ejemplo publicado, utilidad y limitación.',
    'Alcance: Gaucher, Fabry y Pompe como eje, con mucopolisacaridosis, leucodistrofia metacromática y gangliosidosis donde hay estudios sólidos. Pompe tendrá menos peso porque tiene menos evidencia; el texto lo dirá.'])
H2('Índice definitivo y palabras por sección')
TB(['Sección', 'Contenido', 'Palabras'], [
    ['Resumen y abstract', 'Estructurados (objetivo, métodos, resultados, conclusiones). No cuentan en el cuerpo.', '250 + 250'],
    ['1. Introducción', 'Enfermedades lisosomales, retraso diagnóstico y dificultad de seguimiento; por qué la IA; objetivo.', '250'],
    ['2. Qué es y qué no es la IA', 'Aprendizaje automático, aprendizaje profundo, lenguaje natural y modelos generativos, con analogías clínicas; entrenar frente a validar. Remite a la Figura 1.', '220'],
    ['3. Sospechar antes: historias clínicas y cribado', 'Gaucher, Fabry, Pompe y mucopolisacaridosis; reconocimiento facial; lecciones de la inmunodeficiencia común variable.', '380'],
    ['4. Ver mejor: imagen y patología digital', 'Corazón, riñón, cerebro y retina en Fabry; bazo y hueso en Gaucher; diafragma y músculo en Pompe; leucodistrofias.', '380'],
    ['5. Genes, biomarcadores y ómicas', 'Variantes y chaperonas; AlphaMissense y sus límites; metabolómica y espectroscopia; lo que falta con lyso-Gb1 y lyso-Gb3.', '260'],
    ['6. Pronóstico, tratamiento y seguimiento', 'Trayectorias renales y óseas; anticuerpos frente a la enzima; marcha y diafragma en Pompe; ausencia de modelos de respuesta.', '260'],
    ['7. IA generativa e investigación clínica', 'Modelos de lenguaje en enfermedades raras (resultados y contrapesos), controles externos y reposicionamiento; todo como evidencia transferible.', '240'],
    ['8. Gaucher, Fabry y Pompe frente a frente', 'Comentario breve de la Tabla 2.', '120'],
    ['9. Limitaciones y marco regulatorio', 'Muestras pequeñas, sobreajuste, falta de validación externa, interoperabilidad y privacidad; guías TRIPOD+AI, STARD-AI, CONSORT-AI y otras; reglamentos europeos.', '260'],
    ['10. Conclusiones', 'Qué está consolidado, qué es prometedor y qué es experimental.', '150'],
    ['Total del cuerpo', '', '≈ 2.520']], [4.6, 9.6, 1.8])
P('El total queda en el límite alto del margen orientativo (1.500 a 2.500). Si hay que recortar, las secciones 7 y 8 pueden fundirse.')
H2('Figuras y tablas propuestas')
TB(['Elemento', 'Objetivo', 'Contenido y estructura', 'Origen'], [
    ['Figura 1. Cómo aprende y cómo se comprueba un modelo', 'Que un clínico sin formación técnica entienda entrenamiento, validación interna y validación externa.', 'Esquema horizontal en tres pasos: datos (historia clínica, analítica, genética, imagen), entrenamiento con casos conocidos, comprobación con pacientes nuevos. Recuadro con los tres errores típicos: muestra pequeña, sobreajuste y falta de validación externa. Sin cifras.', 'Original, conceptual.'],
    ['Figura 2. La IA en el recorrido del paciente con una enfermedad lisosomal', 'Mostrar de un vistazo dónde hay evidencia directa y dónde solo extrapolación.', 'Línea de seis etapas (sospecha, diagnóstico, caracterización, pronóstico, tratamiento, seguimiento). Bajo cada etapa, las aplicaciones estudiadas con un código de tres colores según el nivel de evidencia y las iniciales de la enfermedad.', 'Original, conceptual. Los colores resumen la Tabla 1; no son resultados experimentales.'],
    ['Tabla 1. Estudios representativos', 'Dar los datos verificables.', 'De 12 a 15 filas elegidas del apartado 4: enfermedad, objetivo clínico, datos, modelo, resultado, validación y grado.', 'Elaboración propia a partir de los estudios citados.'],
    ['Tabla 2. Gaucher, Fabry y Pompe frente a frente', 'Comparar y señalar lagunas.', 'Filas: aplicaciones con evidencia, datos usados, mejor nivel de validación, aplicaciones experimentales, lagunas y barreras. Las limitaciones metodológicas y regulatorias (la Tabla 3 del encargo) se integrarían como última fila y en el texto.', 'Elaboración propia.']], [3.4, 3.2, 6.6, 2.8])
P('El encargo original pedía tres tablas y dos figuras, y la ampliación pide dos o tres elementos visuales. Las revisiones publicadas en el número 10 de la revista llevan entre dos y cuatro. Propongo cuatro (dos figuras y dos tablas) e integrar la Tabla 3 en la Tabla 2 y en el texto. Si prefieres la Tabla 3 separada, cabe, a costa de texto.')
H2('Normas de la revista: comprobadas')
P('Las instrucciones oficiales están en la página 35 del número 10 (octubre de 2026). Coinciden con las del encargo:')
UL(['Revisiones: resumen estructurado, palabras clave, introducción, desarrollo con subtítulos libres y conclusiones.',
    'Word, Arial 11, doble espacio, cada sección en página nueva. De 3 a 6 palabras clave MeSH o DeCS.',
    'Citas con números arábigos entre corchetes por orden de aparición; formato ICMJE; seis autores y «et al.».',
    'Tablas y pies de figura al final, cada una en su página. Figuras en archivos PDF o JPG independientes. Toda la iconografía debe ser original.',
    'Envío por correo electrónico a la dirección que figura en esas instrucciones.'])
P('Diferencias y vacíos respecto al encargo:')
UL(['Las normas no fijan número de palabras ni de páginas. Las revisiones del número 10 ocupan de 3 a 5 páginas, así que el objetivo de unas 2.000 a 2.500 palabras es razonable, pero es una estimación.',
    'El límite de 250 palabras para el resumen aparece solo para los originales. Para las revisiones se pide «resumen estructurado» sin cifra; aplicaré 250.',
    'El resumen en inglés se exige de forma expresa solo en los originales, pero las revisiones publicadas lo incluyen. Lo incluiré.',
    'No hay política escrita sobre el uso de IA. En el número 10 hay figuras con la nota «elaborada con asistencia de inteligencia artificial generativa y revisada por los autores». Recomiendo declarar el uso de IA en la preparación del manuscrito, como piden las recomendaciones del ICMJE.'])

H1('11. Lo que necesito que valides antes de redactar')
UL(['Título: ¿el 1, el 2 o el 3?',
    'Alcance: ¿incluimos mucopolisacaridosis, leucodistrofia metacromática y gangliosidosis junto a Gaucher, Fabry y Pompe (mi recomendación), o solo las tres principales?',
    'Elementos visuales: ¿dos figuras y dos tablas (recomendado), o las tres tablas del encargo original?',
    'Trabajos en la frontera de la IA (regresión logística, puntuaciones por reglas): ¿los incluimos explicando qué son (recomendado) o los excluimos?',
    'Bases de datos: ¿alguien con acceso institucional puede repetir la búsqueda en Embase, Scopus y Web of Science? Si no, el manuscrito dirá que la búsqueda se hizo en PubMed, Europe PMC y ClinicalTrials.gov.',
    'Textos completos: ¿puedes facilitarme los PDF de los estudios de pago que entren en la Tabla 1? Sin ellos, algunos datos quedarán como «no consta».'])

H1('Anexo. Referencias verificadas en formato Vancouver')
P('Orden alfabético provisional; la numeración definitiva seguirá el orden de aparición en el manuscrito.')
refs = sorted(set(list(CORE) + [p for p, _, _ in TR] + list(TRANSFER_NM) + [p for p, _, _ in FR] + ['41661224', '40247315', '42738907', '39859472', '36384353', '39617306']), key=lambda p: by[p]['_v']['pubmed']['authors'][0].lower())
B.append(('ol', [vanc(p) for p in refs]))

# ---------- Markdown
md = []
for k, c in B:
    if k == 'title': md.append('# ' + c + '\n')
    elif k == 'h1': md.append('\n## ' + c + '\n')
    elif k == 'h2': md.append('\n### ' + c + '\n')
    elif k == 'p': md.append(c + '\n')
    elif k == 'ul': md.append('\n'.join('- ' + x for x in c) + '\n')
    elif k == 'ol': md.append('\n'.join(f'{i + 1}. ' + x for i, x in enumerate(c)) + '\n')
    elif k == 'table':
        h, rows, w = c; md.append('| ' + ' | '.join(h) + ' |\n|' + '---|' * len(h) + '\n' + '\n'.join('| ' + ' | '.join(str(x).replace('|', '/') for x in r) + ' |' for r in rows) + '\n')
open(OUT + '/fase1_fase2_mapa_y_propuesta.md', 'w', encoding='utf8').write('\n'.join(md))
# ---------- Word
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
doc = Document(); sec = doc.sections[0]; sec.orientation = WD_ORIENT.LANDSCAPE; sec.page_width, sec.page_height = Cm(29.7), Cm(21.0)
for m in ('left_margin', 'right_margin', 'top_margin', 'bottom_margin'): setattr(sec, m, Cm(1.8))
st = doc.styles['Normal']; st.font.name = 'Arial'; st.font.size = Pt(11); st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial')
for n in ('Heading 1', 'Heading 2', 'Title'):
    s = doc.styles[n]; s.font.name = 'Arial'; s.font.color.rgb = RGBColor(0x1F, 0x3A, 0x5F); s.element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial'); s.element.rPr.rFonts.set(qn('w:ascii'), 'Arial'); s.element.rPr.rFonts.set(qn('w:hAnsi'), 'Arial')
doc.styles['Heading 1'].font.size = Pt(15); doc.styles['Heading 2'].font.size = Pt(12.5); doc.styles['Title'].font.size = Pt(20)
def shade(cell, hexc):
    tcPr = cell._tc.get_or_add_tcPr(); sh = OxmlElement('w:shd'); sh.set(qn('w:val'), 'clear'); sh.set(qn('w:color'), 'auto'); sh.set(qn('w:fill'), hexc); tcPr.append(sh)
for k, c in B:
    if k == 'title': doc.add_heading(c, 0)
    elif k == 'h1': doc.add_heading(c, 1)
    elif k == 'h2': doc.add_heading(c, 2)
    elif k == 'p': doc.add_paragraph(c)
    elif k == 'ul':
        for x in c: doc.add_paragraph(x, style='List Bullet')
    elif k == 'ol':
        for x in c:
            p = doc.add_paragraph(x, style='List Number'); 
            for r in p.runs: r.font.size = Pt(9.5)
    elif k == 'table':
        h, rows, w = c; t = doc.add_table(rows=1, cols=len(h)); t.style = 'Table Grid'; t.autofit = False
        for i, x in enumerate(h):
            cell = t.rows[0].cells[i]; cell.text = ''; r = cell.paragraphs[0].add_run(x); r.bold = True; r.font.size = Pt(9); shade(cell, 'D9E2F3')
        for row in rows:
            cells = t.add_row().cells
            for i, x in enumerate(row):
                cells[i].text = ''; r = cells[i].paragraphs[0].add_run(str(x)); r.font.size = Pt(8.5)
                if h[i] == 'Grado': shade(cells[i], {'A': 'C6E0B4', 'B': 'E2EFDA', 'C': 'FFF2CC', 'D': 'EDEDED'}.get(str(x), 'FFFFFF'))
        if w:
            tot = sum(w); k_ = 25.9 / tot
            tblPr = t._tbl.tblPr; lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr.append(lay)
            for i, gc in enumerate(t._tbl.tblGrid.findall(qn('w:gridCol'))): gc.set(qn('w:w'), str(int(w[i] * k_ * 567)))
            for i, col in enumerate(t.columns): col.width = Cm(w[i] * k_)
            for row in t.rows:
                for i, cell in enumerate(row.cells): cell.width = Cm(w[i] * k_)
        doc.add_paragraph()
doc.save(OUT + '/Fase1_Fase2_mapa_y_propuesta.docx')
# ---------- CSV con todos los registros
with open(OUT + '/fase1_mapa_evidencia/todos_los_registros.csv', 'w', newline='', encoding='utf-8-sig') as f:
    wri = csv.writer(f); wri.writerow(['ambito', 'pmid_o_id', 'verificacion', 'primer_autor', 'anio', 'revista', 'doi_pubmed', 'titulo', 'tipo', 'enfermedad', 'nivel_evidencia', 'area', 'objetivo', 'algoritmo', 'muestra', 'resultados', 'validacion', 'limitaciones', 'cita_literal', 'grado_orquestador', 'nota_orquestador'])
    for s in d:
        v = s['_v']; pb = v.get('pubmed', {}); c = CORE.get(v['pmid'])
        prob = [x for x in v.get('problemas', []) if not x.startswith('DOI')]
        wri.writerow([v['file'].replace('.json', ''), v['pmid'], ('existe en PubMed' if pb else v.get('estado', '')) + ('; ' + ' / '.join(prob) if prob else ''), s.get('primer_autor'), s.get('anio'), pb.get('journal') or s.get('revista'), pb.get('doi', ''), pb.get('title') or s.get('titulo'),
                      s.get('tipo_publicacion'), s.get('enfermedad'), s.get('nivel_evidencia'), s.get('area'), s.get('objetivo'), s.get('algoritmo'), s.get('muestra_y_datos'), s.get('resultados_metricas'), s.get('validacion'), s.get('limitaciones'), s.get('cita_literal'), c[2] if c else '', c[3] if c else ''])
print('bloques', len(B), '| refs', len(refs), '| core', len(CORE)); print({g: sum(1 for v in CORE.values() if grp(v[0]) == g or (v[0].startswith('Gaucher,') and g=='Trans')) for g in GORD})
