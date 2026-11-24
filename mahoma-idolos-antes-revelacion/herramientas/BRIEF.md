# Encargo común (léelo entero)

PREGUNTA DE INVESTIGACIÓN: ¿Dicen al-Tabari (sobre todo) y otras fuentes suníes que el profeta Mahoma adoró ídolos, ofreció sacrificios a ídolos o siguió la religión politeísta de su pueblo ANTES de la revelación del Corán? Y, si hay textos así, ¿cómo los valoran los propios eruditos suníes?

Trabajas para una investigación honesta y documentada. Nuestro objetivo es saber QUÉ DICEN EXACTAMENTE LOS TEXTOS, no confirmar una tesis. Hay que recoger con la misma exactitud:
(a) los textos que lo afirman o lo sugieren;
(b) los que lo niegan expresamente (por ejemplo, «nunca tocó un ídolo»);
(c) cómo los interpretan o critican los eruditos (cadena de transmisión, autenticidad, doctrina de la impecabilidad o ʿiṣma).

## Fuentes que funcionan (usa WebFetch o curl con Bash)
- Al-Maktaba al-Shamila: https://shamela.ws/book/<ID>/<página>. Por ejemplo, Tarij al-Tabari es el libro 9783: https://shamela.ws/book/9783/1000. Cada página tiene volumen y número de página impresa. Para encontrar otros libros: https://shamela.ws/search?q=<texto> o la página del libro https://shamela.ws/book/<ID> (índice).
- Tafsir de al-Tabari, versículo a versículo (árabe): https://api.quran.com/api/v4/tafsirs/15/by_ayah/<sura>:<aleya> (devuelve JSON; el texto está en tafsir.text). Ibn Kathir árabe: id 14; Ibn Kathir inglés abreviado: id 169; al-Qurtubi: id 90.
- Hadices (árabe e inglés), espejo público: https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/<edición>/<número>.json. Ediciones: ara-bukhari, eng-bukhari, ara-muslim, eng-muslim, ara-nasai, ara-abudawud, ara-tirmidhi, ara-ibnmajah, ara-malik… Lista completa: https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions.json
- islamweb, biblioteca y fetuas: https://www.islamweb.net/ar/library/ (tiene libros de hadiz y tafsir con página).
- archive.org (traducciones y ediciones escaneadas): https://archive.org/advancedsearch.php?q=...&fl[]=identifier&rows=20&output=json y el texto OCR en https://archive.org/stream/<id>/<archivo>_djvu.txt
- Wikisource árabe: https://ar.wikisource.org

PROHIBIDO: sunnah.com, dorar.net, alukah.net, al-maktaba.org y cualquier sitio que muestre un control anti-bots o devuelva 403. No intentes saltártelos. Si una fuente falla, usa otra y anótalo.

## Reglas inviolables
1. NO INVENTES NADA: ni textos, ni cadenas, ni referencias, ni páginas, ni gradaciones. Solo vale lo que hayas leído en una página descargada.
2. Cada hallazgo lleva la CITA LITERAL en árabe (copiada tal cual) y, si existe, la traducción publicada (inglés), con la URL exacta de donde la leíste y la referencia (obra, volumen, página o número de hadiz).
3. Traduce tú al español cada cita, de forma literal, y señala las palabras ambiguas (por ejemplo, nuṣub o anṣāb: piedra de sacrificio o ídolo; ḍāll: extraviado o perdido; ʿalā dīn qawmī: según la religión de mi pueblo).
4. Distingue siempre: quién lo narra y por qué cadena; si es un dicho atribuido al Profeta, a un compañero o el comentario de un autor; y la valoración de autenticidad SOLO si la encuentras escrita (de quién, dónde).
5. Si una versión difiere de otra del mismo episodio (por ejemplo, quién ofreció la carne a quién), recoge ambas literalmente.
6. No abras subagentes. Escribe solo en tu archivo de salida. Guarda el JSON a menudo (cada 3-4 hallazgos).

## Formato de salida (JSON UTF-8, escrito con Python json.dump(ensure_ascii=False, indent=1))
{
 "ambito": "...",
 "busquedas": ["qué buscaste y dónde, con resultado"],
 "hallazgos": [ {
   "id": "H1",
   "obra": "autor, título",
   "referencia": "volumen, página o número de hadiz; edición si consta",
   "url": "…",
   "tipo": "relato histórico | hadiz | tafsir | comentario de erudito | estudio académico",
   "postura": "afirma | sugiere/ambiguo | niega | interpreta/critica",
   "narrador_y_cadena": "…(si consta)",
   "texto_arabe": "…cita literal…",
   "traduccion_publicada": "…(si existe, con su fuente)…",
   "traduccion_propia": "…",
   "palabras_ambiguas": "…",
   "valoracion_autenticidad": "…quién la califica y dónde, o NO CONSTA…",
   "comentario": "por qué importa y qué NO permite concluir"
 } ],
 "no_encontrado": ["lo que buscaste y no apareció"],
 "notas": "dudas, discrepancias, cosas a comprobar"
}
Al terminar, valida que el JSON carga con json.load e informa brevemente: número de hallazgos, los 5 más importantes y lo que no encontraste.
