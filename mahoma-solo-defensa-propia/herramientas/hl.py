# Resalta frases en una página PDF con capa de texto (pdftotext -bbox) y recorta la zona.
import sys, subprocess, re, unicodedata, html, os
from PIL import Image, ImageDraw
def fold(t):
    t=unicodedata.normalize('NFD',html.unescape(t).lower()); t=''.join(c for c in t if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z0-9α-ω]','',t)
def words(pdf,n):
    x=subprocess.run(['pdftotext','-f',str(n),'-l',str(n),'-bbox',pdf,'-'],capture_output=True,text=True).stdout
    W=float(re.search(r'<page width="([\d.]+)"',x).group(1)); H=float(re.search(r'height="([\d.]+)"',x).group(1))
    ws=[(float(a),float(b),float(c),float(d),html.unescape(w)) for a,b,c,d,w in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>',x)]
    return W,H,ws
def find(ws,phrase):
    toks=[fold(t) for t in phrase.split() if fold(t)]
    fw=[fold(w[4]) for w in ws]
    best=None
    for i in range(len(ws)):
        ok=0;j=i
        for t in toks:
            if j<len(fw) and (fw[j]==t or (len(t)>3 and (t in fw[j] or fw[j] in t) and len(fw[j])>2)): ok+=1
            j+=1
        if ok>=max(1,int(len(toks)*0.7)) and (best is None or ok>best[0]): best=(ok,i,i+len(toks))
    return best
def render(pdf,n,phrases,out,dpi=150,pad=180,width=980,full=False):
    W,H,ws=words(pdf,n)
    tmp=out+'.tmp'
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r',str(dpi),'-png','-singlefile',pdf,tmp],check=True)
    im=Image.open(tmp+'.png').convert('RGB'); os.remove(tmp+'.png')
    sx,sy=im.width/W,im.height/H
    ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov); ys=[]; res=[]
    for ph in phrases:
        b=find(ws,ph); res.append((ph[:30],b and b[0]))
        if not b: continue
        lines={}
        for u in range(b[1],min(b[2],len(ws))):
            x0,y0,x1,y1,_=ws[u]; lines.setdefault(round(y0/3),[]).append((x0,y0,x1,y1))
        for bs in lines.values():
            x0=min(q[0] for q in bs);x1=max(q[2] for q in bs);y0=min(q[1] for q in bs);y1=max(q[3] for q in bs)
            ys+= [y0*sy,y1*sy]
            d.rectangle([x0*sx-2,y0*sy-1,x1*sx+2,y1*sy+2],fill=(255,214,0,100))
            d.line([x0*sx-2,y1*sy+3,x1*sx+2,y1*sy+3],fill=(200,110,0,255),width=3)
    im=Image.alpha_composite(im.convert('RGBA'),ov).convert('RGB')
    if ys and not full: im=im.crop((0,max(0,int(min(ys))-pad),im.width,min(im.height,int(max(ys))+pad)))
    if im.width>width: im=im.resize((width,round(im.height*width/im.width)),Image.LANCZOS)
    im.save(out,quality=78); print(out,im.size,res)
if __name__=='__main__':
    pass
