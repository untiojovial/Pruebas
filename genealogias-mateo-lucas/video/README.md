# Vídeo TikTok: «¿José tenía dos padres?»

`genealogias_tiktok.mp4`: 8 min 58 s, vertical 1080×1920, 24 fps, H.264 + AAC, audio normalizado a unos −14 LUFS.

- **Contenido:** 18 escenas con monigotes que resumen el estudio de las genealogías (`../genealogias_mateo_lucas.html`).
- **Voces sintéticas de Microsoft Edge (edge-tts):** narrador es-ES Álvaro, escéptico es-MX Jorge, Padres citados es-CO Gonzalo.
- **Subtítulos:** quemados en el vídeo y sincronizados por palabra; la palabra que se pronuncia sale en color.
- **Recortes de página:** Eusebio (Loeb), Ireneo (Harvey), Westcott-Hort y Strauss.

Herramientas en `herramientas/`:
- `script.py`: guion.
- `tts.py`: voz.
- `engine.py`: monigotes y tarjetas.
- `render.py`: escenas, subtítulos, mezcla y codificación.

Para regenerarlo: `python3 tts.py && python3 render.py`. Necesita las fuentes Baloo 2, Patrick Hand y Gentium Book Plus en `fonts/`, y las imágenes de `../paginas/` copiadas en `pg/`.
