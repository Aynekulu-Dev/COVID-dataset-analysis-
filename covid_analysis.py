# COVID-19 Data Analysis (Data Science Part)
# This script performs data cleaning, exploratory data analysis, and visualization
# Outputs are saved as images in the 'plots/' folder for README inclusion

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------------
# Setup
# -------------------------
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12,6)

# Create folder for plots if it doesn't exist
if not os.path.exists("plots"):
    os.makedirs("plots")

# -------------------------
# 1. Load Dataset
# -------------------------
df = pd.read_csv("data/owid-covid-data.csv")

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])

# Remove global aggregate
df = df[df['location'] != 'World']

# Drop irrelevant columns
columns_to_drop = ['iso_code', 'continent', 'tests_units']
df = df.drop(columns=columns_to_drop, errors='ignore')

# -------------------------
# 2. Global Trends: New Cases & Deaths
# -------------------------
global_df = df.groupby('date')[['new_cases', 'new_deaths']].sum().reset_index()

plt.figure()
plt.plot(global_df['date'], global_df['new_cases'], label='New Cases', color='blue')
plt.plot(global_df['date'], global_df['new_deaths'], label='New Deaths', color='red')
plt.title("Global COVID-19 New Cases & Deaths")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.tight_layout()
plt.savefig("plots/global_trends.png")
plt.show()

# -------------------------
# 3. Top 10 Countries by Total Cases
# -------------------------
latest_df = df[df['date'] == df['date'].max()]
top_countries = latest_df.nlargest(10, 'total_cases')[['location','total_cases']]

plt.figure()
sns.barplot(x='total_cases', y='location', data=top_countries, palette='Reds_r')
plt.title("Top 10 Countries by Total COVID-19 Cases")
plt.xlabel("Total Cases")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("plots/top10_cases.png")
plt.show()

# -------------------------
# 4. Top 10 Countries by Vaccination
# -------------------------
if 'people_vaccinated' in df.columns:
    top_vaccinated = latest_df.nlargest(10, 'people_vaccinated')[['location','people_vaccinated']]
    
    plt.figure()
    sns.barplot(x='people_vaccinated', y='location', data=top_vaccinated, palette='Blues_r')
    plt.title("Top 10 Countries by People Vaccinated")
    plt.xlabel("People Vaccinated")
    plt.ylabel("Country")
    plt.tight_layout()
    plt.savefig("plots/top10_vaccinated.png")
    plt.show()

# -------------------------
# 5. Correlation Heatmap
# -------------------------
numeric_cols = [col for col in ['total_cases','new_cases','total_deaths','new_deaths','total_vaccinations','people_vaccinated'] if col in df.columns]

plt.figure()
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation between COVID-19 Metrics")
plt.tight_layout()
plt.savefig("plots/correlation_heatmap.png")
plt.show()

# -------------------------
# Script Finished
# -------------------------
print("All plots saved in the 'plots/' folder ✅")
