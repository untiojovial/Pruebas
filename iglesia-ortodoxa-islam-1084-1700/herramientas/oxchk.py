import sys, re, unicodedata
sys.path.insert(0, '.')
import oxstatic as S
from oxfigs import FIGS
def plain(s):
    s = re.sub(r'\[\[[a-z]:', '', s).replace(']]', '')
    s = unicodedata.normalize('NFC', s).lower()
    s = re.sub(r'[«»"“”‘’\'¿?¡!,.;:—–\-\[\]…()]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()
T = {f['id']: plain(' '.join(q['es'] for q in f['quotes'])) for f in FIGS}
bad = 0
def chk(where, text, ids):
    global bad
    for ph in re.findall(r'«([^»]+)»', re.sub(r'\[\[[a-z]:', '', text).replace(']]', '')):
        p = plain(ph)
        if not p: continue
        if not any(p in T[i] for i in ids):
            bad += 1; print('NO VERBATIM', where, '|', ph)
for k, (obra, dice) in S.ROWS.items(): chk(k, dice, [k])
for n, head, txt, codes in S.CONCL1 + S.CONCL2: chk('concl ' + n, txt, codes)
print('fallos:', bad)
