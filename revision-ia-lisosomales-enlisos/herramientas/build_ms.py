# -*- coding: utf-8 -*-
"""Genera el manuscrito en Word según las normas de en-LISOS y un informe de recuento de palabras y referencias."""
import re, sys, json
import msbuild as M, ms_content as C
from docx.shared import Pt, Cm
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
keys = lambda rows: [k for r in rows for cell in r for m in M.CITE.finditer(str(cell)) for k in m.group(1).split(',')]
t1keys = [r[-1].rstrip('*') for r in C.T1_ROWS]
texto = C.INTRO + [p for _, ps in C.DESARROLLO for p in ps] + C.CONCLUSIONES
en_texto = set(keys([[p] for p in texto]))
solo = lambda ks: [k for k in dict.fromkeys(ks) if k not in en_texto]   # citas que solo aparecen en la tabla
R = M.Refs(extra=C.EXTRA, table_keys={'T1': solo(t1keys), 'T2': solo(keys(C.T2_ROWS))})
body = []   # (tipo, texto ya numerado)
for p in C.INTRO: body.append(('p', R.render(p)))
dev = []
for h, ps in C.DESARROLLO: dev.append((h, [R.render(p) for p in ps]))
concl = [R.render(p) for p in C.CONCLUSIONES]
t1 = [list(r[:-1]) + [R.compact([R.num(r[-1].rstrip('*'))]).strip('[]') + ('*' if r[-1].endswith('*') else '')] for r in C.T1_ROWS]
t2 = [[R.render(c) for c in r] for r in C.T2_ROWS]
refs = R.listing()
# ---- recuento
wc = {'Introducción': sum(M.words(p) for p in C.INTRO)}
for h, ps in C.DESARROLLO: wc[h] = sum(M.words(p) for p in ps)
wc['Conclusiones'] = sum(M.words(p) for p in C.CONCLUSIONES)
tot = sum(wc.values()); wr = sum(M.words(t) for _, t in C.RESUMEN); wa = sum(M.words(t) for _, t in C.ABSTRACT)
rep = {'palabras_por_seccion': wc, 'cuerpo': tot, 'resumen': wr, 'abstract': wa, 'referencias': len(refs), 'orden': R.order}
json.dump(rep, open(OUT + '/recuento.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in rep.items() if k != 'orden'}, ensure_ascii=False, indent=1))
# ---- Word
d = M.new_doc()
# PARTE 1
M.para(d, 'PRIMERA PARTE', bold=True); M.para(d, 'Tipo de artículo: Revisión')
M.para(d, '**Título:** ' + C.TITULO); M.para(d, '**Título en inglés:** ' + C.TITLE_EN); M.para(d, '**Título abreviado:** ' + C.TITULO_CORTO)
for lab, ph in (('Autores', '[Nombre y apellidos de cada autor, en el orden de firma]'), ('Departamentos e instituciones', '[Servicio o departamento, institución, ciudad y país de cada autor]'),
                ('Autor responsable de la correspondencia', '[Nombre, dirección postal y correo electrónico]'), ('Agradecimientos', '[Completar o indicar «Ninguno»]'),
                ('Financiación', '[Indicar las ayudas recibidas o «Este trabajo no ha recibido financiación específica»]'), ('Conflictos de intereses', '[Declarar los de cada autor o «Los autores declaran no tener conflictos de intereses»]')):
    M.para(d, f'**{lab}:** {ph}')
M.para(d, '**Uso de inteligencia artificial en la preparación del manuscrito:** [Texto propuesto, que los autores deben revisar y adaptar] En la preparación de este trabajo se utilizó un asistente de inteligencia artificial generativa (Claude, Anthropic) para la búsqueda bibliográfica en bases de datos públicas, la extracción de datos de los artículos, la redacción del borrador y la elaboración de las figuras mediante programación. Los autores han revisado y verificado el contenido y asumen toda la responsabilidad sobre él.')
M.para(d, f'**Recuento:** resumen, {wr} palabras; abstract, {wa} palabras; texto, {tot} palabras; {len(refs)} referencias; 2 tablas; 2 figuras.')
M.page_break(d)
# PARTE 2
M.para(d, 'SEGUNDA PARTE', bold=True); M.para(d, C.TITULO, bold=True)
d.add_heading('Resumen', 1)
for lab, t in C.RESUMEN: M.para(d, f'**{lab}.** {t}')
M.para(d, '**Palabras clave:** ' + C.PALABRAS_CLAVE)
M.page_break(d); d.add_heading('Abstract', 1)
for lab, t in C.ABSTRACT: M.para(d, f'**{lab}.** {t}')
M.para(d, '**Keywords:** ' + C.KEYWORDS)
M.page_break(d); d.add_heading('Introducción', 1)
for _, t in body: M.para(d, t)
M.page_break(d); d.add_heading('Desarrollo', 1)
for h, ps in dev:
    d.add_heading(h, 2)
    for t in ps: M.para(d, t)
M.page_break(d); d.add_heading('Conclusiones', 1)
for t in concl: M.para(d, t)
M.page_break(d); d.add_heading('Bibliografía', 1)
for i, r in enumerate(refs): M.para(d, f'{i + 1}. {r}')
# PARTE 3
M.landscape_section(d); M.para(d, 'TERCERA PARTE', bold=True); M.para(d, C.T1_TITULO, bold=True)
M.table(d, C.T1_HEAD, t1, [2.4, 3.2, 3.6, 3.0, 3.0, 5.6, 2.9, 1.4], size=9); M.para(d, C.T1_PIE, size=9)
M.page_break(d); M.para(d, C.T2_TITULO, bold=True)
M.table(d, C.T2_HEAD, t2, [3.2, 7.0, 7.2, 7.7], size=9); M.para(d, C.T2_PIE, size=9)
M.portrait_section(d); d.add_heading('Pies de figura', 1); M.para(d, C.FIG1_PIE); M.page_break(d); M.para(d, C.FIG2_PIE)
M.para(d, 'Las figuras se envían en archivos independientes: Figura_1.pdf, Figura_1.jpg, Figura_2.pdf y Figura_2.jpg.')
d.save(OUT + '/Manuscrito_IA_enfermedades_lisosomales_enLISOS.docx')
open(OUT + '/referencias.txt', 'w', encoding='utf8').write('\n'.join(f'{i + 1}. {r}' for i, r in enumerate(refs)))
