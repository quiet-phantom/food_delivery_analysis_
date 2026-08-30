# Food Delivery Dataset Analysis & Data Cleaning


## Overview
This repository contains data cleaning, preprocessing, exploratory analysis, and visualization for the Food Delivery Dataset (38,964 total records).

## Data Cleaning & Preprocessing Decisions

### 1. Duplicate Records
- **Detection**: Analyzed all 38,964 rows across 22 columns using `df.duplicated().sum()`.
- **Finding**: 0 duplicate rows were found.
- **Decision**: No duplicate rows needed to be dropped; all original entries were unique and retained.

### 2. Missing Values Imputation
- **`Delivery_person_Age`** (1,019 missing values): 
  - **Decision**: Imputed using the **median** age. Median was selected to prevent distortion from potential extreme value outliers.
- **`Delivery_person_Ratings`** (1,055 missing values): 
  - **Decision**: Imputed using the **mean** rating score. This maintains sample size without skewing overall performance trends.
- **`Time_Orderd`** (835 missing values): 
  - **Decision**: Imputed using **backward fill (`bfill`)** to maintain time-sequence consistency.

### 3. Data Type Formatting
- **`Delivery_person_Age`**: Converted to integer (`int64`) post-imputation for accurate representation.
- **`Delivery_person_Ratings`**: Rounded to 2 decimal places to match standard scales.
- **`Time_taken (min)`**: Extracted numeric integer values to perform mathematical aggregations and correlation analysis.

## Key Insights Summary
- **Traffic Impact**: Higher traffic density directly correlates with an increase in average delivery time.
- **Condition Analysis**: Weather and traffic density combined play the most critical role in delivery delays.

  ## Basic Dataset Metrics

- **Total Deliveries**: 38,964
- **Delivery Time**:
  - **Average**: ~26.29 mins
  - **Minimum**: 10 mins
  - **Maximum**: 54 mins
- **Distance & Speed**:
  - **Average Distance**: ~15.84 km
  - **Average Speed**: ~33.20 km/h
- **Delivery Person Demographics**:
  - **Average Rating**: 4.63 / 5.0
  - **Average Age**: 29.6 years

---

## Competition Analysis & Findings

### Q1 – Traffic Impact
**Question:** Which road traffic condition has the highest average delivery time?

**Answer & Data Breakdown:**
- **Jam** traffic density has the highest average delivery time (**31.44 minutes**).
- **Data Breakdown:**
  - **Jam**: 31.44 mins
  - **High**: 27.41 mins
  - **Medium**: 26.93 mins
  - **Low**: 21.50 mins
- **Conclusion:** Heavy traffic congestion adds nearly 10 extra minutes per delivery compared to low traffic conditions.

---

### Q2 – Distance Impact
**Question:** How does delivery distance affect delivery time? Support your conclusion with data.

**Answer & Data Breakdown:**
- **Correlation:** There is a positive correlation (**r = 0.32**) between delivery distance and time taken.
- **Data Breakdown:**
  - **0–5 km**: 22.42 mins
  - **5–10 km**: 24.64 mins
  - **10–15 km**: 30.09 mins
  - **15–20 km**: 30.07 mins
  - **20+ km**: 30.08 mins
- **Conclusion:** Short-distance orders (under 5 km) are fulfilled fastest (~22 mins), while distances beyond 10 km consistently average around 30 minutes.

- ---

### Q3 – Combined Conditions Impact
**Question:** Which combination of weather condition and traffic density has the highest average delivery time?

**Answer & Data Breakdown:**
- **Fog** weather combined with **Jam** traffic density has the highest average delivery time (**36.89 minutes**).
- **Top 5 Worst Weather & Traffic Combinations:**
  - **Fog + Jam**: 36.89 mins
  - **Cloudy + Jam**: 36.71 mins
  - **Windy + Jam**: 30.40 mins
  - **Sandstorms + Jam**: 30.25 mins
  - **Stormy + Jam**: 30.20 mins
- **Conclusion:** Traffic density (**Jam**) is the primary multiplier for delays, but when paired with low visibility conditions like **Fog** or **Cloudy** weather, delivery times reach their absolute maximum (~37 minutes).

- ### Visualizations

#### Chart 1: Average Delivery Time by Traffic Density

<img width="784" height="483" alt="download" src="https://github.com/user-attachments/assets/42977a9b-d126-4aab-bc2a-641fabbed5e9" />

**Key Observations:**
- **Jam / Congested Traffic** results in the highest average delivery time (**31.44 minutes**).
- Delivery times decrease progressively as traffic density eases: **High (27.41 mins)**, **Medium (26.93 mins)**, and **Low (21.50 mins)**.
- Severe traffic density adds an extra delay of nearly **10 minutes per order** compared to clear roads.

#### Chart 2: Delivery Distance vs. Delivery Time

<img width="884" height="584" alt="download (1)" src="https://github.com/user-attachments/assets/fb48bff8-5a8c-4a15-af80-c5f50b052495" />

**Key Observations:**
- There is a positive correlation between delivery distance and delivery time (as distance increases, delivery time tends to increase).
- However, the overall scatter distribution indicates that distance alone is not the sole factor in delays; external conditions like traffic density and weather heavily influence overall delivery duration.

  ---

## Business Insights & Strategic Recommendations

