# ¿Adoró Mahoma ídolos antes de la revelación? Al-Tabari y otras fuentes suníes

- [`Mahoma_idolos_antes_de_la_revelacion.pdf`](Mahoma_idolos_antes_de_la_revelacion.pdf): informe de conclusiones (9 páginas), con el texto árabe, la traducción, la referencia y la valoración de cada pasaje.
- `informe.html`: fuente del PDF. Para regenerarlo: `python3 herramientas/build_pdf.py .` y después `node herramientas/topdf.js informe_build.html salida.pdf`. Hacen falta las fuentes Amiri y Lora (Google Fonts, licencia OFL) en una carpeta `fonts/`.
- `datos_investigadores/`: los hallazgos de los tres documentalistas en JSON. T1 trata a al-Tabari; T2, las colecciones de hadiz; T3, la sira, Ibn al-Kalbi y los eruditos. Cada hallazgo lleva la cita árabe literal, la URL y la traducción.
- `herramientas/BRIEF.md`: las instrucciones comunes que recibieron.

**Límites.** No se leyó el estudio de Kister «A bag of meat» (1970). Las versiones de Ahmad, al-Nasa'i, Abu Ya'la y al-Bazzar se conocen solo por las citas de Ibn Hajar y al-Dhahabi. No se usaron sunnah.com, dorar.net ni el buscador de la Shamela, porque muestran controles anti-bots.
