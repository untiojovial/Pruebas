# Resalta el escaneo de Ahlwardt (Berlín, vol. 9, p. 64, n.º 9455) con los colores del pack.
import json
from PIL import Image, ImageChops, ImageDraw
HP='/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hp/AhlImg/'
COL={'ctx':(255,240,160),'key':(255,176,0),'alt':(159,211,245)}
im=Image.open(HP+'p76full.jpg').convert('RGB'); W,H=im.size
top=int(H*0.075); c=im.crop((0,top,int(W*0.52),int(H*0.37)))
ov=Image.new('RGB',c.size,(255,255,255)); d=ImageDraw.Draw(ov)
def R(x0,y0,x1,y1,k): d.rectangle([x0,y0,x1,y1],fill=COL[k])
R(228,92,1152,488,'ctx')
R(880,278,1148,326,'key')      # «Abschrift von»
R(228,330,1148,384,'key')      # nombre del copista + «im J. 890 Ragab (1485)»
R(228,392,1152,486,'alt')      # «Collationirt ... im J. 960/1553»
c=ImageChops.multiply(c,ov).crop((200,60,1180,492))
c.save('rawt/X-ahl_seg1.png')
M=json.load(open('rawt/manifest.json')); M['X-ahl']={'segs':['rawt/X-ahl_seg1.png'],'title':None,'errors':[]}
json.dump(M,open('rawt/manifest.json','w'),ensure_ascii=False,indent=1)
print(c.size)
