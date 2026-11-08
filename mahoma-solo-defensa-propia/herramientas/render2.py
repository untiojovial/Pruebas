# -*- coding: utf-8 -*-
import json, math, os, re, subprocess, sys, wave, hashlib
import numpy as np
from PIL import Image, ImageDraw
B = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, B + '/../vid'); sys.path.insert(0, B)
import engine as E
from engine import F, wrap, rrect, ease, mix
from sketch import *
from script import SCENES, VOICES

FPS = 24; GAP = 0.28; LEAD = 0.45; TAIL = 0.40
PG = B + '/pg'
SEP = (88, 52, 30); RED = (160, 40, 36); GOLD = (196, 140, 40); GREEN = (46, 110, 70); BLUE = (40, 70, 120); GRAY = (120, 110, 96)

def hkey(spk, text):
    v, r, p = VOICES[spk]; return hashlib.sha1(f'{v}|{r}|{p}|{text}'.encode()).hexdigest()[:12]
def wav_info(p):
    w = wave.open(p); n = w.getnframes(); sr = w.getframerate()
    return np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768, sr
def align(text, words):
    toks = text.split(); out = []; j = 0
    norm = lambda s: re.sub(r'[^\wáéíóúüñÁÉÍÓÚÜÑ]', '', s.lower())
    for (off, du, w) in words:
        nw = norm(w); disp = w
        for k in range(j, min(j + 4, len(toks))):
            if norm(toks[k]) and (norm(toks[k]).startswith(nw) or nw.startswith(norm(toks[k]))):
                disp = toks[k]; j = k + 1; break
        out.append((off, du, disp))
    return out
def chunks(words, maxw=6):
    out = []; cur = []
    for w in words:
        cur.append(w)
        if len(cur) >= maxw or (re.search(r'[.,;:!?¡¿]$', w[2]) and len(cur) >= 2): out.append(cur); cur = []
    if cur: out.append(cur)
    return out
def build_timeline():
    T = []; t = 0.0
    for si, s in enumerate(SCENES):
        sc = dict(i=si, start=t, id=s['id'], title=s['title'], vis=s['vis'], segs=[]); t += LEAD
        for spk, text in s['segs']:
            key = hkey(spk, text); a, sr = wav_info(f'{B}/audh/{key}.wav'); dur = len(a) / sr
            hop = int(sr / FPS); env = np.array([float(np.sqrt(np.mean(a[k:k + hop] ** 2))) for k in range(0, len(a), hop)])
            env = np.clip(env / max(1e-6, np.percentile(env, 95)), 0, 1)
            sc['segs'].append(dict(spk=spk, text=text, key=key, t0=t, dur=dur, words=align(text, json.load(open(f'{B}/audh/{key}.json'))), env=env))
            t += dur + GAP
        t += TAIL - GAP; sc['end'] = t; T.append(sc)
    return T, t

class Ctx:
    def __init__(s, sc, lt, gt):
        s.sc = sc; s.lt = lt; s.gt = gt; s.seg = -1; s.st = 0.0; s.spk = None; s.amp = 0.0
        for gi, g in enumerate(sc['segs']):
            if gt >= g['t0'] - 0.05: s.seg = gi; s.st = gt - g['t0']
        if s.seg >= 0:
            g = sc['segs'][s.seg]
            if 0 <= s.st <= g['dur']:
                s.spk = g['spk']; k = int(s.st * FPS); s.amp = float(g['env'][k]) if k < len(g['env']) else 0.0
    def on(s, k, dt=0.0, dur=0.45):
        if k >= len(s.sc['segs']): return 0.0
        return ease((s.gt - s.sc['segs'][k]['t0'] - dt) / dur)
    def talk(s, who): return s.amp if s.spk == who else 0.0
def slide(p, y): return y + (1 - p) * 60

IM = {}; FOC = {}; VW = {}
PGH = B + '/pgh'
def hires(name):
    if name not in IM:
        p = f'{PGH}/{name}' if os.path.exists(f'{PGH}/{name}') else f'{PG}/{name}'
        im = Image.open(p).convert('RGB'); a = np.asarray(im).astype(int)
        m = (a[..., 0] > 215) & (a[..., 1] > 185) & (a[..., 2] < 165) & (a[..., 0] - a[..., 2] > 80)
        ys, xs = np.nonzero(m)
        FOC[name] = (xs.min(), ys.min(), xs.max(), ys.max()) if len(xs) > 50 else (0, 0, im.width, im.height)
        PADB = 1200; pad = Image.new('RGB', (im.width + 2 * PADB, im.height + 2 * PADB), (250, 248, 240)); pad.paste(im, (PADB, PADB))
        IM[name] = (im.size, pad, PADB)
    return IM[name]
