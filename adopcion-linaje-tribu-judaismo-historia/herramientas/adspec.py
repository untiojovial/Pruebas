# -*- coding: utf-8 -*-
# Especificación de las 34 pruebas (AD01–AD34). Los textos originales salen de passages.json (ya comprobados contra su página);
# las traducciones al español son mías. Las marcas [[k:...]] resaltan la frase clave.
import json, unicodedata, re
AD = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ad'
_P = {}
def P(ag, pid):
    if ag not in _P:
        _P[ag] = {p['id']: p for p in json.load(open(f'{AD}/{ag}/passages.json', encoding='utf-8'))}
    return _P[ag][pid]
def _norm(c):
    d = unicodedata.normalize('NFKD', c).casefold()
    return ''.join(x for x in d if not unicodedata.combining(x) and x.isalnum()).replace('ς', 'σ')
def mark_letters(text, keys):
    """Envuelve en [[k:..]] el tramo de `text` que corresponde (solo letras, sin vocales ni acentos) a cada clave."""
    pos = []   # (letra normalizada, índice original)
    for i, ch in enumerate(text):
        for n in _norm(ch):
            pos.append((n, i))
    flat = ''.join(p[0] for p in pos)
    spans = []
    for k in keys:
        kk = ''.join(_norm(c) for c in k)
        j = flat.find(kk)
        if j < 0: raise ValueError('clave no encontrada: ' + k)
        a = pos[j][1]; b = pos[j + len(kk) - 1][1] + 1
        while b < len(text) and unicodedata.combining(text[b]): b += 1   # incluye vocales/acentos finales
        spans.append((a, b))
    spans.sort()
    for (a1, b1), (a2, b2) in zip(spans, spans[1:]):
        if a2 < b1: raise ValueError('claves solapadas')
    out = text
    for a, b in reversed(spans):
        out = out[:a] + '[[k:' + out[a:b] + ']]' + out[b:]
    return out
def q(ag, pid, field='quote_orig'): return P(ag, pid)[field]
def S(url): return url

SEF = 'Sefaria (Miqra according to the Masorah, CC BY-SA)'
JPS = 'JPS 1917 (inglés, dominio público)'
WSK = 'Wikisource Talmud Bavli (ed. Vilna) vía Sefaria, CC BY-SA'
CARDS = []
def add(**c): CARDS.append(c)

# ============================ A · Adopción y herencia tribal (Efraín y Manasés) ============================
c = dict(id='AD01', tags=['A'], scope='DIRECT', lang='he', work='Génesis', author='Biblia hebrea (Torá)', date='texto bíblico',
 title='Génesis 48:5-6 · Jacob hace suyos a Efraín y Manasés «como Rubén y Simeón»', ref='Génesis 48:5-6',
 edition='Miqra according to the Masorah (Sefaria; CC BY-SA)', orig_url='https://www.sefaria.org/Genesis.48.5-6',
 url='https://www.sefaria.org/Genesis.48.5-6', base='Texto hebreo (Miqra según la Masorá, vía Sefaria) cotejado con JPS 1917',
 licence='Hebreo: Miqra according to the Masorah, vía Sefaria (CC BY-SA). Inglés de cotejo: JPS 1917 (dominio público).',
 es='«Y ahora tus dos hijos, que te nacieron en la tierra de Egipto antes de que yo viniera a ti a Egipto, míos son: Efraín y Manasés, [[como Rubén y Simeón serán míos]]. Pero los hijos que engendres después de ellos serán tuyos; [[por el nombre de sus hermanos serán llamados en su heredad]].»',
 shows='Jacob declara suyos a los dos hijos de José nacidos en Egipto y los pone en el mismo rango que Rubén y Simeón; a los hijos que José engendre después, los inscribe «en su heredad» bajo el nombre de sus hermanos. Es el pasaje que comentan después los targumim, Rashi, el Midrás y Josefo.')
c['orig'] = mark_letters(q('A1', 'A1-P01'), ['כראובן ושמעון יהיו לי', 'על שם אחיהם יקראו בנחלתם']); add(**c)

c = dict(id='AD02', tags=['A'], scope='DIRECT', lang='he', work='Génesis', author='Biblia hebrea (Torá)', date='texto bíblico',
 title='Génesis 48:16 · «Sea nombrado en ellos mi nombre y el de mis padres»', ref='Génesis 48:16',
 edition='Miqra according to the Masorah (Sefaria; CC BY-SA)', orig_url='https://www.sefaria.org/Genesis.48.16',
 url='https://www.sefaria.org/Genesis.48.16', base='Texto hebreo (Miqra según la Masorá, vía Sefaria) cotejado con JPS 1917',
 licence='Hebreo: Miqra according to the Masorah, vía Sefaria (CC BY-SA). Inglés de cotejo: JPS 1917 (dominio público).',
 es='«El ángel que me ha redimido de todo mal bendiga a los muchachos, y [[sea nombrado en ellos mi nombre y el nombre de mis padres, Abraham e Isaac]], y crezcan en multitud en medio de la tierra.»',
 shows='En la misma escena de Gn 48, Jacob pide que su nombre y el de Abraham e Isaac sea nombrado sobre los dos jóvenes: los vincula expresamente con el nombre de los patriarcas.')
c['orig'] = mark_letters(q('A1', 'A1-P02'), ['ויקרא בהם שמי ושם אבתי אברהם ויצחק']); add(**c)

c = dict(id='AD03', tags=['A'], scope='DIRECT', lang='he', work='Targum Onkelos sobre Génesis', author='Tradición targúmica (atribuida a Onkelos)', date='antigüedad tardía (fecha discutida)',
 title='Targum Onkelos sobre Gn 48:5-6 · «como Rubén y Simeón serán delante de mí»', ref='Targum Onkelos, Génesis 48:5-6 (arameo)',
 edition='«Onkelos Genesis» (Sefaria; dominio público)', orig_url='https://www.sefaria.org/Onkelos_Genesis.48.5',
 url='https://www.sefaria.org/Onkelos_Genesis.48.5', base='Arameo (Sefaria) cotejado con la traducción inglesa de J. W. Etheridge (1862, dominio público)',
 licence='Arameo: «Onkelos Genesis» (Sefaria, dominio público). Inglés de cotejo: Etheridge 1862 (dominio público por antigüedad).',
 es='«Y ahora tus dos hijos que te nacieron en la tierra de Egipto, antes de que yo viniera a ti a Egipto, míos son: Efraín y Manasés, [[como Rubén y Simeón serán delante de mí]]. Y los hijos que engendres después de ellos serán tuyos; [[por el nombre de sus hermanos serán llamados en su heredad]].»',
 shows='El Targum arameo oficial de la Torá traduce «serán míos» como «serán delante de mí», como Rubén y Simeón, y mantiene que los hijos posteriores de José serán llamados «por el nombre de sus hermanos en su heredad».')
c['orig'] = mark_letters(q('A2', 'A2-P02'), ['כראובן ושמעון יהון קדמי', 'על שום אחוהון יתקרון באחסנתהון']); add(**c)

