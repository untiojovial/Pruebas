import json
ALL={}
for k in range(1,12):
    d=json.load(open(f'/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/tq/T{k}/passages.json'))
    for i,p in enumerate(d):
        pid=p.get('id') or f'T{k}-{i+1:02d}'
        p['id']=pid; ALL[pid]=p
