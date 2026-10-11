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
 ("Muwatta' de Malik 36-25 y 36-26 (179 H), leído directamente", "«Quien cambie su religión, cortadle el cuello» (mursal) y la explicación de Malik: zanadiqa sin arrepentimiento; el declarado, arrepentimiento y, si no, muerte; ʿUmar y el apóstata de Tustar (plazo de tres días)", "Jurista fundador (texto original)", "AP33, AP34", "ok"),
 ("ʿAbd al-Razzaq (211 H): capítulo de 35 relatos (18768-18802)", "ʿUmar, ʿAli, Ibn Masʿud, ʿUmar ibn ʿAbd al-ʿAziz: ofrecer volver y matar al que se niega (ʿAli a un anciano cristiano converso, Mustawrid); pero Ibn Masʿud destierra a los seguidores de Musaylima y ʿUmar ibn ʿAbd al-ʿAziz deja a unos conversos de la Yazira", "Prácticas de Compañeros y sucesores (con contrarios)", "AP24-AP30", "mid"),
 ("Saʿid ibn Mansur (227 H) 2586-2587 y la Mudawwana de Sahnun (240 H)", "ʿUmar y Tustar con otra cadena; según Anas, su opción era ofrecer volver y, si no, la cárcel. Mudawwana: a la apóstata «se le pide que se arrepienta y, si no, se le corta el cuello»; la muerte cubre los demás castigos; sus bienes van a la comunidad", "Compañero y escuela maliki", "AP31, AP32, AP35, AP36", "mid"),
 ("Ibn al-Mundhir (319 H), Kitab al-Ijmaʿ 719 y 725", "Los sabios convinieron en que, si se pide arrepentimiento y no se arrepiente, se mata; y en aceptar dos testigos (al-Hasan pide cuatro). Fórmula: «no conozco desacuerdo»", "Consenso (fórmula del autor)", "AP37, AP38", "ok"),
 ("Ibn Qudama (620 H), al-Mughni 9/3-6, hanbali", "«Los sabios convinieron en la obligatoriedad de matar al apóstata… y no se rechazó»; la mayoría pide tres días; al-Nakhaʿi («siempre») es «contrario a la sunna y al consenso»; la apostasía nace de una duda; si no se arrepiente, muerte con espada", "Consenso por silencio + posturas", "AP39, AP40, AP41", "ok"),
 ("Ibn Rushd el abuelo (520 H), al-Bayan 16/378-392 y al-Muqaddimat 1/141; Ibn Rushd el nieto (595 H), Bidaya 4/242", "«La muerte se debe por persistir en la incredulidad»; no se conserva de los Compañeros desacuerdo en pedir arrepentimiento (solo en el plazo); Abu Bakr y Umm Qirfa; «acordaron que se mata al hombre»; «consenso de los sabios sin desacuerdo» (frase ambigua)", "Jurista maliki (comparación de escuelas)", "AP42-AP47", "ok"),
]
B = [
 ("¿Se pide arrepentimiento antes?", "La mayoría: sí (Malik y Ahmad: tres días; al-Shafiʿi, dos dichos). ʿUbayd ibn ʿUmayr, Tawus y al-Hasan, y lo que defiende Ibn Taymiyya: no hace falta. Plazos citados: una hora, tres días, veinte noches, un mes, dos meses, cien veces. Ibn Rushd (el abuelo) afirma que de los Compañeros «no se conserva desacuerdo» en pedirlo, solo en el plazo; Ibn Qudama lo apoya en que la apostasía nace de una duda.", "Varía", "AP08, AP17, AP19, AP40, AP41, AP43", "mid"),
 ("¿Se mata a las mujeres?", "Malik (Mudawwana), al-Awzaʿi, al-Shafiʿi, al-Layth, Abu Bakr con Umm Qirfa, y para Ibn Rushd «la mayoría»: sí. Hanafíes (al-Thawri, Abu Hanifa), y transmisiones de ʿAli, al-Hasan y Qatada: no, se las encarcela o esclaviza (hadiz de Ibn Abbas «no se mata a las mujeres»; el editor de Ibn Abi Shayba lo califica de débil: AP23).", "Dividido", "AP05, AP16, AP19, AP22, AP23, AP35, AP39, AP45, AP46", "no"),
 ("¿Es castigo por creer?", "Hanafíes: «matar no es retribución por la apostasía… se debe por la persistencia en la incredulidad… para repeler el combate»; la retribución de la incredulidad va al más allá. Ibn Taymiyya: «el que deja su religión, el que se separa de la comunidad» puede explicarse por el combatiente.", "Lectura alternativa clásica", "AP16, AP18", "mid"),
 ("¿Alcanza al dhimmi que cambia de religión?", "No: «el conjunto de los sabios»: quien pasa del judaísmo al cristianismo, siendo dhimmi, no es muerto (la pena es para quien sale del islam).", "Acotado", "AP14", "mid"),
 ("¿Qué dice el Corán?", "Al-Tabari: el ansari que apostató y preguntó si había arrepentimiento fue aceptado al arrepentirse (3:86); en 4:137, el arrepentimiento se acepta cada vez y «su islam protege su sangre». Al-Qurtubi: 2:217 solo habla de que sus obras se pierden; la pena sale de los hadices.", "En contra (matiz)", "AP19, AP20, AP21", "no"),
 ("Los «consensos»", "Ibn al-Mundhir: «no conozco desacuerdo» (con arrepentimiento previo; testigos: al-Hasan discrepa). Ibn Qudama: «y no se rechazó, fue consenso» (pero en la misma página, las mujeres). Ibn Rushd el nieto: «acordaron que se mata al hombre». Ibn Rushd el abuelo: «sin desacuerdo» (frase ambigua). Cada autor registra a la vez excepciones.", "Consenso con salvedades", "AP37, AP38, AP39, AP46, AP47", "mid"),
 ("Calidad de las cadenas", "Los editores de Ibn Abi Shayba califican de «débiles» o «cortadas» los relatos de ʿUmar (30925), ʿAli (30926), Muʿadh (30930) y ʿUmar a ʿAmr (34937); los de Mustawrid (34960) y Ibn Masʿud-Ibn al-Nawwaha, «ṣaḥīḥ». El hadiz base es de un solo Compañero por un solo transmisor (Ibn Abbas–ʿIkrima).", "Matiz", "AP08–AP10, AP01–AP02", "mid"),
 ("¿Qué hacía ʿUmar con el apóstata?", "Cuatro colecciones (Muwatta', ʿAbd al-Razzaq, Saʿid ibn Mansur, Ibn Abi Shayba) cuentan que reprochó la ejecución de un apóstata en Tustar sin darle plazo; según Anas (Saʿid ibn Mansur 2587), su opción era «ofrecerles volver y, si no, depositarlos en la cárcel». A Ibn al-ʿAs le escribe: arrepentimiento y, si no, córtale el cuello (34937).", "Matiz (importante)", "AP09, AP10, AP24, AP31, AP32, AP34", "no"),
 ("Disidencia clásica", "Ibrahim al-Nakhaʿi: «se le pide arrepentimiento siempre [abadan]» (ʿAbd al-Razzaq 18775, con al-Thawri: «esto adoptamos»; Ibn Qudama: «contrario a la sunna y al consenso») y «cada vez que apostata» (al-Tabari 4:137); ʿUmar ibn ʿAbd al-ʿAziz deja a unos conversos de la Yazira (18792); los modernistas (ʿAbduh, Rida, Shaltut) la leen como pena solo al apóstata hostil.", "Minoritaria / moderna", "AP21, AP22, AP28, AP30, AP41", "mid"),
]
body = f'''<div class="ans"><b>Sí: hay textos tempranos y abundantes.</b> Tres bloques: (1) <b>hadices</b>: «Quien cambie su religión, matadlo» (Ibn Abbas, Bujari 6922 y 3017, Tirmidhi 1458) y «no es lícita la sangre de un musulmán salvo por una de tres… el que deja su religión» (Ibn Masʿud en Bujari 6878 y Muslim 1676; ʿUthman en Abu Dawud 4502); (2) <b>casos y prácticas de los Compañeros</b>: Muʿadh y Abu Musa en Yemen (Bujari 6923), ʿAli y Mustawrid, ʿUmar a ʿAmr ibn al-ʿAs, Ibn Masʿud e Ibn al-Nawwaha; y (3) <b>juristas</b> desde el siglo II H (Malik, al-Shafiʿi, la escuela hanafí con al-Sarakhsi, Ibn ʿAbd al-Barr, al-Qurtubi, Ibn Taymiyya). <b>Ampliación (lectura directa, sin agentes):</b> el Muwatta' mismo, ʿAbd al-Razzaq, Saʿid ibn Mansur, la Mudawwana, Ibn al-Mundhir, Ibn Qudama (la frase del consenso, textual: «los sabios convinieron en la obligatoriedad de matar al apóstata… y no se rechazó») e Ibn Rushd (abuelo y nieto): confirman la doctrina y la matizan. <b>Pero no es un bloque sin matices</b>: casi todos piden primero el arrepentimiento; los hanafíes no matan a las mujeres; los hanafíes razonan la pena como «repeler el combate», no como castigo por creer; el Corán, según al-Tabari y al-Qurtubi, no fija una pena mundana; hay un caso contrario (el ansari de 3:86 es aceptado); y varios relatos tienen cadena débil según sus editores.</div>
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
NEG = '''<div class="box"><h3>Pistas que no salieron como se esperaba, y correcciones tras la lectura directa</h3><ul class="l">
<li><b>«من رجع عن دينه فاستتبه فإن تاب وإلا فاضرب عنقه»</b> (hadiz de Muʿadh con esas palabras): no se halló tal cual en ninguna página leída. Lo más cercano, según mis agentes y sin que yo lo haya leído: una versión de Muʿadh que cita Ibn Hajar («أيما رجل ارتد عن الإسلام فادعه…»), y el relato de ʿUmar a ʿAmr (AP10, cadena «cortada» según el editor).</li>
<li><b>Bujari 6878</b> dice «والمارق من الدين التارك الجماعة»; la fórmula «التارك لدينه المفارق للجماعة» es la de Muslim 1676 y Abu Dawud 4352 (AP03, AP04).</li>
<li><b>ʿUkl y ʿUrayna</b>: solo Bujari 6802 usa «فارتدوا» (palabra del narrador); en 233 y 4192 no aparece «ارتد» (según mi agente Z1; no capturado). Según mi agente, al-Tahawi lo lee como ḥirāba.</li>
<li><b>Musaylima</b>: el hadiz de los enviados (Abu Dawud 2761) lo narra Nuʿaym ibn Masʿud, no Ibn Masʿud; el caso de Ibn Masʿud e Ibn al-Nawwaha es Abu Dawud 2762 (AP11).</li>
<li><b>Ibn Hazm</b> (al-Muhalla 12/163 de Shamela): en esa página trata el caso del hombre que reprochó al Profeta y concluye «la obligación de matar al apóstata», pero su capítulo propio sobre el apóstata no lo he localizado; no lo uso.</li>
<li><b>Corrección: al-Nakhaʿi «yustatab abadan»</b>. Antes dije que no la había encontrado y que lo de al-Tabari («cada vez que apostata») no era lo mismo. Ahora leí la formulación «se le pide arrepentimiento siempre» en ʿAbd al-Razzaq 18775 (AP28), con al-Thawri («esto adoptamos»), y la cita Ibn Qudama (AP41). Existe; no sé si equivale a «cada vez que apostata».</li>
<li><b>Corrección: Mustawrid al-ʿIjli</b>. Antes dije que solo aparecía en Ibn Abi Shayba. Está también en ʿAbd al-Razzaq 18788 y 18789 (AP26); según mis agentes, no figura en Tabari ni al-Baladhuri (no lo comprobé).</li>
<li><b>Ijmāʿ de Ibn Qudama</b>: «وأجمع أهل العلم على وجوب قتل المرتد» lo vi antes solo en un escaneo ilegible y no lo usaba. Ahora lo leí yo en Shamela, edición Maktabat al-Qahira, vol. 9 p. 3 (AP39): la frase es esa, textual, seguida de «y no se rechazó, así que fue consenso». En la misma página trae las excepciones sobre las mujeres.</li>
<li><b>Ibn Rushd</b>: la Bidaya no tiene tratado propio de la apostasía, solo una sección breve al final de la hiraba (AP46); el desarrollo está en al-Bayan wa-l-tahsil (AP42-AP45); en las Muqaddimat solo una frase incidental (AP47).</li>
<li><b>Saʿid ibn Mansur</b>: en el volumen de la edición Aʿzami que cubre «Faraʾid → Yihad» (Shamela 13122), recorrí todo el Kitab al-yihad buscando «مرتد/ارتد/استتاب»: no hay capítulo de la apostasía; solo 2586 y 2587 (ʿUmar y Tustar), y 2832-2834 (un prisionero que se hace cristiano: efecto sobre el matrimonio y la herencia, no su muerte).</li>
<li><b>Mudawwana</b>: recorrí las 2437 páginas de Shamela buscando «مرتد/استتاب/ارتد/زنديق»: no hay capítulo propio; las menciones son incidentales (matrimonio, tadbir, herencia, qadhf, jawarij). Lo útil: AP35 y AP36.</li>
<li><b>Ijmāʿ de al-Shafiʿi e Ibn ʿAbd al-Barr</b>: al-Shafiʿi dice «no discreparon los musulmanes» sobre rescatar o perdonar al apóstata (AP12); Ibn ʿAbd al-Barr, «no hay desacuerdo» sobre el dhimmi (AP14).</li>
<li><b>Sigue sin leer</b>: al-Khiraqi, Ibn al-Qayyim (Ahkam ahl al-dhimma), Ibn al-Mundhir fuera de al-Ijmaʿ (al-Awsat, al-Ishraf), el resto de Saʿid ibn Mansur (otros volúmenes, como el de tafsir, no los busqué) y las versiones tempranas de Sayf ibn ʿUmar sobre la ridda (fuente muy criticada: no la uso).</li>
</ul></div>
<div class="box ojo"><h3>Lo que no se puede afirmar</h3><ul class="l">
<li><b>«El islam manda matar a cualquiera que cambie de religión.»</b> Demasiado simple: los textos hablan de quien sale del islam, piden en su mayoría el arrepentimiento y no alcanzan al dhimmi que cambia entre religiones (AP14).</li>
<li><b>«Hay unanimidad entre los musulmanes.»</b> No: los hanafíes no matan a las mujeres, hay quien no pide arrepentimiento y quien lo pide siempre, y los modernistas leen la pena como contra el apóstata hostil (AP19, AP22). Ibn al-Mundhir, Ibn Qudama e Ibn Rushd hablan de «consenso» pero cada uno registra a la vez excepciones con nombre (al-Hasan sobre los testigos; Abu Hanifa y transmisiones de ʿAli, al-Hasan y Qatada sobre las mujeres; ʿUbayd ibn ʿUmayr, Tawus y al-Nakhaʿi sobre el arrepentimiento: AP37-AP41, AP43, AP46).</li>
<li><b>«El Corán lo ordena.»</b> Ningún comentarista citado (al-Tabari, al-Qurtubi) lo deduce de 2:217, 3:86 o 4:137; al-Sarakhsi invoca 48:16 diciendo «se dijo…» (AP15).</li>
<li><b>«El Profeta mató a los apóstatas.»</b> Los textos capturados no lo muestran tan limpio: Ibn Abi Sarh es perdonado (AP11); Muʿadh y los Compañeros son quienes ejecutan (AP07–AP11); el hadiz de las tres causas dice «sangre lícita», no «mátese» (AP03–AP04).</li>
<li><b>«Estos textos prueban que hoy se aplica la pena.»</b> Eso es otra cuestión: son textos de doctrina clásica; Peters y De Vries (1976-77) escriben que «la apostasía ya no cae bajo el derecho penal» y que la cuestión sigue debatiéndose (AP22).</li>
</ul></div>'''
page('AP00c_es', 'AP00c', 'Apostasía · límites', 'Resumen en español',
     'Correcciones, lo que no salió, lo que sigue sin leer y lo que no se puede afirmar',
     'Los resultados negativos importan: dicen hasta dónde llega la afirmación.', 'حدود', NEG,
     'Los agentes de búsqueda (modelo pequeño) no son fuente; solo valen las citas que leí en la página original, y lo señalo donde no es así. Las calificaciones de cadenas son las que imprimen los editores o los sitios, no las mías.<br>Pack «Apostasía en las fuentes islámicas tempranas»')
D = [
 ("Muwatta' de Malik (recensión de Yahya), 36-25 y 36-26 — hadithunlocked.com", "Hadiz mursal de Zayd ibn Aslam «quien cambie su religión, cortadle el cuello» con la explicación de Malik (zanadiqa sin plazo; declarado: arrepentimiento y, si no, muerte; no alcanza a quien cambia entre otras religiones) y el relato de ʿUmar y el apóstata de Tustar.", "Leído y capturado", "AP33, AP34", "ok"),
 ("ʿAbd al-Razzaq, Musannaf, capítulo «Bab fi l-kufr baʿd al-iman» (18768-18802: 35 relatos) — hadithunlocked.com", "Leídos los 35. Capturados 7: ʿUmar y Tustar (18773), ʿAli y el anciano cristiano (18787), Mustawrid (18788), Ibn Masʿud y los de Musaylima (18786), al-Nakhaʿi «abadan» (18775), ʿUmar ibn ʿAbd al-ʿAziz (18791, 18792). Sin capturar: ʿAta', ʿAli (un mes), ʿUthman (tres días), al-Zuhri, ʿUbayd ibn ʿUmayr («se mata»), Tawus («no se le acepta salvo con su sangre»), las tres causas, Muʿadh, Ibn Abbas, ʿAli y los zanadiqa, y las guerras de la ridda.", "Leído; 7 capturados", "AP24-AP30", "ok"),
 ("Saʿid ibn Mansur, Sunan (ed. al-Aʿzami), Shamela 13122: volumen «Faraʾid → Yihad»", "Recorrí todo el Kitab al-yihad (pp. 2293-3074): no hay capítulo de apostasía; aparecen 2586 y 2587 (ʿUmar y Tustar; según Anas, «los habría depositado en la cárcel») y 2832-2834 (prisionero que se hace cristiano).", "Leído; 2 capturados", "AP31, AP32", "ok"),
 ("Mudawwana de Sahnun, Shamela 587 (2437 páginas recorridas)", "Sin capítulo propio. Útil: 2/55 (la apóstata se mata si no se arrepiente) y 2/227-228 (la muerte cubre los demás castigos; los bienes van a la comunidad). También el apartado sobre los jawarij (1/530-531: «que se arrepientan o los maten»): no es apostasía.", "Leído; 2 capturados", "AP35, AP36", "ok"),
 ("Ibn al-Mundhir, Kitab al-Ijmaʿ, Shamela 151100: «Kitab al-murtadd», 717-725", "719 (consenso: si no se arrepiente, se mata) y 725 (dos testigos; solo al-Hasan discrepa). También 720 (quien insulta al Profeta: la muerte) y 724 (nadie impone un castigo al que vuelve), sin capturar.", "Leído; 2 capturados", "AP37, AP38", "ok"),
 ("Ibn Qudama, al-Mughni (ed. Maktabat al-Qahira), Shamela 8463: vol. 9 pp. 3-7", "La frase del consenso, legible y textual (p. 3); mujeres, tres días, al-Nakhaʿi «siempre» (contrario a la sunna y al consenso), la apostasía por duda, espada y no fuego, el zindiq y la repetición, Ibn Masʿud e Ibn al-Nawwaha.", "Leído; 5 capturas", "AP39-AP41", "ok"),
 ("Ibn Rushd el abuelo, al-Bayan wa-l-tahsil, Shamela 21751: vol. 16 pp. 359-445; al-Muqaddimat, Shamela 21735", "«La muerte se debe por persistir en la incredulidad»; plazo de tres días; no se conserva desacuerdo de los Compañeros en pedir arrepentimiento; zindiq; Abu Bakr y Umm Qirfa; mujeres. Muqaddimat: frase incidental «consenso de los sabios sin desacuerdo».", "Leído; 7 capturas", "AP42-AP45, AP47", "ok"),
 ("Ibn Rushd el nieto, Bidayat al-mujtahid, Shamela 21739 (944 páginas recorridas)", "Una sección breve en el libro de la hiraba: «acordaron que se mata al hombre»; discrepancias sobre la mujer y el arrepentimiento. Sin otro tratamiento.", "Leído; 1 captura", "AP46", "ok"),
]
body3 = f'''<div class="ans"><b>Cómo se hizo.</b> Descargué las páginas originales, las busqué con las palabras «مرتد / ارتد / يستتاب / زنديق / الردة» y leí yo mismo los pasajes: <b>no se usó ningún agente</b> para esta ampliación. Las capturas en árabe son de la página original; las traducciones son literales y mías, con las correcciones o dudas señaladas en cada tarjeta.</div>
<h2 class="g">Fuentes que no había podido leer antes y ahora sí</h2>{table(D, ("Fuente y lugar", "Qué se leyó y qué aporta", "Estado", "Tarjetas"))}'''
page('AP00d_es', 'AP00d', 'Apostasía · lectura directa', 'Resumen en español',
     'Lo que ahora he leído yo mismo: fuente, página y qué aporta',
     "Muwatta', ʿAbd al-Razzaq, Saʿid ibn Mansur, Mudawwana, Ibn al-Mundhir, Ibn Qudama e Ibn Rushd", 'قراءة', body3,
     'Las calificaciones de cadenas que se mencionan son las que imprime el sitio o el editor, no las mías. Textos de Shamela y hadithunlocked.com (páginas web, no ediciones impresas, salvo donde se cita volumen y página).<br>Pack «Apostasía en las fuentes islámicas tempranas»')
print('ok')
