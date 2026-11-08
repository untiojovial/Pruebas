# -*- coding: utf-8 -*-
# Personajes y escenarios en estilo «dibujo a mano»: trazo de tinta temblón, relleno de acuarela, sombreado a rayas.
import math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
W, H = 1080, 1920
INK = (38, 30, 24)
PAPER = (240, 229, 204)

def rng(seed, t=0.0, boil=True):
    # «boil»: el trazo cambia ligeramente cada 4 fotogramas, como en animación dibujada
    k = int(t * 6) if boil else 0
    return random.Random(hash((seed, k)) & 0xffffffff)

def wob(pts, r, amp):
    return [(x + r.uniform(-amp, amp), y + r.uniform(-amp, amp)) for x, y in pts]

def sline(d, pts, seed, t=0.0, w=4, col=INK, amp=1.6, passes=2):
    r = rng(seed, t)
    for p in range(passes):
        q = wob(pts, r, amp)
        d.line(q, fill=col, width=max(1, w - p), joint='curve')

def spoly(d, pts, seed, t=0.0, fill=None, w=4, col=INK, amp=1.6):
    r = rng(seed, t)
    if fill: d.polygon(wob(pts, r, amp * 0.5), fill=fill)
    q = wob(pts, r, amp); sline(d, q + [q[0]], seed + 7, t, w, col, amp * 0.6)

def sellipse(d, box, seed, t=0.0, fill=None, w=4, col=INK, amp=1.4, n=28):
    x0, y0, x1, y1 = box; cx, cy = (x0 + x1) / 2, (y0 + y1) / 2; rx, ry = (x1 - x0) / 2, (y1 - y0) / 2
    pts = [(cx + rx * math.cos(2 * math.pi * k / n), cy + ry * math.sin(2 * math.pi * k / n)) for k in range(n)]
    spoly(d, pts, seed, t, fill, w, col, amp)

def hatch(d, box, seed, t=0.0, step=11, col=(60, 48, 38), w=2, ang=1.0, clip=None):
    x0, y0, x1, y1 = box; r = rng(seed, t)
    for k in range(int(-(y1 - y0)), int(x1 - x0), step):
        a = (x0 + k, y1); b = (x0 + k + (y1 - y0) * ang, y0)
        d.line(wob([a, b], r, 1.2), fill=col, width=w)

_CANVAS = [None]
def set_canvas(im): _CANVAS[0] = im
def hatch_poly(poly, seed, t=0.0, step=11, col=(60, 48, 38), w=2, ang=0.35):
    im = _CANVAS[0]
    if im is None: return
    xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
    x0, y0, x1, y1 = int(min(xs)) - 2, int(min(ys)) - 2, int(max(xs)) + 2, int(max(ys)) + 2
    if x1 <= x0 or y1 <= y0: return
    m = Image.new('L', (x1 - x0, y1 - y0), 0); ImageDraw.Draw(m).polygon([(px - x0, py - y0) for px, py in poly], fill=150)
    lay = Image.new('L', m.size, 0); dl = ImageDraw.Draw(lay); r = rng(seed, t)
    hgt = y1 - y0
    for k in range(-hgt, x1 - x0, step):
        dl.line(wob([(k, hgt), (k + hgt * ang, 0)], r, 1.0), fill=255, width=w)
    from PIL import ImageChops
    a = ImageChops.multiply(lay, m)
    im.paste(Image.new('RGB', m.size, col), (x0, y0), a)

def paper(seed=1):
    r = np.random.default_rng(seed)
    base = np.ones((H, W, 3), np.float32) * np.array(PAPER, np.float32)
    noise = r.normal(0, 6, (H // 4, W // 4)).astype(np.float32)
    noise = np.array(Image.fromarray(noise).resize((W, H), Image.BICUBIC))
    fib = r.normal(0, 3, (H, W)).astype(np.float32)
    base += (noise + fib)[..., None]
    yy, xx = np.mgrid[0:H, 0:W]
    vig = ((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H / 2) / (H * 0.75)) ** 2
    base *= (1 - 0.18 * vig)[..., None]
    return Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))

# ---------- personas ----------
SKIN = [(214, 170, 130), (196, 150, 108), (226, 188, 150), (176, 128, 92)]

