# -*- coding: utf-8 -*-
import sys, os, shutil, re
B = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad'
UG = B + '/hr'; UQ = B + '/hr'
sys.path.insert(0, B + '/hb'); sys.path.insert(0, UG)
import hbcss, genpad
from hbcss import E
from hrdata import S
OUT = UG + '/hrcards'; os.makedirs(OUT + '/img', exist_ok=True)
PACK = 'Pack «Hipólito de Roma, ¿trinitario? «Un solo poder, dos personas, y la tercera la gracia del Espíritu»»'
CSS = hbcss.CSS + genpad.CQ + """
.lq{border:1px solid #d6dbe4;border-radius:10px;margin:0 0 10px;background:#fff;overflow:hidden}
.lq .la{font-family:'Gentium Plus','Gentium Book Plus','DejaVu Serif','Bitstream Charter',serif;font-size:17px;line-height:1.5;color:#2f3a52;background:#f6f4ec;padding:9px 16px;border-bottom:1px solid #e3e7ee}
.lq .la.lat{font-style:italic}
.lq .la.en{font-family:'Inter',sans-serif;font-size:15px}
.lq .es{font-size:17.5px;line-height:1.5;padding:9px 16px;color:#1b2333}
.lq .rf{font-size:12.5px;color:#566079;padding:5px 16px;background:#eef1f8;line-height:1.4}
.lq .rf b{color:#14213d}
.lq .lg{font-size:11px;letter-spacing:.08em;text-transform:uppercase;font-weight:700;color:#8a6d00;margin-right:6px;font-family:'Inter',sans-serif;font-style:normal}
.lq .lg.en{color:#1d5f9a}
.rs2{border-left:6px solid #14213d;background:#eef1f8;padding:12px 20px;border-radius:0 8px 8px 0;font-size:15.5px;line-height:1.52;margin-top:8px}
.rs2 b{color:#14213d}
.capg{display:flex;gap:14px;align-items:flex-start}
.capg .c{flex:1;min-width:0;border:1px solid #cfd6e2;border-radius:8px;overflow:hidden;background:#fff}
.capg img{width:100%;display:block}
.capg .t{font-size:12.5px;line-height:1.4;color:#2f3a52;padding:6px 10px;background:#f4f5f8}
.v1{color:#1d7a4f}.v2{color:#9a6a00}.v3{color:#b44a2f}
"""
LANG = {'gr': ('Griego', 'la', ''), 'en': ('Inglés', 'la en', 'en'), 'la': ('Latín', 'la lat', '')}
def hdr(cid, tag, kind, title, ref):
    return f'<div class="hd alt"><div class="row"><div class="badge"><b>{cid}</b>{tag}</div><span class="kind es">{kind}</span></div><h1>{title}</h1><div class="row"><div class="ref">{ref}</div></div></div>'
def card(fname, head, body, foot):
    h = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="card">{head}<div class="bd">{body}</div><div class="ft"><div class="u">{foot}</div></div></div></body></html>'
    open(f'{OUT}/{fname}.html', 'w', encoding='utf-8').write(h)
def qhtml(q):
    nm, cls, lc = LANG[q['lang']]
    return f'<div class="lq"><div class="{cls}"><span class="lg {lc}">{nm}</span>{E(q["txt"])}</div><div class="es"><span class="lg" style="color:#1d7a4f">Español</span> {E(re.sub(r"<[^>]+>","",q["es"]))}</div><div class="rf"><b>{E(q["ref"])}</b> · {E(q["src"])} · <span style="color:#8a93a6">{q["id"]}</span></div></div>'
