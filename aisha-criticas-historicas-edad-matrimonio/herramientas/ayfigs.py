# -*- coding: utf-8 -*-
# Reúne las figuras en orden cronológico y les asigna AE01…
import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ay')
from aydata import FIGS as A
ORDER = ['ibn-shubruma', 'kindi', 'riccoldo', 'pascual', 'juan-andres', 'prideaux']
_all = {f['slug']: f for f in A}
assert set(_all) == set(ORDER), set(_all) ^ set(ORDER)
FIGS = []
for i, s in enumerate(ORDER, 1):
    f = _all[s]; f['id'] = f'AE{i:02d}'; FIGS.append(f)
