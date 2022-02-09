# Weather Report

A personal script that uses the [OpenWeatherMap](https://openweathermap.org/api/one-call-api) API to send a daily weather report to a Telegram [bot](https://core.telegram.org/bots).

## Usage

The script needs a trigger to run at a certain time. I run the script at 7am every morning via a cron job.

```sh
0 7 * * * cd weather-report/ && /usr/bin/python3 weather-report/main.py
```

## Configuration File

You must create a file named `config.yml` which contains _real_ key/values below. An example file named `config_template.yml` is also provided in the repository.

```yaml
latitude: -71.413177
longitude: 21.144019
openweather_api_token: 3lc7bnsiutp6iypfmi26lt9b40fdi1bv
openweather_base_url: https://api.openweathermap.org
telegram_base_url: https://api.telegram.org
telegram_bot_chat_id: 7290765823
telegram_bot_token: 5327221129:HPsqtlsXDX2d8au2LsvdN88yqvpWjQLw9ML
log_path: /tmp
```

## Output

The script will output the following message and also post it to your Telegram bot.

> Weather Report
> Wednesday 09 February 2022
> 
> - Mainly Light rain.
> - High of 10°C. Low of 7°C.
>   - 7 AM: 8°C (4°C) Broken clouds
>   - 12 PM: 9°C (7°C) Overcast clouds
>   - 5 PM: 9°C (8°C) Light rain
>   - 10 PM: 7°C (6°C) Overcast clouds
>   - 3 AM: 5°C (3°C) Overcast clouds
>   - 5 AM: 4°C (2°C) Overcast clouds
> - Wind speed of 18mph
> - Humidity at 80%
> - Sun rises at 07:25. Sets at 17:01.
> - Moon is 0.28% full.

