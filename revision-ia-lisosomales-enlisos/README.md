# Inteligencia artificial en las enfermedades de depósito lisosomal (revisión para en-LISOS)

**Título:** *Inteligencia artificial en las enfermedades de depósito lisosomal: qué está demostrado, qué es prometedor y qué falta para llegar a la práctica clínica.*

**Estado:** manuscrito completo, listo para que los autores lo revisen, rellenen la primera parte (autores, filiaciones, financiación y conflictos de intereses) y lo envíen.

## Para enviar a la revista
| Archivo | Contenido |
|---|---|
| [`manuscrito/Manuscrito_IA_enfermedades_lisosomales_enLISOS.docx`](manuscrito/Manuscrito_IA_enfermedades_lisosomales_enLISOS.docx) | Manuscrito en Word con el formato de la revista: Arial 11, doble espacio, cada sección en página nueva y tres partes. Texto: 2.495 palabras. Resumen: 227. Abstract: 200. 99 referencias, 2 tablas y 2 figuras |
| `manuscrito/figuras/Figura_1.pdf` y `.jpg` | Cómo aprende y cómo se valida un modelo, con el sobreajuste |
| `manuscrito/figuras/Figura_2.pdf` y `.jpg` | La IA en el recorrido del paciente, por niveles de evidencia |
| `manuscrito/Manuscrito_IA_enfermedades_lisosomales_enLISOS.pdf` | Vista previa del Word en PDF (no es para enviar) |

## Para los autores
| Archivo | Contenido |
|---|---|
| [`Informe_revision_mapa_y_critica.docx`](Informe_revision_mapa_y_critica.docx) (también en [`informe.md`](informe.md)) | Mapa ampliado (59 estudios), discrepancias entre resumen y texto completo, barreras, índice y palabras, figuras y tablas, qué entra y qué queda fuera, y crítica como revisor externo con los problemas pendientes |
| [`Fase1_Fase2_mapa_y_propuesta.docx`](Fase1_Fase2_mapa_y_propuesta.docx) | Primer mapa de evidencia y propuesta editorial (primera ronda) |
| `manuscrito/referencias.txt` | Las 99 referencias en formato Vancouver/ICMJE |
| `fase1_mapa_evidencia/` y `fase2b_mapa_ampliado/` | Salida de los documentalistas (JSON) y verificación contra PubMed de cada registro |
| `herramientas/` | Búsqueda (`pm.py`), verificación, selección de estudios, generación del Word (`build_ms.py`, con el texto en `ms_content.py`) y de las figuras (`fig1.py`, `fig2.py`, `svg2out.js`) |
| `revista/` | Instrucciones oficiales para autores (nº 10, p. 35), encargo original e instrucciones de continuación |

## Límites
- La búsqueda es del 16 de noviembre de 2026 y solo usa PubMed, Europe PMC y ClinicalTrials.gov. No se consultaron Embase, Scopus, Web of Science ni Google Scholar.
- Cada referencia se verificó automáticamente contra PubMed: existe, coincide en título, primer autor y año, no está retractada y tiene una cita literal localizada en el resumen o en el texto completo.
- Las cifras del manuscrito se comprobaron en los textos completos abiertos cuando existían. Un estudio de la tabla 1 solo pudo leerse en resumen y lleva asterisco.
- El trabajo se ha hecho con un asistente de IA. Los autores deben revisar el contenido y declarar ese uso; la primera parte del Word incluye un texto propuesto.
- Los scripts de `herramientas/` se escribieron para la carpeta de trabajo original y esperan los datos en `out/` y `out2/`. Para ejecutarlos de nuevo hay que copiar ahí los JSON de las carpetas de datos.
