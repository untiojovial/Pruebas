# -*- coding: utf-8 -*-
# Páginas de resumen del pack NQ (la mujer «deficiente en razón y religión»): NQ00, NQ00b, NQ00c, NQ00d
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
OUT = 'nqcards'
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

# ---------- NQ00: el hadiz y sus variantes ----------
A = [
 ("Bujari 304 (256 H) · Abu Saʿid al-Judri", "«ناقصات عقل ودين، أذهب للب الرجل الحازم من إحداكن». Explica el Profeta: «deficiencia de razón» = el testimonio de la mujer, «como la mitad del testimonio del hombre»; «deficiencia de religión» = no reza ni ayuna menstruando", "Muttafaq ʿalayh", "NQ01", "ok"),
 ("Muslim 79 · Ibn ʿUmar", "«أغلب لذي لب منكن». «El testimonio de dos mujeres equivale al de un hombre; esa es la deficiencia de la razón»; «permanece noches sin rezar y rompe el ayuno en Ramadán: esa es la deficiencia de la religión»", "Sahih (Muslim)", "NQ02", "ok"),
 ("Bujari 2658 · Abu Saʿid", "Solo la parte del testimonio, en el Libro de los testimonios", "Misma cadena que 304", "NQ03", "ok"),
 ("Bujari 1462 · Abu Saʿid · Zaynab", "La frase y, después, la consulta de Zaynab (mujer de Ibn Masʿud) sobre su limosna", "Sahih", "NQ04", "ok"),
 ("Abu Dawud 4679 · Ibn ʿUmar", "Variante «ناقصات عقل ولا دين»; mismas dos explicaciones", "Sahih (al-Albani)", "NQ05", "ok"),
 ("Tirmidhi 2613 · Abu Huraira", "«أغلب لذوي الألباب وذوي الرأي»; la menstruación: «tres y cuatro [días]»", "Sahih (al-Albani)", "NQ06", "ok"),
 ("Ahmad 8862 · Abu Huraira", "Variante «nawaqis ʿuqul» (plural); Zaynab pregunta qué es la deficiencia; texto impreso termina «…شهادة المرأة نصف شهادة» (sin «الرجل»)", "Cadena buena (Shuʿayb)", "NQ07", "mid"),
 ("Ibn Hibban 3323 · Ibn Masʿud", "«Dijo ʿAbd Allah: no hay entre los deficientes en razón y religión quienes más dominen a los hombres con mando sobre su asunto que las mujeres»; testimonio y días sin rezar. No queda claro si cita al Profeta", "Débil (Shuʿayb)", "NQ08", "mid"),
 ("Ibn Abi Shayba 31048 · Ibn Masʿud", "En primera persona de Ibn Masʿud, «deficiente en religión y criterio», sin «قال رسول الله»", "Sin grado en el sitio", "NQ09", "mid"),
 ("Nasaʾi 4805 · ʿAmr ibn Shuʿayb", "«El ʿaql de la mujer es como el ʿaql del hombre hasta que alcanza un tercio de su diya» (ʿaql = diya)", "Débil", "NQ10", "no"),
 ("Bayhaqi 16407 · ʿAli (por Ibrahim al-Nakhaʿi)", "«El ʿaql de la mujer es la mitad del ʿaql del hombre en la vida y en lo que es menos»: la fórmula más cercana a «mitad de razón» que existe, y es de derecho penal (diya)", "Cadena cortada", "NQ11", "no"),
 ("Bujari 3411 · Muslim 2431 · Abu Musa", "«Han alcanzado la perfección muchos hombres, y de las mujeres solo Asiya y Maryam»; ʿAʾisha por encima de las demás «como el tharid»", "Muttafaq ʿalayh", "NQ12", "ok"),
 ("Bujari 4425 · Abu Bakra", "«No prosperará un pueblo que confíe su gobierno a una mujer» (otro tema: gobierno)", "Sahih (otro tema)", "NQ13", "no"),
 ("Abu Dawud 236 · ʿAʾisha", "«Las mujeres son las hermanas gemelas de los hombres» (contexto: baño ritual)", "Discutido", "NQ14", "mid"),
 ("Bujari 2731 · Tirmidhi 3883", "Umm Salama aconseja y el Profeta lo sigue en Hudaybiya; Abu Musa: los Compañeros hallaban conocimiento en ʿAʾisha", "Sahih / hasan sahih", "NQ15, NQ16", "ok"),
]
body = f'''<div class="ans"><b>El hadiz existe, pero no dice «la mitad de inteligencia».</b> El texto (Bujari 304, 1462, 2658; Muslim 79; Abu Dawud 4679; Tirmidhi 2613; Ahmad 8862) dice que las mujeres son <b>«naqisat ʿaql wa-din»</b>, «deficientes en razón y religión», y <b>el propio Profeta lo explica</b>: la «deficiencia de razón» es que <b>el testimonio de dos mujeres equivale al de un hombre</b> (Corán 2:282); la «deficiencia de religión» es que <b>no rezan ni ayunan cuando menstrúan</b>. La búsqueda de «نصف عقل» («mitad de razón») dio resultado <b>negativo</b> en todos los hadices y comentarios leídos. La fórmula más parecida es de <b>derecho penal</b>: «el ʿaql de la mujer es la mitad del ʿaql del hombre», pero ahí <b>ʿaql significa diya</b> (precio de sangre; Bayhaqi 16407, atribuido a ʿAli, con cadena cortada; Nasaʾi 4805, débil). <b>Pero no basta con eso</b>: el texto sí dice «deficientes en razón», y varios exégetas y juristas de primer orden —al-Razi, al-Baydawi, Ibn Kathir, Ibn Qudama, al-Alusi— lo generalizaron a una superioridad intelectual del hombre; mientras que otros —al-Mazari, al-Nawawi, Ibn Taymiyya, Ibn al-Qayyim— lo limitan a la <b>precisión al retener (dabt) en el testimonio</b>; y en el siglo XIX, Tahtawi, ʿAbduh y Qasim Amin discuten la causa (ignorancia y falta de educación, no naturaleza). Cada punto remite a una tarjeta con la página original.</div>
<h2 class="g">1 · El hadiz, sus variantes y los textos relacionados</h2>{table(A, ("Fuente", "Qué dice", "Grado / nota", "Tarjeta"))}'''
page('NQ00_es', 'NQ00', 'Mujer · razón y testimonio', 'Resumen en español',
     '¿Dice el islam que la mujer tiene «la mitad de inteligencia»? Lo que dice el hadiz de las «deficientes en razón y religión», sus variantes y textos parecidos',
     'Comprobado en las páginas originales (hadithunlocked, Shamela, comentarios coránicos en línea, escaneos de archive.org); con 8 agentes de búsqueda cuyos hallazgos revisé yo.', 'نقص العقل', body,
     'Colores de la columna «Grado / nota»: verde = texto firme · ocre = texto con variante o cadena discutida · rojo = otro significado de «ʿaql» (diya) o de otro tema.<br>Pack «La mujer ‹deficiente en razón y religión›: el hadiz, sus variantes y lo que dijeron los sabios hasta el siglo XIX»')

