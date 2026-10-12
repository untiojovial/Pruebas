import json,sys
n=sys.argv[1]; ids=sys.argv[2:] 
p=json.load(open(f'H{n}/passages.json'))
for x in p:
    if ids and not any(x.get('id','').startswith(i) for i in ids): continue
    print('---',x.get('id'),x.get('theme'),'|',x.get('work'),'|',x.get('ref'),'|',x.get('url'))
    print(x.get('quote_en',''))
    print('NOTE:',str(x.get('note') or x.get('context') or '')[:500])
