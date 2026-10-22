import bands, numpy as np
from PIL import Image, ImageDraw
im=bands.render('A4/dl/otto1857_athenagoras.pdf',208,'V_o124_hi',dpi=220)
a=np.array(im.convert('L')); H,W=a.shape
def bl(x0,x1,y0,y1,thr=110,minc=6,minh=12):
    sub=a[y0:y1,x0:x1]; dark=(sub<thr).sum(axis=1); B=[];on=False
    for y,v in enumerate(dark):
        if v>minc and not on: s=y;on=True
        elif v<=minc and on:
            on=False
            if y-s>minh: B.append((s+y0,y+y0))
    return B
main=bl(int(W*0.12),int(W*0.8),int(H*0.06),int(H*0.55))
ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
Y=((255,214,0),(230,120,0,255)); BL=((80,160,255),(30,110,200,255))
def box(i,x0,x1,c):
    y0,y1=main[i]; d.rectangle([x0,y0-3,x1,y1+3],fill=c[0]+(95,)); d.line([x0,y1+5,x1,y1+5],fill=c[1],width=3)
box(4,200,1012,Y); box(5,200,300,Y); box(5,300,612,BL); box(5,612,1012,Y); box(6,200,1012,Y); box(7,200,600,Y)
out=Image.alpha_composite(im.convert('RGBA'),ov).convert('RGB')
out.crop((120,40,1083,int(H*0.58))).save('pg/otto124.png'); print(Image.open('pg/otto124.png').size)
