# -*- coding: utf-8 -*-
"""«El error coránico de los mandeos» — estilo 2. Reutiliza la línea de tiempo, los recortes y el audio de render3.py."""
import os, sys, math, subprocess
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT + '/componentes'); sys.path.insert(0, ROOT + '/escenas')
import paper as P
P.B = ROOT + '/assets'                      # paper.py busca las fuentes en {P.B}/fonts
import render3 as R
from render3 import *
import style2 as S2
from style2 import TEAL, GOLDK, REDK, INK2, tag2, card2, premise, bg2, waves, nearmap, NEARPT, staff, bowl, amulet, scrollbig, reeds
import guion_datos as script5
B = ROOT + '/audio'                         # audh/ (voz) y out/ (mezcla y partes) viven aquí
R.GAP = 0.24; R.LEAD = 0.26; R.SCENES = script5.SCENES; R.VOICE = script5.VOICE; R.clean = script5.clean; R.B = B
R.PG = ROOT + '/assets/paginas'; R.PGH = ROOT + '/assets/paginas'
R.figure = S2.figure; R.draw_fig = S2.draw_fig
OUT = 'mandeos'

# ------------------------------------------------------------------ reparto
NAR = dict(coat=(54, 70, 96), tunic=(236, 232, 222), head='hair', hair=(52, 40, 32), skin=0, glasses=True, beard=None)
PRIEST = dict(coat=(242, 240, 232), tunic=(242, 240, 232), head='mandaean', headcol=(246, 244, 238), beard=(150, 140, 128), skin=1, stole=(212, 222, 206))
MAND = lambda k=0: dict(coat=(240, 238, 230), tunic=(240, 238, 230), head='kufi', headcol=(246, 244, 238), skin=k % 4, beard=[(60, 46, 36), None, (120, 110, 100)][k % 3])
JOHN = dict(coat=(170, 140, 96), tunic=(236, 230, 214), head='long', hair=(70, 50, 34), beard=(70, 50, 34), skin=2)
JESUS = dict(coat=(162, 48, 48), tunic=(240, 236, 226), head='long', hair=(96, 64, 42), beard=(96, 64, 42), skin=1)
IKS = dict(coat=(52, 104, 82), tunic=(236, 232, 222), head='turban', beard=(206, 202, 196), skin=3, trim=(214, 176, 96))
TAB = dict(coat=(120, 84, 56), tunic=(236, 232, 222), head='turban', beard=(90, 80, 72), skin=2, trim=(214, 176, 96))
OBJ = dict(coat=(96, 104, 112), tunic=(240, 238, 230), head='kufi', headcol=(244, 242, 236), beard=(52, 42, 34), skin=2)
ACAD = lambda k=0: dict(coat=[(60, 64, 76), (110, 70, 64), (70, 96, 90)][k % 3], tunic=(236, 236, 232), head='hair', hair=[(60, 48, 40), (160, 150, 140), (40, 36, 32)][k % 3], skin=[3, 0, 1][k % 3], glasses=k % 2 == 0)

_ILL = {}
def ill(st):
    if 'i' not in _ILL: _ILL['i'] = tag2('ILUSTRACIÓN · RECREACIÓN', 30, bg=(20, 20, 22), accent=(190, 150, 80))
    put(st, _ILL['i'], 230, 70)
def fig2(st, c, spec, x, y, s=1.0, talk=False, **kw):
    S2.draw_fig(st, S2.figure(**spec), x, y, s, talk=(c.seg['kind'] == 'N' and c.t < c.seg['dur'] and talk), t=c.gt, seed=int(x) % 7, **kw)
def conc2(st, text, x, y, p, size=46):
    if p <= 0: return
    sp = tag2(text, size, accent=TEAL); pop(st, sp, x, y, p, rot=-1); pop(st, check(84), x - sp.im.width / 2 + 10, y - 2, clamp(p * 1.2 - .2))
def red2(text, size=50): return tag2(text, size, bg=(120, 30, 36), accent=(250, 120, 110))
def gold2(text, size=50): return tag2(text, size, bg=(40, 36, 30), accent=GOLDK)
def baptism(st, c, x, y, s, spec=MAND(0), talk=False, dip=0.0):
    """figura metida en el agua hasta la cintura"""
    tmp = Image.new('RGBA', (W, SH), (0, 0, 0, 0))
    S2.draw_fig(tmp, S2.figure(**spec), x, y + dip * 120 * s, s, aL=30, aR=30, t=c.gt, seed=3)
    cut = int(y - 230 * s); m = tmp.getchannel('A').point(lambda v: v); ImageDraw.Draw(m).rectangle((0, cut, W, SH), fill=0)
    st.paste(tmp, (0, 0), m)
    d = ImageDraw.Draw(st, 'RGBA'); d.ellipse((x - 150 * s, cut - 14, x + 150 * s, cut + 22), outline=(230, 244, 244, 160), width=4)

