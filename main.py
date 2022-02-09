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

    for hour in hourly:

        hour_time = datetime.datetime.fromtimestamp(hour["dt"]).strftime("%-I %p")
        hours.append(hour_time)

        hour_temp = int(hour["temp"])
        hours_temp.append(hour_temp)

        hour_feels = int(hour["feels_like"])
        hours_feels.append(hour_feels)

        hour_weather = hour["weather"]
        hours_weather.append(hour_weather[0]["description"].capitalize())

    # Store values:
    date = datetime.datetime.fromtimestamp(daily["dt"]).strftime("%A %d %B %Y")
    sunrise = datetime.datetime.fromtimestamp(daily["sunrise"]).strftime("%H:%M")
    sunset = datetime.datetime.fromtimestamp(daily["sunset"]).strftime("%H:%M")
    moon_phase = daily["moon_phase"]
    humidity = daily["humidity"]
    wind_speed = round(float(daily["wind_speed"]) * 2.236936)  # Convert to MPH
    max_temp = int(daily["temp"]["max"])
    min_temp = int(daily["temp"]["min"])
    weather = daily["weather"][0]["description"].capitalize()

    weather_report = f"""
<b>Weather Report</b>
<i>{date}</i>

- Mainly {weather}.
- High of {max_temp}°C. Low of {min_temp}°C.
  - {hours[0]}: {hours_temp[0]}°C (<i>{hours_feels[0]}°C</i>) {hours_weather[0]}
  - {hours[5]}: {hours_temp[5]}°C (<i>{hours_feels[5]}°C</i>) {hours_weather[5]}
  - {hours[10]}: {hours_temp[10]}°C (<i>{hours_feels[10]}°C</i>) {hours_weather[10]}
  - {hours[15]}: {hours_temp[15]}°C (<i>{hours_feels[15]}°C</i>) {hours_weather[15]}
  - {hours[20]}: {hours_temp[20]}°C (<i>{hours_feels[20]}°C</i>) {hours_weather[20]}
  - {hours[22]}: {hours_temp[22]}°C (<i>{hours_feels[22]}°C</i>) {hours_weather[22]}
- Wind speed of {wind_speed}mph
- Humidity at {humidity}%
- Sun rises at {sunrise}. Sets at {sunset}.
- Moon is {moon_phase}% full.
"""

    # Telegram API Configuration:
    bot_token = config_file["telegram_bot_token"]
    base_url = config_file["telegram_base_url"]
    chat_id = str(config_file["telegram_bot_chat_id"])
    api_url = f"/bot{bot_token}/sendMessage"
    api_payload = {
        "chat_id": chat_id,
        "parse_mode": "HTML",
        "text": f"{weather_report}",
    }
    api_endpoint = base_url + api_url

    # Telegram API call:
    response = requests.post(
        api_endpoint,
        headers={"Content-Type": "application/json"},
        data=json.dumps(api_payload),
    )


if __name__ == "__main__":
    main()
