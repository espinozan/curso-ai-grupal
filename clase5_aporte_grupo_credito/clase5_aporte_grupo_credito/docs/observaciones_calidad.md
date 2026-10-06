# Observaciones de calidad detectadas

Esta revisión se hizo sobre el CSV entregado para la Clase 5.

| Control | Resultado | Qué hacemos |
|---|---:|---|
| Filas | 1.190 | Se conservan |
| Columnas | 26 | Se conservan |
| Duplicados exactos | 0 | No hay que eliminar por este criterio |
| `relacion_dependencia` faltantes | 138 | Se dejan como faltantes |
| `Cantidad_consultas_7_dias` faltantes | 1 | Se deja como faltante |
| `edad` menor a 18 o mayor a 100 | 1 caso potencial | Se revisa, no se elimina automáticamente |
| `BCRA_Peor_Situacion` negativa | 119 casos | Se registra para investigar significado del código |
| `Nivel_Socioeconomico` negativo | 1 caso | Se registra para investigar significado del código |

## Por qué no corregimos automáticamente

Todavía no conocemos con suficiente precisión el diccionario de datos. Un valor especial o negativo puede ser un código válido y un valor extremo puede ser un caso real. Cambiarlo sin confirmar su significado puede introducir un problema nuevo y hacer menos trazable el análisis.
