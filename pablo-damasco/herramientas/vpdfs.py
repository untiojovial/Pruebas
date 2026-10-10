import json, sys
from pdfhl import run
HP = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hp'
REC = {p['id']: p for p in json.load(open(f'{HP}/V6/passages.json'))}
def R(pid, pdf, page, keys=None, alts=(), extra=()):
    r = REC[pid]; return dict(pdf=pdf, page=page, from_=r['from_'], to=r['to'], keys=(r['keys'] if keys is None else keys) + list(extra), alts=list(alts))
F = f'{HP}/T4/dl/folks.pdf'
Wh = f'{HP}/V6/dl/9f1cb40d.bin'
PDFS = {
 'X-fk84': [R('V6-14', F, 94)],
 'X-fk85': [R('V6-15', F, 95, keys=['it appears to be a retelling of Paul’s supernatural conversion', 'he does not include any details about Paul persecuting Christians']),
            R('V6-14b', F, 95, keys=['he does not claim Paul corrupted the religion of Jesus'], alts=['he does claim Paul opposed the message of Jesus'])],
 'X-fk86': [R('V6-16', F, 96), R('V6-16b', F, 96, keys=['it lacks allegations of corruption'], alts=['merely an indication of what one medieval Muslim knew about Paul'])],
 'X-fk31': [R('V6-11', F, 41), R('V6-12', F, 41)],
 'X-wh10': [R('V6-19', Wh, 7, keys=['The occasional glimpse of a more positive view does, however, also appear'], alts=['Paul is widely regarded as the central figure in distorting the original teachings of Jesus']),
            R('V6-20', Wh, 7), R('V6-21', Wh, 7)],
 'X-wh11': [R('V6-22', Wh, 8), R('V6-23', Wh, 8)],
}
run({k: v for k, v in PDFS.items() if not sys.argv[1:] or k in sys.argv[1:]})
