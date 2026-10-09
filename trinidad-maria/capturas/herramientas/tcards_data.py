# -*- coding: utf-8 -*-
# Pack Trinidad–María (T): Allah, Jesús y María como «Trinidad» en los textos islámicos, y los coliridianos.
# [[k:...]] naranja = frase clave; [[a:...]] azul = matiz, discrepancia o lo que juega en contra.
import copy as _copy
import rcards_data as _r
SH = "shamela.ws (Maktaba Shamila; paginación igual a la edición impresa)"
S = "https://shamela.ws/book/"
WS = "https://ar.wikisource.org/wiki/"
WSQ = "ar.wikisource.org (texto del Corán, edición de Medina, rasm uthmani)"
TAB = "al-Tabari, Jamiʿ al-bayan (Tafsir), ed. Shakir (Dar al-Tarbiya wa-l-Turath)"
_R = {c['id']: c for c in _r.RCARDS}

C = []
def add(sec, who, **kw):
    kw['sec'] = sec; kw.setdefault('tag_who', who); C.append(kw)
def again(sec, who, src, **kw):
    # reutiliza una tarjeta del pack histórico (R..)
    c = _copy.deepcopy(_R[src]); c.update(kw); c['orig'] = src
    c['sec'] = sec; c['tag_who'] = who
    for k in ('tag', 'uso', 'id'): c.pop(k, None)
    C.append(c)

for f in ('tcards_s1.py', 'tcards_s2.py', 'tcards_s3.py', 'tcards_s4.py', 'tcards_s5.py'):
    try: exec(open(f).read())
    except FileNotFoundError: pass

SECN = {1: "el Corán", 2: "comentaristas", 3: "heresiógrafos e historiadores", 4: "coliridianos", 5: "la cadena de Sayf"}
TCARDS = []
for i, c in enumerate(C, 1):
    c['id'] = f"T{i:02d}"
    c['tag'] = f"{SECN[c['sec']][0].upper() + SECN[c['sec']][1:]} · {c.pop('tag_who')}"
    base = f"Pack Trinidad–María · sección {c['sec']} ({SECN[c['sec']]})"
    c['uso'] = base + (f" · ya capturada como {c['orig']} en el pack histórico" if 'orig' in c else '')
    if not c.get('ojo'): c.pop('ojo', None)
    TCARDS.append(c)
import re as _re
KEY = {c['key']: c['id'] for c in TCARDS}
def _sub(x):
    if isinstance(x, str): return _re.sub(r'#(\w+)#', lambda m: KEY.get(m.group(1), '¿' + m.group(1) + '?'), x)
    if isinstance(x, list): return [_sub(y) for y in x]
    return x
for c in TCARDS:
    for f in list(c):
        if f not in ('specs', 'key'): c[f] = _sub(c[f])