FOOT = PACK + '<br>Traducciones al español mías. Griego/latín/inglés tal como se indica en cada cita; entre corchetes […] lo omitido. Lo no verificado se dice.'
TABLE = [
 ('A · «el Padre manda, el Hijo obedece» (C. Noet. 14)', 'Se explica, con límite', 'Hipólito mismo da la razón: «por economía» se reúne en un solo Dios; Padre «sobre todos», Hijo «por todos», Espíritu «en todos». Orden de oficio; no dice «de la misma naturaleza».', 'HP06 · HP17'),
 ('B · el Verbo, «Hijo por lo que iba a ser»; no «Hijo perfecto» antes de la carne (C. Noet. 15)', 'Parcial', 'Bull: «unigénito» ya antes de la carne; plenitud de filiación en el Encarnado. Bethune-Baker y Döllinger leen un Hijo «hecho» al encarnarse: se resuelve por relectura posterior.', 'HP07 · HP17'),
 ('C · Verbo «concebido» y luego «engendrado» para crear; «engendró como quiso» (Ref. 10.33; C. Noet. 10 y 16)', 'Parcial', 'Atanasio: «era siempre»; Aquino: Verbo personal y substancial. Hipólito mismo dice que el modo no se puede explicar (C. Noet. 16). No distingue generación eterna de generación para crear.', 'HP04 · HP08 · HP17'),
 ('D · «te has hecho Dios… deificado» (Ref. 10.34)', 'Se explica', 'Don futuro y condicional («si obedeces… si quieres ser también Dios»), con el Verbo como «modelo»; el Verbo es «de la sustancia» de Dios y el hombre «de nada».', 'HP09 · HP10'),
 ('E · acusación de «ditheísmo» por Calixto (Ref. 9.11-12)', 'Se explica', 'Informes de Hipólito sobre el modalismo de Calixto (un solo prosopon); sirven para ver que distinguía Padre e Hijo; no son doctrina propia.', 'HP11'),
 ('F · «Hijo de Dios» y «Dios encarnado»; «Verbo… engendrado del corazón del Padre antes de todo»', 'Sí, con límite', 'Cristo y Anticristo 26; Daniel 3 y 7: Hijo antes de la carne, no «sin principio»; «Cristo es Dios» en Cristo y Anticristo 6 no está confirmado.', 'HP12'),
 ('G · el Espíritu: «gracia», «tercera economía», «da entendimiento»', 'Parcial', 'Nombrado con Padre e Hijo («tres», «tríada»), pero sin la personalidad de igual orden que Basilio y Gregorio expresan; el punto más débil.', 'HP03 · HP05 · HP18'),
 ('H · «un solo Dios, dos personas y la tercera», «estos son verdaderamente tres», «Cristo es el Dios sobre todo»', 'Sí', '«Ἓν ἐσμεν… δύο πρόσωπα, δύναμιν δὲ μίαν» (7); «τρία» (8); «τριάς» (14); «el Verbo es Dios, siendo ousía de Dios» (Ref. 10.33). Páginas vistas por mí (HP20-HP22).', 'HP03 · HP05 · HP09'),
]
def cls(v): return 'v1' if v.startswith('Sí') or v == 'Se explica' else ('v3' if v.startswith('No') else 'v2')
CONC = '<div class="rs2"><b>Conclusión.</b> Hipólito es un testigo temprano (c. 200-235) de la <b>estructura</b> trinitaria: «un solo Dios, dos personas y la tercera», «tres», «tríada», el Verbo «Dios… sustancia de Dios» y «Cristo, Dios sobre todo». <b>No es arriano ni modalista, pero tampoco un trinitario niceno formulado</b>: la unidad se dice «en poder» y «economía», el Espíritu es «gracia» y «tercera economía», la filiación se vincula a la encarnación, y el Verbo se «concibe» y «engendra» para crear. Defenderlo honestamente es decir esto y explicar el vocabulario del siglo III con la metafísica posterior (Tertuliano, Atanasio, Basilio, Agustín, Aquino).</div>'
for s in S:
    if s['id'] == 'HP19':
        rh = ''.join(f'<tr><td style="font-weight:700;font-size:14px">{a}</td><td class="{cls(b)}" style="font-weight:700;white-space:normal">{b}</td><td style="font-size:13.5px">{c}</td><td style="font-weight:700;white-space:nowrap;font-size:13px">{d}</td></tr>' for a, b, c, d in TABLE)
        body = f'<table class="v" style="table-layout:fixed"><tr><th style="width:310px">Pasaje difícil</th><th style="width:130px">¿Se resuelve?</th><th>Cómo</th><th style="width:130px">Diapositivas</th></tr>{rh}</table>{CONC}'
        card('HP19', hdr('HP19', 'Hipólito · mapa', 'Resumen', s['title'], s['sub']), body, FOOT); continue
    body = ''.join(qhtml(q) for q in s['quotes']) + f'<div class="rs2">{s["res"]}</div>'
    card(s['id'], hdr(s['id'], 'Hipólito', 'Cita y resolución', s['title'], s['sub']), body, FOOT)