def person(d, x, y, s=1.0, spec=None, talk=0.0, t=0.0, seed=0, pose='stand', face=1, walk=0.0):
    """Persona de cuerpo entero con los pies en (x, y). spec: dict(skin, robe, robe2, head, beard, prop, female, hair, sash)."""
    sp = dict(skin=SKIN[0], robe=(232, 222, 200), robe2=(200, 186, 160), head='keffiyeh', headcol=(236, 230, 214), beard='full', beardcol=(52, 40, 32), prop=None, female=False, hair=(40, 30, 24), sash=None, cape=None)
    sp.update(spec or {})
    bob = 3 * s * math.sin(2 * math.pi * 0.5 * t + seed)
    y = y + bob
    hh = 40 * s  # semialtura de cabeza
    hx, hy = x, y - 342 * s
    sh_y = y - 284 * s; hip_y = y - 150 * s
    # piernas/pies (asoman bajo la túnica)
    st = math.sin(walk * 2 * math.pi) * 14 * s
    for dx, sg in ((-14 * s, 1), (14 * s, -1)):
        sellipse(d, (x + dx - 16 * s + st * sg, y - 10 * s, x + dx + 20 * s + st * sg, y + 6 * s), seed + 11 + sg, t, fill=(92, 70, 52), w=3)
    # capa
    if sp['cape']:
        spoly(d, [(x - 58 * s, sh_y), (x + 58 * s, sh_y), (x + 82 * s, y - 14 * s), (x - 82 * s, y - 14 * s)], seed + 3, t, fill=sp['cape'], w=4)
    # túnica (trapecio)
    robe = [(x - 40 * s, sh_y), (x - 18 * s, sh_y - 6 * s), (x + 18 * s, sh_y - 6 * s), (x + 40 * s, sh_y), (x + 56 * s, y - 12 * s), (x - 56 * s, y - 12 * s)]
    spoly(d, robe, seed + 1, t, fill=sp['robe'], w=4)
    hatch_poly([(x + 8 * s, sh_y + 10 * s), (x + 40 * s, sh_y), (x + 56 * s, y - 12 * s), (x + 8 * s, y - 12 * s)], seed + 2, t, step=int(10 * s) + 4, col=tuple(max(0, c - 55) for c in sp['robe']), w=2)
    d.line([(x, sh_y + 30 * s), (x, y - 20 * s)], fill=tuple(max(0, c - 50) for c in sp['robe']), width=2)
    if sp['sash']:
        spoly(d, [(x - 50 * s, hip_y - 8 * s), (x + 50 * s, hip_y - 8 * s), (x + 52 * s, hip_y + 12 * s), (x - 52 * s, hip_y + 12 * s)], seed + 4, t, fill=sp['sash'], w=3)
    # brazos
    wig = math.sin(2 * math.pi * 1.3 * t + seed) * 0.35 if talk > 0.05 else 0
    sh = [(x - 38 * s, sh_y + 8 * s), (x + 38 * s, sh_y + 8 * s)]
    if pose == 'raise': angs = (-2.4 + wig, -0.75 - wig)
    elif pose == 'point': angs = (1.9, -0.25 + wig * 0.4) if face > 0 else (-2.9 - wig * 0.4, 1.2)
    elif pose == 'sword': angs = (1.8, -1.2)
    elif pose == 'read': angs = (1.0, 2.1)
    elif pose == 'cross': angs = (0.8, 2.3)
    else: angs = (1.9 + wig, 1.2 - wig)
    hands = []
    for (sx, sy), a, sg in ((sh[0], angs[0], -1), (sh[1], angs[1], 1)):
        a = a if sg < 0 else a  # ángulos absolutos
        ex = sx + math.cos(a) * 70 * s; ey = sy + math.sin(a) * 70 * s
        hx2 = ex + math.cos(a + 0.25 * sg) * 64 * s; hy2 = ey + math.sin(a + 0.25 * sg) * 64 * s
        sline(d, [(sx, sy), (ex, ey), (hx2, hy2)], seed + 20 + sg, t, w=int(24 * s), col=tuple(max(0, c - 25) for c in sp['robe']), amp=0.6, passes=1)
        sline(d, [(sx, sy), (ex, ey), (hx2, hy2)], seed + 22 + sg, t, w=3, col=INK, amp=1.2, passes=1)
        sellipse(d, (hx2 - 10 * s, hy2 - 10 * s, hx2 + 10 * s, hy2 + 10 * s), seed + 24 + sg, t, fill=sp['skin'], w=3)
        hands.append((hx2, hy2))
    # objeto
    if sp['prop'] == 'sword':
        hx2, hy2 = hands[1]
        sline(d, [(hx2, hy2), (hx2 + 16 * s, hy2 - 120 * s)], seed + 30, t, w=int(9 * s) + 2, col=(150, 156, 164), passes=1)
        sline(d, [(hx2, hy2), (hx2 + 16 * s, hy2 - 120 * s)], seed + 31, t, w=2)
        sline(d, [(hx2 - 16 * s, hy2 - 4 * s), (hx2 + 18 * s, hy2 + 2 * s)], seed + 32, t, w=5, col=(110, 80, 40))
    elif sp['prop'] == 'spear':
        hx2, hy2 = hands[1]
        sline(d, [(hx2, hy2 + 120 * s), (hx2, hy2 - 170 * s)], seed + 33, t, w=5, col=(110, 80, 50))
        spoly(d, [(hx2 - 9 * s, hy2 - 168 * s), (hx2 + 9 * s, hy2 - 168 * s), (hx2, hy2 - 205 * s)], seed + 34, t, fill=(170, 172, 178), w=2)
    elif sp['prop'] in ('book', 'scroll'):
        cx = (hands[0][0] + hands[1][0]) / 2; cy = (hands[0][1] + hands[1][1]) / 2
        if sp['prop'] == 'book':
            spoly(d, [(cx - 44 * s, cy - 30 * s), (cx + 44 * s, cy - 30 * s), (cx + 44 * s, cy + 24 * s), (cx - 44 * s, cy + 24 * s)], seed + 35, t, fill=(120, 40, 36), w=3)
            d.line([(cx, cy - 30 * s), (cx, cy + 24 * s)], fill=(230, 200, 120), width=3)
        else:
            spoly(d, [(cx - 40 * s, cy - 22 * s), (cx + 40 * s, cy - 22 * s), (cx + 40 * s, cy + 22 * s), (cx - 40 * s, cy + 22 * s)], seed + 35, t, fill=(246, 234, 200), w=3)
    if sp['prop'] == 'shield':
        hx2, hy2 = hands[0]
        sellipse(d, (hx2 - 40 * s, hy2 - 50 * s, hx2 + 40 * s, hy2 + 40 * s), seed + 36, t, fill=(130, 90, 50), w=4)
        sellipse(d, (hx2 - 10 * s, hy2 - 15 * s, hx2 + 10 * s, hy2 + 5 * s), seed + 37, t, fill=(200, 170, 90), w=2)
    # cuello y cabeza
    spoly(d, [(x - 12 * s, sh_y - 4 * s), (x + 12 * s, sh_y - 4 * s), (x + 10 * s, hy + hh * 0.7), (x - 10 * s, hy + hh * 0.7)], seed + 40, t, fill=sp['skin'], w=3)
    if sp['female']:
        sellipse(d, (hx - hh * 1.25, hy - hh * 1.25, hx + hh * 1.25, hy + hh * 1.6), seed + 41, t, fill=sp['headcol'], w=4)
    sellipse(d, (hx - hh * 0.82, hy - hh, hx + hh * 0.82, hy + hh), seed + 42, t, fill=sp['skin'], w=4)
    # cabello
    if sp['head'] == 'none' and not sp['female']:
        d.chord((hx - hh * 0.84, hy - hh * 1.04, hx + hh * 0.84, hy + hh * 0.2), 180, 360, fill=sp['hair'])
    # cara
    ex = 5 * s * face
    blink = (t * 0.29 + seed * 0.13) % 1.0 < 0.03
    for dx in (-hh * 0.33, hh * 0.33):
        cx_, cy_ = hx + dx + ex, hy - hh * 0.12
        if blink: d.line([(cx_ - 9 * s, cy_), (cx_ + 9 * s, cy_)], fill=INK, width=3)
        else:
            d.ellipse((cx_ - 8 * s, cy_ - 5 * s, cx_ + 8 * s, cy_ + 5 * s), fill=(250, 246, 236), outline=INK, width=2)
            d.ellipse((cx_ - 3.8 * s + ex * 0.4, cy_ - 3.8 * s, cx_ + 3.8 * s + ex * 0.4, cy_ + 3.8 * s), fill=INK)
        d.line([(cx_ - 10 * s, cy_ - 12 * s), (cx_ + 10 * s, cy_ - 14 * s if dx < 0 else cy_ - 12 * s)], fill=INK, width=max(2, int(4 * s)))
    sline(d, [(hx + ex + 2 * s, hy - hh * 0.05), (hx + ex + 8 * s * face, hy + hh * 0.28), (hx + ex, hy + hh * 0.32)], seed + 43, t, w=3)
    my = hy + hh * 0.55
    if sp['beard'] == 'full':
        spoly(d, [(hx - hh * 0.8, hy + hh * 0.05), (hx - hh * 0.6, hy + hh * 0.85), (hx, hy + hh * 1.35), (hx + hh * 0.6, hy + hh * 0.85), (hx + hh * 0.8, hy + hh * 0.05), (hx + hh * 0.45, hy + hh * 0.48), (hx - hh * 0.45, hy + hh * 0.48)], seed + 44, t, fill=sp['beardcol'], w=3)
        my = hy + hh * 0.62
    elif sp['beard'] == 'short':
        spoly(d, [(hx - hh * 0.8, hy + hh * 0.1), (hx - hh * 0.5, hy + hh * 0.8), (hx, hy + hh * 1.0), (hx + hh * 0.5, hy + hh * 0.8), (hx + hh * 0.8, hy + hh * 0.1), (hx + hh * 0.4, hy + hh * 0.5), (hx - hh * 0.4, hy + hh * 0.5)], seed + 44, t, fill=sp['beardcol'], w=3)
    if talk > 0.05:
        oh = (5 + 14 * talk) * s
        d.ellipse((hx + ex - 10 * s, my - oh / 2, hx + ex + 10 * s, my + oh / 2), fill=(110, 30, 34), outline=INK, width=2)
    else:
        d.line([(hx + ex - 10 * s, my), (hx + ex + 10 * s, my - 1)], fill=INK, width=3)
    # tocado
    if sp['head'] == 'keffiyeh':
        spoly(d, [(hx - hh * 0.95, hy - hh * 0.55), (hx, hy - hh * 1.25), (hx + hh * 0.95, hy - hh * 0.55), (hx + hh * 1.05, hy + hh * 1.2), (hx + hh * 0.75, hy + hh * 1.25), (hx + hh * 0.78, hy - hh * 0.2), (hx - hh * 0.78, hy - hh * 0.2), (hx - hh * 0.75, hy + hh * 1.25), (hx - hh * 1.05, hy + hh * 1.2)], seed + 45, t, fill=sp['headcol'], w=4)
        sline(d, [(hx - hh * 0.92, hy - hh * 0.62), (hx + hh * 0.92, hy - hh * 0.62)], seed + 46, t, w=int(7 * s) + 2, col=(40, 34, 30))
    elif sp['head'] == 'turban':
        sellipse(d, (hx - hh * 0.98, hy - hh * 1.55, hx + hh * 0.98, hy - hh * 0.35), seed + 45, t, fill=sp['headcol'], w=4)
        for k in range(3): sline(d, [(hx - hh * 0.8, hy - hh * (0.6 + 0.25 * k)), (hx + hh * 0.8, hy - hh * (0.8 + 0.22 * k))], seed + 47 + k, t, w=2)
    elif sp['head'] == 'helmet':
        d.chord((hx - hh * 0.92, hy - hh * 1.3, hx + hh * 0.92, hy + hh * 0.1), 180, 360, fill=(140, 144, 150), outline=INK, width=4)
        sline(d, [(hx + ex, hy - hh * 0.55), (hx + ex, hy + hh * 0.05)], seed + 48, t, w=6, col=(120, 124, 130))
    if sp['female']:
        spoly(d, [(hx - hh * 0.9, hy - hh * 0.6), (hx, hy - hh * 1.2), (hx + hh * 0.9, hy - hh * 0.6), (hx + hh * 0.86, hy - hh * 0.35), (hx - hh * 0.86, hy - hh * 0.35)], seed + 49, t, fill=sp['headcol'], w=3)

