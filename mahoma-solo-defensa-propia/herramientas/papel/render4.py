# -*- coding: utf-8 -*-
"""«¿Qué pasó con los poetas?» — vídeo corto en papel recortado. Reutiliza el motor y las ayudas de render3.py."""
import os, sys, math, subprocess
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, B)
import paper
paper.TICKER = '¿QUÉ PASÓ CON LOS POETAS?|LO QUE DICEN LAS FUENTES ISLÁMICAS'
import render3 as R
from render3 import *
import script4
R.SCENES = script4.SCENES
OUT = 'poetas_papel'
GU = 'IBN ISHAQ (TRAD. GUILLAUME), P. '
KAB = dict(coat=(110, 84, 60), head='turban', skin=1)
AFAK = dict(coat=(96, 100, 84), head='turban', headcol=(226, 220, 200), skin=2, beard=(206, 202, 196))
ASMA = dict(coat=(120, 60, 70), head='keffiyeh', headcol=(170, 104, 112), skin=0)
ZUH = dict(coat=(70, 110, 120), head='turban', skin=0)
def SING(k): return dict(coat=[(150, 96, 60), (96, 120, 110)][k], head='keffiyeh', headcol=[(206, 160, 90), (150, 170, 150)][k], skin=k)
def pt_(c): return fig

