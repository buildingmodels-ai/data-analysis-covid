# COVID-19 Data Analysis
Exploratory data analysis of COVID-19 trends using Pandas and Matplotlib.

## Objective
The goal of this project is to analyze COVID-19 case trends using real-world data and apply fundamental data science techniques such as filtering, cleaning, aggregation, and visualization.

## Dataset
This project uses the COVID-19 dataset from Our World in Data (OWID).

Download the dataset from:
https://ourworldindata.org/coronavirus

Place the file `owid-covid-data.csv` in the project directory before running the script.

## Methodology
- Filter data for a specific country (France)
- Select relevant variables (cases and deaths)
- Handle missing values
- Compute 7-day rolling averages
- Generate statistical summaries
- Visualize case trends over time

## Technologies Used
- Python
- Pandas
- Matplotlib

## How to Run
```bash
python analysis.py
```
The script will generate summary statistics and save a visualization as `covid_analysis.png`.
