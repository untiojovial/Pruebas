from PIL import Image, ImageDraw
im=Image.open('V_otto164_raw.png').convert('RGB'); ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
B={5:(576,602),6:(635,658),7:(683,707),8:(732,755),9:(768,797),10:(817,852)}
def box(i,x0,x1,col,line):
    y0,y1=B[i]; d.rectangle([x0,y0-3,x1,y1+3],fill=col+(95,)); d.line([x0,y1+5,x1,y1+5],fill=line,width=3)
Y=((255,214,0),(230,120,0,255)); BL=((80,160,255),(30,110,200,255))
box(5,1245,1496,*Y); box(6,283,1496,*Y); box(7,283,1385,*Y)
box(8,283,1496,*BL); box(9,283,1496,*BL); box(10,283,975,*BL)
im=Image.alpha_composite(im.convert('RGBA'),ov).convert('RGB')
im=im.crop((240,300,1540,2300)); im.save('pg/otto164.png'); print(im.size)
