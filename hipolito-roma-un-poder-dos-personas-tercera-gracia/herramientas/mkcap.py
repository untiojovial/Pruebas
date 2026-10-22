import bands
from PIL import Image, ImageDraw
P='../hq/H9/dl/lagarde1858_text.pdf'
Y=((255,214,0),(230,120,0,255)); BL=((80,160,255),(30,110,200,255)); R=((255,160,120),(200,70,30,255)); GR=((120,210,120),(40,140,40,255))
def make(n,out,boxes,crop):
    im=bands.render(P,n,f'raw{n}',dpi=200); B=bands.bands(im,thr=120,minc=8,minh=12)
    ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
    for (i,x0,x1,c) in boxes:
        y0,y1=B[i]
        d.rectangle([x0,y0-3,x1,y1+3],fill=c[0]+(95,)); d.line([x0,y1+5,x1,y1+5],fill=c[1],width=3)
    o=Image.alpha_composite(im.convert('RGBA'),ov).convert('RGB').crop(crop)
    o.save(out); print(out,o.size)
make(73,'pg/hp52.png',[(26,285,1060,BL),(27,285,1060,BL),(28,795,1060,Y),(29,285,1060,Y),(30,285,1060,Y)],(230,180,1100,1430))
make(74,'pg/hp53.png',[(1,150,910,Y),(2,150,910,Y),(4,150,910,Y),(5,150,910,Y),(6,150,910,Y),(6,435,910,BL),(7,150,910,BL),(16,330,910,GR),(17,150,815,GR)],(110,180,960,1400))
make(72,'pg/hp51.png',[(9,580,925,Y),(10,150,690,Y),(13,255,925,BL),(14,150,925,BL),(15,150,740,BL)],(110,180,960,1100))
make(75,'pg/hp54.png',[(12,590,1050,Y),(13,290,1050,Y),(14,290,570,Y),(15,985,1050,R),(16,290,1050,R),(17,290,1050,R),(18,290,1050,R),(19,290,650,R),(25,705,1050,GR),(26,290,1050,GR),(27,290,350,GR)],(230,180,1100,1430))
def make2(P,n,out,boxes,crop,dpi=200):
    im=bands.render(P,n,f'raw_{out[3:6]}',dpi=dpi); B=bands.bands(im,thr=120,minc=8,minh=12)
    ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
    for (i,x0,x1,c) in boxes:
        y0,y1=B[i]
        d.rectangle([x0,y0-3,x1,y1+3],fill=c[0]+(95,)); d.line([x0,y1+5,x1,y1+5],fill=c[1],width=3)
    o=Image.alpha_composite(im.convert('RGBA'),ov).convert('RGB').crop(crop)
    o.save(out); print(out,o.size)
make2('../hq/H4/dl/miller1851.pdf',354,'pg/mil336.png',[(2,120,860,BL),(3,120,860,BL),(4,120,860,BL),(5,120,860,BL),(6,120,585,BL),(6,595,860,Y),(7,120,760,Y),(27,120,870,GR),(28,120,855,GR)],(60,100,898,1330))
make2('../hq/H3/dl/ds1859.pdf',469,'pg/dun458.png',[(1,250,530,Y),(3,570,1060,BL),(4,250,1060,BL),(5,250,1060,BL),(15,880,1060,GR),(16,250,1060,GR),(17,250,545,GR)],(150,190,1100,1500))
