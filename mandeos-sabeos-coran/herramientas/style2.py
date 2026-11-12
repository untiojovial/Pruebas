# -*- coding: utf-8 -*-
"""Estilo 2: figuras planas con cara (parpadeo y boca), sombreado en dos tonos, fondos cinematográficos
y panel inferior oscuro con barra de capítulos (sin cinta «||||»)."""
import math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import paper as P
from paper import Cut, Sp, one, stack, put, F, W, H, SH, clamp, ease, eout, lerp, mix, shade, grain, SPAD

INK2 = (38, 34, 44)
TEAL = (64, 168, 164); GOLDK = (240, 178, 72); REDK = (214, 64, 70)
SKIN2 = [(236, 196, 160), (214, 168, 128), (176, 128, 92), (242, 214, 188), (150, 104, 74)]

# ------------------------------------------------------------------ figuras con cara
_FIG = {}
def figure(coat=(70, 90, 120), tunic=(238, 234, 224), skin=0, head='turban', headcol=(240, 238, 230), beard=None, hair=None,
           trim=None, sash=None, glasses=False, female=False, stole=None, **kw):
    key = (coat, tunic, skin, head, headcol, beard, hair, trim, sash, glasses, female, stole)
    if key in _FIG: return _FIG[key]
    sk = SKIN2[skin % len(SKIN2)] if isinstance(skin, int) else skin
    BW, BH = 420, 470; ox, oy = BW / 2, BH - 18
    L = []
    c = Cut(BW, BH, ox, oy)
    for sg in (-1, 1): c.rr((sg * 48 - 34, -26, sg * 48 + 34, 6), 14, shade(coat, 0.45), 3, INK2)
    L.append((c.out(0), 0, 0, False))
    # túnica / manto con sombreado de dos tonos
    c = Cut(BW, BH, ox, oy)
    body = [(-96, -420), (96, -420), (128, -22), (-128, -22)]
    c.poly(body, tunic, 4, INK2)
    c.poly([(8, -420), (96, -420), (128, -22), (20, -22)], shade(tunic, 0.88), 0)
    c.line(body + body[:1], INK2, 4)
    if coat and coat != tunic:
        for sg in (-1, 1):
            pts = [(sg * 96, -420), (sg * 30, -420), (sg * 44, -22), (sg * 128, -22)]
            c.poly(pts, coat, 4, INK2)
            c.poly([(sg * 70, -420), (sg * 96, -420), (sg * 128, -22), (sg * 92, -22)], shade(coat, 0.82), 0)
            c.line(pts + pts[:1], INK2, 4)
            if trim: c.line([(sg * 32, -416), (sg * 46, -26)], trim, 6)
    if stole:
        for sg in (-1, 1): c.poly([(sg * 22, -420), (sg * 40, -420), (sg * 34, -150), (sg * 16, -150)], stole, 3, INK2)
    if sash: c.rr((-100, -236, 100, -208), 6, sash, 3, INK2)
    c.line([(-24, -420), (0, -384), (24, -420)], INK2, 4)
    L.append((c.out(0.03, 1), 0, 0, dict(off=(3, 6), blur=6, op=.30)))
    bodysp = stack(BW, BH, L, ox, oy)
    # brazo (cuelga desde el hombro)
    AW, AH = 110, 320; aox, aoy = AW / 2, 22
    c = Cut(AW, AH, aox, aoy); col = coat or tunic
    c.poly([(-34, -12), (34, -12), (40, 222), (-40, 222)], col, 4, INK2)
    c.poly([(6, -12), (34, -12), (40, 222), (12, 222)], shade(col, 0.82), 0); c.line([(-34, -12), (34, -12), (40, 222), (-40, 222), (-34, -12)], INK2, 4)
    c.ell((-27, 214, 27, 268), sk, 4, INK2)
    arm = one(c.out(0.02, 3), aox, aoy, off=(2, 4), blur=5, op=.28)
    # cabeza: 4 variantes (boca 0/1 × ojos abiertos/cerrados)
    heads = {}
    for mo in (0, 1):
        for bl in (0, 1):
            HW, HH = 280, 330; hox, hoy = HW / 2, HH - 40
            c = Cut(HW, HH, hox, hoy)
            if head == 'long' or female:
                c.rr((-84, -190, 84, 40 if female else 10), 60, hair or (70, 50, 36), 4, INK2)
            if head in ('keffiyeh', 'veil'):
                c.rr((-92, -200, 92, 30), 56, headcol, 4, INK2)
            c.rr((-20, -40, 20, 6), 8, shade(sk, 0.9), 4, INK2)               # cuello
            c.ell((-74, -186, 74, -26), sk, 4, INK2)                           # cara
            c.chord((-74, -186, 74, -26), 300, 60, shade(sk, 0.93), 0)         # sombra lateral
            c.ell((-86, -118, -64, -86), sk, 3, INK2); c.ell((64, -118, 86, -86), sk, 3, INK2)  # orejas
            if hair and head not in ('turban', 'kufi', 'keffiyeh', 'veil', 'helmet'):
                c.chord((-78, -196, 78, -100), 180, 360, hair, 4, INK2)
            # ojos
            for sg in (-1, 1):
                ex = sg * 28
                if bl: c.line([(ex - 10, -110), (ex + 10, -110)], INK2, 4)
                else:
                    c.ell((ex - 9, -122, ex + 9, -100), (252, 250, 246), 3, INK2); c.ell((ex - 4, -116, ex + 5, -105), INK2, 0)
                c.line([(ex - 14, -134 - (2 if sg > 0 else 0)), (ex + 12, -136)], shade(hair or (60, 44, 34), 0.8), 5)
            c.ell((-46, -96, -30, -84), mix(sk, (230, 120, 110), .35), 0); c.ell((30, -96, 46, -84), mix(sk, (230, 120, 110), .35), 0)
            c.line([(0, -104), (-5, -84), (3, -82)], shade(sk, 0.7), 3)   # nariz
            if beard:
                c.chord((-66, -150, 66, -6), 15, 165, beard, 4, INK2)
                c.chord((-64, -150, 64, -6), 15, 165, beard, 0)
            if mo: c.ell((-12, -74, 12, -54), (120, 46, 50), 3, INK2)
            else: c.arc((-14, -84, 14, -62), 20, 160, INK2, 4)
            if glasses:
                for sg in (-1, 1): c.ell((sg * 28 - 17, -126, sg * 28 + 17, -96), None, 4, INK2)
                c.line([(-11, -112), (11, -112)], INK2, 3)
            if head == 'turban':
                c.ell((-84, -236, 84, -138), headcol, 4, INK2)
                for k in (-1, 0, 1): c.arc((-70 + k * 30, -230, 50 + k * 30, -150), 200, 300, shade(headcol, 0.78), 3)
            elif head == 'kufi': c.chord((-72, -212, 72, -130), 180, 360, headcol, 4, INK2)
            elif head == 'keffiyeh':
                c.chord((-80, -214, 80, -120), 180, 360, headcol, 4, INK2); c.rr((-82, -170, 82, -156), 6, (40, 36, 40), 3, INK2)
            elif head == 'veil': c.chord((-78, -214, 78, -120), 180, 360, headcol, 4, INK2)
            elif head == 'mandaean':   # turbante blanco de sacerdote mandeo con caída lateral
                c.ell((-80, -232, 80, -140), headcol, 4, INK2); c.poly([(56, -170), (92, -150), (86, -40), (62, -60)], headcol, 4, INK2)
            heads[(mo, bl)] = one(c.out(0.02, 5 + mo), hox, hoy, off=(2, 4), blur=4, op=.25)
    f = dict(body=bodysp, arm=arm, heads=heads); _FIG[key] = f; return f

