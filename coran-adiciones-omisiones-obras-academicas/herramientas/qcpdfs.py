# -*- coding: utf-8 -*-
# Capturas de las obras del pack QC a partir de PDF con capa de texto (pdfhl2) o escaneados (scanhl). Uso: python3 -I qcpdfs.py [ids]
import sys, json
import qccap
SP = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/qc'
def P(q):
    return {e['id']: e for e in json.load(open(f'{SP}/{q}/passages.json', encoding='utf-8'))}
PQ = {}
for q in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q8'): PQ.update(P(q))
def spec(pdf, ids, lang=None, page=None, ocr=False, pages=None, dpi=None):
    out = []
    for n, i in enumerate(ids):
        e = PQ[i]; pg = (pages[n] if pages else None) or page or e.get('pdf_page') or None
        d = dict(pdf=pdf, page=pg, from_=e['from_'], to=e['to'], keys=e['keys'], alts=e['alts'])
        if lang: d['lang'] = lang
        if ocr: d['ocr'] = True
        if dpi: d['dpi'] = dpi
        out.append(d)
    return out
TXT = {  # id: (pdf, ids)
 'QC-sinai': (f'{SP}/V/sinai/keyterms.pdf', ['kt-pref-1', 'kt-q37-1', 'kt-q29-1', 'kt-q74-1', 'kt-ubayy-1', 'kt-jahannam-1']),
 'QC-shoemaker': (f'{SP}/V/shoemaker/shoemaker.pdf', ['shoemaker2022-01', 'shoemaker2022-05', 'shoemaker2022-07', 'shoemaker2022-11', 'shoemaker2022-23', 'shoemaker2022-20']),
 'QC-deroche14': (f'{SP}/V/q5/deroche.pdf', ['q5-deroche2014-10', 'q5-deroche2014-11', 'q5-deroche2014-15', 'q5-deroche2014-18']),
 'QC-vanputten': (f'{SP}/V/q5/vanputten.pdf', ['q5-vanputten2019-21', 'q5-vanputten2019-22', 'q5-vanputten2019-25']),
 'QC-dye': (f'{SP}/V/archimede/D1_02_DYE.pdf', ['dye2023-contextes-02', 'dye2023-contextes-03', 'dye2023-contextes-04', 'dye2023-contextes-05']),
 
 'QC-chahdi': (f'{SP}/V/archimede/D1_05_CHAHDI.pdf', ['chahdi2023-canonisation-02', 'chahdi2023-canonisation-03', 'chahdi2023-canonisation-04']),
 'QC-vk': (f'{SP}/V/q6/vk2009.pdf', ['vk2009-01', 'vk2009-02', 'vk2009-07', 'vk2009-08', 'vk2009-10']),
}
TXT.update({
 'QC-nold09': (f'{SP}/V/q2/v1.pdf', ['n1909_fischer_moeglich', 'n1909_sur74_interpolation', 'n1909_sur8_nachtrag', 'n1909_verlorene_angaben', 'n1909_verlorene_agnostisch', 'n1909_steinigung_nicht_koranisch']),
 'QC-nold19': (f'{SP}/V/q2/v2.pdf', ['n1919_praeliminar_revision', 'n1919_ubai_zwei_suren_D', 'n1919_ubai_suren_unecht', 'n1919_ibn_masud_ablehnung_berechtigt', 'n1919_burning_uthman_accepted', 'n1919_gestalt_fertig_hafsa']),
 'QC-nold38': (f'{SP}/Q2/dl/v3_comb.pdf', ['n1938_palimpsest_konsonantentext', 'n1938_palimpsest_keine_spur_ibnmasud', 'n1938_mingana_zitate_nicht_koran']),
 'QC-hirsch': (f'{SP}/V/q2/newresearchesint00hirs.pdf', ['hirsch_omissions_miracle', 'hirsch_noeldeke_denies', 'hirsch_fabricated']),
 'QC-muir': (f'{SP}/V/q2/cornitscompos00muir.pdf', ['muir_uthman_recension', 'muir_codices_burned', 'muir_interpolated_medina_22', 'muir_interpolated_sura2', 'muir_faithful']),
})
ONLY = sys.argv[1:]
T = {k: spec(*v) for k, v in TXT.items() if not ONLY or k in ONLY}
BOU = f'{SP}/V/archimede/D1_03_BOUALI.pdf'
EXTRA = {
 'QC-bouali': [dict(pdf=BOU, page=7, from_='Une seconde hypothèse est cependant possible', to="qui porte l’empreinte", keys=['le processus rédactionnel fut continu', 'il ne faut pas totalement exclure que ce verset (Q17, 33)'], alts=[]),
               dict(pdf=BOU, page=7, from_='du Décalogue', to='caractérise en tout cas ce verset', keys=['une interpolation peut-être introduite à l’époque sufyanide'], alts=['Si rien n’est évidemment certain']),
               dict(pdf=BOU, page=PQ['bouali2023-enjeux-03'].get('pdf_page') or None, from_=PQ['bouali2023-enjeux-03']['from_'], to=PQ['bouali2023-enjeux-03']['to'], keys=PQ['bouali2023-enjeux-03']['keys'], alts=PQ['bouali2023-enjeux-03']['alts'])],
 'QC-weil': spec(f'{SP}/V/q2/historischkriti00weilgoog.pdf', ['weil_uthman_varianten', 'weil_nach_othman_keine_veraenderungen', 'weil_abu_bekr_interpoliert'], lang='Fraktur', ocr=True, pages=[80, 82, 121], dpi=250),
 'QC-neu07': spec(f'{SP}/Q3/dl/pageplace_preview_studien2007.pdf', ['q3-s2007-01', 'q3-s2007-02', 'q3-s2007-03', 'q3-s2007-04'], lang='deu', ocr=True),
 'QC-jeffery': spec(f'{SP}/Q5/dl/jeffery1937_img.pdf', ['q5-jeffery1937-02', 'q5-jeffery1937-03', 'q5-jeffery1937-05', 'q5-jeffery1937-07'], lang='eng', ocr=True),
}
T.update({k: v for k, v in EXTRA.items() if not ONLY or k in ONLY})
if T: qccap.run(T)
