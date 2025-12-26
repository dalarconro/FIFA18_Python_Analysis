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


# 5. 📋 Market Inflation: Positional Value & Scarcity Analysis

## Introduction
To conclude our strategic assessment, we shift our focus to the economic structure of the football market. Recruitment is not only about finding talent but also about understanding where capital is most efficiently deployed. This analysis explores **Positional Inflation**: the phenomenon where certain areas of the pitch command a premium price regardless of player quality. By utilizing our `club_filtering` utility, we segment the global market into competitive tiers (Elite, Top-Tier, and Mid-Market). This allows us to identify 'Scarcity Zones'—positions where talent is exceptionally expensive—and 'Value Pockets'—positions where high-quality reinforcements can be acquired at a fraction of the cost. Understanding these dynamics is the final step in building a sustainable and financially responsible recruitment strategy.

---

## Executive Summary: Positional Market Dynamics

### 1. Market Segmentation & Concentration
The market is heavily top-heavy, with the **Elite (75+)** tier commanding release clauses nearly **8.5 times higher** than the Mid-High segment. While the **Development (<65)** tier serves as a high-volume talent pool, capital concentration in the Elite tier creates a high-barrier entry for clubs attempting to break into the top competitive bracket.

### 2. The "Attacker Tax" & Scarcity Premium
Our analysis confirms that goal-scoring talent is the most inflated commodity in football:
* **Acquisition Inflation:** In the Elite tier, clubs pay **€0.58M per Overall point** for attackers, a **69.13% premium** over defenders.
* **Maintenance Burden:** The "Status Premium" is evident in wages, where elite attackers earn **1.20K per point**, significantly outstripping the salary growth of goalkeepers and defenders.
* **Early Speculation:** Surprisingly, the highest acquisition premium relative to quality (**81.37%**) is found in the **Development** tier, indicating that clubs aggressively overprice young attacking prospects based on potential rather than current output.

### 3. Strategic "Value Pockets"
The **Mid-High (65-75)** tier represents the most rational and efficient segment of the market. With an attacking premium of only **32.03%**—the lowest across all tiers—this segment offers the best opportunity for clubs to upgrade their squads without facing the exponential "superstar tax" of the Elite tier or the speculative volatility of the Development tier.

### 4. Strategic Recommendations
* **For Buyer Clubs:** Focus investment on the **Mid-High** tier for attacking roles to maximize "Quality per Euro".
* **For Seller Clubs:** Target the **Elite** market when offloading attackers, as the price-to-quality ratio scales most aggressively in that segment.
* **Budget Allocation:** Prioritize high-spending for **ATT** and **MDF** roles while seeking "Efficient Stability" in **DEF** and **GK** positions, where quality can be acquired at nearly half the cost per point.

---

## Visual Data Analysis

### Absolute Market Heat: Average Release Clause by Tier & Position
"This first visualization maps the absolute costs across market tiers. It highlights where the largest financial investments are concentrated and confirms the exponential price jump as we move from development leagues to the elite footballing world. It serves as a 'Heat Map' for where the most capital is required to compete."

**Conclusion:** The absolute market value distribution confirms a massive financial 'jump' between tiers. In the **Elite (75+)** segment, attackers (ATT) command an average release clause of **€44.7M**, which is more than **8.5 times** the cost of an attacker in the **Mid-High (65-75)** tier (€5.2M). This highlights that while the Mid-High market is relatively accessible, competing for elite talent requires an exponential increase in capital.

### The Efficiency Map: Cost per Quality Point (M EUR)
"Beyond absolute prices, we need to understand value. This chart displays the 'Acquisition Cost per Overall Point', revealing how much a club pays for each unit of performance. This is the definitive tool for identifying 'Positional Inflation'—showing exactly where the market is overpaying for quality and where the most efficient impact signings are hidden."

**Conclusion:** This chart reveals the true 'Positional Inflation' by neutralizing the player's quality (Overall). It illustrates that in the **Elite** tier, a club pays **€0.58M per point of Overall** for an attacker, nearly **double** what they pay for a goalkeeper (€0.29M). Interestingly, the **Development (<65)** tier also shows a significant efficiency gap, suggesting that the market aggressively overprices goal-scoring potential even at lower levels.

### The Status Premium: Wage Cost per Quality Point (K EUR)
"Finally, we analyze the 'Wage Cost per Overall Point'. This provides a view of the recurring financial burden (salaries) relative to player quality. It helps identify if certain positions command a higher 'Status Premium' in their weekly paychecks compared to their defensive counterparts, which is critical for long-term financial sustainability."

**Conclusion:** The wage analysis demonstrates that elite attackers do not just cost more to buy; they are significantly more expensive to maintain. In the **Elite** tier, attackers earn **1.20K per point of Overall**, a 'Status Premium' that sits **41% higher** than defenders (0.85K). For a club's long-term sustainability, the most significant 'wage bill' risk lies in the attacking frontline.
