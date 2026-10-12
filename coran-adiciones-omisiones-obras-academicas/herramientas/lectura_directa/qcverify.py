# -*- coding: utf-8 -*-
# Uso: python3 -I qcverify.py <pdf> <passages.json> <work_id> [offset]   (offset = PDF page - printed page)
import sys, json, re, unicodedata, subprocess
pdf, pj, work = sys.argv[1:4]
def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in (('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('–', '-'), ('—', '-'), ('­', ''), ('ﬁ', 'fi'), ('ﬂ', 'fl')):
        s = s.replace(a, b)
    s = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', s)
    s = re.sub(r'\[\d{1,3}\]', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()
raw = subprocess.run(['pdftotext', '-raw', pdf, '-'], capture_output=True, text=True).stdout
pages = [norm(p) for p in raw.split('\f')]
ps = [e for e in json.load(open(pj, encoding='utf-8')) if e['work'] == work]
ok = bad = 0
for e in ps:
    q = norm(e['passage'])
    hit = [i + 1 for i, p in enumerate(pages) if q in p]
    if hit: ok += 1
    else:
        bad += 1
        # buscar el comienzo y el final
        h1 = [i + 1 for i, p in enumerate(pages) if q[:60] in p]
        h2 = [i + 1 for i, p in enumerate(pages) if q[-60:] in p]
    print(e['id'], 'pdf_page(agente)=', e.get('pdf_page'), 'ref=', e['ref'][:30], '->', hit if hit else ('NO; inicio', h1, 'fin', h2))
print('ok', ok, 'no', bad)
