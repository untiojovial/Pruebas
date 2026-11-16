# Inteligencia artificial en las enfermedades de depósito lisosomal (revisión para en-LISOS)

Estado: **Fase 1 (mapa de evidencia) y Fase 2 (propuesta editorial) terminadas. Pendiente de validación.** El manuscrito (Fases 3 a 5) no se ha redactado todavía, como pedía el encargo.

| Archivo | Contenido |
|---|---|
| [`Fase1_Fase2_mapa_y_propuesta.docx`](Fase1_Fase2_mapa_y_propuesta.docx) | Documento principal: método, mapa, estudios nucleares, evidencia transferible, marcos, lagunas, avisos de calidad, propuesta editorial y decisiones por validar |
| [`fase1_fase2_mapa_y_propuesta.md`](fase1_fase2_mapa_y_propuesta.md) | Lo mismo en Markdown |
| [`fase1_mapa_evidencia/todos_los_registros.csv`](fase1_mapa_evidencia/todos_los_registros.csv) | Los 190 registros recogidos, con la cita literal del resumen y el estado de verificación |
| `fase1_mapa_evidencia/datos_investigadores/` | Salida de cada documentalista (JSON) y `verificado.json` (cada registro cotejado con PubMed) |
| `herramientas/` | `pm.py` (búsqueda), `verify.py` (verificación), `core.py` (selección y grados), `build12.py` (genera el documento), `BRIEF.md` (instrucciones a los documentalistas) |
| `revista/` | Instrucciones oficiales para autores (nº 10, p. 35) y el texto del encargo |

## Límites
- Búsqueda del 16 de noviembre de 2026 en PubMed, Europe PMC (preprints) y ClinicalTrials.gov. **No se consultaron** Embase, Scopus, Web of Science, Cochrane ni Google Scholar (sin acceso).
- Los datos proceden de los resúmenes, no de los textos completos.
- Los 146 PMID existen en PubMed y coinciden en título, primer autor y año. Los grados A a D son una valoración provisional.
- Los 28 preprints y registros de ensayos no se han cotejado uno a uno más allá de lo que anotó el documentalista.
