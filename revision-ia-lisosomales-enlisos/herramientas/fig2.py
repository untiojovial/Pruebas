# -*- coding: utf-8 -*-
"""Figura 2. Aplicaciones de la IA a lo largo del recorrido del paciente con una enfermedad lisosomal. Genera fig2.svg."""
import html
from PIL import ImageFont
W = 2000
INK, INK2, GRID = '#0b0b0b', '#52514e', '#c9c8c2'
BLUE, ORANGE, AQUA = '#2a78d6', '#eb6834', '#1baf7a'
FR = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'; FB = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
def tw(s, size, bold=False): return ImageFont.truetype(FB if bold else FR, size).getlength(s)
def wrap(s, size, maxw, bold=False):
    out, cur = [], ''
    for w in s.split(' '):
        t = (cur + ' ' + w).strip()
        if tw(t, size, bold) <= maxw or not cur: cur = t
        else: out.append(cur); cur = w
    if cur: out.append(cur)
    return out
o = []
def T(x, y, s, size=22, w='400', fill=INK, anchor='start'):
    o.append(f"<text x='{x:.1f}' y='{y:.1f}' font-size='{size}' font-weight='{w}' fill='{fill}' text-anchor='{anchor}'>{html.escape(s)}</text>")
STAGES = ['Sospecha', 'Diagnóstico', 'Caracterización', 'Pronóstico', 'Tratamiento', 'Seguimiento']
ROWS = [
 ('Evidencia directa', 'Estudios en enfermedades lisosomales', BLUE, 'solid', [
   ['Búsqueda de casos en historias clínicas (G, F, P, MPS)', 'Reconocimiento facial (G, ML, MPS)', 'Cribado neonatal con reconocimiento de patrones (Krabbe, P, MPS I)'],
   ['Resonancia cardíaca frente a miocardiopatía hipertrófica (F)', 'Resonancia muscular (P)', 'Biopsia renal digital (F)', 'Perfil de glucosaminoglucanos (MPS)'],
   ['Volumen del bazo y lesión ósea (G)', 'Desmielinización y edad cerebral (LDM, GM1, F, AGU)', 'Edad ósea (MPS, alfa-manosidosis)', 'Variantes genéticas (MPS III, LDM, F)'],
   ['Complicaciones óseas (G)', 'Trayectorias de función renal (F)'],
   ['Anticuerpos frente a la enzima (F)', 'Respuesta a chaperonas, estudio computacional (F, P, G)', 'Cribado de fármacos, preclínico (MPS IIIA)'],
   ['Movimiento del diafragma y marcha (P)', 'Función motora a partir de vídeo (LDM)', 'Asincronía respiratoria (MPS IVA)']]),
 ('Evidencia complementaria', 'Estudios en otras enfermedades raras', ORANGE, 'hatch', [
   ['Algoritmo validado en millones de historias de otros sistemas sanitarios (inmunodeficiencia variable común)'],
   ['Electrocardiograma con IA y cribado en un ensayo no aleatorizado (amiloidosis cardíaca)', 'Modelos de lenguaje para ordenar diagnósticos (enfermedades raras)'],
   ['Predicción del efecto de variantes con AlphaMissense (distrofias de retina)'],
   [], [], []]),
 ('Aplicaciones potenciales', 'Aún sin estudios en enfermedades lisosomales', AQUA, 'dash', [
   ['Alertas integradas en la historia clínica electrónica', 'Modelos de lenguaje como apoyo a la sospecha'],
   ['Electrocardiograma con IA (F)'],
   ['Modelos validados que integren lyso-Gb1 o lyso-Gb3'],
   ['Predicción individual de la progresión'],
   ['Predicción de la respuesta al tratamiento enzimático o de reducción de sustrato'],
   ['Monitorización a distancia con sensores']]),
]
X0, LW, GAP = 40, 250, 10
CW = (W - 2 * X0 - LW - 6 * GAP) / 6
FS, LH, PAD = 21, 26, 14
# cabecera: flechas de etapa
y = 40; HH = 74
T(X0, y + 30, 'Recorrido', 24, '700'); T(X0, y + 58, 'del paciente', 24, '700')
for i, s in enumerate(STAGES):
    x = X0 + LW + GAP + i * (CW + GAP)
    o.append(f"<path d='M{x:.1f} {y} h{CW - 22:.1f} l22 {HH / 2} l-22 {HH / 2} h-{CW - 22:.1f} l22 -{HH / 2} z' fill='#eceae4' stroke='{INK2}' stroke-width='1.5'/>" if i else
             f"<path d='M{x:.1f} {y} h{CW - 22:.1f} l22 {HH / 2} l-22 {HH / 2} h-{CW - 22:.1f} z' fill='#eceae4' stroke='{INK2}' stroke-width='1.5'/>")
    o.append(f"<circle cx='{x + 46:.1f}' cy='{y + HH / 2}' r='17' fill='{INK}'/>"); T(x + 46, y + HH / 2 + 8, str(i + 1), 22, '700', '#ffffff', 'middle')
    T(x + 72, y + HH / 2 + 8, s, 23, '700')
