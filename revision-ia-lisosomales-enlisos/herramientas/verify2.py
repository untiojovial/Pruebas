# -*- coding: utf-8 -*-
"""Verifica la segunda ronda: cada PMID se vuelve a pedir a PubMed; se comparan título, primer autor y año;
se buscan retractaciones y erratas; y se comprueba que la cita literal aparece en el resumen o en el texto completo abierto."""
import json, glob, re, os, unicodedata, sys
import pm
def norm(s):
    s = unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()
out = []; log = []
for f in sorted(glob.glob('out2/E*.json')):
    d = json.load(open(f, encoding='utf8'))
    ids = [str(s.get('pmid', '')).strip() for s in d['estudios']]
    recs = {r['pmid']: r for r in pm.records([i for i in ids if i.isdigit()])}
    for s in d['estudios']:
        p = str(s.get('pmid', '')).strip(); v = {'pmid': p, 'file': os.path.basename(f), 'problemas': []}
        if not p.isdigit():
            v['estado'] = 'SIN PMID (preprint o registro)'; s['_v'] = v; out.append(s); continue
        r = recs.get(p)
        if not r:
            v['estado'] = 'NO EXISTE EN PUBMED'; s['_v'] = v; out.append(s); log.append(f'{f} {p} NO EXISTE'); continue
        v['pubmed'] = r
        ta, tb = norm(s.get('titulo')), norm(r['title'])
        if ta[:45] != tb[:45]: v['problemas'].append('título distinto')
        fa = norm((s.get('primer_autor') or '').split(' ')[0]); ra = norm(r['authors'][0].split(' ')[0]) if r['authors'] else ''
        if fa and ra and fa != ra and fa not in norm(r['authors'][0]): v['problemas'].append(f"primer autor: {s.get('primer_autor')} / {r['authors'][0]}")
        if str(s.get('anio')) != str(r['year']): v['problemas'].append(f"año: {s.get('anio')} / {r['year']}")
        bad = [t for t in r['types'] if re.search('Retract|Erratum|Expression of Concern', t)]
        if bad: v['problemas'].append('TIPO: ' + '; '.join(bad))
        q = norm(s.get('cita_literal')); src = norm(r['abstract'] + ' ' + r['title'])
        ftp = f'ft/{p}.txt'; v['ft'] = os.path.exists(ftp)
        if v['ft']: src += ' ' + norm(open(ftp, encoding='utf8').read())
        if q:
            chunks = [c for c in re.split(r'\s*(?:\.\.\.|\[\.\.\.\]|…)\s*', s.get('cita_literal', '')) if len(c.strip()) > 25]
            miss = [c[:60] for c in chunks if norm(c)[:120] not in src]
            if miss: v['problemas'].append('cita no hallada: ' + ' / '.join(miss)[:150])
        else: v['problemas'].append('sin cita literal')
        v['estado'] = 'OK' if not v['problemas'] else 'REVISAR'
        if v['problemas']: log.append(f"{os.path.basename(f)[:3]} {p} {'; '.join(v['problemas'])}")
        s['_v'] = v; out.append(s)
json.dump(out, open('out2/verificado2.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
open('verify2.log', 'w', encoding='utf8').write('\n'.join(log))
import collections
print('registros', len(out), collections.Counter(s['_v']['estado'] for s in out)); print('\n'.join(log))
