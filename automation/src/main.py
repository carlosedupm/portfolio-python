import requests
import schedule
import time
import os
from dotenv import load_dotenv
from typing import List

load_dotenv()

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")


def get_weather_data(city: str) -> dict:
    """
    Fetches weather data from OpenWeatherMap API.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def transform_weather_data(data: dict) -> dict:
    """
    Transforms weather data to extract relevant information.
    """
    city_name = data["name"]
    if not city_name:
        raise ValueError("City name not found in the response.")
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    return {"city": city_name, "temperature": temperature, "humidity": humidity, "description": description}


def save_weather_data(data: dict, filename: str = "weather_data.csv") -> None:
    """
    Saves weather data to a CSV file.
    """
    with open(filename, "w") as f:
        f.write("temperature,humidity,description\n")
        f.write(
            f"{data['city']},{data['temperature']},{data['humidity']},{data['description']}\n")


def job(city: str) -> None:
    """
    Job to be scheduled to fetch and save weather data.
    """
    try:
        weather_data = get_weather_data(city)
        transformed_data = transform_weather_data(weather_data)
        save_weather_data(transformed_data)
        print(f"Weather data for {city} fetched and saved successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    city = "London"  # Default city
    schedule.every().hour.do(job, city=city)

    while True:
        schedule.run_pending()
        time.sleep(1)
