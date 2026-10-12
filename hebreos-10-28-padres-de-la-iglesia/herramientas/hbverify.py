# -*- coding: utf-8 -*-
# Comprueba de forma independiente que cada cita (quote_en) está en la página que dice el agente. Uso: python3 -I hbverify.py H3 H4 ...
import sys, json, re, html, os, subprocess, hashlib, unicodedata
HB='/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb'
def L(s):
    s=unicodedata.normalize('NFKD',s).casefold(); s=''.join(c for c in s if not unicodedata.combining(c))
    return ''.join(c for c in s if c.isalnum())
def page(url):
    u=url.split(' ')[0].split('(')[0].strip()
    f=f'{HB}/Vc/'+hashlib.md5(u.encode()).hexdigest()+'.html'
    if not os.path.exists(f) or os.path.getsize(f)<500:
        subprocess.run(['curl','-sS','-m','60','-L','-A','Mozilla/5.0 (research)','-o',f,u],capture_output=True)
    try: s=open(f,encoding='utf-8',errors='ignore').read()
    except: return ''
    t=html.unescape(re.sub(r'<(script|style)[^>]*>.*?</\1>',' ',s,flags=re.S)); t=re.sub(r'<[^>]+>',' ',t)
    return L(t)
for h in sys.argv[1:]:
    P=json.load(open(f'{HB}/{h}/passages.json',encoding='utf-8'))
    for p in P:
        T=page(p['url']); q=L(p['quote_en'])
        # quita marcas de nota entre corchetes tipo [1710] ya normalizadas por L, probar por trozos
        ok=q in T
        if not ok:
            parts=[x for x in re.split(r'\.\.\.|…|\[…\]',p['quote_en']) if len(L(x))>25]
            ok2=all(L(x) in T for x in parts) if parts else False
        else: ok2=True
        print(h,p['id'],'OK' if ok else ('OK(trozos)' if ok2 else 'NO ENCONTRADA'),'| páginas:',len(T), '|', p['url'][:70])