def draw_fig(dst, f, x, y, s=1.0, aL=6, aR=6, tilt=0.0, holdL=None, holdR=None, a=1.0, talk=0.0, t=0.0, seed=0):
    put(dst, f['body'], x, y, s, 0, a)
    for sg, ang, hold in ((-1, aL, holdL), (1, aR, holdR)):
        sx, sy = x + sg * 108 * s, y - 398 * s; th = math.radians(sg * ang)
        if hold is not None: put(dst, hold, sx + math.sin(th) * 240 * s, sy + math.cos(th) * 240 * s, s, sg * ang, a)
        put(dst, f['arm'], sx, sy, s, sg * ang, a)
    blink = 1 if ((t * 0.37 + seed * 0.13) % 1.0) < 0.035 else 0
    mo = 1 if talk > 0 and math.sin(t * 22 + seed) > -0.1 else 0
    put(dst, f['heads'][(mo, blink)], x, y - 412 * s, s, tilt, a)

# ------------------------------------------------------------------ objetos nuevos
_M = {}
def memo(fn):
    def w(*a, **k):
        kk = (fn.__name__, a, tuple(sorted(k.items())))
        if kk not in _M: _M[kk] = fn(*a, **k)
        return _M[kk]
    return w
@memo
def staff(L=520):
    c = Cut(90, L + 40, 45, 20)
    c.rr((-7, 0, 7, L), 5, (126, 96, 60), 3, INK2); c.poly([(7, 40), (42, 56), (36, 130), (7, 112)], (238, 236, 226), 3, INK2)
    return one(c.out(0.04), 45, 20 + L * 0.42, off=(2, 4), blur=4, op=.3)
