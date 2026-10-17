# -*- coding: utf-8 -*-
# Fichas de las obras, ediciones y utilidades para armar las citas
import sys, os
IT = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/it'
sys.path.insert(0, IT)
import itsrc, itlib, itpages, re
BK = {
 'jawab': dict(ar='الجواب الصحيح لمن بدل دين المسيح', lat='Al-Jawab al-Sahih li-man baddala din al-Masih', es='Al-Jawab al-Sahih li-man baddala din al-Masih («La respuesta correcta a quienes cambiaron la religión de Cristo»)', ed="Dar al-'Asima, Arabia Saudí, 2.ª ed., 1419 H/1999, 6 vols. · OpenITI Shamela0000170", short='Al-Jawab al-Sahih', key='JawabSahih'),
 'dar': dict(ar='درء تعارض العقل والنقل', lat="Dar' ta'arud al-'aql wa'l-naql", es="Dar' ta'arud al-'aql wa'l-naql («Evitar la contradicción entre razón y revelación»)", ed="Dar al-Kutub al-'Ilmiyya, Beirut, 1417 H/1997 (ed. 'Abd al-Latif 'Abd al-Rahman) · OpenITI ShamAY0033865", short="Dar' ta'arud", key='DarTacarud'),
 'maj': dict(ar='مجموع الفتاوى', lat="Majmu' al-Fatawa", es="Majmu' al-Fatawa («Recopilación de fatuas»)", ed="ed. 'Abd al-Rahman b. Qasim, Maŷma' al-Malik Fahd, Medina, 1416 H/1995 · OpenITI Shamela0007289", short="Majmu' al-Fatawa", key='MajmucFatawa'),
 'radd': dict(ar='الرد على المنطقيين', lat="Al-Radd 'ala al-mantiqiyyin", es="Al-Radd 'ala al-mantiqiyyin («Refutación de los lógicos»)", ed="Dar al-Ma'rifa, Beirut (la cabecera de OpenITI no da editor ni fecha) · OpenITI Shamela0007626", short="Al-Radd 'ala al-mantiqiyyin", key='RaddCalaMantiqiyyin'),
 'wasit': dict(ar='العقيدة الواسطية', lat="Al-'Aqida al-Wasitiyya", es="Al-'Aqida al-Wasitiyya («El credo de Wasit»)", ed="Maktabat al-Ma'arif, Riad, con comentario de Ibn Mani' (sin fecha) · OpenITI Sham19Y0018098", short="Al-'Aqida al-Wasitiyya", key='CaqidaWasitiyya'),
 'tadm': dict(ar='الرسالة التدمرية', lat='Al-Risala al-Tadmuriyya', es='Al-Risala al-Tadmuriyya («La epístola de Tadmur»)', ed="Maktabat al-'Ubaykan, Riad, 6.ª ed., 1421 H/2000 (ed. Muhammad b. 'Awda al-Sa'wi) · OpenITI Shamela0022666", short='Al-Tadmuriyya', key='RisalaTadmuriyya'),
 'isf': dict(ar='شرح العقيدة الأصفهانية', lat="Sharh al-'Aqida al-Isfahaniyya", es="Sharh al-'Aqida al-Isfahaniyya («Comentario al credo de Isfahan»)", ed="Dar al-Minhaj, Riad, 1.ª ed., 1430 H (ed. Muhammad b. 'Awda al-Sa'wi) · OpenITI ShamAY0034392", short="Sharh al-Isfahaniyya", key='SharhCaqidaIsfahaniyya'),
}
KEY2BK = {v['key']: k for k, v in BK.items()}
KEY2BK.update({'wasitiyya': 'wasit', 'tadmuriyya': 'tadm', 'isfahaniyya': 'isf', 'majmu': 'maj', 'jawab': 'jawab', 'dartacarud': 'dar'})
def url_of(bk):
    vs = itlib.versions(BK[bk]['key']); vs.sort(key=lambda v: -v[1]); return vs[0][2]
DATE = 'ss. XIII–XIV · árabe'
def vp_es(vp):
    return vp.replace('vol.', 'vol.').replace('p.', 'p.') if vp else ''
def pagefix(bk, text, hint=None):
    """Página impresa del pasaje: el marcador de OpenITI cierra la página (comprobado en Al-Jawab al-Sahih), así que la página es marcador+1."""
    hits = [h for h in itpages.pages(BK[bk]['key'], text) if h]
    m = re.match(r'vol\. (\d+), p\. (\d+)', hint or '')
    if m and len(hits) > 1:
        v, p = int(m.group(1)), int(m.group(2))
        hits.sort(key=lambda h: abs(h[1] - p) if h[0] == v else 10**9)
    return itpages.fmt(hits[0]) if hits else hint
JAWAB_IMG = " · cotejado con la página escaneada de la edición"
def Q(pid, bk=None, es='', clar='', theme=(), verdict=None, vtxt=None, christian=None, start=None, end=None, text=None, vol_page=None, date=DATE, url=None, corr=None):
    """Arma una cita: árabe literal (por código) + datos; 'christian' = dict(head, txt, orig, src)."""
    x = itsrc.P.get(pid) if pid else None
    if bk is None: bk = KEY2BK[x['work']]
    if text is None:
        text = itsrc.ar(pid, start, end)
    assert itsrc.check(pid, text) if (pid and x and x.get('ar') and x['work'] in itsrc.BOOK) else True, pid
    vp = pagefix(bk, text, vol_page or (x['vol_page'] if x else None))
    note = JAWAB_IMG if bk == 'jawab' else ''
    for old, new in (corr or []):
        assert old in text, old
        text = text.replace(old, new); note += f' · una letra corregida según la página impresa («{old}» → «{new}»; el texto de OpenITI trae un error)'
    return dict(theme=list(theme), es=es, work=BK[bk]['es'], date=date, ref=f"{BK[bk]['short']}, {vp}", trans=f"Texto digitalizado de OpenITI (copia de Shamela) · edición: {BK[bk]['ed'].split(' · OpenITI')[0]}{note}", url=url or (x.get('openiti_url') if x and x.get('openiti_url') else url_of(bk)), ar=text, clar=clar, verdict=verdict, vtxt=vtxt, christian=christian, _bk=bk)
def SP(bk, start, end, **kw):
    """Cita por intervalo literal en el libro (frases inicial y final incluidas)."""
    work = BK[bk]['key']
    text = itsrc.span(work, start, end)
    d = Q(None, bk=bk, text=text, **kw)
    return d
def F(id, name, block, role, why, bks, foot, quotes, dates=None):
    works = [dict(ar=BK[b]['ar'], lat=BK[b]['lat'], ed=BK[b]['ed']) for b in bks]
    return dict(id=id, name=name, dates=dates or block, block=block, role=role, why=why, works=works, foot=foot, quotes=quotes)
FOOT = "Árabe copiado por código del texto de OpenITI (digitalización de Shamela) y limpiado de marcas editoriales; traducción al español mía. Página impresa deducida de los marcadores de OpenITI (el marcador cierra la página); la tarjeta indica las citas cotejadas con el escaneo de la edición."
