#!/usr/bin/env python3
"""Herramienta de búsqueda bibliográfica (PubMed E-utilities, Europe PMC, ClinicalTrials.gov) con caché y control de ritmo.
Uso:
  python3 pm.py search '<consulta PubMed>' [retmax=40]     -> PMID | año | revista | título
  python3 pm.py fetch <PMID> [<PMID> ...]                  -> registro completo con resumen (abstract)
  python3 pm.py epmc '<consulta Europe PMC>' [n=25]        -> incluye preprints (añade 'SRC:PPR' para solo preprints)
  python3 pm.py ctgov '<consulta>' [n=20]                  -> estudios registrados en ClinicalTrials.gov
  python3 pm.py oa <PMID> ...                              -> ¿hay texto completo en acceso abierto? (PMCID, isOpenAccess)
  python3 pm.py ft <PMID> ...                              -> descarga el texto completo abierto a ft/<PMID>.txt (léelo con Read)
  python3 pm.py ftgrep <PMID> '<regex>'                    -> busca en el texto completo y muestra el contexto
"""
import sys, os, json, time, hashlib, fcntl, urllib.request, urllib.parse, ssl, re
import xml.etree.ElementTree as ET
B = os.path.dirname(os.path.abspath(__file__)); C = B + '/cache'
ctx = ssl.create_default_context(cafile='/root/.ccr/ca-bundle.crt')
def get(url):
    k = C + '/' + hashlib.sha1(url.encode()).hexdigest()
    if os.path.exists(k): return open(k, encoding='utf8').read()
    with open(C + '/.lock', 'w') as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        for a in range(6):
            try:
                time.sleep(0.45)
                r = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'lit-review-tool/1.0'}), context=ctx, timeout=60).read().decode('utf8', 'replace'); break
            except Exception as e:
                r = None; time.sleep(2 + a * 2)
        fcntl.flock(lk, fcntl.LOCK_UN)
    if r is None: print('ERROR de red:', url[:120]); sys.exit(1)
    open(k, 'w', encoding='utf8').write(r); return r
EU = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
def txt(e): return ''.join(e.itertext()).strip() if e is not None else ''
def records(pmids):
    out = []
    for i in range(0, len(pmids), 40):
        x = get(EU + 'efetch.fcgi?db=pubmed&retmode=xml&id=' + ','.join(pmids[i:i + 40])); root = ET.fromstring(x)
        for a in root.findall('.//PubmedArticle'):
            m = a.find('MedlineCitation'); art = m.find('Article'); j = art.find('Journal')
            au = []
            for p in art.findall('.//AuthorList/Author'):
                ln = txt(p.find('LastName')); ini = txt(p.find('Initials')); cn = txt(p.find('CollectiveName'))
                au.append((ln + ' ' + ini).strip() or cn)
            year = txt(j.find('.//PubDate/Year')) or txt(j.find('.//PubDate/MedlineDate'))[:4]
            doi = ''
            for idn in a.findall('PubmedData/ArticleIdList/ArticleId'):
                if idn.get('IdType') == 'doi': doi = idn.text or ''
            ab = ' '.join((('[' + t.get('Label') + '] ') if t.get('Label') else '') + txt(t) for t in art.findall('.//Abstract/AbstractText'))
            out.append(dict(pmid=txt(m.find('PMID')), title=txt(art.find('ArticleTitle')), authors=au, journal=txt(j.find('ISOAbbreviation')) or txt(j.find('Title')), year=year,
                            volume=txt(j.find('.//Volume')), issue=txt(j.find('.//Issue')), pages=txt(art.find('.//MedlinePgn')) or txt(art.find('.//ELocationID')), doi=doi,
                            types=[txt(t) for t in art.findall('.//PublicationTypeList/PublicationType')], abstract=ab))
    return out

def oa(pmid):
    """Estado de acceso abierto según Europe PMC: dict(pmcid, isOpenAccess, inEPMC, license, doi)."""
    d = json.loads(get('https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=1&query=' + urllib.parse.quote('EXT_ID:' + str(pmid) + ' AND SRC:MED')))
    r = (d.get('resultList', {}).get('result') or [{}])[0]
    return {'pmid': str(pmid), 'pmcid': r.get('pmcid'), 'isOpenAccess': r.get('isOpenAccess'), 'inEPMC': r.get('inEPMC'), 'license': r.get('license'), 'doi': r.get('doi')}
