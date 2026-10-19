# -*- coding: utf-8 -*-
# Genera las diapositivas del pack «¿Dijo Jesús que era Dios?»: JD00 (mapa), JD01-JD08 (puntos), 8 académicos x 2, JD90 (blog), JD99 (fuentes y límites)
import sys, os, re, shutil, html
JD = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/jd'
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb')
sys.path.insert(0, JD)
import hbcss, genpad
from hbcss import E
from jdpoints import POINTS, VIDEO
from jdsch import SCH
OUT = JD + '/jdcards'
os.makedirs(OUT + '/img', exist_ok=True)
PACK = 'Pack «¿Dijo Jesús que era Dios?»: respuesta al vídeo de @isarojasmx (Cap. 8 de «El Nuevo Testamento a examen»)'
hbcss.TAGNAME.update({'F': 'Lo que afirma', 'C': 'Concesión / límite'})
CSS = hbcss.CSS + genpad.CQ + """
.tgF{background:#d9ecdf;color:#14213d}.tgC{background:#cfe3f7;color:#14213d}
.lb{font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;font-weight:700;color:#3b4660;margin-bottom:3px}
.vsay{background:#f3f4f8;border-left:5px solid #8a93a6;border-radius:0 8px 8px 0;padding:11px 18px;margin-bottom:10px}
.vsay p{font-size:16.5px;line-height:1.5;color:#2b3550}
.conc{background:#fff4dd;border-left:5px solid #e0a100;border-radius:0 8px 8px 0;padding:11px 18px;margin-bottom:6px}
.conc p{font-size:16.5px;line-height:1.5}
ol.rs{margin:6px 0 12px 24px;font-size:17px;line-height:1.5}
ol.rs li{margin:6px 0}
.srcs{font-size:13.5px;line-height:1.45;color:#566079;border-top:1px solid #e3e7ee;padding-top:8px;margin-top:10px}
.sy .b p{font-size:17px}
.pgcol{width:620px;flex:none}
.pgimg{border:1px solid #cfd6e2;border-radius:8px;overflow:hidden;margin-bottom:10px;background:#fff}
.pgimg img{width:100%;display:block}
.pgimg .cp{font-size:12.5px;color:#566079;padding:5px 9px;background:#f4f5f8;line-height:1.35}
.cvs{display:flex;gap:10px;margin-top:4px}
.cvs img{height:150px;border:1px solid #cfd6e2;border-radius:4px;box-shadow:0 2px 8px rgba(20,33,61,.18)}
.info2{display:flex;gap:26px;align-items:flex-start}
.info2 .rt{flex:1;min-width:0}
.info2 .nm{font-size:27px}
.work .cl,.work .oj{font-size:16px}
.map td{font-size:14.5px;line-height:1.4;vertical-align:top}
.map td.v{font-weight:700;white-space:normal}
.v1{color:#1d7a4f}.v2{color:#9a6a00}.v3{color:#b44a2f}
"""
def hdr(cid, tag, kind, title, ref):
    return f'''<div class="hd alt"><div class="row"><div class="badge"><b>{cid}</b>{tag}</div><span class="kind es">{kind}</span></div>
<h1>{title}</h1><div class="row"><div class="ref">{ref}</div></div></div>'''
def card(fname, head, body, foot):
    h = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="card">{head}<div class="bd">{body}</div><div class="ft"><div class="u">{foot}</div></div></div></body></html>'
    open(f'{OUT}/{fname}.html', 'w', encoding='utf-8').write(h)
def ei(t):
    return E(t).replace('&lt;i&gt;', '<i>').replace('&lt;/i&gt;', '</i>')
def sb(t):
    return t.replace('<b>', '<strong>').replace('</b>', '</strong>')
