# -*- coding: utf-8 -*-
# Diapositivas «de método» del pack Hebreos 10:28 (video, texto, silogismos, distinción, Aquino, cierre del vídeo)
import sys, os, shutil
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb')
from hbcss import *
OUT = 'hbcards'
os.makedirs(OUT + '/img', exist_ok=True)
for t in (9, 28, 47, 82):
    shutil.copy(f'{HBD}/vid/hq_{t}.png', f'{OUT}/img/video_{t}.png')

# ---------------------------------------------------------------- HB00
body = f'''<div class="ans"><b>Lo que dice el vídeo.</b> Un vídeo de TikTok (@antibulos1, 1 min 30 s; responde a un tal «Eduardo») dice que «Eduardo no quiere exponer la brutalidad de sus textos» y trae tres ejemplos: <b>1)</b> Hebreos 10:28, que «recoge la severidad de las sanciones previstas por la legislación mosaica, incluida la pena de muerte»; <b>2)</b> Tomás de Aquino, que «defendió que los herejes pertinaces podían ser entregados al poder secular para recibir la pena de muerte»; <b>3)</b> un hadiz islámico (el hombre que abandona el islam y se rebela contra Alá y su Mensajero: ejecución, crucifixión o destierro). Añade que ese hadiz «debe distinguirse del abandono pacífico y libre de la religión», que «equiparar automáticamente ambos supuestos supondría ignorar una distinción fundamental» y concluye que «determinadas tradiciones religiosas han admitido castigos extremos» y que Estados Unidos mantiene la pena capital para la traición federal.</div>
<div class="vid">
<figure><img src="img/video_9.png"><figcaption>0:07–0:25 · «1. Hebreos 10:28. El Nuevo Testamento»: capturas de versiones en español de la Biblia</figcaption></figure>
<figure><img src="img/video_28.png"><figcaption>0:25–0:41 · «2. Tomás de Aquino: la ejecución de los herejes» (texto de la Suma, II-II, q. 11, a. 3, en español)</figcaption></figure>
<figure><img src="img/video_47.png"><figcaption>0:41–1:12 · «3. El hadiz islámico: apostasía y rebelión» (Nasaʾi 4059, ʿAʾisha) y «la distinción»</figcaption></figure>
<figure><img src="img/video_82.png"><figcaption>1:12–1:30 · «Conclusión»: pena capital por traición federal en EE. UU. (18 U.S.C. § 2381)</figcaption></figure>
</div>
<h2 class="g">Cómo responde este pack</h2>
<ul class="l">
<li><b>Hebreos 10:28 no manda nada</b>: describe lo que pasaba bajo la ley de Moisés y lo usa en un razonamiento «cuánto más» que termina en el <b>juicio de Dios</b> (10:29–31). Los Padres lo leen así (HB01–HB03 y P01–P08).</li>
<li><b>Los Padres de la Iglesia</b> (8 leídos): ninguno usa Hebreos 10:28 como orden de matar; varios dicen expresamente que no se debe matar ni forzar la fe (Crisóstomo, Orígenes, Tertuliano, Lactancio, Atanasio) y otros exigen matices honestos (Agustín defendió la coerción legal; Jerónimo invoca Dt 13) (HB04, P01–P08).</li>
<li><b>Aquino</b> es del siglo XIII, teólogo y no jurista, y <b>no es tradición apostólica</b>; él mismo cita a Crisóstomo en contra (AQ01–AQ02).</li>
<li><b>El método del vídeo</b> («distinguir antes de equiparar») aplicado a Hebreos y a Aquino deshace su paralelo; su cierre es un «tú también» y la comparación con la traición castiga actos, no creencias (CV01–CV02).</li>
</ul>'''
page(OUT, 'HB00_es', 'HB00', 'Hebreos 10:28 · el vídeo', 'Resumen en español',
     'Qué dice el vídeo de @antibulos1 («Eduardo no quiere exponer la brutalidad de sus textos») y cómo se responde',
     'Vídeo de TikTok de 90 s, transcrito y revisado fotograma a fotograma; los subtítulos y capturas son del propio vídeo.', body,
     'Transcripción hecha con un modelo de voz (Whisper large-v3) y revisada con los subtítulos del vídeo. Las capturas se muestran como cita breve del vídeo para poder responderle.<br>' + PACK)

