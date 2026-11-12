# -*- coding: utf-8 -*-
"""Motor «papel recortado»: piezas planas con contorno, grano de papel y sombra proyectada."""
import math, os, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

B = os.path.dirname(os.path.abspath(__file__))
W, H, SH = 1080, 1920, 1490          # lienzo y altura del escenario (el resto es el panel de subtítulos)
INK = (46, 36, 28)
WHITE = (245, 241, 232)
GOLD = (203, 164, 72)
RED = (182, 30, 42)
SS = 2
SKIN = [(226, 190, 156), (205, 160, 122), (171, 125, 90), (238, 206, 178)]

_F = {}
FONTS = dict(bebas='Bebas.ttf', anton='Anton.ttf', lorai='LoraI.ttf', lora='Lora.ttf')   # Bebas Neue, Anton y Lora (SIL OFL 1.1)
def F(n, s, wght=None):
    k = (n, int(s), wght)
    if k not in _F:
        if n == 'sans': f = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf', int(s))
        elif n == 'sansb': f = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf', int(s))
        else:
            f = ImageFont.truetype(f'{B}/fonts/{FONTS[n]}', int(s))
            if wght:
                try: f.set_variation_by_axes([wght])
                except Exception: pass
        _F[k] = f
    return _F[k]

def clamp(x, a=0.0, b=1.0): return a if x < a else b if x > b else x
def ease(p): p = clamp(p); return p * p * (3 - 2 * p)
def eout(p): p = clamp(p); return 1 - (1 - p) ** 3
def eback(p):
    p = clamp(p); c = 1.70158; return 1 + (c + 1) * (p - 1) ** 3 + c * (p - 1) ** 2
def lerp(a, b, p): return a + (b - a) * p
def mix(c1, c2, p): return tuple(int(round(a + (b - a) * p)) for a, b in zip(c1, c2))
def shade(c, k): return tuple(int(clamp(v * k, 0, 255)) for v in c)