@memo
def bowl(d=300, seed=0):
    c = Cut(d + 20, d * 0.62 + 20, d / 2 + 10, 10)
    c.chord((-d / 2, -d * 0.3, d / 2, d * 0.6), 0, 180, (206, 176, 136), 4, INK2)
    c.ell((-d / 2, -d * 0.12, d / 2, d * 0.12), (226, 202, 164), 4, INK2)
    r = random.Random(seed)
    for k in range(24):
        a = k / 24 * math.pi * 2; rr = d * 0.36 - k * 2.2
        c.line([(math.cos(a) * rr * 0.9, math.sin(a) * rr * 0.22), (math.cos(a + 0.2) * (rr - 3) * 0.9, math.sin(a + 0.2) * (rr - 3) * 0.22)], (96, 70, 50), 2)
    return one(c.out(0.08), d / 2 + 10, 10 + d * 0.3)
@memo
def amulet():
    c = Cut(260, 120, 0, 0); c.rr((10, 20, 250, 100), 30, (150, 150, 158), 4, INK2)
    for k in range(4): c.line([(40, 40 + k * 16), (220, 40 + k * 16)], (96, 96, 104), 2)
    return one(c.out(0.08), 130, 60)
@memo
def scrollbig(title='', col=(234, 222, 192), w=420, h=260):
    c = Cut(w + 60, h + 40, 30, 20); c.rr((0, 0, w, h), 6, col, 4, INK2); c.ell((-26, -10, 26, h + 10), shade(col, 0.88), 4, INK2); c.ell((w - 26, -10, w + 26, h + 10), shade(col, 0.88), 4, INK2)
    for k in range(6): c.line([(46, 60 + k * 30), (w - 46, 60 + k * 30)], (150, 128, 96), 3)
    if title: c.text((w / 2, 30), title, 'bebas', 40, INK2)
    return one(c.out(0.06), (w + 60) / 2, (h + 40) / 2)
@memo
def reeds(seed=0, n=9, h=240):
    c = Cut(360, h + 20, 0, h + 10); r = random.Random(seed)
    for k in range(n):
        x = 20 + k * 36 + r.uniform(-8, 8); hh = h * r.uniform(0.6, 1.0); bend = r.uniform(-30, 30)
        c.line([(x, 0), (x + bend * 0.4, -hh * 0.5), (x + bend, -hh)], (64, 96, 64), 5)
        c.ell((x + bend - 7, -hh - 34, x + bend + 7, -hh + 4), (120, 86, 52), 0)
    return one(c.out(0.04), 180, h + 10, off=(2, 3), blur=3, op=.2)
@memo
def card2(title, body, w=880, col=TEAL, tcol=(250, 248, 240), fs=46, h=None):
    f = F('bebas', fs); words = body.split(); lines = [[]]
    for wd in words:
        if f.getlength(' '.join(lines[-1] + [wd])) > w - 80 and lines[-1]: lines.append([])
        lines[-1].append(wd)
    hh = h or (110 + len(lines) * int(fs * 1.06) + 30)
    c = Cut(w + 10, hh + 10, 5, 5); c.rr((0, 0, w, hh), 22, (30, 34, 44), 0); c.rr((0, 0, w, 74), 22, col, 0, corners=(True, True, False, False))
    c.text((36, 38), title, 'bebas', 50, tcol, anchor='lm')
    y = 110 + fs * 0.5
    for ln in lines: c.text((40, y), ' '.join(ln), 'bebas', fs, (236, 234, 228), anchor='lm'); y += fs * 1.06
    return one(c.out(0.02), (w + 10) / 2, (hh + 10) / 2, off=(5, 8), blur=8, op=.45)
