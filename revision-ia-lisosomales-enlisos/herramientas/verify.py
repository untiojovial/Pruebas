#!/usr/bin/env python3
"""Verifica los JSON de los investigadores contra PubMed: existencia del PMID, título, primer autor, año, DOI,
presencia de la cita literal en el resumen y de las cifras declaradas. Escribe out/verificado.json."""
import json, glob, re, sys, os, unicodedata, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pm
def nrm(s): 
    s = unicodedata.normalize('NFKD', (s or '').lower()); s = ''.join(c for c in s if not unicodedata.combining(c)); return re.sub(r'[^a-z0-9]+', ' ', s).strip()
def sim(a, b): return difflib.SequenceMatcher(None, nrm(a), nrm(b)).ratio()
allrec = []; 
for f in sorted(glob.glob('out/R*.json')):
    if 'R6c' in f or 'verific' in f: continue
    try: d = json.load(open(f, encoding='utf8'))
    except Exception as e: print('JSON INVÁLIDO', f, e); continue
    for s in d.get('estudios', []): s['_file'] = os.path.basename(f); allrec.append(s)
pmids = sorted({str(s.get('pmid', '')).strip() for s in allrec if str(s.get('pmid', '')).strip().isdigit()})
recs = {r['pmid']: r for r in pm.records(pmids)} if pmids else {}
out = []; bad = 0
for s in allrec:
    p = str(s.get('pmid', '')).strip(); v = dict(pmid=p, file=s['_file'], problemas=[])
    if not p.isdigit(): v['estado'] = 'NO-PUBMED (registro/preprint): verificar aparte'; s['_v'] = v; out.append(s); continue
    r = recs.get(p)
    if not r: v['estado'] = 'PMID INEXISTENTE'; v['problemas'].append('PMID no devuelto por PubMed'); bad += 1; s['_v'] = v; out.append(s); continue
    ts = sim(s.get('titulo', ''), r['title'])
    if ts < 0.8: v['problemas'].append(f"título no coincide ({ts:.2f}): PubMed='{r['title'][:90]}'")
    fa = nrm(r['authors'][0]) if r['authors'] else ''
    if fa and nrm(s.get('primer_autor', '')).split(' ')[0] not in fa: v['problemas'].append(f"primer autor: declarado '{s.get('primer_autor')}', PubMed '{r['authors'][0]}'")
    if str(s.get('anio', ''))[:4] != r['year'][:4]: v['problemas'].append(f"año: declarado {s.get('anio')}, PubMed {r['year']}")
    if s.get('doi') and r['doi'] and nrm(s['doi']) != nrm(r['doi']): v['problemas'].append(f"DOI: declarado {s.get('doi')}, PubMed {r['doi']}")
    ab = nrm(r['abstract'] + ' ' + r['title']); q = nrm(s.get('cita_literal', ''))
    if q:
        words = q.split(); hit = q in ab
        if not hit and len(words) > 8:   # coincidencia por ventanas de 8 palabras
            wins = [' '.join(words[i:i + 8]) for i in range(0, len(words) - 7, 4)]; hit = sum(w in ab for w in wins) >= max(1, len(wins) // 2)
        if not hit: v['problemas'].append('la cita literal NO aparece en el resumen de PubMed')
    else: v['problemas'].append('sin cita literal')
    nums = set(re.findall(r'\d+(?:[.,]\d+)?', s.get('resultados_metricas', '') + ' ' + s.get('muestra_y_datos', '')))
    miss = [n for n in nums if len(n.replace('.', '').replace(',', '')) >= 2 and n.replace(',', '.') not in (r['abstract'] + r['title']).replace(',', '.') and n not in (r['abstract'] + r['title'])]
    if miss: v['problemas'].append('cifras que no están en el resumen: ' + ', '.join(sorted(miss)[:12]))
    v['estado'] = 'OK' if not v['problemas'] else 'REVISAR'; bad += bool(v['problemas'])
    v['pubmed'] = dict(title=r['title'], authors=r['authors'], journal=r['journal'], year=r['year'], volume=r['volume'], issue=r['issue'], pages=r['pages'], doi=r['doi'], types=r['types'], abstract=r['abstract'])
    s['_v'] = v; out.append(s)
json.dump(out, open('out/verificado.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('estudios', len(out), '| PMID únicos', len(pmids), '| con problemas', bad)
for s in out:
    if s['_v'].get('problemas'): print('-', s['_v']['file'], s['_v']['pmid'], '|', (s.get('titulo') or '')[:60], '\n    ', ' ; '.join(s['_v']['problemas'])[:400])