c = dict(id='AD04', tags=['A'], scope='DIRECT', lang='he', work='Targum Pseudo-Jonatán sobre Génesis', author='Tradición targúmica (anónimo)', date='fecha discutida (antigüedad tardía–Edad Media)',
 title='Targum Pseudo-Jonatán sobre Gn 48:5-6 · «serán contados para mí»', ref='Targum Pseudo-Jonatán, Génesis 48:5-6 (arameo)',
 edition='«Targum Jonathan on Genesis» (Sefaria; dominio público)', orig_url='https://www.sefaria.org/Targum_Jonathan_on_Genesis.48.5',
 url='https://www.sefaria.org/Targum_Jonathan_on_Genesis.48.5', base='Arameo (Sefaria) cotejado con la traducción inglesa de J. W. Etheridge (1862, dominio público)',
 licence='Arameo: «Targum Jonathan on Genesis» (Sefaria, dominio público). Inglés de cotejo: Etheridge 1862 (dominio público por antigüedad).',
 es='«Y ahora tus dos hijos que te nacieron en la tierra de Egipto, antes de que yo viniera a ti a Egipto, míos son: Efraín y Manasés, como Rubén y Simeón [[serán contados para mí]]; y los hijos que engendres después de ellos serán tuyos; [[por el nombre de sus hermanos serán llamados en su heredad]].»',
 shows='El Targum Pseudo-Jonatán traduce «serán míos» como «serán contados para mí» (מִתְחַשְׁבִין לִי): Efraín y Manasés son tenidos por hijos de Jacob a la par de Rubén y Simeón.')
c['orig'] = mark_letters(q('A2', 'A2-P03'), ['מתחשבין לי', 'על שום אחיהון יתקרון באחסנתהון']); add(**c)

c = dict(id='AD05', tags=['A'], scope='DIRECT', lang='he', work='Comentario de Rashi a Génesis', author='Rashi (Shlomó Yitsjaquí)', date='1040–1105',
 title='Rashi sobre Gn 48:5 · «Cuentan entre mis demás hijos, para tomar parte en la Tierra»', ref='Rashi sobre Génesis 48:5, «לי הם»',
 edition='Rosenbaum y Silbermann, 1929–1934 (Sefaria; dominio público)', orig_url='https://www.sefaria.org/Rashi_on_Genesis.48.5',
 url='https://www.sefaria.org/Rashi_on_Genesis.48.5', base='Hebreo de Rashi (Rosenbaum y Silbermann, 1929–34, vía Sefaria)',
 licence='Hebreo y traducción inglesa de Rosenbaum y Silbermann (1929–34): dominio público (metadatos de Sefaria).',
 es='«[[Míos son]]: [[en el cómputo de mis demás hijos son, para tomar parte en la Tierra]], cada uno por su lado.»',
 shows='Rashi explica «míos son» (Gn 48:5) como: se cuentan entre los demás hijos de Jacob y reciben, cada uno, una porción en la Tierra. Es la lectura judía clásica que vincula la frase de Jacob con el reparto de la tierra entre las tribus.')
c['orig'] = mark_letters(q('A2', 'A2-P04'), ['בחשבון שאר בני הם לטל חלק בארץ']); c['es'] = '«Míos son: [[se cuentan en el cómputo de mis demás hijos, para tomar parte en la Tierra]], cada uno por su lado.»'; add(**c)

c = dict(id='AD06', tags=['A'], scope='DIRECT', lang='he', work='Midrás Tanjumá, Vayejí', author='Anónimo', date='compilación tardoantigua–medieval (fecha discutida)',
 title='Midrás Tanjumá, Vayejí 6:6 · «Comenzó a hacer tribus a los hijos de José»', ref='Midrás Tanjumá, Vayejí 6:6',
 edition='Midrash Tanchuma — Torat Emet (Sefaria; dominio público)', orig_url='https://www.sefaria.org/Midrash_Tanchuma,_Vayechi.6.6',
 url='https://www.sefaria.org/Midrash_Tanchuma,_Vayechi.6.6', base='Hebreo (Torat Emet, vía Sefaria) cotejado con la traducción inglesa de S. A. Berman (CC BY)',
 licence='Hebreo: Midrash Tanchuma — Torat Emet (dominio público, Sefaria). Inglés de cotejo: Berman (CC BY).',
 es='«Y dijo Jacob a José: “El Dios Todopoderoso…”, etcétera; y dijo: “He aquí que yo te haré fecundo y te multiplicaré”. [[Comenzó a hacer tribus a los hijos de José]], pues está dicho: “Efraín y Manasés, como Rubén y Simeón, serán míos”.»',
 shows='El midrás entiende que, al decir Jacob «Efraín y Manasés, como Rubén y Simeón, serán míos», empezó a hacer tribus a los hijos de José: la declaración de Jacob los constituye como tribus.')
c['orig'] = mark_letters(q('A2', 'A2-P16'), ['התחיל עושה את בני יוסף שבטים']); add(**c)

c = dict(id='AD07', tags=['A'], scope='DIRECT', lang='en', work='Antigüedades judías', author='Flavio Josefo', date='c. 93–94 d. C.',
 title='Josefo, Antigüedades 2.8.1 · «admitan entre ellos a los hijos de José»', ref='Josefo, Antigüedades judías II, 8, 1 (numeración de Whiston)',
 edition='Traducción inglesa de W. Whiston (1737), Project Gutenberg n.º 2848', orig_url='https://www.gutenberg.org/ebooks/2848',
 url='https://www.gutenberg.org/cache/epub/2848/pg2848.txt', base='Traducción inglesa de Whiston (1737); no he leído el griego',
 licence='Whiston 1737 (Project Gutenberg n.º 2848; dominio público en EE. UU.). Texto griego no consultado.',
 es='«Ordenó entonces a sus propios hijos que [[admitieran entre ellos a los hijos de José, Efraín y Manasés, y repartieran con ellos la tierra de Canaán]]».',
 shows='Josefo cuenta que Jacob mandó a sus hijos que admitieran en su número a Efraín y Manasés y que dividieran con ellos la tierra de Canaán: los dos jóvenes entran en el reparto igual que los demás hijos.')
c['orig'] = mark_letters(q('A5', 'A5-P10', 'quote_en'), ["admit Joseph's sons, Ephraim and Manasses, into their number, and divide the land of Canaan in common with them"]); add(**c)

c = dict(id='AD08', tags=['A'], scope='DIRECT', lang='en', work='Antigüedades judías', author='Flavio Josefo', date='c. 93–94 d. C.',
 title='Josefo, Antigüedades 3.12.4 · «para que fueran suyos por adopción»', ref='Josefo, Antigüedades judías III, 12, 4 (numeración de Whiston)',
 edition='Traducción inglesa de W. Whiston (1737), Project Gutenberg n.º 2848', orig_url='https://www.gutenberg.org/ebooks/2848',
 url='https://www.gutenberg.org/cache/epub/2848/pg2848.txt', base='Traducción inglesa de Whiston (1737); no he leído el griego',
 licence='Whiston 1737 (Project Gutenberg n.º 2848; dominio público en EE. UU.). Texto griego no consultado.',
 es='«En lugar de Leví, Moisés tomó a Manasés, hijo de José, entre los jefes de las tribus; y a Efraín en lugar de José. Era, en efecto, el deseo del propio Jacob a José, que le diera a sus hijos [[para que fueran suyos por adopción]], como ya he relatado.»',
 shows='Josefo usa expresamente la palabra «adopción» para Efraín y Manasés y añade que, en el censo del desierto, Manasés entra «entre los jefes de las tribus» y Efraín ocupa el lugar de José.')
c['orig'] = mark_letters(q('A5', 'A5-P02', 'quote_en'), ['to be his own by adoption', 'Ephraim instead of Joseph']); add(**c)

