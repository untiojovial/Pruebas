# -*- coding: utf-8 -*-
# Motor de dibujo: monigotes, tarjetas, flechas, subtítulos. Lienzo 1080x1920 (TikTok).
import math, os
from PIL import Image, ImageDraw, ImageFont
W, H = 1080, 1920
B = os.path.dirname(os.path.abspath(__file__))
INK = (29, 36, 51)
PAL = dict(blue=(52, 98, 196), red=(205, 62, 62), gold=(214, 150, 30), green=(46, 140, 92), purple=(120, 78, 170),
           teal=(26, 128, 140), gray=(130, 136, 148), brown=(140, 92, 52), pink=(214, 96, 150), orange=(226, 120, 40))
_F = {}
def F(name, size):
    k = (name, size)
    if k not in _F:
        if name == 'title':
            f = ImageFont.truetype(B + '/fonts/Baloo2.ttf', size); f.set_variation_by_name('ExtraBold')
        elif name == 'bold':
            f = ImageFont.truetype(B + '/fonts/Baloo2.ttf', size); f.set_variation_by_name('Bold')
        elif name == 'semi':
            f = ImageFont.truetype(B + '/fonts/Baloo2.ttf', size); f.set_variation_by_name('SemiBold')
        elif name == 'hand':
            f = ImageFont.truetype(B + '/fonts/PatrickHand-Regular.ttf', size)
        elif name == 'greek':
            f = ImageFont.truetype(B + '/fonts/GentiumBookPlus-Regular.ttf', size)
        elif name == 'greekb':
            f = ImageFont.truetype(B + '/fonts/GentiumBookPlus-Bold.ttf', size)
        elif name == 'heb':
            f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', size)
        _F[k] = f
    return _F[k]

def ease(x):
    x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3
def lerp(a, b, t): return a + (b - a) * t
def mix(c1, c2, t): return tuple(int(lerp(a, b, t)) for a, b in zip(c1, c2))

def wrap(d, text, font, maxw):
    words = text.split(); lines = []; cur = ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def text_c(d, xy, text, font, fill=INK, stroke=0, sfill=(255, 255, 255), anchor='mm'):
    d.text(xy, text, font=font, fill=fill, anchor=anchor, stroke_width=stroke, stroke_fill=sfill)

def rrect(d, box, r, fill, outline=None, w=4):
    d.rounded_rectangle(box, r, fill=fill, outline=outline, width=w)

def card(d, x, y, w, lines, font, color=INK, bg=(255, 255, 255), border=None, pad=24, lh=None, title=None, tfont=None, tcolor=None, align='l', shadow=True):
    """Tarjeta con título opcional y líneas ya envueltas o texto (str)."""
    if isinstance(lines, str): lines = wrap(d, lines, font, w - 2 * pad)
    lh = lh or int(font.size * 1.22)
    th = 0
    tl = []
    if title:
        tfont = tfont or F('title', int(font.size * 0.9)); tl = wrap(d, title, tfont, w - 2 * pad); th = len(tl) * int(tfont.size * 1.15) + 8
    h = pad * 2 + th + lh * len(lines)
    if shadow: rrect(d, (x + 8, y + 10, x + w + 8, y + h + 10), 26, (0, 0, 0, 40) if False else mix(bg, INK, 0.18))
    rrect(d, (x, y, x + w, y + h), 26, bg, border or INK, 5)
    yy = y + pad
    for t in tl:
        d.text((x + pad if align == 'l' else x + w / 2, yy), t, font=tfont, fill=tcolor or color, anchor='la' if align == 'l' else 'ma'); yy += int(tfont.size * 1.15)
    if tl: yy += 8
    for t in lines:
        d.text((x + pad if align == 'l' else x + w / 2, yy), t, font=font, fill=color, anchor='la' if align == 'l' else 'ma'); yy += lh
    return h

def arrow(d, p1, p2, color=INK, w=8, head=26):
    d.line([p1, p2], fill=color, width=w)
    a = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
    pts = [p2, (p2[0] - head * math.cos(a - 0.45), p2[1] - head * math.sin(a - 0.45)), (p2[0] - head * math.cos(a + 0.45), p2[1] - head * math.sin(a + 0.45))]
    d.polygon(pts, fill=color)

def check(d, x, y, s=1.0, color=PAL['green']):
    d.line([(x - 28 * s, y), (x - 6 * s, y + 24 * s), (x + 34 * s, y - 26 * s)], fill=color, width=int(14 * s), joint='curve')
def cross(d, x, y, s=1.0, color=PAL['red']):
    d.line([(x - 26 * s, y - 26 * s), (x + 26 * s, y + 26 * s)], fill=color, width=int(14 * s))
    d.line([(x - 26 * s, y + 26 * s), (x + 26 * s, y - 26 * s)], fill=color, width=int(14 * s))