def view(name, bw, bh, z, src=None):
    z = round(max(0.0, min(1.0, z)), 3)
    k = (name, bw, bh, z, src)
    if k in VW: return VW[k]
    (iw, ih), pad, PB = hires(name)
    if src: ox0, oy0, ox1, oy1 = src; iw2, ih2 = ox1 - ox0, oy1 - oy0
    else: ox0, oy0, iw2, ih2 = 0, 0, iw, ih
    A = bw / bh
    fx0, fy0, fx1, fy1 = FOC[name]; cx, cy = (fx0 + fx1) / 2, (fy0 + fy1) / 2
    w0 = iw2; h0 = w0 / A
    if h0 < ih2: c0 = (ox0 + iw2 / 2, min(max(cy, oy0 + h0 / 2), oy0 + ih2 - h0 / 2))
    else: h0 = ih2; w0 = h0 * A; c0 = (ox0 + iw2 / 2, oy0 + ih2 / 2)
    fw = (fx1 - fx0) * 1.10 + 70; fh = (fy1 - fy0) * 1.35 + 90
    if fw / fh < A: fw = fh * A
    else: fh = fw / A
    fw = max(fw, bw * 0.8); fw = min(fw, w0); fh = fw / A
    w = w0 + (fw - w0) * z; h = w / A; c = (c0[0] + (cx - c0[0]) * z, c0[1] + (cy - c0[1]) * z)
    box = (int(c[0] - w / 2 + PB), int(c[1] - h / 2 + PB), int(c[0] + w / 2 + PB), int(c[1] + h / 2 + PB))
    out = pad.crop(box).resize((bw, bh), Image.LANCZOS if z in (0.0, 1.0) else Image.BILINEAR)
    if z in (0.0, 1.0): VW[k] = out
    return out
def scan(im, d, name, y, bh=700, cap=None, p=1.0, z=1.0, bw=960, x=None, src=None):
    """Recorte de página con zoom: z=0 vista general, z=1 zoom a la zona subrayada."""
    if p <= 0: return y
    s = view(name, bw, bh, z, src); y = int(slide(p, y)); x = x if x is not None else (W - bw) // 2
    d.rectangle((x + 10, y + 12, x + bw + 10, y + bh + 12), fill=(150, 130, 100))
    im.paste(s, (x, y)); d.rectangle((x, y, x + bw, y + bh), outline=INK, width=3)
    for tx in (x + 30, x + bw - 90):
        d.polygon([(tx, y - 14), (tx + 70, y - 8), (tx + 64, y + 18), (tx - 6, y + 12)], fill=(236, 222, 170))
    if cap:
        f = F('bold', 28); tw = d.textlength(cap, font=f)
        d.rounded_rectangle((x + 14, y + bh - 30, x + 14 + tw + 32, y + bh + 22), 12, fill=(46, 32, 22))
        d.text((x + 30, y + bh - 4), cap, font=f, fill=(246, 234, 206), anchor='lm')
    return y + bh
def zin(ctx, k, dt):
    """zoom que empieza 1.2 s después de aparecer el recorte"""
    return ease((ctx.gt - ctx.sc['segs'][k]['t0'] - dt - 1.2) / 1.6) if k < len(ctx.sc['segs']) else 1.0

def card(d, x, y, w, lines, font, color=INK, bg=(250, 242, 222), border=SEP, title=None, tcolor=RED, align='l', tfont=None):
    return E.card(d, x, y, w, lines, font, color=color, bg=bg, border=border, title=title, tcolor=tcolor, align=align, tfont=tfont)
def pill(d, x, y, t, c, f=None): return E.pill(d, x, y, t, c, f or F('bold', 34))
def stamp(d, x, y, t, c, size=60): E.stamp(d, x, y, t, c, size)

# ---------- personajes ----------
NAR = dict(skin=SKIN[2], robe=(52, 66, 96), head='none', beard='short', beardcol=(70, 52, 38), hair=(60, 44, 30))
DEF = dict(skin=SKIN[1], robe=(232, 232, 226), head='turban', headcol=(246, 246, 240), beard='short', beardcol=(40, 30, 24))
ARAB = lambda c=(196, 170, 130), h='keffiyeh', p=None, s=0: dict(skin=SKIN[s % 4], robe=c, head=h, headcol=(228, 218, 196), prop=p, beardcol=(48, 36, 28))
SCHOLAR = lambda c=(70, 90, 70): dict(skin=SKIN[0], robe=c, head='turban', headcol=(244, 242, 232), beard='full', beardcol=(200, 196, 190), prop='book')
def narr(d, ctx, x=900, y=1500, s=0.8, pose=None):
    person(d, x, y, s, NAR, ctx.talk('N'), ctx.gt, 101, pose=pose or ('point' if ctx.talk('N') else 'stand'), face=-1)
def defe(d, ctx, x=220, y=1500, s=1.0):
    person(d, x, y, s, DEF, ctx.talk('D'), ctx.gt, 202, pose='raise' if ctx.talk('D') else 'cross', face=1)

