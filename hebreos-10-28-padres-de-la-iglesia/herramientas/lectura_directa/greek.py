# -*- coding: utf-8 -*-
import sys
F={'Mt':'61-Mt','Lk':'63-Lk','Jn':'64-Jn','Ro':'66-Ro','1Co':'67-1Co','2Co':'68-2Co','Ga':'69-Ga','2Ti':'76-2Ti','Tit':'77-Tit','Heb':'79-Heb'}
D='/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb/V/'
def verses(book):
    V={}
    for l in open(D+f'mg_{F[book]}.txt',encoding='utf-8'):
        p=l.split()
        if len(p)<4: continue
        ref=p[0]; ch=int(ref[2:4]); v=int(ref[4:6]); V.setdefault((ch,v),[]).append(p[3])
    return {k:' '.join(w) for k,w in V.items()}
def g(book,ch,a,b=None):
    V=verses(book); b=b or a
    return ' '.join(f'{v} '+V[(ch,v)] for v in range(a,b+1))
if __name__=='__main__':
    for spec in sys.argv[1:]:
        book,rest=spec.split(' ',1) if ' ' in spec else spec.split(':')[:1]+[spec.split(':',1)[1]]
        ch,vs=rest.split(':'); a,_,b=vs.partition('-')
        print(spec,'→',g(book,int(ch),int(a),int(b) if b else None)); print()
