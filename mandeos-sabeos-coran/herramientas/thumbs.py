# storyboard (un fotograma por plano) y miniaturas
import os, sys, math
sys.argv = [sys.argv[0]]
import render5 as M
from render5 import *
# miniaturas
def thumb(Wt, Ht, out):
    st = S2.bg2('river').copy(); S2.waves(st, 1.0, 820)
    S2.draw_fig(st, S2.figure(**PRIEST), 300, 1250, 1.05, aR=40, aL=60, t=0.3); put(st, staff(), 140, 1080, 1.15)
    S2.draw_fig(st, S2.figure(**JESUS), 800, 1260, 1.0, aL=20, t=0.3); put(st, red2('JUAN SÍ, JESÚS NO', 64), 560, 520, 1.0, -2)
    S2.waves(st, 1.5, 1150, SH, 1.4)
    if Wt > Ht:
        fr = Image.new('RGB', (1920, 1080), (18, 17, 18)); fr.paste(st.crop((0, 300, 1080, 1490)).resize((907, 1000)), (1013, 80))
        d = ImageDraw.Draw(fr)
        put(fr, bigword('¿SALVADOS', 190, GOLDK), 500, 300, 1.0, -2); put(fr, bigword('O CONDENADOS?', 160, REDK), 520, 500, 1.0, -2)
        put(fr, tag2('EL DILEMA CORÁNICO DE LOS MANDEOS', 60), 500, 700)
        put(fr, tag2('CORÁN 5:69 VS 4:150-151', 56, accent=TEAL), 500, 860)
        fr = fr.resize((Wt, Ht), Image.LANCZOS)
    else:
        fr = Image.new('RGB', (1080, 1920), (18, 17, 18)); fr.paste(st, (0, 430))
        put(fr, bigword('¿SALVADOS', 200, GOLDK), 540, 170, 1.0, -2); put(fr, bigword('O CONDENADOS?', 140, REDK), 540, 360, 1.0, -2)
        put(fr, tag2('EL DILEMA CORÁNICO DE LOS MANDEOS', 54), 540, 1700); put(fr, tag2('CORÁN 5:69 VS 4:150-151', 52, accent=TEAL), 540, 1820)
    fr.save(out, quality=92)
thumb(1280, 720, 'thumbs/miniatura_youtube_1280x720.jpg'); thumb(1080, 1920, 'thumbs/miniatura_tiktok_1080x1920.jpg')