def sky(d, col=(206, 220, 226), h=700):
    d.rectangle((0, 0, W, h), fill=col)
def night(d, h=900):
    d.rectangle((0, 0, W, h), fill=(46, 52, 78))
    for k in range(40):
        r = random.Random(k); x, y = r.randint(0, W), r.randint(260, h - 40); d.ellipse((x - 2, y - 2, x + 2, y + 2), fill=(240, 236, 210))
    d.ellipse((800, 270, 900, 370), fill=(240, 230, 190)); d.ellipse((830, 260, 920, 360), fill=(46, 52, 78))

# ---------- mapa ----------
MAP = dict(Meca=(560, 1010), Medina=(500, 640), Najla=(650, 975), Badr=(400, 760), Jaybar=(560, 470), Tabuk=(330, 280), Taif=(690, 1060))
LBL = dict(Meca=('La Meca', -20, 20, 'rm'), Najla=('Najla', 18, -14, 'lb'), Taif=('Taif', 18, 10, 'lm'))
def hijaz(d, t, seed=5, show=('Meca', 'Medina', 'Badr', 'Jaybar', 'Tabuk')):
    d.rectangle((60, 260, 960, 1220), fill=(232, 214, 176))
    sea = [(60, 260), (260, 260)] + [(260 - k * 14 + 18 * math.sin(k), 260 + k * 60) for k in range(16)] + [(60, 1220)]
    d.polygon(sea, fill=(150, 186, 196)); sline(d, sea[1:-1], seed, t, w=4)
    d.text((150, 420), 'Mar Rojo', font=F('hand', 40), fill=(40, 70, 90), anchor='mm')
    d.rectangle((60, 260, 960, 1220), outline=SEP, width=5)
    for n in show:
        x, y = MAP[n]; lab, dx, dy, an = LBL.get(n, (n, 20, 0, 'lm'))
        d.ellipse((x - 11, y - 11, x + 11, y + 11), fill=INK)
        d.text((x + dx, y + dy), lab, font=F('bold', 34), fill=INK, anchor=an)
def dash(d, p1, p2, col, w=6, seg=22, prog=1.0):
    x1, y1 = p1; x2, y2 = p2; L = math.hypot(x2 - x1, y2 - y1); n = int(L / seg)
    for k in range(0, int(n * prog), 2):
        a = k / n; b = min(1, (k + 1) / n)
        d.line([(x1 + (x2 - x1) * a, y1 + (y2 - y1) * a), (x1 + (x2 - x1) * b, y1 + (y2 - y1) * b)], fill=col, width=w)

GUI = 'Ibn Ishaq, Sira (trad. Guillaume 1955), p. '
# ---------- escenas ----------
def v_hook(d, im, ctx):
    sky(d, (214, 200, 170), 1000); dunes(d, 1000, 3, ctx.gt)
    if ctx.seg <= 0 or ctx.talk('D'):
        E.bubble(d, 300, 560, 640, 'Mahoma solo luchó en defensa propia.', font=F('hand', 56), tail=(250, 1050))
    defe(d, ctx, 230, 1500, 1.0)
    if ctx.seg >= 1:
        d.text((560, 300), 'vídeo anterior: los críticos', font=F('semi', 32), fill=SEP, anchor='mm')
        for k, n in enumerate(["Ka'b ibn al-Ashraf", "'Asma' bint Marwan", "Abu 'Afak"]):
            q = ctx.on(1, 0.3 + k * 1.1)
            if q: pill(d, 560, slide(q, 360 + k * 80), n, RED, F('bold', 36))
    if ctx.seg >= 2:
        for k, (n, c) in enumerate([('Corán', GREEN), ('Tafsir', BLUE), ('Bujari · Muslim', GOLD), ('Ibn Ishaq', SEP)]):
            q = ctx.on(2, 0.4 + k * 0.9)
            if q:
                y = slide(q, 640 + k * 100)
                for j in range(3): d.rectangle((420 + j * 6, y - 40 + j * 8, 820 + j * 6, y + 30 + j * 8), fill=mix(c, (255, 255, 255), 0.25 + j * 0.15), outline=INK)
                d.text((620, y - 5), n, font=F('title', 42), fill=(255, 255, 255), anchor='mm')
    narr(d, ctx, 870, 1500, 1.0)