@memo
def tag2(text, size=54, bg=(26, 30, 38), fg=(244, 242, 236), accent=TEAL):
    f = F('bebas', size); tw = f.getlength(text); w, h = int(tw + 64), int(size * 1.36)
    c = Cut(w + 10, h + 10, 5, 5); c.rr((0, 0, w, h), 10, bg, 0); c.rr((0, 0, 12, h), 6, accent, 0, corners=(True, False, False, True))
    c.text((w / 2 + 6, h / 2 + size * 0.05), text, 'bebas', size, fg)
    return one(c.out(0.02), (w + 10) / 2, (h + 10) / 2, off=(4, 7), blur=6, op=.45)
@memo
def premise(n, text, w=900, col=TEAL, fs=42):
    f = F('bebas', fs); words = text.split(); lines = [[]]
    for wd in words:
        if f.getlength(' '.join(lines[-1] + [wd])) > w - 170 and lines[-1]: lines.append([])
        lines[-1].append(wd)
    hh = max(120, 36 + len(lines) * int(fs * 1.08) + 20)
    c = Cut(w + 10, hh + 10, 5, 5); c.rr((0, 0, w, hh), 18, (244, 241, 234), 4, INK2)
    c.ell((22, hh / 2 - 44, 110, hh / 2 + 44), col, 0); c.text((66, hh / 2 + 3), str(n), 'anton', 54, (250, 248, 242))
    y = hh / 2 - (len(lines) - 1) * fs * 0.54
    for ln in lines: c.text((136, y), ' '.join(ln), 'bebas', fs, INK2, anchor='lm'); y += fs * 1.08
    return one(c.out(0.02), (w + 10) / 2, (hh + 10) / 2, off=(4, 7), blur=6, op=.38)

