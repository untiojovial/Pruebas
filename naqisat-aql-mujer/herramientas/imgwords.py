# -*- coding: utf-8 -*-
# Lee palabras (con cajas) de una página de un djvu.xml de archive.org. Uso: python3 -I imgwords.py <xml> <n>
import re, sys, html
def page_words(xml, n):
    t = open(xml, encoding='utf-8', errors='ignore').read()
    pages = re.split(r'<OBJECT ', t)[1:]
    p = pages[n]
    m = re.search(r'width="(\d+)" height="(\d+)"', p)
    W, H = int(m.group(1)), int(m.group(2))
    lines = []
    for ln in re.findall(r'<LINE>(.*?)</LINE>', p, re.S):
        ws = []
        for c, s in re.findall(r'<WORD coords="([^"]*)"[^>]*>(.*?)</WORD>', ln, re.S):
            a = [int(x) for x in c.split(',')[:4]]  # left,bottom,right,top
            ws.append(dict(t=html.unescape(s), l=a[0], b=a[1], r=a[2], tp=a[3]))
        if ws: lines.append(ws)
    return W, H, lines
if __name__ == '__main__':
    W, H, lines = page_words(sys.argv[1], int(sys.argv[2]))
    print(W, H, len(lines))
    for i, ln in enumerate(lines):
        y0 = min(w['tp'] for w in ln); y1 = max(w['b'] for w in ln)
        print(i, y0, y1, ' '.join(w['t'] for w in ln))