def v_medina(d, im, ctx):
    hijaz(d, ctx.gt)
    p = ctx.on(0, 0.5)
    if p:
        dash(d, MAP['Meca'], MAP['Medina'], RED, prog=p); d.text((600, 820), 'Hégira 622', font=F('hand', 46), fill=RED, anchor='lm')
    p1 = ctx.on(1, 1.0)
    if p1:
        dash(d, (600, 1180), (420, 300), GOLD, 5, prog=p1)
        d.text((440, 320), 'ruta de caravanas: La Meca ↔ Siria', font=F('semi', 30), fill=SEP, anchor='lm')
        for k, (a, b2) in enumerate([(MAP['Medina'], (440, 520)), (MAP['Medina'], (420, 760)), (MAP['Medina'], (470, 900))]):
            q = ctx.on(1, 2.0 + k * 0.8)
            if q: E.arrow(d, a, (a[0] + (b2[0] - a[0]) * q, a[1] + (b2[1] - a[1]) * q), RED, 7)
        if ctx.on(1, 5.0): card(d, 430, 1150, 560, ['Waddan · Buwat · al-\'Ushayra · Najla…', '(Ibn Ishaq, pp. 281-287)'], F('bold', 28), title='Expediciones contra caravanas', tfont=F('title', 30))
    narr(d, ctx, 200, 1510, 0.7, 'point')

def v_nakhla(d, im, ctx):
    night(d, 920); dunes(d, 920, 4, ctx.gt, (150, 132, 110))
    palm(d, 110, 920, 0.8, ctx.gt, 3); palm(d, 990, 920, 0.7, ctx.gt, 4)
    walk = ctx.gt * 0.6
    camel(d, 600, 960, 0.62, ctx.gt, 21, walk, face=-1, rider=ARAB((120, 80, 60), 'keffiyeh', None, 1))
    camel(d, 860, 975, 0.56, ctx.gt, 22, walk + 0.3, face=-1)
    for k in range(3):
        person(d, 110 + k * 120, 1040, 0.62, ARAB((90, 80, 70), 'keffiyeh', 'sword', k), 0, ctx.gt, 30 + k, pose='sword' if ctx.seg >= 1 else 'stand')
    if ctx.seg == 0:
        p = ctx.on(0, 3.0)
        if p:
            y = slide(p, 300)
            d.rectangle((280, y, 800, y + 210), fill=(246, 234, 200), outline=INK, width=4)
            d.text((540, y + 70), '«Id a Najla y acechad', font=F('hand', 44), fill=INK, anchor='mm'); d.text((540, y + 125), 'allí a Quraysh»', font=F('hand', 44), fill=INK, anchor='mm')
            d.ellipse((720, y + 150, 770, y + 200), fill=RED)
    if ctx.seg >= 1:
        scan(im, d, 'g_nakhla.jpg', 1070, 380, cap=GUI + '287', p=ctx.on(1, -0.2), z=zin(ctx, 1, -0.2))
    if ctx.seg >= 2 and ctx.on(2, 4.0):
        card(d, 70, slide(ctx.on(2, 4.0), 280), 940, ['«luchar en él es grave… pero la persecución', 'es peor que matar» (Corán 2:217)'], F('bold', 34), title='Mes sagrado', tfont=F('title', 32))

def v_badr(d, im, ctx):
    sky(d, (220, 206, 176), 920); dunes(d, 920, 6, ctx.gt)
    walk = ctx.gt * 0.5
    for k in range(3): camel(d, 560 + k * 170, 960 + k * 6, 0.5, ctx.gt, 40 + k, walk + k * 0.3, face=-1, rider=ARAB((140, 90, 60), 'keffiyeh', None, k) if k == 0 else None)
    d.text((760, 600), 'caravana de Abu Sufyán', font=F('hand', 42), fill=SEP, anchor='mm')
    if ctx.on(0, 4.0):
        for k in range(4): person(d, 70 + k * 100, 1040, 0.6, ARAB((200, 190, 160), 'turban', 'spear', k), 0, ctx.gt, 50 + k, walk=walk)
    if ctx.seg >= 1:
        scan(im, d, 'g_badr.jpg', 1080, 370, cap=GUI + '289', p=ctx.on(1, -0.2), z=zin(ctx, 1, -0.2))
    else:
        narr(d, ctx, 900, 1500, 0.8)
    if ctx.seg >= 2:
        stamp(d, 540, 330, 'Primero, la caravana', RED, 56)

def v_kab(d, im, ctx):
    night(d, 900)
    fortress(d, 620, 900, 380, 200, ctx.gt, 61)
    for k in range(3): person(d, 110 + k * 130, 900, 0.6, ARAB((70, 60, 54), 'keffiyeh', 'sword', k), 0, ctx.gt, 70 + k)
    if ctx.seg <= 1:
        scan(im, d, 'b4037.jpg', 960, 490, cap='Sahih al-Bujari 4037 (trad. Muhsin Khan)', p=ctx.on(0, 1.5), z=zin(ctx, 0, 1.5))
    elif ctx.seg == 2:
        scan(im, d, 'g_kab2.jpg', 990, 460, cap='Ibn Ishaq, Sira (trad. Guillaume 1955), pp. 368-369', p=ctx.on(2, -0.2), z=zin(ctx, 2, -0.2))
    else:
        scan(im, d, 'g_mecca.jpg', 990, 460, cap=GUI + '551', p=ctx.on(3, -0.2), z=zin(ctx, 3, -0.2))

