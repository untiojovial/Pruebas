# Busca en qué página del PDF aparece un texto. Uso: python3 -I pdffind.py file.pdf "texto"
import subprocess, sys, re
f, q = sys.argv[1], sys.argv[2]
n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', f], capture_output=True, text=True).stdout).group(1))
norm = lambda s: re.sub(r'\W+', ' ', s).lower().strip()
Q = norm(q)
for p in range(1, n + 1):
    t = subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), '-layout', f, '-'], capture_output=True, text=True).stdout
    if Q in norm(t.replace('-\n', '')): print(p)