### Insight 1: Heavy Traffic is the Primary Bottleneck
- **Finding:** Delivery times surge to an average of **31.44 minutes** during high-traffic (Jam) conditions, compared to **21.50 minutes** during low-traffic periods—a delay increase of **~46%**.
- **Impact for Business:** Traffic congestion directly increases order fulfillment times, leading to customer dissatisfaction, higher churn, and increased operational fuel costs for fleet partners.
- **Actionable Strategy:** Implement dynamic ETA calculations during peak traffic hours, adjust customer expectations on the app, and offer batching/routing optimizations for drivers in dense zones.

---

### Insight 2: High Visibility Loss (Fog & Severe Weather) Magnifies Delays
- **Finding:** When severe traffic jams coincide with low visibility weather conditions (like Fog or Heavy Clouds), average delivery times reach their highest point at **~36.89 minutes**.
- **Impact for Business:** Bad weather combined with traffic congestion significantly raises delivery safety risks for drivers and creates severe logistics backlogs during peak ordering windows.
- **Actionable Strategy:** Introduce dynamic peak-surcharge fees during severe weather to incentivize driver availability, and expand delivery radius limits slightly to avoid bottlenecking specific route corridors.

---

### Insight 3: Distance Alone Does Not Dictate Delivery Duration
- **Finding:** The scatter analysis reveals a positive trend between distance and delivery time, but with significant variation across similar distances. Short-distance orders often experience long delivery times due to environmental delays.
- **Impact for Business:** Charging or predicting delivery times based strictly on distance ($km$) without factoring in real-time road conditions creates inaccurate ETAs and sub-optimal pricing models.
- **Actionable Strategy:** Shift from simple distance-based delivery fee structures to **time-estimated dynamic pricing** that accounts for traffic density and weather conditions simultaneously.

  ### AI-Generated Executive Summary
  Our analysis reveals that traffic congestion and environmental visibility—rather than geographic distance—are the primary drivers of delivery delays. Severe traffic jams create a major operational bottleneck, increasing average delivery times by **46.23%** (rising from 21.50 minutes in low traffic to 31.44 minutes). This bottleneck is significantly exacerbated by poor weather conditions; the combination of heavy fog and jam traffic represents our worst-performing operational scenario, pushing average delivery times to a peak of 36.89 minutes. While distance maintains a mild positive correlation with delivery duration, traffic density and visibility are the statistically dominant factors constraining fleet throughput.

These operational constraints directly threaten customer retention and increase fleet operating costs. The nearly 15-minute variance caused by traffic and weather severely compromises Estimated Time of Arrival (ETA) accuracy, leading to missed delivery windows and diminished customer satisfaction. Operationally, prolonged delivery cycles during high-density traffic hours reduce total driver utilization rates, increase vehicle idling and fuel expenses, and create compounding schedule delays across the entire fleet network during peak demand periods.

To optimize performance and mitigate these risk factors, we recommend three strategic initiatives. First, upgrade our dispatch technology to prioritize real-time traffic density and visibility metrics over simple distance-based routing. Second, introduce dynamic ETA forecasting that automatically adjusts promised delivery windows for customers during severe weather events like heavy fog. Finally, optimize fleet staging by pre-positioning drivers near high-demand clusters prior to peak traffic windows, thereby reducing exposure to high-density gridlock and stabilizing overall fulfillment times.

---

## Recommended Workflow

To ensure reproducibility, data integrity, and actionable business insights, this project follows an end-to-end analytical framework:

1. **Load**
   - Ingest raw dataset (`food_delivery_dataset.csv`) into Pandas DataFrames.
   - Perform initial structural inspection (`.info()`, `.head()`, `.shape`).

2. **Clean**
   - Handle missing values and duplicate entries.
   - Convert data types (e.g., categorical variables, temporal attributes, numeric distances).
   - Standardize column naming conventions for analytical consistency.

3. **Analyze**
   - Perform Exploratory Data Analysis (EDA) and numerical aggregations.
   - Evaluate relationships between key factors (e.g., Weather, Traffic Density, Delivery Distance vs. Delivery Time).

4. **Visualize**
   - Generate clear statistical plots using Seaborn and Matplotlib (Bar charts for traffic impact, Scatter plots with trendlines for distance correlation).
   - Apply professional design standards (consistent color palettes, custom opacity, clear titles/labels).

5. **Interpret**
   - Translate chart trends and statistical correlations into concrete empirical findings.
   - Evaluate operational bottlenecks and business pain points.

6. **Explain**
   - Integrate Google Gemini API (`gemini-3.6-flash`) to generate structured, executive-level summaries for non-technical stakeholders.
   - Document strategic recommendations in the repository README.
  
   - ---

## 5. Optional Bonus Features

To enhance the business usability and interactive analytical capabilities of this project, several bonus features have been implemented and structured for future expansion:

### Integrated & Planned Bonus Capabilities

* **Streamlit Interactive Dashboard:**  
  Designed a dynamic web application layout using Streamlit to allow users to interactively filter food delivery data by weather conditions, vehicle types, and traffic density in real time.

* **Advanced Visualizations & Interactive Charts:**  
  Expanded static Matplotlib/Seaborn visual output with interactive **Plotly** charts, enabling smooth hover details, zoom functionalities, and export capabilities.

* **Multi-Factor Comparisons:**  
  Engineered comparative filters to analyze performance metrics across different cities, vehicle modes (scooter, motorcycle, bicycle), and compound weather scenarios.

* **AI-Generated Strategic Recommendations:**  
  Automated executive insight generation by feeding aggregated Pandas metrics directly into the **Google Gemini 2.5 Flash API** to generate plain-language strategic business steps without ML overhead.

* **Exportable Reports & Charts:**  
  Added functionality to download high-resolution visual assets (`.png` at 300 DPI) and export analytical summaries for offline distribution and executive slide decks.
