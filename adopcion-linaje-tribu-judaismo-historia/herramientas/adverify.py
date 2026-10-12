# -*- coding: utf-8 -*-
# Comprueba de forma independiente que cada cita (quote_en / quote_orig) de passages.json está en la página que indica el agente.
# Uso: python3 -I adverify.py A1 A2 ...    (normaliza: solo letras; hebreo sin vocales ni cantilación; griego sin acentos; mayúsculas/minúsculas ignoradas)
import sys, json, re, html, os, subprocess, hashlib, unicodedata
AD = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ad'
os.makedirs(f'{AD}/Vc', exist_ok=True)
def L(s):
    s = unicodedata.normalize('NFKD', s).casefold()
    s = ''.join(c for c in s if not unicodedata.combining(c))          # quita acentos, niqqud y teamim (categoría Mn)
    s = s.replace('־', '')                                           # maqaf
    s = s.replace('σ', 'ς').replace('ς', 'σ')                              # unifica sigma final
    return ''.join(c for c in s if c.isalnum())
def flat(o):
    if isinstance(o, str): return [o]
    if isinstance(o, list): return [x for e in o for x in flat(e)]
    if isinstance(o, dict): return [x for v in o.values() for x in flat(v)]
    return []
def pages(urlfield):
    us = re.findall(r'https?://[^\s;,()<>«»\"\']+', urlfield or '')
    if not us: return ''
    out = []
    for u in us:
        u = u.rstrip('.')
        out.append(page(u))
        m = re.match(r'https?://www\.sefaria\.org/(?!api/)([^?#]+)', u)
        if m:   # página de Sefaria (JS): añade la API con el mismo ref (hebreo y todas las versiones)
            ref = m.group(1)
            out.append(page(f'https://www.sefaria.org/api/texts/{ref}?context=0&commentary=0'))
            out.append(page(f'https://www.sefaria.org/api/v3/texts/{ref}?context=0&version=source&version=english'))
    return ' '.join(out)
def page(url):
    u = url.strip().split(' ')[0]
    f = f'{AD}/Vc/' + hashlib.md5(u.encode()).hexdigest() + '.dat'
    if not os.path.exists(f) or os.path.getsize(f) < 300:
        subprocess.run(['curl', '-sS', '-m', '90', '-L', '-A', 'Mozilla/5.0 (research)', '-o', f, u], capture_output=True)
    try: raw = open(f, encoding='utf-8', errors='ignore').read()
    except Exception: return ''
    s = raw.lstrip()
    if s[:1] in '{[':
        try: raw = ' '.join(flat(json.loads(s)))
        except Exception: pass
    t = html.unescape(re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', raw, flags=re.S)); t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    return L(t)
def parts(q):
    ps = [x for x in re.split(r'\.\.\.|…|\[…\]|\[\.\.\.\]', q) if len(L(x)) > 18]
    return ps or [q]
def check(q, T):
    if not q or not T: return None
    qq = L(q)
    if qq and qq in T: return 'OK'
    ps = parts(q)
    if len(ps) > 1 and all(L(x) in T for x in ps): return 'OK(trozos)'
    return 'NO'
if __name__ == '__main__':
    for h in sys.argv[1:]:
        try: P = json.load(open(f'{AD}/{h}/passages.json', encoding='utf-8'))
        except Exception as e:
            print(h, 'passages.json ERROR', e); continue
        for p in P:
            en = p.get('quote_en') or ''; orig = p.get('quote_orig') or ''
            r1 = check(en, pages(p['url'])) if en and p.get('url') else '-'
            ou = p.get('orig_url') or p.get('url') or ''
            r2 = check(orig, pages(ou)) if orig and ou else '-'
            print(h, p.get('id'), '| en:', r1, '| orig:', r2, '|', p.get('scope'), p.get('tag'), '|', (p.get('ref') or '')[:50])