def cap(fn, cid, title, items, note, ref):
    g = ''
    for i, (img, t) in enumerate(items):
        shutil.copy(UQ + '/pg/' + img, f'{OUT}/img/{cid}_{i}.png')
        g += f'<div class="c"><img src="img/{cid}_{i}.png"><div class="t">{t}</div></div>'
    card(fn, hdr(cid, 'Páginas reales', 'Capturas', title, ref), f'<div class="capg">{g}</div><div class="rs2">{note}</div>', PACK)
cap('HP20', 'HP20', 'Páginas reales del griego (Lagarde 1858): Contra Noeto 14, pp. 52-53', [('hp52.png', '<b>Lagarde, <i>Hippolyti Romani quae feruntur omnia graece</i> (1858), p. 52</b> · azul: «el Verbo era Dios» (Jn 1:1); oro: «δύο μὲν οὐκ ἐρῶ θεοὺς ἀλλ’ ἢ ἕνα, πρόσωπα δὲ δύο, οἰκονομίᾳ δὲ τρίτην τὴν χάριν τοῦ ἁγίου πνεύματος». Abajo, las variantes del editor (l. 29: «οἰκονομία R, οἰκονομίαν cod.»).'), ('hp53.png', '<b>p. 53</b> · oro: «πατὴρ ἐντέλλεται, λόγος ἀποτελεῖ, υἱὸς δὲ δείκνυται… ὁ κελεύων πατήρ, ὁ δὲ ὑπακούων υἱός, τὸ δὲ συνετίζον ἅγιον πνεῦμα»; azul: «de otro modo no podemos pensar en un solo Dios, si no creemos de verdad en el Padre, el Hijo y el Espíritu Santo»; verde: «διὰ γὰρ τῆς τριάδος ταύτης πατὴρ δοξάζεται… πατὴρ ἠθέλησεν, υἱὸς ἐποίησεν, πνεῦμα ἐφανέρωσεν».')],
    'Escaneo con capa de texto de archive.org (Teubner, Leipzig 1858). El griego lo leí yo en la imagen. «Persona» es <i>prosopon</i>: no es la «persona» de Basilio y Gregorio. El subrayado es mío.', 'Lagarde 1858, escaneo abierto; subrayado mío')
cap('HP21', 'HP21', 'Páginas reales del griego (Lagarde 1858): Contra Noeto 10-11 y 15-16, pp. 51 y 54', [('hp51.png', '<b>Lagarde, p. 51</b> · oro (cap. 10): «καὶ φῶς ἐκ φωτὸς γεννῶν προῆκεν τῇ κτίσει κύριον τὸν ἴδιον νοῦν»; azul (cap. 11): «ἕτερον δὲ λέγων οὐ δύο θεοὺς λέγω, ἀλλ’ ὡς φῶς ἐκ φωτὸς… δύναμις γὰρ μία… ἐξ οὗ δύναμις λόγος».'), ('hp54.png', '<b>p. 54</b> · oro: «ποῖον οὖν υἱὸν ἑαυτοῦ ὁ θεὸς διὰ τῆς σαρκὸς κατέπεμψεν ἀλλ’ ἢ τὸν λόγον; ὃν υἱὸν προσηγόρευε διὰ τὸ μέλλειν αὐτὸν γενέσθαι»; rojo: «οὔτε γὰρ ἄσαρκος καὶ καθ’ ἑαυτὸν ὁ λόγος τέλειος ἦν υἱός… οὕτως οὖν εἷς υἱὸς τέλειος θεοῦ ἐφανερώθη»; verde (cap. 16): «ἀλλ’ ἐρεῖς μοι Πῶς γεγέννηται; …».')],
    'El pasaje más difícil de <i>Contra Noeto</i> (rojo) está en esta página; el pasaje de la generación «inenarrable» (verde) también. Leí el griego en la imagen. El subrayado es mío.', 'Lagarde 1858, escaneo abierto; subrayado mío')
