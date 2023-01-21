"""
Weather Report
"""

import datetime
import logging
import json
import requests
import yaml


def main():

    """
    Main functionality
    """

    # Configuration file:
    with open("config.yml", "r", encoding="utf-8") as config:

        # Load config file:
        config_file = yaml.safe_load(config)

    # OpenWeatherMap API Configuration:
    auth_token = config_file["openweather_api_token"]
    base_url = config_file["openweather_base_url"]
    api_url = "/data/2.5/onecall"
    api_entries_params = {
        "lat": config_file["latitude"],
        "lon": config_file["longitude"],
        "exclude": "minutely",
        "units": "metric",
        "appid": auth_token,
    }
    api_endpoint = base_url + api_url

    # OpenWeatherMap API call:
    response = requests.get(
        api_endpoint,
        params=api_entries_params,
    )

    # Select first day only (today):
    daily = response.json()["daily"][0]
    hourly = response.json()["hourly"]

    hours = []
    hours_temp = []
    hours_feels = []
    hours_weather = []
    hours_rain_chance = []

    for hour in hourly:

        hour_time = datetime.datetime.fromtimestamp(hour["dt"]).strftime("%-I %p")
        hours.append(hour_time)

        hour_temp = int(hour["temp"])
        hours_temp.append(hour_temp)

        hour_feels = int(hour["feels_like"])
        hours_feels.append(hour_feels)

        hour_weather = hour["weather"]
        hours_weather.append(hour_weather[0]["description"].capitalize())

        hour_rain_chance = round(float(hour["pop"]) * 100)
        hours_rain_chance.append(hour_rain_chance)

    # Store values:
    date = datetime.datetime.fromtimestamp(daily["dt"]).strftime("%A %d %B %Y")
    sunrise = datetime.datetime.fromtimestamp(daily["sunrise"]).strftime("%H:%M")
    sunset = datetime.datetime.fromtimestamp(daily["sunset"]).strftime("%H:%M")
    humidity = daily["humidity"]
    wind_speed = round(float(daily["wind_speed"]) * 2.236936)  # Convert to MPH
    max_temp = int(daily["temp"]["max"])
    min_temp = int(daily["temp"]["min"])
    weather = daily["weather"][0]["description"].capitalize()

    weather_report = f"""
*{date}*

- Mainly {weather}.
- High of {max_temp}°C. Low of {min_temp}°C.
  - {hours[0]}:
    - {hours_temp[0]}°C feels {hours_feels[0]}°C
    - {hours_weather[0]}
    - {hours_rain_chance[0]}% chance of rain
  - {hours[5]}:
    - {hours_temp[5]}°C feels {hours_feels[5]}°C
    - {hours_weather[5]}
    - {hours_rain_chance[5]}% chance of rain
  - {hours[10]}:
    - {hours_temp[10]}°C feels {hours_feels[10]}°C
    - {hours_weather[10]}
    - {hours_rain_chance[10]}% chance of rain
  - {hours[15]}:
    - {hours_temp[15]}°C feels {hours_feels[15]}°C
    - {hours_weather[15]}
    - {hours_rain_chance[15]}% chance of rain
  - {hours[20]}:
    - {hours_temp[20]}°C feels {hours_feels[20]}°C
    - {hours_weather[20]}
    - {hours_rain_chance[20]}% chance of rain
  - {hours[22]}:
    - {hours_temp[22]}°C feels {hours_feels[22]}°C
    - {hours_weather[22]}
    - {hours_rain_chance[22]}% chance of rain
- Wind speed of {wind_speed}mph
- Humidity at {humidity}%
- Sun rises at {sunrise}. Sets at {sunset}.
"""

    # Gotify API Configuration:
    token = config_file["gotify_app_token"]
    base_url = config_file["gotify_base_url"]
    api_url = f"/message?token={token}"
    api_payload = {
        "priority": 4,
        "title": "Weather Report",
        "message": f"{weather_report}",
        "extras": {
          "client::display": {
            "contentType": "text/markdown"
          },
        },
    }
    api_endpoint = base_url + api_url

    # Gotify API call:
    response = requests.post(
        api_endpoint,
        headers={"Content-Type": "application/json"},
        data=json.dumps(api_payload),
    )


if __name__ == "__main__":
    main()
