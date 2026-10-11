import re,html,glob,sys
book=sys.argv[1]; pat=sys.argv[2]; minn=int(sys.argv[3]) if len(sys.argv)>3 else 1
dia=re.compile('[ً-ٰٟـ]')
out=[]
for f in glob.glob(f'dl/{book}/p*.html'):
    t=open(f,encoding='utf-8',errors='ignore').read()
    m=re.search(r'<div class="nass[^"]*"[^>]*>(.*?)</div>\s*</div>',t,re.S)
    s=dia.sub('',html.unescape(re.sub(r'<[^>]+>','',m.group(1) if m else t)))
    n=len(re.findall(pat,s))
    if n>=minn:
        ti=re.search(r'<title>(.*?)</title>',t,re.S)
        out.append((int(re.search(r'p(\d+)',f).group(1)),n,html.unescape(ti.group(1))[:100]))
for o in sorted(out): print(o)
