import bands
from PIL import Image, ImageDraw
im=Image.open('V_tr124_hi.png').convert('RGB')
B=bands.bands(im,thr=110,minc=20,minh=24)
ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
Y=((255,214,0),(230,120,0,255)); BL=((80,160,255),(30,110,200,255))
def box(i,x0,x1,c):
    y0,y1=B[i]; d.rectangle([x0,y0-3,x1,y1+3],fill=c[0]+(95,)); d.line([x0,y1+5,x1,y1+5],fill=c[1],width=3)
W=im.width; L=int(W*0.15); R=int(W*0.985)
for i in (1,2,3,4): box(i,L,R,Y)
box(8,L,R,Y) if False else None
box(8,430,R,BL); 
for i in (9,10,11,12): box(i,L,R,BL)
box(13,L,500,BL)
out=Image.alpha_composite(im.convert('RGBA'),ov).convert('RGB')
out.crop((0,int(0.07*im.height),im.width,int(0.45*im.height))).save('pg/trollope124.png')