# ---------------------------------------------------------------- HB01
body = f'''<div class="two">
<div class="pn"><h4>Texto griego (SBLGNT)</h4><div class="gr">
<sup>26</sup> Ἑκουσίως γὰρ ἁμαρτανόντων ἡμῶν μετὰ τὸ λαβεῖν τὴν ἐπίγνωσιν τῆς ἀληθείας, οὐκέτι περὶ ἁμαρτιῶν ἀπολείπεται θυσία, <sup>27</sup> φοβερὰ δέ τις ἐκδοχὴ κρίσεως καὶ πυρὸς ζῆλος ἐσθίειν μέλλοντος τοὺς ὑπεναντίους. <sup>28</sup> <mark class="k">ἀθετήσας τις νόμον Μωϋσέως χωρὶς οἰκτιρμῶν ἐπὶ δυσὶν ἢ τρισὶν μάρτυσιν ἀποθνῄσκει·</mark> <sup>29</sup> <mark class="a">πόσῳ δοκεῖτε χείρονος ἀξιωθήσεται τιμωρίας</mark> ὁ τὸν υἱὸν τοῦ θεοῦ καταπατήσας, καὶ τὸ αἷμα τῆς διαθήκης κοινὸν ἡγησάμενος ἐν ᾧ ἡγιάσθη, καὶ τὸ πνεῦμα τῆς χάριτος ἐνυβρίσας. <sup>30</sup> οἴδαμεν γὰρ τὸν εἰπόντα· <mark class="a">Ἐμοὶ ἐκδίκησις, ἐγὼ ἀνταποδώσω·</mark> καὶ πάλιν· Κρινεῖ κύριος τὸν λαὸν αὐτοῦ. <sup>31</sup> φοβερὸν τὸ ἐμπεσεῖν εἰς χεῖρας θεοῦ ζῶντος.</div></div>
<div class="pn"><h4>Traducción literal propia</h4><div class="es2">
<sup>26</sup> Porque si pecamos voluntariamente después de haber recibido el pleno conocimiento de la verdad, ya no queda sacrificio por los pecados, <sup>27</sup> sino cierta terrible expectativa de juicio y un celo de fuego que ha de devorar a los adversarios. <sup>28</sup> <mark class="k">Quien ha desechado la ley de Moisés muere sin compasión, por dos o tres testigos.</mark> <sup>29</sup> <mark class="a">¿Cuánto peor castigo pensáis que merecerá</mark> el que pisoteó al Hijo de Dios, tuvo por profana la sangre de la alianza con la que fue santificado y ultrajó al Espíritu de la gracia? <sup>30</sup> Pues conocemos al que dijo: <mark class="a">«Mía es la venganza; yo pagaré»</mark>, y otra vez: «El Señor juzgará a su pueblo». <sup>31</sup> ¡Terrible cosa es caer en manos del Dios vivo!</div></div></div>
<h2 class="g">Lo que se ve en el propio texto</h2>
<ul class="l">
<li><b>Es descripción, no mandato.</b> El v. 28 usa el presente descriptivo («muere», <span class="gr">ἀποθνῄσκει</span>) y en 10:26–31 <b>no hay ningún imperativo</b> (verbos en indicativo, participio y futuro; los imperativos empiezan en 10:32: «Recordad…»). Nadie recibe la orden de ejecutar a nadie.</li>
<li><b>Es un argumento «cuánto más» (<i>a fortiori</i>).</b> «¿Cuánto peor castigo…?» (v. 29): el v. 28 es el caso menor y el v. 29 el mayor. La literatura académica lo ve así: Coetsee (<i>Verbum et Ecclesia</i> 45/1, 2024, pp. 3–4): «Hebrews 10:28–29 contains an a fortiori (qal wahomer) argument […], with verse 28 providing the lesser situation»; el v. 28 alude a Dt 17:6 (los dos o tres testigos).</li>
<li><b>El «castigo peor» lo ejecuta Dios.</b> Los vv. 30–31 citan Dt 32:35–36: «Mía es la venganza; yo pagaré… El Señor juzgará a su pueblo»; «terrible cosa es caer en manos <i>del Dios vivo</i>». La misma cita sirve a Pablo para <i>prohibir</i> la venganza personal (Rom 12:19).</li>
<li><b>Los destinatarios eran las víctimas</b> (10:32–34): injuriados, encarcelados, despojados de sus bienes, y los exhorta a perseverar y a «perseguir la paz con todos» (12:14).</li>
<li><b>La misma carta</b> declara «antigua» la primera alianza (8:13), «débil e inútil» el mandamiento anterior porque «la ley nada perfeccionó» (7:18–19) y «sombra» a la ley (10:1).</li>
</ul>
<div class="box ojo"><h3>Ojo</h3>Hebreos <b>sí</b> menciona una pena de muerte (la de la ley de Moisés) y <b>sí</b> advierte con dureza del juicio de Dios a quien abandona a Cristo (10:26–27, 29–31). Lo que no hace es mandar a los cristianos ejecutarla; y tampoco «condena» la ley antigua: la cita como antecedente legítimo. La ley del v. 28 es la de Dt 17:2–7 (idolatría/apostasía bajo la alianza de Moisés, con la regla de los dos o tres testigos).</div>'''
page(OUT, 'HB01_es', 'HB01', 'Hebreos 10:26–31 · el propio texto', 'Resumen en español',
     'Hebreos 10:28 leído en su contexto: describe, razona «cuánto más» y termina en el juicio de Dios',
     'Texto griego: SBLGNT (SBL y Logos, CC BY 4.0), obtenido de MorphGNT; traducción literal mía. Coetsee: doi 10.4102/ve.v45i1.3068 (acceso abierto, CC BY).', body,
     'Fuentes: morphgnt/sblgnt (GitHub) para el griego; A. J. Coetsee, «Warning through song and legislation? An intertextual study of Hebrews 10:26–31 and Deuteronomy», Verbum et Ecclesia 45(1), 2024, a3068 (PDF de scielo.org.za).<br>' + PACK)

