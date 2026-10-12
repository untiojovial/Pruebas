# -*- coding: utf-8 -*-
# Páginas de resumen del pack QC (adiciones, interpolaciones o supresiones en el Corán según obras académicas): QC00, QC00b, QC00c, QC00d
import re, html, os
src = open('genv.py', encoding='utf-8').read()
CSS = re.search(r'CSS = """(.*?)"""', src, re.S).group(1)
CSS += """
table.v{width:100%;border-collapse:collapse;font-size:16px;line-height:1.38}
table.v th{background:#eef1f6;text-align:left;padding:7px 9px;font-size:12.5px;text-transform:uppercase;letter-spacing:.05em;color:#3b4660}
table.v td{border-top:1px solid #e3e7ee;padding:7px 9px;vertical-align:top}
table.v td:first-child{white-space:nowrap;font-weight:700;color:#14213d}
.t{display:inline-block;border-radius:4px;padding:1px 7px;font-weight:700;font-size:14px;margin-right:3px;background:#eef1f8;color:#14213d}
.ta{background:#ffe8b0}.tb{background:#fbd5c8}.tc{background:#e9c9ef}.td{background:#cfe3f7}.te{background:#cdeedd}
.ok{color:#1d7a4f;font-weight:700}.no{color:#b44a2f;font-weight:700}.mid{color:#9a6a00;font-weight:700}
.ans{border-left:6px solid #14213d;background:#eef1f8;padding:16px 22px;border-radius:0 8px 8px 0;font-size:20px;line-height:1.55;margin-bottom:18px}
.ans b{color:#14213d}
h2.g{font-size:19px;margin:18px 0 8px;color:#14213d;border-bottom:2px solid #fca311;padding-bottom:3px}
ul.l{margin:6px 0 0 22px;font-size:18.5px;line-height:1.5}
"""
E = lambda s: html.escape(s, quote=False)
OUT = 'qccards'
os.makedirs(OUT, exist_ok=True)
FOOT = 'Pack «¿Adiciones, interpolaciones o supresiones en el Corán? Lo que dicen obras académicas»'
def page(fname, cid, tag, kind, title, ref, arref, body, foot):
    out = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="card">
