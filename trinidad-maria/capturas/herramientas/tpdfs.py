import json
from pdfhl import run
HP = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hp'
REC = {p['id']: p for d in ('T3', 'T4') for p in json.load(open(f'{HP}/{d}/passages.json'))}
def R(pid, pdf, page, keys=None, alts=()):
    r = REC[pid]; return dict(pdf=pdf, page=page, from_=r['from_'], to=r['to'], keys=r['keys'] if keys is None else keys, alts=list(alts))
K, Q, H, F = f'{HP}/T3/dl/kateusz.pdf', f'{HP}/T3/dl/qsc.pdf', f'{HP}/T3/dl/hos.pdf', f'{HP}/T4/dl/folks.pdf'
PDFS = {
 'P-KT': [R('T3-16', K, 23)],
 'P-QS': [R('T3-17', Q, 135), R('T3-18', Q, 136), R('T3-19', Q, 282)],
 'P-RG': [R('T3-22', H, 4), R('T3-23', H, 7)],
 'P-FK': [R('T4-20', F, 35), R('T4-21', F, 35), R('T4-23', F, 45)],
}
import sys
run({k: v for k, v in PDFS.items() if not sys.argv[1:] or k in sys.argv[1:]})
