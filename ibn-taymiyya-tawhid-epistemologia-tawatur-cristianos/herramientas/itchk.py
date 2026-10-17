import sys, re, unicodedata
sys.path.insert(0, '.')
import itstatic as S
from itfigs import FIGS
def plain(s):
    s = re.sub(r'\[\[[a-z]:', '', s).replace(']]', '')
    s = unicodedata.normalize('NFC', s).lower()
    s = re.sub(r'[«»"“”‘’\'¿?¡!,.;:—–\-\[\]…()]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()
T = {}
for f in FIGS:
    parts = []
    for q in f['quotes']:
        parts += [q['es'], q.get('clar') or '', q.get('vtxt') or '']
        c = q.get('christian')
        if c: parts += [c['txt'], c.get('orig') or '']
    parts += [f['role'], f['why']]
    T[f['id']] = plain(' '.join(parts))
bad = 0
def chk(where, text, ids):
    global bad
    for ph in re.findall(r'«([^»]+)»', re.sub(r'\[\[[a-z]:', '', text).replace(']]', '')):
        p = plain(ph)
        if not p: continue
        if not any(p in T[i] for i in ids):
            bad += 1; print('NO VERBATIM', where, '|', ph)
for k, dice in S.ROWS.items(): chk(k, dice, [k])
for n, head, txt, codes in S.CONCL1 + S.CONCL2: chk('concl ' + n, txt, codes)
for code, claim, v, why in S.BAL: chk('bal ' + code, claim, [code]); chk('bal-why ' + code, why, [code])
print('fallos:', bad)