# ---------- NQ00b: lo que dijeron los sabios, por época ----------
B = [
 ("Ibn Masʿud (Ibn Abi Shayba; Ibn Hibban)", "«No he visto… deficiente en religión y criterio…»; las dos explicaciones: menstruación y testimonio de dos mujeres con un hombre", "Limita al testimonio", "NQ08, NQ09", "mid"),
 ("ʿUmar, ʿAli, Ibn ʿUmar, al-Zuhri, Makhul, al-Shaʿbi, Shurayh (vía Ibn al-Qayyim)", "Dos clases de testimonio: a solas, en lo que solo ellas ven; con hombres, en dinero; no en divorcio, matrimonio, sangres ni penas fijas. Sin hablar de razón. Relatos que admiten el testimonio de cuatro (ʿUmar), diez (ʿAli) u ocho mujeres (ʿAtaʾ)", "Limita; con variación", "NQ17, NQ20, NQ21", "mid"),
 ("Tawus y ʿAtaʾ (ʿAbd al-Razzaq)", "Las mujeres testifican con los hombres «en todo»; la excepción del adulterio es por recato, no por razón; ʿAtaʾ admite hasta dos mujeres + tres hombres en el adulterio", "Cualifica", "NQ18, NQ19", "ok"),
 ("Malik (179 H)", "Tabla: no con un hombre ni sin él en talión, penas fijas, matrimonio, divorcio…; sí en deudas y bienes; solas en el parto, la lactancia, los defectos de las mujeres", "Limita al testimonio", "NQ22", "mid"),
 ("Nahj al-balagha, sermón 80 (atribuido a ʿAli; compilación de al-Radi, m. 406 H), en transcripción de un foro", "«Las mujeres son deficientes en fe, en parte y en razones»: la fe = menstruación; la parte = herencia, la mitad; las razones = el testimonio de dos mujeres = uno de hombre", "Limita a reglas legales (fuente débil)", "NQ53", "mid"),
 ("Wahb ibn Munabbih, en Ibn Qutayba (m. 276 H)", "«Dios castigó a la mujer con diez cosas… la hizo deficiente en razón y religión… y no habrá profeta entre ellas»; sin cadena", "Generaliza (como castigo)", "NQ23", "no"),
 ("Abu ʿUbayd (224 H) y al-Tabari (310 H)", "«Dalal» en 2:282 = olvido de una parte del testimonio; explicación por el olvido, no por «razón»", "Limita al testimonio", "NQ24, NQ25", "mid"),
 ("al-Maturidi (333 H)", "Las mujeres «fueron hechas» para el descuido y la «deficiencia de razón y religión» → duda en los hudud → no valen en ellos", "Generaliza (en el testimonio)", "NQ26", "no"),
 ("al-Jattabi (388 H)", "El fundamento del testimonio es la razón con la honradez; el testimonio del «descuidado» es débil aunque sea piadoso", "Limita al testimonio", "NQ36", "mid"),
 ("Ibn Hazm (456 H)", "Acepta «dos mujeres = un hombre» solo por mandato textual; niega diferencia racional en mentir o descuidarse; tacha de débil la «sunna» de al-Zuhri; restringe «no prosperará…» al califato; sostiene que hubo profetisas (Maryam, la madre de Musa, la de Isaac)", "Cualifica o rechaza", "NQ43–NQ46", "ok"),
 ("al-Mazari (536 H) y al-Nawawi (676 H)", "«Esa es la deficiencia de la razón» = «señal» de ella; «ellas son escasas en precisión»; la «deficiencia de religión» puede ser un mandato; discrepancia sobre qué es la razón", "Limita a la precisión", "NQ39, NQ40", "mid"),
 ("al-Razi (606 H)", "2:282: «el olvido prevalece en la naturaleza de las mujeres» (frío y humedad); 4:34: «no hay duda de que las razones de los hombres y sus conocimientos son más»", "Generaliza (naturaleza)", "NQ28, NQ30", "no"),
 ("Ibn Qudama (620 H)", "«La mujer es deficiente en razón y escasa en criterio»; no juez, no gobernante, ni su testimonio «aunque hubiera con ella mil mujeres» sin un hombre", "Generaliza", "NQ42", "no"),
 ("al-Qurtubi (671 H)", "Abu ʿUbayd: dalal = olvido parcial; y «lo correcto es que Maryam es profetisa»", "Limita / cualifica", "NQ25, NQ47", "ok"),
 ("al-Baydawi (c. 685 H)", "2:282: «indicio de la deficiencia de su razón y la escasa precisión»; 4:34: «perfección de la razón y buen gobierno» de los hombres → profecía, imamato, testimonio…", "Generaliza (4:34)", "NQ27, NQ31", "no"),
 ("Ibn Taymiyya (728 H) e Ibn al-Qayyim (751 H)", "«La mitad de su testimonio es por la debilidad de la razón, no de la religión»; la ʿadala de la mujer es igual a la del hombre; sin riesgo de olvido, sin «mitad»; la mujer «en la mitad» en cinco juicios (testimonio, herencia, diya, ʿaqiqa, manumisión)", "Limita a la precisión", "NQ48, NQ49", "mid"),
 ("Ibn Kathir (774 H)", "2:282: «por la deficiencia de la razón de la mujer» (patrimonial); 4:34: «el hombre es mejor que la mujer; por eso la profecía es solo de hombres»", "Limita (2:282); generaliza (4:34)", "NQ29, NQ32", "no"),
 ("Ibn Hayar (852 H) y al-ʿAyni (855 H)", "«Sin reproche ni censura»; la escasa precisión indica deficiencia de razón; «proviene de la creación original»; el pecado va ligado a la ingratitud, no a la deficiencia; rechazan que ʿaql sea diya", "Limita a la precisión; la ve innata", "NQ37, NQ38, NQ41", "mid"),
 ("al-Shawkani (1250 H / 1834)", "2:282: «por la debilidad de las mujeres»; 4:34: cargos de gobierno y guerra (sin «razón» ni «religión»)", "Limita", "NQ34", "mid"),
 ("al-Alusi (1270 H / 1854)", "«Ha llegado que son deficientes en razón y religión y los hombres lo contrario»; por eso la profecía y el mensaje «según lo más conocido»", "Generaliza", "NQ33", "no"),
 ("Tahtawi (1290 H / 1873)", "La «ligereza de razón» de las mujeres viene de la ignorancia; los dichos sobre «la falta de perfección de sus razones» «no se aplican a todas las mujeres»; defiende enseñarles a escribir", "Cualifica o rechaza", "NQ51", "ok"),
 ("Siddiq Hasan Jan (1307 H / 1890)", "Añade «por la deficiencia de su razón y su precisión» (2:282) y «el exceso de razón y de religión» (4:34) a lo que decía al-Shawkani", "Generaliza", "NQ35", "no"),
 ("Muhammad ʿAbduh / Rida, Manar (m. 1905)", "Rechaza la explicación por el temperamento («no comprobada»); la causa es no ocuparse de las finanzas; en lo doméstico, su memoria es mejor que la del hombre", "Cualifica (causa social)", "NQ50", "ok"),
 ("Qasim Amin (1899; m. 1908)", "Concede que «la mujer ahora es deficiente en razón y muy astuta» pero es «efecto de la ignorancia y la decadencia»; la educación es el remedio", "Cualifica (causa social)", "NQ52", "ok"),
]
body2 = f'''<h2 class="g">2 · Qué dijeron los sabios, por orden de época aproximada</h2>{table(B, ("Sabio / fuente", "Qué dice", "Lectura", "Tarjeta"))}'''
page('NQ00b_es', 'NQ00b', 'Mujer · razón y testimonio · sabios', 'Resumen en español',
     'Lo que dijeron los sabios tempranos, medievales y del siglo XIX sobre «la deficiencia de razón» de la mujer',
     'Cada fila remite a una tarjeta con la página original. «Lectura» es mi clasificación del pasaje concreto leído, no una etiqueta de toda la obra del autor.', 'علماء', body2,
     'Colores de la columna «Lectura»: rojo = atribuye a la naturaleza o al género una inferioridad de razón más allá de la regla del testimonio · ocre = la limita al testimonio, a la precisión al retener o a reglas legales · verde = la cualifica o la rechaza.<br>Pack «La mujer ‹deficiente en razón y religión›: el hadiz, sus variantes y lo que dijeron los sabios hasta el siglo XIX»')

