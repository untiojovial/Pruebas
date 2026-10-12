# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from qcc_a import QCA
from qcc_b import QCB
from qcc_c import QCC
from qcc_d import QCD
QCCARDS = sorted(QCA + QCB + QCC + QCD, key=lambda c: c['id'])
