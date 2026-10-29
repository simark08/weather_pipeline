# Weather Data Engineering Pipeline

## Project Overview
This project collects current weather data using the Open-Meteo API, combines it with population data for 70 cities, and analyses the results using Google BigQuery and Looker Studio.

## Technologies Used
- Python, Pandas, Requests
- Open-Meteo API
- Google BigQuery
- Looker Studio
- Git and GitHub

## Project Structure
```text
weather_pipeline/
├── scripts/
│   └── main.py
├── data/
├── requirements.txt
├── .gitignore
└── README.md
```

## Pipeline Workflow
1. Read city population and location data.
2. Fetch current weather information through the API.
3. Merge weather and population datasets.
4. Validate and save the processed CSV.
5. Upload the dataset to BigQuery for SQL analysis.
6. Visualize temperature data using a Looker Studio dashboard.

## How to Run
Install dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python scripts/main.py
```

## BigQuery
Table: `weather-data-pipeline-513120.weather_analytics.city_weather`

The dataset supports analysis of city populations, temperatures, and wind speeds.

## Security
Never commit GCP JSON keys or sensitive credentials to GitHub. Use `.gitignore` to exclude sensitive files and generated data where appropriate.