def camel(d, x, y, s=1.0, t=0.0, seed=0, walk=0.0, col=(196, 160, 112), face=1, rider=None):
    f = face
    legs_y = y; body_y = y - 150 * s
    ph = walk * 2 * math.pi
    for k, (dx, off) in enumerate(((-70, 0), (-50, math.pi), (55, math.pi), (75, 0))):
        sw = math.sin(ph + off) * 18 * s
        top = (x + dx * s * f, body_y + 20 * s)
        knee = (x + dx * s * f + sw * 0.6, y - 70 * s)
        foot = (x + dx * s * f + sw, y)
        sline(d, [top, knee, foot], seed + k, t, w=int(14 * s) + 2, col=tuple(c - 20 for c in col), amp=0.8, passes=1)
        sline(d, [top, knee, foot], seed + 10 + k, t, w=3)
    if rider:
        person(d, x + 15 * s * f, body_y + 40 * s, s * 0.75, rider, 0, t, seed + 50, pose='sword' if rider.get('prop') == 'sword' else 'stand', face=f)
    sellipse(d, (x - 105 * s, body_y - 45 * s, x + 105 * s, body_y + 45 * s), seed + 20, t, fill=col, w=4)
    sellipse(d, (x - 55 * s * f - 35 * s, body_y - 95 * s, x - 55 * s * f + 40 * s, body_y - 20 * s), seed + 21, t, fill=col, w=4)
    nk = [(x + 85 * s * f, body_y - 10 * s), (x + 145 * s * f, body_y - 60 * s), (x + 160 * s * f, body_y - 120 * s)]
    sline(d, nk, seed + 22, t, w=int(30 * s), col=col, amp=0.5, passes=1); sline(d, nk, seed + 23, t, w=3)
    sellipse(d, (x + 140 * s * f - 22 * s, body_y - 150 * s, x + 140 * s * f + 48 * s * f if f > 0 else x + 140 * s * f + 22 * s, body_y - 108 * s), seed + 24, t, fill=col, w=3)
    d.ellipse((x + 165 * s * f - 4 * s, body_y - 138 * s, x + 165 * s * f + 4 * s, body_y - 130 * s), fill=INK)
    hatch_poly([(x - 80 * s, body_y + 10 * s), (x + 80 * s, body_y + 10 * s), (x + 60 * s, body_y + 40 * s), (x - 60 * s, body_y + 40 * s)], seed + 25, t, step=10, col=tuple(c - 50 for c in col), w=2)