def v_mustaliq(d, im, ctx):
    sky(d, (232, 196, 150), 900); dunes(d, 900, 8, ctx.gt)
    d.ellipse((380, 860, 700, 940), fill=(110, 150, 170), outline=INK, width=4)
    for k in range(3): camel(d, 420 + k * 140, 900, 0.42, ctx.gt, 80 + k, 0.0, face=1 if k % 2 else -1)
    tent(d, 880, 900, 0.7, ctx.gt, 85); tent(d, 160, 900, 0.6, ctx.gt, 86)
    if ctx.seg >= 1:
        scan(im, d, 'b2541.jpg', 970, 480, cap='Sahih al-Bujari 2541 (trad. Muhsin Khan)', p=ctx.on(1, -0.2), z=zin(ctx, 1, -0.2))
    else:
        narr(d, ctx, 900, 1500, 0.8)
    if ctx.seg >= 2 and ctx.on(2, 6.5):
        card(d, 70, slide(ctx.on(2, 6.5), 290), 940, ['«invitar [al islam] antes del combate', 'era en los primeros tiempos del islam»'], F('bold', 34), title='Sahih Muslim 1730 (Nafi\')', tfont=F('title', 30))

def v_qurayza(d, im, ctx):
    d.rectangle((0, 0, W, H), fill=(214, 200, 176))
    scan(im, d, 'g_qurayza.jpg', 300, 620, cap=GUI + '464', p=ctx.on(0, -0.3), z=zin(ctx, 0, 2.0))
    if ctx.seg >= 2:
        stamp(d, 540, 1010, '600-700 (algunos: 800-900)', RED, 52)
    if ctx.seg == 0:
        card(d, 70, 990, 940, ['Acusados de traición en la batalla de la Trinchera (627)', '— lo concedemos —'], F('bold', 32), align='c')
    narr(d, ctx)

def v_khaybar(d, im, ctx):
    sky(d, (244, 206, 160), 900)
    d.ellipse((440, 760, 640, 960), fill=(250, 196, 110))
    dunes(d, 900, 9, ctx.gt); fortress(d, 330, 880, 480, 230, ctx.gt, 91)
    for k in range(5): person(d, 70 + k * 80, 1030, 0.55, ARAB((170, 150, 120), 'helmet', 'spear', k), 0, ctx.gt, 95 + k, walk=ctx.gt * 0.5)
    if ctx.seg >= 1:
        scan(im, d, 'g_khaybar.jpg', 1060, 390, cap=GUI + '511', p=ctx.on(1, -0.2), z=zin(ctx, 1, -0.2))
    else:
        narr(d, ctx, 920, 1500, 0.8)
    if ctx.seg >= 2:
        card(d, 70, slide(ctx.on(2, 0.2), 280), 940, ['Criterio: ¿llamada a la oración?', 'No: si no eran musulmanes, atacaba.'], F('title', 40), align='c', tcolor=RED)

def v_tabuk(d, im, ctx):
    if ctx.seg == 0:
        hijaz(d, ctx.gt)
        p = ctx.on(0, 1.0); E.arrow(d, MAP['Medina'], (MAP['Medina'][0] + (MAP['Tabuk'][0] - MAP['Medina'][0]) * p, MAP['Medina'][1] + (MAP['Tabuk'][1] - MAP['Medina'][1]) * p), RED, 10)
        if p > 0.9:
            d.text((600, 540), '~700 km', font=F('title', 44), fill=RED, anchor='lm'); d.text((600, 590), '30.000 hombres', font=F('title', 40), fill=RED, anchor='lm')
            d.text((470, 282), '→ frontera bizantina', font=F('hand', 40), fill=RED, anchor='lm')
    else:
        d.rectangle((0, 0, W, H), fill=(218, 204, 178))
        if ctx.seg == 1:
            scan(im, d, 'w_q929.png', 300, 560, cap='Corán 9:29 (quran.com)', p=ctx.on(1, -0.2), z=zin(ctx, 1, -0.2) * 0.3, src=(0, 0, 1064, 620))
        else:
            scan(im, d, 'ik929.jpg', 290, 840, cap='Tafsir Ibn Kathir (abreviado, Darussalam), vol. 4', p=ctx.on(2, -0.2), z=zin(ctx, 2, -0.2))
    narr(d, ctx, 900, 1510, 0.8)