def fulltext(pmid):
    """Texto completo (solo si Europe PMC lo sirve en acceso abierto). Devuelve (ruta_txt, n_caracteres) o (None, motivo)."""
    o = oa(pmid)
    if not o['pmcid']: return None, 'sin PMCID: texto completo no disponible en PubMed Central'
    p = B + '/ft/' + str(pmid) + '.txt'
    if os.path.exists(p): return p, os.path.getsize(p)
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/' + o['pmcid'] + '/fullTextXML'
    k = C + '/' + hashlib.sha1(url.encode()).hexdigest()
    if not os.path.exists(k):
        try:
            time.sleep(0.4); x = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'lit-review-tool/1.0'}), context=ctx, timeout=90).read().decode('utf8', 'replace')
        except Exception as e:
            return None, 'Europe PMC no sirve el XML (' + str(e)[:60] + '): ' + o['pmcid']
        open(k, 'w', encoding='utf8').write(x)
    x = open(k, encoding='utf8').read()
    try: root = ET.fromstring(x)
    except Exception as e: return None, 'XML no legible'
    out = []
    def walk(e, depth=0):
        tag = e.tag.split('}')[-1]
        if tag in ('ref-list', 'back', 'front'): return
        if tag == 'title': out.append('\n' + '#' * min(depth, 4) + ' ' + txt(e))
        elif tag == 'p': out.append(txt(e))
        elif tag in ('table-wrap', 'fig'):
            out.append('[' + tag.upper() + '] ' + re.sub(r'\s+', ' ', txt(e))[:2500])
        else:
            for c in e: walk(c, depth + (1 if tag == 'sec' else 0))
    body = root.find('.//body')
    if body is None: return None, 'XML sin cuerpo (solo metadatos): ' + o['pmcid']
    walk(body); t = '\n'.join(out)
    os.makedirs(B + '/ft', exist_ok=True); open(p, 'w', encoding='utf8').write(t); return p, len(t)
if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'search':
        n = sys.argv[3] if len(sys.argv) > 3 else '40'
        d = json.loads(get(EU + 'esearch.fcgi?db=pubmed&retmode=json&sort=relevance&retmax=' + n + '&term=' + urllib.parse.quote(sys.argv[2])))['esearchresult']
        print('TOTAL', d['count'], '| mostrando', len(d['idlist']))
        for r in records(d['idlist']): print(f"{r['pmid']} | {r['year']} | {r['journal']} | {r['title']} | {'; '.join(r['types'][:2])}")
    elif cmd == 'fetch':
        for r in records(sys.argv[2:]):
            print('=' * 100); print('PMID', r['pmid'], '| DOI', r['doi']); print(r['title']); print(', '.join(r['authors'][:8]) + (' et al.' if len(r['authors']) > 8 else ''))
            print(f"{r['journal']}. {r['year']};{r['volume']}({r['issue']}):{r['pages']} | tipos: {'; '.join(r['types'])}"); print('RESUMEN:', r['abstract'] or '(sin resumen en PubMed)')
    elif cmd == 'oa':
        for p in sys.argv[2:]: print(oa(p))
    elif cmd == 'ft':
        for p in sys.argv[2:]:
            a, b = fulltext(p); print(p, '->', a, '|', b)
    elif cmd == 'ftgrep':
        a, b = fulltext(sys.argv[2])
        if not a: print('NO DISPONIBLE:', b)
        else:
            t = open(a, encoding='utf8').read()
            for m in re.finditer(sys.argv[3], t, flags=re.I): print('...' + t[max(0, m.start() - 250):m.end() + 350].replace('\n', ' ') + '...\n')
    elif cmd == 'epmc':
        n = sys.argv[3] if len(sys.argv) > 3 else '25'
        d = json.loads(get('https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=' + n + '&query=' + urllib.parse.quote(sys.argv[2])))
        print('TOTAL', d.get('hitCount'))
        for r in d.get('resultList', {}).get('result', []):
            print('=' * 100); print(r.get('source'), r.get('id'), '| PMID', r.get('pmid'), '| DOI', r.get('doi'), '|', r.get('pubYear'), '|', (r.get('journalInfo') or {}).get('journal', {}).get('title') or (r.get('bookOrReportDetails') or {}).get('publisher') or r.get('source'))
            print(r.get('title')); print(r.get('authorString', '')[:200]); print('RESUMEN:', re.sub('<[^>]+>', '', r.get('abstractText', '') or '')[:1800])
    elif cmd == 'ctgov':
        n = sys.argv[3] if len(sys.argv) > 3 else '20'
        d = json.loads(get('https://clinicaltrials.gov/api/v2/studies?pageSize=' + n + '&query.term=' + urllib.parse.quote(sys.argv[2])))
        for s in d.get('studies', []):
            p = s['protocolSection']; i = p['identificationModule']; st = p.get('statusModule', {}); de = p.get('descriptionModule', {})
            print('=' * 100); print(i['nctId'], '|', st.get('overallStatus'), '|', (st.get('startDateStruct') or {}).get('date'), '|', i.get('briefTitle')); print('COND:', p.get('conditionsModule', {}).get('conditions')); print('RESUMEN:', (de.get('briefSummary') or '')[:900])
