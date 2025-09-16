# COVID-19 Data Analysis (Data Science Part)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12,6)

# -------------------------
# 1. Load Dataset
# -------------------------
df = pd.read_csv("data/owid-covid-data.csv")

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Remove global aggregate
df = df[df['location'] != 'World']

# Drop irrelevant columns
columns_to_drop = ['iso_code', 'continent', 'tests_units']
df = df.drop(columns=columns_to_drop, errors='ignore')

# -------------------------
# 2. Global Trends
# -------------------------
global_df = df.groupby('date')[['new_cases', 'new_deaths']].sum().reset_index()

plt.plot(global_df['date'], global_df['new_cases'], label='New Cases')
plt.plot(global_df['date'], global_df['new_deaths'], label='New Deaths')
plt.title("Global COVID-19 New Cases & Deaths")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.show()

# -------------------------
# 3. Top 10 Countries by Total Cases
# -------------------------
latest_df = df[df['date'] == df['date'].max()]
top_countries = latest_df.nlargest(10, 'total_cases')[['location','total_cases']]

sns.barplot(x='total_cases', y='location', data=top_countries, palette='Reds_r')
plt.title("Top 10 Countries by Total COVID-19 Cases")
plt.show()

# -------------------------
# 4. Vaccination Analysis
# -------------------------
if 'people_vaccinated' in df.columns:
    top_vaccinated = latest_df.nlargest(10, 'people_vaccinated')[['location','people_vaccinated']]
    sns.barplot(x='people_vaccinated', y='location', data=top_vaccinated, palette='Blues_r')
    plt.title("Top 10 Countries by People Vaccinated")
    plt.show()

# -------------------------
# 5. Correlation Heatmap
# -------------------------
numeric_cols = [col for col in ['total_cases','new_cases','total_deaths','new_deaths','total_vaccinations','people_vaccinated'] if col in df.columns]

sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation between COVID-19 Metrics")
plt.show()