c = dict(id='AD09', tags=['A'], scope='ANALOGY', lang='he', work='1 Crónicas', author='Biblia hebrea (Ketuvim)', date='texto bíblico',
 title='1 Crónicas 5:1-2 · La primogenitura de Rubén «fue dada a los hijos de José»', ref='1 Crónicas 5:1-2',
 edition='Miqra according to the Masorah (Sefaria; CC BY-SA)', orig_url='https://www.sefaria.org/I_Chronicles.5.1-2',
 url='https://www.sefaria.org/I_Chronicles.5.1-2', base='Texto hebreo (Miqra según la Masorá, vía Sefaria) cotejado con JPS 1917',
 licence='Hebreo: Miqra according to the Masorah, vía Sefaria (CC BY-SA). Inglés de cotejo: JPS 1917 (dominio público).',
 es='«Y los hijos de Rubén, primogénito de Israel —pues él era el primogénito, pero por haber profanado el lecho de su padre, [[su primogenitura fue dada a los hijos de José]], hijo de Israel, aunque no para ser registrado en la genealogía como primogénito. Porque Judá prevaleció sobre sus hermanos, y de él vino el príncipe, pero la primogenitura fue de José—.»',
 shows='El cronista dice que la primogenitura de Rubén pasó a los hijos de José (las tribus de Efraín y Manasés): un derecho hereditario transferido por la voluntad del padre, que el pasaje distingue del liderazgo, que corresponde a Judá.')
c['orig'] = mark_letters(q('A1', 'A1-P03'), ['נתנה בכרתו לבני יוסף', 'והבכרה ליוסף']); add(**c)

# ============================ B · Principio rabínico ============================
c = dict(id='AD10', tags=['B'], scope='ANALOGY', lang='he', work='Talmud Bavli, Sanedrín 19b', author='Anónimo (amoraím y estamaím)', date='redacción c. s. VI d. C.',
 title='Sanedrín 19b · Los hijos de Merab se llaman «de Mical», que los crió', ref='Talmud Bavli, Sanedrín 19b (sobre 2 Sam 21:8)',
 edition='Talmud Bavli (Wikisource, ed. Vilna) vía Sefaria; CC BY-SA', orig_url='https://www.sefaria.org/Sanhedrin.19b',
 url='https://www.sefaria.org/Sanhedrin.19b', base='Texto hebreo-arameo (Wikisource, ed. Vilna, vía Sefaria); sin traducción inglesa de dominio público; traducción mía',
 licence='Hebreo-arameo: Wikisource Talmud Bavli (CC BY-SA; el texto de Vilna es de dominio público). Traducción mía.',
 es='«Y R. Josué ben Korjá [objeta]: ¿no está escrito “los cinco hijos de Mical, hija de Saúl”? Te dice R. Josué: ¿acaso Mical los dio a luz?, ¿no los dio a luz Merab? Merab los dio a luz y Mical los crió; [[por eso fueron llamados por su nombre]]. Para enseñarte que [[todo el que cría a un huérfano en su casa, la Escritura se lo cuenta como si lo hubiera engendrado]].»',
 shows='La Guemará establece que a quien cría a un huérfano en su casa la Escritura se lo cuenta «como si lo hubiera engendrado», y que por eso los hijos de Merab son llamados por el nombre de Mical (2 Sam 21:8). Es el principio rabínico de que la crianza atribuye la filiación.')
c['orig'] = mark_letters(q('A3', 'P04'), ['לפיכך נקראו על שמה', 'שכל המגדל יתום בתוך ביתו מעלה עליו הכתוב כאילו ילדו']); add(**c)

c = dict(id='AD11', tags=['B'], scope='ANALOGY', lang='he', work='Talmud Bavli, Sanedrín 19b', author='Anónimo (amoraím y estamaím)', date='redacción c. s. VI d. C.',
 title='Sanedrín 19b · Los hijos de Aarón se llaman de Moisés, que los enseñó', ref='Talmud Bavli, Sanedrín 19b (sobre Núm 3:1)',
 edition='Talmud Bavli (Wikisource, ed. Vilna) vía Sefaria; CC BY-SA', orig_url='https://www.sefaria.org/Sanhedrin.19b',
 url='https://www.sefaria.org/Sanhedrin.19b', base='Texto hebreo-arameo (Wikisource, ed. Vilna, vía Sefaria) cotejado con Rodkinson (1918, dominio público); traducción mía',
 licence='Hebreo-arameo: Wikisource Talmud Bavli (CC BY-SA; el texto de Vilna es de dominio público). Cotejo: Rodkinson 1918 (dominio público). Traducción mía.',
 es='«Todo el que enseña Torá al hijo de su prójimo, [[la Escritura se lo cuenta como si lo hubiera engendrado]], pues se dice (Núm 3:1): “Y estas son las generaciones de Aarón y Moisés”, y está escrito: “Y estos son los nombres de los hijos de Aarón”. Para decirte: Aarón engendró y Moisés enseñó; [[por eso fueron llamados por su nombre]].»',
 shows='Los hijos de Aarón figuran en la Torá como «generaciones de Aarón y Moisés»: la Guemará lo explica diciendo que Aarón los engendró y Moisés los enseñó, y que por eso se les llama por el nombre de Moisés.')
c['orig'] = mark_letters(q('A3', 'P08'), ['מעלה עליו הכתוב כאילו ילדו', 'לפיכך נקראו על שמו']); add(**c)

c = dict(id='AD12', tags=['B'], scope='ANALOGY', lang='he', work='Talmud Bavli, Meguilá 13a', author='Anónimo (amoraím y estamaím)', date='redacción c. s. VI d. C.',
 title='Meguilá 13a · «Quien cría a un huérfano… como si lo hubiera engendrado»', ref='Talmud Bavli, Meguilá 13a (sobre 1 Crón 4:18)',
 edition='Talmud Bavli (Wikisource, ed. Vilna) vía Sefaria; CC BY-SA', orig_url='https://www.sefaria.org/Megillah.13a',
 url='https://www.sefaria.org/Megillah.13a', base='Texto hebreo-arameo (Wikisource, ed. Vilna, vía Sefaria) cotejado con Rodkinson (1918, dominio público); traducción mía',
 licence='Hebreo-arameo: Wikisource Talmud Bavli (CC BY-SA; el texto de Vilna es de dominio público). Cotejo: Rodkinson 1918 (dominio público). Traducción mía.',
 es='«[¿Acaso Bitia] lo dio a luz? ¿No fue ella quien lo crió? Para decirte que [[todo el que cría a un huérfano o a una huérfana en su casa, la Escritura se lo cuenta como si lo hubiera engendrado]].»',
 shows='A propósito de Bitia, hija del faraón, y de Moisés (1 Crón 4:18), la Guemará enuncia el principio general: quien cría a un huérfano o a una huérfana en su casa es tenido por la Escritura como quien lo engendró.')
c['orig'] = mark_letters(q('A3', 'P07'), ['כל המגדל יתום ויתומה בתוך ביתו מעלה עליו הכתוב כאילו ילדו']); add(**c)

