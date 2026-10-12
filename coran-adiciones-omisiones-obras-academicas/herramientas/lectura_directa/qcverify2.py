# -*- coding: utf-8 -*-
# Verificación tolerante: compara solo letras (sin espacios, dígitos ni puntuación). Uso: python3 -I qcverify2.py <pdf|txt> <passages.json> <work_id>
import sys, json, re, unicodedata, subprocess
src, pj, work = sys.argv[1:4]
def letters(s):
    s = unicodedata.normalize('NFKD', s).casefold()
    s = ''.join(c for c in s if not unicodedata.combining(c)).replace('ʿ', '').replace('ʾ', '')
    return ''.join(c for c in s if c.isalpha())
if src.endswith('.pdf'):
    raw = subprocess.run(['pdftotext', '-raw', src, '-'], capture_output=True, text=True).stdout
    pages = [letters(p) for p in raw.split('\f')]
else:
    pages = [letters(open(src, encoding='utf-8', errors='ignore').read())]
ps = [e for e in json.load(open(pj, encoding='utf-8')) if e['work'] == work]
ok = bad = 0
for e in ps:
    q = letters(e['passage']); hit = [i + 1 for i, p in enumerate(pages) if q in p]
    if hit: ok += 1
    else: bad += 1
    print(e['id'], 'pdf_page(agente)=', e.get('pdf_page'), '->', hit if hit else 'NO')
print('ok', ok, 'no', bad)
