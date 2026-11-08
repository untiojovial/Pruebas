import re,base64,os
s=open('body.html',encoding='utf-8').read()
def rep(m):
    f,alt=m.group(1).split('|',1)
    p='pg/'+f; b=base64.b64encode(open(p,'rb').read()).decode()
    mime='image/png' if f.endswith('.png') else 'image/jpeg'
    return f'<img src="data:{mime};base64,{b}" alt="{alt}">'
s=re.sub(r'\{\{IMG ([^}]+)\}\}',rep,s)
open('genealogias_mateo_lucas.html','w',encoding='utf-8').write(s)
print(len(s)/1e6,'MB')
