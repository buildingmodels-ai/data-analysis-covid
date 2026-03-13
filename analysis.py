import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("owid-covid-data.csv")

# Select country
country = "France"
df = df[df["location"] == country].copy()

# Keep relevant columns
columns = ["date", "total_cases", "new_cases", "total_deaths"]
df = df[columns]

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Drop missing values
df = df.dropna()

# Compute 7-day rolling average for new cases
df["new_cases_7day_avg"] = df["new_cases"].rolling(window=7).mean()

# Basic statistics
print(f"\nCOVID-19 Analysis for {country}")
print("=" * 50)
print(f"Total cases: {df['total_cases'].iloc[-1]:,.0f}")
print(f"Total deaths: {df['total_deaths'].iloc[-1]:,.0f}")
print(f"Average daily cases: {df['new_cases'].mean():,.0f}")
print(f"Peak daily cases: {df['new_cases'].max():,.0f}")

# Plot rolling average of new cases
plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["new_cases_7day_avg"])
plt.title(f"7-Day Rolling Average of New COVID-19 Cases in {country}")
plt.xlabel("Date")
plt.ylabel("New Cases (7-day avg)")
plt.grid(True)
plt.tight_layout()
plt.savefig("covid_analysis.png")
plt.show()
