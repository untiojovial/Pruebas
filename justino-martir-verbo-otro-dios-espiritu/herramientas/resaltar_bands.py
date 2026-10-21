import sys, subprocess, os
import numpy as np
from PIL import Image, ImageDraw
def render(pdf, n, out, dpi=200):
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r',str(dpi),'-png','-singlefile',pdf,out],check=True)
    return Image.open(out+'.png').convert('RGB')
def bands(im, thr=110, minc=10, minh=12):
    a=np.array(im.convert('L')); dark=(a<thr).sum(axis=1)
    B=[];on=False
    for y,v in enumerate(dark):
        if v>minc and not on: s=y;on=True
        elif v<=minc and on:
            on=False
            if y-s>minh: B.append((s,y))
    return B
if __name__=='__main__':
    pdf,n,out=sys.argv[1],int(sys.argv[2]),sys.argv[3]
    im=render(pdf,n,out+'_raw'); B=bands(im)
    d=ImageDraw.Draw(im)
    for i,(y0,y1) in enumerate(B): d.text((2,y0),str(i),fill=(255,0,0))
    im.save(out+'_dbg.png'); print(im.size,len(B))
