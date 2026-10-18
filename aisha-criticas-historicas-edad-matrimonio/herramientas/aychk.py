# -*- coding: utf-8 -*-
# Comprueba que cada frase entre «» de los resúmenes figura, tal cual, en las citas traducidas (es) o, si es un título de obra, en los datos.
import sys, re, unicodedata
AY = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ay'
sys.path.insert(0, AY)
import aystatic as S
from ayfigs import FIGS
def plain(s):
    s = re.sub(r'\[\[[a-z]:', '', s).replace(']]', '')
    s = unicodedata.normalize('NFC', s).lower()
    s = re.sub(r'[«»"“”‘’\'¿?¡!,.;:—–\-\[\]…()]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()
POOL = plain(' '.join((q.get('es') or '') + ' ' + q.get('clar', '') + ' ' + q.get('work', '') for f in FIGS for q in f['quotes']))
T = {f['id']: plain(' '.join((q.get('es') or '') + ' ' + q.get('work', '') for q in f['quotes'])) for f in FIGS}
bad = 0
def chk(where, text, ids=None):
    global bad
    t = re.sub(r'<[^>]+>', '', re.sub(r'\[\[[a-z]:', '', text).replace(']]', ''))
    for ph in re.findall(r'«([^»]+)»', t):
        p = plain(ph)
        if not p: continue
        ok = any(p in T[i] for i in ids) if ids else p in POOL
        if not ok:
            bad += 1; print('NO VERBATIM', where, '|', ph)
ID = {f['slug']: f['id'] for f in FIGS}
for slug, (obra, dice) in S.ROWS.items(): chk(slug, dice, [ID[slug]])
for n, head, txt, codes in S.CONCL1 + S.CONCL2: chk('concl ' + n, txt, codes or None)
for fecha, quien, nombra, edad, que in S.MAP: chk('map ' + fecha, nombra + ' ' + edad + ' ' + que)
print('fallos:', bad)
