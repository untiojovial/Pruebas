# -*- coding: utf-8 -*-
"""«¿Solo en defensa propia?» en formato papel recortado: línea de tiempo, coreografía, audio y montaje."""
import json, math, os, re, subprocess, sys, wave, hashlib, unicodedata
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, B)
from paper import *
from script3 import SCENES, VOICE, clean

FPS = 30; GAP = 0.30; LEAD = 0.30; TAIL = 0.40; PRE = 0.16
PG = B + '/../jv/pg'; PGH = B + '/../jv/pgh'
MISS = set()

# ------------------------------------------------------------------ línea de tiempo
def hkey(text):
    v, r, p = VOICE; return hashlib.sha1(f'{v}|{r}|{p}|{text}'.encode()).hexdigest()[:12]
def wav(p):
    w = wave.open(p); n = w.getnframes(); sr = w.getframerate()
    return np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768, sr
def nrm(s):
    s = unicodedata.normalize('NFD', s.lower()); return re.sub(r'[^a-z0-9]', '', ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn'))
def token_times(toks, words, dur):
    tt = [None] * len(toks); j = 0
    for off, du, w in words:
        nw = nrm(w)
        if not nw: continue
        for k in range(j, min(j + 5, len(toks))):
            nt = nrm(toks[k][0])
            if nt and (nt.startswith(nw) or nw.startswith(nt)):
                if tt[k] is None: tt[k] = off
                j = k + 1; break
    if tt[0] is None: tt[0] = 0.0
    known = [(i, v) for i, v in enumerate(tt) if v is not None] + [(len(toks), dur)]
    for (i0, v0), (i1, v1) in zip(known, known[1:]):
        for i in range(i0 + 1, i1): tt[i] = v0 + (v1 - v0) * (i - i0) / (i1 - i0)
    return tt
def chunkize(toks, maxw=5, maxc=26):
    out = []; cur = []
    for i, (w, red) in enumerate(toks):
        if cur and (len(cur) >= maxw or len(' '.join(toks[j][0] for j in cur)) + 1 + len(w) > maxc): out.append(cur); cur = []
        cur.append(i)
        if re.search(r'[.,;:!?»]$', w) and len(cur) >= 2: out.append(cur); cur = []
    if cur:
        if len(cur) == 1 and out and len(out[-1]) < maxw and len(' '.join(toks[j][0] for j in out[-1] + cur)) <= maxc + 4: out[-1] += cur
        else: out.append(cur)
    return out
def build():
    T = []; t = 0.0
    for si, s in enumerate(SCENES):
        sc = dict(i=si, id=s['id'], start=t, segs=[]); t += LEAD
        for kind, text, src in s['segs']:
            ct = clean(text); key = hkey(ct); a, sr = wav(f'{B}/audh/{key}.wav'); dur = len(a) / sr
            toks = [(w.replace('*', ''), '*' in w) for w in text.split()]
            tt = token_times(toks, json.load(open(f'{B}/audh/{key}.json')), dur)
            beats = []; lastb = 0.0
            for i in range(1, len(toks)):
                if kind != 'Q' and re.search(r'[.?:!]»?$', toks[i - 1][0]) and tt[i] - lastb > 2.2 and dur - tt[i] > 1.2: beats.append(tt[i] - 0.08); lastb = tt[i]
            sc['segs'].append(dict(kind=kind, text=ct, src=src, key=key, t0=t, dur=dur, toks=toks, tt=tt, chunks=chunkize(toks), beats=beats))
            t += dur + GAP
        t += TAIL - GAP; sc['end'] = t
        for k, g in enumerate(sc['segs']): g['cut'] = sc['start'] if k == 0 else g['t0'] - PRE
        T.append(sc)
    return T, t

class C:
    def __init__(s, sc, gt):
        s.sc = sc; s.gt = gt; s.k = 0
        for k, g in enumerate(sc['segs']):
            if gt >= g['cut']: s.k = k
        s.seg = sc['segs'][s.k]; s.t = gt - s.seg['t0']; s.n = len(sc['segs'])
        s.cut0 = s.seg['cut']; s.cut1 = sc['segs'][s.k + 1]['cut'] if s.k + 1 < s.n else sc['end']
    def w(s, sub, nth=0):
        n = nrm(sub); cnt = 0
        for (tok, _), tm in zip(s.seg['toks'], s.seg['tt']):
            if n in nrm(tok):
                if cnt == nth: return tm
                cnt += 1
        MISS.add((s.sc['id'], s.k, sub)); return 0.0
    def at(s, sub, dt=0.0, dur=0.4, nth=0): return clamp((s.t - s.w(sub, nth) - dt) / dur)
    def p(s, t0, dur=0.4): return clamp((s.t - t0) / dur)
    def shown(s, i0=0): return sum(1 for tm in s.seg['tt'][i0:] if s.t >= tm - 0.04)
    def idx(s, sub):
        n = nrm(sub)
        for i, (tok, _) in enumerate(s.seg['toks']):
            if n in nrm(tok): return i
        MISS.add((s.sc['id'], s.k, sub)); return 0

# ------------------------------------------------------------------ recortes de página
IMH = {}; FOC = {}; VW = {}; DOC = {}
def hires(name):
    if name not in IMH:
        p = f'{PGH}/{name}' if os.path.exists(f'{PGH}/{name}') else f'{PG}/{name}'
        im = Image.open(p).convert('RGB'); a = np.asarray(im).astype(int)
        m = (a[..., 0] > 215) & (a[..., 1] > 185) & (a[..., 2] < 165) & (a[..., 0] - a[..., 2] > 80)
        ys, xs = np.nonzero(m)
        FOC[name] = (xs.min(), ys.min(), xs.max(), ys.max()) if len(xs) > 50 else (0, 0, im.width, im.height)
        PB = 1200; pad = Image.new('RGB', (im.width + 2 * PB, im.height + 2 * PB), (250, 248, 240)); pad.paste(im, (PB, PB))
        IMH[name] = (im.size, pad, PB)
    return IMH[name]
def view(name, bw, bh, z, src=None):
    z = round(clamp(z), 3); k = (name, bw, bh, z, src)
    if k in VW: return VW[k]
    (iw, ih), pad, PB = hires(name)
    if src: ox0, oy0, ox1, oy1 = src; iw2, ih2 = ox1 - ox0, oy1 - oy0
    else: ox0, oy0, iw2, ih2 = 0, 0, iw, ih
    A = bw / bh; fx0, fy0, fx1, fy1 = FOC[name]; cx, cy = (fx0 + fx1) / 2, (fy0 + fy1) / 2
    w0 = iw2; h0 = w0 / A
    if h0 < ih2: c0 = (ox0 + iw2 / 2, min(max(cy, oy0 + h0 / 2), oy0 + ih2 - h0 / 2))
    else: h0 = ih2; w0 = h0 * A; c0 = (ox0 + iw2 / 2, oy0 + ih2 / 2)
    fw = (fx1 - fx0) * 1.10 + 70; fh = (fy1 - fy0) * 1.35 + 90
    if fw / fh < A: fw = fh * A
    fw = min(max(fw, bw * 0.8), w0)
    w = w0 + (fw - w0) * z; h = w / A; cc = (c0[0] + (cx - c0[0]) * z, c0[1] + (cy - c0[1]) * z)
    box = (int(cc[0] - w / 2 + PB), int(cc[1] - h / 2 + PB), int(cc[0] + w / 2 + PB), int(cc[1] + h / 2 + PB))
    out = pad.crop(box).resize((bw, bh), Image.LANCZOS if z in (0.0, 1.0) else Image.BILINEAR)
    if z in (0.0, 1.0): VW[k] = out
    return out
def doc(name, bw, bh, z=1.0, src=None):
    """hoja con marco blanco; devuelve (sprite, estático)"""
    z = round(clamp(z), 3)
    if z in (0.0, 1.0):
        k = (name, bw, bh, z, src)
        if k not in DOC: DOC[k] = sheet(view(name, bw, bh, z, src))
        return DOC[k], True
    return sheet(view(name, bw, bh, z, src)), False

# ------------------------------------------------------------------ ayudas de animación
def pop(st, sp, x, y, p, s=1.0, rot=0.0):
    if p <= 0: return
    put(st, sp, x, y, s * (0.55 + 0.45 * eback(p)), rot + (1 - ease(p)) * 7, min(1.0, p * 3))
def drop(st, sp, x, y, p, rot=0.0, s=1.0, cache=True):
    if p <= 0: return
    e = eback(p) if p < 1 else 1.0; put(st, sp, x, y - (1 - min(e, 1.0)) * 900 - max(0.0, e - 1) * 60, s, rot + (1 - eout(p)) * 12, 1.0, cache)
def fig(st, spec, x, y, s=1.0, **kw): draw_fig(st, figure(**spec), x, y, s, **kw)
def rtag(t, size=56): return tag(t, size, bg=RED, fg=(250, 246, 238))
def btag(t, size=56): return tag(t, size)
def ctag(t, size=48): return tag(t, size, bg=(240, 233, 214), fg=INK, border=INK)
def conc(st, text, x, y, p, size=48):
    """lo que se concede: etiqueta crema con ✓ verde"""
    if p <= 0: return
    sp = ctag(text, size); pop(st, sp, x, y, p, rot=-1.5); pop(st, check(92), x - sp.im.width / 2 + 6, y - 4, clamp(p * 1.2 - .2))
def arrow(st, p1, p2, col=RED, w=9, head=30):
    d = ImageDraw.Draw(st); d.line([p1, p2], fill=col, width=w); a = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
    d.polygon([(p2[0] + head * .5 * math.cos(a), p2[1] + head * .5 * math.sin(a)), (p2[0] + head * math.cos(a + 2.5), p2[1] + head * math.sin(a + 2.5)), (p2[0] + head * math.cos(a - 2.5), p2[1] + head * math.sin(a - 2.5))], fill=col)
def dash(st, p1, p2, col, w=7, seg=24, prog=1.0):
    d = ImageDraw.Draw(st); x1, y1 = p1; x2, y2 = p2; L = math.hypot(x2 - x1, y2 - y1); n = max(1, int(L / seg))
    for k in range(0, int(n * prog), 2):
        a = k / n; b = min(1, (k + 1) / n); d.line([(x1 + (x2 - x1) * a, y1 + (y2 - y1) * a), (x1 + (x2 - x1) * b, y1 + (y2 - y1) * b)], fill=col, width=w)
def mapboard(st, bx, by, s, show=('Meca', 'Medina', 'Badr', 'Jaybar', 'Tabuk'), p=1.0):
    by2 = by + (1 - eout(p)) * 60; a = min(1.0, p * 3)
    put(st, board(600, 720, 220), bx, by2, s, 0, a); mx, my = bx - 300 * s + 20 * s, by2 - 940 * s + 20 * s
    put(st, hijaz_map(show), mx, my, s, 0, a)
    return lambda n: (mx + MAPPT[n][0] * s, my + MAPPT[n][1] * s)
def calendar(st, bx, by, s, header, text, sub=None, old=None, pf=0.0, p=1.0, fs=150):
    by2 = by + (1 - eout(p)) * 60; a = min(1.0, p * 3)
    put(st, board(560, 440, 260), bx, by2, s, 0, a); cy = by2 - 480 * s
    put(st, page(header, text, sub=sub, fs=fs), bx, cy, s, 0, a)
    if old and pf < 1:
        e = ease(pf); put(st, page(*old[:2], sub=old[2] if len(old) > 2 else None, fs=fs), bx + e * 520 * s, cy - math.sin(e * math.pi) * 160 * s + e * e * 300 * s, s, -e * 38, 1 - max(0, pf - .7) / .3)
def crowd(st, x0, y0, cols, rows, p=1.0, dx=44, dy=46, col=(48, 38, 32), fade=0.0, h=60):
    n = cols * rows; sp = pawn(col, h); k = 0
    for r in range(rows):
        for q in range(cols):
            if k / n < p:
                a = 1.0 - 0.82 * clamp((fade * (n + 4) - k) / 4) if fade > 0 else 1.0
                put(st, sp, x0 + q * dx + (r % 2) * dx / 2, y0 + r * dy, 1.0, 0, a)
            k += 1
def qcard_follow(st, c, y=56, w=930, fs=None, i0=0, i1=None, rot=-1.2, t0=-0.1, ref=None):
    toks = tuple(c.seg['toks'][i0:i1]); fs = fs or (50 if len(toks) <= 22 else 44)
    sp, h = qcard(toks, c.shown(i0), w, fs, ref=ref); p = c.p(t0 if i0 == 0 else c.seg['tt'][i0] - 0.3, .4)
    put(st, sp, 540, y - (1 - eout(p)) * (h + 200), 1.0, rot); return h
def qcard_static(st, c, text, t0, y=56, w=930, fs=48, rot=-1.2, ref=None, speed=9.0, x=540):
    toks = tuple((wd.replace('*', ''), '*' in wd) for wd in text.split())
    p = c.p(t0, .4)
    if p <= 0: return 0
    sp, h = qcard(toks, int(max(0, (c.t - t0 - 0.15)) * speed) + 1, w, fs, ref=ref)
    put(st, sp, x, y - (1 - eout(p)) * (h + 200), 1.0, rot); return h
def docdrop(st, c, name, x, y, bw, bh, t0, rot=-2.2, src=None, zmax=1.0, zt=1.2):
    p = c.p(t0, .55)
    if p <= 0: return
    sp, static = doc(name, bw, bh, ease(c.p(t0 + zt, 1.6)) * zmax, src); drop(st, sp, x, y, p, rot, cache=static)
    if p >= 1: put(st, tape(), x - bw * .3, y - bh / 2 - 12, 1, rot + 6); put(st, tape(), x + bw * .3, y - bh / 2 - 12, 1, rot - 5)
def qshot(st, c, name, src=None, zmax=1.0, who=None, bw=840, x=500):
    """plano de cita: tarjeta arriba (se escribe al ritmo de la voz), página real debajo con zoom a lo subrayado"""
    toks = c.seg['toks']; fs = 50 if len(toks) <= 22 else 44
    _, h = qcard(tuple(toks), 0, 930, fs); y1 = 56 + h + 44; bh = int(clamp(1236 - y1, 300, 580))
    docdrop(st, c, name, x, y1 + bh / 2 + 16, bw, bh, 0.1, src=src, zmax=zmax)
    qcard_follow(st, c, fs=fs)
    if who: fig(st, who, 905, 1420, 0.78, aL=88 + 5 * math.sin(c.t * 2.2), tilt=2 * math.sin(c.t * 2.6))

# ------------------------------------------------------------------ reparto
OBJ = dict(coat=WHITE, tunic=WHITE, head='turban', skin=1)
NAR = dict(coat=(64, 88, 128), head='hair', hair=(58, 42, 32), skin=0)
def RAID(k): return dict(coat=[(70, 62, 58), (92, 72, 52), (58, 70, 66)][k % 3], head='keffiyeh', skin=k % 3)
def QUR(k=0): return dict(coat=[(158, 96, 62), (140, 84, 70), (170, 120, 70)][k % 3], head='turban', headcol=(236, 224, 196), skin=(k + 1) % 3)
def SOLD(k=0, col=(122, 100, 70)): return dict(coat=col, head='helmet', skin=k % 3)
def TRIBE(k=0): return dict(coat=[(104, 112, 126), (126, 110, 96), (96, 116, 104)][k % 3], head='kufi', headcol=(70, 62, 60), skin=k % 3)
IK = dict(coat=(48, 84, 64), head='turban', skin=3)
QT = dict(coat=(112, 52, 52), head='turban', skin=1)
JUR1 = dict(coat=(52, 62, 98), head='turban', skin=0); JUR2 = dict(coat=(104, 74, 52), head='turban', skin=2)
JESUS = dict(coat=(164, 46, 46), tunic=WHITE, head='long', hair=(96, 64, 42), beard=(96, 64, 42), trim=None, skin=1)
PETER = dict(coat=(124, 100, 66), tunic=(226, 214, 190), head='hair', hair=(150, 146, 140), beard=(150, 146, 140), trim=None, skin=0)
WATT = dict(coat=(84, 86, 92), tunic=WHITE, head='hair', hair=(176, 172, 166), trim=None, skin=3)
G = 'Ibn Ishaq (trad. Guillaume), p. '

# ------------------------------------------------------------------ escenas
def s_hook(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg('day').copy(); q = c.at('Eso', -0.25, .5)
        if q > 0:
            for sg in (-1, 1): put(st, sword(250), 330, 800, 0.8 + 0.75 * eout(q), 180 + sg * 38, min(1, q * 3))
        p0 = c.p(-0.3, .5); put(st, shield(), 330, 800, 0.6 + 0.4 * eback(p0), 0, min(1, p0 * 3))
        pop(st, tag('DEFENSA PROPIA', 78, bg=(240, 232, 210), fg=INK, border=INK), 330, 812, c.at('defensa', -0.05, .35), rot=4)
        fig(st, OBJ, lerp(1400, 815, eout(c.p(-0.1, .7))), 1190, 1.0, aL=6 + 66 * ease(c.at('defensa', -0.1, .4)), tilt=2 * math.sin(t * 3))
        pop(st, bigword('¿SOLO?', 210), 420, 1310, c.at('Eso', 0, .4), rot=3); pop(st, arrow_curve(), 180, 1120, c.at('Eso', .2, .35))
    elif k == 1:
        st = bg('sand').copy()
        pop(st, btag('LOS POETAS QUE LO CRITICARON', 58), 540, 170, c.at('poetas', -0.1, .35), rot=-2)
        cast = [("Ka'b", "KA'B IBN AL-ASHRAF", dict(coat=(110, 84, 60), head='turban', skin=1)), ('Asma', 'ASMA BINT MARWÁN', dict(coat=(120, 60, 70), head='keffiyeh', headcol=(170, 104, 112), skin=0)),
                ('Afak', 'ABU AFAK', dict(coat=(96, 100, 84), head='turban', headcol=(226, 220, 200), skin=2, beard=(196, 192, 186)))]
        for i, (wd, lab, spec) in enumerate(cast):
            p = c.at(wd, -0.3, .45); x = 200 + i * 340
            if p > 0:
                fig(st, spec, x, 1180 + (1 - eout(p)) * 520, 0.72, aR=28, holdR=scroll())
                pop(st, tag(lab, 42, seed=i), x, 650 - (i % 2) * 86, c.at(wd, 0.05, .35), rot=(-3, 2, -2)[i])
                pop(st, xmark(200), x, 960, c.at(wd, 0.8, .3))
        g = c.at('guerras', -0.15, .4)
        if g > 0:
            for sg in (-1, 1): put(st, sword(250), 540 + sg * 400, 1400, 0.9 * eout(g), 180 - sg * 25, min(1, g * 3))
            pop(st, bigword('LAS GUERRAS', 170), 540, 1290, g, rot=-2)
    else:
        st = bg('desk').copy()
        pop(st, rtag('SOLO FUENTES MUSULMANAS', 62), 540, 200, c.at('musulmanas', -0.15, .35), rot=-2)
        books = [('Corán', 'EL|CORÁN', (52, 96, 70)), ('comentarios', 'TAFSIR', (52, 70, 110)), ('Bujari', 'BUJARI|MUSLIM', (124, 88, 46)), ('biografía', 'IBN|ISHAQ', (124, 50, 54))]
        for i, (wd, ti, col) in enumerate(books):
            drop(st, book(ti, col), 160 + i * 253, 960, c.at(wd, -0.15, .5), rot=(-4, 2, -2, 3)[i], s=1.3)
        pp = c.at('páginas', -0.2, .5)
        if pp > 0:
            sp, _ = doc('g_badr.jpg', 620, 330, 1.0); drop(st, sp, 540, 1240, pp, rot=4)
            pop(st, btag('CON LAS PÁGINAS EN PANTALLA', 46), 540, 1040, c.at('páginas', .25, .35), rot=-2)
    return st

def s_medina(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg('dusk').copy()
        for i, x in enumerate((90, 250)): put(st, house((206, 170, 132) if i else (196, 160, 124)), x, 860, 0.75)
        pop(st, btag('LA MECA', 44), 170, 660, c.p(0.2, .35), rot=-3)
        calendar(st, 760, 1010, 0.82, 'AÑO', '622', p=c.p(-0.2, .5))
        g = c.at('emigran', -0.2, 2.6)
        for i in range(3):
            x = lerp(-160 - i * 150, 430 - i * 150, ease(g)); fig(st, [QUR(0), RAID(1), TRIBE(2)][i] if i else OBJ, x, 1250 + (i % 2) * 26, 0.6, aR=10 + 8 * math.sin(t * 5 + i), aL=10 - 8 * math.sin(t * 5 + i))
        pop(st, btag('DE LA MECA A MEDINA', 50), 420, 520, c.at('emigran', 0.1, .35), rot=2)
        conc(st, 'SUFRIERON PERSECUCIÓN', 560, 250, c.at('persecución', -0.15, .4), 54)
        conc(st, 'PERDIERON SUS CASAS', 560, 360, c.at('casas', -0.2, .4), 54)
    else:
        st = bg('day').copy(); pm = c.p(-0.25, .5); pt = mapboard(st, 430, 1300, 0.98, p=pm)
        pr = c.at('expediciones', -0.6, 1.2)
        if pr > 0:
            mc, bd, tb = pt('Meca'), pt('Badr'), pt('Tabuk'); route = [(mc[0] - 6, mc[1] - 14), (bd[0] - 14, bd[1] + 20), (bd[0] - 50, bd[1] - 150), (tb[0] - 46, tb[1] + 40), (tb[0] - 40, tb[1] - 70)]
            for i, (a, b) in enumerate(zip(route, route[1:])): dash(st, a, b, (176, 122, 30), 9, prog=clamp(pr * 4 - i))
        pop(st, tag('RUTA DE CARAVANAS A SIRIA', 32, bg=(196, 146, 44), fg=INK), pt('Meca')[0] + 30, pt('Meca')[1] + 84, c.at('caravanas', -0.1, .35), rot=-2)
        tg = [(pt('Badr')[0] + 30, pt('Badr')[1] - 40), (pt('Medina')[0] - 130, pt('Medina')[1] - 60), (pt('Medina')[0] - 70, pt('Medina')[1] + 150)]
        for i, (x, y) in enumerate(tg):
            q = c.at('expediciones', 0.2 + i * 0.5, .5)
            if q > 0: m = pt('Medina'); arrow(st, m, (m[0] + (x - m[0]) * eout(q), m[1] + (y - m[1]) * eout(q)), RED, 10)
        g = c.at('caravanas', -0.2, 6.0)
        for i in range(2): put(st, camel(load=True, seed=i), lerp(1300 + i * 260, 760 + i * 250, eout(g)), 1390 - i * 20, 0.55)
        pop(st, btag('EXPEDICIONES', 60), 850, 300, c.at('expediciones', -0.1, .35), rot=3)
        conc(st, 'VARIAS, SIN COMBATE', 850, 440, c.at('Varias', -0.1, .4), 42)
        pop(st, rtag('OBJETIVO: LA CARAVANA', 50), 800, 590, c.at('objetivo', -0.1, .35), rot=-3)
    return st

def raiders(st, c, x0=130, y=1210, s=0.62, up=0.0, n=3, dx=150, slide=1.0):
    for i in range(n):
        fig(st, RAID(i), lerp(-200 - i * 120, x0 + i * dx, eout(slide)), y + (i % 2) * 22, s, aR=14 + up * (126 if i != 1 else 136), holdR=sword(), tilt=2 * math.sin(c.t * 2 + i))

def s_nakhla(c):
    k, t = c.k, c.t; st = bg('night').copy()
    if k == 0:
        put(st, palm(1), 120, 800, 0.9); put(st, palm(2), 980, 790, 0.8)
        pop(st, btag('NAJLA · ENTRE LA MECA Y TAIF', 50), 540, 170, c.at('Najla', -0.1, .35), rot=-2)
        raiders(st, c, slide=c.at('grupo', -0.4, .8))
        drop(st, letter(), 640, 620, c.at('carta', -0.2, .55), rot=-4, s=1.15)
        pop(st, rtag('ACECHAD', 64), 800, 900, c.at('acechad', -0.05, .35), rot=5)
    elif k == 1:
        qshot(st, c, 'g_nakhla.jpg')
        fig(st, RAID(1), 905, 1420, 0.78, aL=20 + 126 * ease(c.at('matar', -0.1, .4)), holdL=sword(), tilt=2 * math.sin(t * 2.6))
    else:
        put(st, palm(1), 120, 800, 0.9)
        calendar(st, 250, 1230, 0.72, 'MES SAGRADO', 'RAJAB', sub='NO HAY GUERRA', p=c.p(-0.2, .5), fs=130)
        conc(st, 'PRIMERO LO DESAPRUEBA', 720, 200, c.at('desaprueba', -0.3, .4), 46)
        hq = qcard_static(st, c, 'Luchar en él es grave… pero la persecución es *peor* *que* *matar*.', c.w('versículo') - 0.1, y=270, w=880, fs=46, ref='CORÁN 2:217')
        g = c.at('toma', -0.2, 1.4)
        raiders(st, c, x0=620, y=1330, s=0.5, n=3, dx=120, slide=c.p(0.2, .8))
        put(st, camel(load=True), lerp(1300, 880, eout(g)), 1100, 0.6); put(st, camel((176, 132, 90), load=True, seed=2), lerp(1500, 1010, eout(g)), 1150, 0.5)
        pop(st, rtag('Y TOMA LA CARAVANA', 56), 760, 830, c.at('toma', 0.1, .35), rot=-3)
    return st

def caravan(st, c, x0, y, p, n=3, s=0.62, lead=True):
    for i in range(n): put(st, camel((196, 150, 100) if i % 2 == 0 else (178, 134, 92), load=True, seed=i), x0 + i * 250 + (1 - eout(p)) * 900, y + (i % 2) * 18 + 3 * math.sin(c.t * 3 + i), s)
    if lead: fig(st, QUR(0), x0 - 190 + (1 - eout(p)) * 900, y + 30, s * 0.95, aR=12)

def s_badr(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg('day').copy()
        calendar(st, 250, 1000, 0.72, 'AÑO', '624', old=('AÑO', '622'), pf=c.p(0.1, .7), p=1.0)
        pop(st, btag('BADR', 84), 250, 250, c.at('Badr', -0.1, .35), rot=-3)
        pop(st, qmark(300), 800, 380, c.at('Empezó', -0.1, .4), rot=6)
        pop(st, ctag('¿ATACÓ LA MECA A MEDINA?', 44), 720, 600, c.at('Empezó', 0.2, .35), rot=-2)
        caravan(st, c, 470, 1230, c.at('Abu', -0.5, 1.2))
        pop(st, btag('ABU SUFYÁN', 44), 300, 1330, c.at('Abu', 0.3, .35), rot=2)
        pop(st, tag('DE SIRIA A LA MECA', 40, bg=(190, 140, 40), fg=INK), 800, 880, c.at('Siria', 0, .35), rot=-2)
    elif k == 1:
        st = bg('desk').copy(); qshot(st, c, 'g_badr.jpg', who=NAR)
    else:
        st = bg('day').copy(); caravan(st, c, 560, 1120, 1.0, lead=False, s=0.55)
        g = c.at('salieron', -0.3, .9)
        for i in range(4): fig(st, SOLD(i, (150, 90, 60)), lerp(1300 + i * 100, 300 + i * 170, eout(g)), 1300 + (i % 2) * 30, 0.62, aR=16, holdR=spear())
        pop(st, btag('SALEN A PROTEGER SU CARAVANA', 50), 540, 250, c.at('proteger', -0.3, .35), rot=-2)
        pop(st, rtag('LA BATALLA VINO DESPUÉS', 66), 540, 420, c.at('batalla', -0.1, .35), rot=2)
    return st

def s_kab(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg('night').copy(); put(st, fortress(), 300, 900, 0.9, 0, min(1, c.p(-0.2, .4) * 2))
        pop(st, btag('DESPUÉS DE BADR', 60), 540, 180, c.p(0.0, .35), rot=-2)
        pop(st, btag("KA'B IBN AL-ASHRAF", 40), 300, 560, c.at('críticos', -0.1, .35), rot=2)
        docdrop(st, c, 'b4037.jpg', 690, 900, 520, 560, c.w('Bujari') - 0.3, rot=3, zmax=0.0)
        pop(st, btag('SAHIH AL-BUJARI 4037', 50), 690, 590, c.at('Bujari', 0.2, .35), rot=-3)
    elif k == 1:
        st = bg('desk').copy(); qshot(st, c, 'b4037.jpg')
        fig(st, RAID(0), 905, 1420, 0.78, aL=88 + 5 * math.sin(t * 2.2), tilt=2 * math.sin(t * 2.6))
    elif k == 2:
        st = bg('desk').copy()
        docdrop(st, c, 'g_kab2.jpg', 540, 900, 960, 560, -0.05, rot=-1.5)
        qcard_static(st, c, '*Matad* a cualquier judío que caiga en vuestro poder.', c.w('Matad') - 0.25, y=70, fs=54, ref=G.upper() + '369')
        pop(st, btag('A LA MAÑANA SIGUIENTE', 50), 540, 1290, c.at('mañana', -0.2, .35), rot=-2)
    else:
        st = bg('day').copy(); p0 = c.p(-0.2, .5)
        put(st, kaaba(), 270, 1000 + (1 - eout(p0)) * 60, 1.0, 0, min(1, p0 * 3))
        pop(st, btag('LA MECA · AÑO 630', 54), 330, 250, c.at('Meca', -0.1, .35), rot=-2)
        docdrop(st, c, 'g_mecca.jpg', 710, 1130, 640, 400, c.w('excluidos') - 0.4, rot=3)
        pop(st, rtag('EXCLUIDOS DEL PERDÓN', 60), 700, 420, c.at('excluidos', -0.05, .35), rot=3)
        pop(st, ctag('«AUNQUE ESTÉN BAJO LAS CORTINAS DE LA KAABA»', 34), 540, 560, c.at('aunque', -0.1, .35), rot=-2)
    return st

_FLIP = {}
def flip(sp):
    if sp.k not in _FLIP: _FLIP[sp.k] = Sp(sp.im.transpose(Image.FLIP_LEFT_RIGHT), sp.im.width - sp.ax, sp.ay)
    return _FLIP[sp.k]
def camp(st, c):
    put(st, tent(), 170, 880, 0.9); put(st, tent((170, 120, 86)), 930, 860, 0.8); put(st, well(), 540, 1010, 1.0)
    put(st, camel((190, 146, 98), seed=4), 300, 1010, 0.5); put(st, flip(camel((178, 134, 92), seed=5)), 790, 1010, 0.5)

def s_mustaliq(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg('dusk').copy(); camp(st, c)
        for i in range(3): fig(st, TRIBE(i), 300 + i * 230, 1300 + (i % 2) * 24, 0.6, tilt=2 * math.sin(t * 2 + i))
        pop(st, btag('SAHIH AL-BUJARI 2541', 50), 540, 180, c.p(0.1, .35), rot=-2)
        pop(st, btag('BANU AL-MUSTALIQ', 76), 540, 330, c.at('tribu', -0.1, .35), rot=2)
    elif k == 1:
        st = bg('desk').copy(); qshot(st, c, 'b2541.jpg')
        pop(st, rtag('SIN AVISO', 80), 860, 1330, c.at('aviso', -0.1, .35), rot=-6)
    else:
        st = bg('dusk').copy(); camp(st, c)
        for i in range(3): fig(st, TRIBE(i), 520 + i * 190, 1300 + (i % 2) * 24, 0.55)
        conc(st, 'IBN ISHAQ: «SE REUNÍAN CONTRA ÉL»', 560, 180, c.at('motivo', -0.2, .4), 44)
        g = c.at('sorpresa', -0.5, .7)
        if g > 0: raiders(st, c, x0=60, y=1340, s=0.55, up=ease(g), n=3, dx=130, slide=g)
        pop(st, rtag('ATAQUE POR SORPRESA', 64), 540, 330, c.at('sorpresa', -0.1, .35), rot=-3)
        qcard_static(st, c, 'Invitar al islam antes de atacar era cosa de *los* *primeros* *tiempos*.', c.w('Muslim') - 0.2, y=450, w=880, fs=44, ref="SAHIH MUSLIM 1730 · NAFI'")
    return st

def s_qurayza(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg('sand').copy(); put(st, fortress(520, 300, (170, 150, 124)), 300, 1000, 0.95)
        for i in range(3): fig(st, TRIBE(i + 1), 620 + i * 170, 1290 + (i % 2) * 22, 0.58)
        pop(st, btag('BANU QURAYZA · MEDINA, 627', 54), 540, 170, c.p(0.0, .35), rot=-2)
        conc(st, 'ACUSADOS DE TRAICIÓN', 520, 310, c.at('traición', -0.2, .4), 50)
        conc(st, 'LO CONCEDEMOS', 640, 420, c.at('Concedámoslo', -0.1, .4), 50)
        pop(st, bigword('¿SENTENCIA?', 150), 540, 590, c.at('Cuál', -0.1, .4), rot=-3)
    elif k == 1:
        st = bg('desk').copy(); qshot(st, c, 'g_qurayza.jpg', who=NAR)
    else:
        st = bg('sand').copy()
        pop(st, btag('MERCADO DE MEDINA', 50), 540, 170, c.p(0.0, .35), rot=-2)
        put(st, trench(820), 540, 1120, 1.0, 0, c.at('zanjas', -0.2, .4))
        g = c.at('decapitaron', 0.0, 3.0)
        crowd(st, 150, 760, 18, 5, p=c.p(0.3, 1.6), fade=g, dx=44, dy=62)
        pop(st, bigword('600-700', 190), 540, 1290, c.at('Seiscientos', -0.1, .4), rot=-2)
        pop(st, rtag('ALGUNOS DICEN: 800-900', 54), 540, 440, c.at('Algunos', -0.1, .35), rot=2)
    return st

def s_khaybar(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg('dawn').copy(); pt = mapboard(st, 400, 1300, 0.98, p=c.p(-0.25, .5)); q = c.at('kilómetros', -0.8, .8)
        if q > 0:
            m, j = pt('Medina'), pt('Jaybar'); arrow(st, m, (m[0] + (j[0] - m[0]) * eout(q), m[1] + (j[1] - m[1]) * eout(q) + 14), RED, 11)
        pop(st, rtag('150 KM', 46), pt('Jaybar')[0] + 190, pt('Jaybar')[1] + 60, c.at('kilómetros', -0.1, .35), rot=-4)
        pop(st, btag('JAYBAR · AÑO 628', 60), 830, 260, c.p(0.0, .35), rot=3)
        pop(st, ctag('OASIS JUDÍO', 46), 850, 390, c.at('oasis', -0.1, .35), rot=-2)
        conc(st, 'NO SITIABA MEDINA', 800, 560, c.at('sitiando', -0.2, .4), 44)
    elif k == 1:
        st = bg('desk').copy(); qshot(st, c, 'g_khaybar.jpg', who=NAR)
    else:
        st = bg('dawn').copy(); put(st, fortress(), 770, 1240, 0.8)
        for i in range(3): fig(st, SOLD(i), 110 + i * 150, 1390 + (i % 2) * 20, 0.5, aR=14, holdR=spear())
        pop(st, sign('¿LLAMADA A LA ORACIÓN?', 600, 110, fs=54), 400, 170, c.p(0.1, .35))
        pop(st, sign('SÍ: SE DETENÍA', 430, 100, fs=50, col=(214, 232, 212)), 250, 300, c.at('atacado', -0.6, .35), rot=-2)
        pop(st, sign('NO: ATACABA', 400, 100, fs=50, col=(240, 204, 200)), 700, 300, c.at('atacado', -0.2, .35), rot=2)
        pop(st, rtag('EL CRITERIO: SER MUSULMÁN', 60), 540, 450, c.at('musulmanes', -0.2, .35), rot=-2)
        qcard_static(st, c, 'Dios es grande, Jaybar está *destruida*.', c.w('Dios') - 0.2, y=540, w=820, fs=52, ref=G.upper() + '511')
    return st

def s_tabuk(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg('day').copy(); pt = mapboard(st, 400, 1300, 0.98, p=c.p(-0.25, .5)); q = c.at('Tabuk', -0.1, 1.0)
        if q > 0:
            m, j = pt('Medina'), pt('Tabuk'); arrow(st, m, (m[0] + (j[0] - m[0] + 20) * eout(q), m[1] + (j[1] - m[1] + 26) * eout(q)), RED, 12)
        pop(st, btag('TABUK · AÑO 9 H. (630)', 54), 800, 240, c.at('Tabuk', -0.1, .35), rot=3)
        pop(st, bigword('30.000', 108), 812, 420, c.at('treinta', -0.1, .4), rot=-3)
        crowd(st, 670, 560, 8, 4, p=c.at('treinta', 0.1, 1.2), dx=40, dy=50)
        pop(st, tag('CONTRA LOS BIZANTINOS', 40, bg=(120, 40, 50), fg=(250, 246, 238)), 830, 800, c.at('bizantinos', -0.1, .35), rot=2)
        pop(st, rtag('~700 KM', 46), pt('Jaybar')[0] - 150, pt('Jaybar')[1] - 10, c.at('setecientos', -0.1, .35), rot=-62)
        pop(st, btag('CORÁN 9:29', 64), 820, 960, c.at('Corán', -0.1, .35), rot=-3)
    elif k == 1:
        st = bg('desk').copy(); qshot(st, c, 'w_q929.png', src=(0, 0, 1064, 620), zmax=0.3)
    else:
        st = bg('desk').copy(); docdrop(st, c, 'ik929.jpg', 470, 720, 800, 800, -0.05, rot=-2)
        fig(st, IK, 900, 1420, 0.8, aL=88 + 5 * math.sin(t * 2.2), tilt=2 * math.sin(t * 2.6))
        pop(st, btag('IBN KATHIR · SIGLO XIV', 46), 760, 1150, c.p(0.3, .35), rot=3)
        pop(st, rtag('JUDÍOS Y CRISTIANOS', 62), 400, 1260, c.at('judíos', -0.1, .35), rot=-3)
        pop(st, btag('CONTRA LOS ROMANOS', 50), 420, 1380, c.at('romanos', -0.2, .35), rot=2)
    return st

def steps(st, c, k):
    S = [('1', 'INVÍTALOS AL ISLAM', (58, 128, 76), 'invítalos'), ('2', 'SI NO: EXIGE EL TRIBUTO', (196, 140, 40), 'exígeles'), ('3', 'SI NO: COMBÁTELOS', RED, 'combátelos')]
    for i, (n, tx, col, wd) in enumerate(S):
        p = c.at(wd, -0.15, .4) if k == 2 else 1.0
        pop(st, sign(tx, 760, 130, num=n, nc=col, fs=62), 540, 430 + i * 190, p, rot=(-1.5, 1, -1)[i])
        if i < 2 and p >= 1 and (k == 3 or c.at(S[i + 1][3], -0.5, .3) > 0): arrow(st, (540, 505 + i * 190), (540, 548 + i * 190), INK, 9, 26)

def s_hadith(c):
    k, t = c.k, c.t; st = bg('desk').copy()
    if k == 0:
        pop(st, btag('NO ES SOLO HISTORIA', 70), 540, 200, c.p(0.1, .35), rot=-2)
        pop(st, bigword('ES DOCTRINA', 170), 540, 400, c.at('doctrina', -0.2, .4), rot=2)
        docdrop(st, c, 'b25.jpg', 540, 960, 760, 520, c.w('Bujari') - 0.3, rot=-2, zmax=0.0)
        pop(st, btag('SAHIH AL-BUJARI 25', 54), 540, 680, c.at('Bujari', 0.2, .35), rot=3)
    elif k == 1:
        qshot(st, c, 'b25.jpg', who=NAR)
    else:
        pop(st, btag('SAHIH MUSLIM 1731 · INSTRUCCIONES A LOS EJÉRCITOS', 40), 540, 200, c.p(0.0, .35) if k == 2 else 1.0, rot=-1.5)
        steps(st, c, k)
        for i in range(2): fig(st, SOLD(i), 130 + i * 820, 1400, 0.6, aR=14, holdR=spear())
        if k == 3:
            pop(st, rtag('NO DEPENDE DE QUE TE ATAQUEN', 62), 540, 1060, c.at('depende', -0.2, .35), rot=-2)
            pop(st, btag('DEPENDE DE: ISLAM O TRIBUTO', 52), 540, 1190, c.at('Depende', -0.1, .35, nth=1), rot=2)
    return st

def s_sword(c):
    k, t = c.k, c.t; st = bg('desk').copy()
    if k == 0:
        sw = c.at('Ibn', -0.3, .5)
        if sw <= 0: docdrop(st, c, 'w_q95.png', 500, 800, 840, 500, 0.0, src=(0, 0, 1064, 620), zmax=0.3)
        else: docdrop(st, c, 'ik95b.jpg', 500, 850, 840, 560, c.w('Ibn') - 0.3)
        qcard_static(st, c, '*Matad* a los politeístas dondequiera que los encontréis.', c.w('Matad') - 0.3, y=70, fs=52, ref='CORÁN 9:5')
        g = c.at('espada', -0.2, .5)
        if g > 0: put(st, sword(250), 980, 1420, 1.4 * eout(g), 180 + 14, min(1, g * 3))
        pop(st, rtag('EL VERSÍCULO DE LA ESPADA', 62), 480, 1290, c.at('espada', -0.1, .35), rot=-3)
        pop(st, btag('«ABROGÓ TODO PACTO DE PAZ»', 48), 470, 1400, c.at('abrogó', -0.1, .35), rot=2)
    elif k == 1:
        docdrop(st, c, 'ik95.jpg', 500, 900, 840, 560, -0.05)
        qcard_static(st, c, 'Búscalos y sítialos en sus fortalezas, para que no les quede más opción que *morir* o abrazar el islam.', c.w('Búscalos') - 0.2, y=64, fs=46, ref='TAFSIR IBN KATHIR · SOBRE 9:5')
        fig(st, IK, 905, 1420, 0.78, aL=88 + 5 * math.sin(t * 2.2), tilt=2 * math.sin(t * 2.6))
    else:
        docdrop(st, c, 'w_qurtubi_2193.png', 500, 620, 860, 420, -0.05, src=(0, 280, 1064, 760), zmax=0.35)
        pop(st, btag('AL-QURTUBI · SIGLO XIII', 50), 380, 180, c.p(0.2, .35), rot=-2)
        fig(st, QT, 905, 1420, 0.78, aL=88 + 5 * math.sin(t * 2.2), tilt=2 * math.sin(t * 2.6))
        qcard_static(st, c, 'Es una orden de combatir *sin* *la* *condición* de que empiecen los incrédulos.', c.w('escribe') + 0.2, y=860, w=740, fs=42, ref='SOBRE CORÁN 2:193', x=400)
        pop(st, rtag('LA CAUSA: LA INCREDULIDAD', 58), 440, 1330, c.at('causa', -0.1, .35), rot=-3)
    return st

def s_fiqh(c):
    k, t = c.k, c.t; st = bg('room').copy()
    if k == 0:
        pop(st, btag('DERECHO ISLÁMICO CLÁSICO', 62), 540, 200, c.at('manuales', -0.3, .35), rot=-2)
        drop(st, book('RELIANCE|OF THE|TRAVELLER', (60, 84, 70), 250, 330, 40), 380, 1010, c.at('Reliance', -0.4, .5), rot=-3, s=1.5)
        fig(st, JUR1, 800, 1230, 0.85, aL=40 + 30 * ease(c.at('Reliance', -0.2, .4)), tilt=2 * math.sin(t * 2.6))
        pop(st, ctag('MANUAL SHAFIÍ · SIGLO XIV', 44), 420, 440, c.at('shafií', -0.1, .35), rot=2)
    elif k == 1:
        sw = c.at('combate', -0.4, .1)
        toks = c.seg['toks']; _, h = qcard(tuple(toks), 0, 930, 44); y1 = 56 + h + 44; bh = int(clamp(1236 - y1, 300, 580))
        if sw <= 0: docdrop(st, c, 'rel98.jpg', 500, y1 + bh / 2 + 16, 840, bh, 0.1)
        else: docdrop(st, c, 'rel99.jpg', 500, y1 + bh / 2 + 16, 840, bh, c.w('combate') - 0.4, zt=0.5)
        qcard_follow(st, c, fs=44); fig(st, JUR1, 905, 1420, 0.78, aL=88 + 5 * math.sin(t * 2.2), tilt=2 * math.sin(t * 2.6))
    else:
        fig(st, JUR2, 250, 1340, 0.72, aR=30, holdR=scroll(), tilt=2 * math.sin(t * 2.6) if c.at('Rushd', 0, .1) <= 0 else 0)
        pop(st, btag('IBN QUDAMA · HANBALÍ', 44), 270, 800, c.p(0.0, .35), rot=-3)
        qcard_static(st, c, 'La yihad, como mínimo, *una* *vez* *al* *año*.', c.w('yihad') - 0.2, y=64, w=820, fs=48, ref='IBN QUDAMA · AL-MUGHNI')
        g = c.at('Rushd', -0.5, .6)
        if g > 0:
            fig(st, JUR1 | dict(coat=(96, 60, 84)), lerp(1350, 830, eout(g)), 1340, 0.72, aL=30, holdL=scroll(), tilt=2 * math.sin(t * 2.6))
            pop(st, btag('IBN RUSHD · MALIKÍ', 44), 820, 800, c.at('Rushd', 0.0, .35), rot=3)
            qcard_static(st, c, 'Los juristas están de acuerdo en que se combate a *todos* *los* *politeístas*.', c.w('juristas') - 0.2, y=330, w=880, fs=44, ref='IBN RUSHD · BIDAYAT AL-MUYTAHID')
    return st

def balance(st, x, y, s, ang, left=(), right=()):
    post, beam, pan = scale_parts(); put(st, post, x, y, s); by = y - 570 * s; a = math.radians(ang)
    for sg, items in ((-1, left), (1, right)):
        ex, ey = x + sg * 340 * s * math.cos(a), by - sg * 340 * s * math.sin(a); put(st, pan, ex, ey, s); yy = ey + 236 * s
        for it in items:
            sp, p = it[:2]; dx = it[2] if len(it) > 2 else 0; adv = it[3] if len(it) > 3 else True
            if p > 0: pop(st, sp, ex + dx, yy - sp.im.height / 2 + 26, p)
            if p > 0 and adv: yy -= (sp.im.height - 2 * SPAD - 6)
    put(st, beam, x, by, s, ang)

def s_counter(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg('day').copy(); fig(st, OBJ, lerp(-300, 250, eout(c.p(-0.1, .6))), 1250, 0.95, aR=30 + 60 * ease(c.at('Corán', -0.2, .4)), tilt=2.5 * math.sin(t * 3))
        pop(st, btag('TE RESPONDERÁN…', 54), 300, 640, c.p(0.0, .35), rot=-3)
        qcard_follow(st, c, y=70, fs=48, i0=c.idx('combatid'), ref='CORÁN 2:190 · 22:39')
    elif k == 1:
        st = bg('day').copy(); fig(st, OBJ, 250, 1250, 0.95, aR=30)
        pop(st, btag('ES VERDAD', 80), 600, 200, c.p(0.0, .35), rot=-2)
        conc(st, 'CORÁN 2:190 Y 22:39: DEFENSA', 600, 380, c.at('Dos', -0.1, .4), 50)
        conc(st, 'IBN KATHIR: NO MATAR', 660, 520, c.at('prohíbe', -0.3, .4), 50)
        for i, (wd, lab) in enumerate((('mujeres', 'MUJERES'), ('niños', 'NIÑOS'), ('ancianos', 'ANCIANOS'), ('monjes', 'MONJES'))):
            pop(st, ctag(lab, 44), 560 + (i % 2) * 260, 650 + (i // 2) * 100, c.at(wd, -0.1, .35), rot=(-2, 2, 2, -2)[i])
    elif k == 2:
        st = bg('day').copy(); camps = ['Najla', 'Badr', 'Mustaliq', 'Jaybar', 'Tabuk']
        R = [(rtag('9:5', 46), c.at('espada', -0.6, .35), -62, False), (rtag('9:29', 46), c.at('veintinueve', -0.3, .35), 62, True)]
        R += [(btag(n.upper(), 30), c.at(n, -0.1, .35), (-70, 70)[i % 2] if i < 4 else 0, i % 2 == 1 or i == 4) for i, n in enumerate(camps)]
        wgt = sum(1 for it in R if it[1] > 0) + (1 if c.at('espada', -0.6, .35) > 0 else 0); ang = lerp(9, -13, ease(wgt / 8))
        balance(st, 540, 1340, 0.98, ang + 0.6 * math.sin(t * 2), left=[(ctag('2:190', 46), c.p(0.2, .35))], right=R)
        pop(st, ctag('«FUE SOLO EL PRINCIPIO»', 46), 540, 180, c.at('principio', -0.3, .35), rot=-2)
        conc(st, 'IBN KATHIR: 2:190 NO ESTÁ ABROGADO', 560, 300, c.at('cree', -0.5, .4), 40)
        pop(st, rtag('NO FUE SOLO DEFENSA', 66), 540, 440, c.at('solo', -0.2, .35, nth=1), rot=2)
    elif k == 3:
        st = bg('desk').copy(); docdrop(st, c, 'watt231.jpg', 470, 640, 780, 760, c.w('escribió') - 0.6, rot=-2, zt=1.0)
        fig(st, WATT, lerp(1400, 900, eout(c.p(-0.1, .6))), 1420, 0.8, aL=20 + 68 * ease(c.at('escribió', -0.2, .4)), tilt=2 * math.sin(t * 2.6))
        pop(st, btag('W. M. WATT · OXFORD, 1956', 48), 420, 160, c.at('Watt', -0.1, .35), rot=-2)
        pop(st, ctag('NADA HOSTIL AL ISLAM', 40), 470, 250, c.at('hostil', -0.2, .35), rot=2) if c.at('escribió', -0.6, .1) <= 0 else None
        pop(st, rtag('OFENSIVAS', 70), 300, 1180, c.at('ofensivas', -0.1, .35), rot=-4)
        pop(st, rtag('«INCLUSO BADR FUE UNA RAZIA»', 50), 420, 1320, c.at('Incluso', -0.1, .35), rot=2)
    else:
        st = bg('day').copy()
        pop(st, btag("IBN SA'D · TABAQAT", 54), 540, 180, c.p(0.0, .35), rot=-2)
        pop(st, numcard('27', 'EXPEDICIONES|DIRIGIDAS POR ÉL'), 520, 420, c.at('veintisiete', -0.1, .4), 1.25)
        pop(st, numcard('47', 'EXPEDICIONES|ENVIADAS'), 520, 720, c.at('cuarenta', -0.1, .4), 1.25)
        for i in range(4): fig(st, SOLD(i) if i % 2 else RAID(i), 140 + i * 270, 1420, 0.5, aR=120 if i % 2 == 0 else 14, holdR=flag() if i % 2 == 0 else spear())
        pop(st, bigword('¿TODAS EN DEFENSA?', 120), 540, 1000, c.at('Todas', -0.1, .4), rot=-2)
    return st

def s_jesus(c):
    k, t = c.k, c.t; st = bg('garden').copy()
    put(st, palm(5), 110, 800, 0.9); put(st, palm(6), 990, 790, 0.75)
    if k <= 1:
        up = 1.0 if k == 0 else 1 - ease(c.at('Vuelve', 0.6, 1.4))
        pin = c.p(-0.1, .6) if k == 0 else 1.0
        fig(st, SOLD(1, (120, 40, 50)), lerp(1400, 985, eout(pin)), 1320, 0.58, aL=14, holdL=spear())
        fig(st, PETER, 700, 1270, 0.78, aR=14 + 130 * up * ease(c.at('sacó', -0.2, .4) if k == 0 else 1), holdR=sword(), tilt=2 * math.sin(t * 2))
        fig(st, JESUS, 270, 1270, 0.86, aR=20 + 50 * (ease(c.at('dijo', -0.4, .4)) if k == 0 else 1), tilt=(2 * math.sin(t * 2.6) if k == 1 else 0))
        if k == 0:
            pop(st, btag('COMPÁRALO CON JESÚS', 62), 540, 190, c.p(0.0, .35), rot=-2); pop(st, ctag('GETSEMANÍ', 44), 540, 320, c.at('Pedro', -0.1, .35), rot=2)
            pop(st, btag('PEDRO', 40), 700, 650, c.at('Pedro', 0.0, .35), rot=3)
        else: qcard_follow(st, c, y=70, fs=52, ref='MATEO 26:52')
    else:
        fig(st, JESUS, 300, 1280, 0.92, aR=40, tilt=2 * math.sin(t * 2.6))
        qcard_static(st, c, 'Mi reino *no* *es* *de* *este* *mundo*. Si lo fuera, mis servidores pelearían.', c.w('reino') - 0.4, y=64, w=900, fs=46, ref='JUAN 18:36')
        g = c.at('discípulos', -0.3, .6)
        if g > 0:
            for i in range(2): fig(st, PETER | dict(coat=[(96, 110, 90), (124, 100, 66)][i], hair=[(70, 50, 36), (150, 146, 140)][i], beard=None), lerp(1400, 700 + i * 200, eout(g)), 1300 + i * 20, 0.66, aR=20 + 100 * ease(c.at('fuego', -0.2, .4)) * (1 - ease(c.at('reprendió', 0, .5))))
        pop(st, rtag('¿FUEGO DEL CIELO?', 50), 800, 800, c.at('fuego', -0.1, .35), rot=3)
        if c.at('reprendió', -0.1, .3) > 0: pop(st, xmark(130), 800, 920, c.at('reprendió', -0.1, .3))
        qcard_static(st, c, 'El Hijo del Hombre no ha venido a destruir vidas, sino a *salvarlas*.', c.w('Hijo') - 0.5, y=360, w=900, fs=46, ref='LUCAS 9:55-56')
    return st

def s_end(c):
    k, t = c.k, c.t; st = bg('day').copy()
    S = [('1', 'EXPEDICIONES CONTRA CARAVANAS', 'Uno'), ('2', 'ATAQUES POR SORPRESA', 'Dos'), ('3', 'COMBATIR HASTA EL ISLAM O EL TRIBUTO', 'Tres'), ('4', 'ASÍ LO ENTENDIERON LOS CLÁSICOS', 'Cuatro')]
    if k <= 1:
        pop(st, btag('RESUMEN', 84), 540, 180, c.p(0.0, .35) if k == 0 else 1.0, rot=-2)
        for i, (n, tx, wd) in enumerate(S):
            p = 1.0 if (k == 1 and i < 2) else (c.at(wd, -0.15, .4) if (i // 2) == k else 0.0)
            pop(st, sign(tx, 900, 130, num=n, nc=RED, fs=50 if len(tx) > 30 else 56), 540, 380 + i * 180, p, rot=(-1.2, 1, -1, 1.2)[i])
        fig(st, NAR, 540, 1440, 0.62, aR=20 + 20 * math.sin(t * 2), aL=20 - 20 * math.sin(t * 2))
    else:
        conc(st, 'RESPETO A LOS MUSULMANES', 560, 170, c.at('respetamos', -0.4, .4), 50)
        pop(st, btag('RIGOR CON LAS FUENTES', 54), 540, 290, c.at('fuentes', -0.3, .35), rot=2)
        q = c.at('pregunta', -0.2, .5)
        if q > 0:
            for sg in (-1, 1): put(st, sword(250), 330, 800, 0.8 + 0.75 * eout(q), 180 + sg * 38, min(1, q * 3))
            put(st, shield(), 330, 800, 0.6 + 0.4 * eback(q), 0, min(1, q * 3)); pop(st, tag('DEFENSA PROPIA', 78, bg=(240, 232, 210), fg=INK, border=INK), 330, 812, clamp(q * 1.5 - .5), rot=4)
            fig(st, NAR, lerp(1400, 815, eout(q)), 1190, 1.0, aL=6 + 66 * ease(c.at('verdad', -0.2, .4)), tilt=2 * math.sin(t * 3))
        pop(st, bigword('¿SOLO?', 210), 420, 1310, c.at('defensa', -0.3, .4), rot=3)
        pc = c.at('Comenta', -0.2, .35); pop(st, pill('COMENTA', size=58), 300, 480, pc); pop(st, pill('PIDE LAS FUENTES', bg=RED, fg=(250, 246, 238), size=58), 730, 480, c.at('pídelas', -0.2, .35))
        if pc > 0:
            g = ease(c.at('pídelas', -0.5, .5)); cx, cy = lerp(330, 780, g), lerp(500, 500, g)
            click = 0.9 if (0.25 < c.at('Comenta', 0, 1.2) < 0.4 or 0.3 < c.at('pídelas', 0, 1.2) < 0.45) else 1.0
            put(st, cursor(), cx + (1 - eout(pc)) * 200, cy + (1 - eout(pc)) * 200, click)
    return st

VIS = dict(hook=s_hook, medina=s_medina, nakhla=s_nakhla, badr=s_badr, kab=s_kab, mustaliq=s_mustaliq, qurayza=s_qurayza, khaybar=s_khaybar, tabuk=s_tabuk,
           hadith=s_hadith, sword=s_sword, fiqh=s_fiqh, counter=s_counter, jesus=s_jesus, end=s_end)

# ------------------------------------------------------------------ fotograma
def caption(c):
    g = c.seg; t = c.t
    if t > g['dur'] + 0.5: return []
    cur = g['chunks'][0]
    for ch in g['chunks']:
        if t >= g['tt'][ch[0]] - 0.07: cur = ch
    return [(g['toks'][i][0].upper(), 0 if t < g['tt'][i] - 0.03 else (2 if g['toks'][i][1] else 1)) for i in cur]

def frame(T, gt):
    sc = T[-1]
    for s in T:
        if s['start'] <= gt < s['end']: sc = s
    c = C(sc, gt); st = VIS[sc['id']](c)
    span = max(0.5, c.cut1 - c.cut0); z = 1 + 0.035 * ease((gt - c.cut0) / span); blur = 0.0; shift = 0.0; hb = 1.0
    din = gt - c.cut0; dout = c.cut1 - gt; last = (c.k == c.n - 1)
    if c.k > 0 and din < 0.24: p = din / 0.24; blur = 11 * (1 - ease(p)); z *= 1 + 0.07 * (1 - eout(p))
    if not last and dout < 0.12: p = 1 - dout / 0.12; blur = max(blur, 9 * p * p); z *= 1 + 0.04 * p * p
    bt = [b for b in c.seg['beats'] if b <= c.t]
    if bt and c.t - bt[-1] < 0.2: p = (c.t - bt[-1]) / 0.2; blur = max(blur, 6 * (1 - ease(p))); z *= 1 + 0.045 * (1 - eout(p))
    if c.k == 0 and din < 0.26:
        p = din / 0.26
        if sc['i'] == 0: blur = 12 * (1 - ease(p)); z *= 1 + 0.08 * (1 - eout(p))
        else: shift = (1 - eout(p)) * W * 0.6; hb = 1 + (1 - p) * 40
    if last and dout < 0.16 and sc['i'] < len(T) - 1: p = 1 - dout / 0.16; shift = -ease(p) * W * 0.6; hb = 1 + p * 40
    st = cam(st, z, W / 2, SH * 0.47)
    if blur > 0.4: st = gblur(st, blur)
    if hb > 1.5:
        base = hblur(st, 90); st = hblur(st, hb); base.paste(st, (int(shift), 0)); st = base
    st = finish(st, gt)
    if last and sc['i'] == len(T) - 1 and dout < 0.5:
        st = Image.blend(st, Image.new('RGB', st.size, (16, 14, 14)), clamp(1 - dout / 0.5))
    fr = Image.new('RGB', (W, H)); fr.paste(st, (0, 0)); draw_panel(fr, gt, caption(c), c.seg['src'])
    return fr

# ------------------------------------------------------------------ audio
def make_audio(T, total, sr=48000):
    n = int((total + 0.6) * sr); voice = np.zeros(n, dtype=np.float32)
    for sc in T:
        for g in sc['segs']:
            a, _ = wav(f"{B}/audh/{g['key']}.wav"); i = int(g['t0'] * sr); voice[i:i + len(a)] += a[:max(0, n - i)]
    tt = np.arange(n, dtype=np.float32) / sr; rs = np.random.RandomState(5)
    # colchón: acordes menores que cambian cada 8 s, con notas dobladas y desafinadas (para que no suene a zumbido)
    pad = np.zeros(n, dtype=np.float32); chords = [[110.0, 130.81, 164.81, 220.0], [87.31, 110.0, 130.81, 174.61], [73.42, 110.0, 146.83, 174.61], [82.41, 123.47, 164.81, 207.65]]; cl = 8.0
    for ci in range(int(total / cl) + 2):
        ch = chords[ci % 4]; a0 = ci * cl - 1.0; a1 = a0 + cl + 2.0; i0 = max(0, int(a0 * sr)); i1 = min(n, int(a1 * sr))
        if i1 <= i0: continue
        x = tt[i0:i1] - a0; env = np.clip(np.minimum(x / 2.0, (a1 - a0 - x) / 2.0), 0, 1); env = env * env * (3 - 2 * env); sig = np.zeros(i1 - i0, dtype=np.float32)
        for j, f in enumerate(ch):
            for det in (0.9972, 1.0028): sig += np.sin(2 * np.pi * f * det * x + j) * (0.5 if j == 0 else 0.33)
            sig += 0.10 * np.sin(2 * np.pi * 2 * f * x + j * 1.7)
        sig += 0.45 * np.sin(2 * np.pi * ch[0] / 2 * x)
        pad[i0:i1] += sig * env
    pad *= (0.85 + 0.15 * np.sin(2 * np.pi * 0.11 * tt)); pad *= 0.017 / float(np.sqrt((pad ** 2).mean()))
    def band_noise(L, lo, hi):
        x = rs.normal(0, 1, L).astype(np.float32); X = np.fft.rfft(x); fr = np.fft.rfftfreq(L, 1 / sr); X[(fr < lo) | (fr > hi)] = 0
        y = np.fft.irfft(X, L).astype(np.float32); return y / (np.abs(y).max() + 1e-9)
    fx = np.zeros(n, dtype=np.float32)
    def add(sig, t0):
        i = int(t0 * sr)
        if i < 0: sig = sig[-i:]; i = 0
        fx[i:i + len(sig)] += sig[:max(0, n - i)]
    def whoosh(d, amp, lo=350, hi=3200):
        L = int(d * sr); e = np.sin(np.pi * np.arange(L) / L) ** 2.2; return band_noise(L, lo, hi) * e * amp
    def boom(amp=0.22):
        L = int(0.9 * sr); x = np.arange(L) / sr; f = 62 * np.exp(-x * 3.2) + 38; ph = 2 * np.pi * np.cumsum(f) / sr
        return (np.sin(ph) * np.exp(-x * 4.2) * amp).astype(np.float32)
    for sc in T:
        add(whoosh(0.5, 0.075), sc['start'] - 0.25); add(boom(), sc['start'] + 0.02)
        for g in sc['segs'][1:]: add(whoosh(0.32, 0.035, 500, 4200), g['cut'] - 0.16); add(boom(0.09), g['cut'])
        for g in sc['segs']:
            for b in g['beats']: add(whoosh(0.24, 0.018, 700, 5000), g['t0'] + b - 0.12)
    fade = np.clip(np.minimum(tt / 1.5, (total + 0.5 - tt) / 1.5), 0, 1)
    out = voice * 0.92 + (pad + fx) * fade
    if os.environ.get('AUDIO_STATS'):
        rms = lambda x: float(np.sqrt((x ** 2).mean())); sp = np.abs(voice) > 0.02
        print('voz rms(habla)', round(rms(voice[sp]), 4), 'colchón rms', round(rms(pad), 4), 'efectos pico', round(float(np.abs(fx).max()), 3), 'mezcla pico', round(float(np.abs(out).max()), 3))
    w = wave.open(f'{B}/out/mix.wav', 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes((np.clip(out, -1, 1) * 32767).astype(np.int16).tobytes()); w.close()

def render_part(args):
    k, n, total = args
    T, _ = build(); nf = int(total * FPS); a = nf * k // n; b = nf * (k + 1) // n
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', f'{B}/out/part{k}.mp4'], stdin=subprocess.PIPE)
    for fi in range(a, b): p.stdin.write(frame(T, fi / FPS).tobytes())
    p.stdin.close(); p.wait(); return k

if __name__ == '__main__':
    os.makedirs(B + '/out', exist_ok=True)
    T, total = build()
    print('duración', round(total, 1), 's =', round(total / 60, 2), 'min')
    if len(sys.argv) > 1 and sys.argv[1] == 'times':
        for s in T: print(s['i'], s['id'], round(s['start'], 1), [(round(g['t0'], 1), round(g['dur'], 1)) for g in s['segs']])
        sys.exit()
    if len(sys.argv) > 1 and sys.argv[1] == 'preview':
        import time
        for tv in map(float, sys.argv[2:]):
            t0 = time.time(); frame(T, tv).save(f'{B}/out/prev_{tv:07.2f}.png')
        print('MISS', MISS); sys.exit()
    if len(sys.argv) > 1 and sys.argv[1] == 'clip':
        a, b = float(sys.argv[2]), float(sys.argv[3])
        p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '23', '-pix_fmt', 'yuv420p', f'{B}/out/clip.mp4'], stdin=subprocess.PIPE)
        for fi in range(int(a * FPS), int(b * FPS)): p.stdin.write(frame(T, fi / FPS).tobytes())
        p.stdin.close(); p.wait(); sys.exit()
    make_audio(T, total)
    from multiprocessing import Pool
    n = 4
    with Pool(n) as pool: list(pool.imap_unordered(render_part, [(k, n, total) for k in range(n)]))
    open(f'{B}/out/list.txt', 'w').write(''.join(f"file 'part{k}.mp4'\n" for k in range(n)))
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', f'{B}/out/list.txt', '-i', f'{B}/out/mix.wav',
                    '-c:v', 'copy', '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-ar', '48000', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', f'{B}/out/defensa_papel.mp4'], check=True)
    print('ok')
