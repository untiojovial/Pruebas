# -*- coding: utf-8 -*-
# Páginas de resumen y silogismos del pack TA (taʿliq de Ibn Abbas): TA00, TA00b, TA00c y S1–S3.
import re, html, os
src = open('genv.py', encoding='utf-8').read()
CSS = re.search(r'CSS = """(.*?)"""', src, re.S).group(1)
CSS += """
table.v{width:100%;border-collapse:collapse;font-size:17px;line-height:1.4}
table.v th{background:#eef1f6;text-align:left;padding:8px 10px;font-size:13px;text-transform:uppercase;letter-spacing:.05em;color:#3b4660}
table.v td{border-top:1px solid #e3e7ee;padding:8px 10px;vertical-align:top}
.ok{color:#1d7a4f;font-weight:700}.no{color:#b44a2f;font-weight:700}.mid{color:#9a6a00;font-weight:700}
.ans{border-left:6px solid #14213d;background:#eef1f8;padding:16px 22px;border-radius:0 8px 8px 0;font-size:21px;line-height:1.55;margin-bottom:20px}
.ans b{color:#14213d}
.pr{border:1px solid #d6dbe4;border-radius:8px;padding:14px 20px;margin-bottom:12px;font-size:21px;line-height:1.5;background:#fff}
.pr .n{display:inline-block;background:#14213d;color:#fff;border-radius:6px;padding:1px 9px;font-weight:700;margin-right:8px;font-size:17px}
.pr .w{color:#566079;font-size:16px;margin-top:4px}
.cc{border-left:6px solid #2a9d8f;background:#eef8f6;padding:14px 20px;border-radius:0 8px 8px 0;font-size:22px;line-height:1.5;font-weight:600;margin:6px 0 14px}
ul.l{margin:6px 0 0 22px;font-size:19px;line-height:1.5}
h2.g{font-size:19px;margin:18px 0 8px;color:#14213d;border-bottom:2px solid #fca311;padding-bottom:3px}
"""
E = lambda s: html.escape(s, quote=False)
OUT = 'tacards'
os.makedirs(OUT, exist_ok=True)

def page(fname, cid, tag, kind, title, ref, arref, body, foot):
    out = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="card">
