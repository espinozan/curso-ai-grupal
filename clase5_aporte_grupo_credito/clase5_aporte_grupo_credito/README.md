# Aporte individual – Clase 5: análisis exploratorio de crédito

Este proyecto contiene mi parte del trabajo grupal de la Clase 5. La idea es analizar de forma simple y reproducible **cómo se distribuye la morosidad entre los productos registrados** en `dataset_credito.csv`.

No buscamos demostrar que un producto cause morosidad. Primero describimos lo que muestran los datos, verificamos los cálculos y dejamos claros los límites.

## Pregunta de análisis

> ¿Cómo se distribuye la morosidad entre los distintos productos registrados?

## Qué hice con los datos

- Cargué el CSV sin modificar el archivo original.
- Revisé tamaño, tipos de datos, valores faltantes y duplicados.
- No eliminé filas ni imputé faltantes porque en esta etapa no tenemos una justificación suficiente para hacerlo.
- Calculé la cantidad de casos, cantidad de morosos y proporción de morosos por `PRODUCTO`.
- Comparé siempre **cantidad de casos** y **porcentaje dentro de cada producto**, para no confundir volumen con tasa.
- Generé un gráfico de la proporción de morosidad por producto.
- Dejé señalados algunos valores que conviene investigar (por ejemplo, edades fuera de lo esperable), pero no los corregí automáticamente.

## ¿Se limpió el dataset?

**No se hizo una limpieza destructiva.** La limpieza fue principalmente de revisión y validación.

El archivo original tiene:

- 1.190 registros.
- 26 columnas.
- 0 duplicados exactos.
- 138 faltantes en `relacion_dependencia`.
- 1 faltante en `Cantidad_consultas_7_dias`.

Los faltantes se conservan como faltantes. No se convierten en cero porque un dato faltante no significa necesariamente que el valor sea cero.

## ¿Se normalizaron los datos?

**No.** Para este análisis exploratorio y descriptivo no necesitamos normalizar ni escalar las variables numéricas. La normalización es más relevante cuando después se quiere entrenar ciertos modelos o comparar variables en una misma escala.

En este trabajo nos interesa conservar los valores en su escala original para poder interpretarlos y comunicarlos con facilidad.

Tampoco se codificó `PRODUCTO` ni `PROVINCIA` porque acá estamos haciendo análisis descriptivo, no entrenamiento de un modelo.

## Resultado principal

La morosidad general del dataset es de aproximadamente **22,6%**.

Entre los productos aparecen diferencias importantes. Por ejemplo, `DS_BASICO` tiene una proporción de morosidad mucho mayor que `DS_REFINANCIACION`. Pero esa diferencia es **descriptiva**: con este análisis solo no podemos afirmar que el producto sea la causa.

Además, hay productos con pocos registros, por lo que sus porcentajes requieren más cautela.

## Cómo ejecutarlo

### Opción A: usar la estructura de la clase

Si el proyecto está dentro de `modulo_5/`, el código busca por defecto:

```text
../modulo_3/dataset_credito.csv
```

Ejemplo:

```bash
python src/analisis_credito.py
```

### Opción B: indicar la ruta manualmente

```bash
python src/analisis_credito.py --csv /ruta/al/dataset_credito.csv
```

También se puede colocar el archivo en `data/dataset_credito.csv`.

## Dependencias

```bash
pip install -r requirements.txt
```

## Archivos

- `src/analisis_credito.py`: análisis reproducible en Python.
- `notebooks/01_eda_morosidad_producto.ipynb`: versión para abrir en Jupyter.
- `docs/aporte_para_el_grupo.md`: explicación corta para compartir con los compañeros.
- `resultados/morosidad_por_producto.csv`: resultado agregado sin datos individuales.
- `resultados/grafico_morosidad_producto.png`: gráfico del análisis.
- `data/README.md`: dónde colocar el CSV original.

## Qué llevaría yo a la reunión del grupo

> Analicé la morosidad por producto. No modifiqué ni normalicé los datos porque primero estamos haciendo exploración y necesitamos conservar la escala original. Revisé calidad, encontré faltantes pero no los imputé, y comprobé cantidad y proporción de morosos por producto. Mi propuesta es usar esta comparación como uno de nuestros hallazgos y después investigar si la diferencia se mantiene al considerar otras variables.