<div class="hd"><div class="row"><div class="badge"><b>{cid}</b>{E(tag)}</div><span class="kind es">{E(kind)}</span></div>
<h1>{E(title)}</h1>
<div class="row"><div class="ref">{E(ref)}</div><div class="arref">{arref}</div></div></div>
<div class="bd">{body}</div>
<div class="ft"><div class="u">{foot}</div></div>
</div></body></html>'''
    open(f'{OUT}/{fname}.html', 'w').write(out)
def tags(t):
    return ''.join(f'<span class="t t{c.lower()}">{c}</span>' for c in t if c != ' ')
def table(rows):
    r = ''
    for code, who, what, typ, stance in rows:
        r += f'<tr><td>{E(code)}</td><td>{E(who)}</td><td>{E(what)}</td><td>{tags(typ)}</td><td>{E(stance)}</td></tr>'
    th = ''.join(f'<th>{h}</th>' for h in ('Tarjeta', 'Obra (idioma)', 'Qué dice, en breve', 'Tipo', 'Postura'))
    return f'<table class="v"><tr>{th}</tr>{r}</table>'

# ---------- QC00: respuesta corta + obras recientes y de manuscritos ----------
A = [
 ("QC01", "Sinai, Key Terms of the Qur’an, 2023 (inglés)", "«No descarta» ediciones y ampliaciones tempranas posproféticas; casos: Q 3:7–9, 29:46 («adición medinense»), 74:56, 76:30, 81:29; informa de dos «suras» de Ubayy; rechaza la tesis de interpolación de jahannam", "AC E", "Propia, condicional · informa · rechaza"),
 ("QC02", "Shoemaker, Creating the Qur’an, 2022 (inglés)", "Forma canónica fijada hacia el 700 (ʿAbd al-Malik y al-Ḥajjāj); «censura» de códices rivales; él mismo precisa que no es creación «de la nada» y que el Corán refleja la enseñanza de Muhammad", "BC", "Propia (minoritaria)"),
 ("QC03", "Neuwirth, Studien zur Komposition…, 2.ª ed., 2007 (alemán)", "«Ampliaciones medinenses» de textos mequíes (Becerro de Oro, sura 20); informa de Crone/Cook/Hawting y de Lüling; critica a Wansbrough", "AB E", "Propia · informa · rechaza"),
 ("QC04", "Corpus Coranicum, comentario cronológico-literario (alemán)", "Adiciones medinenses en las suras 19, 20 y 37; la Fātiḥa antepuesta «por la redacción ʿuthmánica o posterior»; rechaza la pérdida del comienzo de la 97, la interpolación en la 96 y las revisiones de Bell en la 67", "AB CE", "Propia · rechaza"),
 ("QC05", "Dye, «Quelques questions sur les contextes du Coran», 2023 (francés)", "Versiones paralelas = revisiones y reescrituras sucesivas; hay que estudiar los estratos del texto; la forma del corpus refleja lo que sus responsables «pudieron» y «quisieron» conservar", "A", "Propia (método)"),
 ("QC06", "Bouali, «Enjeux politiques…», 2023 (francés)", "Hipótesis, expresamente incierta, de que Q 17:33 sea una interpolación de época sufyánida; bajo al-Ḥajjāj, «mejora de la Vulgata» y destrucción de códices rivales", "ABC", "Propia (hipótesis) · fuentes"),
 ("QC07", "Jeffery, Materials for the History of the Text of the Qurʾān, 1937 (inglés)", "El texto ʿuthmánico es «solo uno entre varios»; el códice de Ibn Masʿūd sin la Fātiḥa ni las Muʿawwidhatān («adiciones litúrgicas» según la erudición moderna); el de Ubayy con dos suras «extra»", "CD", "Propia · informa de fuentes"),
 ("QC08", "Déroche, Qurʾans of the Umayyads, 2014 (inglés)", "El palimpsesto Ṣanʿāʾ I omite 9:85 y tiene adiciones; su texto inferior difiere del ʿuthmánico y de Ibn Masʿūd/Ubayy; el papel del califa pudo ser menor", "CD", "Propia (manuscrito)"),
 ("QC09", "van Putten, «The Grace of God…», 2019 (inglés)", "La ortografía común de 14 manuscritos exige un arquetipo escrito de época ʿuthmánica: «corrobora muy precisamente» el relato tradicional", "E", "Contraevidencia"),
 ("QC10", "Chahdi, «La canonisation des variantes…», 2023 (francés)", "Informa de la hipótesis de Nasser (cinco etapas de canonización); concluye que la historia tradicional es una «reconstitución posterior»", "BD", "Informa · propia"),
]
body = f'''<div class="ans"><b>Respuesta corta.</b> Sí hay obras académicas que proponen <b>adiciones o interpolaciones</b> en el Corán, pero casi todas dentro de la <b>formación del texto en vida de Muhammad</b> (ampliaciones «medinenses» de suras mequíes: Nöldeke, Neuwirth, Sinai, Corpus Coranicum) y con lenguaje condicional («no descarto», «podría», «dürfte»). Las tesis de <b>fijación o redacción posterior</b> (Shoemaker hacia el 700; Wansbrough hacia el 800, que cita van Koningsveld para rechazarla) son <b>minoritarias y discutidas</b>. Sobre <b>supresiones</b>, ninguna obra leída muestra suras o versículos perdidos del texto actual: hay <b>informes</b> (Ubayy, Ibn Masʿūd, ʿUmar, ʿĀʾisha) que las propias fuentes árabes registran, clasifican como «abrogación de la recitación» o rechazan (al-Nawawī, Ibn Ḥazm, al-Zurqānī, Ṣubḥī al-Ṣāliḥ). Y la <b>evidencia de los manuscritos</b> (Bergsträsser–Pretzl, van Putten, Déroche con la excepción de Ṣanʿāʾ I) muestra un texto consonántico estable desde muy pronto. Ver QC00b y QC00c.</div>
<h2 class="g">1 · Obras recientes sobre la formación del texto y los manuscritos</h2>{table(A)}'''
page('QC00_es', 'QC00', 'Corán · adiciones, interpolaciones, supresiones', 'Resumen en español',
     '¿Dice la erudición que el Corán sufrió adiciones, interpolaciones o supresiones? Lo que dicen 25 obras en inglés, alemán, neerlandés, francés y árabe',
     'Comprobado en copias digitales de las obras (PDF, escaneos, texto web de Shamela, API del Corpus Coranicum); con 8 agentes de búsqueda cuyos hallazgos revisé yo.', 'القرآن', body,
     'Tipo: <span class="t ta">A</span> adición o interpolación · <span class="t tb">B</span> redacción o fijación posterior · <span class="t tc">C</span> supresión, pérdida u omisión (incluye informes de «abrogación de la recitación») · <span class="t td">D</span> códices alternativos y variantes · <span class="t te">E</span> contraevidencia o rechazo.<br>' + FOOT)

# ---------- QC00b: clásicos, neerlandés y árabe ----------
B = [
 ("QC11", "Weil, Historisch-kritische Einleitung in den Koran, 1844 (alemán)", "ʿUthmān eliminó las variantes para tener un solo Corán; después de él, «con certeza» sin adiciones ni omisiones intencionadas; hipótesis alternativa: que Abū Bakr interpolara los versículos sobre la mortalidad de Muhammad", "BAE", "Propia · hipótesis"),
 ("QC12", "Muir, The Corân: its composition and teaching, 1878 (inglés)", "Recensión de ʿUthmān con «remedio drástico» y quema de copias; «pasajes medinenses interpolados» en suras mequíes y en la sura 2; pero «toda garantía» de que Zayd actuó con fidelidad", "BC AE", "Propia"),
 ("QC13", "Hirschfeld, New Researches…, 1902 (inglés)", "«Habría sido un milagro» que no hubiera omisiones e interpolaciones; informa de que Nöldeke lo niega; la tradición del versículo de la lapidación, «fabricada»", "CE", "Propia · informa · rechaza"),
 ("QC14", "Nöldeke–Schwally, Geschichte des Qorans I, 1909 (alemán)", "La posibilidad de interpolaciones debe admitirse; casos en las suras 74 y 8; «algunos datos» sobre pasajes perdidos que no puede juzgar; el versículo de la lapidación nunca fue Corán", "ACE", "Propia"),
 ("QC15", "Nöldeke–Schwally, Geschichte des Qorans II, 1919 (alemán)", "Ampliaciones y sustituciones hechas por Muhammad en Medina; suras de Ubayy no genuinas; ʿUthmān destruyó manuscritos divergentes; el texto estaba «en lo esencial» terminado dos o tres años tras su muerte", "AD CE", "Propia"),
 ("QC16", "Bergsträsser–Pretzl, Geschichte des Qorāns III, 1938 (alemán)", "Los manuscritos muestran el texto consonántico ʿuthmánico salvo los palimpsestos de Lewis; sin rastro de Ibn Masʿūd/Ubayy; rechazan la tesis siríaca de Mingana", "ED", "Contraevidencia"),
 ("QC17", "«De Koran», 4.ª ed. neerlandesa, ca. 1916 (neerlandés)", "Informa de tradiciones de versículos perdidos y borrados; infiere que Abū Bakr incorporó versículos contra la voluntad del Profeta; afirma que ʿUthmān quemó las copias anteriores (autor del texto no identificado)", "CB", "Informa · inferencia"),
 ("QC18", "van Koningsveld, Revisionisme en Moderne Islamitische Theologie, 2009 (neerlandés)", "El texto oficial de ʿUthmān (hacia 650) desplazó a otros códices; presenta las tesis de Wansbrough (redacción hacia 800) y Lüling y las rechaza como dogmáticas", "BE", "Contraevidencia"),
 ("QC19", "al-Suyūṭī, al-Itqān I (árabe, clásico)", "Informes: Barāʾa «perdió su comienzo» (Mālik); códices de Ibn Masʿūd (112 suras) y de Ubayy (116); al-Nawawī e Ibn Ḥazm: lo atribuido a Ibn Masʿūd «es falso»", "CD E", "Informa · cita rechazos"),
 ("QC20", "al-Suyūṭī, al-Itqān II (árabe, clásico)", "Abrogación de la recitación: «mucho Corán se ha ido» (Ibn ʿUmar), al-Aḥzāb de 200 versículos, una sura como Barāʾa, el versículo de la lapidación, los «diez amamantamientos»; rechazo de Ibn Ẓafar", "CE", "Informa · cita rechazo"),
 ("QC21", "al-Zarkashī, al-Burhān (árabe, clásico)", "Versículo de la lapidación y suras del qunūt como «retirados de la escritura»; rechaza que ʿUthmān alterara el Corán; las Muʿawwidhatān son Corán", "CE", "Informa · rechaza"),
 ("QC22", "Abū ʿUbayd, Faḍāʾil al-Qurʾān (árabe, clásico)", "ʿUmar y un versículo «omitido con lo que se omitió»; Ubayy/Ibn Masʿūd con la Fātiḥa y las Muʿawwidhatān; ʿUthmān «digno de confianza sobre lo que omitió»", "CD E", "Informa · opina"),
 ("QC23", "Ibn Abī Dāwūd, Kitāb al-Maṣāḥif (árabe, clásico)", "ʿUthmān ordena quemar el resto de hojas y códices; Ibn Masʿūd retiene el suyo; Zayd «pierde» un versículo de al-Aḥzāb (33:23) y lo encuentra", "CD", "Informa"),
 ("QC24", "Ṣubḥī al-Ṣāliḥ, Mabāḥith fī ʿulūm al-Qurʾān (árabe, moderno)", "ʿUthmān copió de las hojas de Ḥafṣa «cerrando todo pretexto»; las adiciones de Ibn Masʿūd son explicaciones; critica la abrogación por informes de uno solo", "E", "Contraevidencia"),
 ("QC25", "al-Zurqānī, Manāhil al-ʿirfān (árabe, moderno)", "Refuta la acusación de omisión de versículos y suras («sura de la walāya»); lo de Ibn Masʿūd no implica negación; afirma la abrogación de recitación y norma (diez amamantamientos)", "EC", "Rechaza · afirma abrogación"),
]
body2 = f'''<h2 class="g">2 · Clásicos de la crítica textual, obras en neerlandés y obras en árabe</h2>{table(B)}'''
page('QC00b_es', 'QC00b', 'Corán · adiciones, interpolaciones, supresiones · obras', 'Resumen en español',
     'Clásicos (1844–1938), obras en neerlandés y fuentes árabes: qué dice cada una',
     'Cada fila remite a tres diapositivas (texto original con subrayado, traducción al español y portada). «Postura» se refiere al pasaje leído, no a toda la obra.', 'علوم القرآن', body2,
     'Tipo: <span class="t ta">A</span> adición o interpolación · <span class="t tb">B</span> redacción o fijación posterior · <span class="t tc">C</span> supresión, pérdida u omisión · <span class="t td">D</span> códices alternativos y variantes · <span class="t te">E</span> contraevidencia o rechazo.<br>' + FOOT)

# ---------- QC00c: lecturas y qué se puede afirmar ----------
C = '''<div class="box"><h3>Cuatro clases de afirmaciones que aparecen en las obras</h3><ul class="l">
<li><b>1 · Adiciones y ampliaciones dentro de la formación del texto, en vida de Muhammad.</b> Nöldeke 1919 (adiciones medinenses «con pequeñas intercalaciones»), Neuwirth 2007, el comentario del Corpus Coranicum (suras 19, 20, 37), Sinai 2023 (Q 29:46, 74:56, 76:30, 81:29), Muir 1878. Son hipótesis de crítica literaria, casi siempre con matices; no dicen que el texto se alterase después.</li>
<li><b>2 · Redacción, fijación o interpolación posterior a Muhammad.</b> Shoemaker 2022 (hacia el 700), Bouali 2023 (hipótesis incierta sobre Q 17:33), Sinai 2023 (Q 3:7–9, «a contemplar»), Dye 2023 (revisiones sucesivas), Wansbrough y Lüling (citados por van Koningsveld y Neuwirth para criticarlos). Son tesis minoritarias o hipotéticas; Sinai y Neuwirth rechazan explícitamente varias.</li>
<li><b>3 · Supresiones: informes, no fragmentos.</b> El versículo de la lapidación, «al-Aḥzāb de doscientos versículos», una sura «como Barāʾa», los «diez amamantamientos», al-Khalʿ y al-Ḥafd, la Fātiḥa y las Muʿawwidhatān en Ibn Masʿūd, 9:85 en Ṣanʿāʾ I. Las fuentes árabes (al-Suyūṭī, al-Zarkashī, Abū ʿUbayd, Ibn Abī Dāwūd) los recogen; al-Zarkashī, al-Suyūṭī y al-Zurqānī los clasifican como «abrogación de la recitación» (el texto fue levantado por Dios), y al-Nawawī, Ibn Ḥazm, Ibn Ẓafar, Ṣubḥī al-Ṣāliḥ o Nöldeke (para la lapidación) los rechazan o los limitan.</li>
<li><b>4 · Estabilidad del texto.</b> Bergsträsser–Pretzl 1938 (los manuscritos muestran el texto ʿuthmánico, salvo los palimpsestos de Lewis), van Putten 2019 (arquetipo escrito ʿuthmánico), van Koningsveld 2009, Nöldeke 1919 (texto «en lo esencial» terminado dos o tres años tras la muerte de Muhammad), Muir 1878 y Weil 1844.</li>
</ul></div>
<div class="box"><h3>Lo que se puede afirmar con base en lo leído</h3><ul class="l">
<li>Obras académicas serias (Nöldeke, Neuwirth, Sinai, Corpus Coranicum) hablan de <b>adiciones y ampliaciones</b> en la formación de ciertas suras; se discuten caso por caso.</li>
<li>Existen <b>informes antiguos</b>, registrados por las propias fuentes árabes, de códices con suras ausentes o extra (Ibn Masʿūd, Ubayy) y de textos «levantados»; la tradición los explica como abrogación de la recitación o los rechaza.</li>
<li>El palimpsesto <b>Ṣanʿāʾ I</b> tiene un texto inferior que omite 9:85 y difiere en palabras del texto ʿuthmánico (Déroche); en cambio los manuscritos tempranos estudiados siguen el texto ʿuthmánico (Bergsträsser–Pretzl; van Putten).</li>
<li>Hay <b>tesis de fijación tardía</b> (Shoemaker, hacia el 700) y la <b>réplica</b> (van Putten, Déroche, van Koningsveld): el debate está abierto.</li>
</ul></div>
<div class="box ojo"><h3>Lo que no se puede afirmar</h3><ul class="l">
<li><b>«Los académicos han demostrado que el Corán fue falsificado.»</b> Ninguna obra leída lo afirma como demostrado; lo más fuerte (Shoemaker, Wansbrough) es minoritario y discutido, y varias obras de este pack lo contradicen.</li>
<li><b>«Los académicos dicen que no hay nada que discutir.»</b> Tampoco: hay adiciones propuestas por especialistas, un palimpsesto con variantes y un debate vivo sobre cuándo se fijó el texto.</li>
<li><b>«Faltan suras en el Corán actual.»</b> Ninguna obra leída muestra suras perdidas del texto actual; hay informes de suras «extra» o ausentes en códices particulares y de textos «levantados» sin fragmentos conservados (Nöldeke 1909: «no podemos decidir qué hay de verdad»).</li>
<li><b>«Las fuentes islámicas ocultan esos informes.»</b> No: los registran y discuten ellas mismas (al-Suyūṭī, al-Zarkashī, Abū ʿUbayd, Ibn Abī Dāwūd).</li>
<li><b>«La abrogación de la recitación prueba manipulación humana.»</b> Es lo contrario de lo que dicen esas fuentes: para ellas fue Dios quien retiró o hizo olvidar el texto; eso es un debate teológico, no una evidencia textual.</li>
</ul></div>'''
page('QC00c_es', 'QC00c', 'Corán · adiciones, interpolaciones, supresiones · lecturas', 'Resumen en español',
     'Cuatro clases de afirmaciones, y lo que se puede y no se puede afirmar',
     'Resumen de lo comprobado en las diapositivas QC01–QC25.', 'قراءات', C,
     'Todas las afirmaciones remiten a una obra con su captura; las clasificaciones son mías y se refieren al pasaje leído, no a toda la obra del autor.<br>' + FOOT)

# ---------- QC00d: fuentes leídas, no leídas, correcciones ----------
D = [
 ("QC01–QC02", "Sinai (Key Terms, ORA), Shoemaker (Luminos)", "PDF de acceso abierto; pasajes comprobados en el PDF y subrayados sobre la imagen de la página", "Leído y capturado"),
 ("QC03", "Neuwirth 2007", "Solo la vista previa gratuita del editor; el apartado «Spätere Zusätze» no está en ella", "Parcial (vista previa)"),
 ("QC04", "Corpus Coranicum", "API pública del proyecto; transcripción (la web es una aplicación JavaScript)", "Leído; transcripción"),
 ("QC05–QC06, QC10", "Dye, Bouali, Chahdi (Archimède 10)", "PDF de acceso abierto de la revista («todos los derechos reservados»)", "Leído y capturado"),
 ("QC07–QC09", "Jeffery, Déroche, van Putten", "Jeffery: escaneo con OCR; Déroche: OAPEN (licencia no confirmada); van Putten: CC BY 4.0", "Leído y capturado"),
 ("QC11–QC16", "Weil, Muir, Hirschfeld, Nöldeke–Schwally (2 vols.), Bergsträsser–Pretzl", "Escaneos de archive.org; subrayado con la capa de texto del PDF o con OCR (Weil, Neuwirth, Bergsträsser–Pretzl, Hirschfeld seg. 3, Muir seg. 5)", "Leído y capturado"),
 ("QC17–QC18", "«De Koran» (Gutenberg), van Koningsveld", "Gutenberg: dominio público. van Koningsveld: copia en un servidor de terceros (bieb.islamnu.nl); la del repositorio de Leiden estaba bloqueada", "Leído y capturado; fuente de terceros"),
 ("QC19–QC25", "al-Suyūṭī, al-Zarkashī, Abū ʿUbayd, Ibn Abī Dāwūd, Ṣubḥī al-Ṣāliḥ, al-Zurqānī (Shamela)", "Texto web de la Biblioteca Shamela; cada cita la comprobé en la página, con volumen y página impresa", "Leído y capturado"),
]
F = [
 ("Sinai, The Qur’an: A Historical-Critical Introduction (2017); Sinai 2010, 2015, 2017, 2021, 2022", "No encontré copia abierta; el agente solo halló fichas bibliográficas. No las cito", "Sin leer"),
 ("Wansbrough 1977, Crone 1994, Cook 2000, Donner 1998 y 2008, Reynolds 2010, Powers 1986 y 2009, Madigan 2001, Stewart 2008, Motzki 2001, Anthony 2019, Burton 1977, Small 2011, Cook 2004, Sidky 2020, Jeffery 1952, Puin 1996, Hilali 2017, Sadeghi–Bergmann 2010, Sadeghi–Goudarzi 2012", "Sin copia legal accesible: de pago, o solo copias subidas por terceros (Scribd, almuslih.org, universidades) que no usé. Wansbrough y Lüling los conozco solo por lo que dicen van Koningsveld y Neuwirth", "Sin leer"),
 ("Nöldeke 1860, Margoliouth 1905, Casanova 1911–1924, Rodwell 1861, Neuwirth 2010 (muestra), Beeckman 2020, Déroche 2016, Sinai 2014 (BSOAS)", "Los agentes los localizaron y extrajeron pasajes (Rodwell: ninguno); no los verifiqué ni hice tarjeta", "Pistas sin verificar"),
 ("al-Jābirī, Abū Zayd, ʿAbd al-Majīd al-Sharfī (Charfi), Arkoun, Shaḥrūr, ʿAbd al-Ṣabūr Shāhīn, al-Khuʾī", "Autores árabes modernos buscados por el agente de árabe: solo hay reseñas, agregadores o copias de terceros; ningún texto legal abierto", "Sin leer"),
]
G = [
 ("Ibn Abī Dāwūd (Kitāb al-Maṣāḥif)", "No hay en el texto de Shamela ninguna mención de al-Muʿawwidhatān, al-Khalʿ/al-Ḥafd ni del versículo de la lapidación (búsqueda de mi agente)", "Resultado negativo"),
 ("Ṣubḥī al-Ṣāliḥ, al-Zurqānī", "Ṣubḥī: no menciona al-Khalʿ/al-Ḥafd; al-Zurqānī: no encontré el texto «al-shaykh wa-l-shaykha»; no comprobé exhaustivamente otras partes de cada obra", "Resultado negativo (parcial)"),
 ("Hirschfeld seg. 3 y Muir seg. 5", "La capa de texto del PDF tiene el orden de palabras alterado; usé OCR sobre la imagen. Los resaltados de OCR pueden desviarse ±1 palabra", "Cautela"),
 ("Páginas de Shamela", "Shamela da «pageNum» (página impresa según su ficha) y marcadores ⦗n⦘ dentro del texto. El versículo perdido de Zayd (33:23) está en la p. 89 y no en la 88 que dijo el agente: corregido", "Corrección"),
 ("Derechos y cubiertas", "Sinai: acceso abierto, se cita «Courtesy of Princeton University Press». Déroche: licencia no confirmada, solo fragmentos. Bergsträsser–Pretzl 1938, Ṣubḥī y al-Zurqānī: derechos no verificados, fragmentos breves. Cubiertas de Itqān, Burhān, Mabāḥith y Manāhil: miniaturas de baja resolución; Keyzer: cubierta generada sin autores; Corpus Coranicum: sin portada; Abū ʿUbayd: ficha de Shamela; Ibn Abī Dāwūd: portada de otra edición (la de Jeffery 1937)", "Aviso"),
]
body3 = f'''<div class="ans"><b>Cómo se hizo.</b> Ocho agentes de búsqueda (modelo pequeño) buscaron obras y pasajes en toda la web; <b>solo cuenta lo que yo abrí en una copia digital de la obra</b> y comprobé en la página (los subrayados se dibujaron sobre la imagen de la página o sobre la página web; donde no hay copia digital, hay transcripción con su referencia). Las traducciones son literales y mías, con aclaraciones entre corchetes. No usé copias subidas por terceros, salvo la de van Koningsveld (marcada).</div>
<h2 class="g">Lo que leí yo mismo</h2><table class="v"><tr><th>Tarjetas</th><th>Obras</th><th>Fuente y estado</th><th>Estado</th></tr>{''.join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td><td>{E(d)}</td></tr>" for a,b,c,d in D)}</table>
<h2 class="g">Lo que no leí (sin copia legal accesible, o sin verificar)</h2><table class="v"><tr><th>Obras</th><th>Por qué no las uso</th><th>Estado</th></tr>{''.join(f"<tr><td style='white-space:normal'>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>" for a,b,c in F)}</table>
<h2 class="g">Resultados negativos, correcciones y avisos</h2><table class="v"><tr><th>Asunto</th><th>Qué pasó</th><th>Tipo</th></tr>{''.join(f"<tr><td style='white-space:normal'>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>" for a,b,c in G)}</table>'''
page('QC00d_es', 'QC00d', 'Corán · adiciones, interpolaciones, supresiones · fuentes', 'Resumen en español',
     'Qué leí yo, qué no, resultados negativos y avisos',
     'Los resultados negativos y las obras no leídas dicen hasta dónde llega cada afirmación.', 'مصادر', body3,
     'Las traducciones son mías. Textos de Shamela y del Corpus Coranicum: páginas web, no ediciones impresas.<br>' + FOOT)
print('ok')
