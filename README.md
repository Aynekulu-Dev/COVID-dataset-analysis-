# COVID-19 Dataset Analysis (Data Science Part)

## Project Overview
This project performs a **comprehensive analysis of the global COVID-19 pandemic** using publicly available datasets.  
It focuses on **Data Science** tasks only (no Machine Learning yet).  
The goal is to **clean, explore, and visualize** the data to gain meaningful insights about the pandemic's trends worldwide.

- **Dataset File:** `data/owid-covid-data.csv`
- **Source:** [Our World in Data](https://ourworldindata.org/covid-data)
- **Scope (This Week):** Exploratory Data Analysis (EDA) and visualization.
- **Key Columns:**
  - `date` — Date of record
  - `location` — Country name
  - `total_cases`, `new_cases` — Total and daily new confirmed cases
  - `total_deaths`, `new_deaths` — Total and daily new deaths
  - `total_vaccinations`, `people_vaccinated` — Vaccination metrics

---

## Tools & Libraries
- **Python 3** — Programming language
- **pandas** — Data manipulation
- **numpy** — Numerical operations
- **matplotlib** — Static plotting
- **seaborn** — Statistical visualizations
- **plotly** — Interactive visualizations (optional for future use)

---

## Methodology

### 1. Data Cleaning
Before analysis, we clean the dataset to make it usable:
- Remove irrelevant columns such as `iso_code`, `continent`, `tests_units`.
- Remove aggregate rows like `World` to focus on individual countries.
- Convert the `date` column to `datetime` format.
- Handle missing values (if any) by skipping or filtering.

### 2. Exploratory Data Analysis (EDA)
We analyze the dataset from multiple perspectives:

1. **Global Trends**
   - Visualize total **new cases** and **new deaths** over time worldwide.
   - Identify peaks, waves, and overall progression of the pandemic.

2. **Top 10 Countries by Total Cases**
   - Determine which countries were most affected.
   - Use bar charts for easy comparison of total cases per country.

3. **Vaccination Analysis**
   - Examine vaccination progress in top 10 countries by number of people vaccinated.
   - Understand how vaccination rollout differs among countries.

4. **Correlation Analysis**
   - Examine relationships between COVID-19 metrics (`total_cases`, `new_cases`, `total_deaths`, `new_deaths`, `total_vaccinations`, `people_vaccinated`) using a correlation heatmap.
   - Identify strong and weak correlations to understand the dataset structure.

---

## Output Graphs

### 1. Global Trends of COVID-19
Shows worldwide **new cases** and **new deaths** over time.

![Global Trends](plots/global_trends.png)

**Insights:**
- Peaks correspond to waves in the pandemic.
- Deaths generally lag behind cases.

---

### 2. Top 10 Countries by Total Cases
Bar chart of countries with the **highest cumulative cases**.

![Top 10 Cases](plots/top10_cases.png)

**Insights:**
- Identify the most affected countries.
- Compare the scale of impact globally.

---

### 3. Vaccination Progress
Bar chart showing **people vaccinated** in top 10 countries.

![Top 10 Vaccinated](plots/top10_vaccinated.png)

**Insights:**
- Provides perspective on vaccination rollout.
- Highlights countries leading in vaccination coverage.

---

### 4. Correlation Heatmap
Shows correlations between **COVID-19 metrics**.

![Correlation Heatmap](plots/correlation_heatmap.png)

**Insights:**
- Strong correlation between total and new cases.
- Helps identify relationships useful for future predictive modeling.

---

## How to Run

1. Activate your virtual environment:

```bash
source .venv/bin/activate