# ---------------------------------------------------------------- HB02 (silogismos 1-3)
def sy(n, title, ps, c, note=''):
    pr = ''.join(f'<p><b class="p">P{i+1}.</b> {p}</p>' for i, p in enumerate(ps))
    nt = f'<div class="n">{note}</div>' if note else ''
    return f'<div class="sy"><div class="t">{E(title)}<span>silogismo {n}</span></div><div class="b">{pr}<div class="c">{c}</div>{nt}</div></div>'
S = [
 sy(1, 'Descripción y prescripción',
    ['Un texto que describe una sanción jurídica vigente en otro marco histórico no ordena, por ese solo hecho, que sus lectores la apliquen.',
     'Hebreos 10:28 describe lo que ocurría bajo la ley de Moisés (<span class="gr">ἀποθνῄσκει</span>, presente descriptivo) y en 10:26–31 no hay ningún imperativo dirigido a los lectores.'],
    'C. Hebreos 10:28 no manda a los cristianos ejecutar a quienes abandonan la fe.',
    'Respaldo: comprobado en el griego (HB01). No hace falta negar que la ley de Moisés contemplara la pena capital.'),
 sy(2, 'Quién ejerce el castigo',
    ['Si el autor atribuye la retribución a Dios y no ordena a nadie ejecutarla, el pasaje no autoriza imponerla con violencia humana.',
     'Hebreos 10:30 cita «Mía es la venganza; yo pagaré» y «El Señor juzgará a su pueblo» (Dt 32:35–36), y 10:31 habla de caer «en manos del Dios vivo».'],
    'C. El castigo mayor del pasaje es juicio divino, no una sentencia que los cristianos deban ejecutar; convertirlo en orden de matar añade algo que el texto no dice.',
    'Respaldo: Rom 12:19 usa la misma cita para <i>prohibir</i> que los cristianos se venguen.'),
 sy(3, 'El argumento «cuánto más» (a fortiori)',
    ['Una comparación de castigos hecha para mostrar la gravedad de una falta no implica que ambos castigos los ejecuten las mismas autoridades.',
     'Hebreos 10:28–29 compara la sanción de la ley de Moisés con un castigo «peor» para quien rechaza a Cristo.',
     'El propio pasaje identifica ese castigo mayor con el juicio de Dios (10:30–31).'],
    'C. La comparación establece la gravedad de rechazar a Cristo, pero no autoriza a los cristianos a aplicar una pena capital.',
    'Respaldo académico: A. J. Coetsee, Verbum et Ecclesia 45/1 (2024), pp. 3–4: «a fortiori (qal wahomer) argument […] with verse 28 providing the lesser situation» (alusión a Dt 17:6).'),
]
body = ''.join(S) + '<div class="box"><h3>Idea de fondo</h3>Para decir que un pasaje ordena violencia religiosa hay que demostrar que <b>manda</b> ejercerla, no solo que <b>recuerda</b> una sanción histórica. Mencionar una pena capital no equivale a ordenar su aplicación.</div>'
page(OUT, 'HB02_es', 'HB02', 'Hebreos 10:28 · silogismos (1/2)', 'Resumen en español',
     'Tres silogismos: descripción frente a prescripción, quién castiga y el argumento «cuánto más»',
     'Los silogismos parten de la guía aportada por el usuario; cada premisa se contrastó con el texto griego y con la bibliografía citada.', body,
     'Premisas bíblicas comprobadas en el griego (SBLGNT). Traducciones mías.<br>' + PACK)