def mk(s):
    s = E(s)
    s = s.replace('&lt;i&gt;', '<i>').replace('&lt;/i&gt;', '</i>').replace('&lt;b&gt;', '<b>').replace('&lt;/b&gt;', '</b>')
    s = re.sub(r'\[\[k:(.+?)\]\]', r'<mark class="k">\1</mark>', s)
    s = re.sub(r'\[\[a:(.+?)\]\]', r'<mark class="a">\1</mark>', s)
    return s

# ---------------------------------------------------------------- JD01-JD08
for p in POINTS:
    rs = ''.join(f'<li>{x}</li>' for x in p['resp'])
    p1, p2, c = p['syl']
    syl = f'''<div class="sy"><div class="t">Silogismo <span>{p["id"]}</span></div><div class="b">
<p><b class="p">P1.</b> {p1}</p><p><b class="p">P2.</b> {p2}</p><div class="c"><b>C.</b> {c}</div></div></div>'''
    body = f'''<div class="vsay"><div class="lb">Lo que dice el vídeo</div><p>{p["says"]}</p></div>
<div class="conc"><div class="lb">Lo que se puede conceder</div><p>{p["conc"]}</p></div>
<h2 class="g">Respuesta</h2><ol class="rs">{rs}</ol>{syl}<div class="srcs"><b>Fuentes.</b> {p["srcs"]}</div>'''
    card(p['id'], hdr(p['id'], p['tag'], 'Refutación', p['title'], p['ref']), body,
         PACK + '<br>Traducciones al español mías. Los códigos BK, BR, WR, HU, SC, BO, PI, BI remiten a las diapositivas de cada académico (cita y página).')

# ---------------------------------------------------------------- académicos
def cita_slide(f):
    qs = ''
    for tg, txt, src in f['quotes']:
        qs += f'<div class="qq"><div class="n"><span class="chips"><span class="tg tg{tg}">{hbcss.TAGNAME[tg]}</span></span></div><blockquote>{mk(txt)}<span class="ac">{ei(src)}</span></blockquote></div>'
    h = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}.qq blockquote{{font-size:26px;line-height:1.5}}.qq blockquote .ac{{font-size:16px;margin-top:10px}}.qs{{min-height:700px}}</style></head><body><div class="qs">
<div class="top"><div class="who"><b>{f["id"]}</b>{E(f["name"])}<i>{E(f["dates"])}</i></div></div>
<div class="mid">{qs}</div>
<div class="ft2"><span>Citas traducidas al español por mí; las partes subrayadas en oro son lo que afirma, en azul lo que concede o limita. Fuente y página en la diapositiva siguiente.</span><span>{f["id"]} · 1/2</span></div></div></body></html>'''
    open(f'{OUT}/{f["id"]}_cita.html', 'w', encoding='utf-8').write(h)
def info_slide(f):
    pgs = ''
    for i, (src, cap) in enumerate(f['images']):
        dst = f'{OUT}/img/{f["id"]}_{i}.png'
        shutil.copy(src, dst)
        pgs += f'<div class="pgimg"><img src="img/{f["id"]}_{i}.png"><div class="cp">{cap}</div></div>'
    cvs = ''
    for i, c in enumerate(f['covers']):
        dst = f'{OUT}/img/{f["id"]}_cv{i}.jpg'
        shutil.copy(c, dst)
        cvs += f'<img src="img/{f["id"]}_cv{i}.jpg">'
    cvh = f'<div class="cvs">{cvs}</div>' if cvs else ''
    works = ''
    for t, ed, url, est in f['works']:
        works += f'''<div class="work"><div class="wt">{t}</div><table>
<tr><td>Edición</td><td>{ed}</td></tr><tr><td>Leído en</td><td style="word-break:break-all">{url}</td></tr><tr><td>Estado</td><td><b>{est}</b></td></tr></table></div>'''
    if f.get('wide'):
        body = f'''<div style="display:flex;flex-direction:column;gap:0">{pgs}</div>{('<div class="cvs" style="margin:4px 0 12px">'+cvs+'</div>') if cvs else ''}
