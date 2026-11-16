# -*- coding: utf-8 -*-
"""Motor del manuscrito: numera las citas por orden de aparición (formato de en-LISOS: [1-3,6]),
da formato Vancouver/ICMJE a las referencias a partir de PubMed y escribe el Word (Arial 11, doble espacio).

En el texto, una cita se escribe {{clave}} o {{clave1,clave2}}; la clave es un PMID o una clave de EXTRA (referencias sin PMID).
Las citas de una tabla se numeran en el punto en que la tabla se menciona por primera vez en el texto ({{T1}}, {{T2}}).
"""
import re, json, os
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_BREAK, WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import pm

CITE = re.compile(r'\{\{([^{}]+)\}\}')


def vancouver(r):
    au = r['authors']
    a = ', '.join(au[:6]) + (', et al' if len(au) > 6 else '')
    t = r['title'].strip()
    if not t.endswith(('.', '?', '!')): t += '.'
    s = f"{a}. {t} {r['journal']}. {r['year']}"
    if r['volume']: s += f";{r['volume']}" + (f"({r['issue']})" if r['issue'] else '')
    if r['pages']: s += f":{r['pages']}"
    s += '.'
    if r['doi']: s += f" doi: {r['doi']}"
    return s


class Refs:
    def __init__(self, extra=None, table_keys=None):
        self.order = []; self.extra = extra or {}; self.table_keys = table_keys or {}

    def num(self, key):
        key = key.strip()
        if key not in self.order: self.order.append(key)
        return self.order.index(key) + 1

    @staticmethod
    def compact(nums):
        nums = sorted(set(nums)); out = []; i = 0
        while i < len(nums):
            j = i
            while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1: j += 1
            out.append(str(nums[i]) if j == i else (f'{nums[i]}-{nums[j]}' if j - i >= 2 else f'{nums[i]},{nums[j]}'))
            i = j + 1
        return '[' + ','.join(out) + ']'

    def render(self, text):
        def sub(m):
            keys = [k.strip() for k in m.group(1).split(',')]
            if len(keys) == 1 and keys[0] in self.table_keys:      # primera mención de una tabla: numera sus citas aquí
                for k in self.table_keys[keys[0]]: self.num(k)
                return ''
            return self.compact([self.num(k) for k in keys])
        t = CITE.sub(sub, text)
        return re.sub(r'\s+([.,;:])', r'\1', t).replace('  ', ' ')

    def listing(self):
        pmids = [k for k in self.order if k.isdigit()]
        recs = {r['pmid']: r for r in pm.records(pmids)} if pmids else {}
        out = []
        for k in self.order:
            if k.isdigit():
                if k not in recs: raise SystemExit('PMID no encontrado en PubMed: ' + k)
                out.append(vancouver(recs[k]))
            else:
                out.append(self.extra[k])
        return out


def words(text):
    return len(re.findall(r"[0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ%+\-]+", CITE.sub('', text)))


# ------------------------------------------------------------------ Word
def new_doc():
    d = Document(); s = d.sections[0]
    s.page_width, s.page_height = Cm(21.0), Cm(29.7)
    for m in ('left_margin', 'right_margin', 'top_margin', 'bottom_margin'): setattr(s, m, Cm(2.5))
    for name in ('Normal', 'Heading 1', 'Heading 2', 'Title'):
        st = d.styles[name]; st.font.name = 'Arial'; st.font.size = Pt(11)
        rf = st.element.get_or_add_rPr().get_or_add_rFonts()
        for a in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'): rf.set(qn(a), 'Arial')
        st.font.color.rgb = None
    pf = d.styles['Normal'].paragraph_format; pf.line_spacing = 2.0; pf.space_after = Pt(0); pf.space_before = Pt(0)
    for name, size in (('Heading 1', 12), ('Heading 2', 11), ('Title', 14)):
        st = d.styles[name]; st.font.size = Pt(size); st.font.bold = True; st.font.italic = False
        st.paragraph_format.line_spacing = 2.0; st.paragraph_format.space_before = Pt(0); st.paragraph_format.space_after = Pt(0); st.paragraph_format.keep_with_next = True
    # numeración de páginas al pie
    p = s.footer.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for tag, txt in (('begin', None), (None, 'PAGE'), ('end', None)):
        r = p.add_run()
        if tag:
            f = OxmlElement('w:fldChar'); f.set(qn('w:fldCharType'), tag); r._r.append(f)
        else:
            i = OxmlElement('w:instrText'); i.set(qn('xml:space'), 'preserve'); i.text = txt; r._r.append(i)
    return d


def add_rich(p, text, size=None, bold=None):
    """Texto con **negrita** y *cursiva* sencillas."""
    for part in re.split(r'(\*\*[^*]+\*\*|\*[^*]+\*)', text):
        if not part: continue
        if part.startswith('**'): r = p.add_run(part[2:-2]); r.bold = True
        elif part.startswith('*'): r = p.add_run(part[1:-1]); r.italic = True
        else: r = p.add_run(part)
        if bold: r.bold = True
        if size: r.font.size = Pt(size)
    return p


def para(d, text, style=None, align=None, **k):
    p = d.add_paragraph(style=style) if style else d.add_paragraph()
    add_rich(p, text, **k)
    if align == 'center': p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    return p


def page_break(d):
    d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def landscape_section(d):
    s = d.add_section(WD_SECTION.NEW_PAGE); s.orientation = WD_ORIENT.LANDSCAPE; s.page_width, s.page_height = Cm(29.7), Cm(21.0)
    for m in ('left_margin', 'right_margin', 'top_margin', 'bottom_margin'): setattr(s, m, Cm(2.0))
    return s


def portrait_section(d):
    s = d.add_section(WD_SECTION.NEW_PAGE); s.orientation = WD_ORIENT.PORTRAIT; s.page_width, s.page_height = Cm(21.0), Cm(29.7)
    for m in ('left_margin', 'right_margin', 'top_margin', 'bottom_margin'): setattr(s, m, Cm(2.5))
    return s


def table(d, header, rows, widths_cm, size=9, spacing=2.0):
    t = d.add_table(rows=1, cols=len(header)); t.style = 'Table Grid'; t.autofit = False
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); t._tbl.tblPr.append(lay)
    def fill(cell, text, bold=False):
        cell.text = ''; p = cell.paragraphs[0]; p.paragraph_format.line_spacing = spacing
        add_rich(p, str(text), size=size, bold=bold)
    for i, h in enumerate(header): fill(t.rows[0].cells[i], h, True)
    # repetir la fila de encabezado en cada página
    trPr = t.rows[0]._tr.get_or_add_trPr(); th = OxmlElement('w:tblHeader'); th.set(qn('w:val'), 'true'); trPr.append(th)
    for row in rows:
        cells = t.add_row().cells
        for i, x in enumerate(row): fill(cells[i], x)
    for i, gc in enumerate(t._tbl.tblGrid.findall(qn('w:gridCol'))): gc.set(qn('w:w'), str(int(widths_cm[i] * 567)))
    for r in t.rows:
        for i, c in enumerate(r.cells): c.width = Cm(widths_cm[i])
    return t