c = dict(id='AD13', tags=['A'], scope='DIRECT', lang='he', work='Éxodo', author='Biblia hebrea (Torá)', date='texto bíblico',
 title='Éxodo 2:10 · Moisés «fue para ella un hijo»', ref='Éxodo 2:10',
 edition='Miqra according to the Masorah (Sefaria; CC BY-SA)', orig_url='https://www.sefaria.org/Exodus.2.10',
 url='https://www.sefaria.org/Exodus.2.10', base='Texto hebreo (Miqra según la Masorá, vía Sefaria) cotejado con JPS 1917',
 licence='Hebreo: Miqra according to the Masorah, vía Sefaria (CC BY-SA). Inglés de cotejo: JPS 1917 (dominio público).',
 es='«Y creció el niño, y ella lo llevó a la hija del faraón, y [[fue para ella un hijo]]; y [[le puso por nombre Moisés]], y dijo: “Porque de las aguas lo saqué”.»',
 shows='El niño, llevado a la hija del faraón, «fue para ella un hijo» y ella le puso el nombre: la Torá usa el lenguaje de la filiación y del nombre para quien no nació de ella.')
c['orig'] = mark_letters(q('A1', 'A1-P09'), ['ויהי לה לבן', 'ותקרא שמו משה']); add(**c)

c = dict(id='AD14', tags=['A'], scope='DIRECT', lang='en', work='Antigüedades judías', author='Flavio Josefo', date='c. 93–94 d. C.',
 title='Josefo, Antigüedades 2.9.7 · Termutis adopta a Moisés como hijo y heredero', ref='Josefo, Antigüedades judías II, 9, 7 (numeración de Whiston)',
 edition='Traducción inglesa de W. Whiston (1737), Project Gutenberg n.º 2848', orig_url='https://www.gutenberg.org/ebooks/2848',
 url='https://www.gutenberg.org/cache/epub/2848/pg2848.txt', base='Traducción inglesa de Whiston (1737); no he leído el griego (el original inglés tiene una nota «21» y una frase truncada que aquí se omiten con […])',
 licence='Whiston 1737 (Project Gutenberg n.º 2848; dominio público en EE. UU.). Texto griego no consultado.',
 es='«Termutis, pues, viendo que era un niño tan notable, [[lo adoptó por hijo]], no teniendo hijo propio. […] “[…] pensé conveniente [[adoptarlo como hijo mío y heredero de tu reino]].”»',
 shows='Según Josefo, la hija del faraón adoptó a Moisés como hijo y propuso a su padre hacerlo su sucesor y «heredero de tu reino»: la adopción se plantea aquí como vía de herencia y de sucesión real.')
c['orig'] = mark_letters("Thermuthis therefore perceiving him to be so remarkable a child, adopted him for her son, having no child of her own. […] “[…] I thought proper to adopt him my son, and the heir of thy kingdom.”", ['adopted him for her son', 'adopt him my son, and the heir of thy kingdom']); add(**c)

c = dict(id='AD15', tags=['A'], scope='ANALOGY', lang='he', work='Ester', author='Biblia hebrea (Ketuvim)', date='texto bíblico',
 title='Ester 2:7 · «Mardoqueo la tomó para sí como hija»', ref='Ester 2:7',
 edition='Miqra according to the Masorah (Sefaria; CC BY-SA)', orig_url='https://www.sefaria.org/Esther.2.7',
 url='https://www.sefaria.org/Esther.2.7', base='Texto hebreo (Miqra según la Masorá, vía Sefaria) cotejado con JPS 1917',
 licence='Hebreo: Miqra according to the Masorah, vía Sefaria (CC BY-SA). Inglés de cotejo: JPS 1917 (dominio público).',
 es='«Y crió a Hadasa, es decir, Ester, hija de su tío, pues no tenía padre ni madre; la joven era de hermosa figura y de buen aspecto; y al morir su padre y su madre, [[Mardoqueo la tomó para sí como hija]].»',
 shows='Mardoqueo, primo de Ester, la cría y, muertos sus padres, «la toma para sí como hija»: el texto bíblico describe una adopción dentro de la misma familia.')
c['orig'] = mark_letters(q('A1', 'A1-P10'), ['לקחה מרדכי לו לבת']); add(**c)

# ============================ E · Levirato y filiación legal ============================
c = dict(id='AD16', tags=['E'], scope='ANALOGY', lang='he', work='Deuteronomio', author='Biblia hebrea (Torá)', date='texto bíblico',
 title='Deuteronomio 25:5-6 · El primogénito del levirato «sucederá en el nombre de su hermano muerto»', ref='Deuteronomio 25:5-6',
 edition='Tanach with Ta’amei Hamikra (Sefaria; dominio público)', orig_url='https://www.sefaria.org/Deuteronomy.25.5-10',
 url='https://www.sefaria.org/Deuteronomy.25.5-10', base='Texto hebreo (Tanach with Ta’amei Hamikra, vía Sefaria) cotejado con JPS 1917',
 licence='Hebreo: Tanach with Ta’amei Hamikra (dominio público, Sefaria). Inglés de cotejo: JPS 1917 (dominio público).',
 es='«Cuando habiten juntos hermanos y muera uno de ellos sin hijo, la mujer del muerto no se casará fuera con un extraño; su cuñado vendrá a ella, la tomará por mujer y cumplirá con ella el deber de cuñado. Y el primogénito que ella dé a luz [[sucederá en el nombre de su hermano muerto]], para que [[su nombre no sea borrado de Israel]].»',
 shows='La ley bíblica del levirato asigna al primogénito de la viuda el nombre del hermano muerto, para que ese nombre no desaparezca de Israel: la filiación legal sigue al nombre, no solo a la sangre.')
c['orig'] = mark_letters(q('A4', 'E-06'), ['יקום על שם אחיו המת', 'ולא ימחה שמו מישראל']); add(**c)

c = dict(id='AD17', tags=['E'], scope='ANALOGY', lang='he', work='Rut', author='Biblia hebrea (Ketuvim)', date='texto bíblico',
 title='Rut 4:9-10 · «Levantar el nombre del muerto sobre su heredad»', ref='Rut 4:9-10',
 edition='Tanach with Ta’amei Hamikra (Sefaria; dominio público)', orig_url='https://www.sefaria.org/Ruth.4.9-10',
 url='https://www.sefaria.org/Ruth.4.1-22', base='Texto hebreo (Tanach with Ta’amei Hamikra, vía Sefaria) cotejado con JPS 1917',
 licence='Hebreo: Tanach with Ta’amei Hamikra (dominio público, Sefaria). Inglés de cotejo: JPS 1917 (dominio público).',
 es='«Y Booz dijo a los ancianos y a todo el pueblo: “Ustedes son hoy testigos de que he comprado todo lo que era de Elimélec, y todo lo que era de Quilión y de Majlón, de mano de Noemí. Y también a Rut la moabita, mujer de Majlón, la he adquirido por mujer, [[para levantar el nombre del muerto sobre su heredad]], para que no sea borrado el nombre del muerto de entre sus hermanos ni de la puerta de su lugar; hoy son ustedes testigos”.»',
 shows='Booz declara ante testigos que toma a Rut para levantar el nombre del muerto (Majlón) sobre su heredad: el hijo de esa unión ocupará el nombre y la heredad del difunto.')
c['orig'] = mark_letters(q('A4', 'E-03', 'quote_orig'), ['להקים שם המת על נחלתו']); add(**c)

