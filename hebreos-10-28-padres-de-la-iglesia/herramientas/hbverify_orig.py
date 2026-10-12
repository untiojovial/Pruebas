# -*- coding: utf-8 -*-
# Comprueba que cada fragmento 'orig' de hbpadres.py (latín/griego) está (a) en la ficha del agente y (b) en la página de orig_url.
import sys, re, json, importlib.util
sys.path.insert(0,'/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb')
HB='/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb'
import hashlib, os, subprocess, html, unicodedata
def L(s):
    s=unicodedata.normalize('NFKD',s).casefold(); s=''.join(c for c in s if not unicodedata.combining(c))
    return ''.join(c for c in s if c.isalnum())
def page(url):
    u=url.split(' ')[0].split('(')[0].strip()
    f=f'{HB}/Vc/'+hashlib.md5(u.encode()).hexdigest()+'.html'
    if not os.path.exists(f) or os.path.getsize(f)<500:
        subprocess.run(['curl','-sS','-m','60','-L','-A','Mozilla/5.0 (research)','-o',f,u],capture_output=True)
    s=open(f,encoding='utf-8',errors='ignore').read()
    t=html.unescape(re.sub(r'<(script|style)[^>]*>.*?</\1>',' ',s,flags=re.S)); t=re.sub(r'<[^>]+>',' ',t)
    return L(t)
from hbpadres import PADRES
N={'P01':1,'P02':2,'P03':3,'P04':4,'P05':5,'P06':6,'P07':7,'P08':8}
for f in PADRES:
    P=json.load(open(f'{HB}/H{N[f["id"]]}/passages.json',encoding='utf-8'))
    for q in f['quotes']:
        if not q.get('orig'): continue
        parts=[x for x in re.split(r'…',q['orig']) if len(L(x))>12]
        # ficha por URL
        cands=[p for p in P if p['url'].rstrip('/').split('#')[0]==q['url'].rstrip('/')]
        inficha=all(any(L(x) in L(p.get('quote_orig','')) for p in cands) for x in parts)
        ou=[p.get('orig_url') for p in cands if p.get('orig_url')]
        inweb=None
        for u in ou:
            T=page(u)
            if all(L(x) in T for x in parts): inweb=u; break
        print(f['id'],q['ref'][:30],'| ficha:',inficha,'| web:',inweb)