def v_hadith(d, im, ctx):
    d.rectangle((0, 0, W, H), fill=(222, 210, 186))
    if ctx.seg <= 1:
        scan(im, d, 'b25.jpg', 290, 780, cap='Sahih al-Bujari 25 (trad. Muhsin Khan)', p=ctx.on(0, 0.5), z=zin(ctx, 0, 1.0))
        person(d, 200, 1510, 0.8, SCHOLAR((90, 70, 50)), 0, ctx.gt, 110, pose='read')
    else:
        d.text((540, 320), 'Sahih Muslim 1731', font=F('title', 52), fill=SEP, anchor='mm')
        steps = [('1', 'Invítalos al islam', GREEN), ('2', 'Si no: exige el tributo (yizya)', GOLD), ('3', 'Si no: combátelos', RED)]
        for k, (n, t, c) in enumerate(steps):
            q = ctx.on(2, 2.5 + k * 2.6)
            if not q: continue
            y = slide(q, 410 + k * 200)
            rrect(d, (90, y, 990, y + 160), 26, (250, 242, 222), c, 6)
            d.ellipse((120, y + 30, 220, y + 130), fill=c); d.text((170, y + 82), n, font=F('title', 60), fill=(255, 255, 255), anchor='mm')
            d.text((260, y + 82), t, font=F('title', 44), fill=INK, anchor='lm')
        if ctx.seg >= 3: stamp(d, 540, 1080, 'No depende de que te ataquen', RED, 50)
    narr(d, ctx, 900, 1510, 0.8)

def v_sword(d, im, ctx):
    d.rectangle((0, 0, W, H), fill=(216, 206, 186))
    if ctx.seg == 0:
        scan(im, d, 'w_q95.png', 280, 430, cap='Corán 9:5 (quran.com)', p=ctx.on(0, -0.2), z=zin(ctx, 0, -0.2) * 0.3, src=(0, 0, 1064, 620))
        if ctx.on(0, 5.0): scan(im, d, 'ik95b.jpg', 770, 400, cap='Ibn Kathir: «el versículo de la espada»', p=ctx.on(0, 5.0), z=zin(ctx, 0, 5.0))
    elif ctx.seg == 1:
        scan(im, d, 'ik95.jpg', 290, 780, cap='Tafsir Ibn Kathir (Darussalam), vol. 4', p=ctx.on(1, -0.2), z=zin(ctx, 1, -0.2))
    else:
        scan(im, d, 'w_qurtubi_2193.png', 290, 600, cap='al-Qurtubi, tafsir de 2:193 (quran.com)', p=ctx.on(2, -0.2), z=zin(ctx, 2, -0.2) * 0.35, src=(0, 280, 1064, 760))
        if ctx.on(2, 6.0): card(d, 70, slide(ctx.on(2, 6.0), 950), 940, ['«la causa del combate es la incredulidad»', '(al-Yami\' li-ahkam al-Qur\'an)'], F('title', 40), align='c', tcolor=RED)
    narr(d, ctx, 900, 1510, 0.8)

def v_fiqh(d, im, ctx):
    d.rectangle((0, 0, W, H), fill=(220, 208, 184))
    person(d, 200, 1510, 0.8, SCHOLAR((60, 80, 110)), 0, ctx.gt, 120, pose='read')
    if ctx.seg <= 1:
        y = scan(im, d, 'rel98.jpg', 290, 480, cap="Reliance of the Traveller, o9.8", p=ctx.on(0, 1.0), z=zin(ctx, 0, 1.0))
        if ctx.seg == 1 and ctx.on(1, 5.5): scan(im, d, 'rel99.jpg', 820, 330, cap='o9.9', p=ctx.on(1, 5.5), z=zin(ctx, 1, 5.5))
    else:
        card(d, 90, slide(ctx.on(2, 0.2), 340), 900, ['«lo mínimo: una vez cada año»'], F('title', 44), title='Ibn Qudama, al-Mughni (hanbalí)', tfont=F('title', 32), align='c')
        if ctx.on(2, 4.0): card(d, 90, slide(ctx.on(2, 4.0), 620), 900, ['«los juristas están de acuerdo en que', 'se combate a todos los politeístas»'], F('bold', 38), title='Ibn Rushd, Bidayat al-muytahid (maliki)', tfont=F('title', 32), align='c')
    narr(d, ctx, 900, 1510, 0.8)

