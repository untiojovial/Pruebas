import json,sys
a=sys.argv[1]; ids=sys.argv[2:]
W={w['id']:w for w in json.load(open(f'{a}/works.json',encoding='utf-8'))}
for p in json.load(open(f'{a}/passages.json',encoding='utf-8')):
    if ids and p['id'] not in ids: continue
    w=W.get(p.get('work'),{})
    print('=====',p['id'],'|',p.get('ref'))
    print('URL:',p.get('url'))
    print('ORIG_URL:',p.get('orig_url'))
    print('WORK:',w.get('title_en') or w.get('title_orig'),'| date:',w.get('date'),'| ed_orig:',str(w.get('edition_original'))[:200],'| ed_en:',str(w.get('edition_english'))[:200],'| lic:',str(w.get('licence'))[:150])
    for k in ('quote_orig','quote_en','own_translation_en'):
        v=p.get(k)
        if v: print(k.upper()+':',v)
    print('KEYS:',p.get('keys'))
    print('SAYS:',p.get('what_it_says'))
    print('LIMITS:',p.get('limits'))
    print('LICNOTE:',p.get('licence_note'))