_rs = np.random.RandomState(7)
_g = _rs.normal(0, 1, (720, 720)).astype(np.float32)
GR = np.asarray(Image.fromarray((_g * 42 + 128).clip(0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.7)), dtype=np.float32) / 128.0 - 1.0
def grain(im, k=0.09, seed=0):
    a = np.asarray(im).astype(np.float32); h, w = a.shape[:2]
    oy, ox = (seed * 37) % 200, (seed * 91) % 200
    g = np.tile(GR, ((h + 200) // 720 + 1, (w + 200) // 720 + 1))[oy:oy + h, ox:ox + w]
    a[..., :3] = np.clip(a[..., :3] * (1 + k * g[..., None]), 0, 255)
    return Image.fromarray(a.astype(np.uint8), im.mode)

class Sp:
    """sprite RGBA con ancla"""
    _n = 0
    def __init__(s, im, ax=None, ay=None, r0=0.0):
        s.im = im; s.ax = im.width / 2 if ax is None else ax; s.ay = im.height / 2 if ay is None else ay; s.r0 = r0
        Sp._n += 1; s.k = Sp._n

SPAD = 22
def shadowed(im, off=(6, 8), blur=6, op=0.36):
    w, h = im.size; p = SPAD
    sh = Image.new('L', (w + 2 * p, h + 2 * p), 0); sh.paste(im.getchannel('A'), (p + off[0], p + off[1]))
    sh = sh.filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(v * op))
    base = Image.new('RGBA', (w + 2 * p, h + 2 * p), (20, 14, 10, 0)); base.putalpha(sh)
    base.alpha_composite(im, (p, p)); return base

class Cut:
    """lienzo de recorte: se dibuja a SSx y se reduce (bordes suaves)"""
    def __init__(s, w, h, ox=0, oy=0):
        s.w, s.h, s.ox, s.oy = int(w), int(h), ox, oy
        s.im = Image.new('RGBA', (s.w * SS, s.h * SS), (0, 0, 0, 0)); s.d = ImageDraw.Draw(s.im)
    def _p(s, pts): return [((x + s.ox) * SS, (y + s.oy) * SS) for x, y in pts]
    def _b(s, b): return [(b[0] + s.ox) * SS, (b[1] + s.oy) * SS, (b[2] + s.ox) * SS, (b[3] + s.oy) * SS]
    def poly(s, pts, fill, ow=5, oc=INK):
        P = s._p(pts); s.d.polygon(P, fill=fill)
        if ow: s.d.line(P + P[:2], fill=oc, width=int(ow * SS), joint='curve')
    def rr(s, box, r, fill, ow=5, oc=INK, corners=None):
        r = max(0, min(r, (box[2] - box[0]) / 2 - 1, (box[3] - box[1]) / 2 - 1))
        s.d.rounded_rectangle(s._b(box), r * SS, fill=fill, outline=oc if ow else None, width=int(ow * SS) if ow else 0, corners=corners)
    def ell(s, box, fill, ow=5, oc=INK):
        s.d.ellipse(s._b(box), fill=fill, outline=oc if ow else None, width=int(ow * SS) if ow else 0)
    def chord(s, box, a0, a1, fill, ow=5, oc=INK):
        s.d.chord(s._b(box), a0, a1, fill=fill, outline=oc if ow else None, width=int(ow * SS) if ow else 0)
    def line(s, pts, col=INK, w=4):
        s.d.line(s._p(pts), fill=col, width=int(w * SS), joint='curve')
    def arc(s, box, a0, a1, col=INK, w=4): s.d.arc(s._b(box), a0, a1, fill=col, width=int(w * SS))
    def text(s, xy, t, font, size, fill, anchor='mm', wght=None, **kw):
        s.d.text(((xy[0] + s.ox) * SS, (xy[1] + s.oy) * SS), t, font=F(font, size * SS, wght), fill=fill, anchor=anchor, **kw)
    def out(s, g=0.09, seed=0):
        im = s.im.resize((s.w, s.h), Image.LANCZOS); return grain(im, g, seed) if g else im

def stack(w, h, layers, ax, ay):
    """capas (im, x, y[, sombra]) → sprite; cada capa proyecta su sombra sobre las de debajo"""
    p = SPAD + 2; cv = Image.new('RGBA', (int(w) + 2 * p, int(h) + 2 * p), (0, 0, 0, 0))
    for L in layers:
        im, x, y = L[:3]; sh = L[3] if len(L) > 3 else True
        if sh:
            kw = sh if isinstance(sh, dict) else {}
            cv.alpha_composite(shadowed(im, **kw), (int(x) + p - SPAD, int(y) + p - SPAD))
        else: cv.alpha_composite(im, (int(x) + p, int(y) + p))
    return Sp(cv, ax + p, ay + p)
def one(im, ax=None, ay=None, **kw):
    """una pieza con su sombra"""
    s = shadowed(im, **kw); return Sp(s, (im.width / 2 if ax is None else ax) + SPAD, (im.height / 2 if ay is None else ay) + SPAD)

_SC = {}; _RC = {}
def _scaled(sp, s):
    if abs(s - 1) < 1e-3: return sp.im
    k = (sp.k, s)
    if k not in _SC:
        if len(_SC) > 900: _SC.clear()
        _SC[k] = sp.im.resize((max(1, round(sp.im.width * s)), max(1, round(sp.im.height * s))), Image.LANCZOS if s < 1 else Image.BICUBIC)
    return _SC[k]
def put(dst, sp, x, y, s=1.0, rot=0.0, a=1.0, cache=True):
    """pega el sprite con su ancla en (x, y). rot en grados (antihorario), s escala, a opacidad"""
    if a <= 0.004 or s <= 0.02: return
    s = 1.0 if abs(s - 1) < 1e-3 else round(s, 2)
    im = _scaled(sp, s) if cache else (sp.im if s == 1.0 else sp.im.resize((max(1, round(sp.im.width * s)), max(1, round(sp.im.height * s))), Image.BILINEAR))
    ax, ay = sp.ax * s, sp.ay * s
    rq = round((rot + sp.r0) * 2) / 2
    if abs(rq) > 0.01:
        k = (sp.k, s, rq)
        if not cache or k not in _RC:
            R = int(math.ceil(max(math.hypot(ax, ay), math.hypot(im.width - ax, ay), math.hypot(ax, im.height - ay), math.hypot(im.width - ax, im.height - ay)))) + 2
            cv = Image.new('RGBA', (2 * R, 2 * R), (0, 0, 0, 0)); cv.alpha_composite(im, (int(round(R - ax)), int(round(R - ay))))
            v = (cv.rotate(rq, resample=Image.BICUBIC), R)
            if cache:
                if len(_RC) > 900: _RC.clear()
                _RC[k] = v
        else: v = _RC[k]
        im, R = v; px, py = int(round(x - R)), int(round(y - R))
    else: px, py = int(round(x - ax)), int(round(y - ay))
    if a < 0.996:
        dst.paste(im, (px, py), im.getchannel('A').point(lambda v: int(v * a)))
    else: dst.paste(im, (px, py), im)

# ------------------------------------------------------------------ figuras
_FIG = {}
def figure(coat=(122, 100, 70), tunic=WHITE, skin=0, head='turban', headcol=WHITE, trim=GOLD, beard=None, hair=None, shoes=(60, 42, 32), seed=0):
    key = (coat, tunic, skin, head, headcol, trim, beard, hair, shoes)
    if key in _FIG: return _FIG[key]
    sk = SKIN[skin] if isinstance(skin, int) else skin
    BW, BH = 440, 480; ox, oy = BW / 2, BH - 20
    L = []
    c = Cut(BW, BH, ox, oy); c.chord((-112, -34, -20, 28), 180, 360, shoes, 4); c.chord((20, -34, 112, 28), 180, 360, shoes, 4); L.append((c.out(seed=seed), 0, 0, False))
    c = Cut(BW, BH, ox, oy); c.rr((-112, -436, 112, -10), 12, tunic)
    if trim:
        c.line([(-16, -430), (-16, -14)], trim, 5); c.line([(16, -430), (16, -14)], trim, 5)
    L.append((c.out(seed=seed + 1), 0, 0, dict(off=(2, 4), blur=4, op=.25)))
    if coat:
        for sg in (-1, 1):
            c = Cut(BW, BH, ox, oy); x0, x1 = sorted((sg * 204, sg * 56))
            c.rr((x0, -442, x1, -48), 26, coat, corners=(sg < 0, sg > 0, False, False))
            if trim: c.line([(sg * 66, -434), (sg * 66, -54)], trim, 6)
            c.line([(sg * 128, -300), (sg * 128, -56)], shade(coat, 0.86), 3)
            L.append((c.out(seed=seed + 2 + sg), 0, 0, dict(off=(sg * 3 + 2, 6), blur=5, op=.34)))
    body = stack(BW, BH, L, ox, oy)
    # brazo (cuelga hacia abajo desde el hombro, pivote en el origen)
    AW, AH = 120, 340; aox, aoy = AW / 2, 26
    c = Cut(AW, AH, aox, aoy); c.rr((-25, 222, 25, 290), 22, sk, 4)
    c.rr((-44, -16, 44, 238), 24, shade(coat or tunic, 0.94))
    if trim: c.d.rectangle(c._b((-41, 204, 41, 220)), fill=trim)
    c.line([(-44, 204), (44, 204)], INK, 3); c.line([(-44, 220), (44, 220)], INK, 3)
    arm = one(c.out(seed=seed + 5), aox, aoy, off=(2, 4), blur=5, op=.3)
    # cabeza (origen = base del cuello)
    HW, HH = 260, 330; hox, hoy = HW / 2, HH - 40
    hl = []
    def piece(fn, sh=True):
        c = Cut(HW, HH, hox, hoy); fn(c); hl.append((c.out(seed=seed + 7 + len(hl)), 0, 0, dict(off=(2, 4), blur=4, op=.28) if sh else False))
    if head == 'keffiyeh': piece(lambda c: c.rr((-98, -196, 98, 30), 44, headcol))
    if hair and head in ('long',): piece(lambda c: c.rr((-92, -180, 92, 36), 46, hair))
    piece(lambda c: c.rr((-76, -172, 76, 0), 60, sk))
    if beard: piece(lambda c: c.rr((-64, -66, 64, 8), 34, beard, 4), False)
    if head == 'turban':
        def tb(c):
            c.chord((-96, -252, 96, -84), 180, 360, headcol)
            for x0, x1, yt in ((-58, -34, -236), (-10, 14, -244), (38, 56, -226)): c.line([(x0, -158), ((x0 + x1) / 2 - 3, (-158 + yt) / 2), (x1, yt)], shade(headcol, 0.72), 3)
            c.rr((-98, -152, 98, -106), 20, headcol)
            c.line([(-60, -128), (60, -128)], shade(headcol, 0.78), 3)
        piece(tb)
    elif head == 'kufi': piece(lambda c: c.rr((-74, -200, 74, -146), 22, headcol))
    elif head == 'keffiyeh':
        piece(lambda c: (c.rr((-88, -196, 88, -128), 34, headcol), c.rr((-90, -152, 90, -134), 6, (34, 30, 28), 3)))
    elif head == 'helmet':
        def hm(c):
            c.poly([(-8, -236), (0, -262), (8, -236)], (150, 150, 156), 3)
            c.chord((-86, -240, 86, -76), 180, 360, (176, 178, 184)); c.rr((-90, -164, 90, -138), 8, (150, 152, 158))
            c.rr((-9, -150, 9, -92), 6, (150, 152, 158), 4)
        piece(hm)
    elif head in ('hair', 'long'):
        piece(lambda c: c.rr((-80, -182, 80, -118), 40, hair or (70, 50, 36), corners=(True, True, False, False)))
    hd = stack(HW, HH, hl, hox, hoy)
    f = dict(body=body, arm=arm, head=hd); _FIG[key] = f; return f

def draw_fig(dst, f, x, y, s=1.0, aL=6, aR=6, tilt=0.0, holdL=None, holdR=None, a=1.0):
    """figura con los pies en (x, y). aL/aR = ángulo de cada brazo (0 colgando, 90 horizontal hacia fuera, 150 en alto)."""
    put(dst, f['body'], x, y, s, 0, a)
    for sg, ang, hold in ((-1, aL, holdL), (1, aR, holdR)):
        sx, sy = x + sg * 176 * s, y - 398 * s; th = math.radians(sg * ang)
        if hold is not None:
            put(dst, hold, sx + math.sin(th) * 258 * s, sy + math.cos(th) * 258 * s, s, sg * ang, a)
        put(dst, f['arm'], sx, sy, s, sg * ang, a)
    put(dst, f['head'], x, y - 420 * s, s, tilt, a)

_P = {}
def memo(fn):
    def w(*a, **k):
        key = (fn.__name__, a, tuple(sorted(k.items())))
        if key not in _P: _P[key] = fn(*a, **k)
        return _P[key]
    return w

@memo
def pawn(col=(48, 38, 32), h=60):
    c = Cut(40, 70, 20, 66); c.poly([(-13, 0), (-9, -34), (9, -34), (13, 0)], col, 0); c.ell((-10, -56, 10, -34), col, 0)
    im = c.out(0); k = h / 60
    if k != 1: im = im.resize((round(40 * k), round(70 * k)), Image.LANCZOS)
    return one(im, 20 * k, 66 * k, off=(2, 3), blur=3, op=.3)

# ------------------------------------------------------------------ objetos
@memo
def sword(L=250):
    c = Cut(80, L + 70, 40, 34)
    c.rr((-7, -28, 7, 6), 5, (110, 78, 50), 3); c.poly([(-10, 8), (-10, L - 24), (0, L + 20), (10, L - 24), (10, 8)], (208, 211, 216), 4)
    c.line([(0, 14), (0, L - 20)], (160, 164, 170), 2); c.rr((-30, 0, 30, 14), 5, (170, 140, 70), 3)
    return one(c.out(0.05), 40, 34 + 4, off=(2, 4), blur=4, op=.3)
@memo
def spear(L=520):
    c = Cut(60, L + 40, 30, 20 + L * 0.42)
    y0 = -L * 0.42; y1 = L * 0.58
    c.rr((-6, y0, 6, y1), 4, (128, 92, 58), 3); c.poly([(-14, y0 + 6), (0, y0 - 16 - 30), (14, y0 + 6)], (200, 204, 210), 4)
    return Sp(shadowed(c.out(0.05), off=(2, 4), blur=4, op=.3), 30 + SPAD, 20 + L * 0.42 + SPAD)
@memo
def flag(col=(214, 176, 58), L=380):
    c = Cut(180, L + 40, 20, 20 + L * 0.3)
    y0 = -L * 0.3; y1 = L * 0.7
    c.rr((-5, y0, 5, y1), 4, (120, 88, 56), 3); c.poly([(5, y0 + 4), (140, y0 + 40), (5, y0 + 84)], col, 4)
    return Sp(shadowed(c.out(0.06), off=(2, 4), blur=4, op=.3), 20 + SPAD, 20 + L * 0.3 + SPAD)
@memo
def scroll(col=(232, 220, 190)):
    c = Cut(120, 90, 60, 45); c.rr((-46, -26, 46, 26), 6, col, 4); c.ell((-58, -30, -34, 30), shade(col, 0.9), 4); c.ell((34, -30, 58, 30), shade(col, 0.9), 4)
    for k in range(3): c.line([(-26, -12 + k * 12), (26, -12 + k * 12)], (150, 130, 100), 2)
    return one(c.out(0.06), 60, 45, off=(2, 4), blur=4, op=.3)
@memo
def camel(col=(196, 150, 100), load=False, seed=0):
    c0 = Cut(540, 450); dk = shade(col, 0.8)
    for x in (128, 322): c0.rr((x, 262, x + 24, 430), 8, dk, 4)
    c0.poly([(70, 196), (40, 232), (46, 300), (58, 300), (56, 240), (82, 214)], dk, 4)
    c0.ell((150, 70, 300, 250), col, 4)
    c0.poly([(326, 200), (376, 92), (418, 60), (446, 92), (404, 132), (384, 250), (330, 250)], col, 4)
    c0.ell((56, 140, 384, 300), col, 4)
    for x in (96, 352): c0.rr((x, 262, x + 26, 436), 8, col, 4)
    for x in (92, 124, 318, 348): c0.rr((x, 424, x + 34, 440), 6, shade(col, 0.6), 3)
    c0.rr((398, 42, 500, 98), 24, col, 4); c0.ell((404, 28, 424, 56), col, 4); c0.ell((466, 58, 474, 66), INK, 0)
    c0.line([(486, 84), (498, 84)], INK, 3)
    if load:
        c0.rr((150, 96, 232, 200), 16, (214, 196, 160), 4); c0.rr((226, 100, 306, 204), 16, (170, 120, 80), 4)
        c0.line([(150, 150), (306, 150)], (110, 80, 50), 4); c0.rr((186, 60, 268, 112), 14, (196, 150, 90), 4)
    return one(c0.out(0.08, seed), 270, 440)
@memo
def fortress(w=560, h=330, col=(182, 146, 108)):
    c = Cut(w + 20, h + 60, 10, 50); dk = shade(col, 0.82)
    for tx in (0, w - 110):
        c.rr((tx, -30, tx + 110, h), 4, dk)
        for k in range(3): c.rr((tx + 4 + k * 36, -50, tx + 30 + k * 36, -22), 2, dk, 4)
    c.rr((70, 40, w - 70, h), 4, col)
    n = int((w - 140) / 44)
    for k in range(n): c.rr((78 + k * 44, 16, 104 + k * 44, 46), 2, col, 4)
    for r in range(1, 5):
        c.line([(74, 40 + r * (h - 40) / 5), (w - 74, 40 + r * (h - 40) / 5)], shade(col, 0.78), 2)
    c.rr((w / 2 - 50, h - 150, w / 2 + 50, h + 30), 50, (70, 48, 34), 5, corners=(True, True, False, False))
    c.d.rectangle(c._b((0, h, w, h + 10)), fill=(0, 0, 0, 0))
    return one(c.out(0.08), (w + 20) / 2, h + 50)
@memo
def tent(col=(150, 100, 78), s=1.0):
    c = Cut(300, 220, 150, 210); c.poly([(-140, 0), (0, -190), (140, 0)], col); c.poly([(-34, 0), (0, -110), (34, 0)], shade(col, 0.55), 4)
    c.line([(0, -190), (0, -214)], INK, 5)
    return one(c.out(0.08), 150, 210)
@memo
def palm(seed=0):
    c = Cut(360, 520, 180, 510); r = random.Random(seed)
    c.poly([(-18, 0), (-10, -330), (14, -330), (20, 0)], (136, 100, 66))
    for k in range(6): c.line([(-12, -50 - k * 50), (16, -62 - k * 50)], (100, 72, 46), 3)
    for a in (-150, -115, -80, -40, -10, 20, 200):
        pts = []; L = 150 + r.random() * 20
        for t in (0, .3, .6, 1): pts.append((math.cos(math.radians(a)) * L * t, -330 + math.sin(math.radians(a)) * L * t * 0.7 + 60 * t * t))
        up = [(x - 14 * (1 - t), y - 22 * (1 - t) - 4) for (x, y), t in zip(pts, (0, .3, .6, 1))]
        c.poly(pts + up[::-1], (96, 126, 78), 4)
    return one(c.out(0.08, seed), 180, 510)
@memo
def house(col=(206, 178, 138), w=200, h=170):
    c = Cut(w + 10, h + 30, 5, 25); c.rr((0, 0, w, h), 4, col); c.rr((-4, -14, w + 4, 8), 4, shade(col, 0.85))
    c.rr((w * .38, h - 84, w * .62, h + 4), 22, (84, 58, 40), 4, corners=(True, True, False, False)); c.rr((w * .12, 40, w * .28, 76), 3, (84, 58, 40), 4); c.rr((w * .72, 40, w * .88, 76), 3, (84, 58, 40), 4)
    return one(c.out(0.08), (w + 10) / 2, h + 25)
@memo
def kaaba(w=300, h=300):
    c = Cut(w + 10, h + 10, 5, 5); c.rr((0, 0, w, h), 4, (34, 32, 34)); c.d.rectangle(c._b((3, h * .26, w - 3, h * .36)), fill=GOLD)
    c.line([(0, h * .26), (w, h * .26)], INK, 3); c.line([(0, h * .36), (w, h * .36)], INK, 3)
    c.rr((w * .62, h * .5, w * .84, h + 4), 4, GOLD, 4)
    for k in range(7): c.line([(20 + k * 40, h * .42), (20 + k * 40, h - 8)], (52, 50, 54), 2)
    return one(c.out(0.06), (w + 10) / 2, h + 5)
@memo
def shield(d=420):
    c = Cut(d + 20, d + 20, d / 2 + 10, d / 2 + 10); r = d / 2
    c.ell((-r, -r, r, r), (150, 104, 66), 6); c.ell((-r + 26, -r + 26, r - 26, r - 26), (196, 150, 92), 4)
    for a in range(0, 360, 45): c.line([(math.cos(math.radians(a)) * 60, math.sin(math.radians(a)) * 60), (math.cos(math.radians(a)) * (r - 26), math.sin(math.radians(a)) * (r - 26))], (150, 104, 66), 4)
    c.ell((-62, -62, 62, 62), (176, 178, 184), 5); c.ell((-24, -24, 24, 24), (140, 142, 150), 4)
    for a in range(0, 360, 30): c.ell((math.cos(math.radians(a)) * (r - 13) - 6, math.sin(math.radians(a)) * (r - 13) - 6, math.cos(math.radians(a)) * (r - 13) + 6, math.sin(math.radians(a)) * (r - 13) + 6), (214, 190, 120), 2)
    return one(c.out(0.08), d / 2 + 10, d / 2 + 10)
@memo
def book(title, col=(92, 60, 44), w=190, h=270, fs=40):
    c = Cut(w + 10, h + 10, 5, 5); c.rr((0, 0, w, h), 8, col); c.rr((0, 0, 26, h), 6, shade(col, 0.75)); c.rr((40, 30, w - 16, 30 + 110), 4, (232, 220, 190), 3)
    ls = title.split('|'); y = 30 + 55 - (len(ls) - 1) * fs * 0.48
    for l in ls: c.text((40 + (w - 56) / 2, y), l, 'bebas', fs, INK); y += fs * 0.96
    c.line([(40, h - 40), (w - 16, h - 40)], GOLD, 4); c.line([(40, h - 56), (w - 16, h - 56)], GOLD, 4)
    return one(c.out(0.08), (w + 10) / 2, h + 5)
@memo
def letter():
    c = Cut(470, 300, 5, 5); c.rr((0, 0, 460, 290), 6, (236, 224, 192))
    c.text((230, 96), '«Id a Najla y acechad', 'lorai', 40, INK); c.text((230, 150), 'allí a Quraysh»', 'lorai', 40, INK)
    c.ell((196, 196, 264, 264), (170, 34, 40), 4); c.ell((214, 214, 246, 246), (140, 24, 30), 2)
    return one(c.out(0.08), 235, 150)
@memo
def well(w=420):
    c = Cut(w + 10, 150, 5, 5); c.ell((0, 0, w, 130), (120, 160, 178), 5); c.arc((40, 30, w - 60, 100), 190, 260, (170, 200, 214), 4); c.arc((120, 50, w - 30, 116), 20, 80, (170, 200, 214), 4)
    return one(c.out(0.06), (w + 10) / 2, 75, off=(0, 3), blur=4, op=.25)
@memo
def trench(w=760):
    c = Cut(w + 10, 100, 5, 5); c.poly([(30, 0), (w - 30, 0), (w, 80), (0, 80)], (58, 42, 32), 5)
    return one(c.out(0.1), (w + 10) / 2, 50, off=(0, 0), blur=3, op=.2)

_rnd = random.Random(3)
@memo
def tag(text, size=56, bg=(24, 22, 20), fg=(244, 240, 230), font='bebas', padx=24, pady=10, seed=1, border=None):
    f = F(font, size); tw = f.getlength(text); w, h = int(tw + 2 * padx), int(size * 0.92 + 2 * pady)
    r = random.Random(seed + len(text)); j = lambda: r.uniform(-3, 3)
    c = Cut(w + 12, h + 12, 6, 6)
    c.poly([(j(), j()), (w * .5, j() * .6), (w + j(), j()), (w + j(), h + j()), (w * .5, h + j() * .6), (j(), h + j())], bg, 4 if border else 0, border or INK)
    c.text((w / 2, h / 2 + size * 0.045), text, font, size, fg)
    return one(c.out(0.07, seed), (w + 12) / 2, (h + 12) / 2, off=(4, 6), blur=5, op=.4)
@memo
def bigword(text, size=220, col=RED, font='anton'):
    f = F(font, size); tw = int(f.getlength(text)); w, h = tw + 60, int(size * 1.25)
    c = Cut(w, h, 0, 0); c.text((w / 2 + 5, h / 2 + 7), text, font, size, (60, 12, 16)); c.text((w / 2, h / 2), text, font, size, col)
    return one(c.out(0.12, 3), w / 2, h / 2, off=(4, 7), blur=6, op=.35)
@memo
def arrow_curve(col=RED, flip=False):
    c = Cut(200, 240, 0, 0); c.arc((40, 30, 260, 250), 160, 262, col, 9)
    c.poly([(150, 6), (196, 34), (146, 58)], col, 0)
    im = c.out(0.05)
    if flip: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    return one(im, 100, 120, off=(3, 4), blur=4, op=.3)
@memo
def xmark(size=150, col=RED):
    c = Cut(size, size, 0, 0); m = size * .16
    c.line([(m, m), (size - m, size - m)], col, size * .13); c.line([(size - m, m), (m, size - m)], col, size * .13)
    return one(c.out(0.08), off=(3, 4), blur=4, op=.3)
@memo
def check(size=120, col=(58, 128, 76)):
    c = Cut(size, size, 0, 0); c.line([(size * .14, size * .54), (size * .4, size * .8), (size * .88, size * .2)], col, size * .14)
    return one(c.out(0.08), off=(3, 4), blur=4, op=.3)
@memo
def qmark(size=260, col=RED): return bigword('?', size, col)
@memo
def pill(text, bg=(244, 240, 230), fg=(26, 24, 22), size=44, icon=None):
    f = F('bebas', size); tw = f.getlength(text); w, h = int(tw + 80), int(size * 1.7)
    c = Cut(w + 10, h + 10, 5, 5); c.rr((0, 0, w, h), h / 2, bg, 5); c.text((w / 2, h / 2 + size * .05), text, 'bebas', size, fg)
    return one(c.out(0.05), (w + 10) / 2, (h + 10) / 2, off=(4, 6), blur=5, op=.4)
@memo
def cursor():
    c = Cut(70, 90, 4, 4); c.poly([(0, 0), (0, 62), (16, 48), (28, 76), (40, 70), (28, 44), (50, 44)], (250, 250, 250), 5)
    return one(c.out(0), 4, 4, off=(3, 5), blur=3, op=.4)
@memo
def numcard(n, label, col=RED):
    c = Cut(700, 250, 0, 0); c.text((120, 125), n, 'anton', 190, col);
    ls = label.split('|'); y = 125 - (len(ls) - 1) * 26
    for l in ls: c.text((250, y), l, 'bebas', 56, INK, anchor='lm'); y += 54
    return one(c.out(0.08), 330, 125, off=(3, 5), blur=4, op=.25)

# tarjeta de cita (papel rasgado, comillas rojas, cursiva, marcador amarillo)
_QC = {}
def qcard(tokens, shown, w=930, fs=50, lh=None, ref=None):
    """tokens: [(palabra, marcada)]. shown = nº de palabras ya visibles. Devuelve sprite (ancla arriba-centro)."""
    key = (tuple(tokens), w, fs, ref); lh = lh or int(fs * 1.34)
    if key not in _QC:
        f = F('lorai', fs, 500); x0, x1 = 150, w - 56; sp = f.getlength(' ')
        lines = [[]]; x = x0
        for i, (t, m) in enumerate(tokens):
            tw = f.getlength(t)
            if x + tw > x1 and lines[-1]: lines.append([]); x = x0
            lines[-1].append((i, t, m, x, tw)); x += tw + sp
        h = 64 + len(lines) * lh + (70 if ref else 44)
        r = random.Random(len(tokens) * 7 + w); j = lambda k=5: r.uniform(-k, k)
        c = Cut(w + 16, h + 16, 8, 8); top = [(w * k / 9 + j(3), j()) for k in range(10)]; bot = [(w * k / 9 + j(3), h + j()) for k in range(9, -1, -1)]
        c.poly(top + bot, (229, 214, 183), 0); im = c.out(0.11, 5)
        a = np.asarray(im).astype(np.float32); yy = np.linspace(-1, 1, a.shape[0])[:, None]; xx = np.linspace(-1, 1, a.shape[1])[None, :]
        a[..., :3] *= (1 - 0.10 * np.clip(np.maximum(np.abs(yy) ** 6, np.abs(xx) ** 8), 0, 1))[..., None]
        base = Image.fromarray(a.clip(0, 255).astype(np.uint8), 'RGBA'); d = ImageDraw.Draw(base)
        d.text((8 + 34, 8 + 30), '«', font=F('lora', 150, 700), fill=(176, 30, 42))
        d.line([(8 + 64, 8 + h - (52 if ref else 26)), (8 + w - 64, 8 + h - (52 if ref else 26))], fill=(120, 104, 84), width=2)
        if ref: d.text((8 + 64, 8 + h - 28), ref, font=F('sans', 22), fill=(110, 96, 78), anchor='lm')
        _QC[key] = dict(base=shadowed(base, off=(6, 9), blur=8, op=.42), lines=lines, h=h, f=f, cache={})
    q = _QC[key]; shown = min(shown, len(tokens))
    if shown not in q['cache']:
        if len(q['cache']) > 6: q['cache'].clear()
        im = q['base'].copy(); d = ImageDraw.Draw(im); ox = oy = 8 + SPAD
        for li, ln in enumerate(q['lines']):
            y = oy + 58 + li * lh
            # marcador amarillo por tramos contiguos
            for (i, t, m, x, tw) in ln:
                if m and i < shown: d.rounded_rectangle((ox + x - 7, y - fs * .44, ox + x + tw + 7, y + fs * .5), 6, fill=(243, 205, 84))
            for (i, t, m, x, tw) in ln:
                if i < shown: d.text((ox + x, y), t, font=q['f'], fill=(46, 36, 28), anchor='lm')
        q['cache'][shown] = Sp(im, im.width / 2, SPAD + 8)
    return q['cache'][shown], q['h']

# hoja (recorte de página) con borde blanco y cinta
_SHF = {}
def sheet_frame(bw, bh, bd=16):
    k = (bw, bh, bd)
    if k not in _SHF:
        c = Cut(bw + 2 * bd, bh + 2 * bd, 0, 0); c.rr((0, 0, bw + 2 * bd, bh + 2 * bd), 3, (248, 246, 240), 3, (120, 110, 100))
        _SHF[k] = shadowed(c.out(0.03), off=(8, 11), blur=9, op=.42)
    return _SHF[k]
@memo
def tape(w=120, rot=0):
    c = Cut(w + 6, 46, 3, 3); c.poly([(0, 4), (w, 0), (w - 4, 38), (4, 40)], (232, 218, 168, 215), 0)
    return one(c.out(0.1), off=(1, 2), blur=2, op=.25)
def sheet(content, bd=16):
    """content RGB → sprite de hoja con marco blanco"""
    bw, bh = content.size; fr = sheet_frame(bw, bh, bd).copy(); fr.paste(content, (SPAD + bd, SPAD + bd))
    ImageDraw.Draw(fr).rectangle((SPAD + bd, SPAD + bd, SPAD + bd + bw - 1, SPAD + bd + bh - 1), outline=(150, 140, 126), width=2)
    return Sp(fr, fr.width / 2, fr.height / 2)

# tablero con patas (calendario, mapa, letreros)
@memo
def board(w=560, h=440, legs=260, col=(120, 84, 56), inner=(244, 240, 230)):
    c = Cut(w + 20, h + legs + 20, 10, 10)
    for x in (w * .16, w * .84): c.rr((x - 13, h - 20, x + 13, h + legs), 4, shade(col, 0.85))
    c.rr((0, 0, w, h), 10, col, 5); c.rr((18, 18, w - 18, h - 18), 4, inner, 4)
    return one(c.out(0.08), (w + 20) / 2, h + legs + 10)
@memo
def page(header, text, w=480, h=360, hc=RED, fs=150, sub=None):
    c = Cut(w + 10, h + 10, 5, 5); c.rr((0, 0, w, h), 4, (248, 246, 240), 4); c.d.rectangle(c._b((3, 3, w - 3, 78)), fill=hc); c.line([(0, 80), (w, 80)], INK, 4)
    for x in (w * .2, w * .5, w * .8): c.rr((x - 9, -4, x + 9, 30), 6, (214, 190, 120), 3)
    c.text((w / 2, 46), header, 'bebas', 44, (250, 246, 238))
    c.text((w / 2, 80 + (h - 80) / 2 + (0 if not sub else -26)), text, 'bebas', fs, INK)
    if sub: c.text((w / 2, h - 52), sub, 'bebas', 50, (110, 96, 84))
    return one(c.out(0.05), (w + 10) / 2, (h + 10) / 2, off=(3, 5), blur=4, op=.3)
@memo
def sign(text, w=560, h=120, col=(244, 240, 230), fg=INK, num=None, nc=RED, fs=58):
    c = Cut(w + 10, h + 10, 5, 5); c.rr((0, 0, w, h), 10, col, 5)
    x = 30
    if num:
        c.ell((18, h / 2 - 40, 98, h / 2 + 40), nc, 4); c.text((58, h / 2 + 3), num, 'anton', 50, (250, 246, 238)); x = 122
    c.text((x, h / 2 + 3), text, 'bebas', fs, fg, anchor='lm')
    return one(c.out(0.06), (w + 10) / 2, (h + 10) / 2)
@memo
def scale_parts():
    c = Cut(140, 620, 70, 610); c.rr((-60, -26, 60, 0), 8, (150, 110, 70)); c.rr((-36, -48, 36, -22), 6, (170, 126, 80)); c.rr((-9, -560, 9, -40), 4, (196, 164, 96)); c.ell((-20, -590, 20, -550), (214, 180, 104), 4)
    post = one(c.out(0.06), 70, 610)
    c = Cut(760, 60, 380, 30); c.rr((-360, -8, 360, 8), 6, (196, 164, 96)); c.ell((-16, -16, 16, 16), (150, 110, 70), 4)
    beam = one(c.out(0.06), 380, 30, off=(2, 4), blur=4, op=.3)
    c = Cut(300, 330, 150, 10); c.line([(0, 0), (-120, 250)], (120, 100, 70), 3); c.line([(0, 0), (120, 250)], (120, 100, 70), 3); c.chord((-130, 200, 130, 300), 0, 180, (206, 174, 104), 4)
    pan = one(c.out(0.06), 150, 10, off=(2, 4), blur=4, op=.3)
    return post, beam, pan

# mapa del Hiyaz (papel clavado en tablero)
MAPPT = dict(Meca=(300, 560), Medina=(262, 330), Najla=(356, 540), Badr=(196, 400), Jaybar=(300, 226), Tabuk=(170, 96), Taif=(380, 590))
@memo
def hijaz_map(show=('Meca', 'Medina', 'Badr', 'Jaybar', 'Tabuk')):
    w, h = 560, 680; c = Cut(w + 10, h + 10, 5, 5); c.rr((0, 0, w, h), 4, (236, 222, 186), 4)
    sea = [(3, 3), (130, 3)] + [(130 - k * 9 + 12 * math.sin(k * 1.3), k * 45) for k in range(1, 15)] + [(3, h - 3)]
    c.poly(sea, (150, 186, 198), 3)
    c.text((52, 300), 'MAR', 'bebas', 30, (60, 96, 110)); c.text((48, 332), 'ROJO', 'bebas', 30, (60, 96, 110))
    for n in show:
        x, y = MAPPT[n]; c.ell((x - 10, y - 10, x + 10, y + 10), INK, 0)
        lab = {'Meca': 'LA MECA'}.get(n, n.upper())
        if n == 'Meca': c.text((x - 18, y + 26), lab, 'bebas', 36, INK, anchor='rm')
        elif n == 'Najla': c.text((x + 16, y - 20), lab, 'bebas', 34, INK, anchor='lm')
        else: c.text((x + 18, y + 2), lab, 'bebas', 36, INK, anchor='lm')
    for px in (14, w - 14): c.ell((px - 8, 6, px + 8, 22), RED, 3)
    return one(c.out(0.07), 5, 5, off=(4, 6), blur=5, op=.35)

# ------------------------------------------------------------------ fondos
_BG = {}
def _vgrad(h, stops):
    a = np.zeros((h, 3), np.float32); ys = np.arange(h)
    for (y0, c0), (y1, c1) in zip(stops, stops[1:]):
        m = (ys >= y0) & (ys <= y1); t = ((ys[m] - y0) / max(1, y1 - y0))[:, None]; a[m] = np.array(c0) * (1 - t) + np.array(c1) * t
    return a
def bg(kind):
    if kind in _BG: return _BG[kind]
    P = dict(
        day=dict(sky=[(233, 221, 192), (245, 236, 210)], d1=(224, 205, 166), d2=(213, 190, 148), fl=[(205, 178, 134), (172, 142, 100)], sun=(252, 246, 216)),
        dusk=dict(sky=[(232, 158, 118), (246, 208, 168)], d1=(218, 164, 122), d2=(204, 148, 106), fl=[(190, 136, 98), (146, 100, 74)], sun=(252, 226, 180)),
        dawn=dict(sky=[(214, 196, 204), (246, 222, 188)], d1=(222, 190, 156), d2=(208, 172, 134), fl=[(196, 160, 122), (160, 124, 92)], sun=(254, 240, 206)),
        night=dict(sky=[(46, 46, 80), (92, 84, 118)], d1=(108, 96, 118), d2=(94, 82, 104), fl=[(100, 86, 102), (66, 56, 74)], sun=None),
        garden=dict(sky=[(190, 204, 214), (228, 226, 208)], d1=(160, 170, 128), d2=(142, 152, 110), fl=[(176, 170, 128), (134, 128, 94)], sun=(250, 248, 232)))
    r = np.random.RandomState(sum(map(ord, kind)))
    if kind in P:
        p = P[kind]; hz = 700
        col = _vgrad(SH, [(0, p['sky'][0]), (hz, p['sky'][1]), (hz + 1, p['fl'][0]), (SH - 1, p['fl'][1])])
        a = np.repeat(col[:, None, :], W, axis=1)
        im = Image.fromarray(a.astype(np.uint8), 'RGB'); d = ImageDraw.Draw(im, 'RGBA')
        if p['sun']:
            g = Image.new('L', (W, SH), 0); ImageDraw.Draw(g).ellipse((700, 60, 1020, 380), fill=150); ImageDraw.Draw(g).ellipse((780, 140, 940, 300), fill=255)
            g = g.filter(ImageFilter.GaussianBlur(40)); im.paste(Image.new('RGB', (W, SH), p['sun']), (0, 0), g.point(lambda v: int(v * .75)))
        else:
            for k in range(70):
                x, y, rr = r.randint(0, W), r.randint(20, 620), r.choice([2, 2, 3, 4]); d.ellipse((x - rr, y - rr, x + rr, y + rr), fill=(240, 236, 214, int(r.randint(120, 230))))
            mm = Image.new('L', (W, SH), 0); dm = ImageDraw.Draw(mm); dm.ellipse((790 * 1, 120, 910, 240), fill=255); dm.ellipse((826, 104, 936, 214), fill=0)
            im.paste(Image.new('RGB', (W, SH), (238, 232, 200)), (0, 0), mm.filter(ImageFilter.GaussianBlur(1.2)))
        d = ImageDraw.Draw(im)
        pts = [(x, 640 + 46 * math.sin(x / 210 + 1.3) + 22 * math.sin(x / 90)) for x in range(-20, W + 40, 20)]; d.polygon(pts + [(W + 20, 860), (-20, 860)], fill=p['d1'])
        pts = [(x, 716 + 34 * math.sin(x / 260 + 4.0) + 14 * math.sin(x / 70 + 1)) for x in range(-20, W + 40, 20)]; d.polygon(pts + [(W + 20, 900), (-20, 900)], fill=p['d2'])
        a = np.asarray(im).astype(np.float32); fy = 780
        t = np.clip((np.arange(SH) - (fy - 60)) / 120.0, 0, 1)[:, None, None]
        a = a * (1 - t) + np.repeat(col[:, None, :], W, axis=1) * t
        n = r.normal(0, 1, (SH, W)).astype(np.float32); k = np.where(np.arange(SH) > 640, 0.045, 0.014)[:, None]
        a *= (1 + n * k)[..., None]
        im = Image.fromarray(a.clip(0, 255).astype(np.uint8), 'RGB')
    else:
        if kind == 'desk': wall = [(172, 178, 188), (216, 212, 202)]; fy = 900; fl = [(206, 172, 126), (174, 138, 96)]; stripes = False
        elif kind == 'room': wall = [(226, 214, 188), (236, 226, 200)]; fy = 1010; fl = [(150, 104, 70), (116, 78, 52)]; stripes = True
        else: wall = [(196, 176, 150), (222, 202, 170)]; fy = 900; fl = [(190, 150, 108), (156, 118, 82)]; stripes = False   # 'sand': pared arena
        col = _vgrad(SH, [(0, wall[0]), (fy, wall[1]), (fy + 1, fl[0]), (SH - 1, fl[1])])
        a = np.repeat(col[:, None, :], W, axis=1); n = r.normal(0, 1, (SH, W)).astype(np.float32); a *= (1 + n * 0.02)[..., None]
        im = Image.fromarray(a.clip(0, 255).astype(np.uint8), 'RGB'); d = ImageDraw.Draw(im, 'RGBA')
        if stripes:
            for x in range(30, W, 64): d.line([(x, 0), (x, fy)], fill=(150, 130, 100, 60), width=3)
        d.rectangle((0, fy - 6, W, fy + 4), fill=(60, 44, 32, 70))
        y = fy + 70
        while y < SH:
            d.line([(0, y), (W, y)], fill=(70, 48, 30, 70), width=3); y += 78
        g = Image.new('L', (W, SH), 0); ImageDraw.Draw(g).rectangle((0, fy, W, fy + 50), fill=90); g = g.filter(ImageFilter.GaussianBlur(24))
        im.paste(Image.new('RGB', (W, SH), (40, 28, 20)), (0, 0), g.point(lambda v: int(v * .5)))
    _BG[kind] = im; return im

_yy, _xx = np.mgrid[0:SH, 0:W].astype(np.float32)
_v = 1 - 0.34 * np.clip(((_xx - W / 2) / (W * 0.62)) ** 2 + ((_yy - SH * 0.46) / (SH * 0.66)) ** 2, 0, 1.6) ** 1.5
VIG = Image.fromarray(np.repeat((np.clip(_v, 0, 1) * 255).astype(np.uint8)[..., None], 3, axis=2), 'RGB')
_dr = random.Random(11)
DUST = [(_dr.uniform(0, W), _dr.uniform(0, SH), _dr.uniform(-8, 8), _dr.uniform(-14, -4), _dr.choice([2, 2, 3, 3, 4, 5]), _dr.uniform(0, 6.28)) for _ in range(30)]
def finish(st, t):
    """polvo flotante + viñeta"""
    d = ImageDraw.Draw(st, 'RGBA')
    for x0, y0, vx, vy, r, ph in DUST:
        x = (x0 + vx * t + 14 * math.sin(t * 0.5 + ph)) % W; y = (y0 + vy * t) % SH
        a = int(70 + 60 * math.sin(t * 0.8 + ph)); d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 250, 236, max(20, a)))
    return ImageChops.multiply(st, VIG)
