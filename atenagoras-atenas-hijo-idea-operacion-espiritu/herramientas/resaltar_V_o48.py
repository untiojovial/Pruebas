import bands, numpy as np
from PIL import Image, ImageDraw
im=bands.render('A2/dl/otto7_text.pdf',133,'V_o48_hi',dpi=220)
a=np.array(im.convert('L')); H,W=a.shape
def bl(x0,x1,y0,y1,thr=110,minc=6,minh=12):
    sub=a[y0:y1,x0:x1]; dark=(sub<thr).sum(axis=1); B=[];on=False
    for y,v in enumerate(dark):
        if v>minc and not on: s=y;on=True
        elif v<=minc and on:
            on=False
            if y-s>minh: B.append((s+y0,y+y0))
    return B
main=bl(int(W*0.15),int(W*0.74),int(H*0.08),int(H*0.5))
xl=220; xr=1035; Lw=xr-xl
ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
Y=((255,214,0),(230,120,0,255)); BL=((80,160,255),(30,110,200,255))
def box(i,f0,f1,c):
    y0,y1=main[i]; x0=xl+int(Lw*f0); x1=xl+int(Lw*f1)
    d.rectangle([x0,y0-3,x1,y1+3],fill=c[0]+(95,)); d.line([x0,y1+5,x1,y1+5],fill=c[1],width=3)
box(1,0.0,1,Y); box(2,0,1,Y); box(3,0,0.48,Y)
box(3,0.51,1,BL); box(4,0,1,BL); box(5,0,1,BL); box(6,0,0.755,BL)
out=Image.alpha_composite(im.convert('RGBA'),ov).convert('RGB')
out.crop((int(W*0.08),int(H*0.04),int(W*0.97),int(H*0.9))).save('pg/otto48.png')
print(Image.open('pg/otto48.png').size)
