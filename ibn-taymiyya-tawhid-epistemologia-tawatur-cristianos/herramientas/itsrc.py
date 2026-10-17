# -*- coding: utf-8 -*-
# Reúne los pasajes de los investigadores y sirve el árabe literal (cortado por código del texto de OpenITI) con su ficha.
import sys, glob, json, re, os
IT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, IT)
import itlib
P = {}
for f in glob.glob(f'{IT}/T*/passages.json'):
    for x in json.load(open(f, encoding='utf-8')):
        P[x['id']] = x
MARK = re.compile(r'\(¬\d+\)|\|\|? ?AUTO|\|')
def tidy(s):
    s = MARK.sub(' ', s).replace('#', ' ')
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'(?:(?<=\s)|^)([بك]) (?=\S)', r'\1', s)   # espacios espurios tras ب / ك sueltas (artefacto de la digitalización)
    return s.strip()
_book_cache = {}
BOOK = {'JawabSahih': 'JawabSahih', 'jawab': 'JawabSahih', 'DarTacarud': 'DarTacarud', 'dartacarud': 'DarTacarud', 'MajmucFatawa': 'MajmucFatawa', 'majmu': 'MajmucFatawa',
        'RaddCalaMantiqiyyin': 'RaddCalaMantiqiyyin', 'wasitiyya': 'CaqidaWasitiyya', 'tadmuriyya': 'RisalaTadmuriyya', 'RisalaTadmuriyya': 'RisalaTadmuriyya',
        'isfahaniyya': 'SharhCaqidaIsfahaniyya', 'SharhCaqidaIsfahaniyya': 'SharhCaqidaIsfahaniyya', 'RisalaFiCilmQiraat': 'RisalaFiCilmQiraat', 'MinhajSunna': 'MinhajSunna',
        'Istighatha': 'Istighatha', 'hamawiyya': 'HamawiyyaKubra'}
BOOK.update({v: v for v in set(BOOK.values())})
def book_text(work):
    b = BOOK[work]
    if b not in _book_cache:
        t = itlib.get(b)
        _book_cache[b] = tidy(itlib.clean(t))
    return _book_cache[b]
def ar(pid, start=None, end=None):
    """Árabe de un pasaje (limpio de marcas editoriales); con start/end recorta por frases literales contenidas en él."""
    x = P[pid]; s = tidy(x['ar'])
    if start:
        i = s.index(start); s = s[i:]
    if end:
        j = s.index(end) + len(end); s = s[:j]
    return s
def check(pid, text):
    return text in book_text(P[pid]['work'])
def info(pid):
    x = P[pid]; return dict(work=x['work'], vol_page=x.get('vol_page'), url=x.get('openiti_url'), edition=x.get('edition_note'))
if __name__ == '__main__':
    print(len(P), 'pasajes')
    bad = 0
    for pid in P:
        if not P[pid].get('ar') or P[pid].get('work') not in BOOK: continue
        if not check(pid, ar(pid)): bad += 1; print('NO LITERAL', pid)
    print('fallos', bad)

def span(work, start, end):
    """Pasaje literal del libro entre dos frases (ambas incluidas); devuelve (texto, (vol,pág.) inicial) o lanza ValueError."""
    t = itlib.get(BOOK[work]); ct = tidy(itlib.clean(t))
    i = ct.index(start); j = ct.index(end, i) + len(end)
    return ct[i:j]
def where(work, text):
    """(vol, pág.) del comienzo de 'text' en el libro (buscando sus primeras 40 letras en el texto crudo)."""
    t = itlib.get(BOOK[work]); idx = itlib.Index(t)
    key = text[:45]
    hits = idx.find(re.escape(itlib.norm(key)))
    return [idx.where(s) for s, e in hits[:3]]
