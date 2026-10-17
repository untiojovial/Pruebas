# -*- coding: utf-8 -*-
# Reúne las diez figuras en orden cronológico y les asigna OI01–OI10.
import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ox')
from oxdata import FIGS as A
from oxdata_extra import EXTRA as B
from oxdata_extra2 import EXTRA2 as C
ORDER = ['zigabeno', 'zonaras', 'glykas', 'choniates', 'cantacuzeno', 'palamas', 'manuel-ii', 'simeon-tesalonica', 'maximo-griego', 'melisseno']
_all = {f['slug']: f for f in A + B + C}
assert set(_all) == set(ORDER), set(_all) ^ set(ORDER)
FIGS = []
for i, s in enumerate(ORDER, 1):
    f = _all[s]; f['id'] = f'OI{i:02d}'; FIGS.append(f)