c = dict(id='AD18', tags=['E'], scope='ANALOGY', lang='he', work='Rut', author='Biblia hebrea (Ketuvim)', date='texto bíblico',
 title='Rut 4:16-17 · «Le ha nacido un hijo a Noemí»', ref='Rut 4:16-17',
 edition='Miqra according to the Masorah (Sefaria; CC BY-SA)', orig_url='https://www.sefaria.org/Ruth.4.16-17',
 url='https://www.sefaria.org/Ruth.4.16-17', base='Texto hebreo (Miqra según la Masorá, vía Sefaria) cotejado con JPS 1917',
 licence='Hebreo: Miqra according to the Masorah, vía Sefaria (CC BY-SA). Inglés de cotejo: JPS 1917 (dominio público).',
 es='«Y Noemí tomó al niño, lo puso en su regazo y [[fue su nodriza]]. Y las vecinas le pusieron nombre, diciendo: “[[Le ha nacido un hijo a Noemí]]”; y le pusieron por nombre Obed; él es el padre de Isaí, padre de David.»',
 shows='La comunidad proclama «le ha nacido un hijo a Noemí» sobre el niño de Rut, que Noemí cría en su regazo, y ese niño es el abuelo de David: la atribución del hijo a la casa de Elimélec y Noemí forma parte del relato que llega hasta David.')
c['orig'] = mark_letters(q('A1', 'A1-P15'), ['ותהי לו לאמנת', 'ילד בן לנעמי']); add(**c)

c = dict(id='AD19', tags=['E', 'A'], scope='ANALOGY', lang='he', work='Talmud Bavli, Yebamot 24a', author='Anónimo (amoraím y estamaím)', date='redacción c. s. VI d. C.',
 title='Yebamot 24a · El «nombre» del levirato es «para la heredad» (Gn 48:6)', ref='Talmud Bavli, Yebamot 24a (sobre Dt 25:6)',
 edition='Talmud Bavli (Wikisource, ed. Vilna) vía Sefaria; CC BY-SA', orig_url='https://www.sefaria.org/Yevamot.24a',
 url='https://www.sefaria.org/Yevamot.24a', base='Texto hebreo-arameo (Wikisource, ed. Vilna, vía Sefaria); sin traducción inglesa de dominio público; traducción mía',
 licence='Hebreo-arameo: Wikisource Talmud Bavli (CC BY-SA; el texto de Vilna es de dominio público). Traducción mía.',
 es='«[…] ¿Dices “para la heredad” o no es sino “por el nombre” —a José se le llama José, a Yojanán se le llama Yojanán? Se dice aquí “sucederá en el nombre de su hermano” y se dice allí (Gn 48:6) “por el nombre de sus hermanos serán llamados en su heredad”: [[así como el nombre mencionado allí es para la heredad, también el nombre mencionado aquí es para la heredad]].»',
 shows='La baraita lee el «nombre» del levirato (Dt 25:6) como «para la heredad» por analogía verbal con Gn 48:6, el verso de Efraín y Manasés: el Talmud une el caso del levirato con el de la adopción de los hijos de José.')
c['orig'] = mark_letters(q('A3', 'P03'), ['מה שם האמור להלן נחלה אף שם האמור כאן לנחלה']); add(**c)

c = dict(id='AD20', tags=['E'], scope='ANALOGY', lang='en', work='Antigüedades judías', author='Flavio Josefo', date='c. 93–94 d. C.',
 title='Josefo, Antigüedades 4.8.23 · El hijo del levirato, «heredero de su herencia»', ref='Josefo, Antigüedades judías IV, 8, 23 (numeración de Whiston)',
 edition='Traducción inglesa de W. Whiston (1737), Project Gutenberg n.º 2848', orig_url='https://www.gutenberg.org/ebooks/2848',
 url='https://www.gutenberg.org/cache/epub/2848/pg2848.txt', base='Traducción inglesa de Whiston (1737); no he leído el griego',
 licence='Whiston 1737 (Project Gutenberg n.º 2848; dominio público en EE. UU.). Texto griego no consultado.',
 es='«Si muere el marido de una mujer y la deja sin hijos, que se case con ella su hermano, y que [[llame al hijo que le nazca con el nombre de su hermano y lo eduque como heredero de su herencia]], pues este procedimiento será para beneficio público, porque así no faltarán las familias y la hacienda continuará entre los parientes;»',
 shows='Josefo resume la ley del levirato: el hijo nacido del cuñado lleva el nombre del hermano muerto y es educado como heredero de la herencia del difunto, para que las familias no se extingan.')
c['orig'] = mark_letters(q('A4', 'E-02', 'quote_en'), ["call the son that is born to him by his brother's name, and educate him as the heir of his inheritance"]); add(**c)

# ============================ C · Incorporación a una tribu o linaje ============================
c = dict(id='AD21', tags=['C'], scope='ANALOGY', lang='he', work='Ezequiel', author='Biblia hebrea (Profetas)', date='texto bíblico',
 title='Ezequiel 47:22-23 · Los forasteros reciben heredad «en la tribu en que residan»', ref='Ezequiel 47:22-23',
 edition='Miqra according to the Masorah (Sefaria; CC BY-SA)', orig_url='https://www.sefaria.org/Ezekiel.47.22-23',
 url='https://www.sefaria.org/Ezekiel.47.22-23', base='Texto hebreo (Miqra según la Masorá, vía Sefaria) cotejado con JPS 1917',
 licence='Hebreo: Miqra according to the Masorah, vía Sefaria (CC BY-SA). Inglés de cotejo: JPS 1917 (dominio público).',
 es='«Y sucederá que la repartirán por suerte como heredad para ustedes y para los forasteros que residen en medio de ustedes, que hayan engendrado hijos entre ustedes; y [[serán para ustedes como el natural entre los hijos de Israel]]; con ustedes echarán suerte por heredad en medio de las tribus de Israel. Y sucederá que [[en la tribu en que resida el forastero, allí le darán su heredad]], dice el Señor Dios.»',
 shows='En la visión del reparto de la tierra, Ezequiel manda tratar a los forasteros residentes que tengan hijos «como el natural entre los hijos de Israel» y darles heredad en la tribu donde residan.')
c['orig'] = mark_letters(q('A1', 'A1-P05'), ['והיו לכם כאזרח בבני ישראל', 'בשבט אשר גר הגר אתו שם תתנו נחלתו']); add(**c)

X = json.load(open(f'{AD}/extra_he.json', encoding='utf-8'))
hb34 = X['c2_34']
c = dict(id='AD22', tags=['C'], scope='ANALOGY', lang='he', work='1 Crónicas', author='Biblia hebrea (Ketuvim)', date='texto bíblico',
 title='1 Crónicas 2:34-36 · Un siervo egipcio dentro de la genealogía de Judá', ref='1 Crónicas 2:34-36',
 edition='Miqra according to the Masorah (Sefaria; CC BY-SA)', orig_url='https://www.sefaria.org/I_Chronicles.2.34-36',
 url='https://www.sefaria.org/I_Chronicles.2.34-36', base='Texto hebreo (Miqra según la Masorá, vía Sefaria) cotejado con JPS 1917',
 licence='Hebreo: Miqra according to the Masorah, vía Sefaria (CC BY-SA). Inglés de cotejo: JPS 1917 (dominio público).',
 es='«[34] Y Sesán no tuvo hijos sino hijas; y Sesán tenía [[un siervo egipcio, de nombre Jarhá]]. [35] Y Sesán dio su hija a Jarhá, su siervo, por mujer, y ella le dio a luz a Atay. [36] Y Atay engendró a Natán, y Natán engendró a Zabad;»',
 shows='Sesán, que solo tenía hijas, da una de ellas a su siervo egipcio, y los descendientes (Atay, Natán, Zabad…) quedan registrados en la genealogía de Judá: un extranjero queda incorporado a un linaje de la tribu.')
