# -*- coding: utf-8 -*-
"""Figura 1. Cómo aprende y cómo se valida un modelo de IA. Genera fig1.svg (datos simulados, semilla fija)."""
import random, math, html
W, H = 2000, 1400
INK, INK2, GRID = '#0b0b0b', '#52514e', '#c9c8c2'
BLUE, ORANGE, AQUA = '#2a78d6', '#eb6834', '#1baf7a'
FONT = "font-family='Liberation Sans, Arial, Helvetica, sans-serif'"
o = []
def T(x, y, s, size=26, w='400', fill=INK, anchor='start', style=''):
    o.append(f"<text x='{x}' y='{y}' font-size='{size}' font-weight='{w}' fill='{fill}' text-anchor='{anchor}' {style}>{html.escape(s)}</text>")
def TL(x, y, lines, size=24, lh=None, **k):
    lh = lh or size * 1.28
    for i, s in enumerate(lines): T(x, y + i * lh, s, size, **k)
# ---------- Panel A: cinco pasos
T(40, 52, 'A', 40, '700'); T(84, 52, 'Del dato a la práctica clínica: cinco pasos y cuánto podemos fiarnos en cada uno', 30, '700')
steps = [('1', 'Datos', ['Historia clínica, analítica,', 'genética, biomarcadores', 'e imagen de pacientes', 'con diagnóstico conocido']),
         ('2', 'Entrenamiento', ['El modelo busca patrones', 'que distinguen a los', 'enfermos, como quien', 'aprende viendo casos']),
         ('3', 'Validación interna', ['Se prueba con pacientes', 'del mismo centro que', 'el modelo no ha visto', 'durante el entrenamiento']),
         ('4', 'Validación externa', ['Se prueba con pacientes', 'de otros hospitales,', 'países, poblaciones', 'y equipos']),
         ('5', 'Evaluación clínica', ['Se usa de forma prospectiva', 'en pacientes reales y se', 'mide si mejora la atención', ''])]
bw, bh, gap, x0, y0 = 352, 244, 40, 40, 92
shade = ['#f1f0ec', '#f1f0ec', '#dbe8f8', '#b9d3f2', '#8fb9ea']
for i, (n, h, ls) in enumerate(steps):
    x = x0 + i * (bw + gap)
    o.append(f"<rect x='{x}' y='{y0}' width='{bw}' height='{bh}' rx='14' fill='{shade[i]}' stroke='{INK2}' stroke-width='1.5'/>")
    o.append(f"<circle cx='{x + 40}' cy='{y0 + 44}' r='24' fill='{INK}'/>"); T(x + 40, y0 + 54, n, 28, '700', '#ffffff', 'middle')
    T(x + 76, y0 + 54, h, 27, '700'); TL(x + 22, y0 + 108, ls, 24, fill=INK)
    if i < 4:
        ax = x + bw + 6; ay = y0 + bh / 2
        o.append(f"<path d='M{ax} {ay} h{gap - 16} m-10 -9 l10 9 l-10 9' fill='none' stroke='{INK}' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/>")
# escala de confianza
yb = y0 + bh + 44
o.append(f"<path d='M{x0 + bw + gap} {yb} H{W - 64} m-14 -11 l14 11 l-14 11' fill='none' stroke='{INK}' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/>")
T(x0 + bw + gap, yb + 40, 'Menos fiable: el resultado puede ser un espejismo', 23, fill=INK2); T(W - 64, yb + 40, 'Más fiable: el modelo funciona fuera de donde nació', 23, fill=INK2, anchor='end')
# llave: dónde se queda la mayoría
xa, xb_ = x0 + (bw + gap), x0 + 2 * (bw + gap) + bw
yk = yb + 76
o.append(f"<path d='M{xa} {yk} v14 H{xb_} v-14' fill='none' stroke='{ORANGE}' stroke-width='3'/>")
T((xa + xb_) / 2, yk + 48, 'Aquí se detiene la mayoría de los estudios publicados en enfermedades lisosomales', 24, '700', anchor='middle')
# ---------- Panel B: sobreajuste
yB = 590
o.append(f"<line x1='40' y1='{yB - 46}' x2='{W - 40}' y2='{yB - 46}' stroke='{GRID}' stroke-width='1.5'/>")
T(40, yB + 4, 'B', 40, '700'); T(84, yB + 4, 'El sobreajuste: memorizar los casos estudiados no es aprender a reconocer casos nuevos', 30, '700')
def sample(rng, n):
    pts = []
    for k in range(n):
        c = k % 2; cx, cy = ((0.36, 0.38) if c == 0 else (0.64, 0.62))
        while True:
            x, y = rng.gauss(cx, 0.17), rng.gauss(cy, 0.17)
            if 0.06 < x < 0.94 and 0.06 < y < 0.94: break
        pts.append((x, y, c))
    return pts
simple = lambda x, y, tr: 1 if x + y > 1 else 0
def overfit(x, y, tr):   # vecino más cercano: reproduce cada caso de entrenamiento
    return min(tr, key=lambda p: (p[0] - x) ** 2 + (p[1] - y) ** 2)[2]
