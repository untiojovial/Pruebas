# -*- coding: utf-8 -*-
# Páginas de resumen del pack «Pablo en Damasco»: W00 (respuesta y verificación), W00b (hallazgos nuevos) y S1–S5 (silogismos).
import re, html
src = open('genv.py', encoding='utf-8').read()
CSS = re.search(r'CSS = """(.*?)"""', src, re.S).group(1)
CSS += """
table.v{width:100%;border-collapse:collapse;font-size:18px;line-height:1.42}
table.v th{background:#eef1f6;text-align:left;padding:9px 11px;font-size:14px;text-transform:uppercase;letter-spacing:.05em;color:#3b4660}
table.v td{border-top:1px solid #e3e7ee;padding:9px 11px;vertical-align:top}
.ok{color:#1d7a4f;font-weight:700}.no{color:#b44a2f;font-weight:700}.mid{color:#9a6a00;font-weight:700}
.ans{border-left:6px solid #14213d;background:#eef1f8;padding:16px 22px;border-radius:0 8px 8px 0;font-size:21px;line-height:1.55;margin-bottom:20px}
.ans b{color:#14213d}
.pr{border:1px solid #d6dbe4;border-radius:8px;padding:14px 20px;margin-bottom:12px;font-size:21px;line-height:1.5;background:#fff}
.pr .n{display:inline-block;background:#14213d;color:#fff;border-radius:6px;padding:1px 9px;font-weight:700;margin-right:8px;font-size:17px}
.pr .w{color:#566079;font-size:16px;margin-top:4px}
.cc{border-left:6px solid #2a9d8f;background:#eef8f6;padding:14px 20px;border-radius:0 8px 8px 0;font-size:22px;line-height:1.5;font-weight:600;margin:6px 0 14px}
ul.l{margin:6px 0 0 22px;font-size:19px;line-height:1.5}
"""
E = lambda s: html.escape(s, quote=False)

def page(fname, cid, tag, kind, title, ref, arref, body, foot):
    out = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="card">