# ------------------------------------------------------------------ fondos
_BG = {}
def bg2(kind):
    if kind in _BG: return _BG[kind]
    r = np.random.RandomState(sum(map(ord, kind)))
    yy = np.arange(SH)[:, None, None]
    def grad(stops):
        a = np.zeros((SH, 3), np.float32); ys = np.arange(SH)
        for (y0, c0), (y1, c1) in zip(stops, stops[1:]):
            m = (ys >= y0) & (ys <= y1); t = ((ys[m] - y0) / max(1, y1 - y0))[:, None]; a[m] = np.array(c0) * (1 - t) + np.array(c1) * t
        return np.repeat(a[:, None, :], W, axis=1)
    if kind == 'river':
        a = grad([(0, (246, 196, 146)), (560, (250, 226, 186)), (700, (198, 176, 140)), (760, (120, 156, 160)), (1100, (70, 116, 128)), (SH - 1, (44, 78, 92))])
        im = Image.fromarray(a.clip(0, 255).astype(np.uint8)); d = ImageDraw.Draw(im, 'RGBA')
        g = Image.new('L', (W, SH), 0); ImageDraw.Draw(g).ellipse((620, 340, 960, 680), fill=255); g = g.filter(ImageFilter.GaussianBlur(50))
        im.paste(Image.new('RGB', (W, SH), (255, 236, 200)), (0, 0), g.point(lambda v: int(v * .8)))
        d = ImageDraw.Draw(im, 'RGBA')
        pts = [(x, 640 + 30 * math.sin(x / 160) + 12 * math.sin(x / 55)) for x in range(-20, W + 40, 20)]; d.polygon(pts + [(W + 20, 770), (-20, 770)], fill=(150, 136, 104, 255))
        for k in range(9):   # palmeras lejanas
            x = r.randint(0, W); y = 660 + r.randint(-20, 20); hgt = r.randint(110, 190); col = (96, 98, 82, 255)
            d.line([(x, y), (x + 8, y - hgt)], fill=col, width=7)
            for a_ in range(6): ang = math.radians(200 + a_ * 28); d.line([(x + 8, y - hgt), (x + 8 + math.cos(ang) * 70, y - hgt + math.sin(ang) * 34 + 26)], fill=col, width=6)
        d.rectangle((0, 760, W, 778), fill=(230, 220, 190, 90))
    elif kind == 'study':
        a = grad([(0, (34, 40, 54)), (900, (52, 60, 76)), (901, (96, 66, 46)), (SH - 1, (64, 42, 30))])
        im = Image.fromarray(a.clip(0, 255).astype(np.uint8)); d = ImageDraw.Draw(im, 'RGBA')
        for row in range(3):
            y0 = 140 + row * 230; d.rectangle((40, y0 + 190, W - 40, y0 + 204), fill=(80, 58, 40, 255))
            x = 60
            while x < W - 70:
                bw = r.randint(26, 46); bh = r.randint(130, 185); col = [(120, 60, 50), (60, 80, 110), (90, 110, 70), (150, 120, 70), (80, 60, 90)][r.randint(0, 4)]
                d.rectangle((x, y0 + 190 - bh, x + bw, y0 + 190), fill=col + (150,)); x += bw + r.randint(2, 6)
        d.rectangle((0, 0, W, 900), fill=(20, 24, 34, 120))
        g = Image.new('L', (W, SH), 0); ImageDraw.Draw(g).ellipse((90, 300, 990, 1300), fill=255); g = g.filter(ImageFilter.GaussianBlur(120))
        im.paste(Image.new('RGB', (W, SH), (255, 220, 160)), (0, 0), g.point(lambda v: int(v * .18)))
        d = ImageDraw.Draw(im, 'RGBA'); y = 960
        while y < SH: d.line([(0, y), (W, y)], fill=(40, 26, 18, 90), width=3); y += 90
    elif kind == 'court':
        a = grad([(0, (18, 22, 32)), (SH - 1, (30, 36, 50))])
        im = Image.fromarray(a.clip(0, 255).astype(np.uint8))
        g = Image.new('L', (W, SH), 0); ImageDraw.Draw(g).polygon([(420, 0), (660, 0), (1000, SH), (80, SH)], fill=255); g = g.filter(ImageFilter.GaussianBlur(60))
        im.paste(Image.new('RGB', (W, SH), (120, 136, 160)), (0, 0), g.point(lambda v: int(v * .32)))
        d = ImageDraw.Draw(im, 'RGBA'); d.ellipse((140, 1300, 940, 1440), fill=(140, 160, 190, 50))
    elif kind == 'map':
        a = grad([(0, (60, 70, 80)), (SH - 1, (34, 40, 50))]); im = Image.fromarray(a.clip(0, 255).astype(np.uint8))
    elif kind == 'garden':
        a = grad([(0, (196, 214, 222)), (640, (236, 230, 206)), (700, (150, 164, 118)), (SH - 1, (106, 120, 84))]); im = Image.fromarray(a.clip(0, 255).astype(np.uint8))
        d = ImageDraw.Draw(im, 'RGBA'); pts = [(x, 640 + 40 * math.sin(x / 200 + 1)) for x in range(-20, W + 40, 20)]; d.polygon(pts + [(W + 20, 760), (-20, 760)], fill=(140, 156, 108, 255))
    else:
        im = P.bg(kind).copy()
    n = r.normal(0, 1, (SH, W)).astype(np.float32); a = np.asarray(im).astype(np.float32) * (1 + n * 0.018)[..., None]
    im = Image.fromarray(a.clip(0, 255).astype(np.uint8)); _BG[kind] = im; return im

def waves(st, t, y0=820, y1=SH, amp=1.0):
    d = ImageDraw.Draw(st, 'RGBA')
    for k in range(14):
        y = y0 + (k + 0.5) * (y1 - y0) / 14; ph = t * (0.8 + k * 0.05) + k
        pts = [(x, y + 6 * amp * math.sin(x / 70 + ph)) for x in range(0, W + 30, 30)]
        d.line(pts, fill=(220, 236, 236, 70 - k * 3), width=3)

# ------------------------------------------------------------------ panel inferior nuevo
_PB = {}
def panel_base():
    if 'b' not in _PB:
        h = H - SH; a = np.zeros((h, W, 3), np.float32)
        top = np.array((30, 34, 44)); bot = np.array((18, 20, 28)); t = np.linspace(0, 1, h)[:, None, None]
        a[:] = top * (1 - t) + bot * t
        n = np.random.RandomState(4).normal(0, 1, (h, W)).astype(np.float32); a *= (1 + n * 0.02)[..., None]
        im = Image.fromarray(a.clip(0, 255).astype(np.uint8)); d = ImageDraw.Draw(im)
        d.rectangle((0, 0, W, 5), fill=TEAL); d.line([(80, 236), (1000, 236)], fill=(70, 76, 90), width=2)
        _PB['b'] = im
    return _PB['b']
def wave_icon(d, x, y, col, s=1.0):
    for k in range(3):
        pts = [(x + i * 3 * s, y + k * 9 * s + 4 * s * math.sin(i * 0.7)) for i in range(12)]
        d.line(pts, fill=col, width=max(2, int(3 * s)))
