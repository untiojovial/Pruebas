# -*- coding: utf-8 -*-
# Páginas de resumen del pack AP (apostasía en las fuentes tempranas): AP00, AP00b, AP00c
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
h2.g{font-size:19px;margin:18px 0 8px;color:#14213d;border-bottom:2px solid #fca311;padding-bottom:3px}
ul.l{margin:6px 0 0 22px;font-size:19px;line-height:1.5}
"""
E = lambda s: html.escape(s, quote=False)
OUT = 'apcards'
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
def table(rows, heads):
    r = ''.join(f'<tr><td>{E(a)}</td><td>{E(b)}</td><td class="{c}">{E(d)}</td><td>{E(e)}</td></tr>' for a, b, d, e, c in rows)
    th = ''.join(f'<th>{h}</th>' for h in heads)
    return f'<table class="v"><tr>{th}</tr>{r}</table>'

A = [
 ("Bujari 6922 y 3017 (256 H) · Ibn Abbas, vía ʿIkrima", "«Quien cambie su religión, matadlo»; Ibn Abbas objeta a ʿAli que queme a los zanadiqa («los habría matado»)", "Hadiz (palabra del Profeta)", "AP01, AP02", "ok"),
 ("Tirmidhi 1458 (279 H)", "Misma historia; ʿAli: «Ibn Abbas ha dicho la verdad»; «la práctica entre la gente del conocimiento es esta»", "Hadiz + práctica de los sabios", "AP05", "ok"),
 ("Bujari 6878 · Muslim 1676 · Ibn Masʿud", "«No es lícita la sangre de un musulmán… salvo por una de tres: la vida por la vida, el casado adúltero y el que deja su religión / se aparta de la comunidad»", "Hadiz (sangre lícita)", "AP03, AP04", "ok"),
 ("Abu Dawud 4502 · ʿUthman · al-Shafiʿi", "«…incredulidad tras el islam, o adulterio tras estar casado, o matar a una persona»", "Hadiz (sangre lícita)", "AP06, AP12", "ok"),
 ("Bujari 6923 · Muʿadh y Abu Musa", "«No me siento hasta que sea ejecutado: dictamen de Dios y de Su Mensajero» (judío convertido que vuelve al judaísmo)", "Caso de un Compañero", "AP07", "ok"),
 ("Abu Dawud 4356 e Ibn Abi Shayba 30930", "El mismo caso con plazo de arrepentimiento: veinte noches / dos meses, y luego se le corta la cabeza", "Caso (con matiz)", "AP08", "mid"),
 ("Ibn Abi Shayba (235 H): ʿUmar, ʿAli, ʿAmr", "Pedir el arrepentimiento (tres veces / tres días) y matar al que no se arrepiente; ʿAli mata a Mustawrid al-ʿIjli", "Prácticas de Compañeros (cadenas débiles/cortadas según el editor)", "AP09, AP10", "mid"),
 ("Abu Dawud 4359 y 2762", "El Profeta lamenta que nadie matara a Ibn Abi Sarh antes de aceptarle la lealtad; Ibn Masʿud ejecuta a Ibn al-Nawwaha (seguidor de Musaylima)", "Casos tempranos (con matices)", "AP11", "mid"),
 ("Malik (179 H) según Ibn ʿAbd al-Barr (463 H)", "«Quien cambie su religión, cortadle el cuello»; zanadiqa se matan sin plazo; apóstata declarado: arrepentimiento y luego muerte", "Jurista fundador", "AP13, AP14", "ok"),
 ("al-Shafiʿi (204 H), al-Umm", "«Incredulidad tras la fe» hace lícita la sangre; no se puede rescatar, perdonar ni dejar al apóstata «hasta que se haga musulmán o sea muerto»", "Jurista fundador", "AP12", "ok"),
 ("al-Sarakhsi (c. 483 H), hanafí", "Se ofrece el islam y, si no acepta, se mata en el acto (o tres días); fundamento: Corán 48:16, el hadiz y la práctica de ʿAli, Ibn Masʿud y Muʿadh", "Jurista (regla de escuela)", "AP15", "ok"),
 ("al-Qurtubi (671 H) sobre 2:217", "Resumen de posiciones; el hadiz de las tres causas «abarca a todo el que cometa incredulidad tras su fe, y es lo más válido»", "Comentario coránico", "AP19", "ok"),
 ("Ibn Taymiyya (728 H), al-Sarim al-maslul", "Defiende que se mata sin pedir arrepentimiento; argumenta con Ibn Abi Sarh, Miqyas e Ibn Jatal «que eran apóstatas»", "Jurista (posición propia)", "AP17", "ok"),
 ("Peters y De Vries (1976-77)", "«La pena establecida para la apostasía es la pena de muerte» (doctrina clásica), con excepciones", "Estudio académico (secundaria)", "AP22", "mid"),
]
B = [
 ("¿Se pide arrepentimiento antes?", "La mayoría: sí (Malik y Ahmad: tres días; al-Shafiʿi, dos dichos). ʿUbayd ibn ʿUmayr y Tawus, y lo que defiende Ibn Taymiyya: no hace falta. Plazos citados: una hora, tres días, veinte noches, un mes, dos meses, cien veces.", "Varía", "AP08, AP17, AP19", "mid"),
 ("¿Se mata a las mujeres?", "Malik, al-Awzaʿi, al-Shafiʿi y al-Layth: sí. Hanafíes (al-Thawri, Abu Hanifa): no, se las encarcela (con el hadiz de Ibn Abbas «no se mata a las mujeres»; el editor de Ibn Abi Shayba lo califica de débil: AP23).", "Dividido", "AP05, AP16, AP19, AP22, AP23", "no"),
 ("¿Es castigo por creer?", "Hanafíes: «matar no es retribución por la apostasía… se debe por la persistencia en la incredulidad… para repeler el combate»; la retribución de la incredulidad va al más allá. Ibn Taymiyya: «el que deja su religión, el que se separa de la comunidad» puede explicarse por el combatiente.", "Lectura alternativa clásica", "AP16, AP18", "mid"),
 ("¿Alcanza al dhimmi que cambia de religión?", "No: «el conjunto de los sabios»: quien pasa del judaísmo al cristianismo, siendo dhimmi, no es muerto (la pena es para quien sale del islam).", "Acotado", "AP14", "mid"),
 ("¿Qué dice el Corán?", "Al-Tabari: el ansari que apostató y preguntó si había arrepentimiento fue aceptado al arrepentirse (3:86); en 4:137, el arrepentimiento se acepta cada vez y «su islam protege su sangre». Al-Qurtubi: 2:217 solo habla de que sus obras se pierden; la pena sale de los hadices.", "En contra (matiz)", "AP19, AP20, AP21", "no"),
 ("Calidad de las cadenas", "Los editores de Ibn Abi Shayba califican de «débiles» o «cortadas» los relatos de ʿUmar (30925), ʿAli (30926), Muʿadh (30930) y ʿUmar a ʿAmr (34937); los de Mustawrid (34960) y Ibn Masʿud-Ibn al-Nawwaha, «ṣaḥīḥ». El hadiz base es de un solo Compañero por un solo transmisor (Ibn Abbas–ʿIkrima).", "Matiz", "AP08–AP10, AP01–AP02", "mid"),
 ("Disidencia clásica", "Ibrahim al-Nakhaʿi: «cada vez que apostata» (al-Tabari 4:137); Peters y De Vries recogen una «opinión aislada» suya de pedirle arrepentimiento siempre; los modernistas (ʿAbduh, Rida, Shaltut) la leen como pena solo al apóstata hostil.", "Minoritaria / moderna", "AP21, AP22", "mid"),
]
body = f'''<div class="ans"><b>Sí: hay textos tempranos y abundantes.</b> Tres bloques: (1) <b>hadices</b>: «Quien cambie su religión, matadlo» (Ibn Abbas, Bujari 6922 y 3017, Tirmidhi 1458) y «no es lícita la sangre de un musulmán salvo por una de tres… el que deja su religión» (Ibn Masʿud en Bujari 6878 y Muslim 1676; ʿUthman en Abu Dawud 4502); (2) <b>casos y prácticas de los Compañeros</b>: Muʿadh y Abu Musa en Yemen (Bujari 6923), ʿAli y Mustawrid, ʿUmar a ʿAmr ibn al-ʿAs, Ibn Masʿud e Ibn al-Nawwaha; y (3) <b>juristas</b> desde el siglo II H (Malik, al-Shafiʿi, la escuela hanafí con al-Sarakhsi, Ibn ʿAbd al-Barr, al-Qurtubi, Ibn Taymiyya). <b>Pero no es un bloque sin matices</b>: casi todos piden primero el arrepentimiento; los hanafíes no matan a las mujeres; los hanafíes razonan la pena como «repeler el combate», no como castigo por creer; el Corán, según al-Tabari y al-Qurtubi, no fija una pena mundana; hay un caso contrario (el ansari de 3:86 es aceptado); y varios relatos tienen cadena débil según sus editores.</div>
<h2 class="g">1 · Los textos que respaldan la pena (por orden de antigüedad aproximada)</h2>{table(A, ("Fuente", "Qué dice", "Tipo", "Tarjeta"))}'''
page('AP00_es', 'AP00', 'Apostasía · textos tempranos', 'Resumen en español',
     '¿Qué dicen los textos tempranos sobre matar al apóstata del islam?',
     'Comprobado en las páginas originales (Shamela, hadithunlocked, Wikisource, tafsir en línea, PDF); con 8 agentes de búsqueda cuyos hallazgos revisé yo.', 'الردة', body,
     'Colores de la columna «Tipo»: verde = el texto lo dice con claridad · ocre = con matiz o cadena discutida.<br>Pack «Apostasía en las fuentes islámicas tempranas»')
body2 = f'''<h2 class="g">2 · Matices, disidencia y contrarios que hay que decir a la vez</h2>{table(B, ("Tema", "Qué dicen las fuentes", "Resultado", "Tarjeta"))}'''
page('AP00b_es', 'AP00b', 'Apostasía · matices y contrarios', 'Resumen en español',
     'Lo que los mismos textos matizan, discuten o contradicen',
     'Si se cita el texto que respalda la pena, hay que citar también sus condiciones; cada fila remite a una tarjeta.', 'مواقف', body2,
     'Pack «Apostasía en las fuentes islámicas tempranas»')
NEG = '''<div class="box"><h3>Pistas que se comprobaron y no salieron como se esperaba</h3><ul class="l">
<li><b>«من رجع عن دينه فاستتبه فإن تاب وإلا فاضرب عنقه»</b> (hadiz de Muʿadh con esas palabras): no se halló tal cual en ninguna página leída. Lo más cercano, según mis agentes y sin que yo lo haya leído: una versión de Muʿadh que cita Ibn Hajar («أيما رجل ارتد عن الإسلام فادعه…»), y el relato de ʿUmar a ʿAmr (AP10, cadena «cortada» según el editor).</li>
<li><b>Bujari 6878</b> dice «والمارق من الدين التارك الجماعة»; la fórmula «التارك لدينه المفارق للجماعة» es la de Muslim 1676 y Abu Dawud 4352 (AP03, AP04).</li>
<li><b>ʿUkl y ʿUrayna</b>: solo Bujari 6802 usa «فارتدوا» (palabra del narrador); en 233 y 4192 no aparece «ارتد» (según mi agente Z1; no capturado). Según mi agente, al-Tahawi lo lee como ḥirāba.</li>
<li><b>Musaylima</b>: el hadiz de los enviados (Abu Dawud 2761) lo narra Nuʿaym ibn Masʿud, no Ibn Masʿud; el caso de Ibn Masʿud e Ibn al-Nawwaha es Abu Dawud 2762 (AP11).</li>
<li><b>Ibn Hazm</b> (al-Muhalla 12/163 de Shamela): en esa página trata el caso del hombre que reprochó al Profeta y concluye «la obligación de matar al apóstata», pero su capítulo propio sobre el apóstata no lo he localizado; no lo uso.</li>
<li><b>Ijmāʿ</b>: al-Shafiʿi dice «no discreparon los musulmanes» sobre rescatar o perdonar al apóstata (AP12); Ibn ʿAbd al-Barr, «no hay desacuerdo» sobre el dhimmi (AP14). La frase de Ibn Qudama («أجمع أهل العلم على وجوب قتل المرتد») la vi solo en un escaneo OCR ilegible en el verbo y no la uso; la de Ibn al-Mundhir no se alcanzó.</li>
<li><b>Fuentes que no pude leer</b>: el Muwatta' mismo, ʿAbd al-Razzaq, Saʿid ibn Mansur, la Mudawwana, Ibn Rushd, al-Khiraqi, Ibn al-Qayyim (Ahkam ahl al-dhimma) y las versiones tempranas de Sayf ibn ʿUmar sobre la ridda (fuente muy criticada: no la uso).</li>
</ul></div>
<div class="box ojo"><h3>Lo que no se puede afirmar</h3><ul class="l">
<li><b>«El islam manda matar a cualquiera que cambie de religión.»</b> Demasiado simple: los textos hablan de quien sale del islam, piden en su mayoría el arrepentimiento y no alcanzan al dhimmi que cambia entre religiones (AP14).</li>
<li><b>«Hay unanimidad entre los musulmanes.»</b> No: los hanafíes no matan a las mujeres, hay quien no pide arrepentimiento y quien lo pide siempre, y los modernistas leen la pena como contra el apóstata hostil (AP19, AP22).</li>
<li><b>«El Corán lo ordena.»</b> Ningún comentarista citado (al-Tabari, al-Qurtubi) lo deduce de 2:217, 3:86 o 4:137; al-Sarakhsi invoca 48:16 diciendo «se dijo…» (AP15).</li>
<li><b>«El Profeta mató a los apóstatas.»</b> Los textos capturados no lo muestran tan limpio: Ibn Abi Sarh es perdonado (AP11); Muʿadh y los Compañeros son quienes ejecutan (AP07–AP11); el hadiz de las tres causas dice «sangre lícita», no «mátese» (AP03–AP04).</li>
<li><b>«Estos textos prueban que hoy se aplica la pena.»</b> Eso es otra cuestión: son textos de doctrina clásica; Peters y De Vries (1976-77) escriben que «la apostasía ya no cae bajo el derecho penal» y que la cuestión sigue debatiéndose (AP22).</li>
</ul></div>'''
page('AP00c_es', 'AP00c', 'Apostasía · límites', 'Resumen en español',
     'Qué se comprobó y no salió, qué no se pudo leer, y qué no se puede afirmar',
     'Los resultados negativos importan: dicen hasta dónde llega la afirmación.', 'حدود', NEG,
     'Los agentes de búsqueda (modelo pequeño) no son fuente; solo valen las citas que leí en la página original, y lo señalo donde no es así. Las calificaciones de cadenas son las que imprimen los editores o los sitios, no las mías.<br>Pack «Apostasía en las fuentes islámicas tempranas»')
print('ok')
