# Escaneos con resaltado. Sayf: islamland 35696.pdf = archive.org 20220829_20220829_1712 (ed. al-Samarrai, 2.ª impr. 1418/1997).
# Eutiquio (Ibn al-Bitriq): archive.org annaleseuty00euty, ed. Cheikho (CSCO), p. 126.
from scanhl import run
P = 'scan/ridda-%d.png'
EB = [(289, 337), (360, 404), (427, 473), (498, 543)]
SCANS = {
 'TS1': [dict(img=P % 136, first=6, last=13, hl=[(7, 120, 1300, 'key'), (8, 960, 1300, 'key'), (11, 140, 1105, 'key')])],
 'TS2': [dict(img=P % 138, first=6, last=14, hl=[(11, 555, 1300, 'key'), (12, 120, 1300, 'key'), (13, 1105, 1300, 'key'), (13, 655, 1100, 'alt')])],
 'TS3': [dict(img=P % 136, first=19, last=25, hl=[(20, 1025, 1300, 'key'), (23, 555, 1170, 'alt')])],
 'TE1': [dict(img='scan/eut-126.jpg', B=EB, first=0, last=3, xl=70, xr=1300, hl=[(2, 70, 850, 'key'), (3, 740, 1300, 'key')])],
}
run(SCANS)