best = None
for seed in range(60000):
    rng = random.Random(seed); tr = sample(rng, 24); new = sample(rng, 24)
    a = sum(simple(x, y, tr) == c for x, y, c in tr); b = sum(simple(x, y, tr) == c for x, y, c in new); d = sum(overfit(x, y, tr) == c for x, y, c in new)
    dmin = min(min(math.dist(p[:2], q[:2]) for i, p in enumerate(S_) for q in S_[:i]) for S_ in (tr, new))
    if a in (20, 21) and b in (20, 21) and d in (16, 17) and dmin > 0.045: best = (seed, tr, new, a, b, d); break
seed, tr, new, a, b, d = best; print('semilla', seed, 'sencillo', a, b, 'sobreajustado 24', d)
S = 440; px = [40 + i * (S + 30) + (50 if i >= 2 else 0) for i in range(4)]; py = yB + 186
groups = [('Modelo sencillo', 'Una frontera simple: se equivoca en algunos casos, pero rinde igual con pacientes nuevos', px[0]), ('Modelo sobreajustado', 'Una frontera retorcida que acierta todos los casos estudiados y falla con los nuevos', px[2])]
for name, sub, gx in groups:
    T(gx, yB + 66, name, 28, '700'); 
    words = sub.split(); l1 = ' '.join(words[:9]); l2 = ' '.join(words[9:])
    T(gx, yB + 100, l1, 22, fill=INK2); T(gx, yB + 127, l2, 22, fill=INK2)
def panel(x0_, model, pts, title, ok):
    o.append(f"<rect x='{x0_}' y='{py}' width='{S}' height='{S}' fill='#ffffff' stroke='{INK2}' stroke-width='1.5'/>")
    step = 2
    for r in range(0, S, step):          # zona que el modelo clasifica como «enfermo», por tramos horizontales
        yy = 1 - (r + step / 2) / S; run = None
        for cidx in range(0, S + 1, step):
            v = model((cidx + step / 2) / S, yy, tr) if cidx < S else 0
            if v and run is None: run = cidx
            if not v and run is not None:
                o.append(f"<rect x='{x0_ + run}' y='{py + r}' width='{cidx - run}' height='{step}' fill='{BLUE}' fill-opacity='0.16'/>"); run = None
    for x, y, c in pts:
        X, Y = x0_ + x * S, py + (1 - y) * S; good = model(x, y, tr) == c
        if c: o.append(f"<circle cx='{X:.1f}' cy='{Y:.1f}' r='9' fill='{BLUE}' stroke='#ffffff' stroke-width='2'/>")
        else: o.append(f"<rect x='{X - 8:.1f}' y='{Y - 8:.1f}' width='16' height='16' fill='#ffffff' stroke='{ORANGE}' stroke-width='3.5'/>")
        if not good: o.append(f"<path d='M{X - 17:.1f} {Y - 17:.1f} l34 34 m0 -34 l-34 34' stroke='{INK}' stroke-width='3' stroke-linecap='round'/>")
    T(x0_, py - 12, title, 23, '700'); T(x0_, py + S + 36, f'Aciertos: {ok} de {len(pts)}', 25, '700')
panel(px[0], simple, tr, 'Casos de entrenamiento', a); panel(px[1], simple, new, 'Pacientes nuevos', b)
panel(px[2], overfit, tr, 'Casos de entrenamiento', 24); panel(px[3], overfit, new, 'Pacientes nuevos', d)
# leyenda
ly = py + S + 96; lx = 40
o.append(f"<circle cx='{lx + 10}' cy='{ly - 8}' r='9' fill='{BLUE}'/>"); T(lx + 30, ly, 'Paciente con la enfermedad', 23)
o.append(f"<rect x='{lx + 372}' y='{ly - 16}' width='16' height='16' fill='#ffffff' stroke='{ORANGE}' stroke-width='3.5'/>"); T(lx + 402, ly, 'Persona sin la enfermedad', 23)
o.append(f"<rect x='{lx + 740}' y='{ly - 20}' width='34' height='24' fill='{BLUE}' fill-opacity='0.16' stroke='{GRID}'/>"); T(lx + 786, ly, 'Zona que el modelo clasifica como «enfermo»', 23)
o.append(f"<path d='M{lx + 1300} {ly - 20} l22 22 m0 -22 l-22 22' stroke='{INK}' stroke-width='3' stroke-linecap='round'/>"); T(lx + 1336, ly, 'Error del modelo', 23)
T(40, ly + 44, 'Datos simulados con fines didácticos (24 casos de entrenamiento y 24 pacientes nuevos); no proceden de ningún estudio.', 21, fill=INK2)
svg = f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' width='{W}' height='{H}' {FONT}><rect width='{W}' height='{H}' fill='#ffffff'/>" + ''.join(o) + '</svg>'
open('fig1.svg', 'w', encoding='utf8').write(svg); print(len(svg) // 1024, 'KB')