def draw_panel(frame, t, toks, source, ch, nch, chname, chprog):
    frame.paste(panel_base(), (0, SH)); d = ImageDraw.Draw(frame)
    if source:
        d.rectangle((80, SH + 252, 90, SH + 262), fill=TEAL); P.spaced(d, 102, SH + 257, source, F('sans', 21), (150, 156, 168), 1.4)
    # barra de capítulos
    y = SH + 330
    wave_icon(d, 80, y - 12, TEAL, 1.0)
    P.spaced(d, 128, y, f'{ch + 1:02d} · {chname}', F('bebas', 38), (226, 232, 236), 2)
    x0, x1 = 600, 1000; gw = (x1 - x0 - (nch - 1) * 8) / nch
    for k in range(nch):
        xa = x0 + k * (gw + 8); d.rounded_rectangle((xa, y - 6, xa + gw, y + 6), 6, fill=(56, 62, 76))
        fillw = gw if k < ch else (gw * clamp(chprog) if k == ch else 0)
        if fillw > 2: d.rounded_rectangle((xa, y - 6, xa + fillw, y + 6), 6, fill=TEAL if k < ch else GOLDK)
    if toks:
        fs = 86
        while True:
            f = F('bebas', fs); sp = f.getlength(' '); tw = sum(f.getlength(w) for w, _ in toks) + sp * (len(toks) - 1)
            if tw <= 920 or fs <= 54: break
            fs -= 4
        x = W / 2 - tw / 2; yy = SH + 118
        for w, stt in toks:
            col = ((92, 98, 112), (244, 242, 236), GOLDK)[stt]
            d.text((x, yy), w, font=f, fill=col, anchor='lm'); x += f.getlength(w) + sp

@memo
def nearmap():
    """Oriente Próximo: Mediterráneo, Jordán, Tigris, Éufrates y golfo Pérsico."""
    w, h = 900, 820; c = Cut(w + 10, h + 10, 5, 5); c.rr((0, 0, w, h), 10, (236, 224, 192), 4, INK2)
    sea = (150, 186, 198)
    c.poly([(0, 0), (120, 0), (150, 120), (130, 260), (160, 420), (120, 600), (0, 640)], sea, 3, INK2)
    c.poly([(640, h), (700, 700), (780, 640), (900, 600), (900, h)], sea, 3, INK2)
    c.line([(236, 380), (240, 430), (232, 480), (238, 520)], (70, 120, 150), 6)            # Jordán
    c.line([(420, 120), (470, 230), (540, 360), (600, 470), (650, 560), (700, 690)], (70, 120, 150), 7)   # Éufrates
    c.line([(560, 90), (590, 200), (630, 320), (660, 430), (690, 540), (710, 680)], (70, 120, 150), 7)   # Tigris
    c.text((64, 330), 'MAR', 'bebas', 32, (60, 96, 110)); c.text((64, 362), 'MEDIT.', 'bebas', 32, (60, 96, 110))
    c.text((800, 730), 'GOLFO', 'bebas', 30, (60, 96, 110)); c.text((800, 760), 'PÉRSICO', 'bebas', 30, (60, 96, 110))
    c.text((498, 300), 'ÉUFRATES', 'bebas', 28, (50, 90, 120), anchor='rm'); c.text((682, 250), 'TIGRIS', 'bebas', 28, (50, 90, 120), anchor='lm')
    c.text((262, 400), 'JORDÁN', 'bebas', 28, (50, 90, 120), anchor='lm')
    for n, (x, y), side in (('JERUSALÉN', (236, 470), 'l'), ('HARRÁN', (470, 110), 'r'), ('BAGDAD', (620, 420), 'r'), ('SUR DE IRAK', (700, 640), 'l'), ('JUZESTÁN (IRÁN)', (800, 560), 'l')):
        c.ell((x - 10, y - 10, x + 10, y + 10), INK2, 0)
        c.text((x - 16, y + 2) if side == 'l' else (x + 16, y + 2), n, 'bebas', 34, INK2, anchor='rm' if side == 'l' else 'lm')
    return one(c.out(0.05), (w + 10) / 2, (h + 10) / 2, off=(6, 9), blur=8, op=.45)
NEARPT = {'Jerusalem': (236, 470), 'Harran': (470, 110), 'Bagdad': (620, 420), 'SurIrak': (700, 640)}
