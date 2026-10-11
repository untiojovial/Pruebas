# -*- coding: utf-8 -*-
from nqcards_a import NQA
from nqcards_b import NQB, NQC
from nqcards_d import NQD, NQE
from nqcards_f import NQF, NQG
from nqcards_h import NQH
NQCARDS = NQA + NQB + NQC + NQD + NQE + NQF + NQG + NQH
if __name__ == '__main__':
    ids = [c['id'] for c in NQCARDS]
    assert len(ids) == len(set(ids)), 'ids repetidos'
    assert ids == ['NQ%02d' % i for i in range(1, len(ids) + 1)], ids
    print(len(ids), 'tarjetas')
