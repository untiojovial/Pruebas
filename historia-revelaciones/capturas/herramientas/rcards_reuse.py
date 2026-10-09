# -*- coding: utf-8 -*-
# Tarjetas ya capturadas en packs anteriores que entran en el pack histórico.
import copy
import zcards_data as _z, hcards_data as _h, kcards_data as _k

_SRC = {c['id']: c for c in _z.ZCARDS + _h.HCARDS + _k.KCARDS}


def reuse(src, **kw):
    c = copy.deepcopy(_SRC[src])
    c['specs'] = c.get('specs') or [src]
    for k in ('year', 'who', 'postura', 'chip'):
        c.pop(k, None)
    c['uso'] = f'Ya capturada como {src} en un pack anterior; aquí se reutiliza.'
    c.update(kw)
    c['orig'] = src
    return c


REUSE = {
    'K01': lambda **kw: reuse('K01', **kw),
    'H11b': lambda **kw: reuse('H11b', **kw),
    'H11c': lambda **kw: reuse('H11c', **kw),
    'H10a': lambda **kw: reuse('H10a', **kw),
    'Z14': lambda **kw: reuse('Z14', **kw),
    'Z22': lambda **kw: reuse('Z22', **kw),
    'Z26': lambda **kw: reuse('Z26', **kw),
    'Z27': lambda **kw: reuse('Z27', **kw),
}
