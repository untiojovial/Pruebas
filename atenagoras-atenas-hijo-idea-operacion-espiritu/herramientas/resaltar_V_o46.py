import bands, numpy as np
from PIL import Image, ImageDraw
im=bands.render('A2/dl/otto7_text.pdf',131,'V_o46_hi',dpi=220)
a=np.array(im.convert('L')); H,W=a.shape
def bl(x0,x1,y0,y1,thr=110,minc=6,minh=12):
    sub=a[y0:y1,x0:x1]; dark=(sub<thr).sum(axis=1); B=[];on=False
    for y,v in enumerate(dark):
        if v>minc and not on: s=y;on=True
        elif v<=minc and on:
            on=False
            if y-s>minh: B.append((s+y0,y+y0))
    return B
main=bl(int(W*0.15),int(W*0.82),int(H*0.08),int(H*0.37)); note=bl(int(W*0.15),int(W*0.5),int(H*0.37),int(H*0.95))
xl=int(W*0.155); xr=int(W*0.745); Lw=xr-xl
ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
Y=((255,214,0),(230,120,0,255)); BL=((80,160,255),(30,110,200,255)); R=((255,160,120),(200,70,30,255)); G=((120,210,120),(40,140,40,255))
def box(B,i,f0,f1,c):
    y0,y1=B[i]; x0=xl+int(Lw*f0); x1=xl+int(Lw*f1)
    d.rectangle([x0,y0-3,x1,y1+3],fill=c[0]+(95,)); d.line([x0,y1+5,x1,y1+5],fill=c[1],width=3)
for i in (0,1): box(main,i,0,1,Y)
box(main,2,0,0.12,Y); box(main,2,0.12,1,BL); box(main,3,0,1,BL); box(main,4,0,0.33,BL)
box(main,5,0.575,1,R)
for i in (6,7): box(main,i,0,1,R)
box(main,8,0,0.52,R)
box(main,10,0.575,1,G); box(main,11,0,0.14,G)
NL=int(W*0.15); NR=int(W*0.5)
def nbox(i,c):
    y0,y1=note[i]; d.rectangle([NL,y0-3,NR,y1+3],fill=c[0]+(95,)); d.line([NL,y1+5,NR,y1+5],fill=c[1],width=3)
for i in (13,14,15,16,19): nbox(i,BL)
out=Image.alpha_composite(im.convert('RGBA'),ov).convert('RGB')
out.crop((int(W*0.08),int(H*0.04),int(W*0.88),int(H*0.9))).save('pg/otto46.png')
