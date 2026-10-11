import re,html,sys,subprocess
bid=sys.argv[1]; pat=sys.argv[2] if len(sys.argv)>2 else None
t=subprocess.run(['curl','-sS','-m','90',f'https://shamela.ws/book/{bid}'],capture_output=True,text=True).stdout
ti=re.search(r'<title>(.*?)</title>',t,re.S); print('TITLE:',html.unescape(ti.group(1)).strip() if ti else '', len(t))
links=re.findall(r'<a[^>]+href="(?:https://shamela.ws)?/book/%s/(\d+)[^"]*"[^>]*>(.*?)</a>'%bid,t,re.S)
print('links',len(links))
for pid,s in links:
    s=html.unescape(re.sub(r'<[^>]+>','',s)); s=re.sub(r'\s+',' ',s).strip()
    if pat is None or re.search(pat,s): print(pid,s[:90])
