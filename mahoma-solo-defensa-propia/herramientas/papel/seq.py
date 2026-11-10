# secuencia de fotogramas (para revisar movimiento) y medida de velocidad
import sys, time
from render3 import *
T,total=build(); a,b,step=float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]); out=sys.argv[4]
ts=[]; t=a
while t<b: ts.append(t); t+=step
t0=time.time(); ims=[frame(T,x).resize((270,480),Image.BILINEAR) for x in ts]; dt=(time.time()-t0)/len(ts)
cols=12; rows=(len(ims)+cols-1)//cols; sh=Image.new('RGB',(cols*270,rows*480))
for i,im in enumerate(ims): sh.paste(im,((i%cols)*270,(i//cols)*480))
sh.save(out,quality=85); print(len(ims),'frames',round(dt,3),'s/frame')
