# -*- coding: utf-8 -*-
"""Evidencia directa tras la segunda ronda: estudios originales en EDL (pacientes, variantes o células de pacientes)
con IA, aprendizaje automático o modelos predictivos computacionales. Se añaden a CORE (primera ronda) los nuevos verificados.
Validación con datos externos: modelo probado con datos de otro centro o herramienta desarrollada con otros datos y evaluada en pacientes con EDL."""
from core import CORE
NEW = {  # pmid: (grupo, área, clase, nota)
 '40275674': ('Pompe', '4.4', 'AA', 'Myo-Guide: 116 pacientes con Pompe entre 20 enfermedades neuromusculares; acierto 70-80 % en Pompe. Antes clasificado como transferible; el texto completo confirma la inclusión de Pompe.'),
 '41593722': ('MPS', '4.1', 'AP', 'Redes de grafos; mismos 106 sujetos (37 MPS) que 40770294. No es evidencia independiente.'),
 '30566525': ('MPS', '4.1', 'AA', 'Naive Bayes en atención primaria (Canadá); 73 casos de MPS II creados artificialmente para el entrenamiento.'),
 '36979466': ('MPS', '4.3', 'EC', 'Lasso multinomial sobre glucosaminoglucanos; 38 MPS; validación cruzada.'),
 '29623569': ('MPS y mucolipidosis', '4.1', 'AP', 'DeepGestalt en 289 pacientes con errores congénitos (MPS I, II, ML II/III y otros); exactitud 62 %.'),
 '32298796': ('Mucolipidosis IV', '4.1', 'AP', 'DeepGestalt en 10 pacientes; AUC 0,82-0,89.'),
 '37106005': ('MPS IVA', '4.1', 'AP', 'Face2Gene en muestra colombiana: 0 % de acierto en primera opción para Morquio. Herramienta externa evaluada en otra población.'),
 '34063456': ('MPS IVA', '4.6', 'EC', 'Regresión logística elastic-net entrenada en niños sanos y aplicada a 17 pacientes con Morquio.'),
 '33239591': ('Krabbe y Pompe', '4.1', 'EC', 'Herramientas posanalíticas (CLIR) en cribado neonatal: derivaciones por Krabbe de 48 a 10.'),
 '32064362': ('Pompe y MPS I', '4.1', 'EC', 'CLIR en cribado neonatal de Georgia (59.332 recién nacidos); VPP 66,7 % para Pompe.'),
 '42606959': ('Leucodistrofia metacromática', '4.6', 'AP', 'Función motora desde vídeo en 44 niños del ensayo EMBOLDEN; 82,1 % de acierto. Solo resumen.'),
 '40055237': ('Leucodistrofia metacromática', '4.2', 'AA', 'Desafío CAGI con 219 variantes de ARSA; el mejor modelo usaba herramientas estándar.'),
 '42648230': ('Varias EDL', '4.3', 'EC', 'Regresión logística regularizada; EDL frente a enfermedad mitocondrial primaria; AUC 0,988 interna, 88 participantes.'),
 '33553934': ('Sialidosis', '4.8', 'AA', 'Aprendizaje automático y bibliometría para buscar ligandos de NEU1; validación in vitro.'),
}
EXTERNAL = {'38706878': 'otro hospital (31 estudios)', '41526641': 'otro centro (15 casos)', '41727682': 'herramienta desarrollada con otros datos (186 radiografías)', '37106005': 'herramienta comercial en población colombiana'}
ALL = {**{p: (g, a, None, n) for p, (g, a, gr, n) in CORE.items()}, **NEW}
if __name__ == '__main__':
    import collections
    print('total', len(ALL), '| primera ronda', len(CORE), '| nuevos', len(NEW))
    print(collections.Counter(v[0] for v in ALL.values()))