# ---------------------------------------------------------------- HB02b (silogismos 4-5 + pasajes)
S2 = [
 sy(4, 'La Antigua y la Nueva Alianza',
    ['Una disposición judicial propia de una alianza anterior no pasa a regir a los miembros de otra por el mero hecho de ser mencionada.',
     'Hebreos 8:13 declara «antigua» a la primera alianza al decir «nueva»; 7:18–19 la llama «débil e inútil», pues «la ley nada perfeccionó»; 10:1 la llama «sombra».',
     'Hebreos 10:28 cita una disposición judicial de la alianza mosaica sin incorporarla al régimen jurídico de la comunidad cristiana.'],
    'C. Hebreos 10:28 no obliga a los cristianos a aplicar aquella sanción judicial.'),
 sy(5, 'El argumento definitivo (carga de la prueba)',
    ['Afirmar que un pasaje ordena violencia religiosa a sus destinatarios exige demostrar que establece un mandato, y no solo que recuerda una sanción histórica.',
     'Hebreos 10:28 no contiene ese mandato: refiere la ley mosaica; y 10:29–31 la usa para advertir del juicio de Dios, sin instituir procedimiento humano alguno de ejecución.'],
    'C. Hebreos 10:28–31 no prescribe que los cristianos ejecuten a los apóstatas; leerlo así es una inferencia que no se sigue del texto.'),
]
rows = [
 ('Hb 10:30–31', 'El juicio anunciado se atribuye a Dios: «Mía es la venganza; yo pagaré… Terrible cosa es caer en manos del Dios vivo».'),
 ('Hb 10:32–34', 'Los destinatarios habían sufrido injurias, cárcel y despojo; se les exhorta a perseverar, no a castigar.'),
 ('Hb 12:14', '«Perseguid la paz con todos, y la santificación…».'),
 ('Rom 12:19', '«No os venguéis vosotros mismos… dad lugar a la ira; porque escrito está: Mía es la venganza; yo pagaré, dice el Señor».'),
 ('Lc 9:51–56', 'Santiago y Juan proponen hacer bajar fuego del cielo sobre una aldea que no los recibe: Jesús «se volvió y los reprendió».'),
 ('Mt 26:52 · Jn 18:36', '«Vuelve tu espada a su lugar…»; «Mi reino no es de este mundo; si lo fuera, mis servidores combatirían».'),
 ('2 Co 10:3–4 · 2 Tm 2:24–26', '«Las armas de nuestra milicia no son carnales…»; «el siervo del Señor no debe pelear… corrigiendo con mansedumbre a los que se oponen, por si Dios les concede arrepentimiento».'),
]
tbl = '<table class="v"><tr><th>Pasaje</th><th>Qué dice (traducción literal mía del griego)</th></tr>' + ''.join(f'<tr><td class="who">{E(a)}</td><td>{E(b)}</td></tr>' for a, b in rows) + '</table>'
body = ''.join(S2) + '<h2 class="g">Pasajes del Nuevo Testamento que apuntan en la misma dirección</h2>' + tbl + '<div class="box ojo"><h3>Objeción previsible</h3>«Hebreos 10:26–27 habla de “fuego que ha de devorar a los adversarios”.» Sí: es una advertencia seria a los cristianos, pero escatológica: la ejecuta Dios («el Dios vivo»), no la comunidad. Nadie niega que el autor considere gravísima la apostasía; lo que se niega es que ordene una ejecución humana.</div>'
page(OUT, 'HB02b_es', 'HB02b', 'Hebreos 10:28 · silogismos (2/2) y pasajes', 'Resumen en español',
     'Dos silogismos más y los pasajes del Nuevo Testamento que confirman la lectura',
     'Textos griegos comprobados (SBLGNT, vía MorphGNT); traducciones literales mías.', body,
     'Fuente de los textos griegos: morphgnt/sblgnt (SBLGNT, CC BY 4.0). Lc 9:51–56 y Mt 26:52 verificados en esa edición.<br>' + PACK)