def palm(d, x, y, s=1.0, t=0.0, seed=0):
    pts = [(x + math.sin(k / 6) * 10 * s, y - k * 30 * s) for k in range(12)]
    sline(d, pts, seed, t, w=int(22 * s), col=(140, 104, 70), amp=0.5, passes=1); sline(d, pts, seed + 1, t, w=3)
    top = pts[-1]
    for k in range(7):
        a = -math.pi / 2 + (k - 3) * 0.5 + math.sin(t * 1.5 + k) * 0.05
        e = (top[0] + math.cos(a) * 130 * s, top[1] + math.sin(a) * 90 * s + 50 * s)
        mid = (top[0] + math.cos(a) * 70 * s, top[1] + math.sin(a) * 70 * s)
        spoly(d, [top, mid, e, (mid[0] + 8 * s, mid[1] + 14 * s)], seed + 10 + k, t, fill=(92, 128, 70), w=3)

def dunes(d, y, seed, t=0.0, col=(222, 196, 150)):
    pts = [(x, y + 30 * math.sin(x / 160 + seed) + 15 * math.sin(x / 57)) for x in range(-20, W + 40, 40)]
    d.polygon(pts + [(W + 40, H), (-20, H)], fill=col)
    sline(d, pts, seed, t, w=4, amp=1.0, passes=1)

