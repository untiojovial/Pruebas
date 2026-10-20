import sys,re,glob,unicodedata
sys.path.insert(0,'.')
import tqdata
def fold(t):
    t=unicodedata.normalize('NFD',t.lower()); t=''.join(c for c in t if unicodedata.category(c)!='Mn')
    t=t.replace('v','u').replace('j','i').replace('æ','ae')
    t=re.sub(r'[^a-z ]',' ',t)
    return re.sub(r'\s+',' ',t).strip()
base='/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/tq/'
files=glob.glob(base+'T*/dl/*.txt')+glob.glob(base+'T*/*.txt')
corp={}
for f in files:
    try: corp[f]=fold(open(f,encoding='utf-8',errors='ignore').read())
    except: pass
# hyphen join: Kroymann OCR hyphenates lines -> also build version with 'x-\ny' joined
def foldj(t): return fold(re.sub(r'-\s*\n\s*','',t))
for f in list(corp):
    if 'csel' in f or 'kroymann' in f.lower() or 'djvu' in f:
        try: corp[f+'#j']=foldj(open(f,encoding='utf-8',errors='ignore').read())
        except: pass
allc=' '.join(corp.values())
def cov(q,n=4):
    w=fold(q).split()
    if len(w)<n: return 1.0 if ' '.join(w) in allc else 0.0
    grams=[' '.join(w[i:i+n]) for i in range(len(w)-n+1)]
    return sum(g in allc for g in grams)/len(grams)
bad=0
for s in tqdata.S:
    for q in s['quotes']:
        if q['lang']!='la': continue
        c=cov(q['lat'])
        flag='' if c>=0.95 else '  <<<<'
        if flag: bad+=1
        print(s['id'],q['id'],q['ref'],round(c,2),flag)
print('bad',bad)