# ---------- NQ00c: lecturas y qué se puede afirmar ----------
C = '''<div class="box"><h3>Cuatro lecturas en la tradición</h3><ul class="l">
<li><b>1 · «Deficiencia = regla del testimonio / precisión (dabt)».</b> Al-Jattabi, al-Mazari, al-Nawawi, Ibn Hayar, al-ʿAyni, Ibn Taymiyya, Ibn al-Qayyim (NQ36, NQ37, NQ39–NQ41, NQ48–NQ49). Ibn Taymiyya: la mitad es por la razón (la precisión), no por la religión; la rectitud de la mujer es igual a la del hombre; donde no se teme el olvido (parto, lactancia, lo que ven), no hay «mitad».</li>
<li><b>2 · «Superioridad general del hombre en la razón».</b> Al-Razi (4:34: «no hay duda…»), al-Baydawi (4:34), Ibn Qudama, Ibn Kathir (4:34), al-Alusi, Siddiq Hasan Jan (NQ28, NQ30–NQ33, NQ35, NQ42). Se usa para el imamato, la judicatura y hasta la profecía.</li>
<li><b>3 · «ʿAql = diya».</b> Referida por Ibn al-Tin, «de algunos», y rechazada por Ibn Hayar y al-ʿAyni («el contexto lo rechaza», NQ37, NQ41). Existe, en cambio, el uso real de «ʿaql» como diya (NQ10, NQ11).</li>
<li><b>4 · «La causa es social o de costumbre».</b> Tahtawi, ʿAbduh y Qasim Amin (NQ50–NQ52). Los dos primeros no niegan la regla ni la premisa del olvido en finanzas; Qasim Amin concede la «deficiencia» como hecho de su época y la declara efecto de la ignorancia. <b>Ojo:</b> Ibn Hayar (NQ37) ve la misma «deficiencia» como «de la creación original».</li>
</ul></div>
<div class="box"><h3>Lo que se puede afirmar con base en lo leído</h3><ul class="l">
<li>El hadiz de las «naqisat ʿaql wa-din» es de Bujari y Muslim, con variantes de cuatro Compañeros (Abu Saʿid, Ibn ʿUmar, Abu Huraira, Ibn Masʿud); <b>en ningún texto leído aparece «mitad de inteligencia»</b>.</li>
<li>En los textos más firmes (NQ01, NQ02, NQ03), el propio Profeta explica la «deficiencia de razón» por la regla del testimonio y la «de religión» por no rezar ni ayunar durante la menstruación. Ibn Hayar y al-Nawawi aclaran que ni lo uno ni lo otro es, en sí, motivo de reproche o pecado (NQ37, NQ38, NQ40).</li>
<li>La tradición <b>no es unánime</b>: unos limitan el motivo a la precisión (Ibn Taymiyya, al-Mazari), otros lo generalizan (al-Razi, Ibn Qudama, al-Alusi); en el siglo XIX unos lo refuerzan (Siddiq Hasan Jan) y otros lo atribuyen a la ignorancia (Tahtawi, ʿAbduh, Qasim Amin).</li>
<li>Las propias reglas jurídicas son más variadas que «dos mujeres = un hombre»: a solas valen en lo que solo ellas ven (NQ20, NQ22, NQ49); Tawus y ʿAtaʾ las aceptan con los hombres «en todo»; ʿUmar y ʿAli habrían admitido su testimonio en un divorcio y en un homicidio (NQ21); Ibn Hazm niega que se base en psicología (NQ44).</li>
</ul></div>
<div class="box ojo"><h3>Lo que no se puede afirmar</h3><ul class="l">
<li><b>«Todos los musulmanes creen que la mujer tiene la mitad de inteligencia.»</b> No: la fórmula no está en los textos leídos, y los sabios que la tratan la limitan a la precisión en el testimonio o discuten su causa.</li>
<li><b>«El islam nunca ha dicho que las mujeres sean inferiores en razón.»</b> Tampoco: el hadiz dice «deficientes en razón», y exégetas de primer orden lo generalizaron (NQ28, NQ30–NQ33, NQ35, NQ42). La lectura restringida tiene respaldo clásico, pero no es la única.</li>
<li><b>«El hadiz es débil.»</b> No: está en Bujari y Muslim (solo son débiles las variantes de Ibn Masʿud en Ibn Hibban 3323 según Shuʿayb, y los textos de «ʿaql = diya»).</li>
<li><b>«En el hadiz, ʿaql significa diya.»</b> Es una lectura que Ibn Hayar y al-ʿAyni rechazan.</li>
<li><b>«El Corán dice que la mujer olvida más.»</b> 2:282 dice «para que si una de ellas se extravía, la otra la recuerde» y ya; atribuirlo a su naturaleza (al-Razi, humores) o a la falta de dedicación (ʿAbduh) es interpretación.</li>
</ul></div>'''
page('NQ00c_es', 'NQ00c', 'Mujer · razón y testimonio · lecturas', 'Resumen en español',
     'Cuatro lecturas del hadiz, y lo que se puede y no se puede afirmar',
     'Resumen de lo comprobado en las tarjetas NQ01–NQ53.', 'قراءات', C,
     'Todas las afirmaciones remiten a una tarjeta con la página original; las clasificaciones («generaliza», «limita») son mías y se refieren al pasaje leído.<br>Pack «La mujer ‹deficiente en razón y religión›: el hadiz, sus variantes y lo que dijeron los sabios hasta el siglo XIX»')