<div class="hd"><div class="row"><div class="badge"><b>{cid}</b>{E(tag)}</div><span class="kind es">{E(kind)}</span></div>
<h1>{E(title)}</h1>
<div class="row"><div class="ref">{E(ref)}</div><div class="arref">{arref}</div></div></div>
<div class="bd">{body}</div>
<div class="ft"><div class="u">{foot}</div></div>
</div></body></html>'''
    open(f'wcards/{fname}.html', 'w').write(out)

def table(rows):
    r = ''.join(f'<tr><td>{E(a)}</td><td class="{c}">{E(b)}</td><td>{E(d)}</td></tr>' for a, c, b, d in rows)
    return f'<table class="v"><tr><th style="width:36%">Afirmación</th><th style="width:13%">Resultado</th><th>Detalle y tarjeta</th></tr>{r}</table>'

# ---------------- W00: respuesta corta + análisis que te pasaron ----------------
A = [
 ("Ibn Kathir (Bidaya 2/119) pone el hadiz de Abu l-Darda', luego Ibn Jarir/Ibn Ishaq, luego «varios», y luego el relato de Pablo", "ok", "Confirmado", "Mismo orden en Shiri, Saʿada y la edición crítica de 2010. W05, W06"),
 ("El relato de Pablo «bebe» de ese hadiz", "no", "No", "El hadiz no menciona a Pablo, Damasco ni Ḍīnā; el relato es de Wahb ibn Munabbih (Ibn ʿAsakir) y Ibn Kathir lo pone sin cadena. Solo hay vecindad temática. W05, W02"),
 ("Hadiz: cadena Abu Yaʿla → … → Abu l-Darda'; Ibn Kathir: «muy extraño aunque lo autenticó Ibn Hibban»", "ok", "Confirmado", "Texto, cadena y comentario leídos en Shiri y en Saʿada. W05"),
 ("al-Haytami (Mayma' 8/207): «lo transmitió al-Tabarani y sus transmisores son fiables; en algunos hay discrepancia»", "mid", "Solo la nota", "Confirmado como nota del editor de Shiri; no he leído el Mayma' en el original. W05"),
 ("Veredicto de Ibn Hibban / Arna'ut / al-Albani sobre ese hadiz", "mid", "Sin verificar", "Mis agentes no lo hallaron (la edición Arna'ut de Ibn Hibban no devolvió el hadiz en shamela)."),
 ("Dar Ibn Kathir 2010, t. 2, p. 302: pasaje con «في ب: العساكر» y «في ب: سنورده فيما بعد»", "ok", "Confirmado", "Leído sobre la imagen. La nota 1 va en «بغاله», la 3 en «سنورده». Esa edición trae la cláusula «hasta que fue destruida en el tiempo que mencionaremos», que Shiri y Saʿada no traen. W06"),
 ("«21 tomos», editado por ʿAli Abu Zayd y otros", "mid", "Corregido", "Abu Zayd edita la parte 2; la portada atribuye el tomo 1 a M. D. Mistu, con revisión de Arna'ut y ʿAwwad. Son 11 tomos (17 partes + 3 índices), según mi agente V2 leyendo la tabla de la edición."),
 ("Ms. A = al-Ahmadiyya de Alepo, «madre»; notas de propiedad de 874 y 923 H", "ok", "Confirmado", "Leído en pp. 85–86 de la edición. W07"),
 ("Ms. B = Berlín, copista Muhammad ibn Sultan ibn Saʿid al-Baʿli al-Hanbali", "ok", "Confirmado", "Misma fuente. W07"),
 ("B fue copiado en 805 H (según R. B. Olsen)", "no", "Sin confirmar", "La edición dice «no hallamos la fecha de copia»; no he hallado el dato en Olsen. Otro ms. de Berlín (Ahlwardt 9455) es de 890 H y otro copista. W07, W13"),
 ("Saʿada 2/100, nota: «no se halló en las dos copias de la Biblioteca Egipcia»", "ok", "Confirmado", "Pero el alcance es mayor: de «los compañeros de sus compañeros» a [Libro de las noticias…], con poema de al-Qarafi. Mismo fenómeno en los Qisas. W08, W11"),
 ("La edición Dar Hajar (al-Turki) usa manuscritos propios", "mid", "Sin verificar", "La introducción (pp. 5–44, leída por mi agente) no nombra manuscritos; sí describe a la Saʿada. W12"),
 ("Monferrer Sala 1996 (MEAH 45, 147–159): relato que «corría entre la comunidad cristiana de Damasco»", "ok", "Confirmado", "En el resumen del artículo. W16"),
 ("…y en la p. 156 «Jesús es siervo de Dios y Su mensajero» es una interpolación musulmana", "mid", "Sin verificar", "No pude abrir el PDF (servidores de Granada caídos; CORE bloquea la descarga). W16"),
 ("al-Tabari, año 14 H (ed. Beirut 2/432), cuenta el relato de Ḥanīnā y la iglesia", "no", "Incorrecto", "No aparece en su sección del año 14 sobre Damasco (ed. Abu l-Fadl, 3/434–440; 0 coincidencias). Tabari solo nombra a Pablo como «seguidor» enviado a Roma. W17. No miré la ed. de Beirut."),
]
body = f'''<div class="ans"><b>¿El relato de Pablo bebe del hadiz de arriba? No.</b> En el texto original de Ibn Kathir (W05) el hadiz de Abu l-Darda' —doscientos años; «muy extraño»— va primero, y el relato de Pablo viene después como bloque sin cadena. El hadiz no menciona a Pablo ni Damasco; la fuente del relato es Wahb ibn Munabbih (Ibn ʿAsakir, W02). <b>¿Las frases sobre la buena fe de Pablo son de Ibn Kathir?</b> No están en Ibn ʿAsakir ni en Ibn Manzur; las trae primero Ibn Kathir (en lo revisado), y la edición crítica de 2010 las confirma (W06). No puedo probar que no las sacara de otra fuente que no he visto.</div>
{table(A)}'''
page('W00_es', 'W00', 'Verificación · Pablo en Damasco', 'Resumen en español',
     'Qué se ha confirmado del análisis que me pasaste, y qué no',
     'Contrastado con los textos originales (shamela.ws, escaneos, OpenITI) y con 8 agentes de búsqueda cuyos hallazgos revisé yo.',
     'التحقق', body,
     'Fuentes: shamela.ws libros 8376, 23708, 932, 4445, 71, 6521, 9783 · archive.org (ed. Dar Ibn Kathir 2010; Ahlwardt) · repository.sbts.edu · forum-journal.uibk.ac.at · core.ac.uk<br>Pack «Pablo en Damasco» (ampliación)')

# ---------------- W00b: hallazgos nuevos y límites ----------------
B = [
 ("Existía una «iglesia de Pablo» en Damasco: Ibn Kathir (9/581) la lista como quinta, copiando a Ibn ʿAsakir", "ok", "Confirmado", "En los manuscritos de Ibn ʿAsakir la lectura es dudosa («Mariḍ»/«Bariṣ»); el editor la identifica con «Pablo» por el impreso. W14, W15"),
 ("El decorado del relato (Puerta Oriental, iglesia Muṣallaba) es topografía cristiana real", "ok", "Confirmado", "Ibn ʿAsakir: la Muṣallaba «sigue en pie entre Bab Sharqi y Bab Tuma». Coherente con el origen cristiano damasceno, no lo prueba. W15"),
 ("Antes de Ibn ʿAsakir hay textos que nombren la Muṣallaba en este relato", "mid", "No hallado", "No aparece en Tabari, al-Baladhuri, Yaqut, al-Maqdisi ni Ibn Jubayr (agente V4; parte en OCR). La frase de Ibn Shaddad (m. 684 H) es una inserción del editor tomada de Ibn ʿAsakir."),
 ("«La fe de Pablo se volvió buena…» y «la iglesia de Pablo» no están en Ibn ʿAsakir ni en Ibn Manzur", "ok", "Confirmado", "Cero apariciones; en las ediciones de Ibn Kathir sí. W02–W04, W06"),
 ("Ibn Kathir fecha «la gran calamidad» 300 años después del Mesías (Constantino, Credo) y llama al Credo «la mayor incredulidad»", "ok", "Confirmado", "Saʿada 2/101–102, a continuación de la fe de Pablo. W09, W10"),
 ("Ibn Hazm acusa a Pablo: soborno de los rabinos, «maldito», milagros falsos", "ok", "Confirmado", "Y dice que lo oyó «de sus sabios», o sea de los judíos. W18, W19"),
 ("Tabari, Masʿudi, Ibn al-Jawzi, Maqrizi, Ibn Khaldun nombran a Pablo sin acusarlo", "ok", "Confirmado (agente)", "Textos de OpenITI/shamela leídos por mi agente V5; solo Tabari tiene captura. W17"),
 ("Ibn Qayyim: «el primero que corrompió la religión de los cristianos» es Pablo", "mid", "Matiz", "Ese es Pablo de Samosata (patriarca de Antioquía, s. III), no el apóstol; el apóstol aparece decapitado con la espada. Leí los dos pasajes en OpenITI (Hidaya al-hayara); sin captura."),
 ("Ibn Taymiyya: Pablo = corruptor", "mid", "Condicional", "En al-Yawab al-sahih: «si Pablo era sincero, el que vio en su visión era un demonio». Verificado en OpenITI; sin captura. La cita de Mayma' 28:483 («un judío que corrompió») solo la he visto en un ensayo secundario (B. Muhammad)."),
 ("La teoría del «Pablo conspirador» viene de un texto judío (Toledot Yeshu)", "mid", "Hipótesis académica", "Whittingham, Folks y Anthony lo defienden; no es un hecho cerrado. W21, W22"),
 ("Pablo no se nombra en el Corán ni en el hadiz", "ok", "Confirmado", "Whittingham 2025, p. 10. W22"),
 ("En Ibn ʿAsakir, Pablo no es acusado de corromper", "ok", "Confirmado", "Folks 2024, pp. 85–86: «carece de acusaciones de corrupción»; sí se opone al mensaje de Jesús. W20"),
]
LIM = '''<div class="box ojo"><h3>Lo que NO puedes afirmar</h3><ul class="l">
<li><b>«Los musulmanes consideran inocente a Pablo.»</b> Falso: Ibn Hazm, Sayf y otros lo acusan, y Whittingham dice que la acusación domina los escritos musulmanes (W19, W22).</li>
<li><b>«Ibn Kathir demuestra que Pablo no corrompió el cristianismo.»</b> No: es lo que dice Ibn Kathir (y la fuente que se le atribuye), no una prueba histórica (W09, W10).</li>
<li><b>«Las frases sobre la buena fe de Pablo son de Wahb.»</b> No hay prueba: no están en Ibn ʿAsakir ni en Ibn Manzur.</li>
<li><b>«Son una interpolación tardía.»</b> Tampoco: están en la edición crítica y en el ms. B de Berlín (W06); solo faltan en dos copias egipcias, junto con todo un bloque (W08).</li>
<li><b>«El hadiz de Abu l-Darda' es sahih.»</b> No lo he podido comprobar; Ibn Kathir lo llama «muy extraño» (W05).</li>
</ul></div>'''
page('W00b_es', 'W00b', 'Verificación · hallazgos nuevos', 'Resumen en español',
     'Qué hemos encontrado además, y qué límites tiene',
     'Del trabajo de los 8 agentes de búsqueda y de mi verificación directa de las páginas.',
     'ما وجدنا', table(B) + LIM,
     'Los agentes de búsqueda (modelo pequeño) no son fuente: solo valen las citas que comprobé en página/escaneo, y lo digo donde no es así.<br>Pack «Pablo en Damasco» (ampliación)')

# ---------------- Silogismos ----------------
def syl(n, title, prem, concl, weak, use, cards):
    ps = ''.join(f'<div class="pr"><span class="n">P{i+1}</span>{p[0]}<div class="w">{p[1]}</div></div>' for i, p in enumerate(prem))
    body = f'{ps}<div class="cc">∴ {concl}</div><div class="box ojo"><h3>Puntos débiles</h3><ul class="l">{"".join(f"<li>{w}</li>" for w in weak)}</ul></div><div class="box"><h3>Cómo usarlo</h3>{use}</div>'
    page(f'S{n}_es', f'S{n}', 'Silogismo a tu favor · con sus límites', 'Razonamiento', title,
         'Cada premisa remite a una tarjeta con el texto original.', 'منطق', body, f'Tarjetas: {cards}<br>Pack «Pablo en Damasco» (ampliación)')

syl(1, "El dilema del hadiz: si vale, Pablo no corrompió en su tiempo; si no vale, no hay base para una pureza de doscientos años",
 [("Si el hadiz de Abu l-Darda' (en el Sahih de Ibn Hibban) es válido, los compañeros del Mesías permanecieron en su sunna y su guía doscientos años, sin tentación ni cambio.", "W05"),
  ("Pablo actuó en la primera generación después de Jesús: al-Tabari lo cuenta enviado a Roma con Pedro; Ibn Qayyim: «le cortaron el cuello con la espada».", "W17; Ibn Qayyim (Hidaya al-hayara), leído en OpenITI")],
 "O bien el hadiz es válido y la tesis «Pablo corrompió la religión en su tiempo» choca con él, o bien no lo es —Ibn Kathir: «muy extraño»— y esa tesis pierde el único hadiz que le daría una comunidad pura de doscientos años.",
 ["El hadiz habla de «compañeros del Mesías»; Tabari dice que Pablo «no era de los discípulos». Un musulmán puede decir que Pablo queda fuera.",
  "La autenticidad del hadiz no está resuelta: Ibn Hibban lo autentica; Ibn Kathir lo llama «muy extraño»; al-Haytami (vía la nota de Shiri) dice «hay discrepancia en algunos». No hallé el veredicto de Arna'ut ni de al-Albani.",
  "Es un argumento interno, ad hominem: no prueba nada sobre la historia real."],
 "Preséntalo como «lo que se sigue desde premisas musulmanas», no como pretensión de que el hadiz sea fiable. La pregunta que fuerza es: ¿en qué fuente islámica se basa que Pablo cambiara la religión en su época?",
 "W05, W17")

syl(2, "Ibn Kathir culpa al concilio de Constantino, no a Pablo",
 [("En el relato que cuenta Ibn Kathir, Pablo cree en el Mesías y su fe «se volvió buena: que es siervo de Dios y Su mensajero»; se le construye una iglesia con su nombre.", "W06, W09 (edición crítica 2010 y Saʿada)"),
  ("En el mismo apartado, justo después, Ibn Kathir fecha «la gran calamidad y la desgracia mayor» trescientos años después del Mesías, con el concilio ante Constantino, y llama al Credo «la mayor incredulidad y traición».", "W09, W10")],
 "Dentro de Ibn Kathir, el giro doctrinal no se atribuye a Pablo sino al concilio; citarlo como prueba de que «Pablo corrompió el cristianismo» lo lee al revés.",
 ["El bloque falta en dos copias egipcias (W08), aunque está en la edición crítica y en el ms. B (W06, W07). No hay prueba de interpolación, pero tampoco de que las frases sobre la buena fe de Pablo sean de Ibn Kathir y no de una fuente que no vemos.",
  "Ibn Kathir da 300 años y el hadiz 200: no los armoniza.",
  "Que Ibn Kathir no culpe a Pablo no significa que Pablo no enseñara una cristología alta: eso se discute en el Nuevo Testamento, no en esta fuente.",
  "Ibn Kathir condena el Credo como incredulidad: no es un testigo a favor de la doctrina cristiana."],
 "«Ni siquiera Ibn Kathir, la fuente que se cita, dice que fuera Pablo.» Limítate a eso.", "W06, W08, W09, W10")

syl(3, "Las escenas clásicas de la conversión de Pablo en Damasco conservan —no niegan— el relato cristiano",
 [("Los relatos musulmanes de la escena (al-Yaʿqubi; Wahb en Ibn ʿAsakir e Ibn Manzur) son versiones de Hechos 9: una voz, la ceguera, un discípulo de Jesús en Damasco (Ḥananiyā/Ḥanīnā ≈ Ananías), el mercado largo; y su decorado coincide con la topografía de Damasco (Puerta Oriental, Muṣallaba).", "W01–W03, W15"),
  ("Según Folks, en la versión de Ibn ʿAsakir Pablo no es acusado de corromper la religión de Jesús; y según Monferrer, el relato debía correr entre los cristianos de Damasco. En al-Yaʿqubi, tras curarse, Pablo se pone a predicar a Cristo en las iglesias.", "W20, W16, W01")],
 "Los relatos musulmanes clásicos de la escena de Damasco dependen de una tradición cristiana en la que Pablo pasa a creer en el Mesías; no son testigos independientes de un Pablo corruptor.",
 ["La cadena de Wahb es de transmisión escrita y no he evaluado a sus transmisores; Wahb murió hacia el 725: no hay prueba de que la versión sea de él.",
  "Folks añade que en la versión de Ibn ʿAsakir Pablo se opone al mensaje de Jesús (azul, W20): antes de convertirse es un enemigo.",
  "Lo de «origen cristiano damasceno» es una hipótesis de Monferrer (solo vi el resumen), no un dato.",
  "No he hallado ningún texto anterior a Ibn ʿAsakir que nombre la Muṣallaba en este relato (V4, búsqueda parcial)."],
 "Úsalo para mostrar de dónde viene el relato, no para fechar la «buena fe» de Pablo.", "W01–W04, W15, W16, W20")

syl(4, "La acusación de que Pablo corrompió el cristianismo no está en el Corán ni en el hadiz",
 [("Pablo no se nombra ni en el Corán ni en la literatura del hadiz.", "W22 (Whittingham)"),
  ("La primera acusación explícita (Sayf, siglo VIII) tiene paralelos con un relato judío anticristiano (Toledot Yeshu); y Ibn Hazm mismo dice que lo del Pablo «infiltrado» lo oyó de los sabios judíos.", "W21, W22, W18")],
 "El «Pablo corruptor» es una afirmación histórica extra-coránica, de origen discutido; no es un dato de revelación y hay que probarla con historia.",
 ["Falacia genética: que el origen sea judío no la refuta; Ibn Hazm argumenta con el texto de Gálatas (W19) y eso hay que contestarlo con exégesis.",
  "Los apologistas musulmanes razonan desde el tahrif coránico en general, no desde el nombre de Pablo.",
  "Whittingham y Folks son estudiosos, uno de Oxford y otro de un seminario bautista; «hay razones para creer» no es «está demostrado»."],
 "Útil para desplazar la carga de la prueba: si no es revelado, es una tesis histórica y se discute con fuentes históricas.", "W18, W19, W21, W22")

syl(5, "No hay un islam unánime sobre Pablo: el mapa, con nombres",
 [("Fuentes negativas: Ibn Hazm (soborno, «maldito», milagros falsos), Sayf (engañador deliberado) e Ibn Taymiyya (condicional sobre la visión).", "W19, W22; Ibn Taymiyya leído en OpenITI"),
  ("Fuentes que lo nombran sin acusarlo: al-Tabari, Masʿudi, Ibn al-Jawzi, Maqrizi; y Ibn Kathir e Ibn ʿAsakir sin cargo de corrupción.", "W17, W20, W06 · V5 (agente)")],
 "La tradición islámica no habla con una sola voz sobre Pablo: hay una corriente anti-Pablo con nombres de peso, y otra que no lo culpa. Quien diga «el islam siempre enseñó que Pablo corrompió el cristianismo» simplifica.",
 ["Whittingham: «Pablo es ampliamente considerado la figura central en la distorsión de las enseñanzas de Jesús». La corriente negativa es mayoritaria en los escritos polémicos.",
  "Algunos «Pablos» son otros (Pablo de Samosata): no hay que usar a Ibn Qayyim ni a Mas'udi sobre Samosata como si hablaran del apóstol.",
  "Varias lecturas de V5 son de OCR o de OpenITI sin captura; las he marcado como tales (W00b)."],
 "Con honestidad: «hay musulmanes que lo acusan y musulmanes que no; la acusación es una tradición, no un dogma».", "W17–W22, W00b")
print('ok')
