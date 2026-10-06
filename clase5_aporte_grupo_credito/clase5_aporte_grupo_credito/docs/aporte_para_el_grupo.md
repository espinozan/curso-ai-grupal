# Aporte para el grupo

## Pregunta

**¿Cómo se distribuye la morosidad entre los distintos productos registrados?**

## Qué revisé

Primero miré la estructura general del archivo y la calidad de los datos. Hay 1.190 registros y 26 columnas. No hay duplicados exactos.

También encontré 138 faltantes en `relacion_dependencia` y 1 faltante en `Cantidad_consultas_7_dias`. Los dejé como faltantes porque no tenemos información suficiente para reemplazarlos correctamente.

## Limpieza y normalización

No hice una limpieza que borre o cambie registros. La idea en esta etapa es conservar el dato original y documentar los problemas antes de tomar decisiones.

Tampoco normalicé ni escalé variables. Para un análisis descriptivo esto no es necesario y, de hecho, mantener la escala original ayuda a interpretar los resultados.

## Resultado

La morosidad general es de aproximadamente 22,6%.

La proporción de morosos cambia según el producto. La diferencia es suficientemente grande como para que valga la pena investigarla, pero no alcanza para decir que el producto cause la morosidad.

## Limitaciones

- Algunos productos tienen pocos casos.
- No conocemos, a partir del CSV solamente, el origen exacto, período, unidad monetaria o contexto de captura de todas las variables.
- Un porcentaje alto no implica causalidad.
- Hay valores que conviene investigar antes de cualquier modelo, por ejemplo edades muy altas o códigos con valores especiales.

## Para la Clase 6

Una pregunta útil para continuar sería:

> **¿La diferencia de morosidad entre productos se mantiene cuando también consideramos variables como ingresos, edad, nivel socioeconómico, deuda y días de atraso?**
