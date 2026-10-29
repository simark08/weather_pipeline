
import requests
import pandas as pd

# Open-Meteo API endpoint
API_URL = "https://api.open-meteo.com/v1/forecast"


def fetch_weather(city, country, latitude, longitude):
    """Fetch current weather data for one city."""

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m"
    }

    response = requests.get(API_URL, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()
    current = data["current"]

    return {
        "City": city,
        "Country": country,
        "Latitude": latitude,
        "Longitude": longitude,
        "Temperature": current["temperature_2m"],
        "Wind_Speed": current["wind_speed_10m"]
    }


if __name__ == "__main__":
    # Test with one capital city first.
    weather = fetch_weather(
        city="New Delhi",
        country="India",
        latitude=28.6139,
        longitude=77.2090
    )

    weather_df = pd.DataFrame([weather])
    print(weather_df)
