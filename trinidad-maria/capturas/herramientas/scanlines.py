import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('L'); W, H = im.size
px = im.load()
rows = [sum(1 for x in range(0, W, 2) if px[x, y] < 128) for y in range(H)]
bands = []; inb = False
for y, r in enumerate(rows):
    if r > 3 and not inb: s = y; inb = True
    elif r <= 3 and inb:
        inb = False
        if y - s > 6: bands.append((s, y))
for i, (a, b) in enumerate(bands):
    xs = [x for x in range(W) for yy in range(a, b, 3) if px[x, yy] < 128]
    print(i, a, b, min(xs), max(xs))