c['orig'] = '[34] ' + mark_letters(hb34, ['עבד מצרי ושמו ירחע']) + '<br>[35-36] ' + q('A1', 'A1-P18'); add(**c)

hb136 = X['n13_6']
hb3212 = X['n32_12']
c = dict(id='AD23', tags=['C'], scope='ANALOGY', lang='he', work='Números y Josué', author='Biblia hebrea (Torá y Profetas)', date='texto bíblico',
 title='Números 13:6 · 32:12 · Josué 14:6 · Caleb «el cenezeo», de la tribu de Judá', ref='Números 13:6; 32:12; Josué 14:6',
 edition='Miqra according to the Masorah (Sefaria; CC BY-SA)', orig_url='https://www.sefaria.org/Numbers.13.6',
 url='https://www.sefaria.org/Numbers.13.6', base='Texto hebreo (Miqra según la Masorá, vía Sefaria) cotejado con JPS 1917',
 licence='Hebreo: Miqra according to the Masorah, vía Sefaria (CC BY-SA). Inglés de cotejo: JPS 1917 (dominio público).',
 es='«[Nm 13:6] [[De la tribu de Judá, Caleb hijo de Jefone]]. [Nm 32:12] Excepto Caleb hijo de Jefone, [[el cenezeo]], y Josué hijo de Nun, porque siguieron plenamente al Señor. [Jos 14:6] Y se acercaron los hijos de Judá a Josué en Guilgal, y Caleb hijo de Jefone, el cenezeo, le dijo: “Tú conoces la palabra que el Señor dijo a Moisés, hombre de Dios, acerca de mí y de ti en Cadés-Barnea.”»',
 shows='El texto presenta a Caleb a la vez como jefe de la tribu de Judá (Nm 13:6) y como «el cenezeo» (Nm 32:12; Jos 14:6), y lo hace hablar junto a «los hijos de Judá»: quien lleva un gentilicio distinto cuenta como representante de Judá.')
c['orig'] = ('[Nm 13:6] ' + mark_letters(hb136, ['למטה יהודה כלב בן יפנה']) + '<br>[Nm 32:12] ' + mark_letters(hb3212, ['הקנזי']) + '<br>[Jos 14:6] ' + mark_letters(q('A1', 'A1-P19'), ['כלב בן יפנה הקנזי'])); add(**c)

# ============================ G · Historia: derecho antiguo ============================
c = dict(id='AD24', tags=['G'], scope='DIRECT', lang='en', work='Código de Hammurabi', author='Hammurabi, rey de Babilonia (atribuido)', date='c. 1750 a. C.',
 title='Código de Hammurabi §185 · El adoptado criado «no puede ser reclamado»', ref='Código de Hammurabi §185 (numeración de King)',
 edition='Traducción inglesa de L. W. King (1910), Avalon Project (Yale)', orig_url='https://avalon.law.yale.edu/ancient/hamcode.asp',
 url='https://avalon.law.yale.edu/ancient/hamcode.asp', base='Traducción inglesa de L. W. King (1910); no he leído el acadio. La frase inglesa «and to his name as son» es tal como figura en esa página',
 licence='King 1910 (dominio público por fecha); la página del Avalon Project lleva un aviso de copyright 2008 de la biblioteca, sin licencia para la traducción. Acadio no consultado.',
 es='«Si un hombre adopta a un niño [[y lo toma a su nombre como hijo]] y lo cría, [[ese hijo ya crecido no puede ser reclamado]].»',
 shows='Una de las leyes más antiguas conservadas trata la adopción como filiación jurídica: el niño adoptado, tomado a nombre del adoptante «como hijo» y criado por él, ya no puede ser reclamado de vuelta.')
c['orig'] = mark_letters(q('A6', 'A6-G06', 'quote_en'), ['and to his name as son', 'can not be demanded back again']); add(**c)

c = dict(id='AD25', tags=['G'], scope='DIRECT', lang='el', work='Sobre la herencia de Menecles (Iseo 2)', author='Iseo (orador ático)', date='s. IV a. C.',
 title='Iseo 2.14 · El adoptado es introducido en la fratría y registrado en el demo', ref='Iseo 2 (Sobre la herencia de Menecles), 14',
 edition='Texto griego de cts.perseids.org (ed. Forster, Loeb 1927)', orig_url='cts.perseids.org · urn:cts:greekLit:tlg0017.tlg002.perseus-grc2:14',
 url='https://cts.perseids.org/api/cts/?request=GetPassage&urn=urn:cts:greekLit:tlg0017.tlg002.perseus-grc2:14', base='Griego (Perseids, ed. Forster) con traducción inglesa de E. S. Forster (Loeb, 1927)',
 licence='Forster, Loeb 1927: publicado en 1927, de dominio público en EE. UU. desde 2023 (por fecha; la página de Perseids no declara licencia).',
 es='«[…] habiéndome adoptado, [[me introduce entre los miembros de su fratría]], estando presentes estos, y [[me inscribe entre los demotas]] y entre los orgeones.»',
 shows='El hablante, adoptado en vida por Menecles, relata que este lo presentó a su fratría y lo inscribió entre los miembros de su demo y de su asociación religiosa: según este discurso, la adopción incorporaba al adoptado a la fratría y al demo del adoptante.')
c['orig'] = mark_letters(q('A7', 'G-A7-12'), ['εἰσάγει με εἰς τοὺς φράτορας', 'εἰς τοὺς δημότας με ἐγγράφει']); add(**c)

c = dict(id='AD26', tags=['G'], scope='DIRECT', lang='el', work='Sobre la herencia de Menecles (Iseo 2)', author='Iseo (orador ático)', date='s. IV a. C.',
 title='Iseo 2.42 · El adoptado sirve «en la tribu» del adoptante', ref='Iseo 2 (Sobre la herencia de Menecles), 42',
 edition='Texto griego de cts.perseids.org (ed. Forster, Loeb 1927)', orig_url='cts.perseids.org · urn:cts:greekLit:tlg0017.tlg002.perseus-grc2:42',
 url='https://cts.perseids.org/api/cts/?request=GetPassage&urn=urn:cts:greekLit:tlg0017.tlg002.perseus-grc2:42', base='Griego (Perseids, ed. Forster) con traducción inglesa de E. S. Forster (Loeb, 1927)',
 licence='Forster, Loeb 1927: publicado en 1927, de dominio público en EE. UU. desde 2023 (por fecha; la página de Perseids no declara licencia).',
 es='«[…] ejercí de gimnasiarca en el demo y me distinguí como hijo de aquel, y en todas las campañas que hubo durante ese tiempo [[serví en la tribu de aquel y en el demo]]».',
 shows='El mismo adoptado afirma que, como hijo de Menecles, sirvió en las campañas «en la tribu de aquel y en el demo» (phylé y dêmos): en su relato, el adoptado actúa dentro de la tribu del adoptante.')
c['orig'] = mark_letters(q('A7', 'G-A7-11'), ['ἐστράτευμαι ἐν τῇ φυλῇ τῇ ἐκείνου καὶ ἐν τῷ δήμῳ']); add(**c)