def gblur(im, r): return im.filter(ImageFilter.GaussianBlur(r)) if r > 0.4 else im
def hblur(im, k):
    """desenfoque de movimiento horizontal aproximado"""
    if k < 1.5: return im
    return im.resize((max(6, int(W / k)), SH), Image.BOX).resize((W, SH), Image.BILINEAR)
def cam(im, z, cx=W / 2, cy=SH / 2):
    if abs(z - 1) < 0.002: return im
    w, h = W / z, SH / z; x0 = clamp(cx - w / 2, 0, W - w); y0 = clamp(cy - h / 2, 0, SH - h)
    return im.resize((W, SH), Image.BILINEAR, box=(x0, y0, x0 + w, y0 + h))

# ------------------------------------------------------------------ panel inferior
TICKER = '¿SOLO EN DEFENSA PROPIA?|LO QUE DICEN LAS FUENTES ISLÁMICAS'
_PN = {}
def panel_base():
    if 'b' not in _PN:
        im = Image.new('RGB', (W, H - SH), (236, 229, 214)); im = grain(im, 0.035, 2)
        a = np.asarray(im).astype(np.float32); xx = np.linspace(-1, 1, W)[None, :, None]; a *= 1 - 0.05 * np.abs(xx) ** 2
        im = Image.fromarray(a.clip(0, 255).astype(np.uint8), 'RGB'); d = ImageDraw.Draw(im)
        d.rectangle((0, 0, W, 5), fill=(20, 18, 16)); d.line([(99, 227), (981, 227)], fill=(64, 58, 50), width=2)
        d.rectangle((0, 325, W, 378), fill=(18, 16, 15))
        _PN['b'] = im
        f = F('bebas', 31); parts = TICKER.split('|'); x = 0; segs = []
        for ptx in parts:
            segs.append((x, ptx, (244, 240, 230))); x += spaced_len(ptx, f, 3) + 34
            segs.append((x, '||||', (196, 36, 46))); x += spaced_len('||||', f, 1) + 34
        U = int(x); strip = Image.new('RGB', (U * (W // U + 2), 53), (18, 16, 15)); ds = ImageDraw.Draw(strip)
        for rep in range(W // U + 2):
            for sx, tx, colr in segs: spaced(ds, rep * U + sx, 28, tx, f, colr, 3 if tx != '||||' else 1)
        _PN['t'] = (strip, U)
    return _PN['b']
def spaced_len(t, f, sp): return sum(f.getlength(ch) + sp for ch in t)
def spaced(d, x, y, t, f, fill, sp=2):
    for ch in t:
        d.text((x, y), ch, font=f, fill=fill, anchor='lm'); x += f.getlength(ch) + sp
    return x
def draw_panel(frame, t, toks, source):
    """toks: [(texto, estado)] estado 0=por decir, 1=dicho, 2=clave dicha"""
    frame.paste(panel_base(), (0, SH)); d = ImageDraw.Draw(frame)
    strip, U = _PN['t']; off = int(t * 58) % U
    frame.paste(strip.crop((off, 0, off + W, 53)), (0, SH + 325))
    if source: spaced(d, 99, SH + 247, source, F('sans', 21), (112, 104, 94), 1.6)
    if toks:
        fs = 88
        while True:
            f = F('bebas', fs); sp = f.getlength(' '); tw = sum(f.getlength(w) for w, _ in toks) + sp * (len(toks) - 1)
            if tw <= 930 or fs <= 54: break
            fs -= 4
        x = W / 2 - tw / 2; y = SH + 92
        for w, stt in toks:
            d.text((x, y), w, font=f, fill=((188, 182, 170), (26, 24, 22), (178, 28, 40))[stt], anchor='lm'); x += f.getlength(w) + sp
