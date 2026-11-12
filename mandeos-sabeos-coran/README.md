# El error coránico de los mandeos: ¿salvados o condenados?

Documental de 9 min 56 s en español, con dos versiones y miniaturas:

| Archivo | Formato |
|---|---|
| [`renders/mandeos_vertical.mp4`](renders/mandeos_vertical.mp4) | Vertical 1080×1920, para TikTok y Shorts |
| [`renders/mandeos_horizontal.mp4`](renders/mandeos_horizontal.mp4) | Horizontal 1920×1080, para YouTube |
| [`renders/miniatura_youtube_1280x720.jpg`](renders/miniatura_youtube_1280x720.jpg) | Miniatura de YouTube |
| [`renders/miniatura_tiktok_1080x1920.jpg`](renders/miniatura_tiktok_1080x1920.jpg) | Miniatura de TikTok |

## Documentos
- [`guion.md`](guion.md): guion completo, con la fuente que aparece en pantalla en cada frase.
- [`storyboard.md`](storyboard.md): un fotograma por plano (60 planos), con tiempo, narración y fuente.
- [`bibliografia.md`](bibliografia.md): referencias, enlaces y estado de cada una (verificado, solo resumen o no consultado).
- [`fuentes_audiovisuales.md`](fuentes_audiovisuales.md): origen y licencia de cada elemento visual y sonoro.
- [`investigacion.md`](investigacion.md): hechos, hipótesis e interpretaciones; lo que se concede; lo que no se pudo comprobar.

## Tesis y posición final
- **La promesa:** el Corán promete recompensa a los sabeos que crean en Dios y en el Último Día y obren el bien (2:62, 5:69).
- **La condena:** también condena a quien acepta a unos mensajeros y rechaza a otros (4:150-151).
- **El caso:** si los sabeos son los mandeos, que veneran a Juan el Bautista y rechazan a Jesús como Mesías, armonizar ambos textos exige una de estas salidas:
  - añadir una condición que no está escrita;
  - recurrir a la abrogación;
  - negar la identificación histórica.

**Posición final:** el caso mandeo es un desafío importante para la claridad y la coherencia de la soteriología coránica. El vídeo no oculta las respuestas musulmanas: presenta cinco y reconoce cuáles son coherentes.

## Estructura (11 capítulos)
1. El gancho
2. Quiénes son los mandeos
3. La promesa
4. ¿Sabeos = mandeos?
5. Los comentaristas
6. Juan sí, Jesús no
7. La condena
8. El dilema
9. Las respuestas
10. La investigación
11. El veredicto

## Dirección artística
- **Paleta:**
  - negro carbón (paneles y salas);
  - blanco marfil (texto);
  - dorado antiguo (claves, interfaz);
  - rojo oscuro (condena y tensiones);
  - azul profundo (promesa, mapas y río).
- **Figuras:** planas con cara (parpadeo, boca que se mueve al hablar) y sombreado en dos tonos. Las escenas recreadas llevan la etiqueta «ILUSTRACIÓN · RECREACIÓN».
- **Documentos:** recortes reales (quran.com, tafsir, Iranica, Gündüz, Kulinich, Mead, Lidzbarski, Ginza, Bujari) con la frase subrayada y zoom.
- **Afirmaciones académicas:** muestran el nombre del investigador, la obra y el año.
- **Argumento:** diagramas con premisas numeradas, las cuatro salidas con su coste y una balanza entre promesa y condena.
- **Panel inferior:**
  - subtítulo palabra a palabra, con las claves en dorado;
  - fuente en pantalla;
  - barra de capítulos con el progreso;
  - icono de ondas de agua.

  No lleva la cinta «||||» de los vídeos anteriores.
- **Versión horizontal:** escenario a la izquierda; a la derecha, columna con capítulo, barra de progreso, subtítulo grande y fuente.

## Tecnología
Pediste Remotion, React y TypeScript **o una alternativa equivalente si el entorno ya usa otra tecnología**. Este proyecto ya tenía su propia cadena en Python y la he mantenido:
- **Imagen:** PIL dibuja cada fotograma.
- **Voz:** edge-tts, con tiempos por palabra para sincronizar subtítulos y animaciones.
- **Montaje:** ffmpeg codifica en H.264 y AAC y normaliza el volumen a −14 LUFS.

No hay un proyecto de Remotion. Si lo quieres de verdad, habría que reescribir las escenas en React.

```
escenas/        render5.py (escenas, transiciones, vertical y horizontal) · guion_datos.py (guion con palabras clave)
componentes/    style2.py (figuras, fondos, panel) · paper.py y render3.py (motor base, tarjetas, audio) · script3.py (dependencia de render3)
assets/         paginas/ (27 recortes) · fonts/
audio/          tts5.py (voz) · audh/ y out/ se generan (ignorados por git)
fuentes/textos/ versículos (árabe y traducciones), tafsir e Iranica en texto
herramientas/   hl.py (subrayado en PDF) · webshot.js · webshot_local.js · thumbs.py (miniaturas)
renders/        vídeos y miniaturas
storyboard/     fotogramas del storyboard
```

### Cómo regenerarlo
Requisitos: Python 3 con Pillow, numpy y edge-tts; ffmpeg.
```bash
python3 audio/tts5.py                         # 1. voz y tiempos por palabra (audio/audh/)
python3 escenas/render5.py preview 0.85       # 2. hojas de vista previa (audio/out/)
python3 escenas/render5.py                    # 3. vídeo vertical  → renders/mandeos_vertical.mp4
HORIZ=1 python3 escenas/render5.py            # 4. vídeo horizontal → renders/mandeos_horizontal.mp4
HORIZ=1 python3 escenas/render5.py still 300  # fotograma suelto
```
El guion se cambia en `escenas/guion_datos.py`. Las palabras entre asteriscos (`*palabra*`) salen en dorado en los subtítulos y no se leen.
