# Encargo común (léelo entero)

Eres documentalista científico. Ayudas a construir el MAPA DE EVIDENCIA de una revisión para la revista española en-LISOS:
«Aplicaciones de la inteligencia artificial (IA) en las enfermedades de depósito lisosomal (LSD)» (Gaucher, Fabry, Pompe y otras).

## Herramienta (única vía de búsqueda permitida)
Ejecuta con Bash, desde cualquier directorio:
  python3 /tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/rev/pm.py search '<consulta PubMed>' 60
  python3 .../rev/pm.py fetch <PMID> <PMID> ...        (registro completo con resumen)
  python3 .../rev/pm.py epmc '<consulta>' 25             (Europe PMC; añade  AND SRC:PPR  para preprints)
  python3 .../rev/pm.py ctgov '<consulta>' 20            (ClinicalTrials.gov)
La herramienta ya gestiona el ritmo y la caché. NO uses otras webs salvo que tu encargo lo diga expresamente.

## Reglas inviolables
1. NO INVENTES NADA: ni estudios, ni autores, ni cifras, ni PMID, ni DOI. Solo cuenta lo que hayas leído en la salida de la herramienta.
2. Cada dato (tamaño de muestra, AUC, sensibilidad…) debe estar en el resumen que has leído. Si el resumen no lo da, escribe "NO CONSTA EN EL RESUMEN".
3. Para cada estudio copia una CITA LITERAL en inglés del resumen (1-2 frases) que respalde el resultado principal: campo `cita_literal`.
4. Lee el resumen (fetch) de TODO estudio que incluyas. No clasifiques por el título.
5. Descarta lo que no sea IA/aprendizaje automático de verdad (p. ej. estadística clásica sin modelo predictivo) y lo que no trate de tu ámbito. Apunta los descartes dudosos en `descartes` con el motivo.
6. No abras subagentes. No escribas fuera del archivo de salida que se te indica.

## Formato de salida: un archivo JSON (UTF-8) con esta forma
{
 "ambito": "...",
 "consultas": ["consulta 1 (TOTAL n)", "..."],
 "estudios": [ {
   "pmid": "…", "doi": "…", "primer_autor": "Apellido Iniciales", "anio": "…", "revista": "…", "titulo": "…",
   "tipo_publicacion": "original revisado por pares | revisión | revisión sistemática | preprint | registro de ensayo | editorial/opinión",
   "enfermedad": "…",
   "nivel_evidencia": "directa LSD | otra enfermedad rara | población general/extrapolación",
   "area": "4.1 diagnóstico/retraso/HCE-NLP | 4.2 genética/variantes | 4.3 biomarcadores/ómicas | 4.4 imagen | 4.5 pronóstico/estratificación | 4.6 tratamiento | 4.7 IA generativa/LLM | 4.8 investigación clínica/fármacos",
   "objetivo": "…", "algoritmo": "…", "muestra_y_datos": "…", "variables": "…",
   "resultados_metricas": "…", "validacion": "interna | externa | multicéntrica | prospectiva | NO CONSTA EN EL RESUMEN",
   "limitaciones": "…(las que diga el resumen o sean evidentes por el diseño; indica cuál es cuál)",
   "aplicabilidad": "investigación | prototipo validado | uso clínico",
   "cita_literal": "…",
   "relevancia": "alta | media | baja"
 } ],
 "descartes": [ {"pmid": "…", "motivo": "…"} ],
 "lagunas": ["áreas sin evidencia encontrada, con la consulta que lo demuestra"],
 "notas": "problemas, dudas, cosas que conviene comprobar a mano"
}
Escribe el JSON con Python (json.dump, ensure_ascii=False, indent=1) para que sea válido. Al terminar, valida que carga con json.load e informa en tu respuesta final: nº de estudios, las 5 más importantes (PMID + una línea) y las lagunas.