def v_counter(d, im, ctx):
    d.rectangle((0, 0, W, H), fill=(226, 214, 190))
    if ctx.seg == 0:
        E.bubble(d, 300, 520, 700, '«Combatid a los que os combaten, y no os excedáis» (2:190)', font=F('hand', 48), tail=(250, 1050))
        defe(d, ctx)
    elif ctx.seg == 1:
        card(d, 70, slide(ctx.on(1, 0.2), 300), 940, ['2:190 · 22:39 → defensa', 'Ibn Kathir: no matar mujeres, niños, ancianos ni monjes'], F('bold', 36), title='Lo que hay que reconocer', tcolor=GREEN, tfont=F('title', 34))
        defe(d, ctx); E.check(d, 560, 820, 2.0, GREEN)
    elif ctx.seg == 2:
        for k, (t, c) in enumerate([('9:5 «versículo de la espada»', RED), ('9:29 judíos y cristianos', RED), ('Najla · Badr · Mustaliq', SEP), ('Jaybar · Tabuk', SEP)]):
            q = ctx.on(2, 1.0 + k * 2.5)
            if q: pill(d, 540, slide(q, 360 + k * 110), t, c, F('title', 40))
    elif ctx.seg == 3:
        scan(im, d, 'watt231.jpg', 280, 820, cap='W. M. Watt, Muhammad at Medina (Oxford 1956), p. 231', p=ctx.on(3, -0.2), z=zin(ctx, 3, 1.0))
    else:
        d.text((540, 400), 'Ibn Sa\'d, Tabaqat', font=F('title', 50), fill=SEP, anchor='mm')
        for k, (n, t) in enumerate([('27', 'expediciones dirigidas por él'), ('47', 'expediciones enviadas')]):
            q = ctx.on(4, 0.5 + k * 1.5)
            if q:
                y = slide(q, 560 + k * 220)
                d.text((250, y), n, font=F('title', 150), fill=RED, anchor='mm'); d.text((370, y), t, font=F('bold', 40), fill=INK, anchor='lm')
        if ctx.on(4, 4.0): stamp(d, 540, 1040, '¿Todas en defensa propia?', RED, 56)
    narr(d, ctx, 870, 1510, 0.8)

JESUS = dict(skin=SKIN[1], robe=(236, 230, 214), head='none', hair=(70, 48, 30), beard='short', beardcol=(70, 48, 30), cape=(150, 40, 40))
PETER = dict(skin=SKIN[0], robe=(110, 90, 60), head='none', hair=(120, 120, 120), beard='full', beardcol=(140, 136, 130), prop='sword')
def v_jesus(d, im, ctx):
    sky(d, (206, 214, 222), 900); dunes(d, 900, 12, ctx.gt, (196, 186, 150))
    palm(d, 100, 900, 0.8, ctx.gt, 13)
    person(d, 380, 1260, 1.0, JESUS, 0, ctx.gt, 130, pose='point' if ctx.seg >= 1 else 'stand', face=1)
    person(d, 700, 1260, 0.95, PETER, 0, ctx.gt, 131, pose='sword' if ctx.seg == 0 else 'stand', face=-1)
    lines = [('Mateo 26:52', '«Vuelve tu espada a su sitio»'), ('Juan 18:36', '«Mi reino no es de este mundo»'), ('Lucas 9:55-56', '«no ha venido a destruir vidas, sino a salvarlas»')]
    for k, (r, t) in enumerate(lines):
        q = ctx.on(1 if k == 0 else 2, 0.2 if k < 2 else 6.0)
        if q: card(d, 70, slide(q, 260 + k * 150), 940, [t], F('hand', 42), title=r, tfont=F('title', 30), tcolor=BLUE)
    narr(d, ctx, 940, 1510, 0.7)

def v_end(d, im, ctx):
    d.rectangle((0, 0, W, H), fill=(226, 216, 194))
    items = ['Las primeras expediciones: contra caravanas', 'Ataques por sorpresa: Mustaliq, Jaybar', 'Corán y hadices: combatir hasta el islam o la yizya', 'Comentaristas y juristas clásicos: igual']
    for k, t in enumerate(items):
        p = ctx.on(0 if k < 2 else 1, 0.3 + (k % 2) * 3.0)
        if not p: continue
        y = slide(p, 310 + k * 160)
        rrect(d, (70, y, 1010, y + 136), 24, (250, 242, 222), GREEN, 5); E.check(d, 135, y + 68, 1.1, GREEN)
        ls = wrap(d, t, F('bold', 40), 780)
        for j, l in enumerate(ls): d.text((200, y + 68 + (j - (len(ls) - 1) / 2) * 46), l, font=F('bold', 40), fill=INK, anchor='lm')
    if ctx.seg >= 2:
        pill(d, 540, 1000, 'Respeto a los musulmanes · rigor con las fuentes', BLUE, F('bold', 34))
    narr(d, ctx, 540, 1510, 0.9, 'raise' if ctx.seg == 2 else None)

VIS = dict(hook=v_hook, medina=v_medina, nakhla=v_nakhla, badr=v_badr, kab=v_kab, mustaliq=v_mustaliq, qurayza=v_qurayza, khaybar=v_khaybar, tabuk=v_tabuk,
           hadith=v_hadith, sword=v_sword, fiqh=v_fiqh, counter=v_counter, jesus=v_jesus, end=v_end)
SPK = dict(N=BLUE, D=GREEN, F=RED)
SPK_TAG = dict(N=None, D='Objeción', F='Fuente')

