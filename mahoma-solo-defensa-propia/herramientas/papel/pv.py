# vistas previas: un fotograma por plano (cerca del final) o en tiempos dados
import sys, glob, os, time
from render3 import *
T,total=build()
mode=sys.argv[1]
ts=[]
if mode=='ends':
    frac=float(sys.argv[2]) if len(sys.argv)>2 else 0.92
    only=sys.argv[3].split(',') if len(sys.argv)>3 else None
    for s in T:
        if only and s['id'] not in only: continue
        for g in s['segs']: ts.append(g['t0']+g['dur']*frac)
else: ts=[float(x) for x in sys.argv[2:]]
for f in glob.glob('out/prev_*.png'): os.remove(f)
t0=time.time()
for tv in ts:
    try: frame(T,tv).resize((432,768),Image.LANCZOS).save(f'out/prev_{tv:07.2f}.png')
    except Exception as e:
        import traceback; print('ERR at',tv); traceback.print_exc(); break
print('MISS',sorted(MISS)); print('s/frame',(time.time()-t0)/max(1,len(ts)))
fs=sorted(glob.glob('out/prev_*.png')); n=10
for k in range(0,len(fs),n):
    g=fs[k:k+n]; sh=Image.new('RGB',(5*432,2*768),'white')
    for i,f in enumerate(g): sh.paste(Image.open(f),((i%5)*432,(i//5)*768))
    sh.save(f'out/pv{k//n}.jpg',quality=86)
print(len(fs))
