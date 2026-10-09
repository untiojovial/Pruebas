# -*- coding: utf-8 -*-
# Pack histórico (R): cómo narraron los ulemas lo que pasó con la Torá, con Jesús y con los cristianos, hasta el islam.
# [[k:...]] naranja = frase clave; [[a:...]] azul = matiz, discrepancia o lo que juega en contra.
from rcards_reuse import reuse
SH = "shamela.ws (Maktaba Shamila; paginación igual a la edición impresa)"
S = "https://shamela.ws/book/"
TAB = "al-Tabari, Jamiʿ al-bayan (Tafsir), ed. Shakir (Dar al-Tarbiya wa-l-Turath)"

C = []
def add(sec, who, **kw):
    kw['sec'] = sec; kw.setdefault('tag_who', who); C.append(kw)
def again(sec, who, src, **kw):
    c = reuse(src, **kw); c['sec'] = sec; c['tag_who'] = who; c.pop('tag', None); C.append(c)

exec(open('rcards_s1.py').read())
for f in ('rcards_s2.py', 'rcards_s3.py', 'rcards_s4.py', 'rcards_s5.py'):
    try: exec(open(f).read())
    except FileNotFoundError: pass

# numeración y campos comunes
SECN = {1: "siglos I–II H", 2: "siglos III–IV H", 3: "siglos V–VI H", 4: "siglos VII–VIII H", 5: "siglos IX–XIV H"}
RCARDS = []
for i, c in enumerate(C, 1):
    c['id'] = f"R{i:02d}"
    c['tag'] = f"{SECN[c['sec']]} · {c.pop('tag_who')}"
    if 'orig' in c:
        c['uso'] = f"Pack histórico · sección {c['sec'] + 1} ({SECN[c['sec']]}) · ya capturada como {c['orig']}"
    else:
        c['uso'] = f"Pack histórico · sección {c['sec'] + 1} ({SECN[c['sec']]})"
    if not c.get('ojo'): c.pop('ojo', None)
    RCARDS.append(c)
import re as _re
KEY = {c['key']: c['id'] for c in RCARDS}
def _sub(x):
    if isinstance(x, str): return _re.sub(r'#(\w+)#', lambda m: KEY.get(m.group(1), '¿' + m.group(1) + '?'), x)
    if isinstance(x, list): return [_sub(y) for y in x]
    return x
for c in RCARDS:
    for f in list(c):
        if f not in ('specs', 'key'): c[f] = _sub(c[f])