# ---------- NQ00d: lo que leí, lo que no, correcciones ----------
D = [
 ("hadithunlocked.com: Bujari 304, 1462, 2658, 2731, 3411, 4425; Muslim 79; Abu Dawud 236, 4679; Tirmidhi 2613, 3883; Ahmad 8862; Ibn Hibban 3323; Ibn Abi Shayba 31048; Nasaʾi 4805; Bayhaqi 16407; ʿAbd al-Razzaq 15478, 15486, 15487", "Texto árabe, cadena y calificaciones que imprime el sitio (a veces con otro número de edición)", "Leído y capturado", "NQ01–NQ19", "ok"),
 ("Shamela: Ibn Hayar (Fath al-bari 1/406–407), al-Nawawi (2/66–68), al-ʿAyni (3/271), al-Jattabi (1/316), Ibn Qutayba (ʿUyun al-ajbar 4/110–111), Ibn Qudama (Mugni 10/36), Ibn Hazm (Muhalla 8/487–488 y 528; Fisal 5/12–13), Ibn al-Qayyim (Turuq pp. 126–131), Rida (Manar 3/103–104)", "Página con volumen y número de página visibles en la fuente", "Leído y capturado", "NQ20–NQ23, NQ36–NQ50", "ok"),
 ("Exégesis en línea: al-Tabari, al-Qurtubi (2:282 y 3:42), Ibn Kathir (2:282, 4:34), al-Baydawi, al-Razi, al-Maturidi, al-Alusi, al-Shawkani, Siddiq Hasan Jan", "Texto de las páginas web de comentarios (sin paginación impresa)", "Leído y capturado", "NQ24–NQ35, NQ47", "ok"),
 ("Foro de la Atabat al-ʿAbbasiyya (forums.alkafeel.net): sermón 80 del Nahj al-balagha", "Texto del sermón copiado por un usuario del foro; no es una edición con volumen y página; lo marco «fuente secundaria»", "Leído y capturado (fuente débil)", "NQ53", "mid"),
 ("archive.org: Tahtawi (al-Murshid al-amin, 1872, ed. 2012, pp. 143–144) y Qasim Amin (Tahrir al-mar’a, 1899, ed. 1996, p. 55)", "Localizados por mi agente en el texto OCR; yo descargué las imágenes de página, comprobé que son legibles y dibujé el resaltado con las coordenadas del OCR", "Leído y capturado (imagen)", "NQ51, NQ52", "mid"),
]
F = [
 ("Ibn Rushd (Averroes), comentario a la República de Platón (traducción inglesa) sobre las capacidades de las mujeres", "Pista de agente (OCR de archive.org); no leída", "Sin verificar", "—", "no"),
 ("Qadi ʿIyad (Ikmal al-muʿlim), Ibn Battal, al-Kirmani, ʿAli al-Qari (Mirqat), al-Mubarakfuri (Tuhfat al-ahwadhi), al-Shafiʿi (Umm), al-Sarakhsi, al-Kasani, al-Mawardi, al-Yuwayni, Ibn ʿAbidin, Ibn ʿAbd Rabbih (ʿIqd), al-Zarkashi (al-Ijaba)", "Pasajes que mis agentes sacaron de escaneos OCR (muchos ilegibles) o de textos que yo no abrí. Dejo estas fuentes como pistas, no como citas", "Sin leer", "—", "no"),
 ("Mudawwana de Sahnun y Ibn Abi Shayba (directamente)", "Solo los cito a través de Ibn al-Qayyim; no leí el original", "Segunda mano", "NQ20–NQ22", "mid"),
]
G = [
 ("Fórmula «نصف عقل» («mitad de razón»)", "Busqué en los hadices y comentarios leídos: no aparece como dicho del Profeta. Solo hay «ʿaql = diya» en derecho penal (NQ10, NQ11)", "Resultado negativo", "NQ10, NQ11", "mid"),
 ("Páginas del Manar que citaba mi agente (3/124–125)", "En la edición de Shamela que leí, ʿAbduh sobre 2:282 está en 3/103–104; las páginas que decía el agente corresponden a 2:286. Corregido", "Corrección", "NQ50", "mid"),
 ("Califa «no prosperará…» y «la profecía solo de hombres»", "No son textos sobre inteligencia: los incluyo porque los exégetas los encadenan con la «perfección de la razón» (NQ31–NQ33)", "Aclaración", "NQ13, NQ31–NQ33", "mid"),
 ("Anotaciones de grado en hadithunlocked", "El sitio muestra a veces notas de crítica bajo otro número (p. ej., 4818 para Nasaʾi 4805; 8938 para Ahmad 8862): las cito con reserva", "Cautela", "NQ07, NQ10, NQ11", "mid"),
 ("Fechas de muerte de los autores", "Las pongo de memoria (dato general) salvo donde la página las muestra; al-Baydawi (685 o 691 H) no lo verifiqué", "Cautela", "—", "mid"),
]
body3 = f'''<div class="ans"><b>Cómo se hizo.</b> Ocho agentes de búsqueda (modelo pequeño) dieron unas 275 pistas; <b>solo cuenta lo que yo abrí y leí en la página original</b> (hadithunlocked, Shamela, comentarios en línea) o, para los dos autores del siglo XIX con escaneo, en la imagen de la página. Las capturas en árabe son de la página original; las traducciones son literales y mías, con las dudas señaladas en cada tarjeta.</div>
<h2 class="g">Lo que leí yo mismo</h2>{table(D, ("Fuente y lugar", "Qué es", "Estado", "Tarjetas"))}
<h2 class="g">Lo que no leí (pistas de agentes, sin verificar)</h2>{table(F, ("Fuente", "Por qué no la uso", "Estado", "Tarjetas"))}
<h2 class="g">Resultados negativos, correcciones y cautelas</h2>{table(G, ("Asunto", "Qué pasó", "Tipo", "Tarjetas"))}'''
page('NQ00d_es', 'NQ00d', 'Mujer · razón y testimonio · fuentes', 'Resumen en español',
     'Qué leí yo, qué no, y las correcciones',
     'Los resultados negativos importan: dicen hasta dónde llega cada afirmación.', 'مصادر', body3,
     'Las calificaciones de cadenas son las que imprime el sitio, no las mías. Textos de Shamela y hadithunlocked.com (páginas web; Shamela muestra volumen y página).<br>Pack «La mujer ‹deficiente en razón y religión›: el hadiz, sus variantes y lo que dijeron los sabios hasta el siglo XIX»')
print('ok')