c = dict(id='AD27', tags=['G'], scope='DIRECT', lang='el', work='Sobre la herencia de Apolodoro (Iseo 7)', author='Iseo (orador ático)', date='s. IV a. C.',
 title='Iseo 7.17 · Inscrito como «Trasilo, hijo de Apolodoro»', ref='Iseo 7 (Sobre la herencia de Apolodoro), 17',
 edition='Texto griego de cts.perseids.org (ed. Forster, Loeb 1927)', orig_url='cts.perseids.org · urn:cts:greekLit:tlg0017.tlg007.perseus-grc2:17',
 url='https://cts.perseids.org/api/cts/?request=GetPassage&urn=urn:cts:greekLit:tlg0017.tlg007.perseus-grc2:17', base='Griego (Perseids, ed. Forster) con traducción inglesa de E. S. Forster (Loeb, 1927)',
 licence='Forster, Loeb 1927: publicado en 1927, de dominio público en EE. UU. desde 2023 (por fecha; la página de Perseids no declara licencia).',
 es='«Así fui adoptado por él en vida, y [[fui inscrito en el registro público como Trasilo, hijo de Apolodoro]], habiéndome adoptado él de este modo, como las leyes se lo permitían.»',
 shows='El hablante, hijo de la hermana de Apolodoro, cuenta que tras ser adoptado en vida se le inscribió en el registro público con el nombre «Trasilo, hijo de Apolodoro», conforme a las leyes que daban al adoptante ese poder.')
c['orig'] = mark_letters(q('A7', 'G-A7-01'), ['εἰς τὸ κοινὸν γραμματεῖον ἐνεγράφην Θράσυλλος Ἀπολλοδώρου']); add(**c)

c = dict(id='AD28', tags=['G'], scope='DIRECT', lang='la', work='Noches áticas, V, 19', author='Aulo Gelio', date='c. 125–después de 180 d. C.',
 title='Aulo Gelio 5.19.9 · Adrogación: hijo «como si hubiera nacido de ese padre»', ref='Aulo Gelio, Noches áticas V, 19, 9',
 edition='Texto latino de The Latin Library (gellius5)', orig_url='https://www.thelatinlibrary.com/gellius/gellius5.shtml',
 url='https://www.thelatinlibrary.com/gellius/gellius5.shtml', base='Latín (The Latin Library) con traducción inglesa de J. C. Rolfe (Loeb, 1927, vía Perseids)',
 licence='Rolfe, Loeb 1927: publicado en 1927, de dominio público en EE. UU. desde 2023 (por fecha; las páginas no declaran licencia).',
 es='«Quieran y ordenen que Lucio Valerio sea hijo de Lucio Ticio [[con tanto derecho y ley como si hubiera nacido de ese padre y de la madre de su familia]], y que aquel tenga sobre él potestad de vida y de muerte, como la tiene un padre sobre su hijo. Esto, tal como lo he dicho, así os lo pido, Quirites.»',
 shows='Gelio transmite la fórmula con la que el pueblo romano aprobaba una adrogación: el adoptado pasa a ser hijo del adoptante con el mismo derecho que si hubiera nacido de él, con la potestad paterna incluida.')
c['orig'] = mark_letters(q('A7', 'G-A7-05'), ['tam iure legeque filius siet, quam si ex eo patre matreque familias eius natus esset']); add(**c)

c = dict(id='AD29', tags=['G'], scope='DIRECT', lang='la', work='Instituciones de Justiniano, III, 2', author='Justiniano (compiladas por Triboniano y otros)', date='533 d. C.',
 title='Instituciones de Justiniano 3.2.2 · La adopción crea agnación', ref='Instituciones de Justiniano III, 2, 2',
 edition='Texto latino de The Latin Library (institutes3)', orig_url='https://www.thelatinlibrary.com/justinian/institutes3.shtml',
 url='https://www.gutenberg.org/cache/epub/5983/pg5983.txt', base='Latín (The Latin Library) con traducción inglesa de J. B. Moyle (1913, Project Gutenberg n.º 5983)',
 licence='Moyle 1913 (Project Gutenberg n.º 5983; dominio público). Latín: The Latin Library (sin licencia declarada).',
 es='«También por la adopción se constituye el derecho de agnación, por ejemplo entre los hijos naturales y aquellos a quienes su padre adoptó (y no hay duda de que se llaman propiamente consanguíneos); asimismo, si alguno de tus restantes agnados, por ejemplo un hermano o un tío paterno o, en fin, uno de grado más lejano, adopta a alguien, [[no se duda de que hay agnación entre ustedes]].»',
 shows='Las Instituciones de Justiniano afirman que la adopción crea parentesco legal (agnación): los hijos adoptados son «consanguíneos» de los naturales, y el adoptado de un agnado se convierte en agnado de toda la familia.')
c['orig'] = mark_letters(q('A7', 'G-A7-04'), ['Per adoptionem quoque adgnationis ius consistit', 'adgnatio inter vos esse non dubitatur']); add(**c)

c = dict(id='AD30', tags=['G'], scope='DIRECT', lang='la', work='Vida del divino Julio, 83', author='Suetonio', date='c. 120 d. C.',
 title='Suetonio, Divus Iulius 83.2 · César adopta a Octavio «en su familia y nombre»', ref='Suetonio, Divus Iulius 83, 2',
 edition='Texto latino de cts.perseids.org (Suetonio)', orig_url='cts.perseids.org · urn:cts:latinLit:phi1348.abo011.perseus-lat2:83',
 url='https://cts.perseids.org/api/cts/?request=GetPassage&urn=urn:cts:latinLit:phi1348.abo011.perseus-lat2:83', base='Latín (Perseids) con traducción inglesa de Thomson/Reed (1883, vía Perseids)',
 licence='Thomson/Reed 1883 (dominio público por fecha). Latín: Perseids (sin licencia declarada).',
 es='«en el último renglón [del testamento] adoptó además a Gayo Octavio [[en su familia y nombre]];»',
 shows='Suetonio cuenta que César, en su testamento, adoptó a Gayo Octavio —el futuro Augusto— incorporándolo a su familia y a su nombre: la adopción por testamento transmite nombre y casa.')
c['orig'] = mark_letters(q('A7', 'G-A7-08'), ['in familiam nomenque adoptauit']); add(**c)

c = dict(id='AD31', tags=['G'], scope='DIRECT', lang='la', work='Anales, XII', author='Tácito', date='c. 115–117 d. C.',
 title='Tácito, Anales 12.26 · Una ley adopta a Domicio en la familia Claudia con el nombre de Nerón', ref='Tácito, Anales XII, 25-26',
 edition='Texto latino de The Latin Library (tac.ann12)', orig_url='https://www.thelatinlibrary.com/tacitus/tac.ann12.shtml',
 url='https://classics.mit.edu/Tacitus/annals.8.xii.html', base='Latín (The Latin Library) con traducción inglesa de Church y Brodribb (MIT Classics Archive)',
 licence='Church y Brodribb (siglo XIX, dominio público por fecha). Latín: The Latin Library (sin licencia declarada).',
 es='«y se propuso una ley por la que [[pasara a la familia Claudia y al nombre de Nerón]].»',
 shows='Tácito cuenta que una ley adoptó a Domicio, el futuro Nerón, en la familia patricia de los Claudios y con el nombre de Nerón: la adopción cambia la familia y el nombre.')
c['orig'] = mark_letters(q('A7', 'G-A7-07'), ['in familiam Claudiam et nomen Neronis transiret']); add(**c)

