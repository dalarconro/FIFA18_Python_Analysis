# Proyecto de Análisis de Datos con Python

## 📌 Descripción general

Este proyecto tiene como objetivo practicar un **flujo completo de análisis de datos** utilizando Python, con un enfoque orientado a un puesto de **Analista de Datos junior**.

El trabajo sigue un proceso típico de analítica y BI:

1. Carga de datos
2. Exploración inicial
3. Limpieza y transformación
4. Análisis y creación de métricas
5. Visualización básica
6. Exportación de resultados

El énfasis está en el uso de **Pandas**, buenas prácticas básicas y pensamiento de tipo *pipeline*, no en modelos de machine learning.

---

## 🧰 Tecnologías utilizadas

- Python 3
- Pandas
- NumPy
- Matplotlib / Seaborn
- Jupyter Notebook

---

## 📁 Estructura del proyecto

Insertar estructura del proyecto


---

## 🧠 Justificación de la estructura

Aunque en proyectos de datos más grandes es habitual separar completamente las fases de ETL en scripts independientes (`extract.py`, `transform.py`, `load.py`), en este caso se ha optado por un **enfoque híbrido**, más adecuado para un proyecto pequeño y de aprendizaje:

- Los **notebooks** permiten:
  - Seguir el proceso paso a paso de forma clara.
  - Facilitar la exploración y comprensión del dataset.
  - Visualizar resultados de forma inmediata.

- El módulo `src/transformations.py` contiene:
  - Funciones reutilizables de limpieza y transformación.
  - Lógica separada del análisis exploratorio.
  - Código más cercano a un entorno de producción sin sobre-ingeniería.

Este enfoque busca un equilibrio entre **claridad**, **aprendizaje** y **buenas prácticas reales**.

---

## 🔍 Flujo de trabajo

### 1️⃣ Exploración (`01_exploration.ipynb`)
- Carga del dataset original.
- Inspección de estructura, tipos y valores.
- Detección de problemas de calidad de datos.

### 2️⃣ Limpieza y transformación (`02_cleaning.ipynb`)
- Tratamiento de valores nulos y duplicados.
- Conversión de tipos (fechas, numéricos, categóricos).
- Uso de funciones definidas en `src/transformations.py`.

### 3️⃣ Análisis (`03_analysis.ipynb`)
- Creación de métricas clave mediante `groupby` y agregaciones.
- Tablas resumen y pivotes.
- Visualizaciones básicas.
- Exportación de resultados finales.

---

## 📊 Resultados

Los resultados del análisis se encuentran en:
- `outputs/reports/`: tablas finales en formato CSV.
- `outputs/figures/`: gráficos generados durante el análisis.

---

## 🚀 Posibles mejoras futuras

- Automatizar el pipeline en scripts ejecutables.
- Añadir validaciones de datos.
- Conectar el flujo a una base de datos (SQLite / PostgreSQL).
- Incorporar tests básicos para funciones de transformación.

---

## 👤 Autor

Proyecto realizado como ejercicio práctico de aprendizaje en análisis de datos con Python.
