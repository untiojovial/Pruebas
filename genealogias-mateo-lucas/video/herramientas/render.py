# -*- coding: utf-8 -*-
import json, math, os, re, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from engine import *
from script import SCENES

FPS = 24
GAP = 0.32      # pausa entre segmentos
LEAD = 0.55     # entrada de escena
TAIL = 0.45     # salida de escena
PG = B + '/pg'

# ---------- línea de tiempo ----------
def wav_info(p):
    w = wave.open(p); n = w.getnframes(); sr = w.getframerate(); a = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768
    return a, sr

def build_timeline():
    T = []; t = 0.0
    for si, s in enumerate(SCENES):
        sc = dict(i=si, start=t, id=s['id'], title=s['title'], vis=s['vis'], segs=[])
        t += LEAD
        for gi, (spk, text) in enumerate(s['segs']):
            key = f'{si:02d}_{gi}'
            a, sr = wav_info(f'{B}/aud/{key}.wav')
            dur = len(a) / sr
            words = json.load(open(f'{B}/aud/{key}.json'))
            # envolvente para la boca
            hop = int(sr / FPS); env = []
            for k in range(0, len(a), hop):
                env.append(float(np.sqrt(np.mean(a[k:k + hop] ** 2)) if len(a[k:k + hop]) else 0))
            env = np.array(env); mx = max(1e-6, np.percentile(env, 95)); env = np.clip(env / mx, 0, 1)
            sc['segs'].append(dict(spk=spk, text=text, key=key, t0=t, dur=dur, words=align(text, words), env=env))
            t += dur + GAP
        t += TAIL - GAP
        sc['end'] = t
        T.append(sc)
    return T, t

def align(text, words):
    toks = text.split(); out = []; j = 0
    norm = lambda s: re.sub(r'[^\wáéíóúüñÁÉÍÓÚÜÑ]', '', s.lower())
    for (off, du, w) in words:
        nw = norm(w)
        disp = w
        for k in range(j, min(j + 4, len(toks))):
            if norm(toks[k]).startswith(nw) or nw.startswith(norm(toks[k])) and norm(toks[k]):
                disp = toks[k]; j = k + 1; break
        out.append((off, du, disp))
    return out

def chunks(words, maxw=6):
    """Agrupa palabras en bloques de subtítulo (corta en puntuación)."""
    out = []; cur = []
    for w in words:
        cur.append(w)
        if len(cur) >= maxw or re.search(r'[.,;:!?¡¿]$', w[2]) and len(cur) >= 2:
            out.append(cur); cur = []
    if cur: out.append(cur)
    return out

# ---------- escenas ----------
IMGS = {}
def img(name, w=None, crop=None):
    k = (name, w, crop)
    if k not in IMGS:
        im = Image.open(f'{PG}/{name}').convert('RGB')
        if crop: im = im.crop(crop)
        if w: im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
        IMGS[k] = im
    return IMGS[k]

BG = dict(hook=(255, 236, 214), tree=(226, 238, 252), logic=(236, 232, 252), levir=(232, 246, 236), scan_euseb=(244, 238, 226), zoro=(252, 240, 222),
          greek=(230, 242, 250), roads=(238, 246, 230), aaron=(250, 236, 236), jecon=(232, 232, 244), scan_ireneo=(244, 238, 226), y1500=(255, 232, 226),
          justino=(240, 236, 226), timeline=(232, 240, 250), omis=(244, 240, 228), cainan=(230, 244, 244), talmud=(250, 238, 230), end=(228, 244, 236))

class Ctx:
    def __init__(s, sc, lt, gt):
        s.sc = sc; s.lt = lt; s.gt = gt  # tiempo local de escena y global
        s.seg = -1; s.st = 0.0; s.spk = None; s.amp = 0.0
        for gi, g in enumerate(sc['segs']):
            if gt >= g['t0'] - 0.05: s.seg = gi; s.st = gt - g['t0']
        if s.seg >= 0:
            g = sc['segs'][s.seg]
            if 0 <= s.st <= g['dur']:
                s.spk = g['spk']; k = int(s.st * FPS)
                s.amp = float(g['env'][k]) if k < len(g['env']) else 0.0
    def on(s, k, dt=0.0, dur=0.45):
        """Progreso 0..1 de la aparición de un elemento al comenzar el segmento k (+dt s)."""
        if k >= len(s.sc['segs']): return 0.0
        t0 = s.sc['segs'][k]['t0'] + dt
        return ease((s.gt - t0) / dur)
    def talk(s, who):
        return s.amp if s.spk == who else 0.0

def slide(p, y): return y + (1 - p) * 60

def header(d, sc, ctx):
    p = ease(ctx.lt / 0.5)
    n = f"{sc['i'] + 1}/{len(SCENES)}"
    f = F('title', 66 if len(sc['title']) < 26 else 56)
    lines = wrap(d, sc['title'], f, 900)
    y = 175 - (1 - p) * 80
    for l in lines:
        tw = d.textlength(l, font=f)
        rrect(d, (500 - tw / 2 - 26, y - f.size * 0.62, 500 + tw / 2 + 26, y + f.size * 0.62), 20, INK)
        d.text((500, y + 4), l, font=f, fill=(255, 255, 255), anchor='mm'); y += f.size * 1.3
    d.text((60, 108), n, font=F('bold', 32), fill=mix(BG[sc['vis']], INK, 0.55), anchor='lm')

