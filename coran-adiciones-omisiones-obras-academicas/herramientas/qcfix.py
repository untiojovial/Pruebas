# -*- coding: utf-8 -*-
import sys, json
import sys as _s; _s.path.insert(0, ".")
import qccap, pdfhl2, scanhl
from PIL import Image
SP = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/qc'
PQ = {}
for q in ('Q2',):
    for e in json.load(open(f'{SP}/{q}/passages.json', encoding='utf-8')): PQ[e['id']] = e
def s(pdf, pid=None, **kw):
    d = dict(pdf=pdf)
    if pid:
        e = PQ[pid]; d.update(from_=e['from_'], to=e['to'], keys=e['keys'], alts=e['alts'])
    d.update(kw); return d
what = sys.argv[1:]
if 'nold38' in what:
    pdf = f'{SP}/Q2/dl/v3_comb.pdf'
    qccap.run({'QC-nold38': [
        s(pdf, 'n1938_palimpsest_konsonantentext', ocr=True, lang='deu', dpi=200),
        s(pdf, None, from_='Die Ausbeute an bedeutenderen Varianten ist also gering', to='mündlicher wie schriftlicher Uberlieferung ausreichend erklären',
          keys=['Die Ausbeute an bedeutenderen Varianten ist also gering', 'unbeabsichtigten Schwankungen mündlicher wie schriftlicher'], alts=[], page=124, ocr=True, lang='deu', dpi=200),
        s(pdf, None, from_='Die wenigen erheblicheren Varianten machen es immerhin wahrscheinlich', to='Nachwirkungen einer nicht-othmanischen Überlieferung',
          keys=['nicht einfach mit Entstellungen des othmanischen Textes zu tun haben', 'Nachwirkungen einer nicht-othmanischen Überlieferung'], alts=[], page=124, ocr=True, lang='deu', dpi=200),
        s(pdf, 'n1938_palimpsest_keine_spur_ibnmasud', ocr=True, lang='deu', dpi=200),
        s(pdf, 'n1938_mingana_zitate_nicht_koran', ocr=True, lang='deu', dpi=200),
    ]})
if 'hirsch' in what:
    pdf = f'{SP}/V/q2/newresearchesint00hirs.pdf'
    scanhl.seg(dict(pdf=pdf, page=153, lang='eng', from_='it is pretty clear that the whole tradition was fabricated', to="in order to justify Omar's course of action",
                    keys=['pretty clear that the whole tradition was fabricated'], alts=[], dpi=200), 'rawt/QC-hirsch_seg3.png')
    M = json.load(open('rawt/manifest.json')); M['QC-hirsch']['segs'] = [f'rawt/QC-hirsch_seg{i}.png' for i in (1, 2, 3)]
    json.dump(M, open('rawt/manifest.json', 'w'), ensure_ascii=False, indent=1); print('hirsch ok')
if 'muir' in what:
    pdf = f'{SP}/V/q2/cornitscompos00muir.pdf'
    pdfhl2.seg(dict(pdf=pdf, page=43, from_='There is every security that the work of Zeid was', to='the acceptance of', keys=['There is every security that the work of Zeid was executed faithfully'], alts=[]), 'rawt/_m5a.png')
    scanhl.seg(dict(pdf=pdf, page=44, lang='eng', from_='the Coran by Ali and his party', to='the surest guarantee of its genuineness', keys=['the surest guarantee of its genuineness'], alts=[], dpi=200), 'rawt/_m5b.png')
    a, b = Image.open('rawt/_m5a.png').convert('RGB'), Image.open('rawt/_m5b.png').convert('RGB')
    W = max(a.width, b.width); im = Image.new('RGB', (W, a.height + b.height + 14), 'white')
    im.paste(a, (0, 0)); im.paste(b, (0, a.height + 14)); im.save('rawt/QC-muir_seg5.png'); print('muir ok', im.size)
    M = json.load(open('rawt/manifest.json')); M['QC-muir']['segs'] = [f'rawt/QC-muir_seg{i}.png' for i in (1, 2, 3, 4, 5)]
    json.dump(M, open('rawt/manifest.json', 'w'), ensure_ascii=False, indent=1)
