# -*- coding: utf-8 -*-
# Packages the Simonis & Milutin short reply into the repository
import os, shutil, glob
from PIL import Image
SM = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/sm'
AY = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ay'
HB = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb'
R = '/home/user/Pruebas/simonis-milutin-1299-respuesta-breve'
os.chdir(SM)
for d in ('', '/herramientas', '/herramientas/briefs_agentes', '/herramientas/datos_agentes', '/herramientas/paginas_bonn'):
    os.makedirs(R + d, exist_ok=True)
files = [f'SM0{i}.png' for i in range(1, 7)]
for f in files:
    shutil.copy('smcards/' + f, R + '/' + f)
for t in ('smgen.py', 'packsm.py', 'gen.py'):
    shutil.copy(t, R + '/herramientas/' + t)
shutil.copy(AY + '/renderhb.js', R + '/herramientas/renderhb.js')
for t in ('hbcss.py', 'genpad.py'):
    shutil.copy(f'{HB}/{t}', R + '/herramientas/' + t)
shutil.copy('guide.txt', R + '/herramientas/guia_pegada_con_las_fotos.txt')
for s in ('S1', 'S2', 'S3', 'S4'):
    shutil.copy(f'{s}.txt', R + f'/herramientas/briefs_agentes/{s}.txt')
    for n in ('passages.json', 'notes.md'):
        if os.path.exists(f'{s}/{n}'):
            shutil.copy(f'{s}/{n}', R + f'/herramientas/datos_agentes/{s}_{n}')
pages = {'gr203_204_greek.png': 'Gregoras VI.9-10, Bonn I pp. 203-204 (lower half of p. 203 and p. 204 top)',
         'gr348_top.png': 'Gregoras VII.5, Bonn I p. 243 (top)',
         'p273_a.png': 'Pachymeres, Bonn II p. 273 (top)',
         'p273_b.png': 'Pachymeres, Bonn II p. 273 (bottom)',
         'p275_top.png': 'Pachymeres, Bonn II p. 275 (top, section 31)',
         'p279_a.png': 'Pachymeres, Bonn II p. 279 (top)',
         'p280_a.png': 'Pachymeres, Bonn II p. 280 (top)',
         'p285_a.png': 'Pachymeres, Bonn II p. 285 (top)'}
for f in pages:
    shutil.copy('S1/dl/img/' + f, R + '/herramientas/paginas_bonn/' + f)
open(R + '/herramientas/paginas_bonn/LEEME.txt', 'w', encoding='utf-8').write(
    'Crops of the page images I read (Google scans of the Bonn editions on archive.org: nicephorigregor00bekkgoog and georgiipachymer00pousgoog; 1829 and 1835, public domain).\n\n' +
    '\n'.join(f'{k}: {v}' for k, v in pages.items()) + '\n')

def pdf(name, w, q):
    ims = []
    for f in files:
        im = Image.open('smcards/' + f).convert('RGB')
        if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        ims.append(im)
    ims[0].save(R + '/' + name, save_all=True, append_images=ims[1:], resolution=120, quality=q)
    return os.path.getsize(R + '/' + name) / 1e6
PDF = 'simonis_milutin_1299_short_reply.pdf'
mb = pdf(PDF, 1200, 72)
print('pdf MB', mb)
assert mb < 30