<div class="two" style="align-items:start"><div><div class="nm">{E(f["name"])}<span>{f["why"]}</span></div><div style="height:10px"></div>{works}</div>
<div class="work"><div class="cl"><b>Aclaración de las citas</b>{sb(f["clar"])}</div><div class="oj"><b>Ojo: lo que no dice o no pude comprobar</b>{sb(f["ojo"])}</div></div></div>'''
    else:
        body = f'''<div class="info2"><div class="pgcol">{pgs}{cvh}</div>
<div class="rt"><div class="nm">{E(f["name"])}<span>{f["why"]}</span></div><div style="height:12px"></div>{works}
<div class="work"><div class="cl"><b>Aclaración de las citas</b>{sb(f["clar"])}</div><div class="oj"><b>Ojo: lo que no dice o no pude comprobar</b>{sb(f["ojo"])}</div></div></div></div>'''
    card(f'{f["id"]}_info', hdr(f['id'], 'Académico · obra y página', f'{f["id"]} · 2/2', f'{E(f["name"])}: la obra, la página y qué quieren decir las citas', f['role']), body,
         PACK + '<br>Las imágenes son capturas de páginas reales (PDF abiertos o páginas web) con el subrayado mío; cuando no pude ver la página, la tarjeta lo dice.')
for f in SCH:
    cita_slide(f); info_slide(f)

# ---------------------------------------------------------------- JD00 mapa
MAP = [
 ('1', 'Jn 10:30 «uno» y Sal 82', 'v2', 'Parcial', '«Uno» no es por sí solo identidad; Jn 17:21 usa la misma palabra; Brown: Jesús no da afirmación clara en 10:33.', 'El texto registra «te haces Dios» (10:33) y que Jesús no lo retira; Jn 17:21 dice «en nosotros».', 'JD01'),
 ('2', 'Jn 8:58 frente a Jn 9:9', 'v2', 'Parcial', '<i>Egó eimi</i> puede ser corriente (9:9).', 'En 9:9 hay predicado y no hay reacción; en 8:58 no hay predicado, hay contraste con «llegar a ser» y apedreamiento.', 'JD02'),
 ('3', 'Apocalipsis: Alfa y Omega', 'v2', 'Parcial', 'Ap 1:11 falta en el Sinaítico; en 1:8 habla el Padre.', '1:17, 2:8 y 22:13 (Jesús) no dependen de 1:11; «el primero y el último» es de YHWH (Is 44:6); «rey de reyes» es título recibido.', 'JD03'),
 ('4', 'Tomás y Brown (Jn 20:28)', 'v2', 'Parcial', 'Brown dice que Jesús nunca usa el título «Dios» y solo Tomás se lo aplica.', 'Brown habla del título; en 1965 responde «sí» a si el NT llama Dios a Jesús (3+5 casos) y dice que <i>kyrios</i> es el título de YHWH.', 'JD04 · BR'),
 ('5', 'Perdonar pecados', 'v2', 'Parcial', 'Mt 9:8 («a los hombres») y Jn 20:23; Boyarin: autoridad «delegada».', 'Mc 2:5-10: ejerce la prerrogativa en su nombre y valida el principio «solo Dios»; delegada ≠ ausente.', 'JD05 · BO'),
 ('6', 'Señor del sábado, Hijo del hombre', 'v2', 'Parcial', 'Jesús argumenta con David; «hijo de hombre» es de Ezequiel.', 'Con artículo y «las nubes» remite a Dn 7; Hurtado: rasgo del habla de Jesús; Boyarin limita el dominio al ámbito humano.', 'JD06 · HU · BO'),
 ('7', '«Veredicto de los académicos»', 'v3', 'Respondido', 'Hay amplio acuerdo en que Jesús no dijo «soy Dios» explícitamente.', 'Dunn: la frase sigue («pero…») en la misma página; «no deja rastro» es de Renan; Ehrman admite cristología alta muy temprana; Pitre defiende lo contrario.', 'JD07 · PI · BR'),
 ('8', '«Se esperaría una declaración clara»', 'v1', 'Concedido en parte', 'En los Sinópticos Jesús no dice «soy Dios, adórenme».', 'Un judío del s. I lo expresaría con acciones y alusiones (Pitre, Wright, Bird); reacción de blasfemia; culto temprano (Bauckham). Pregunta histórica abierta.', 'JD08 · BK · WR · BI'),
]
rows = ''.join(f'<tr><td class="v">{n}</td><td><b>{t}</b></td><td class="v {c}">{v}</td><td>{conc}</td><td>{resp}</td><td class="v">{sl}</td></tr>' for n, t, c, v, conc, resp, sl in MAP)
body = f'''<table class="v map" style="table-layout:fixed"><tr><th style="width:30px">#</th><th style="width:165px">Punto del vídeo</th><th style="width:118px">Veredicto</th><th style="width:285px">Lo que hay que conceder</th><th>Respuesta en una línea</th><th style="width:125px">Diapositivas</th></tr>{rows}</table>
<div class="ans" style="margin-top:14px"><b>En una frase.</b> El vídeo acierta en que el Jesús de los Sinópticos no dice «soy Dios, adórenme» y en que el título «Dios» para Jesús es tardío; pero no demuestra lo que concluye (que «nunca reclamó lo que no le pertenecía»): <b>los académicos que cita no dicen eso</b> (Dunn, Brown y Ehrman lo matizan; Pitre defiende lo contrario), y la discusión histórica está abierta y dividida.</div>
<div class="two"><div class="pn"><h4>Quién dice qué (resumen honesto)</h4><ul class="l" style="font-size:15.5px;line-height:1.45">
<li><b>Jesús habló y actuó como divino (con matices):</b> Wright, Pitre, Bird, Evans; Boyarin (divino-humano, de segunda mano).</li>
<li><b>Cristología alta muy temprana, sin afirmar que Jesús lo dijera:</b> Hurtado, Bauckham (para las comunidades), Ehrman (para los primeros cristianos).</li>
<li><b>Jesús no lo dijo explícitamente:</b> Dunn, Ehrman, Vermes, Casey, Hurtado; Brown (para el título «Dios»).</li></ul></div>
<div class="pn"><h4>Qué se ha leído de verdad</h4><ul class="l" style="font-size:15.5px;line-height:1.45">
<li><b>Páginas reales vistas:</b> Bauckham 2018 (pp. 12-13), Brown 1965 (pp. 565-566), Schäfer 2020 (p. 5), Hurtado (<i>NIDB</i>), y páginas web de Pitre, Wright, Hurtado, Bird.</li>
<li><b>De segunda mano o parcial:</b> Boyarin, Segal, Dunn (continuación leída solo en el fotograma del vídeo), Vermes.</li>
<li><b>No leídos:</b> los libros principales de Bauckham, Hurtado, Wright, Pitre, Bird, Evans, Bock y Gathercole.</li></ul></div></div>'''
card('JD00', hdr('JD00', 'Mapa · vídeo y respuesta', 'Resumen', '«¿Jesús dijo que era Dios?»: ocho puntos del vídeo y qué responder', VIDEO), body,
     PACK + '<br>Vídeo analizado con los subtítulos automáticos de TikTok, Whisper large-v3 y 74 fotogramas (cada 6 s). El vídeo no distingue entre «título explícito» e «identidad divina», y esa distinción recorre todas las respuestas.')

# ---------------------------------------------------------------- JD90 blog
body = '''<div class="two"><div class="pn"><h4>Qué cubre el blog (12 + 12 + 12 dossiers leídos)</h4><ul class="l" style="font-size:15.5px;line-height:1.45">
<li><b>Útiles:</b> «Padre y yo somos uno» (Jn 10:30; el mejor argumento), «Jesús Hijo de Dios», «Tomás» (Jn 20:28), «Alfa y Omega» (Ap 22:13, 1:17), «Divinidad paulina» (transferencia <i>kyrios</i>/YHWH; Hch 7:59).</li>
<li><b>Responden en parte</b> a los puntos 1-6 del vídeo; <b>no responden</b> a los puntos 7 y 8 ni a: Jn 9:9, Jer 1:5, Dn 2:37, Ap 3:12, la frase de Brown, Mt 9:8 y Jn 20:23, ni a «Hijo del hombre» = Ezequiel. Esos huecos los cubre este pack.</li>
<li>Los dossiers citan a Bauckham, Hurtado, Wright, Evans, Brown y Boyarin, pero <b>ninguno</b> interactúa con Dunn, Vermes, Ehrman ni Pitre.</li></ul></div>
<div class="pn"><h4>Qué no conviene citar sin comprobar (señalado por los investigadores)</h4><ul class="l" style="font-size:15.5px;line-height:1.45">
<li>Varias citas de Padres no están en la obra citada (Tertuliano, <i>Adv. Prax.</i> 22; Atanasio; Ireneo IV.6.3); «Policarpo 14» es falso (la oración va dirigida a Dios) y Flp de Policarpo 12 está mal traducido.</li>
<li><b>Errores bíblicos:</b> en Ap 19:10 el que cae a los pies del ángel es Juan, no Pedro; «ningún ángel del Señor tras el nacimiento» es falso (Hch 12:7); la regla del artículo para «el ángel de YHWH» falla en Ag 1:13; Sal 6:8 lo dice David, no YHWH.</li>
<li><b>Argumentos débiles:</b> la afirmación de 1QIsa<sup>a</sup>, la «unanimidad» de los Padres sobre «Hijo del hombre» (Crisóstomo lo lee como naturaleza humana) y el consenso sobre 4Q246.</li>
<li>El envoltorio «Juan 11» contiene un dossier sobre Jn 1:1; los hadices citados no pudieron comprobarse (sunnah.com bloqueado).</li></ul></div></div>
<div class="ans" style="margin-top:14px"><b>Cómo se usó el blog.</b> Solo como índice de argumentos: ninguna afirmación suya aparece en las diapositivas sin su texto bíblico o su fuente. Los hallazgos completos, con el número de cada dossier, están en <code>herramientas/datos_agentes/J1_notes.md</code>, <code>J2_notes.md</code> y <code>J3_notes.md</code>.</div>'''
card('JD90', hdr('JD90', 'Aviso · el blog «Defendiendo la Fe»', 'Aviso', 'Qué sirve y qué no del blog de apologética', 'Los 36 dossiers leídos por tres investigadores (J1-J3); no todo lo señalado fue recomprobado por mí'), body, PACK)

# ---------------------------------------------------------------- JD99 fuentes y límites
body = '''<div class="two"><div class="pn"><h4>Cómo se hizo</h4><ul class="l" style="font-size:15.5px;line-height:1.45">
<li>El vídeo se analizó con los subtítulos de TikTok, una transcripción de Whisper large-v3 y 74 fotogramas; las páginas que enseña (Dunn, Brown, Vermes, Pitre) se leyeron en los fotogramas.</li>
<li>Once investigadores (modelo pequeño): tres leyeron el blog; ocho buscaron académicos y fuentes primarias. <b>Yo volví a leer</b> en la página: Bauckham (pp. 12-13), Brown (pp. 564-567), Schäfer (p. 5), Hurtado (<i>NIDB</i>), el artículo de Pitre, el ensayo de Wright, el extracto de Bird y Evans.</li>
<li>Los textos bíblicos están en traducción mía; el griego (<i>egó eimi</i>, <i>hén</i>, <i>kyrios</i>) es el del texto estándar.</li></ul></div>
<div class="pn"><h4>Límites</h4><ul class="l" style="font-size:15.5px;line-height:1.45">
<li>No pude leer los libros principales (Bauckham 2008, Hurtado 2003, Wright 1996, Pitre 2024, Evans, Bock, Gathercole): Google Books estaba bloqueado y archive.org solo presta. Las capturas son de PDFs y webs abiertos.</li>
<li><b>Dunn:</b> la continuación de su frase la leí en el fotograma del vídeo; no localicé la edición ni la página (Pitre cita la 2.ª ed., p. 254). <b>Vermes:</b> solo la reseña citada. <b>Segal y Boyarin:</b> de segunda mano.</li>
<li>Ap 1:11: Sinaítico por transcripción (no facsímil); Alejandrino, NA28 y Metzger no consultados.</li>
<li>El vídeo se contesta aquí por sus puntos; no sé quién es «él» salvo por este vídeo: si hay otros, habría que añadirlos.</li>
<li>Esto es argumentación cristiana con fuentes y límites; no pretende zanjar la cuestión histórica, que entre los estudiosos sigue abierta.</li></ul></div></div>'''
card('JD99', hdr('JD99', 'Fuentes, límites y avisos', 'Resumen', 'Qué se leyó, qué se dejó fuera y qué hay que tener en cuenta', 'Resumen honesto del método y de sus límites'), body, PACK)

# ---------------------------------------------------------------- guion (4 diapositivas de texto)
def md_inline(t):
    t = E(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'\*(.+?)\*', r'<i>\1</i>', t)
    return t
g = open(JD + '/guion.md', encoding='utf-8').read()
parts = re.split(r'\n---\n', g)
main = parts[1] if len(parts) > 1 else g
short = parts[2] if len(parts) > 2 else ''
blocks = [ln.strip() for b in main.strip().split('\n\n') for ln in b.split('\n') if ln.strip()]
# agrupa: cada bloque '**[' abre una sección; el siguiente(s) son su cuerpo
secs = []
for b in blocks:
    if b.startswith('**['):
        secs.append([b, []])
    elif secs:
        secs[-1][1].append(b)
def sec_html(h, body):
    hh = md_inline(h.strip('*'))
    out = f'<h2 class="g" style="margin-top:14px">{hh}</h2>'
    for para in body:
        if para.startswith('*Silogismo:*'):
            out += f'<div class="ans" style="font-size:16.5px;margin:6px 0 4px;padding:9px 16px">{md_inline(para)}</div>'
        else:
            out += f'<p class="l" style="font-size:17px;line-height:1.5">{md_inline(para)}</p>'
    return out
groups = [secs[0:4], secs[4:7], secs[7:]]
titles = ['Guion (1/4): apertura y puntos 1-3', 'Guion (2/4): puntos 4-6', 'Guion (3/4): puntos 7-8 y cierre']
for i, (grp, tt) in enumerate(zip(groups, titles), 1):
    body = ''.join(sec_html(h, bd) for h, bd in grp)
    card(f'JDG{i}', hdr(f'JDG{i}', 'Guion del vídeo', 'Guion', tt, 'Unos 8 minutos leído a ritmo normal; entre corchetes, la diapositiva que va en pantalla'), body, PACK + '<br>El guion no añade nada que no esté en las diapositivas JDxx con su fuente.')
sb_ = ''.join(f'<p class="l" style="font-size:19px;line-height:1.6">{md_inline(x.strip())}</p>' for x in short.strip().split('\n\n') if x.strip() and not x.strip().startswith('## '))
card('JDG4', hdr('JDG4', 'Guion del vídeo', 'Guion', 'Guion (4/4): versión corta para TikTok (≈75 s)', 'Para un vídeo breve; fotograma del vídeo con la página de Dunn, BR_info y PI_info en pantalla'), sb_, PACK)
print('guion slides ok')

print('jdgen ok')