def header(d, sc, ctx):
    p = ease(ctx.lt / 0.5); f = F('title', 62 if len(sc['title']) < 28 else 52)
    y = 170 - (1 - p) * 80
    for l in wrap(d, sc['title'], f, 920):
        tw = d.textlength(l, font=f)
        d.rounded_rectangle((540 - tw / 2 - 28, y - f.size * 0.62, 540 + tw / 2 + 28, y + f.size * 0.62), 14, fill=(46, 32, 22))
        d.text((540, y + 4), l, font=f, fill=(246, 234, 206), anchor='mm'); y += f.size * 1.3
    lab = f"{sc['i'] + 1}/{len(SCENES)}"; f2 = F('bold', 28)
    d.rounded_rectangle((44, 80, 60 + d.textlength(lab, font=f2) + 16, 122), 10, fill=(46, 32, 22)); d.text((60, 101), lab, font=f2, fill=(246, 234, 206), anchor='lm')

def captions(d, sc, ctx):
    if ctx.seg < 0: return
    g = sc['segs'][ctx.seg]; st = ctx.st
    if st > g['dur'] + 0.2 or st < -0.05: return
    cur = None
    for ch in chunks(g['words']):
        if st >= ch[0][0] - 0.05: cur = ch
    if cur is None or st > cur[-1][0] + cur[-1][1] + 0.6: return
    f = F('title', 56); lines = wrap(d, ' '.join(w[2] for w in cur), f, 860); lh = 68; h = len(lines) * lh + 30
    y0 = 1680 - h
    d.rounded_rectangle((70, y0, 1010, y0 + h), 24, fill=(252, 246, 232), outline=SPK[g['spk']], width=6)
    if SPK_TAG[g['spk']]:
        E.pill(d, 160, y0 - 4, SPK_TAG[g['spk']], SPK[g['spk']], F('bold', 26))
    idx = 0
    for i, w in enumerate(cur):
        if st >= w[0] - 0.02: idx = i
    k = 0; yy = y0 + 15 + lh / 2
    for l in lines:
        x = 540 - d.textlength(l, font=f) / 2
        for w in l.split():
            d.text((x, yy + 3), w, font=f, fill=SPK[g['spk']] if k == idx else INK, anchor='lm'); x += d.textlength(w + ' ', font=f); k += 1
        yy += lh

PAPER_IMG = None
def frame(T, gt):
    global PAPER_IMG
    if PAPER_IMG is None: PAPER_IMG = paper(3)
    sc = T[-1]
    for s in T:
        if s['start'] <= gt < s['end']: sc = s
    lt = gt - sc['start']
    im = PAPER_IMG.copy(); set_canvas(im); d = ImageDraw.Draw(im)
    ctx = Ctx(sc, lt, gt)
    VIS[sc['vis']](d, im, ctx)
    # textura de papel encima (suave) para unificar el dibujo
    header(d, sc, ctx); captions(d, sc, ctx)
    fade = min(lt / 0.25, (sc['end'] - gt) / 0.25, 1.0)
    if fade < 1: im = Image.blend(Image.new('RGB', (W, H), (240, 229, 204)), im, max(0.0, fade))
    return im

def mix_audio(T, total, sr=48000):
    out = np.zeros(int((total + 1) * sr), dtype=np.float32)
    for sc in T:
        for g in sc['segs']:
            a, _ = wav_info(f"{B}/audh/{g['key']}.wav"); i = int(g['t0'] * sr); out[i:i + len(a)] += a
    w = wave.open(f'{B}/out/voz.wav', 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes((np.clip(out * 0.95, -1, 1) * 32767).astype(np.int16).tobytes()); w.close()

def render_part(args):
    k, n, total = args
    T, _ = build_timeline(); nf = int(total * FPS); a = nf * k // n; b = nf * (k + 1) // n
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', f'{B}/out/part{k}.mp4'], stdin=subprocess.PIPE)
    for fi in range(a, b): p.stdin.write(frame(T, fi / FPS).tobytes())
    p.stdin.close(); p.wait(); return k

if __name__ == '__main__':
    os.makedirs(B + '/out', exist_ok=True)
    T, total = build_timeline()
    print('duración', round(total, 1), 's =', round(total / 60, 2), 'min')
    if len(sys.argv) > 1 and sys.argv[1] == 'preview':
        for t in map(float, sys.argv[2:]): frame(T, t).save(f'{B}/out/prev_{t:07.2f}.png')
        for s in T: print(s['i'], s['id'], round(s['start'], 1), [round(g['t0'] - s['start'], 1) for g in s['segs']])
        sys.exit()
    mix_audio(T, total)
    from multiprocessing import Pool
    n = 4
    with Pool(n) as pool: list(pool.imap_unordered(render_part, [(k, n, total) for k in range(n)]))
    open(f'{B}/out/list.txt', 'w').write(''.join(f"file 'part{k}.mp4'\n" for k in range(n)))
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', f'{B}/out/list.txt', '-i', f'{B}/out/voz.wav',
                    '-c:v', 'copy', '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-ar', '48000', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', f'{B}/out/yihad_tiktok.mp4'], check=True)
    print('ok')
