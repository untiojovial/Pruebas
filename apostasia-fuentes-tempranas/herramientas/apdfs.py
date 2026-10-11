import sys
from pdfhl import run
HP = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hp'
PDV = f'{HP}/Zloc/dl/pdv.pdf'   # Peters & De Vries, «Apostasy in Islam», Die Welt des Islams 17 (1976-77): página impresa n = página PDF n+1
PDFS = {
 'AP-pdv5': [dict(pdf=PDV, page=6, from_='The punishment laid down for apostasy is the death penalty', to='not fully responsible',
                  keys=['The punishment laid down for apostasy is the death penalty'],
                  alts=['is contested by Hanafite and Shafi’ite lawyers', 'Women are “kept in hostage” instead'])],
 'AP-pdv14': [dict(pdf=PDV, page=15, from_='Though apostasy no longer falls under criminal law', to='is even more',
                   keys=['the apostate cannot be put to death on the mere ground of his apostasy'],
                   alts=['No verse in the Koran prescribes capital punishment for the apostate qua apostate']),
              dict(pdf=PDV, page=16, from_='doubtful, as they belong to the category of Traditions', to='fighting apostates',
                   keys=['they must be interpreted as referring only to the inimical and fighting apostates'],
                   alts=['relying on only one authority']),
              dict(pdf=PDV, page=16, from_='A very detailed plea against capital punishment', to='he may not be killed',
                   keys=['an isolated opinion of Ibrahim al-Nakha’i'], alts=[])],
}
run({k: v for k, v in PDFS.items() if not sys.argv[1:] or k in sys.argv[1:]})