def bgfill(img_, col):
    d = ImageDraw.Draw(img_)
    d.rectangle((0, 0, W, H), fill=col)
    dot = mix(col, INK, 0.07)
    for yy in range(40, H, 80):
        for xx in range(40 + (40 if (yy // 80) % 2 else 0), W, 80):
            d.ellipse((xx - 3, yy - 3, xx + 3, yy + 3), fill=dot)

NAR = dict(color=PAL['blue'], name='Narrador', acc=('scroll',))
ESC = dict(color=PAL['red'], name='Escéptico', acc=('cap',))

def nar(d, ctx, x=760, y=1330, s=0.85, arms=None, face=-1):
    figure(d, x, y, s, NAR['color'], ctx.talk('N'), ctx.gt, NAR['name'], NAR['acc'], arms=arms or ('point' if ctx.talk('N') else None), face=face, phase=1.3)
def esc(d, ctx, x=230, y=1330, s=0.85, arms=None, face=1, mood='ok'):
    figure(d, x, y, s, ESC['color'], ctx.talk('E'), ctx.gt, ESC['name'], ESC['acc'], arms=arms or ('shrug' if ctx.talk('E') else 'cross'), face=face, phase=0.4, mood=mood)
    if ctx.talk('E') > 0.05:
        f = F('title', 90); d.text((x + 70, y - 330 * s), '?', font=f, fill=PAL['red'], anchor='mm')

# --- cada visual ---
def v_hook(d, im, ctx):
    p0 = ctx.on(0, 0.2); p1 = ctx.on(0, 2.8)
    if p0:
        y = slide(p0, 380)
        card(d, 70, y, 400, ['José,', 'hijo de JACOB'], F('bold', 46), title='MATEO 1:16', tcolor=PAL['blue'], align='c')
    if p1:
        y = slide(p1, 380)
        card(d, 530, y, 400, ['José,', 'hijo de ELÍ'], F('bold', 46), title='LUCAS 3:23', tcolor=PAL['purple'], align='c')
        pulse = 1 + 0.08 * math.sin(ctx.gt * 6)
        f = F('title', int(110 * pulse)); d.text((500, 470), '≠', font=f, fill=PAL['red'], anchor='mm')
    p2 = ctx.on(1, 3.0)
    if p2:
        for i, (t, c) in enumerate([('griego', PAL['blue']), ('hebreo', PAL['teal']), ('latín', PAL['purple']), ('páginas reales', PAL['gold'])]):
            if ctx.on(1, 3.0 + i * 0.5): pill(d, 500, slide(ctx.on(1, 3.0 + i * 0.5), 690 + i * 72), t, c, F('bold', 38))
    p3 = ctx.on(2, 1.0)
    if p3:
        stamp(d, 500, slide(p3, 1010), '¿INVENTO DEL 1500?', PAL['red'], 62)
    esc(d, ctx, 230, 1340); nar(d, ctx, 770, 1340)

def v_tree(d, im, ctx):
    fN = F('bold', 36)
    def node(x, y, t, c, p=1.0, big=False):
        if p <= 0: return
        f = F('title', 44) if big else fN
        y = slide(p, y)
        pill(d, x, y, t, c, f)
    p = ctx.on(0, 0.3)
    node(500, 340, 'Abrahán', INK, p);
    if ctx.on(0, 1.2): d.line([(500, 375), (500, 440)], fill=INK, width=6); node(500, 470, '… 14 generaciones …', PAL['gray'], ctx.on(0, 1.2))
    if ctx.on(0, 3.0): d.line([(500, 505), (500, 545)], fill=INK, width=6); node(500, 580, 'DAVID', PAL['gold'], ctx.on(0, 3.0), True)
    if ctx.on(0, 0.6):
        d.text((90, 470), 'Mateo ↓', font=F('title', 40), fill=PAL['blue'], anchor='lm'); d.text((910, 470), 'Lucas ↑', font=F('title', 40), fill=PAL['purple'], anchor='rm')
    p1 = ctx.on(1, 1.0)
    if p1:
        d.line([(500, 620), (260, 690)], fill=PAL['blue'], width=8); d.line([(500, 620), (740, 690)], fill=PAL['purple'], width=8)
        node(260, 720, 'Salomón (reyes)', PAL['blue'], p1); node(740, 720, 'Natán', PAL['purple'], ctx.on(1, 3.5))
        if ctx.on(1, 2.0):
            for k in range(3): d.ellipse((252, 780 + k * 26, 268, 796 + k * 26), fill=PAL['blue'])
        if ctx.on(1, 4.0):
            for k in range(3): d.ellipse((732, 780 + k * 26, 748, 796 + k * 26), fill=PAL['purple'])
    p2 = ctx.on(2, 0.6)
    if p2:
        for x, c in ((260, PAL['blue']), (740, PAL['purple'])):
            node(x, 880, 'Salatiel', c, p2); node(x, 950, 'Zorobabel', c, p2)
            for k in range(3): d.ellipse((x - 8, 995 + k * 22, x + 8, 1011 + k * 22), fill=c)
        d.line([(370, 880), (630, 880)], fill=PAL['gold'], width=5); d.line([(380, 950), (620, 950)], fill=PAL['gold'], width=5)
    p3 = ctx.on(2, 4.0)
    if p3:
        node(260, 1090, 'Jacob', PAL['blue'], p3, True); node(740, 1090, 'Elí', PAL['purple'], ctx.on(2, 5.2), True)
        if ctx.on(2, 5.6):
            arrow(d, (300, 1130), (450, 1200), PAL['blue']); arrow(d, (700, 1130), (550, 1200), PAL['purple'])
            node(500, 1235, 'JOSÉ', INK, ctx.on(2, 5.6), True)
            f = F('title', 80); d.text((620, 1235), '?', font=f, fill=PAL['red'], anchor='mm')
    figure(d, 900, 1400, 0.55, NAR['color'], ctx.talk('N'), ctx.gt, None, NAR['acc'], face=-1, phase=1.3)

def v_logic(d, im, ctx):
    p0 = ctx.on(0, 0.3)
    if p0:
        card(d, 70, slide(p0, 360), 860, 'Se contradicen solo si es IMPOSIBLE que las dos sean verdad a la vez.', F('bold', 44), title='P1 · Contradicción', tcolor=PAL['purple'])
    p1 = ctx.on(1, 0.3)
    if p1:
        card(d, 70, slide(p1, 640), 860, 'Basta UN modelo coherente en que ambas sean verdad.', F('bold', 44), title='P2 · Refutación por modelo', tcolor=PAL['purple'])
        if ctx.on(1, 2.5): check(d, 870, 700, 1.4)
    if ctx.on(2, 0):
        if ctx.talk('E') > 0 or ctx.seg == 2:
            bubble(d, 90, 900, 520, '¡Un hombre tiene un solo padre!', tail=(230, 1060))
    p3 = ctx.on(3, 0.2)
    if p3:
        card(d, 360, slide(p3, 900), 570, '∴ Busquemos ese modelo…', F('title', 46), bg=(255, 248, 225), border=PAL['gold'], align='c')
    esc(d, ctx, 230, 1340); nar(d, ctx, 770, 1340)

def v_levir(d, im, ctx):
    s = 0.62
    # Esta en el centro
    pE = ctx.on(0, 1.5)
    if pE: figure(d, 500, 640, s, PAL['pink'], 0, ctx.gt, 'Esta', ('hair', 'dress'), phase=0.2)
    pM = ctx.on(0, 2.6); deadM = ctx.on(1, 0.2) > 0.5
    if pM:
        figure(d, 230, 640, s, PAL['blue'], 0, ctx.gt, 'Matán', (), ghost=deadM, phase=0.7)
        d.text((230, 340), 'línea de Salomón', font=F('semi', 30), fill=PAL['blue'], anchor='mm')
    pJ = ctx.on(0, 5.0)
    if pJ:
        d.line([(320, 600), (390, 760)], fill=PAL['blue'], width=5)
        figure(d, 330, 1000, s, PAL['blue'], 0, ctx.gt, 'Jacob', (), phase=1.1)
    pMe = ctx.on(1, 1.6)
    if pMe:
        figure(d, 770, 640, s, PAL['purple'], 0, ctx.gt, 'Melquí', (), ghost=ctx.on(2, 0) > 0.5 and False, phase=0.9)
        d.text((770, 340), 'línea de Natán', font=F('semi', 30), fill=PAL['purple'], anchor='mm')
    pH = ctx.on(1, 3.6)
    deadH = ctx.on(2, 1.8) > 0.5
    if pH:
        d.line([(680, 600), (610, 760)], fill=PAL['purple'], width=5)
        figure(d, 670, 1000, s, PAL['purple'], 0, ctx.gt, 'Elí', (), ghost=deadH, phase=0.5)
    if ctx.on(1, 5.0):
        pill(d, 500, 790, 'hermanos de madre', PAL['gold'], F('bold', 32))
    pV = ctx.on(2, 0.5)
    if pV:
        figure(d, 850, 1000, s * 0.95, PAL['pink'], 0, ctx.gt, 'viuda', ('hair', 'dress'), phase=0.3)
    pDt = ctx.on(2, 3.2)
    if pDt and ctx.seg == 2:
        scroll(d, 90, slide(pDt, 1080), 820, 160, 'Deuteronomio 25:5-6', ['el hermano toma a la viuda', 'y el primogénito lleva el nombre del muerto'], F('hand', 38))
    pJo = ctx.on(3, 1.0)
    if pJo:
        figure(d, 500, 1340, 0.62, PAL['green'], 0, ctx.gt, 'José', (), phase=0.1)
        arrow(d, (340, 1030), (450, 1150), PAL['green'], 7); arrow(d, (660, 1030), (550, 1150), PAL['gold'], 7)
        d.text((250, 1200), 'por naturaleza', font=F('bold', 38), fill=PAL['green'], anchor='mm')
        d.text((760, 1200), 'por ley', font=F('bold', 38), fill=PAL['gold'], anchor='mm')
    if ctx.on(3, 5.0):
        stamp(d, 500, 1440, '2 padres = 0 contradicción', PAL['green'], 46)

def v_scan(d, im, ctx, name, crop, who, acc, cap, extra=None):
    p = ctx.on(0, -0.3)
    sim = img(name, 860, crop)
    y = int(slide(p, 330))
    rrect(d, (52, y - 18, 52 + 896, y + sim.height + 18), 22, (255, 255, 255), INK, 5)
    im.paste(sim, (70, y))
    d.text((500, y + sim.height + 50), cap, font=F('semi', 30), fill=mix(INK, (255, 255, 255), 0.25), anchor='mm')
    figure(d, 170, 1390, 0.75, PAL['gold'], ctx.talk('P'), ctx.gt, who, acc, arms='up' if ctx.talk('P') else None, phase=0.6)
    if extra: extra(d, im, ctx, y + sim.height)
    nar(d, ctx, 830, 1390, 0.7)

def v_scan_euseb(d, im, ctx):
    def extra(d, im, ctx, yb):
        p = ctx.on(1, 4.0)
        if p:
            card(d, 280, slide(p, 1060), 520, ['εἰ καὶ ἀμάρτυρός ἐστιν', '«aunque no tenga testimonio»'], F('greek', 40), bg=(255, 248, 225), border=PAL['gold'], align='c')
    v_scan(d, im, ctx, 'euseb_he1_7_9.jpg', (0, 600, 784, 1180), 'Eusebio', ('beard', 'cloak'), 'Eusebio, Hist. ecl. 1.7.9 · ed. Loeb 1926, p. 58', extra)

def v_zoro(d, im, ctx):
    p = ctx.on(0, 3.5)
    figure(d, 500, 980, 0.8, PAL['teal'], 0, ctx.gt, 'Zorobabel', ('crown',), phase=0.4)
    if p:
        pill(d, 260, slide(p, 420), 'Salatiel', PAL['blue'], F('title', 44)); d.text((260, 490), 'Esdras 3:2 · Ageo 2:23', font=F('semi', 32), fill=INK, anchor='mm')
        arrow(d, (450, 760), (300, 530), PAL['blue'])
    p2 = ctx.on(0, 7.0)
    if p2:
        pill(d, 740, slide(p2, 420), 'Pedaías', PAL['purple'], F('title', 44)); d.text((740, 490), '1 Crónicas 3:19', font=F('semi', 32), fill=INK, anchor='mm')
        arrow(d, (550, 760), (700, 530), PAL['purple'])
        f = F('title', 70); d.text((500, 600), '2 padres', font=f, fill=PAL['red'], anchor='mm')
    p3 = ctx.on(1, 0.5)
    if p3:
        card(d, 90, slide(p3, 1080), 820, ['1 Cr 3:19 + Esd 3:2  =  Mt 1:16 + Lc 3:23'], F('bold', 40), title='Misma vara de medir', tcolor=PAL['teal'], align='c')
    nar(d, ctx, 840, 1400, 0.62)

def v_greek(d, im, ctx):
    p0 = ctx.on(0, 1.5)
    if p0:
        y = slide(p0, 330)
        rrect(d, (70, y, 930, y + 230), 24, (255, 255, 255), INK, 5)
        d.text((500, y + 40), 'Lucas 3:23', font=F('title', 36), fill=PAL['purple'], anchor='mm')
        d.text((500, y + 115), 'ὡς ἐνομίζετο', font=F('greekb', 84), fill=INK, anchor='mm')
        d.text((500, y + 190), '«según se pensaba»', font=F('bold', 44), fill=PAL['purple'], anchor='mm')
    p1 = ctx.on(1, 0.3)
    if p1:
        sim = img('wh_mt116.jpg', 560, (0, 360, 675, 620))
        y = int(slide(p1, 610))
        rrect(d, (52, y - 12, 52 + 580, y + sim.height + 12), 18, (255, 255, 255), INK, 4)
        im.paste(sim, (62, y))
        d.text((345, y + sim.height + 34), 'Mt 1:16 · Westcott-Hort 1881, p. 4', font=F('semi', 28), fill=INK, anchor='mm')
    p2 = ctx.on(1, 5.5)
    if p2:
        y = slide(p2, 610)
        rrect(d, (660, y, 940, y + 330), 24, (255, 255, 255), PAL['red'], 6)
        d.text((800, y + 90), 'ἐξ ἧς', font=F('greekb', 84), fill=PAL['red'], anchor='mm')
        d.text((800, y + 180), '«de la cual»', font=F('bold', 40), fill=INK, anchor='mm')
        d.text((800, y + 250), '(femenino:', font=F('semi', 32), fill=INK, anchor='mm'); d.text((800, y + 290), 'María)', font=F('semi', 32), fill=INK, anchor='mm')
    p3 = ctx.on(2, 0.5)
    if p3:
        card(d, 70, slide(p3, 1010), 860, 'Ninguno dice que José sea el padre biológico.', F('bold', 42), bg=(236, 248, 240), border=PAL['green'], align='c')
    nar(d, ctx, 840, 1400, 0.62)

def v_roads(d, im, ctx):
    figure(d, 500, 1350, 0.62, PAL['gold'], 0, ctx.gt, 'Jesús', ('halo',), phase=0.3)
    if ctx.seg == 0 or ctx.talk('E'):
        esc(d, ctx, 200, 1350, 0.7)
        bubble(d, 330, 1000, 560, 'Sin sangre de José, ¡no es hijo de David!', tail=(260, 1110))
    p1 = ctx.on(1, 0.5)
    old = ctx.seg >= 4
    if p1:
        pill(d, 250, slide(p1, 360), '1 · LEY', PAL['blue'], F('title', 46))
        card(d, 60, slide(p1, 420), 400, ['«Este es mi hijo»', '→ es creído'], F('bold', 36), title='Misná, Bava Batra 8:6', tfont=F('title', 30), tcolor=PAL['blue'])
    if ctx.on(1, 5.5) and not old:
        card(d, 60, slide(ctx.on(1, 5.5), 640), 400, ['quien cría a un huérfano', '= como si lo engendrara'], F('bold', 32), title='Talmud, Sanedrín 19b', tfont=F('title', 30), tcolor=PAL['blue'])
    if ctx.on(2, 0.3):
        figure(d, 250, 1080, 0.55, PAL['blue'], 0, ctx.gt, 'José', (), phase=0.9)
        arrow(d, (300, 1100), (450, 1220), PAL['blue'], 7)
        d.text((250, 865), '«José, hijo de David»', font=F('hand', 40), fill=PAL['blue'], anchor='mm'); d.text((250, 905), 'Mt 1:20', font=F('semi', 28), fill=INK, anchor='mm')
    p3 = ctx.on(3, 0.3)
    if p3:
        pill(d, 750, slide(p3, 360), '2 · CARNE', PAL['purple'], F('title', 46))
        card(d, 540, slide(p3, 420), 400, ['ἐκ σπέρματος Δαυεὶδ', 'κατὰ σάρκα'], F('greek', 38), title='Romanos 1:3', tfont=F('title', 30), tcolor=PAL['purple'])
    if ctx.on(3, 4.0):
        figure(d, 750, 1080, 0.55, PAL['pink'], 0, ctx.gt, 'María', ('hair', 'dress'), phase=0.2)
        arrow(d, (700, 1100), (550, 1220), PAL['purple'], 7)
    p4 = ctx.on(4, 0.3)
    if p4:
        card(d, 300, slide(p4, 610), 400, ['«el trono de David,', 'su padre»'], F('bold', 34), title='Lucas 1:32', tfont=F('title', 30), tcolor=PAL['gold'], align='c')
    if ctx.on(4, 5.5): stamp(d, 500, 1440, 'LEY + CARNE', PAL['green'], 50)

def v_aaron(d, im, ctx):
    if ctx.seg == 0 or ctx.talk('E'):
        esc(d, ctx, 230, 1340); bubble(d, 330, 980, 560, '¡María era levita!', tail=(280, 1090))
        figure(d, 760, 1340, 0.7, PAL['pink'], 0, ctx.gt, 'Isabel', ('hair', 'dress'), phase=0.5)
        d.text((760, 1040), '«de las hijas de Aarón»', font=F('hand', 38), fill=INK, anchor='mm'); d.text((760, 1080), 'Lc 1:5, 1:36', font=F('semi', 28), fill=INK, anchor='mm')
    p1 = ctx.on(1, 0.5)
    if p1:
        card(d, 70, slide(p1, 360), 860, ['La objeción ya la hizo Fausto el maniqueo (c. 400).', 'Pariente ≠ misma tribu: la tribu va por el padre.'], F('bold', 38), title='Agustín, Contra Faustum 23', tcolor=PAL['red'])
    p2 = ctx.on(2, 0.3)
    if p2:
        figure(d, 300, 1000, 0.68, PAL['teal'], 0, ctx.gt, 'Aarón', ('beard', 'mitre', 'cloak'), phase=0.2)
        figure(d, 560, 1000, 0.68, PAL['orange'], 0, ctx.gt, 'Eliseba', ('hair', 'dress'), phase=0.8)
        d.text((560, 680), 'de JUDÁ', font=F('title', 44), fill=PAL['orange'], anchor='mm')
        d.text((560, 725), 'hermana de Naasón', font=F('semi', 30), fill=INK, anchor='mm')
        d.text((430, 1080), 'Éxodo 6:23 · Números 1:7', font=F('semi', 32), fill=INK, anchor='mm')
    if ctx.on(2, 5.0):
        arrow(d, (430, 1110), (430, 1200), PAL['teal'], 7)
        pill(d, 430, 1240, 'todos los sacerdotes: madre de Judá', PAL['teal'], F('bold', 34))
    if ctx.seg >= 1: nar(d, ctx, 850, 1420, 0.65)

def v_jecon(d, im, ctx):
    if ctx.seg == 0:
        scroll(d, 90, 360, 820, 210, 'Jeremías 22:30', ['«ninguno de su semilla prosperará', 'sentándose en el trono de David»'], F('hand', 42))
        figure(d, 500, 1000, 0.75, PAL['gray'], 0, ctx.gt, 'Jeconías', ('crown',), mood='sad', phase=0.4)
        for k in range(5): d.ellipse((380 + k * 50, 640 + (k % 2) * 20, 470 + k * 50, 700 + (k % 2) * 20), fill=(110, 116, 130))
        esc(d, ctx, 200, 1350, 0.7)
        return
    # dilema
    d.text((500, 360), 'DILEMA', font=F('title', 60), fill=INK, anchor='mm')
    arrow(d, (500, 410), (270, 500), INK); arrow(d, (500, 410), (730, 500), INK)
    p1 = ctx.on(1, 0.5)
    if p1:
        card(d, 50, slide(p1, 520), 430, ['Ageo 2:23: «te pondré', 'como anillo de sello»'], F('bold', 32), title='1 · Se levantó', tfont=F('title', 38), tcolor=PAL['green'])
        d.ellipse((215, 760, 305, 850), outline=PAL['gold'], width=14); d.rectangle((240, 735, 280, 770), fill=PAL['gold'])
    p2 = ctx.on(2, 0.2)
    if p2:
        card(d, 50, slide(p2, 890), 430, ['«el arrepentimiento', 'anuló el juramento', 'y el decreto»'], F('hand', 38), title='Levítico Rabá 10:5', tfont=F('title', 30), tcolor=PAL['teal'])
    p3 = ctx.on(3, 0.3)
    if p3:
        card(d, 520, slide(p3, 520), 430, ['Cae sobre su SEMILLA.', 'Jesús no es semilla', 'de José.'], F('bold', 34), title='2 · Sigue en pie', tfont=F('title', 38), tcolor=PAL['purple'])
        pill(d, 735, slide(p3, 800), 'derecho legal, sin la sangre', PAL['purple'], F('bold', 28))
    if ctx.on(3, 5.0):
        check(d, 265, 1150, 1.6); check(d, 735, 1150, 1.6)
        stamp(d, 500, 1290, 'la objeción no llega', PAL['green'], 54)
    nar(d, ctx, 880, 1400, 0.5)

def v_scan_ireneo(d, im, ctx):
    v_scan(d, im, ctx, 'ireneo_harvey119.jpg', (0, 0, 761, 640), 'Ireneo', ('beard', 'mitre', 'cloak'), 'Ireneo, Contra las herejías 3.21.9 · ed. Harvey 1857, p. 119')

def v_y1500(d, im, ctx):
    if ctx.seg == 0 or ctx.talk('E'):
        esc(d, ctx, 230, 1340); bubble(d, 330, 960, 560, '¡Eso se inventó hacia el 1500!', tail=(280, 1080))
    pA = ctx.on(1, 0.5)
    if pA:
        figure(d, 760, 1000, 0.7, PAL['brown'], 0, ctx.gt, 'Annio de Viterbo', ('hat', 'cloak'), phase=0.7)
        pill(d, 760, slide(pA, 620), 'c. 1490', PAL['red'], F('title', 44))
        if ctx.on(1, 5.0):
            card(d, 70, slide(ctx.on(1, 5.0), 360), 560, ['Verdad: la FÓRMULA', '«Elí = padre de María»', 'no aparece antes.'], F('bold', 38), bg=(255, 248, 225), border=PAL['gold'])
    p2 = ctx.on(2, 0.3)
    if p2:
        card(d, 70, slide(p2, 1060), 860, ['tarde ≠ falso  (falacia genética)'], F('title', 44), title='1 · La conclusión no se sigue', tfont=F('title', 32), tcolor=PAL['purple'], align='c')
    if ctx.on(2, 5.0):
        pill(d, 500, 1300, '2 · Las piezas son antiquísimas →', PAL['green'], F('bold', 38))
    if ctx.seg >= 1: nar(d, ctx, 200, 1400, 0.55, face=1)

def v_justino(d, im, ctx):
    figure(d, 180, 1000, 0.8, PAL['gold'], ctx.talk('P'), ctx.gt, 'Justino', ('beard', 'cloak'), arms='up' if ctx.talk('P') else None, phase=0.6)
    pill(d, 180, 560, 'c. 155', PAL['gold'], F('title', 44))
    p0 = ctx.on(0, 1.5)
    if p0:
        card(d, 330, slide(p0, 360), 600, ['la Virgen, del linaje de', 'David, Jacob, Isaac y Abrahán:', '«los enumerados de los que', 'María trae su linaje»'], F('bold', 34), title='Diálogo con Trifón 100.3', tfont=F('title', 30), tcolor=PAL['gold'])
    p1 = ctx.on(1, 0)
    if p1:
        y = slide(p1, 700)
        rrect(d, (330, y, 930, y + 360), 24, (255, 252, 240), PAL['gold'], 6)
        gl = ['πατέρας τῶν γεννωμένων', 'ταῖς θυγατράσιν αὐτῶν τέκνων', 'τοὺς τῶν θηλειῶν γεννήτορας', 'ἐπιστάμεθα.']
        for k, l in enumerate(gl): d.text((630, y + 50 + k * 50), l, font=F('greek', 38), fill=INK, anchor='mm')
        d.text((630, y + 270), 'los padres de las mujeres son padres', font=F('bold', 30), fill=PAL['brown'], anchor='mm')
        d.text((630, y + 310), 'de los hijos de sus hijas', font=F('bold', 30), fill=PAL['brown'], anchor='mm')
    p2 = ctx.on(2, 0.2)
    if p2:
        sim = img('strauss101.jpg', 600, (0, 160, 705, 470))
        y = int(slide(p2, 1110))
        rrect(d, (322, y - 10, 938, y + sim.height + 10), 16, (255, 255, 255), INK, 4)
        im.paste(sim, (330, y))
        figure(d, 180, 1400, 0.5, PAL['gray'], 0, ctx.gt, 'Strauss (crítico)', ('glasses',), phase=1.0)

def v_timeline(d, im, ctx):
    x0 = 220
    d.line([(x0, 340), (x0, 1330)], fill=INK, width=8)
    items = [(0, 0.3, '155', 'Justino', 'María, del linaje de David', PAL['gold'], ('beard',)),
             (0, 0.6, '180', 'Ireneo', '«ella misma del linaje de David»', PAL['gold'], ('mitre',)),
             (0, 3.4, '210', 'Tertuliano', '«Maria ex David»', PAL['gold'], ()),
             (1, 0.3, 's. IV', 'Eusebio · Jerónimo · Crisóstomo', 'la genealogía de José muestra la de María', PAL['teal'], ('beard',)),
             (2, 0.3, '743', 'Juan Damasceno', 'María por Natán, familia de Elí', PAL['purple'], ('beard',)),
             (3, 0.3, 'c. 1490', 'Annio de Viterbo', 'fórmula explícita', PAL['red'], ('hat',))]
    for k, (sg, dt, yr, who, what, c, acc) in enumerate(items):
        p = ctx.on(sg, dt)
        if not p: continue
        y = 400 + k * 160
        xx = x0 + (1 - p) * -60
        d.ellipse((x0 - 16, y - 16, x0 + 16, y + 16), fill=c, outline=INK, width=4)
        d.text((x0 - 30, y), yr, font=F('title', 34), fill=c, anchor='rm')
        figure(d, x0 + 90, y + 70, 0.36, c, 0, ctx.gt, None, acc, phase=k)
        d.text((x0 + 160, y - 22), who, font=F('title', 38), fill=INK, anchor='lm')
        d.text((x0 + 160, y + 24), what, font=F('semi', 32), fill=mix(INK, (255, 255, 255), 0.2), anchor='lm')
    if ctx.on(3, 3.0):
        pill(d, 680, 1295, 'piezas: siglos II–VIII', PAL['green'], F('bold', 32))
        stamp(d, 470, 1385, 'Africano (c. 220) no la necesita', PAL['green'], 40)

def v_omis(d, im, ctx):
    if ctx.seg == 0 or ctx.talk('E'):
        esc(d, ctx, 200, 1350, 0.7)
    names = ['Joram', 'Ocozías', 'Joás', 'Amasías', 'Ozías']
    p0 = ctx.on(0, 0.5)
    if p0:
        for k, n in enumerate(names):
            y = 380 + k * 72
            om = 1 <= k <= 3
            pill(d, 500, slide(p0, y), n, PAL['red'] if om else PAL['blue'], F('bold', 40))
            if om and ctx.on(0, 1.5 + k * 0.6):
                d.line([(380, y), (620, y)], fill=INK, width=8)
        d.text((790, 560), '1 Cr 3:11-12', font=F('semi', 30), fill=INK, anchor='mm'); d.text((790, 600), 'vs Mt 1:8', font=F('semi', 30), fill=INK, anchor='mm')
    p1 = ctx.on(1, 3.5)
    if p1:
        card(d, 70, slide(p1, 760), 860, ['Esdras «hijo de Seraías» († 586 a. C.)', 'Esd 7:1-5 salta 6 generaciones de 1 Cr 5'], F('bold', 36), title='«hijo de» = descendiente de', tfont=F('title', 36), tcolor=PAL['teal'])
    p2 = ctx.on(2, 0.3)
    if p2:
        y = slide(p2, 1010)
        rrect(d, (240, y, 760, y + 200), 24, (255, 255, 255), PAL['gold'], 6)
        d.text((500, y + 70), 'ד  ו  ד', font=F('heb', 70), fill=INK, anchor='mm')
        d.text((500, y + 150), '4 + 6 + 4 = 14 = DAVID', font=F('title', 44), fill=PAL['gold'], anchor='mm')
    if ctx.on(3, 0.5):
        pill(d, 500, 1270, '41 nombres, no 42: se discute', PAL['gray'], F('bold', 34))
    nar(d, ctx, 880, 1400, 0.45)

def v_cainan(d, im, ctx):
    if ctx.seg == 0 or ctx.talk('E'):
        esc(d, ctx, 200, 1350, 0.7)
    p = ctx.on(1, 0.2)
    if p:
        scroll(d, 90, slide(p, 380), 820, 210, 'Génesis 11 (hebreo)', ['Arfaxad → Selá'], F('title', 48))
    p2 = ctx.on(1, 2.5)
    if p2:
        y2 = slide(p2, 680)
        scroll(d, 90, y2, 820, 260, 'Génesis 11 (Septuaginta)', ['Arfaxad → CAINÁN → Selá'], F('title', 48))
        d.text((500, y2 + 190), 'ἐγέννησεν τὸν Καινάν', font=F('greekb', 50), fill=INK, anchor='mm')
    if ctx.on(1, 6.0):
        arrow(d, (500, 1120), (500, 960), PAL['purple']); pill(d, 500, 1160, 'Lucas 3:36 cita su Biblia griega', PAL['purple'], F('bold', 36))
    nar(d, ctx, 880, 1400, 0.45)

def v_talmud(d, im, ctx):
    p = ctx.on(0, 2.0)
    if p:
        card(d, 70, slide(p, 360), 860, '«El Talmud llama a María hija de Elí»', F('title', 46), title='Lo que repiten muchos', tfont=F('title', 30), tcolor=PAL['gray'], align='c')
    p1 = ctx.on(1, 0.2)
    if p1:
        y = slide(p1, 610)
        rrect(d, (70, y, 930, y + 260), 24, (255, 255, 255), INK, 5)
        d.text((500, y + 50), 'Talmud de Jerusalén, Hagigá 2:2', font=F('title', 34), fill=PAL['teal'], anchor='mm')
        d.text((500, y + 125), '«Miriam, hija de ʿAli Betzalim»', font=F('bold', 44), fill=INK, anchor='mm')
        d.text((500, y + 195), '= «hoja de cebolla»', font=F('bold', 40), fill=PAL['brown'], anchor='mm')
        # cebolla
        d.ellipse((790, y + 150, 880, y + 245), fill=(230, 200, 120), outline=INK, width=4); d.line([(835, y + 150), (835, y + 120)], fill=PAL['green'], width=6)
    if ctx.on(1, 4.5):
        stamp(d, 500, 1000, 'NO ES MARÍA', PAL['red'], 70)
        d.text((500, 1110), 'conjetura de Lightfoot, siglo XVII', font=F('semi', 34), fill=INK, anchor='mm')
    nar(d, ctx, 500, 1390, 0.65)

def v_end(d, im, ctx):
    items = ['No hay contradicción: padre natural y legal', 'Hijo de David por ley (José) y por carne (María)', 'Jeconías: dilema sin salida para la objeción', '«1500» = solo la fórmula; piezas de los s. II-VIII']
    for k, t in enumerate(items):
        sg = 0 if k == 0 else (1 if k == 1 else 2)
        dt = 0.3 if k != 3 else 4.2
        p = ctx.on(sg, dt)
        if not p: continue
        y = slide(p, 380 + k * 175)
        rrect(d, (70, y, 930, y + 145), 24, (255, 255, 255), PAL['green'], 5)
        check(d, 135, y + 72, 1.1)
        ls = wrap(d, t, F('bold', 40), 720)
        for j, l in enumerate(ls): d.text((200, y + 72 + (j - (len(ls) - 1) / 2) * 46), l, font=F('bold', 40), fill=INK, anchor='lm')
    if ctx.on(3, 0.2):
        pill(d, 500, 1130, 'Compártelo · Pide las fuentes en comentarios', PAL['blue'], F('bold', 36))
    nar(d, ctx, 500, 1420, 0.75, arms='up' if ctx.seg == 3 else None)

VIS = dict(hook=v_hook, tree=v_tree, logic=v_logic, levir=v_levir, scan_euseb=v_scan_euseb, zoro=v_zoro, greek=v_greek, roads=v_roads, aaron=v_aaron,
           jecon=v_jecon, scan_ireneo=v_scan_ireneo, y1500=v_y1500, justino=v_justino, timeline=v_timeline, omis=v_omis, cainan=v_cainan, talmud=v_talmud, end=v_end)

SPK_COL = dict(N=PAL['blue'], E=PAL['red'], P=PAL['gold'])
def captions(d, sc, ctx):
    if ctx.seg < 0: return
    g = sc['segs'][ctx.seg]
    st = ctx.st
    if st > g['dur'] + 0.2 or st < -0.05: return
    chs = chunks(g['words'])
    cur = None
    for ch in chs:
        if st >= ch[0][0] - 0.05: cur = ch
    if cur is None: return
    if st > cur[-1][0] + cur[-1][1] + 0.6: return
    f = F('title', 58)
    txt = ' '.join(w[2] for w in cur)
    lines = wrap(d, txt, f, 820)
    lh = 70; h = len(lines) * lh + 30
    y0 = 1660 - h
    rrect(d, (70, y0, 930, y0 + h), 26, (255, 255, 255), SPK_COL[g['spk']], 6)
    # resalta la palabra actual
    idx = 0
    for ch_i, w in enumerate(cur):
        if st >= w[0] - 0.02: idx = ch_i
    k = 0; yy = y0 + 15 + lh / 2
    for l in lines:
        ws = l.split(); x = 500 - d.textlength(l, font=f) / 2
        for w in ws:
            col = SPK_COL[g['spk']] if k == idx else INK
            d.text((x, yy + 3), w, font=f, fill=col, anchor='lm'); x += d.textlength(w + ' ', font=f); k += 1
        yy += lh

def frame(T, gt):
    sc = None
    for s in T:
        if s['start'] <= gt < s['end']: sc = s
    if sc is None: sc = T[-1]
    lt = gt - sc['start']
    im = Image.new('RGB', (W, H))
    bgfill(im, BG[sc['vis']])
    d = ImageDraw.Draw(im)
    ctx = Ctx(sc, lt, gt)
    VIS[sc['vis']](d, im, ctx)
    header(d, sc, ctx)
    captions(d, sc, ctx)
    # fundido entre escenas
    fade = min(lt / 0.25, (sc['end'] - gt) / 0.25, 1.0)
    if fade < 1:
        im = Image.blend(Image.new('RGB', (W, H), (255, 255, 255)), im, max(0.0, fade))
    return im

def mix_audio(T, total, sr=48000):
    out = np.zeros(int((total + 1) * sr), dtype=np.float32)
    for sc in T:
        for g in sc['segs']:
            a, _ = wav_info(f"{B}/aud/{g['key']}.wav")
            i = int(g['t0'] * sr); out[i:i + len(a)] += a
    out = np.clip(out * 0.95, -1, 1)
    w = wave.open(f'{B}/out/voz.wav', 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()

def render_part(args):
    k, n, total = args
    T, _ = build_timeline()
    nf = int(total * FPS)
    a = nf * k // n; b = nf * (k + 1) // n
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', f'{B}/out/part{k}.mp4'], stdin=subprocess.PIPE)
    for fi in range(a, b):
        p.stdin.write(frame(T, fi / FPS).tobytes())
    p.stdin.close(); p.wait()
    return k

if __name__ == '__main__':
    os.makedirs(B + '/out', exist_ok=True)
    T, total = build_timeline()
    print('duración', round(total, 1), 's =', round(total / 60, 2), 'min')
    if len(sys.argv) > 1 and sys.argv[1] == 'preview':
        for t in map(float, sys.argv[2:]):
            frame(T, t).save(f'{B}/out/prev_{t:07.2f}.png')
        for s in T: print(s['i'], s['id'], round(s['start'], 1))
        sys.exit()
    mix_audio(T, total)
    from multiprocessing import Pool
    n = 4
    with Pool(n) as pool:
        list(pool.imap_unordered(render_part, [(k, n, total) for k in range(n)]))
    open(f'{B}/out/list.txt', 'w').write(''.join(f"file 'part{k}.mp4'\n" for k in range(n)))
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', f'{B}/out/list.txt', '-i', f'{B}/out/voz.wav',
                    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', f'{B}/out/genealogias_tiktok.mp4'], check=True)
    print('ok')