# ============================ J · Jesús, José y David ============================
mt = ('Ἰωσὴφ υἱὸς Δαυίδ, μὴ φοβηθῇς παραλαβεῖν Μαρίαν τὴν γυναῖκά σου, τὸ γὰρ ἐν αὐτῇ γεννηθὲν ἐκ πνεύματός ἐστιν ἁγίου· '
      'τέξεται δὲ υἱὸν καὶ καλέσεις τὸ ὄνομα αὐτοῦ Ἰησοῦν, αὐτὸς γὰρ σώσει τὸν λαὸν αὐτοῦ ἀπὸ τῶν ἁμαρτιῶν αὐτῶν. […] '
      'καὶ οὐκ ἐγίνωσκεν αὐτὴν ἕως οὗ ἔτεκεν υἱόν· καὶ ἐκάλεσεν τὸ ὄνομα αὐτοῦ Ἰησοῦν.')
c = dict(id='AD32', tags=['J'], scope='ANALOGY', lang='el', work='Evangelio según Mateo', author='Mateo (atribución tradicional)', date='c. 80–100 d. C. (aprox.)',
 title='Mateo 1:20-25 · José, «hijo de David», pone el nombre al niño', ref='Mateo 1:20-21 y 1:25',
 edition='SBLGNT (Society of Biblical Literature y Faithlife, CC BY 4.0), vía MorphGNT', orig_url='https://github.com/morphgnt/sblgnt',
 url='https://github.com/morphgnt/sblgnt', base='Griego del SBLGNT (MorphGNT; lectura directa mía)',
 licence='SBLGNT: © Society of Biblical Literature y Faithlife, CC BY 4.0. Traducción mía.',
 es='«[20] “[[José, hijo de David]], no temas tomar contigo a María, tu mujer, porque lo engendrado en ella es del Espíritu Santo; [21] dará a luz un hijo y [[le pondrás por nombre Jesús]], porque él salvará a su pueblo de sus pecados.” […] [25] Y no la conocía hasta que dio a luz un hijo; y [[le puso por nombre Jesús]].»',
 shows='El ángel llama a José «hijo de David», le ordena tomar a María y poner el nombre al niño, y el evangelista narra que José lo hizo: es José, hijo de David, quien da el nombre a Jesús.')
c['orig'] = mark_letters(mt, ['Ἰωσὴφ υἱὸς Δαυίδ', 'καλέσεις τὸ ὄνομα αὐτοῦ Ἰησοῦν', 'ἐκάλεσεν τὸ ὄνομα αὐτοῦ Ἰησοῦν']); add(**c)

c = dict(id='AD33', tags=['J', 'E'], scope='ANALOGY', lang='en', work='Historia eclesiástica, I, 7 (cita de la Carta a Aristides)', author='Eusebio de Cesarea, citando a Julio Africano', date='Africano c. 220; Eusebio c. 325',
 title='Julio Africano (en Eusebio, HE I.7) · Generaciones «según la naturaleza o según la ley»', ref='Eusebio, Historia eclesiástica I, 7, 2',
 edition='Traducción inglesa de A. C. McGiffert, NPNF2 vol. 1 (1890), New Advent', orig_url='https://www.newadvent.org/fathers/250101.htm',
 url='https://www.newadvent.org/fathers/250101.htm', base='Traducción inglesa de McGiffert (NPNF2-01, 1890); no he leído el griego',
 licence='McGiffert 1890 (dominio público por fecha). Griego no consultado.',
 es='«Pues mientras que los nombres de las generaciones se contaban en Israel o bien según la naturaleza o bien según la ley —según la naturaleza, por la sucesión de la descendencia legítima; y [[según la ley, cada vez que otro suscitaba un hijo para el nombre de un hermano que moría sin hijos]]; porque, no habiéndose dado aún una esperanza clara de resurrección, tenían una representación de la promesa futura mediante una especie de resurrección mortal, a fin de que el nombre del difunto se perpetuara—»',
 shows='Africano distingue dos formas de contar las generaciones en Israel, «según la naturaleza» y «según la ley», y aplica esa distinción para explicar por qué las genealogías de Jesús en Mateo y Lucas difieren: una sería la línea natural de José y otra la legal.')
c['orig'] = mark_letters(q('A4', 'E-09', 'quote_en'), ['according to law whenever another raised up a child to the name of a brother dying childless']); add(**c)

ag = ("Joseph may have had two fathers — namely, one by whom he was begotten, and a second by whom he may have been adopted. For it was an ancient custom also among that people to adopt children with the view of making sons for themselves of those whom they had not begotten. "
      "For, leaving out of sight the fact that Pharaoh's daughter adopted Moses (as she was a foreigner), Jacob himself adopted his own grandsons, the sons of Joseph, in these very intelligible terms: Now, therefore, your two sons which were born unto you before I came unto you, are mine: Ephraim and Manasseh shall be mine, as Reuben and Simeon: and your issue which you beget after them shall be yours. "
      "Whence also it came to pass that there were twelve tribes of Israel […] Thus, too, we can understand how Luke, in the genealogy contained in his Gospel, has named a father for Joseph, not in the person of the father by whom he was begotten, but in that of the father by whom he was adopted, tracing the list of the progenitors upwards until David is reached.")
c = dict(id='AD34', tags=['J', 'A'], scope='DIRECT', lang='en', work='Armonía de los Evangelios, II, 3', author='Agustín de Hipona', date='c. 400 d. C.',
 title='Agustín, Armonía de los Evangelios II.3.5 · José, hijo de un padre por adopción', ref='Agustín, De consensu evangelistarum II, 3, 5',
 edition='Traducción inglesa de NPNF1 vol. 6 (Schaff, 1888), New Advent', orig_url='https://www.newadvent.org/fathers/1602203.htm',
 url='https://www.newadvent.org/fathers/1602203.htm', base='Traducción inglesa (NPNF1-06, 1888); no he localizado el latín',
 licence='NPNF1 vol. 6 (1888; dominio público por fecha). Latín no consultado.',
 es='«José pudo tener dos padres: uno por el cual fue engendrado, y un segundo por el cual [[pudo ser adoptado]]. Pues también entre aquel pueblo era costumbre antigua adoptar niños para hacerse hijos a aquellos a quienes no habían engendrado. Porque, dejando aparte que la hija del faraón adoptó a Moisés (siendo ella extranjera), [[Jacob mismo adoptó a sus propios nietos, los hijos de José]], en estos términos clarísimos: “Ahora, pues, tus dos hijos que te nacieron antes de que yo viniera a ti son míos: Efraín y Manasés serán míos, como Rubén y Simeón; y la descendencia que engendres después de ellos será tuya.” De ahí también que hubiera doce tribus de Israel […] Así también podemos entender cómo Lucas, en la genealogía de su Evangelio, ha puesto a José [[un padre que no es aquel por el cual fue engendrado, sino aquel por el cual fue adoptado]], remontando la lista de los antepasados hasta llegar a David.»',
 shows='Agustín sostiene que las dos genealogías de José pueden deberse a que tuvo un padre que lo engendró y otro que lo adoptó; apela a la costumbre de adoptar, a Moisés y a Efraín y Manasés, «de ahí también que hubiera doce tribus», y concluye que Lucas sigue la línea del padre adoptivo hasta David.')
c['orig'] = mark_letters(ag, ['by whom he may have been adopted', 'Jacob himself adopted his own grandsons, the sons of Joseph', 'in that of the father by whom he was adopted']); add(**c)

for _c in CARDS:
    _c['es'] = re.sub(r'\[\[(?![kag]:)(.+?)\]\]', r'[[k:\1]]', _c['es'])

if __name__ == '__main__':
    print(len(CARDS), 'tarjetas')
    for c in CARDS: print(c['id'], c['tags'], c['scope'], c['lang'], len(c['orig']), len(c['es']))
