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



## 📋 Executive Scouting Summary & Action Plan

### 1. Methodology Overview
This analysis processed a global database of over 18,000 players to identify high-yield investment opportunities. By applying a **multi-dimensional scoring system**, we filtered the talent pool based on four critical pillars:
* **Value Efficiency:** Identifying high potential at a low market cost.
* **Wage-to-Performance:** Optimizing the salary-to-output ratio.
* **Growth Margin:** Prioritizing young players with the highest development ceiling.
* **Negotiation Urgency:** Leveraging favorable contract situations (expiring within 24 months).

### 2. Strategic Insights
* **The "Value Zone":** The most efficient market segment is found in players with a Release Clause below **€10M**. In this range, the correlation between price and future quality is weakest, offering the highest ROI.
* **Market Anomalies:** Countries like **Spain and Germany** act as "Premium Markets" where mandatory high release clauses penalize players in efficiency rankings. Conversely, **Italy and France** are currently the top exporters of accessible 'Elite' talent.
* **Volume vs. Quality:** While **England** leads the market in sheer volume of professional prospects, the density of **Elite-tier talent** is significantly higher in Southern European and specific South American markets.

### 3. Top Investment Recommendations
Based on the **Final Scouting Score**, the following targets should be prioritized for immediate recruitment:
1.  **Elite Target:** **T. Kubo** — Represents the most statistically sound 'Elite' investment globally.
2.  **Strategic Asset:** **A. Bastoni** — High-caliber defensive prospect with an optimized market valuation.
3.  **High-Efficiency Gem:** **A. Kuruniyan** — Leader of the 'Top Class' tier with exceptional value-for-money metrics.

### 4. Recommended Action Plan
* **Immediate Action:** Initiate contact with the Top 5 ranked players in the **Elite and Top Class** tiers before their market value escalates due to professional growth.
* **Resource Allocation:** Direct physical scouting missions to **Italy and France** to monitor the high-density elite clusters identified.
* **Financial Strategy:** Focus acquisition budgets on undervalued release clauses (under €15M) to maximize the probability of future capital gains.