y += HH + 16
defs = f"<defs><pattern id='hatch' width='10' height='10' patternUnits='userSpaceOnUse' patternTransform='rotate(45)'><rect width='10' height='10' fill='#ffffff'/><rect width='5' height='10' fill='{ORANGE}'/></pattern></defs>"
for name, sub, col, mode, cells in ROWS:
    wrapped = [[wrap(it, FS, CW - 2 * PAD - 22) for it in c] for c in cells]
    hs = [sum(len(l) * LH + 12 for l in c) + 2 * PAD - 12 if c else 0 for c in wrapped]
    RH = max(max(hs), 190)
    # etiqueta de fila
    fill = col if mode == 'solid' else ("url(#hatch)" if mode == 'hatch' else '#ffffff')
    dash = " stroke-dasharray='9 6'" if mode == 'dash' else ''
    o.append(f"<rect x='{X0}' y='{y}' width='{LW}' height='{RH}' rx='10' fill='#ffffff' stroke='{INK2}' stroke-width='1.5'/>")
    o.append(f"<rect x='{X0 + 16}' y='{y + 18}' width='44' height='44' rx='6' fill='{fill}' stroke='{col}' stroke-width='4'{dash}/>")
    for k, l in enumerate(wrap(name, 24, LW - 32, True)): T(X0 + 16, y + 96 + k * 29, l, 24, '700')
    n0 = len(wrap(name, 24, LW - 32, True))
    for k, l in enumerate(wrap(sub, 19, LW - 32)): T(X0 + 16, y + 96 + n0 * 29 + 4 + k * 24, l, 19, fill=INK2)
    for i, c in enumerate(wrapped):
        x = X0 + LW + GAP + i * (CW + GAP)
        o.append(f"<rect x='{x:.1f}' y='{y}' width='{CW:.1f}' height='{RH}' rx='10' fill='#ffffff' stroke='{GRID}' stroke-width='1.5'/>")
        o.append(f"<rect x='{x:.1f}' y='{y}' width='10' height='{RH}' fill='{fill}' stroke='{col}' stroke-width='2'{dash}/>")
        if not c:
            T(x + CW / 2 + 5, y + RH / 2 + 7, 'Sin ejemplos citados', 19, fill=INK2, anchor='middle'); continue
        yy = y + PAD + 18
        for lines in c:
            o.append(f"<circle cx='{x + 28:.1f}' cy='{yy - 7}' r='4' fill='{INK}'/>")
            for l in lines: T(x + 40, yy, l, FS); yy += LH
            yy += 12
    y += RH + GAP
# banda transversal
y += 6; BH = 78
o.append(f"<rect x='{X0}' y='{y}' width='{W - 2 * X0}' height='{BH}' rx='10' fill='#eceae4' stroke='{INK2}' stroke-width='1.5'/>")
T(X0 + 20, y + 32, 'Condiciones comunes a todas las etapas', 23, '700')
T(X0 + 20, y + 62, 'Registros y datos armonizados · colaboración entre centros (aprendizaje federado) · validación externa y prospectiva · evaluación del efecto sobre la atención', 21)
H = int(y + BH + 30)
svg = f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' width='{W}' height='{H}' font-family='Liberation Sans, Arial, Helvetica, sans-serif'>{defs}<rect width='{W}' height='{H}' fill='#ffffff'/>" + ''.join(o) + '</svg>'
open('fig2.svg', 'w', encoding='utf8').write(svg); print(W, H)
