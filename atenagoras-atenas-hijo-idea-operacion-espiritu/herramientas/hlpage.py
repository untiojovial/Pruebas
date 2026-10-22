# -*- coding: utf-8 -*-
# Renders a PDF page to PNG and highlights given phrases (found with pdftotext -bbox).
import subprocess, re, html, sys, os
from PIL import Image, ImageDraw

def norm(w):
    w = html.unescape(w)
    w = w.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('­', '').replace('‑', '-')
    return re.sub(r'[^\w]', '', w, flags=re.U).lower()

def words(pdf, n):
    out = subprocess.run(['pdftotext', '-f', str(n), '-l', str(n), '-bbox', pdf, '-'], capture_output=True, text=True).stdout
    page = re.search(r'<page width="([\d.]+)" height="([\d.]+)"', out)
    W, H = float(page.group(1)), float(page.group(2))
    ws = []
    for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', out):
        ws.append((float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4)), m.group(5)))
    return W, H, ws

def find(ws, phrase):
    def nrm(w):
        w2 = html.unescape(w)
        if re.fullmatch(r'\d{1,3}', w2):
            return ''
        if re.match(r'^[A-Za-z\u00c0-\u024f]+[.,;:"\u201d\u2019]*\d{1,3}$', w2):
            w2 = re.sub(r'\d+$', '', w2)
        return norm(w2)
    joined = ''; owner = []
    for i, w in enumerate(ws):
        t = nrm(w[4])
        joined += t; owner += [i] * len(t)
    target = ''.join(nrm(t) for t in phrase.split())
    res = []
    pos = joined.find(target)
    if pos >= 0:
        used = sorted(set(owner[pos:pos + len(target)]))
        res.append(used)
    return res

def render(pdf, n, phrases, out, dpi=150, crop=None, color=(255, 214, 0), focus=None):
    W, H, ws = words(pdf, n)
    tmp = out + '.tmp'
    subprocess.run(['pdftoppm', '-f', str(n), '-l', str(n), '-r', str(dpi), '-png', '-singlefile', pdf, tmp], check=True)
    im = Image.open(tmp + '.png').convert('RGB')
    sx, sy = im.width / W, im.height / H
    ov = Image.new('RGBA', im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    missing = []
    ys = []
    for ph in phrases:
        col = color
        if isinstance(ph, tuple): ph, col = ph
        hits = find(ws, ph)
        if not hits:
            missing.append(ph); continue
        for used in hits[:1]:
            # merge per line
            lines = {}
            for u in used:
                x0, y0, x1, y1, _ = ws[u]
                key = round(y0 / 3)
                lines.setdefault(key, []).append((x0, y0, x1, y1))
            for key, bs in lines.items():
                x0 = min(b[0] for b in bs); x1 = max(b[2] for b in bs); y0 = min(b[1] for b in bs); y1 = max(b[3] for b in bs)
                ys.append((y0 * sy, y1 * sy))
                d.rectangle([x0 * sx - 2, y0 * sy - 1, x1 * sx + 2, y1 * sy + 1], fill=col + (105,))
                d.line([x0 * sx - 2, y1 * sy + 2, x1 * sx + 2, y1 * sy + 2], fill=((230, 120, 0, 255) if col == color else (30, 110, 200, 255)), width=3)
    im = Image.alpha_composite(im.convert('RGBA'), ov).convert('RGB')
    if focus and ys:
        mt, mb, hh = focus
        top = max(hh + 20, int(min(y[0] for y in ys)) - mt); bot = min(im.height, int(max(y[1] for y in ys)) + mb)
        if top <= hh + 20 + 5:
            band = im.crop((0, 0, im.width, bot))
        else:
            hdr = im.crop((0, 0, im.width, hh)); body = im.crop((0, top, im.width, bot))
            band = Image.new('RGB', (im.width, hh + 16 + body.height), (255, 255, 255))
            band.paste(hdr, (0, 0)); ImageDraw.Draw(band).line([(im.width * 0.35, hh + 7), (im.width * 0.65, hh + 7)], fill=(150, 150, 150), width=2)
            band.paste(body, (0, hh + 16))
        im = band
    if crop:
        fx0, fy0, fx1, fy1 = crop
        im = im.crop((int(fx0 * im.width), int(fy0 * im.height), int(fx1 * im.width), int(fy1 * im.height)))
    im.save(out)
    os.remove(tmp + '.png')
    return missing

if __name__ == '__main__':
    pdf, n, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    print(render(pdf, n, sys.argv[4:], out))