<div class="hd"><div class="row"><div class="badge"><b>{cid}</b>{E(tag)}</div><span class="kind es">{E(kind)}</span></div>
<h1>{E(title)}</h1>
<div class="row"><div class="ref">{E(ref)}</div><div class="arref">{arref}</div></div></div>
<div class="bd">{body}</div>
<div class="ft"><div class="u">{foot}</div></div>
</div></body></html>'''
    open(f'{OUT}/{fname}.html', 'w').write(out)

def table(rows, heads=("Siglo / autor", "Qué dice", "Cómo lo atribuye", "Tarjeta · estado")):
    r = ''.join(f'<tr><td>{E(a)}</td><td>{E(b)}</td><td class="{c}">{E(d)}</td><td>{E(e)}</td></tr>' for a, b, d, e, c in rows)
    th = ''.join(f'<th>{h}</th>' for h in heads)
    return f'<table class="v"><tr>{th}</tr>{r}</table>'

# ---------- TA00 ----------
A = [
 ("541 H · Ibn ʿAtiyya, al-Muharrar 1/260 (2:75)", "«Ibn Abbas sostuvo que su tergiversación y su cambio son solo por la interpretación, y que el texto de la Torá permanece»; concluye «no hay duda de que hicieron las dos cosas»", "Dice que lo dijo Ibn Abbas", "H02a, H15 · verificado antes", "ok"),
 ("745 H · Abu Hayyan, al-Bahr al-Muhit (2:75 y 5:13)", "2:75: «y se dijo: por interpretación, quedando el texto de la Torá; lo dijo Ibn Abbas» (da primero la opinión de la mayoría: cambio de palabras). 5:13: «lo dio como significado Ibn Abbas y otros, y dijeron: es por interpretación, no por cambio de palabras; no es posible»; pero él concluye: «lo correcto es el cambio en texto y significado»", "Dice que lo dijo Ibn Abbas (dos pasajes)", "TA01, TA14 · leído por mí (texto web)", "ok"),
 ("774 H · Ibn Kathir, Tafsir (3:78)", "«Y así transmitió al-Bujari de Ibn Abbas: … nadie quita una palabra de un libro de Dios, pero lo tergiversan: lo interpretan en un sentido que no es el suyo»; luego matiza (el cambio sí entró en lo que tienen)", "Dice que lo transmitió al-Bujari de Ibn Abbas", "TA02 · leído por mí", "ok"),
 ("808 H · Ibn Jaldun, Kitab al-ʿIbar 2/7–8", "«Ibn Abbas, según lo que transmite de él al-Bujari, dijo que eso es improbable… lo tergiversaron con la interpretación»", "Dice que lo dijo Ibn Abbas", "H20a, H20b · verificado antes", "ok"),
 ("852 H · Ibn Hajar, Fath al-Bari 13/533", "Cuenta cuatro opiniones; dice que el matiz «se atribuyó a Wahb ibn Munabbih y también a Ibn Abbas, intérprete del Corán»; «no lo he visto conectado de Ibn Abbas»", "Informa de la atribución (con reserva)", "H21, IH01–IH03 · verificado antes", "mid"),
 ("875 H · al-Thaʿalibi, al-Yawahir al-hisan (2:75)", "«Ibn Abbas sostuvo que su tergiversación y su cambio son solo por interpretación, y que el texto de la Torá permanece»; y otro grupo dijo que cambiaron palabras (posible en la Torá, imposible en el Corán)", "Dice que lo dijo Ibn Abbas (copia de Ibn ʿAtiyya)", "TA15 · leído por mí (texto web)", "ok"),
 ("1270 H · al-Alusi, Ruh al-maʿani (2:75)", "«lo interpretan con una interpretación corrupta… y a eso se inclinó Ibn Abbas; y la mayoría sostiene que su tergiversación fue cambiando palabras»", "Dice que lo dijo Ibn Abbas", "TA03 · leído por mí", "ok"),
 ("1307 H · Siddiq Hasan Khan, Fath al-bayan (5:13, 4:46)", "Copia a Ibn Jaldun: «Ibn Abbas, según lo que transmite de él al-Bujari, dijo que eso es improbable… lo cambiaron por interpretación»; y a Ibn al-Qayyim (con el taʿliq de al-Bujari)", "Cita la atribución (de Ibn Jaldun e Ibn al-Qayyim)", "TA16 · leído por mí (texto web)", "mid"),
 ("1332 H · al-Qasimi, Mahasin al-taʾwil (3:78)", "Copia a Ibn Kathir: «y así transmitió al-Bujari de Ibn Abbas: … tergiversan: quitan…»", "Cita la atribución (de Ibn Kathir)", "TA05 · leído por mí", "ok"),
 ("1393 H · Ibn ʿAshur, al-Tahrir wa-l-tanwir (4:46, 5:13)", "«Lo que se transmite de Ibn Abbas: que la tergiversación es corrupción de la interpretación y que un pueblo no se propone cambiar su libro, se refiere a la mayoría de sus casos»", "Dice que se transmite de Ibn Abbas (y lo limita)", "TA04 · leído por mí", "ok"),
 ("2014 · Mun'im Sirry (Oxford UP), p. 14", "«al-Bujari narra la explicación de Ibn Abbas del significado de tahrif, es decir, falsificación en términos de interpretación»", "Académico: lo da por narrado", "TA09 · leído por mí (fuente secundaria)", "mid"),
]
B = [
 ("310 H · al-Tabari (2:75)", "Glosa «luego lo tergiversan» = «cambian su significado y su interpretación»; pero también «más cercano a que tergiversen lo que hay en sus libros»", "Glosa de significado; no nombra a Ibn Abbas", "TA08 · leído por mí", "mid"),
 ("751 H · Ibn al-Qayyim, Ighathat al-lahfan", "«Un grupo de los imanes del hadiz, el fiqh y el kalam: el cambio fue en la interpretación»; doctrina de al-Bujari y elección de al-Razi; él prefiere la postura intermedia", "Lo atribuye a al-Bujari, no a Ibn Abbas; recoge los argumentos de esa escuela", "TA06, TA17 · leído por mí", "mid"),
 ("Ibn Abbas «hudud Allah» · al-Tabari 5:13 (n.º 11586) y Abu Hayyan 5:41", "«Tergiversan» = «los límites [hudud] de Dios en la Torá»; Abu Hayyan: «cambiaron la lapidación: pusieron el azote en su lugar»", "Ibn Abbas, pero sobre normas; no dice si de texto", "TA18 · leído por mí", "mid"),
 ("804 H · Ibn al-Mulaqqin, al-Tawdih (según Ibn Hajar)", "«Lo que dijo es una de las dos opiniones, y es su elección [la de al-Bujari]»", "Lo lee como palabras de al-Bujari", "H19a, H19b · verificado antes", "mid"),
 ("Siglo XXI · Abd al-ʿAziz al-Rayihi (lección 647)", "al-Bujari «explicó el dicho de Ibn Abbas como tahrif del significado»; pero señala que la frase «tiene un problema» y la acota", "Comentario sobre Ibn Abbas; lo discute", "TA07 · leído por mí (transcripción)", "mid"),
]
C = [
 ("al-Zarkashi (m. 794 H), según Ibn Hajar", "Llama «falsa» la opinión de que el tahrif sea solo de significado; Ibn Hajar replica: «en tildarla de falsa… hay objeción», porque se atribuyó a Wahb y a Ibn Abbas", "En contra, pero criticado", "H21 · verificado antes", "no"),
 ("al-Qastallani (m. 923 H), según un agente (OCR)", "La frase «y nadie quita…» «puede ser de al-Bujari o de Ibn Abbas»; sobre lo que al-Bujari dice aquí: «hay objeción»", "Duda y objeta", "sin captura · agente Y1 (OCR)", "mid"),
 ("606 H · al-Razi, Mafatih al-gayb (2:75, 3:78)", "2:75: lo preferible es entenderlo como cambio de texto, «como se transmitió de Ibn Abbas: que añadieron y quitaron» (dicho del Qadi); y solo si eso no es posible, como interpretación. 3:78: relato de Ibn Abbas: «escribieron un libro» mezclando la descripción de Muhammad", "Narra de Ibn Abbas el cambio de texto", "TA19 · leído por mí (texto web)", "no"),
 ("al-Alusi (4:46) · Ibn Kathir (2:79) · al-Tabari (3:78, 2:79)", "De Ibn Abbas se transmite también que «cambiaron el Libro de Dios… y escribieron con sus manos», y que «añadían al libro de Dios lo que Dios no reveló»", "Narraciones de Ibn Abbas de cambio de texto", "TA10, TA11, TA12 · leídas por mí", "no"),
 ("al-Qasimi (2:75) · Rashid Rida (Manar 5:13) · Ibn ʿAshur", "Aceptan la lectura «de interpretación» como la más ajustada al versículo, pero afirman que el cambio de texto ocurrió también («sin duda»; «ambos»)", "Matizan", "TA13, TA04 · leídas; Manar: agente (Shamela)", "mid"),
]
body = f'''<div class="ans"><b>Sí: hay más.</b> Además de Ibn ʿAtiyya e Ibn Jaldun, lo atribuyen expresamente a Ibn Abbas —o dicen que al-Bujari lo transmitió de él— <b>Abu Hayyan (en dos pasajes), Ibn Kathir, al-Thaʿalibi, al-Alusi, Siddiq Hasan Khan, al-Qasimi e Ibn ʿAshur</b>, e Ibn Hajar lo recoge como atribución que no ve conectada; en total <b>diez autores, de 541 a 1393 H</b>, más el académico Sirry (2014). <b>Pero no son diez testimonios independientes</b> (al-Thaʿalibi copia a Ibn ʿAtiyya, al-Qasimi a Ibn Kathir, Siddiq a Ibn Jaldun e Ibn al-Qayyim) <b>y casi ninguno lo adopta como única postura</b>: Ibn Jaldun es quien más se inclina por ella (admite solo errores no deliberados de copia); los demás la dan junto a la del cambio de texto, o la limitan. De Ibn Abbas se transmiten además relatos de cambio de texto (TA10–TA12, TA19). Ningún autor que he leído habla de «consenso». Ibn Hajar no lo halló conectado «por un camino firme», y mis agentes tampoco lo hallan con cadena en al-Tabari ni en Ibn Abi Hatim.</div>
<h2 class="g">1 · Lo atribuyen a Ibn Abbas (por orden cronológico)</h2>{table(A)}'''
page('TA00_es', 'TA00', 'Taʿliq de Ibn Abbas · quién más lo atribuye', 'Resumen en español',
     '¿Quién más dice que, según Ibn Abbas, el tahrif es de significado y no de texto?',
     'Comprobado en las páginas originales (tafsir en línea, Shamela, Wikisource), con un escaneo propio de 55 comentarios coránicos y con 8 agentes de búsqueda cuyos hallazgos revisé yo.',
     'تعليق ابن عباس', body,
     'Colores de la columna «Cómo lo atribuye»: verde = lo dice expresamente · ocre = parcial o con reservas · rojo = en contra.<br>Pack «Ibn Abbas y el tahrif» (ampliación)')

# ---------- TA00b ----------
body2 = f'''<h2 class="g">2 · Quién lo atribuye a al-Bujari (y no a Ibn Abbas) o lo comenta</h2>{table(B)}
<h2 class="g">3 · Lo que juega en contra</h2>{table(C)}'''
page('TA00b_es', 'TA00b', 'Taʿliq de Ibn Abbas · matices y contrarios', 'Resumen en español',
     'Quién lo atribuye a al-Bujari, y qué hay en contra',
     'Del mismo trabajo. La opinión «solo interpretación» es una de varias que los propios sabios musulmanes recogen.',
     'مواقف', body2,
     'Pack «Ibn Abbas y el tahrif» (ampliación)')

# ---------- TA00c: negativos y límites ----------
NEG = '''<div class="box"><h3>Resultados negativos (buscado y no hallado)</h3><ul class="l">
<li><b>Ibn Hazm</b>, al-Fisal (todo el texto de Shamela descargado, ids 1–708): <b>cero</b> menciones de «Ibn Abbas»; él dice que algunos musulmanes niegan el tahrif «por ignorancia» (H13a).</li>
<li><b>Ibn Taymiyya</b>: Mayʿmuʿ 13 (OCR): recoge la lectura «solo interpretación» como dicha por «muchos musulmanes», sin nombrar a Ibn Abbas y para rechazarla en exclusiva; al-Yawab al-sahih (vols. 1–3, OCR): no cita a Ibn Abbas ni a al-Bujari en esto; vols. 4–7 sin leer.</li>
<li><b>al-Tabari e Ibn Abi Hatim</b>: el taʿliq «yuharrifun: yuzilun… ni uno quita una palabra» <b>no figura con cadena</b> en ninguno (0 coincidencias en 2:75–5:41; el de Ibn Abi Hatim, sobre OCR). Ibn Hajar: «no lo he visto conectado de Ibn Abbas».</li>
<li><b>Ibn al-Qayyim</b> (Hidayat al-hayara), al-Qarafi, al-Samawʾal, al-Zarkashi (al-Bahr al-muhit fi l-usul), al-Ghazali (atribuido), al-Jahiz: sin atribución a Ibn Abbas ni a al-Bujari en el pasaje (OCR o texto de archive.org).</li>
<li><b>Comentaristas de al-Bujari</b>: Ibn Battal (OCR): no comenta el taʿliq; al-Khattabi (copia incompleta), al-Suyuti (al-Tawshih: no llega a Tawhid), Ibn Hajar (Hady al-Sari): nada. Al-Kirmani y al-ʿAyni (OCR): glosan «yuharrifun» como «quitan por el sentido y lo interpretan mal», sin decir «Ibn Abbas».</li>
<li><b>Escaneo propio</b> de 55 comentarios coránicos de quran-tafsir.net en 2:75, 2:79, 3:78, 4:46, 5:13 y 5:41 (324 páginas): busqué «Ibn Abbas» junto a términos de interpretación/texto. Los hallazgos útiles están en TA14–TA16, TA18 y TA19; en los demás (p. ej. al-Khazin, al-Qurtubi, al-Shirbini, Ibn ʿAdil) Ibn Abbas aparece por otras cosas (los «hudud», «ghayr musmaʿ») o no con ese matiz. Un filtro por palabras puede dejar pasar otra formulación.</li>
<li><b>al-Iyi</b> (Yamiʿ al-bayan, 4:46): su página trae el pasaje de Ibn al-Qayyim con el taʿliq, pero en una nota numerada de la edición, no se ve que sea del autor: no lo cuento. Una antología («al-Yamiʿ al-tarijī li-bayan al-Qurʾan al-karim», que reproduce comentarios por orden cronológico) copia la frase de Ibn ʿAtiyya en 2:75: tampoco cuenta.</li>
<li><b>Tafsir sin Ibn Abbas en esto</b>: al-Qurtubi y al-Baghawi (5:13: «interpretan lo que no es» como primera glosa, sin nombre); Rashid Rida (Manar 5:13): «muchos de nuestros sabios eligieron este sentido», que él rechaza.</li>
</ul></div>
<div class="box ojo"><h3>Lo que no se puede afirmar</h3><ul class="l">
<li><b>«Ibn Abbas dijo que nadie puede quitar una palabra de la Torá.»</b> No se ha localizado cadena conectada; Ibn Hajar admite que la frase puede ser de al-Bujari o de Ibn Abbas; al-Mulaqqin la lee como de al-Bujari.</li>
<li><b>«Todos los sabios que lo citan lo aceptan.»</b> Falso: al-Alusi, Abu Hayyan (5:13: «lo correcto: texto y significado») e Ibn ʿAshur dan el cambio de texto como la postura mayoritaria o como también cierto; Ibn Kathir lo matiza; al-Zarkashi la llama falsa; Ibn Taymiyya y Ibn al-Qayyim eligen la postura media. Quien más se inclina por ella es Ibn Jaldun, y aun él admite cambios no deliberados al copiar.</li>
<li><b>«Hay consenso de que el texto de la Biblia está sin cambiar.»</b> No: Ibn Hajar enumera cuatro opiniones, y «muchos» musulmanes han dicho que cambiaron los textos (H19b).</li>
<li><b>«Son diez testimonios independientes.»</b> No: Ibn Kathir e Ibn Jaldun remiten a al-Bujari; al-Qasimi copia a Ibn Kathir; al-Thaʿalibi copia a Ibn ʿAtiyya; Siddiq copia a Ibn Jaldun e Ibn al-Qayyim; varios repiten la misma fórmula.</li>
<li><b>«Ibn Abbas dijo que los judíos no cambiaron ni una palabra.»</b> Eso no lo dice ningún texto que haya leído: lo que se atribuye es «nadie quita una palabra… pero lo tergiversan interpretándolo», y es dudoso que sea suyo. En al-Tabari, Ibn Kathir, al-Alusi y al-Razi el mismo Ibn Abbas aparece diciendo que «añadieron», «quitaron» o «escribieron un libro».</li>
</ul></div>'''
page('TA00c_es', 'TA00c', 'Taʿliq de Ibn Abbas · límites', 'Resumen en español',
     'Qué no se encontró, y qué no se puede afirmar',
     'Los resultados negativos importan: dicen hasta dónde llega la afirmación.',
     'حدود', NEG,
     'Los agentes de búsqueda (modelo pequeño) no son fuente; solo valen las citas que leí en la página original, y lo señalo donde no es así.<br>Pack «Ibn Abbas y el tahrif» (ampliación)')

# ---------- Silogismos ----------
def syl(n, title, prem, concl, weak, use, cards):
    ps = ''.join(f'<div class="pr"><span class="n">P{i+1}</span>{p[0]}<div class="w">{p[1]}</div></div>' for i, p in enumerate(prem))
    body = f'{ps}<div class="cc">∴ {concl}</div><div class="box ojo"><h3>Puntos débiles</h3><ul class="l">{"".join(f"<li>{w}</li>" for w in weak)}</ul></div><div class="box"><h3>Cómo usarlo</h3>{use}</div>'
    page(f'S{n}_es', f'S{n}', 'Silogismo a tu favor · con sus límites', 'Razonamiento', title,
         'Cada premisa remite a una tarjeta con el texto original.', 'منطق', body, f'Tarjetas: {cards}<br>Pack «Ibn Abbas y el tahrif» (ampliación)')

syl(1, "La lectura «el tahrif es sobre todo de significado» no es un invento moderno: diez autores, de 541 a 1393 H, la atribuyen a Ibn Abbas",
 [("Ibn ʿAtiyya, Abu Hayyan, Ibn Kathir, Ibn Jaldun, Ibn Hajar, al-Thaʿalibi, al-Alusi, Siddiq Hasan Khan, al-Qasimi e Ibn ʿAshur la presentan como de Ibn Abbas (o transmitida por al-Bujari de él).", "TA01–TA05, TA14–TA16, H02a, H15, H20a, H20b, H21"),
  ("Pocos la rechazan de plano: al-Zarkashi la llama falsa (y Ibn Hajar le responde que eso es excesivo) y Abu Hayyan, en 5:13, dice que lo «correcto» es el cambio en texto y significado; los demás la recogen sin descartarla, aunque la limitan.", "H21 · TA14 · TA02 · TA04")],
 "Dentro de la tradición clásica y moderna hay una lectura reconocida, atribuida a un Compañero «traductor del Corán» (Ibn Abbas) y recogida por al-Bujari, según la cual lo que el Corán llama tahrif es sobre todo interpretación errónea; no es una tesis apologética reciente.",
 ["La atribución no tiene cadena conectada (Ibn Hajar); y la frase «nadie quita…» puede ser de al-Bujari.",
  "No son testimonios independientes: al-Thaʿalibi copia a Ibn ʿAtiyya, al-Qasimi a Ibn Kathir, Siddiq a Ibn Jaldun e Ibn al-Qayyim, y varios remiten a al-Bujari.",
  "Ninguno la sostiene en exclusiva; todos los que leí dan también el cambio de texto como cierto o como mayoritario.",
  "Ibn Abbas aparece además en relatos de cambio de texto (TA10–TA12, TA19)."],
 "«Hay una lectura clásica, atribuida a Ibn Abbas por X, Y, Z, de que el tahrif coránico es sobre todo de significado.» Sin decir «consenso» ni «Ibn Abbas probó que no se cambió nada».",
 "TA01–TA05, TA14–TA16, H02a, H15, H20a, H21")

syl(2, "No hay consenso musulmán de que el texto de la Biblia esté simplemente «corrompido»",
 [("Ibn Hajar enumera cuatro opiniones: todo cambiado; cambiado en su mayor parte; cambiado en poco; cambio solo de significado (la que ve en al-Bujari).", "H21 · IH10"),
  ("Ibn Taymiyya e Ibn al-Qayyim describen tres posturas, con la intermedia («se añadió algo, cambiaron pocas cosas») como la suya, y al-Qasimi dice que el cambio textual ocurrió «sin duda» pero que la lectura «de interpretación» es la más ajustada al versículo. Ibn al-Qayyim expone además los argumentos de la primera escuela: copias dispersas, el versículo de la lapidación.", "TA06 · TA13 · TA17 · H17")],
 "La afirmación «los musulmanes siempre han enseñado que la Biblia está totalmente falsificada» es falsa: hay al menos cuatro posturas y entre ellas la de «solo significado», atribuida a Ibn Abbas, y la de «cambio parcial».",
 ["La postura más difundida entre los polemistas (Ibn Hazm, al-Qarafi, al-Kairanawi) es el cambio de texto (H13, H23).",
  "Que haya otras posturas no demuestra que el texto actual coincida con el original; eso se estudia con manuscritos, no con exégesis coránica."],
 "Para desmontar la generalización, no para probar la fiabilidad bíblica: el argumento de la fiabilidad se hace con manuscritos.",
 "TA06, TA13, TA17, H17, H21, H19b")

syl(3, "Si Ibn Abbas es testigo, hay que citarlo entero: también cuando dice «cambiaron el Libro de Dios»",
 [("Las mismas fuentes que citan a Ibn Abbas para «interpretación» (Ibn Kathir, al-Alusi, al-Tabari, al-Razi, al-Bujari 7363/7523) citan de Ibn Abbas el relato de que «cambiaron el Libro de Dios y escribieron con sus manos», de que «añadían al libro de Dios lo que Dios no reveló» o de que «añadieron y quitaron».", "TA10, TA11, TA12, TA19, H02b"),
  ("Ibn Hajar señala que el taʿliq «contradice» otra narración de Ibn Abbas y no lo ve conectado.", "H21 · IH03")],
 "No se puede usar a Ibn Abbas como árbitro neutral del tahrif en una sola dirección: lo honesto es presentar las dos narraciones, la cadena de cada una y el hecho de que los sabios las recogen ambas.",
 ["Las cadenas de las narraciones de cambio también son discutidas (la familia de al-ʿAwfi; al-Dahhak) y la de al-Bujari 7523 es de ʿUbayd Allah.",
  "Una narración puede referirse a copias (los «ummiyyun» escribieron un libro) y otra a la revelada (al-Rayihi): hay forma de armonizarlas (TA07)."],
 "Para ser creíble ante un oyente musulmán: presenta las dos y la armonización de al-Rayihi (copias escritas vs. revelación).",
 "TA02, TA07, TA10, TA11, TA12, TA19, H02b")
print('ok')