# ------------------------------------------------------------------ escenas
def s_hook(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg2('river').copy(); waves(st, t, 820)
        put(st, reeds(1), 120, 900, 1.0); put(st, reeds(2), 980, 880, 0.9)
        fig2(st, c, PRIEST, 360, 1150, 0.82, aR=40, aL=60)
        put(st, staff(), 230, 1000, 1.0)
        baptism(st, c, 700, 1240, 0.85, MAND(1), dip=max(0, math.sin(t * 1.1)) * 0.6)
        waves(st, t + 0.5, 1150, SH, 1.4)
        ill(st)
        conc2(st, 'VENERAN A JUAN EL BAUTISTA', 560, 180, c.at('Juan', -0.2, .4), 50)
        pop(st, red2('RECHAZAN A JESÚS COMO MESÍAS', 48), 560, 300, c.at('rechaza', -0.2, .35), rot=1)
        pop(st, gold2('¿LOS SABEOS DEL CORÁN?', 54), 560, 430, c.at('sabeos', -0.2, .35), rot=-1)
    elif k == 1:
        st = bg2('court').copy()
        pop(st, card2('CORÁN 5:69', 'PROMESA DE SALVACIÓN A LOS SABEOS', 880, TEAL, fs=48), 540, 380, c.at('salvación', -0.3, .4), rot=-1.5)
        pop(st, card2('CORÁN 4:150-151', 'CONDENA AL QUE ACEPTA A UNOS MENSAJEROS Y RECHAZA A OTROS', 880, REDK, fs=48), 540, 760, c.at('condena', -0.3, .4), rot=1.5)
        pop(st, bigword('VS', 200, GOLDK), 540, 1170, c.at('condena', 0.4, .4))
    else:
        st = bg2('court').copy(); g = c.at('salva', -0.2, .5)
        balance(st, 540, 1380, 1.0, lerp(0, 9, ease(c.at('condena', -0.3, .5))) + 2 * math.sin(t * 2), left=[(tag2('PROMESA', 40, accent=TEAL), g)], right=[(red2('CONDENA', 40), c.at('condena', -0.3, .4))])
        conc2(st, 'ACEPTA A JUAN', 300, 200, c.at('Juan', -0.2, .4), 46); pop(st, red2('RECHAZA A JESÚS', 46), 780, 200, c.at('Jesús', -0.2, .35))
        pop(st, bigword('¿SALVADOS O CONDENADOS?', 92, GOLDK), 540, 420, c.at('Se', -0.2, .4), rot=-2)
        pop(st, tag2('CON SUS PROPIOS TEXTOS', 50), 540, 580, c.at('textos', -0.3, .35))
    return st

def s_who(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg2('river').copy(); waves(st, t, 820)
        put(st, reeds(3), 140, 900, 1.0)
        for i in range(3): baptism(st, c, 300 + i * 250, 1230 + (i % 2) * 30, 0.7, MAND(i), dip=max(0, math.sin(t * 1.2 + i)) * 0.5)
        waves(st, t + 0.3, 1100, SH, 1.4)
        ill(st)
        pop(st, tag2('LOS MANDEOS', 80), 540, 170, c.p(0.0, .35), rot=-1.5)
        pop(st, tag2('SUR DE IRAK · SUROESTE DE IRÁN', 44), 540, 300, c.at('Irak', -0.3, .35))
        pop(st, gold2('AGUA CORRIENTE = «JORDÁN»', 54), 540, 440, c.at('corriente', -0.2, .35), rot=1)
    elif k == 1:
        st = bg2('study').copy()
        drop(st, book('GINZA|«EL TESORO»', (110, 70, 54), 260, 340, 42), 290, 980, c.at('Ginza', -0.3, .5), rot=-3, s=1.25)
        drop(st, book('LIBRO|DE JUAN', (54, 86, 110), 260, 340, 42), 760, 980, c.at('Libro', -0.3, .5), rot=3, s=1.25)
        pop(st, tag2('LENGUA: MANDEO (ARAMEO ORIENTAL)', 46), 540, 210, c.at('mandeo', -0.3, .35))
        pop(st, gold2('DIOS SUPREMO: LA GRAN VIDA', 50), 540, 340, c.at('Vida', -0.3, .35))
    elif k == 2:
        st = bg2('study').copy()
        drop(st, bowl(320, 1), 280, 360, c.at('cuencos', -0.3, .5), rot=-4); drop(st, amulet(), 800, 360, c.at('amuletos', -0.3, .5), rot=5)
        pop(st, tag2('CUENCOS DE CONJUROS', 40), 280, 520, c.at('cuencos', 0.1, .35)); pop(st, tag2('AMULETOS DE PLOMO', 40), 800, 520, c.at('amuletos', 0.1, .35))
        docdrop(st, c, 'w_ir_preislam.png', 540, 900, 900, 420, c.w('prueban') - 0.4, rot=-1.5)
        pop(st, gold2('SIGLOS III-IV', 70), 540, 1300, c.at('siglos', -0.2, .35), rot=-2)
    else:
        st = bg2('map').copy(); pm = c.p(-0.2, .5)
        put(st, nearmap(), 540, 560 + (1 - eout(pm)) * 60, 1.0, 0, min(1, pm * 3))
        mx, my = 540 - 455, 560 - 415
        J = (mx + NEARPT['Jerusalem'][0], my + NEARPT['Jerusalem'][1]); M = (mx + NEARPT['SurIrak'][0], my + NEARPT['SurIrak'][1])
        q = c.at('discípulos', -0.2, 1.0)
        if q > 0: dash(st, J, (J[0] + (M[0] - J[0]) * q, J[1] + (M[1] - J[1]) * q), GOLDK, 8)
        pop(st, red2('¿DE PALESTINA? HIPÓTESIS', 50), 540, 1060, c.at('hipótesis', -0.2, .35), rot=-1.5)
        pop(st, tag2('LUPIERI: MESOPOTAMIA, S. II, GNOSTICISMO POSCRISTIANO', 36), 540, 1180, c.at('Lupieri', -0.2, .35), rot=1)
        docdrop(st, c, 'w_ir_origin.png', 540, 1340, 860, 220, c.w('Mesopotamia', 0) + 0.6, rot=-1, zmax=1.0) if c.at('posterior', -0.2, .1) > 0 else None
    return st

def s_promise(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg2('study').copy(); pop(st, tag2('AL-SABI\'UN', 90), 540, 300, c.p(0.0, .35), rot=-1.5)
        for i, v in enumerate(('2:62', '5:69', '22:17')): pop(st, gold2('CORÁN ' + v, 56), 540, 560 + i * 140, c.at('veces', -0.4 + i * 0.25, .35), rot=(-2, 1, -1)[i])
        pop(st, bigword('×3', 160, GOLDK), 880, 300, c.at('tres', -0.1, .4), rot=6)
    elif k == 1:
        st = bg2('study').copy(); qshot(st, c, 'w_q262.png', zmax=0.55, who=NAR)
    elif k == 2:
        st = bg2('study').copy(); docdrop(st, c, 'w_q569.png', 540, 420, 860, 460, -0.1, rot=-1.2, zmax=0.6)
        for i, (wd, tx) in enumerate((('Creer', 'CREER EN DIOS'), ('Último', 'CREER EN EL ÚLTIMO DÍA'), ('obrar', 'OBRAR EL BIEN'))):
            pop(st, premise(i + 1, tx, 860, TEAL, 52), 540, 820 + i * 170, c.at(wd, -0.2, .4, nth=1 if wd == 'Creer' else 0) if wd != 'Creer' else c.at('Creer', -0.2, .4), rot=(-1, 1, -1)[i])
    elif k == 3:
        st = bg2('study').copy()
        pop(st, card2('TRADUCCIÓN SAHEEH INTERNATIONAL (2:62)', '«…JEWS OR CHRISTIANS OR SABEANS [BEFORE PROPHET MUHAMMAD] - THOSE [AMONG THEM] WHO BELIEVED…»', 900, (90, 96, 110), fs=44), 540, 400, c.p(0.0, .4), rot=-1)
        q = c.at('corchetes', -0.1, .4)
        if q > 0: d = ImageDraw.Draw(st); d.rounded_rectangle((90, 430, 990, 560), 14, outline=GOLDK, width=int(6 * q))
        pop(st, red2('NO ESTÁ EN EL ÁRABE', 70), 540, 760, c.at('están', -0.2, .35), rot=-2)
        pop(st, tag2('ES INTERPRETACIÓN DEL TRADUCTOR', 50), 540, 900, c.at('interpretación', -0.2, .35), rot=1)
    else:
        st = bg2('study').copy(); docdrop(st, c, 'w_q2217.png', 540, 560, 880, 560, -0.1, rot=-1.2, zmax=0.6)
        pop(st, tag2('NO PROMETE: DIOS JUZGARÁ', 50), 540, 1000, c.at('juzgará', -0.2, .35), rot=-1)
        pop(st, gold2('PERO SON UNA COMUNIDAD DISTINTA', 54), 540, 1140, c.at('comunidad', -0.3, .35), rot=1)
    return st

def s_identity(c):
    k, t = c.k, c.t
    st = bg2('study').copy()
    if k == 0:
        docdrop(st, c, 'w_ik262_sab.png', 480, 680, 820, 620, 0.0, rot=-1.5, zmax=0.8)
        fig2(st, c, IKS, 900, 1420, 0.78, aL=80 + 5 * math.sin(t * 2))
        pop(st, tag2('IBN KATHIR · S. XIV', 46), 300, 230, c.p(0.1, .35), rot=-2)
        pop(st, gold2('«HAY DIFERENCIA DE OPINIÓN»', 52), 420, 1230, c.at('diferencia', -0.2, .35), rot=1)
    elif k == 1:
        fig2(st, c, ACAD(0), lerp(1400, 780, eout(c.p(-0.1, .6))), 1360, 0.85, aL=40, talk=False)
        drop(st, book('ARAM|PERIODICAL|11 (1999)', (120, 50, 50), 250, 330, 40), 330, 1060, c.at('Gündüz', -0.2, .5), rot=-3, s=1.3)
        pop(st, tag2('ŞINASI GÜNDÜZ', 70), 540, 260, c.at('Gündüz', -0.1, .35), rot=-1.5)
        pop(st, gold2('ESPECIALISTA EN LOS MANDEOS', 46), 540, 400, c.at('especialistas', -0.2, .35), rot=1)
    elif k == 2:
        qshot(st, c, 'w_gunduz.png', zmax=1.0, who=ACAD(0))
    elif k == 3:
        docdrop(st, c, 'w_ir_sabians.png', 540, 820, 880, 500, c.w('Iranica') - 0.4, rot=-1.2)
        pop(st, red2('DESDE LOS ABASÍES: CONFUNDIDOS CON HARRÁN', 42), 540, 260, c.at('Harrán', -0.3, .35), rot=-1.5)
        conc2(st, 'TOLERADOS COMO «GENTE DEL LIBRO»', 540, 1240, c.at('tolerados', -0.2, .4), 46)
    else:
        docdrop(st, c, 'w_kulinich.png', 540, 700, 900, 640, -0.1, rot=-1.2)
        pop(st, red2('NO ES CONSENSO UNIVERSAL', 60), 540, 230, c.p(0.1, .35), rot=-2)
        pop(st, gold2('DE SU IDENTIDAD DEPENDE LA SALVACIÓN', 46), 540, 1180, c.at('salvación', -0.3, .35), rot=1)
    return st

def s_exeg(c):
    k, t = c.k, c.t; st = bg2('study').copy()
    if k == 0:
        pop(st, tag2('3 MENCIONES · 0 EXPLICACIONES', 60), 540, 200, c.at('menciona', -0.3, .35), rot=-1.5)
        for i, (wd, tx, col) in enumerate((('Muyahid', 'SIN RELIGIÓN', REDK), ('ángeles', 'ADORAN A LOS ÁNGELES', GOLDK), ('Salmos', 'LEEN LOS SALMOS', TEAL), ('profeta', 'SIN LIBRO NI PROFETA', REDK))):
            pop(st, tag2(tx, 52, accent=col), 540, 420 + i * 150, c.at('distintas', -0.4 + i * 0.25, .35), rot=(-2, 1.5, -1, 2)[i])
        fig2(st, c, TAB, 900, 1420, 0.72, aL=30)
    elif k == 1:
        docdrop(st, c, 'w_tab_mujahid_zayd.png', 540, 640, 900, 640, -0.1, rot=-1.2, zmax=0.8)
        pop(st, tag2('MUYAHID: «NO TIENEN RELIGIÓN»', 46), 540, 1080, c.at('religión', -0.2, .35), rot=-1)
        pop(st, red2('IBN ZAYD: «NI LIBRO NI PROFETA»', 46), 540, 1210, c.at('profeta', -0.2, .35), rot=1)
    elif k == 2:
        docdrop(st, c, 'w_tab262.png', 540, 480, 880, 460, -0.1, rot=-1.2, zmax=0.9)
        docdrop(st, c, 'b344.jpg', 540, 1050, 860, 420, c.w('Bujari') - 0.3, rot=1.2)
        pop(st, gold2('QATADA: ÁNGELES Y SALMOS', 46), 540, 830, c.at('Qatada', -0.2, .35), rot=-1)
    elif k == 3:
        docdrop(st, c, 'b344.jpg', 540, 620, 900, 520, -0.1, rot=-1.2)
        pop(st, red2('NO LO DICE MAHOMA', 64), 540, 1050, c.at('Mahoma', -0.3, .35), rot=-2)
        pop(st, tag2('COMENTARIO DE AL-BUJARI, CITANDO A ABU AL-ALIYA', 40), 540, 1190, c.at('comentario', -0.2, .35), rot=1)
    else:
        docdrop(st, c, 'w_ir_lit.png', 540, 520, 900, 480, -0.1, rot=-1.2)
        fig2(st, c, PRIEST, 220, 1420, 0.78, aR=30); put(st, staff(), 100, 1270, 0.9)
        conc2(st, 'SACERDOTES · LITURGIA · LIBROS', 620, 900, c.at('sacerdotes', -0.2, .4), 44)
        pop(st, tag2('ERROR DE LOS COMENTARISTAS ≠ ERROR DEL CORÁN', 38, accent=GOLDK), 620, 1060, c.at('demuestra', -0.3, .35), rot=1)
    return st

def s_jesus(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg2('study').copy(); docdrop(st, c, 'w_q345.png', 480, 640, 820, 560, -0.1, rot=-1.2, zmax=0.7)
        fig2(st, c, JESUS, 900, 1420, 0.78, aL=20)
        pop(st, gold2('AL-MASIH · EL MESÍAS', 64), 440, 1180, c.at('Mesías', -0.2, .35), rot=-2)
    elif k == 1:
        st = bg2('garden').copy(); docdrop(st, c, 'w_q685.png', 540, 380, 880, 420, -0.1, rot=-1.2, zmax=0.7)
        fig2(st, c, JOHN, 340, 1360, 0.85, aR=30); fig2(st, c, JESUS, 740, 1360, 0.85, aL=30); ill(st)
        conc2(st, 'JUAN', 340, 860, c.at('Juan', -0.2, .4), 54); conc2(st, 'JESÚS', 740, 860, c.at('Jesús', -0.2, .4), 54)
        pop(st, tag2('4:171 · «MENSAJERO DE DIOS»', 46), 540, 720, c.at('mensajero', -0.2, .35))
    elif k == 2:
        st = bg2('river').copy(); waves(st, t, 820); put(st, reeds(4), 980, 880, 0.9)
        baptism(st, c, 330, 1230, 0.85, JOHN)
        g = c.at('Jesús', -0.3, 1.2); fig2(st, c, JESUS, lerp(1300, 760, eout(g)), 1180, 0.8, aL=20 + 40 * ease(c.at('pide', -0.2, .4)))
        waves(st, t + .4, 1150, SH, 1.4)
        ill(st)
        pop(st, tag2('LIBRO DE JUAN MANDEO, § 30', 52), 540, 200, c.p(0.0, .35), rot=-1.5)
        pop(st, gold2('«JUAN, BAUTÍZAME»', 56), 700, 340, c.at('pide', -0.1, .35), rot=1)
    elif k == 3:
        st = bg2('study').copy(); qshot(st, c, 'mead50.jpg', zmax=1.0, who=JOHN)
    elif k == 4:
        st = bg2('study').copy(); docdrop(st, c, 'mead51.jpg', 540, 640, 900, 560, -0.1, rot=-1.2)
        pop(st, red2('«BAUTIZA AL ENGAÑADOR»', 66), 540, 1080, c.at('engañador', -0.2, .35), rot=-2)
        drop(st, scrollbig('CARTA'), 540, 1290, c.at('carta', -0.3, .5), rot=3, s=0.7)
    elif k == 5:
        st = bg2('study').copy(); docdrop(st, c, 'ginza52.jpg', 540, 640, 900, 560, -0.1, rot=-1.2)
        pop(st, red2('«EL MENTIROSO JESÚS»', 66), 400, 1080, c.at('mentiroso', -0.2, .35), rot=-2)
        pop(st, tag2('«EL CRISTO ROMANO»', 54), 640, 1220, c.at('romano', -0.2, .35), rot=1)
    elif k == 6:
        st = bg2('study').copy(); docdrop(st, c, 'ginza_ahmat.jpg', 540, 600, 900, 520, -0.1, rot=-1.2)
        pop(st, gold2('«AHMAT, HIJO DE BIZBAT» = MAHOMA', 50), 540, 1000, c.at('Mahoma', -0.4, .35), rot=-1.5)
        conc2(st, 'EDITADOS EN ÉPOCA ISLÁMICA (AL MENOS EN PARTE)', 540, 1140, c.at('editaron', -0.2, .4), 38)
    else:
        st = bg2('study').copy(); docdrop(st, c, 'w_ir_jesus.png', 540, 600, 900, 520, -0.1, rot=-1.2)
        fig2(st, c, ACAD(1), 900, 1420, 0.7, aL=60)
        pop(st, tag2('KURT RUDOLPH (IRANICA)', 48), 400, 200, c.p(0.1, .35), rot=-2)
        pop(st, red2('¿ANTERIOR AL SIGLO VII? NO DEMOSTRABLE', 44), 440, 1080, c.at('demostrar', -0.3, .35), rot=1)
    return st

def s_condemn(c):
    k, t = c.k, c.t; st = bg2('court').copy()
    if k == 0:
        pop(st, card2('CORÁN 4:150-151', 'LA CONDENA', 820, REDK, fs=70), 540, 560, c.p(0.0, .4), rot=-1.5)
    elif k == 1:
        qshot(st, c, 'w_q4150.png', zmax=0.6)
        pop(st, red2('«LOS VERDADEROS INCRÉDULOS»', 52), 520, 1330, c.at('verdaderos', -0.2, .35), rot=-2)
    elif k == 2:
        docdrop(st, c, 'w_q4152.png', 540, 520, 880, 520, -0.1, rot=-1.2, zmax=0.7)
        conc2(st, '4:152 · SIN HACER DISTINCIÓN', 540, 980, c.at('distinción', -0.2, .4), 50)
        pop(st, tag2('2:285 · «NO HACEMOS DISTINCIÓN»', 50), 540, 1120, c.at('doscientos', -0.2, .35), rot=1)
    elif k == 3:
        docdrop(st, c, 'w_ik4150.png', 480, 640, 820, 640, -0.1, rot=-1.2, zmax=0.8)
        fig2(st, c, IKS, 900, 1420, 0.78, aL=80 + 5 * math.sin(t * 2))
        pop(st, red2('RECHAZAR A UNO = RECHAZAR A TODOS', 46), 420, 1260, c.at('todos', -0.3, .35), rot=-1.5)
    else:
        d = ImageDraw.Draw(st, 'RGBA'); d.ellipse((290, 1340, 790, 1440), fill=(200, 220, 240, 50))
        fig2(st, c, PRIEST, 540, 1400, 0.95, aR=20, aL=20); put(st, staff(), 380, 1240, 1.0)
        conc2(st, 'RECONOCEN A JUAN', 540, 300, c.at('Reconocen', -0.2, .4), 50)
        pop(st, red2('RECHAZAN A JESÚS COMO MESÍAS', 48), 540, 420, c.at('Rechazan', -0.2, .35), rot=1)
        pop(st, bigword('¿Y SE SALVAN?', 130, GOLDK), 540, 640, c.at('salvan', -0.3, .4), rot=-2)
    return st

PREM = [('2:62 Y 5:69: RECOMPENSA A LOS SABEOS CON TRES CONDICIONES', 'Uno', TEAL), ('4:150-151: CONDENA AL QUE ACEPTA A UNOS Y RECHAZA A OTROS', 'Dos', REDK),
        ('EL CORÁN RECONOCE A JUAN Y A JESÚS', 'Tres', TEAL), ('LOS MANDEOS VENERAN A JUAN Y RECHAZAN A JESÚS COMO MESÍAS', 'Cuatro', REDK), ('SABEOS = MANDEOS: DEFENDIDO, NO DEMOSTRADO', 'cinco', GOLDK)]
EXITS = [('1', 'SE SALVA SIN JESÚS', 'CHOCA CON 4:150', 'Primera'), ('2', 'NO SE SALVA SIN JESÚS', 'CONDICIÓN NO ESCRITA', 'Segunda'), ('3', 'PROMESA ABROGADA', '¿POR QUÉ SE REPITE EN 5:69?', 'Tercera'), ('4', 'SABEOS ≠ MANDEOS', '¿QUIÉNES ERAN, ENTONCES?', 'Cuarta')]
def exitcard(n, a, b, w=470, h=300):
    key = ('exit', n, a, b)
    if key not in _EX:
        cc = P.Cut(w + 10, h + 10, 5, 5); cc.rr((0, 0, w, h), 20, (244, 241, 234), 4, INK2)
        cc.ell((18, 18, 98, 98), GOLDK, 0); cc.text((58, 61), n, 'anton', 50, (250, 248, 242))
        for i, l in enumerate(_wrap(a, 'bebas', 50, w - 140)): cc.text((118, 50 + i * 50), l, 'bebas', 50, INK2, anchor='lm')
        cc.rr((18, h - 118, w - 18, h - 18), 14, (120, 30, 36), 0)
        for i, l in enumerate(_wrap('COSTE: ' + b, 'bebas', 40, w - 70)): cc.text((w / 2, h - 90 + i * 40 + (20 if len(_wrap('COSTE: ' + b, 'bebas', 40, w - 70)) == 1 else 0)), l, 'bebas', 40, (250, 236, 232))
        _EX[key] = P.one(cc.out(0.02), (w + 10) / 2, (h + 10) / 2, off=(4, 7), blur=6, op=.4)
    return _EX[key]
_EX = {}
def _wrap(text, font, size, width):
    f = F(font, size); out = [[]]
    for wd in text.split():
        if f.getlength(' '.join(out[-1] + [wd])) > width and out[-1]: out.append([])
        out[-1].append(wd)
    return [' '.join(l) for l in out]

def s_dilemma(c):
    k, t = c.k, c.t; st = bg2('court').copy()
    if k <= 2:
        pop(st, tag2('EL ARGUMENTO, PASO A PASO', 56), 540, 140, c.p(0.0, .35) if k == 0 else 1.0, rot=-1)
        for i, (tx, wd, col) in enumerate(PREM):
            seg_of = (0, 1, 1, 1, 2)[i]
            p = 1.0 if k > seg_of else (c.at(wd, -0.2, .4) if k == seg_of else 0.0)
            pop(st, premise(i + 1, tx, 940, col, 40), 540, 300 + i * 190, p, rot=(-0.8, 0.6, -0.6, 0.8, -0.5)[i])
        if k == 2: pop(st, red2('DEFENDIDA, NO DEMOSTRADA', 52), 540, 1300, c.at('demostrada', -0.2, .35), rot=-2)
    else:
        pop(st, tag2('CUATRO SALIDAS', 64), 540, 140, 1.0 if k > 3 else c.p(0.0, .35), rot=-1)
        for i, (n, a, b, wd) in enumerate(EXITS):
            seg_of = 3 + i
            p = 1.0 if k > seg_of else (c.at(wd, -0.2, .45) if k == seg_of else 0.0)
            pop(st, exitcard(n, a, b), 290 + (i % 2) * 500, 470 + (i // 2) * 360, p, rot=(-1.5, 1.2, 1, -1.2)[i])
        if k == 6:
            pop(st, gold2('CADA SALIDA TIENE UN COSTE', 54), 540, 1220, c.at('coste', -0.2, .35), rot=-1.5)
            pop(st, tag2('CONTRADICCIÓN ESTRICTA: MISMA PERSONA, MISMO SENTIDO', 36), 540, 1350, c.at('estricto', -0.3, .35), rot=1)
    return st

OBJS = ['OBJECIÓN 1 · CADA UNO, SU PROFETA', 'OBJECIÓN 2 · ABROGACIÓN (3:85)', 'OBJECIÓN 3 · FE EN DIOS = FE EN TODOS', 'OBJECIÓN 4 · SABEOS ORIGINALES', 'OBJECIÓN 5 · SIN MENSAJE, SIN CASTIGO']
def s_answers(c):
    k, t = c.k, c.t; st = bg2('study').copy()
    oi = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 4}[k]
    if k != 1: pop(st, tag2(OBJS[oi], 48, accent=GOLDK), 540, 130, 1.0 if k not in (0, 3, 5, 6, 7) else c.p(0.0, .35), rot=-1)
    if k == 0:
        fig2(st, c, OBJ, 300, 1400, 0.9, aR=50 + 10 * math.sin(t * 2))
        fig2(st, c, IKS, 800, 1400, 0.9, aL=30, holdL=book('TAFSIR', (52, 104, 82), 160, 220, 40))
        pop(st, tag2('IBN KATHIR SOBRE 2:62', 50), 800, 640, c.at('Ibn', -0.2, .35), rot=2)
    elif k == 1:
        qshot(st, c, 'w_ik262_abr.png', zmax=1.0, who=IKS)
    elif k == 2:
        conc2(st, 'ARMONIZACIÓN COHERENTE', 540, 380, c.at('coherente', -0.3, .4), 54)
        pop(st, red2('PERO LEE LAS 3 CONDICIONES CON OTROS VERSÍCULOS', 40), 540, 520, c.at('otros', -0.3, .35), rot=1)
        pop(st, bigword('¿QUÉ ALCANCE TIENE?', 100, GOLDK), 540, 780, c.at('alcance', -0.3, .4), rot=-2)
        fig2(st, c, NAR, 540, 1420, 0.7, talk=True, aR=40)
    elif k == 3:
        docdrop(st, c, 'w_q385.png', 540, 470, 880, 420, -0.1, rot=-1.2, zmax=0.6)
        docdrop(st, c, 'w_tab262.png', 540, 1030, 880, 380, c.w('Tabari') - 0.3, rot=1.2, zmax=1.0)
    elif k == 4:
        pop(st, card2('TIRMIDHI 3063 (ABDALLAH IBN AMR)', 'ÚLTIMA SURA REVELADA: AL-MAIDA (SURA 5)', 900, TEAL, fs=48), 540, 420, c.at('Tirmidhi', -0.3, .4), rot=-1)
        pop(st, card2('MUSLIM 1618 (AL-BARA)', 'ÚLTIMA SURA COMPLETA: AL-TAWBA (SURA 9)', 900, (110, 116, 130), fs=48), 540, 720, c.at('Muslim', -0.3, .4), rot=1)
        pop(st, gold2('5:69 REPITE LA PROMESA', 60), 540, 1000, c.at('repite', -0.3, .35), rot=-2)
        pop(st, tag2('LA FECHA DE UNA SURA NO FIJA LA DE CADA VERSÍCULO', 36), 540, 1130, c.at('versículo', -0.3, .35), rot=1)
    elif k == 5:
        fig2(st, c, OBJ, 280, 1400, 0.85, aR=60)
        conc2(st, 'LÓGICAMENTE COHERENTE', 620, 420, c.at('coherente', -0.2, .4), 54)
        pop(st, red2('PROMESA AMPLIA, PERO SOLO PARA QUIEN ACEPTA TODO EL ISLAM', 36), 600, 600, c.at('convierte', -0.2, .35), rot=1)
    elif k == 6:
        fig2(st, c, OBJ, 280, 1400, 0.85, aR=60)
        pop(st, tag2('16:36 · 35:24 · UN MENSAJERO EN CADA PUEBLO', 40), 600, 380, c.p(0.3, .35), rot=-1)
        conc2(st, 'POSIBLE EN TEORÍA', 640, 540, c.at('posible', -0.2, .4), 50)
        pop(st, bigword('¿QUÉ FUENTE?', 130, GOLDK), 640, 780, c.at('fuente', -0.2, .4), rot=-2)
    else:
        fig2(st, c, OBJ, 280, 1400, 0.85, aR=60)
        pop(st, tag2('17:15 · 4:165', 46), 640, 380, c.p(0.3, .35), rot=-1)
        conc2(st, 'ES JUSTO RECONOCERLO', 640, 520, c.at('justo', -0.2, .4), 50)
        pop(st, red2('LA OBJECIÓN: QUIEN RECHAZA A JESÚS A SABIENDAS', 38), 620, 700, c.at('sabiendas', -0.4, .35), rot=1)
    return st

def s_scholar(c):
    k, t = c.k, c.t; st = bg2('study').copy()
    if k == 0:
        pop(st, red2('NO ES UNA INVENCIÓN APOLOGÉTICA', 54), 540, 360, c.p(0.1, .35), rot=-1.5)
        pop(st, tag2('ES UN DEBATE ACADÉMICO', 60), 540, 520, c.at('académica', -0.3, .35), rot=1)
        for i in range(3): drop(st, book(['SCRIPTURAL|POLEMICS', 'ARAM|PERIODICAL', 'J. OF|HUMANITIES'][i], [(60, 64, 84), (120, 50, 50), (60, 90, 70)][i], 220, 300, 38), 230 + i * 310, 1050, c.p(0.3 + i * 0.25, .5), rot=(-3, 2, -2)[i], s=1.2)
    elif k == 1:
        fig2(st, c, ACAD(2), lerp(1400, 820, eout(c.p(-0.1, .6))), 1420, 0.8, aL=40)
        drop(st, book('SCRIPTURAL|POLEMICS|OUP 2014', (60, 64, 84), 260, 360, 40), 320, 1040, c.at('Polemics', -0.3, .5), rot=-3, s=1.35)
        pop(st, tag2("MUN'IM SIRRY · OUP · 2014", 58), 540, 200, c.at('Sirry', -0.2, .35), rot=-1.5)
        pop(st, gold2('CAP. 3 «CONTESTING THE THEOLOGY OF EXCLUSIVIST SALVATION»', 32), 540, 330, c.at('capítulo', -0.2, .35), rot=1)
        conc2(st, 'AMPLIAR', 300, 520, c.at('ampliar', -0.2, .4), 54); pop(st, red2('RESTRINGIR', 54), 760, 520, c.at('restringirla', -0.2, .35))
    elif k == 2:
        fig2(st, c, ACAD(2), 820, 1420, 0.8, aL=40)
        pop(st, card2('SU ANÁLISIS (SIRRY)', 'ESTUDIA EL DEBATE ENTRE VERSÍCULOS Y COMENTARISTAS', 820, (90, 96, 110), fs=46), 470, 420, c.at('Analiza', -0.4, .4), rot=-1)
        pop(st, card2('NUESTRA CONCLUSIÓN', 'EL CASO MANDEO ES UN DESAFÍO PARA LA COHERENCIA', 820, GOLDK, (30, 26, 20), fs=46), 470, 760, c.at('nuestra', -0.3, .4), rot=1)
    else:
        put(st, nearmap(), 540, 600, 0.8)
        pop(st, gold2('CASO CONCRETO: LOS MANDEOS', 62), 540, 1160, c.at('mandeos', -0.3, .35), rot=-1.5)
    return st

def s_end(c):
    k, t = c.k, c.t; st = bg2('court').copy()
    if k == 0:
        pop(st, card2('CORÁN 5:69', 'PROMESA A LOS SABEOS CON TRES CONDICIONES', 880, TEAL, fs=48), 540, 400, c.at('promesa', -0.3, .4), rot=-1.5)
        pop(st, card2('CORÁN 4:150-151', 'CONDENA A QUIEN ACEPTA A UNOS Y RECHAZA A OTROS', 880, REDK, fs=48), 540, 780, c.at('condena', -0.3, .4), rot=1.5)
    elif k == 1:
        fig2(st, c, JOHN, 330, 1400, 0.85, aR=30); drop(st, scrollbig('GINZA'), 760, 1150, c.p(0.0, .5), rot=4, s=0.85)
        ill(st)
        pop(st, bigword('UNA DIFICULTAD DE FONDO', 92, GOLDK), 540, 420, c.at('dificultad', -0.2, .4), rot=-2)
    elif k == 2:
        pop(st, premise('A', 'LA PROMESA BASTA CON 3 CONDICIONES: CHOCA CON 4:150', 940, REDK, 42), 540, 420, c.at('basta', -0.2, .4), rot=-1)
        pop(st, premise('B', 'EXIGIR TODOS LOS MENSAJEROS: CONDICIÓN NO ENUNCIADA', 940, GOLDK, 42), 540, 640, c.at('exigimos', -0.2, .4), rot=1)
    elif k == 3:
        pop(st, premise('C', 'ABROGACIÓN: ¿POR QUÉ REAPARECE EN 5:69?', 940, TEAL, 42), 540, 420, c.at('abrogación', -0.2, .4), rot=-1)
        pop(st, bigword('¿Y LOS SABEOS ANTE DIOS?', 84, GOLDK), 540, 800, c.at('pregunta', -0.2, .4), rot=-2)
    elif k == 4:
        balance(st, 540, 1380, 1.0, 6 + 2 * math.sin(t * 2), left=[(tag2('PROMESA 5:69', 38, accent=TEAL), 1.0)], right=[(red2('CONDENA 4:150', 38), 1.0)])
        pop(st, gold2('UNA PROMESA QUE NECESITA SER REINTERPRETADA', 46), 540, 320, c.at('reinterpretada', -0.4, .35), rot=-1.5)
    else:
        conc2(st, 'RESPETO A LOS MUSULMANES', 540, 180, c.at('respetamos', -0.4, .4), 50)
        pop(st, bigword('¿SALVADOS O CONDENADOS?', 92, GOLDK), 540, 400, c.at('Salvados', -0.3, .4), rot=-2)
        pop(st, tag2('EL DILEMA CORÁNICO DE LOS MANDEOS', 50, accent=GOLDK), 540, 560, c.at('Salvados', 0.4, .35), rot=1)
        fig2(st, c, PRIEST, 300, 1400, 0.8, aR=20); put(st, staff(), 170, 1250, 0.9)
        fig2(st, c, NAR, 780, 1400, 0.8, talk=True, aL=40 + 20 * math.sin(t * 2))
        pc = c.at('Comenta', -0.2, .35); pop(st, pill('COMENTA', bg=(244, 242, 236), size=58), 330, 780, pc); pop(st, pill('PIDE LAS FUENTES', bg=GOLDK, fg=(30, 26, 20), size=58), 740, 780, c.at('pídelas', -0.2, .35))
        if pc > 0:
            g = ease(c.at('pídelas', -0.5, .5)); put(st, cursor(), lerp(360, 790, g) + (1 - eout(pc)) * 200, 800 + (1 - eout(pc)) * 200)
    return st

VISS = dict(hook=s_hook, who=s_who, promise=s_promise, identity=s_identity, exeg=s_exeg, jesus=s_jesus, condemn=s_condemn, dilemma=s_dilemma, answers=s_answers, scholar=s_scholar, end=s_end)

def frame(T, gt):
    sc = T[-1]
    for s in T:
        if s['start'] <= gt < s['end']: sc = s
    c = R.C(sc, gt); st = VISS[sc['id']](c)
    span = max(0.5, c.cut1 - c.cut0); z = 1 + 0.035 * ease((gt - c.cut0) / span); blur = 0.0; shift = 0.0; hb = 1.0
    din = gt - c.cut0; dout = c.cut1 - gt; last = (c.k == c.n - 1)
    if c.k > 0 and din < 0.24: p = din / 0.24; blur = 10 * (1 - ease(p)); z *= 1 + 0.06 * (1 - eout(p))
    if not last and dout < 0.12: p = 1 - dout / 0.12; blur = max(blur, 8 * p * p); z *= 1 + 0.04 * p * p
    bt = [b for b in c.seg['beats'] if b <= c.t]
    if bt and c.t - bt[-1] < 0.2: p = (c.t - bt[-1]) / 0.2; blur = max(blur, 5 * (1 - ease(p))); z *= 1 + 0.04 * (1 - eout(p))
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
    if last and sc['i'] == len(T) - 1 and dout < 0.5: st = Image.blend(st, Image.new('RGB', st.size, (14, 16, 22)), clamp(1 - dout / 0.5))
    prog = (gt - sc['start']) / max(0.1, sc['end'] - sc['start'])
    if HORIZ: return frame_h(st, c, sc, T, gt, prog)
    fr = Image.new('RGB', (W, H)); fr.paste(st, (0, 0))
    S2.draw_panel(fr, gt, R.caption(c), c.seg['src'], sc['i'], len(T), script5.CH[sc['i']], prog)
    return fr

HORIZ = False
HW, HH = 1920, 1080
_HB = {}
def frame_h(st, c, sc, T, gt, prog):
    """versión horizontal: escenario a la izquierda, columna de texto a la derecha"""
    if 'b' not in _HB:
        a = np.zeros((HH, HW, 3), np.float32); t_ = np.linspace(0, 1, HW)[None, :, None]
        a[:] = np.array((30, 29, 30)) * (1 - t_) + np.array((16, 15, 16)) * t_
        n = np.random.RandomState(9).normal(0, 1, (HH, HW)).astype(np.float32); a *= (1 + n * 0.02)[..., None]
        _HB['b'] = Image.fromarray(a.clip(0, 255).astype(np.uint8))
    fr = _HB['b'].copy(); sw = int(W * HH / SH)
    fr.paste(st.resize((sw, HH), Image.BILINEAR), (0, 0)); d = ImageDraw.Draw(fr)
    d.rectangle((sw, 0, sw + 5, HH), fill=GOLDK)
    x0 = sw + 90; xr = HW - 90
    S2.wave_icon(d, x0, 96, GOLDK, 1.2)
    P.spaced(d, x0 + 60, 110, f"{sc['i'] + 1:02d} · {script5.CH[sc['i']]}", F('bebas', 52), (242, 236, 222), 2)
    nch = len(T); gw = (xr - x0 - (nch - 1) * 10) / nch
    for k in range(nch):
        xa = x0 + k * (gw + 10); d.rounded_rectangle((xa, 170, xa + gw, 182), 6, fill=(60, 58, 58))
        fw = gw if k < sc['i'] else (gw * clamp(prog) if k == sc['i'] else 0)
        if fw > 2: d.rounded_rectangle((xa, 170, xa + fw, 182), 6, fill=TEAL if k < sc['i'] else GOLDK)
    toks = R.caption(c)
    if toks:
        f = F('bebas', 96); sp = f.getlength(' '); lines = [[]]; wmax = xr - x0
        for w, stt in toks:
            if lines[-1] and sum(f.getlength(a) for a, _ in lines[-1]) + sp * len(lines[-1]) + f.getlength(w) > wmax: lines.append([])
            lines[-1].append((w, stt))
        y = 540 - (len(lines) - 1) * 56
        for ln in lines:
            x = x0
            for w, stt in ln:
                d.text((x, y), w, font=f, fill=((96, 92, 88), (242, 236, 222), GOLDK)[stt], anchor='lm'); x += f.getlength(w) + sp
            y += 112
    if c.seg['src']:
        d.line([(x0, 900), (xr, 900)], fill=(70, 68, 66), width=2); d.rectangle((x0, 932, x0 + 12, 944), fill=GOLDK)
        P.spaced(d, x0 + 26, 938, c.seg['src'][:70], F('sans', 24), (160, 156, 150), 1.4)
    P.spaced(d, x0, 1020, 'EL ERROR CORÁNICO DE LOS MANDEOS: ¿SALVADOS O CONDENADOS?', F('bebas', 34), (120, 116, 110), 2)
    return fr
R.frame = frame

def render_part(args):
    k, n, total = args
    T, _ = R.build(); nf = int(total * FPS); a = nf * k // n; b = nf * (k + 1) // n
    global HORIZ
    HORIZ = os.environ.get('HORIZ') == '1'; size = f'{HW}x{HH}' if HORIZ else f'{W}x{H}'
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', size, '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', f'{B}/out/p5{"h" if HORIZ else ""}_{k}.mp4'], stdin=subprocess.PIPE)
    for fi in range(a, b): p.stdin.write(frame(T, fi / FPS).tobytes())
    p.stdin.close(); p.wait(); return k

if __name__ == '__main__':
    os.makedirs(B + '/out', exist_ok=True)
    T, total = R.build(); print('duración', round(total, 1), 's =', round(total / 60, 2), 'min')
    if len(sys.argv) > 1 and sys.argv[1] == 'preview':
        frac = float(sys.argv[2]); only = sys.argv[3].split(',') if len(sys.argv) > 3 else None; ims = []
        for s in T:
            if only and s['id'] not in only: continue
            for g in s['segs']: ims.append(frame(T, g['t0'] + g['dur'] * frac).resize((300, 533), Image.LANCZOS))
        cols = 8; rows = (len(ims) + cols - 1) // cols
        for part in range(0, rows, 3):
            sub = ims[part * cols:(part + 3) * cols]; sh = Image.new('RGB', (cols * 300, ((len(sub) + cols - 1) // cols) * 533), 'white')
            for i, im in enumerate(sub): sh.paste(im, ((i % cols) * 300, (i // cols) * 533))
            sh.save(f'{B}/out/p5_prev_{frac}_{part // 3}.jpg', quality=86)
        print('MISS', sorted(R.MISS)); sys.exit()
    HORIZ = os.environ.get('HORIZ') == '1'; SUF = 'h' if HORIZ else ''
    if len(sys.argv) > 1 and sys.argv[1] == 'still':
        for tv in map(float, sys.argv[2:]): frame(T, tv).save(f'{B}/out/still{SUF}_{tv:07.2f}.png')
        sys.exit()
    if not os.path.exists(f'{B}/out/mix5.wav') or not HORIZ:
        R.make_audio(T, total); os.replace(f'{B}/out/mix.wav', f'{B}/out/mix5.wav')
    from multiprocessing import Pool
    n = 4
    with Pool(n) as pool: list(pool.imap_unordered(render_part, [(k, n, total) for k in range(n)]))
    open(f'{B}/out/list5{SUF}.txt', 'w').write(''.join(f"file 'p5{SUF}_{k}.mp4'\n" for k in range(n)))
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', f'{B}/out/list5{SUF}.txt', '-c', 'copy', f'{B}/out/p5{SUF}_full.mp4'], check=True)
    for ps in ('1', '2'):
        cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{B}/out/p5{SUF}_full.mp4'] + (['-i', f'{B}/out/mix5.wav', '-map', '0:v', '-map', '1:a'] if ps == '2' else ['-an'])
        cmd += ['-c:v', 'libx264', '-preset', 'medium', '-tune', 'animation', '-b:v', '1400k' if HORIZ else '1100k', '-pass', ps, '-passlogfile', f'{B}/out/pl5{SUF}', '-pix_fmt', 'yuv420p']
        cmd += ['-f', 'mp4', '/dev/null'] if ps == '1' else ['-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-ar', '48000', '-c:a', 'aac', '-b:a', '128k', '-shortest', '-movflags', '+faststart', f'{ROOT}/renders/{OUT}{"_horizontal" if HORIZ else "_vertical"}.mp4']
        subprocess.run(cmd, check=True)
    print('ok')
