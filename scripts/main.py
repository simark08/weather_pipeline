
import requests
import pandas as pd
import time


# Open-Meteo API endpoint
API_URL = "https://api.open-meteo.com/v1/forecast"



def fetch_weather(city, country, latitude, longitude):
    """Fetch current weather, retrying temporary connection failures."""

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m"
    }

    for attempt in range(3):
        try:
            response = requests.get(
                API_URL,
                params=params,
                timeout=30
            )
            response.raise_for_status()

            current = response.json()["current"]

            return {
                "City": city,
                "Country": country,
                "Latitude": latitude,
                "Longitude": longitude,
                "Temperature": current["temperature_2m"],
                "Wind_Speed": current["wind_speed_10m"]
            }

        except requests.RequestException as error:
            if attempt == 2:
                raise

            print(
                f"Retrying {city} "
                f"({attempt + 1}/2): {error}"
            )
            time.sleep(2)



if __name__ == "__main__":
    # Load all 50 cities from the CSV file
    population_df = pd.read_csv("data/population.csv")

    weather_records = []

    for _, row in population_df.iterrows():
        try:
            weather = fetch_weather(
                city=row["City"],
                country=row["Country"],
                latitude=float(row["Latitude"]),
                longitude=float(row["Longitude"])
            )

            weather_records.append(weather)
            print(f"Fetched weather for {row['City']}")

        except (requests.RequestException, KeyError, ValueError) as error:
            print(f"Error for {row['City']}: {error}")

        time.sleep(0.1)

    # Convert results into a DataFrame
    weather_df = pd.DataFrame(weather_records)

    # Save weather data to CSV
    weather_df.to_csv(
        "data/weather_data.csv",
        index=False
    )

    print("\nWeather data preview:")
    print(weather_df.head())

    print(f"\nTotal cities with weather data: {len(weather_df)}")
    print("Saved to data/weather_data.csv")


    # Merge weather data with population data
    population_df = pd.read_csv("data/population.csv")
    weather_df = pd.read_csv("data/weather_data.csv")

   
    merged_df = population_df.merge(
    weather_df.drop(columns=["Latitude", "Longitude"]),
    on=["City", "Country"],
    how="left",
    validate="one_to_one"
)
    # Save the combined dataset
    merged_df.to_csv(
        "data/merged_weather_population.csv",
        index=False
    )

    print("\nMerged dataset preview:")
    print(merged_df.head())

    print(f"\nTotal merged records: {len(merged_df)}")
    print("Saved to data/merged_weather_population.csv")
