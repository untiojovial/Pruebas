# -*- coding: utf-8 -*-
DY = 0
# Resalta frases latinas en una página de PDF con capa de texto OCR (tolera errores de OCR).
import sys, re, unicodedata, subprocess, html, os
from difflib import SequenceMatcher
from PIL import Image, ImageDraw
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/jd')
import hlpage
def fold(t):
    t = unicodedata.normalize('NFD', html.unescape(t).lower()); t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    t = t.replace('v', 'u').replace('j', 'i')
    return re.sub(r'[^a-z]', '', t)
def fuzzy(ws, phrase, thr=0.80):
    toks = [fold(x) for x in phrase.split()]; toks = [t for t in toks if t]
    pw = [(i, fold(w[4])) for i, w in enumerate(ws)]; pw = [(i, t) for i, t in pw if t and not re.fullmatch(r'\d+', html.unescape(ws[i][4]))]
    n = len(toks); best = (0, None)
    for a in range(len(pw)):
        for L in (n - 1, n, n + 1, n + 2):
            if L < 1 or a + L > len(pw): continue
            win = ''.join(t for _, t in pw[a:a + L]); tgt = ''.join(toks)
            r = SequenceMatcher(None, win, tgt).ratio()
            if r > best[0]: best = (r, [i for i, _ in pw[a:a + L]])
    return best if best[0] >= thr else (best[0], None)
def render(pdf, n, phrases, out, dpi=130, focus=None, thr=0.80):
    W, H, ws = hlpage.words(pdf, n)
    tmp = out + '.tmp'
    subprocess.run(['pdftoppm', '-f', str(n), '-l', str(n), '-r', str(dpi), '-png', '-singlefile', pdf, tmp], check=True)
    im = Image.open(tmp + '.png').convert('RGB'); os.remove(tmp + '.png')
    sx, sy = im.width / W, im.height / H
    ov = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    ys = []; res = []
    for ph in phrases:
        col = (255, 214, 0); 
        if isinstance(ph, tuple): ph, col = ph
        r, used = fuzzy(ws, ph, thr)
        res.append((ph[:40], round(r, 2)))
        if not used: continue
        lines = {}
        for u in used:
            x0, y0, x1, y1, _ = ws[u]; lines.setdefault(round(y0 / 4), []).append((x0, y0, x1, y1))
        for bs in lines.values():
            x0 = min(b[0] for b in bs); x1 = max(b[2] for b in bs); y0 = min(b[1] for b in bs); y1 = max(b[3] for b in bs)
            ys.append(((y0 * sy + DY), (y1 * sy + DY)))
            d.rectangle([x0 * sx - 2, (y0 * sy + DY) - 1, x1 * sx + 2, (y1 * sy + DY) + 1], fill=col + (105,))
            d.line([x0 * sx - 2, (y1 * sy + DY) + 2, x1 * sx + 2, (y1 * sy + DY) + 2], fill=(230, 120, 0, 255) if col == (255, 214, 0) else (30, 110, 200, 255), width=3)
    im = Image.alpha_composite(im.convert('RGBA'), ov).convert('RGB')
    im.save(out)
    return res