cap('HP22', 'HP22', 'Páginas reales del griego: Refutación X.33 (Miller, p. 336) y IX.12 (Duncker, p. 458)', [('mil336.png', '<b>Miller (Oxford 1851), p. 336</b> · azul: «εἰ γὰρ θεόν σε ἠθέλησε ποιῆσαι, ἐδύνατο· ἔχεις τοῦ Λόγου τὸ παράδειγμα… εἰ δὲ θέλεις καὶ θεὸς γενέσθαι, ὑπάκουε τῷ πεποιηκότι»; oro: «Τούτου ὁ Λόγος μόνος ἐξ αὐτοῦ· διὸ καὶ θεός, οὐσία ὑπάρχων Θεοῦ»; verde: «ὁ πρωτόγονος πατρὸς παῖς».'), ('dun458.png', '<b>Duncker-Schneidewin (1859), p. 458</b> · oro: «δίθεοί ἐστε»; azul: «λέγων τὸν λόγον αὐτὸν εἶναι υἱόν, αὐτὸν καὶ πατέρα… ἓν δὲ ὂν τὸ πνεῦμα ἀδιαίρετον· οὐκ ἄλλο εἶναι πατέρα, ἄλλο δὲ υἱόν»; verde: «ἓν ὂν πρόσωπον μὴ δύνασθαι εἶναι δύο, καὶ οὕτως τὸν πατέρα συμπεπονθέναι τῷ υἱῷ».')],
    'Escaneos de archive.org sin capa de texto útil: leí el griego en la imagen. «οὐσία ὑπάρχων Θεοῦ» es la frase más favorable a la consustancialidad, pero <i>theós</i> no lleva artículo y el texto no usa «homoousios». A la derecha, Hipólito <b>cita a Calixto</b> (modalista), no expone su propia doctrina. El subrayado es mío.', 'Miller 1851 y Duncker-Schneidewin 1859, escaneos abiertos; subrayado mío')
body = '''<div class="two"><div class="pn"><h4>Método</h4><ul class="l" style="font-size:15px;line-height:1.45">
<li>Once investigadores (modelo pequeño): H1 Contra Noeto 1-8; H2 Contra Noeto 9-18; H3 Refutación IX; H4 Refutación X.28-34; H5 Daniel y Cristo y Anticristo; H6 Tradición apostólica; H7 obras dudosas; H8 identidad; H9 escaneos y texto; H10 estudiosos y recepción; H11 metafísica y paralelos. Encargos y datos en <code>herramientas/</code>. Un corte por límite de uso los detuvo; los retomé y terminaron.</li>
<li><b>Yo comprobé</b> en imagen de página: Lagarde 1858 pp. 51-54 (Contra Noeto), Miller 1851 p. 336 y Duncker-Schneidewin 1859 p. 458 (Refutación). El resto del griego lo leyeron los investigadores (marcado en cada cita; parte por OCR).</li>
<li>Traducciones al español mías, desde el griego cuando se muestra, desde el inglés cuando sólo hay inglés.</li></ul></div>
<div class="pn"><h4>Correcciones y negativos</h4><ul class="l" style="font-size:14.5px;line-height:1.42">
<li>«Mente… engendró el Verbo… Logos es Dios, sustancia de Dios» es Ref. <b>X.33</b>, no X.32; «cuando quiso creó» y «serás un dios» no están con esas palabras.</li>
<li>«El Padre manda, el Hijo obedece» es C. Noet. <b>14</b>; «dos personas» ya aparece en el cap. 7.</li>
<li>El horno es Dan 3 (LXX 3:92-93), no «4.11». <i>Contra Noeto</i> termina en el cap. 18 con una doxología.</li>
<li>La <i>Tradición apostólica</i> no se conserva en griego; la atribución es discutida; el «homoousion» sahídico es tardío.</li>
<li>«Trinity» en <i>Contra Beron</i> es glosa de la ANF; el griego dice «tetras».</li>
<li>No pude abrir Kelly, Prestige, Hanson, Simonetti, Quasten, Nautin, Brent, Cerrato, Butterworth ni Dix (restringidos); Wendland GCS 26 no se halló; Focio cód. 121 sólo por imagen y OCR.</li>
<li>No resolví el «problema de Hipólito» (uno o dos autores) ni la variante «λόγος σὰρξ ἦν» de Lagarde. No hallé el texto del Credo Niceno en las fuentes leídas.</li></ul></div></div>'''
card('HP23', hdr('HP23', 'Fuentes y límites', 'Resumen', 'Qué se leyó, qué se corrigió y qué no se pudo comprobar', 'Resumen honesto del método y sus límites'), body, FOOT)
print('hrgen ok', len(S))