def s_hook(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg('night').copy()
        for i, spec in enumerate((KAB, AFAK, ASMA)):
            p = c.at('poetas', -0.3 + i * 0.12, .45); x = 200 + i * 340
            if p > 0: fig(st, spec, x, 1200 + (1 - eout(p)) * 520, 0.74, aR=24 + 70 * ease(c.at('poemas', -0.15 + i * 0.1, .35)), holdR=scroll())
            pop(st, xmark(210), x, 960, c.at('muertes', -0.1 + i * 0.14, .3))
        pop(st, bigword('3 POETAS', 170), 540, 330, c.at('poetas', -0.1, .4), rot=-2)
        pop(st, rtag('3 MUERTES', 84), 540, 560, c.at('muertes', -0.05, .35), rot=3)
    else:
        st = bg('desk').copy()
        pop(st, btag('NO LO CUENTA UN ENEMIGO', 60), 540, 200, c.p(0.1, .35), rot=-2)
        drop(st, book('SAHIH|AL-BUJARI', (124, 88, 46), 250, 330, 44), 300, 1010, c.at('Bujari', -0.2, .5), rot=-3, s=1.35)
        drop(st, book('IBN|ISHAQ', (124, 50, 54), 250, 330, 44), 760, 1010, c.at('Ishaq', -0.4, .5), rot=3, s=1.35)
        pop(st, ctag('HADICES · SIGLO IX', 42), 300, 480, c.at('hadices', -0.1, .35), rot=2)
        pop(st, ctag('BIOGRAFÍA · SIGLO VIII', 42), 760, 480, c.at('biógrafo', -0.1, .35), rot=-2)
        pop(st, rtag('FUENTES MUSULMANAS', 62), 540, 1250, c.at('Mahoma', -0.3, .35), rot=-2)
    return st

def s_kab(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg('dusk').copy(); put(st, fortress(), 800, 900, 0.75)
        fig(st, KAB, lerp(-300, 240, eout(c.p(-0.1, .6))), 1280, 0.85, aR=24 + 60 * ease(c.at('verso', -0.2, .4)), holdR=scroll(), tilt=2 * math.sin(t * 2.6))
        pop(st, btag("KA'B IBN AL-ASHRAF", 58), 400, 190, c.at("Ka'b", -0.1, .35), rot=-2)
        pop(st, ctag('POETA DE MEDINA', 44), 380, 310, c.at('poeta', -0.1, .35), rot=2)
        pop(st, btag('TRAS BADR, VIAJA A LA MECA', 44), 660, 440, c.at('viaja', -0.1, .35), rot=-2)
        pop(st, btag('LLORA A LOS MUERTOS DE QURAYSH', 40), 640, 550, c.at('llora', -0.1, .35), rot=2)
        docdrop(st, c, 'g_kabverses.jpg', 640, 1150, 700, 380, c.w('compone') - 0.3, rot=3)
        pop(st, rtag('VERSOS OFENSIVOS', 56), 640, 890, c.at('ofensivos', -0.1, .35), rot=-3)
    elif k == 1:
        st = bg('dusk').copy(); fig(st, KAB, 240, 1280, 0.85, aR=30, holdR=scroll())
        conc(st, 'ENEMIGO DECLARADO', 600, 200, c.at('enemigo', -0.2, .4), 54)
        pop(st, rtag('SU ARMA: LOS VERSOS', 64), 600, 340, c.at('arma', -0.2, .35), rot=-2)
        docdrop(st, c, 'b4037.jpg', 720, 1000, 520, 560, c.w('Bujari') - 0.3, rot=3, zmax=0.0)
        pop(st, btag('SAHIH AL-BUJARI 4037', 50), 720, 690, c.at('Bujari', 0.2, .35), rot=-3)
    elif k == 2:
        st = bg('desk').copy(); qshot(st, c, 'b4037.jpg')
        fig(st, RAID(0), 905, 1420, 0.78, aL=88 + 5 * math.sin(t * 2.2), tilt=2 * math.sin(t * 2.6))
    elif k == 3:
        st = bg('night').copy(); put(st, fortress(), 780, 900, 0.9)
        fig(st, KAB, lerp(780, 620, ease(c.at('sacan', -0.2, 1.0))), 1180, 0.6, a=min(1.0, c.at('sacan', -0.3, .3)))
        raiders(st, c, x0=110, y=1260, s=0.62, up=ease(c.at('Golpead', -0.2, .35)), slide=c.at('noche', -0.4, .8))
        pop(st, btag('DE NOCHE', 60), 300, 190, c.at('noche', -0.1, .35), rot=-3)
        pop(st, btag('FINGEN SER AMIGOS', 54), 660, 300, c.at('Fingen', -0.1, .35), rot=2)
        qcard_static(st, c, '¡*Golpead* al enemigo de Dios!', c.w('Golpead') - 0.3, y=420, w=820, fs=56, ref=GU + '368')
    else:
        st = bg('desk').copy(); docdrop(st, c, 'g_kab2.jpg', 540, 900, 960, 560, -0.05, rot=-1.5)
        qcard_static(st, c, '*Matad* a cualquier judío que caiga en vuestro poder.', c.w('Matad') - 0.25, y=70, fs=54, ref=GU + '369')
        pop(st, btag('A LA MAÑANA SIGUIENTE', 50), 360, 1290, c.p(0.1, .35), rot=-2)
        pop(st, rtag('IBN SUNAYNA, MERCADER', 50), 660, 1400, c.at('Sunayna', -0.2, .35), rot=2)
    return st

def s_afak(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg('day').copy(); put(st, palm(3), 950, 800, 0.9); put(st, tent(), 180, 880, 0.9)
        fig(st, AFAK, lerp(1400, 560, eout(c.p(-0.1, .6))), 1260, 0.95, aL=24 + 60 * ease(c.at('versos', -0.2, .4)), holdL=scroll(), tilt=2 * math.sin(t * 2.6))
        pop(st, btag('ABU AFAK', 84), 540, 200, c.at('Abu', -0.1, .35), rot=-2)
        pop(st, ctag('UN ANCIANO', 50), 540, 340, c.at('anciano', -0.1, .35), rot=2)
        pop(st, rtag('VERSOS CONTRA MAHOMA', 50), 540, 460, c.at('versos', -0.1, .35), rot=-2)
    else:
        st = bg('desk').copy(); qshot(st, c, 'g_abuafak.jpg')
        fig(st, AFAK, 905, 1420, 0.78, aL=20, holdL=scroll()); pop(st, xmark(260), 905, 1150, c.at('mató', -0.05, .3))
    return st

def s_asma(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg('dusk').copy(); put(st, house(), 170, 900, 1.1); put(st, house((196, 160, 124)), 920, 880, 0.9)
        fig(st, ASMA, lerp(-300, 540, eout(c.p(-0.1, .6))), 1260, 0.95, aR=24 + 60 * ease(c.at('versos', -0.2, .4)), holdR=scroll(), tilt=2 * math.sin(t * 2.6))
        pop(st, btag('ASMA BINT MARWÁN', 72), 540, 200, c.at('Asma', -0.1, .35), rot=-2)
        pop(st, ctag('UNA MUJER', 50), 540, 330, c.at('mujer', -0.1, .35), rot=2)
        pop(st, rtag('VERSOS CONTRA EL ISLAM', 50), 540, 450, c.at('versos', -0.1, .35), rot=-2)
    elif k == 1:
        st = bg('desk').copy(); qshot(st, c, 'g_asma.jpg')
        fig(st, ASMA, 905, 1420, 0.78, aL=20, holdL=scroll()); pop(st, xmark(260), 905, 1150, c.at('mató', -0.05, .3))
        pop(st, btag('ESA MISMA NOCHE', 50), 330, 1340, c.at('noche', -0.2, .35), rot=-3)
    else:
        st = bg('dawn').copy(); put(st, house(), 170, 900, 1.1)
        fig(st, RAID(1), 780, 1300, 0.9, aL=30, holdL=sword(), tilt=2 * math.sin(t * 2.6))
        pop(st, btag('POR LA MAÑANA', 56), 300, 190, c.p(0.1, .35), rot=-3)
        qcard_static(st, c, 'Has *ayudado* a Dios y a su apóstol.', c.w('Has') - 0.3, y=280, w=860, fs=54, ref=GU + '676')
        qcard_static(st, c, 'Ni dos cabras se darán de cabezazos por ella.', c.w('Ni') - 0.3, y=560, w=860, fs=50, ref=GU + '676')
    return st

def s_more(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg('day').copy(); p0 = c.p(-0.2, .5); put(st, kaaba(), 240, 960 + (1 - eout(p0)) * 60, 0.9, 0, min(1, p0 * 3))
        pop(st, btag('NO SON CASOS AISLADOS', 60), 540, 180, c.p(0.1, .35), rot=-2)
        pop(st, btag('LA MECA · AÑO 630', 46), 240, 600, c.at('Meca', -0.1, .35), rot=3)
        docdrop(st, c, 'g_singers.jpg', 720, 760, 600, 440, c.w('nombra') - 0.3, rot=2)
        g = c.at('cantoras', -0.3, .6)
        for i in range(2): fig(st, SING(i), lerp(-300 - i * 200, 220 + i * 250, eout(g)), 1380, 0.62, aR=30, holdR=scroll())
        pop(st, rtag('ORDENÓ MATARLAS', 60), 760, 1090, c.at('matarlas', -0.2, .35), rot=-3)
        pop(st, xmark(190), 220, 1200, c.at('murió', -0.1, .3)); conc(st, 'INMUNIDAD', 500, 960, c.at('inmunidad', -0.1, .4), 44)
    else:
        st = bg('desk').copy()
        pop(st, btag('SUNAN ABU DAWUD 4361', 60), 540, 200, c.at('Dawud', -0.2, .35), rot=-2)
        fig(st, dict(coat=(90, 96, 110), head='turban', skin=2), 280, 1300, 0.85, aR=20, tilt=2 * math.sin(t * 2.6))
        pop(st, ctag('UN CIEGO', 46), 280, 700, c.at('ciego', -0.1, .35), rot=-2)
        pop(st, btag('SU ESCLAVA, MADRE DE SUS HIJOS', 42), 680, 420, c.at('esclava', -0.1, .35), rot=2)
        pop(st, rtag('INSULTABA AL PROFETA', 50), 700, 540, c.at('insultaba', -0.1, .35), rot=-2)
        qcard_static(st, c, 'Sed testigos: por su *sangre* no se debe nada.', c.w('Sed') - 0.3, y=680, w=640, fs=48, ref='ABU DAWUD 4361', x=700)
    return st

def s_fair(c):
    k, t = c.k, c.t
    if k == 0:
        st = bg('day').copy(); pop(st, btag('LO JUSTO', 90), 540, 190, c.at('justo', -0.2, .35), rot=-2)
        pop(st, sign("KA'B ANIMABA AL ENEMIGO", 860, 130, num='1', nc=(58, 128, 76), fs=58), 540, 420, c.at('Uno', -0.1, .4), rot=-1)
        pop(st, sign('ABU AFAK Y ASMA: SIN CADENA', 860, 130, num='2', nc=(58, 128, 76), fs=56), 540, 610, c.at('Dos', -0.1, .4), rot=1)
        conc(st, 'MUCHOS ESTUDIOSOS LOS RECHAZAN', 580, 780, c.at('rechazan', -0.3, .4), 42)
        pop(st, rtag("KA'B: EN BUJARI Y MUSLIM", 58), 540, 960, c.at('cambio', -0.2, .35), rot=-2)
        fig(st, NAR, 540, 1440, 0.62, aR=20 + 20 * math.sin(t * 2), aL=20 - 20 * math.sin(t * 2))
    elif k == 1:
        st = bg('desk').copy(); pop(st, sign('PERDONABA AL ARREPENTIDO', 860, 130, num='3', nc=(58, 128, 76), fs=58), 540, 190, c.at('Tres', -0.1, .4), rot=-1)
        docdrop(st, c, 'g_repent.jpg', 500, 660, 860, 460, c.w('Ibn') - 0.1, rot=-2)
        g = c.at('poeta', -0.3, .6)
        if g > 0: fig(st, ZUH, lerp(1400, 860, eout(g)), 1420, 0.8, aL=30, holdL=scroll(), tilt=2 * math.sin(t * 2.6))
        pop(st, btag("KA'B IBN ZUHAYR", 48), 520, 1080, c.at('Zuhayr', -0.2, .35), rot=-2)
        conc(st, 'SE HIZO MUSULMÁN: PERDONADO', 500, 1220, c.at('perdonado', -0.4, .4), 44)
    else:
        st = bg('day').copy(); pop(st, btag('LA CONDICIÓN', 84), 540, 200, c.at('condición', -0.2, .35), rot=-2)
        fig(st, ZUH, 260, 1300, 0.8, aR=30); fig(st, KAB, 820, 1300, 0.8, aL=30, holdL=scroll())
        conc(st, 'SE ARREPIENTE: VIVE', 300, 640, c.at('arrepentía', -0.3, .4), 46)
        pop(st, rtag('SIGUE CON SUS VERSOS', 46), 800, 640, c.at('versos', -0.3, .35), rot=2)
        pop(st, xmark(260), 820, 1040, c.at('no', -0.05, .3, nth=0) if False else c.p(c.seg['tt'][-1] - 0.05, .3))
    return st

def s_jesus(c):
    k, t = c.k, c.t
    if k <= 2:
        st = bg('garden').copy(); put(st, palm(5), 110, 800, 0.9); put(st, palm(6), 990, 790, 0.75)
        fig(st, JESUS, lerp(-300, 300, eout(c.p(-0.1, .6))) if k == 0 else 300, 1290, 0.92, aR=30 + (20 if k == 1 else 0), tilt=2 * math.sin(t * 2.6) if k == 1 else 0)
        if k == 0:
            pop(st, btag('COMPÁRALO CON JESÚS', 66), 540, 200, c.p(0.0, .35), rot=-2)
            for i in range(2): fig(st, PETER | dict(coat=[(96, 110, 90), (124, 100, 66)][i], hair=[(70, 50, 36), (150, 146, 140)][i], beard=None if i == 0 else (150, 146, 140)), lerp(1400, 700 + i * 210, eout(c.at('discípulos', -0.4, .6))), 1320 + i * 20, 0.66)
        elif k == 1:
            for i in range(2): fig(st, PETER | dict(coat=[(96, 110, 90), (124, 100, 66)][i], hair=[(70, 50, 36), (150, 146, 140)][i], beard=None if i == 0 else (150, 146, 140)), 700 + i * 210, 1320 + i * 20, 0.66)
            qcard_follow(st, c, y=70, fs=54, ref='MATEO 5:44')
        else:
            fig(st, PETER, lerp(1400, 780, eout(c.p(-0.1, .6))), 1310, 0.8, aL=40, tilt=2 * math.sin(t * 2.6))
            pop(st, btag('PEDRO', 46), 780, 730, c.at('Pedro', -0.1, .35), rot=3)
            qcard_static(st, c, 'Cuando lo insultaban, no devolvía el *insulto*.', c.w('Cuando') - 0.3, y=70, w=900, fs=52, ref='1 PEDRO 2:23')
    else:
        st = bg('day').copy()
        conc(st, 'RESPETO A LOS MUSULMANES', 560, 190, c.at('respetamos', -0.4, .4), 50)
        pop(st, btag('RIGOR CON LAS FUENTES', 54), 540, 320, c.at('fuentes', -0.3, .35), rot=2)
        for i, spec in enumerate((KAB, AFAK, ASMA)): fig(st, spec, 200 + i * 340, 1300, 0.7, aR=28, holdR=scroll())
        pop(st, bigword('¿Y TÚ?', 200), 540, 720, c.at('parece', -0.5, .4), rot=-3)
        pc = c.at('Comenta', -0.2, .35); pop(st, pill('COMENTA', size=58), 300, 500, pc); pop(st, pill('PIDE LAS PÁGINAS', bg=RED, fg=(250, 246, 238), size=58), 730, 500, c.at('pídelas', -0.2, .35))
        if pc > 0:
            g = ease(c.at('pídelas', -0.5, .5)); put(st, cursor(), lerp(330, 780, g) + (1 - eout(pc)) * 200, 520 + (1 - eout(pc)) * 200)
    return st

R.VIS = dict(hook=s_hook, kab=s_kab, afak=s_afak, asma=s_asma, more=s_more, fair=s_fair, jesus=s_jesus)

def render_part(args):
    k, n, total = args
    T, _ = build(); nf = int(total * FPS); a = nf * k // n; b = nf * (k + 1) // n
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', f'{B}/out/p4_{k}.mp4'], stdin=subprocess.PIPE)
    for fi in range(a, b): p.stdin.write(frame(T, fi / FPS).tobytes())
    p.stdin.close(); p.wait(); return k

if __name__ == '__main__':
    T, total = build(); print('duración', round(total, 1), 's =', round(total / 60, 2), 'min')
    if len(sys.argv) > 1 and sys.argv[1] == 'preview':
        frac = float(sys.argv[2]); ims = []
        for s in T:
            for g in s['segs']: ims.append(frame(T, g['t0'] + g['dur'] * frac).resize((360, 640), Image.LANCZOS))
        cols = 8; rows = (len(ims) + cols - 1) // cols; sh = Image.new('RGB', (cols * 360, rows * 640), 'white')
        for i, im in enumerate(ims): sh.paste(im, ((i % cols) * 360, (i // cols) * 640))
        sh.save(f'{B}/out/p4_prev_{frac}.jpg', quality=86); print('MISS', sorted(R.MISS)); sys.exit()
    make_audio(T, total); os.replace(f'{B}/out/mix.wav', f'{B}/out/mix4.wav')
    from multiprocessing import Pool
    n = 4
    with Pool(n) as pool: list(pool.imap_unordered(render_part, [(k, n, total) for k in range(n)]))
    open(f'{B}/out/list4.txt', 'w').write(''.join(f"file 'p4_{k}.mp4'\n" for k in range(n)))
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', f'{B}/out/list4.txt', '-c', 'copy', f'{B}/out/p4_full.mp4'], check=True)
    for ps in ('1', '2'):
        cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{B}/out/p4_full.mp4'] + (['-i', f'{B}/out/mix4.wav', '-map', '0:v', '-map', '1:a'] if ps == '2' else ['-an'])
        cmd += ['-c:v', 'libx264', '-preset', 'medium', '-tune', 'animation', '-b:v', '1300k', '-pass', ps, '-passlogfile', f'{B}/out/pl4', '-pix_fmt', 'yuv420p']
        cmd += ['-f', 'mp4', '/dev/null'] if ps == '1' else ['-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-ar', '48000', '-c:a', 'aac', '-b:a', '128k', '-shortest', '-movflags', '+faststart', f'{B}/out/{OUT}.mp4']
        subprocess.run(cmd, check=True)
    print('ok')