# ---------------------------------------------------------------- HB03 (distinción)
rows = [
 ('Mt 5:17', 'No vine a abolir la ley o los profetas, sino a <b>cumplir</b> [llevar a plenitud] (<span class="gr">πληρῶσαι</span>).', 'La ley es de Dios y está orientada a su plenitud en Cristo.'),
 ('Mt 5:38–39', '«Habéis oído que se dijo: Ojo por ojo y diente por diente. <b>Pero yo os digo</b>: no resistáis al malvado».', 'La norma antigua limita la venganza; la nueva la supera.'),
 ('Mt 19:8', '«Por vuestra <b>dureza de corazón</b> os permitió Moisés repudiar a vuestras mujeres; pero <b>desde el principio no fue así</b>».', 'Jesús mismo dice que parte de la ley de Moisés fue una concesión al contexto, aún no plena.'),
 ('Ga 3:24–25', '«La ley ha sido nuestro <b>pedagogo</b> hacia Cristo… llegada la fe, ya no estamos bajo pedagogo».', 'La ley como etapa educativa.'),
 ('Hb 7:18–19 · 8:13 · 10:1', '«Débil e inútil… la ley nada perfeccionó»; «antigua… próxima a desaparecer»; «<b>sombra</b> de los bienes venideros».', 'El propio Hebreos hace la distinción: sombra y plenitud.'),
]
tbl = '<table class="v"><tr><th>Pasaje</th><th>Qué dice (traducción literal mía)</th><th>Qué muestra</th></tr>' + ''.join(f'<tr><td class="who">{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in rows) + '</table>'
body = f'''<div class="ans"><b>La distinción.</b> En el Nuevo Testamento y en los Padres, <b>el Evangelio es la moral plena</b> y la ley de Moisés es una <b>moral contextualizada, pedagógica y todavía no plena</b> (la misma de Dios, dada a un pueblo y a un momento). Por eso las penas del código mosaico (Dt 13 y 17: la muerte por idolatría o apostasía) <b>no son la norma de la comunidad cristiana</b>, aunque Hebreos las cite como antecedente.</div>
{tbl}
<h2 class="g">Lo que sale al final de esa distinción (para la Iglesia)</h2>
<ul class="l">
<li><b>La sanción de la Iglesia es espiritual:</b> amonestar, «rehuir» al sectario tras una primera y segunda amonestación (Tt 3:10), no comer con quien causa escándalo y «entregarlo a Satanás para que el espíritu sea salvo» (1 Co 5:5, 11–13), tenerlo «como el gentil y el publicano» (Mt 18:17). El apóstol añade: «a los de fuera los juzga Dios» (1 Co 5:13).</li>
<li><b>El juicio último es de Dios</b> (Hb 10:30; Rom 12:19) y la cizaña «se deja crecer juntamente hasta la siega» (Mt 13:29–30).</li>
<li><b>El Reino no se defiende con la espada</b> (Mt 26:52; Jn 18:36; 2 Co 10:4; Lc 9:54–56).</li>
</ul>
<div class="box ojo"><h3>Ojo</h3>La distinción no dice que el Antiguo Testamento fuera «inmoral»: Ireneo, Tertuliano o Agustín (P04, P05, P02) lo presentan como pedagogía del mismo Dios. Tampoco dice que la autoridad civil no pueda castigar delitos (Rom 13): los Padres separan los <i>delitos</i> de la <i>fe</i>. Y «moral plena» es el criterio cristiano; no significa que cada cristiano o cada época lo haya cumplido (ver Agustín y Jerónimo en P02 y P08).</div>'''
page(OUT, 'HB03_es', 'HB03', 'Evangelio y Antiguo Testamento', 'Resumen en español',
     'La distinción entre el Evangelio (moral plena) y la ley de Moisés (moral contextualizada y aún no plena)',
     'Textos comprobados en el griego (SBLGNT, vía MorphGNT); traducciones literales mías.', body,
     'Mt 5:17, 5:38–39, 18:15–17, 19:8, 13:29–30; Ga 3:24–25; Hb 7:18–19, 8:13, 10:1; 1 Co 5; Tt 3:10 comprobados en el griego.<br>' + PACK)

# ---------------------------------------------------------------- AQ01
body = f'''<div class="two">
<div class="pn"><h4>Latín (Corpus Thomisticum)</h4><div class="lat">Respondeo dicendum quod circa haereticos duo sunt consideranda […]. Ex parte quidem ipsorum est peccatum per quod meruerunt non solum ab Ecclesia per excommunicationem separari, sed etiam <mark class="k">per mortem a mundo excludi</mark>. Multo enim gravius est corrumpere fidem, per quam est animae vita, quam falsare pecuniam […]. Unde […] haeretici, statim cum de haeresi convincuntur, possent non solum excommunicari, sed et iuste occidi. […] Postmodum vero, si adhuc pertinax inveniatur, Ecclesia […] eum ab Ecclesia separando per excommunicationis sententiam; et ulterius <mark class="k">relinquit eum iudicio saeculari</mark> a mundo exterminandum per mortem. Dicit enim Hieronymus, et habetur <mark class="a">XXIV, qu. III</mark>: resecandae sunt putridae carnes, et scabiosa ovis a caulis repellenda […].</div></div>
<div class="pn"><h4>Español (traducción mía)</h4><div class="es2">Sobre los herejes hay que considerar dos cosas […]. Por su parte, hay un pecado por el que merecieron no solo ser separados de la Iglesia por la excomunión, sino también <mark class="k">ser excluidos del mundo por la muerte</mark>. Porque es mucho más grave corromper la fe, por la que vive el alma, que falsificar moneda […]. Por tanto […] los herejes, en cuanto son convictos de herejía, podrían no solo ser excomulgados sino también ser muertos con justicia. […] Después, si aún se halla pertinaz, la Iglesia […] lo separa de sí por sentencia de excomunión y además <mark class="k">lo deja al juicio secular</mark> para ser exterminado del mundo por la muerte. Pues dice Jerónimo, y se recoge en el <mark class="a">Decreto, 24 q. 3</mark>: «hay que cortar las carnes podridas y apartar del aprisco a la oveja sarnosa […]».</div></div></div>
<h2 class="g">Lo que se ve en el propio texto (Suma de Teología, II-II, q. 11, a. 3)</h2>
<ul class="l">
<li><b>Su fuente es un texto jurídico y una cita de Jerónimo, no la tradición apostólica:</b> apoya su respuesta en Tito 3:10 y en Jerónimo (<i>Comentario a Gálatas</i> 5:9), <b>tal como se recoge en el Decreto de Graciano (24 q. 3)</b>, la compilación canónica del siglo XII; en la respuesta 3 vuelve a citar el Decreto («<i>Decret. XXIV, qu. III, can. Notandum</i>»). Es decir, repite el derecho canónico de su tiempo.</li>
<li><b>Quien ejecuta es el poder secular:</b> la Iglesia «lo deja al juicio secular»; ella separa por excomunión. Y solo habla de herejes <b>convictos y pertinaces</b>, tras «la primera y segunda corrección».</li>
<li><b>Él mismo distingue a los no creyentes:</b> a quienes nunca recibieron la fe (gentiles y judíos) «de ningún modo se les ha de forzar a creer, porque creer es cosa de la voluntad» (II-II, q. 10, a. 8); la coacción corporal que admite se refiere a bautizados que luego se apartan (herejes y apóstatas).</li>
<li><b>Aquino conoce la posición contraria de los Padres:</b> en la q. 10, a. 8, objeción 1, cita a Crisóstomo (Hom. 46 sobre Mateo): «No conviene, en efecto, matar a los herejes, porque si los matáis es necesario que muchos de los santos [justos] sean arrancados a la vez» (en la versión latina que él cita); y en la respuesta dice que «algunos entendieron» que ese texto prohíbe no la excomunión, <b>sino la muerte</b> de los herejes. Elige la otra opinión.</li>
</ul>
<div class="box"><h3>Qué sí dice el vídeo, y qué no</h3>El vídeo cita bien la idea de Aquino («corromper la fe más grave que falsificar moneda»; entrega al poder secular tras las correcciones). Lo que no dice es que Aquino lo funda en derecho canónico medieval, que habla de convictos pertinaces, y que él mismo cita a Crisóstomo en sentido contrario.</div>'''
page(OUT, 'AQ01_es', 'AQ01', 'Aquino · qué dice y de dónde lo toma', 'Resumen en español',
     'Tomás de Aquino, Suma de Teología II-II, q. 11, a. 3: qué dice, de qué fuente lo toma y a quién cita en contra',
     'Latín: corpusthomisticum.org (Suma de Teología, IIª-IIae q. 1–16). Inglés de comprobación: traducción de los Padres Dominicos Ingleses (1920), newadvent.org/summa. Traducción al español mía.', body,
     'Citas: ST II-II q. 11 a. 3 (co., ad 3); q. 10 a. 8 (arg. 1, co., ad 1). Jerónimo, In Gal. 5:9, según lo cita Aquino; el contexto original de Jerónimo se ve en P08.<br>' + PACK)

# ---------------------------------------------------------------- AQ02
rows = [
 ('Tardío', 'Nació hacia 1225 y murió en 1274: unos <b>1 200 años después de los apóstoles</b>. La Suma de Teología se escribió entre 1265 y 1274. El período patrístico se da por concluido, por convención, hacia los siglos VII–VIII (Isidoro de Sevilla, † 636; Juan Damasceno, † c. 749); Aquino viene <b>más de cinco siglos después</b>.'),
 ('No es Padre de la Iglesia', 'Fue declarado <b>Doctor de la Iglesia</b> en 1567 por Pío V (canonizado en 1323). «Doctor» no es «Padre»: sus opiniones teológicas no son testimonio de la tradición apostólica, que es lo que se pregunta a los Padres.'),
 ('No era jurista', 'Fraile dominico, <b>teólogo y filósofo</b> (así lo describen las obras de referencia), maestro de teología en París. Su respuesta en la q. 11 a. 3 no es una ley: es una cuestión teológica que remite al <b>Decreto de Graciano</b> y a la tradición canónica de los juristas medievales. No fue legislador ni juez.'),
 ('Una opinión teológica, no la tradición apostólica', 'La q. 11 a. 3 es la respuesta de un teólogo medieval a una cuestión disciplinaria. La Iglesia católica enseña hoy lo contrario en la práctica: el Concilio Vaticano II declara que «todos los hombres han de estar inmunes de coacción» en lo religioso y que «a nadie se obligue a obrar contra su conciencia» (<i>Dignitatis humanae</i>, 2, 1965).'),
 ('Residual, no generalizado (con alcance)', 'Frente a los Padres, la posición de Aquino es <b>residual</b>: lo habitual en los Padres leídos aquí es lo contrario (P01–P08), y la primera ejecución de herejes por la autoridad civil cristiana (Prisciliano, 385) la rechazó Martín de Tours: «bastaba que, declarados herejes por sentencia de los obispos, fueran expulsados de las iglesias» (Sulpicio Severo, <i>Historia Sagrada</i> II, 50). Ver el «Ojo».'),
]
tbl = '<table class="v"><tr><th>Por qué no es referente de la tradición apostólica</th><th>Qué se puede afirmar con las fuentes</th></tr>' + ''.join(f'<tr><td class="who">{a}</td><td>{b}</td></tr>' for a, b in rows) + '</table>'
body = tbl + '''<div class="box ojo"><h3>Ojo (por honestidad)</h3>«Residual» es exacto <b>respecto de los Padres y de la tradición apostólica</b>, no respecto de la Edad Media latina: allí la ejecución de herejes estuvo prevista en leyes y prácticas (p. ej., la legislación de Federico II de 1224 y la inquisición medieval), de modo que no se puede decir que fuera marginal en esa época. Tampoco hay unanimidad entre los Padres: algunos aceptaron la coacción o incluso aplaudieron la pena capital: León I (carta 15, hacia 447) celebra que los gobernantes «abatieron con la espada de las leyes públicas» al promotor del priscilianismo y a la mayoría de sus discípulos, aunque dice que la Iglesia «rehúye la venganza sangrienta» (ver también Agustín y Jerónimo en P02 y P08). Lo que sí se mantiene es que <b>no es la tradición apostólica ni la posición dominante de los Padres</b>, y que el propio Aquino sabía que la autoridad de Crisóstomo iba en contra.</div>'''
page(OUT, 'AQ02_es', 'AQ02', 'Aquino · tardío, teólogo, no jurista', 'Resumen en español',
     'Por qué Aquino no es referente de la tradición apostólica: es tardío, es teólogo (no jurista) y su opinión es residual frente a los Padres',
     'Datos de Aquino: Wikipedia (c. 1225–1274; dominico, teólogo y filósofo; canonizado en 1323; Doctor de la Iglesia en 1567). Dignitatis humanae 2: vatican.va. Martín de Tours: Sulpicio Severo, Sacred History II.50 (NPNF2-11, newadvent.org/fathers/35052.htm).', body,
     'Las fechas del período patrístico son una convención histórica; el alcance de «residual» se explica en el recuadro. La legislación medieval (Federico II, 1224) la cito de memoria como dato general, no la verifiqué en una fuente primaria para este pack.<br>' + PACK)

# ---------------------------------------------------------------- CV01
rows = [
 ('Hadiz (Nasaʾi 4059, ʿAʾisha)', '«El que sale del islam y combate a Alá y a Su Mensajero: es muerto, crucificado o desterrado». El vídeo dice: <b>no equiparar con el abandono pacífico</b>; hay que <b>distinguir</b>.'),
 ('Hebreos 10:28', 'Descripción de la ley de Moisés + argumento «cuánto más» hacia el juicio de Dios (HB01–HB02). Si el vídeo aplica su principio, <b>no equiparar sin distinguir</b>: no es un mandato cristiano.'),
 ('Aquino', 'Opinión teológica tardía que se apoya en derecho canónico medieval y cita a Crisóstomo en contra (AQ01–AQ02). Distinguir: <b>no es tradición apostólica</b>.'),
]
tbl = '<table class="v"><tr><th>Texto</th><th>Qué pasa si se aplica «distinguir antes de equiparar»</th></tr>' + ''.join(f'<tr><td class="who">{a}</td><td>{b}</td></tr>' for a, b in rows) + '</table>'
body = f'''<div class="ans"><b>El vídeo se refuta con su propio método.</b> Para el hadiz dice: «equiparar automáticamente ambos supuestos supondría ignorar una distinción fundamental». Pero hace exactamente eso con Hebreos 10:28 y con Aquino: los presenta como si fueran el equivalente cristiano de una ley penal, sin distinguir entre <b>describir</b> y <b>mandar</b>, ni entre <b>la Escritura y las opiniones tardías de un teólogo</b>.</div>
{tbl}
<h2 class="g">Cuatro fallos del argumento</h2>
<ul class="l">
<li><b>1 · «Tú también» no responde.</b> Aunque un texto cristiano fuera tan duro, eso no dice si la pena islámica por apostasía es justa. Es un argumento <i>tu quoque</i>: reparte culpas, no prueba nada. Y no es cierto que Hebreos o Aquino sean equivalentes (HB01–AQ02).</li>
<li><b>2 · Autoridad distinta.</b> El hadiz que muestra el vídeo lo da la ficha de un sitio web como <b>ṣaḥīḥ</b> (Albānī, <i>Ṣaḥīḥ al-Nasāʾī</i>; se ve en pantalla): es texto de las colecciones canónicas del islam sunní. Aquino no es Escritura ni Padre, y Hebreos no tiene mandato.</li>
<li><b>3 · El «consenso de los sabios» sale al revés.</b> El título del vídeo invoca el «consenso de los sabios»; el consenso de los Padres que leímos es no matar a los herejes (P01–P08). En el derecho islámico clásico la regla se formula para la apostasía misma (ver CV02).</li>
<li><b>4 · Cuando se concede la distinción, se cambia de tema.</b> Si la pena fuera solo por rebelión armada, ya no sería una pena por cambiar de religión y no habría paralelo con Hebreos ni con Aquino, que tratan de la fe misma.</li>
</ul>'''
page(OUT, 'CV01_es', 'CV01', 'El cierre del vídeo (1/2)', 'Resumen en español',
     'La distinción que hace el vídeo, aplicada a sus propios ejemplos: no se puede equiparar sin distinguir',
     'Argumento construido sobre la transcripción del vídeo (0:55–1:12) y sobre HB01–AQ02. Calificación del hadiz: la que muestra el propio vídeo (Albānī, «ṣaḥīḥ»).', body,
     'La frase «equiparar automáticamente ambos supuestos supondría ignorar una distinción fundamental» es del vídeo (1:01–1:11).<br>' + PACK)

# ---------------------------------------------------------------- CV02
body = f'''<div class="ans"><b>La distinción «apostasía pacífica / apostasía con rebelión».</b> El vídeo tiene una parte de razón: la versión del hadiz que muestra (Nasaʾi 4059, ʿAʾisha) habla de quien sale del islam <b>y combate</b> a Alá y a Su Mensajero. Pero esa no es la única base de la doctrina clásica, y las fuentes tempranas y los juristas la formulan también para <b>quien sale del islam sin combatir</b>. Lo que sigue lo leí en las páginas originales en el pack de apostasía (<code>apostasia-fuentes-tempranas</code>); no es investigación nueva de este pack.</div>
<table class="v"><tr><th>Tarjeta AP</th><th>Fuente</th><th>Qué dice (resumen)</th></tr>
<tr><td class="who">AP01 · AP03</td><td>Bujari 6922; Bujari 6878</td><td>«Quien cambie su religión, matadlo»; y «no es lícita la sangre de un musulmán salvo por una de tres… el que se aparta de la religión, el que abandona la comunidad» (sin mención de combate).</td></tr>
<tr><td class="who">AP37 · AP39</td><td>Ibn al-Mundhir; Ibn Qudama</td><td>«Los sabios convinieron en que si apostata… y no se arrepiente, es muerto; no conozco desacuerdo»; «convinieron en la obligatoriedad de matar al apóstata».</td></tr>
<tr><td class="who">AP46</td><td>Ibn Rushd (nieto), <i>Bidaya</i></td><td>«El apóstata, <b>si se le captura antes de que combata</b>, acordaron que se mata al hombre».</td></tr>
<tr><td class="who">AP38</td><td>Ibn al-Mundhir</td><td>La apostasía se prueba con <b>dos testigos</b> y por ella se mata si no vuelve al islam.</td></tr>
<tr><td class="who">AP16 · AP18 · AP22</td><td>al-Sarakhsi; Ibn Taymiyya; Peters y De Vries</td><td><b>Matiz que favorece al vídeo:</b> los hanafíes razonan la pena como «repeler el combate» (y no matan a las mujeres); Ibn Taymiyya recoge una lectura del hadiz por el combatiente; los modernistas limitan la pena al apóstata hostil.</td></tr></table>
<h2 class="g">El cierre sobre la traición</h2>
<ul class="l">
<li><b>La ley de traición castiga actos, no creencias.</b> La Constitución de EE. UU. (art. III, secc. 3) dice que la traición «consistirá únicamente en hacer la guerra contra ellos o en ayudar a sus enemigos», que se prueba por <b>«dos testigos del mismo acto manifiesto»</b> o confesión en juicio, y 18 U.S.C. § 2381 castiga a quien «hace la guerra contra ellos o se une a sus enemigos». Cambiar de religión no es traición.</li>
<li><b>Dilema.</b> Si la pena del hadiz es por <b>traición</b>, debe exigir actos de guerra probados, y entonces las formulaciones clásicas «sin combatir» (AP01, AP03, AP46) no se sostienen. Si es por <b>salir de la religión</b>, la comparación con la traición falla.</li>
<li><b>Sin salida por Hebreos ni Aquino:</b> la pregunta sobre el hadiz se contesta con las fuentes islámicas, no con lo que digan los cristianos; y lo que digan ellos ya está respondido (HB01–AQ02).</li>
</ul>
<div class="box ojo"><h3>Ojo</h3>Hay posiciones islámicas que limitan la pena a la apostasía hostil (modernistas, algunos hanafíes) y relatos de arrepentimiento aceptado (AP20); se citan arriba. Esta diapositiva no afirma que el islam «ordene» o «no ordene» matar al apóstata en general: compara cómo se usa la distinción en el vídeo con lo que dicen las fuentes leídas. Las traducciones y las calificaciones de cadenas son las del pack AP.</div>'''
page(OUT, 'CV02_es', 'CV02', 'El cierre del vídeo (2/2)', 'Resumen en español',
     'Apostasía pacífica y apostasía con rebelión; y por qué la comparación con la traición no cuadra',
     'Constitución de EE. UU., art. III, secc. 3 (archives.gov); 18 U.S.C. § 2381 (law.cornell.edu). Tarjetas AP del pack «La pena para el apóstata en los textos islámicos tempranos».', body,
     'Textos legales comprobados en las páginas oficiales. Las citas islámicas remiten a las tarjetas AP del pack apostasia-fuentes-tempranas (leídas en su día en Shamela y hadithunlocked.com; no vueltas a abrir en este pack).<br>' + PACK)
print('estáticas ok')
