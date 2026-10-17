# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/it')
import itdata1 as A, itdata2 as B
FIGS = [A.IT01, A.IT02, A.IT03, A.IT04, A.IT05, A.IT06, B.IT07, B.IT08, B.IT09, B.IT10, B.IT11, B.IT12]
for i, f in enumerate(FIGS, 1):
    f['id'] = f'IT{i:02d}'
    f['slug'] = f['id'].lower()
    for q in f['quotes']: q.setdefault('verdict', None)