README = f'''# Simonis and Milutin (1299): a short reply to two book pages

Six slides (English) answering two photographed book pages: Kaldellis, *A Cabinet of Byzantine Curiosities* (Oxford UP), p. 12, and Fine, *The Late Medieval Balkans* (Univ. of Michigan Press), p. 222, together with the AI-written guide that came with the photos. Every claim in that guide was checked by four small research agents and then re-checked by me on the page images where it mattered; the slides say what held, what was corrected and what could not be verified. One PDF: [`{PDF}`]({PDF}) ({mb:.1f} MB).

| Slide | Content |
|---|---|
| [SM01](SM01.png) | The short reply, what the sources do and do not establish, and the fair concessions |
| [SM02](SM02.png) | The two pages transcribed, with the words that matter marked and a close reading |
| [SM03](SM03.png) | Pachymeres and Gregoras in Greek with my English: the loophole, her age, the patriarch bypassed, the plan to wait, the abuse allegation |
| [SM04](SM04.png) | Byzantine law and canons on age (Justinian, Ecloga, Prochiron, Milaš, Meyendorff, Tome of Union), each with its check status |
| [SM05](SM05.png) | Milutin the saint, the syllogism, and the Aisha comparison (Ibn Hazm and Ibn Shubruma) |
| [SM06](SM06.png) | Corrections to the guide, what was not verified, limits |

## Result in a few lines

- The marriage is real: Simonis was five when offered (Gregoras: "in her fifth year"; Pachymeres: "not yet past her sixth year"). Both books say it broke Church rules or canons, and that the court got round the objection with a loophole about Milutin's earlier marriages (Pachymeres states the same argument, p. 273).
- The loophole answers only the fourth-marriage objection. For her age the recorded plan was to raise her in his household "until the customary time of marriage" (Gregoras VI.9). Pachymeres lists her immaturity among the obstacles and says the patriarch was not consulted.
- Every age rule I could read (Justinian 12/14, Ecloga 13/15, Milaš 14/12) was above five; Meyendorff concedes that "diplomatic requirements sometimes made this rule flexible" and cites Simonis as the example.
- The only source I found for abuse is Gregoras (VII.5, p. 243): age eight, womb injured, no date for the wedding. Kaldellis' "immediately" is not in it.
- Milutin is venerated as a saint, and the Church did give way. So "the Church rejected it entirely" is too strong; the surviving claim is that this was a rulers' act, not a Christian norm.

## Corrections to the pasted guide

Justinian's ages are in *Inst.* 1.22 pr. (and *Dig.* 23.2.4), not 1.10. The Prochiron "12/14" is not confirmed. "Wait until twelve" is not in Gregoras. Gregoras gives Milutin's age as forty, not fifty, and the eight-year-old claim is not dated to the wedding. Milaš' "Prochiron IV,2" cite points to a chapter on dowry. Failler's reported statement that the conflict continued after the ceremony, and Kosmas' resignation, could not be verified.

## Not verified / limits

- Fine p. 222 and Kaldellis p. 12 were read only from the photos (which carry a TikTok watermark and are not redistributed here); Kaldellis' endnote is not visible.
- Not obtained: Georgievska-Shine (1993), Failler (1990); Lascaratos and Poulakou-Rebelakou (2000) abstract only (it does not name Simonis). Not read: Prochiron title II, the Greek of the Tome of Union, Danilo II's *Life of Milutin*, Metochites' account.
- Negative result: no Orthodox canon or text found citing Simonis as precedent (limited search, poor OCR).
- Greek read on the Bonn page images (pp. 203-204, 243, 273, 275, 279-280, 285), crops in `herramientas/paginas_bonn/`; the smudge on p. 243 hides two letters of "forty". Translations are mine. Pachymeres' book number is ambiguous in the scans, so pages are cited.
- OCA, OrthodoxWiki, Wikipedia and a Serbian state portal are secondary; Milutin's death is dated 1320 or 1321. Ibn Hazm's page numbers (*al-Muhalla* vol. 9, pp. 38-40) are deduced from OpenITI markers.
- Four small AI research agents (S1 primary sources, S2 scholarship, S3 law and canons, S4 Church attitude and sainthood) gathered the material; their briefs and returns are in `herramientas/`.

## Resumen (ES)

PDF corto en inglés (6 diapositivas) que responde a las dos páginas fotografiadas y a la guía pegada. La boda es un hecho; las dos páginas dicen que violó las reglas de la Iglesia y que la corte usó una argucia sobre los matrimonios anteriores; las leyes bizantinas fijaban 12/14 (Justiniano) y 13/15 (Écloga); Grégoras sitúa el abuso a los ocho años, sin fechar la boda. La Iglesia cedió y Milutin es santo: lo que no se sostiene es que fuera doctrina. La guía tenía varios errores (ver SM06). No pude verificar Failler 1990, Georgievska-Shine 1993, el Prochiron (título II) ni la nota de Kaldellis.

## Tools

`herramientas/`: `gen.py` (briefs), `smgen.py` (slides), `renderhb.js` (PNG; needs Playwright), `hbcss.py` and `genpad.py` (base CSS), `packsm.py` (this packaging), `briefs_agentes/`, `datos_agentes/` (S1-S4 passages and notes), `paginas_bonn/` (page crops), `guia_pegada_con_las_fotos.txt` (the guide, original Spanish text).
'''
open(R + '/README.md', 'w', encoding='utf-8').write(README)
print('ok')