def pill(d, x, y, text, color, font=None, fg=(255, 255, 255), anchor='mm'):
    font = font or F('bold', 34)
    tw = d.textlength(text, font=font); h = font.size + 16
    if anchor == 'mm': box = (x - tw / 2 - 20, y - h / 2, x + tw / 2 + 20, y + h / 2)
    else: box = (x, y - h / 2, x + tw + 40, y + h / 2)
    rrect(d, box, h / 2, color)
    d.text(((box[0] + box[2]) / 2, y + 2), text, font=font, fill=fg, anchor='mm')
    return box

def stamp(d, x, y, text, color, size=70, angle_txt=None):
    f = F('title', size); tw = d.textlength(text, font=f)
    rrect(d, (x - tw / 2 - 30, y - size * 0.7, x + tw / 2 + 30, y + size * 0.7), 18, None, color, 9)
    d.text((x, y + 4), text, font=f, fill=color, anchor='mm')

def scroll(d, x, y, w, h, title, lines, font, color=INK):
    paper = (250, 240, 214)
    rrect(d, (x, y, x + w, y + h), 18, paper, INK, 5)
    d.ellipse((x - 22, y - 10, x + 22, y + 34), fill=(222, 204, 160), outline=INK, width=5)
    d.ellipse((x + w - 22, y + h - 34, x + w + 22, y + h + 10), fill=(222, 204, 160), outline=INK, width=5)
    yy = y + 26
    if title:
        d.text((x + w / 2, yy), title, font=F('title', int(font.size * 0.95)), fill=PAL['brown'], anchor='ma'); yy += int(font.size * 1.3)
    for t in lines:
        d.text((x + w / 2, yy), t, font=font, fill=color, anchor='ma'); yy += int(font.size * 1.25)