def fortress(d, x, y, w, h, t=0.0, seed=0):
    spoly(d, [(x, y), (x + w, y), (x + w, y - h), (x, y - h)], seed, t, fill=(184, 160, 126), w=5)
    for k in range(int(w // 50)):
        bx = x + 10 + k * 50
        spoly(d, [(bx, y - h), (bx + 28, y - h), (bx + 28, y - h - 30), (bx, y - h - 30)], seed + 1 + k, t, fill=(184, 160, 126), w=4)
    for k in range(4):
        sline(d, [(x + 10, y - h * (k + 1) / 5), (x + w - 10, y - h * (k + 1) / 5)], seed + 20 + k, t, w=2, col=(120, 100, 76))
    spoly(d, [(x + w / 2 - 40, y), (x + w / 2 + 40, y), (x + w / 2 + 40, y - 90), (x + w / 2 - 40, y - 90)], seed + 30, t, fill=(80, 56, 40), w=4)

def tent(d, x, y, s=1.0, t=0.0, seed=0, col=(120, 84, 60)):
    spoly(d, [(x - 120 * s, y), (x, y - 140 * s), (x + 120 * s, y)], seed, t, fill=col, w=4)
    spoly(d, [(x - 30 * s, y), (x, y - 80 * s), (x + 30 * s, y)], seed + 1, t, fill=(50, 34, 26), w=3)
