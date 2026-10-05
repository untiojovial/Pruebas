# -*- coding: utf-8 -*-
import re, html, glob, os, sys, json
D = os.path.dirname(os.path.abspath(__file__))
HAR = re.compile(r'[ؐ-ًؚ-ٰٟۖ-ۭـ]')
def norm(s):
    s = HAR.sub('', s)
    for a, b in (('أ','ا'),('إ','ا'),('آ','ا'),('ٱ','ا'),('ى','ي'),('ة','ه')):
        s = s.replace(a, b)
    return s
def extract(f):
    t = open(f, encoding='utf-8', errors='ignore').read()
    m = re.search(r'<title>(.*?)</title>', t)
    title = html.unescape(m.group(1)) if m else ''
    if '404' in title: return None
    m = re.search(r'<div class="nass[^"]*"[^>]*>(.*?)<div id="appended_pages"', t, re.S)
    body = m.group(1) if m else ''
    body = re.sub(r'<[^>]+>', ' ', body); body = html.unescape(body)
    return title, re.sub(r'\s+', ' ', body)

NAMES = {
 'زكريا': r'زكريا',
 'يحيى(نبي)': r'يحيي بن زكريا|يحيي عليه السلام|يحيي وعيسي|عيسي ويحيي|زكريا ويحيي|ويحيي عليهم|يا يحيي|يوحنا المعمدان|يوحنا بن زكريا|المعمدان',
 'عيسى/المسيح': r'عيسي عليه السلام|عيسي ابن مريم|عيسي بن مريم|المسيح',
}
CTX = r'التوراه|الانجيل|يحكم|حكم ب|شريعه|شرائع|شرعه|بدل|تبديل|حرف|تحريف|منسوخ|نسخ|الناموس|السنن'
def run(book, outname):
    files = sorted(glob.glob(f'{D}/{book}/*.html'), key=lambda x: int(os.path.basename(x).split('.')[0]))
    hits = []; pages = 0
    for f in files:
        r = extract(f)
        if not r: continue
        pages += 1
        title, body = r
        nb = norm(body)
        pid = os.path.basename(f).split('.')[0]
        for lab, pat in NAMES.items():
            for m in re.finditer(pat, nb):
                ctx = nb[max(0, m.start()-350): m.end()+350]
                ctxw = re.findall(CTX, ctx)
                if ctxw:
                    hits.append(dict(book=book, id=pid, title=title.split(' - ')[0:2], name=lab, ctxwords=sorted(set(ctxw)), ctx=ctx))
    json.dump(hits, open(f'{D}/{outname}', 'w'), ensure_ascii=False, indent=0)
    print(book, 'pages', pages, 'hits', len(hits))
if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2])