# ---------------- monigote ----------------
def figure(d, x, y, s=1.0, color=PAL['blue'], talk=0.0, t=0.0, name=None, acc=(), arms=None, ghost=False, phase=0.0, face=1, mood='ok'):
    """Monigote con pies en (x, y). talk 0..1 abre la boca. acc: beard, mitre, glasses, hat, hair, dress, cap, cloak, scroll, kid, ring."""
    ink = (170, 176, 188) if ghost else INK
    col = (190, 196, 206) if ghost else color
    bob = 4 * s * math.sin(2 * math.pi * 0.55 * t + phase)
    y = y + bob
    lw = max(3, int(9 * s))
    hr = 40 * s
    hx, hy = x, y - 205 * s
    neck = (x, y - 160 * s); hip = (x, y - 70 * s)
    # piernas
    d.line([hip, (x - 30 * s, y)], fill=ink, width=lw); d.line([hip, (x + 30 * s, y)], fill=ink, width=lw)
    if 'dress' in acc:
        d.polygon([(x, y - 150 * s), (x - 52 * s, y - 25 * s), (x + 52 * s, y - 25 * s)], fill=col, outline=ink)
    elif 'cloak' in acc:
        d.polygon([(x - 14 * s, y - 158 * s), (x + 14 * s, y - 158 * s), (x + 46 * s, y - 20 * s), (x - 46 * s, y - 20 * s)], fill=col, outline=ink)
    else:
        d.line([neck, hip], fill=col, width=int(lw * 1.9))
    # brazos
    sh = (x, y - 140 * s)
    wig = (math.sin(2 * math.pi * 1.4 * t + phase) * 0.35 if talk > 0.05 else 0)
    if arms == 'up': angs = (-2.3 + wig, -0.85 - wig)
    elif arms == 'point': angs = (2.35, -0.35 * face + wig * 0.3) if face > 0 else (-2.8 - wig * 0.3, 0.8)
    elif arms == 'cross': angs = (0.6, 2.5)
    elif arms == 'shrug': angs = (-2.6, -0.55)
    else: angs = (2.15 + wig, 0.95 - wig)
    for a in angs:
        ex = sh[0] + math.cos(a) * 52 * s; ey = sh[1] + math.sin(a) * 52 * s
        hx2 = ex + math.cos(a + 0.4) * 46 * s; hy2 = ey + math.sin(a + 0.4) * 46 * s
        d.line([sh, (ex, ey), (hx2, hy2)], fill=ink, width=lw, joint='curve')
    if 'scroll' in acc:
        a = angs[1]; ex = sh[0] + math.cos(a) * 52 * s + math.cos(a + 0.4) * 46 * s; ey = sh[1] + math.sin(a) * 52 * s + math.sin(a + 0.4) * 46 * s
        d.rounded_rectangle((ex - 10 * s, ey - 30 * s, ex + 14 * s, ey + 30 * s), 6, fill=(250, 240, 214), outline=ink, width=max(2, lw // 2))
    # cabeza
    if 'hair' in acc:
        d.ellipse((hx - hr * 1.15, hy - hr * 1.1, hx + hr * 1.15, hy + hr * 1.45), fill=(120, 72, 40) if not ghost else col)
    d.ellipse((hx - hr, hy - hr, hx + hr, hy + hr), fill=(255, 255, 255) if not ghost else (236, 238, 242), outline=ink, width=lw)
    if 'beard' in acc:
        d.chord((hx - hr * 0.95, hy - hr * 0.2, hx + hr * 0.95, hy + hr * 1.55), 0, 180, fill=(205, 205, 210) if not ghost else (226, 228, 232), outline=ink, width=max(2, lw // 2))
    # ojos (parpadeo)
    blink = (t * 0.31 + phase) % 1.0 < 0.035
    ey_ = hy - 8 * s
    for dx in (-14 * s, 14 * s):
        ex_ = hx + dx + 5 * s * face
        if blink: d.line([(ex_ - 6 * s, ey_), (ex_ + 6 * s, ey_)], fill=ink, width=max(2, lw // 2))
        else: d.ellipse((ex_ - 5.5 * s, ey_ - 6.5 * s, ex_ + 5.5 * s, ey_ + 6.5 * s), fill=ink)
    if 'glasses' in acc:
        for dx in (-15 * s, 15 * s):
            ex_ = hx + dx + 5 * s * face; d.ellipse((ex_ - 12 * s, ey_ - 11 * s, ex_ + 12 * s, ey_ + 11 * s), outline=ink, width=max(2, lw // 3))
    # boca
    my = hy + 16 * s + (6 * s if 'beard' in acc else 0); mx = hx + 5 * s * face
    if talk > 0.05:
        oh = (6 + 16 * talk) * s
        d.ellipse((mx - 11 * s, my - oh / 2, mx + 11 * s, my + oh / 2), fill=(150, 40, 50), outline=ink, width=max(2, lw // 3))
    elif mood == 'sad':
        d.arc((mx - 13 * s, my, mx + 13 * s, my + 16 * s), 200, 340, fill=ink, width=max(2, lw // 2))
    else:
        d.arc((mx - 13 * s, my - 10 * s, mx + 13 * s, my + 6 * s), 20, 160, fill=ink, width=max(2, lw // 2))
    # sombreros
    if 'mitre' in acc:
        d.polygon([(hx - hr * 0.8, hy - hr * 0.75), (hx + hr * 0.8, hy - hr * 0.75), (hx + hr * 0.55, hy - hr * 2.0), (hx, hy - hr * 2.35), (hx - hr * 0.55, hy - hr * 2.0)], fill=(250, 246, 232), outline=ink)
        d.line([(hx, hy - hr * 0.8), (hx, hy - hr * 2.3)], fill=PAL['gold'], width=max(2, lw // 2))
    if 'hat' in acc:
        d.rectangle((hx - hr * 1.15, hy - hr * 0.95, hx + hr * 1.15, hy - hr * 0.75), fill=INK)
        d.rectangle((hx - hr * 0.7, hy - hr * 1.75, hx + hr * 0.7, hy - hr * 0.9), fill=INK)
    if 'cap' in acc:
        d.chord((hx - hr * 1.0, hy - hr * 1.15, hx + hr * 1.0, hy + hr * 0.25), 180, 360, fill=col, outline=ink)
        d.rectangle((hx + (0 if face > 0 else -hr * 1.5), hy - hr * 0.48, hx + (hr * 1.5 if face > 0 else 0), hy - hr * 0.36), fill=col)
    if 'kipa' in acc:
        d.chord((hx - hr * 0.6, hy - hr * 1.05, hx + hr * 0.6, hy - hr * 0.45), 180, 360, fill=PAL['blue'])
    if 'crown' in acc:
        d.polygon([(hx - hr * 0.8, hy - hr * 0.8), (hx - hr * 0.8, hy - hr * 1.6), (hx - hr * 0.4, hy - hr * 1.2), (hx, hy - hr * 1.75), (hx + hr * 0.4, hy - hr * 1.2), (hx + hr * 0.8, hy - hr * 1.6), (hx + hr * 0.8, hy - hr * 0.8)], fill=PAL['gold'], outline=ink)
    if 'halo' in acc:
        d.ellipse((hx - hr * 0.9, hy - hr * 1.55, hx + hr * 0.9, hy - hr * 1.15), outline=PAL['gold'], width=max(3, lw // 2))
    if name:
        f = F('bold', max(22, int(34 * s)))
        tw = d.textlength(name, font=f)
        rrect(d, (x - tw / 2 - 14, y + 14 * s, x + tw / 2 + 14, y + 14 * s + f.size + 12), 14, col if not ghost else (205, 208, 214))
        d.text((x, y + 14 * s + (f.size + 12) / 2 + 2), name, font=f, fill=(255, 255, 255), anchor='mm')

def bubble(d, x, y, w, text, font=None, tail=None, color=INK, bg=(255, 255, 255)):
    font = font or F('hand', 46)
    lines = wrap(d, text, font, w - 40); lh = int(font.size * 1.12)
    h = len(lines) * lh + 34
    rrect(d, (x, y, x + w, y + h), 30, bg, INK, 5)
    if tail:
        tx, ty = tail
        bx = min(max(tx, x + 40), x + w - 40)
        d.polygon([(bx - 22, y + h - 3), (bx + 22, y + h - 3), (tx, ty)], fill=bg)
        d.line([(bx - 22, y + h), (tx, ty), (bx + 22, y + h)], fill=INK, width=5)
    yy = y + 17
    for l in lines:
        d.text((x + w / 2, yy), l, font=font, fill=color, anchor='ma'); yy += lh
    return h
