# Weather Report

A personal script that uses the [OpenWeatherMap](https://openweathermap.org/api/one-call-api) API to send a daily weather report to [Gotify](https://gotify.net/).

## Usage

The script needs a trigger to run at a certain time. I run the script at 7am every morning via a cron job.

```sh
0 7 * * * cd weather-report/ && /usr/bin/python3 weather-report/main.py
```

## Configuration File

You must create a file named `config.yml` which contains _real_ key/values below. An example file named `config_template.yml` is also provided in the repository.

## Output

The script will send a message in the following format to a Gotify app specified in `config.yml`.

> Weather Report
> Wednesday 09 February 2022
> 
> - Mainly Light rain.
> - High of 10°C. Low of 7°C.
>   - 7 AM: 8°C (4°C) Broken clouds, 0% 🌧
>   - 12 PM: 9°C (7°C) Overcast clouds, 0% 🌧
>   - 5 PM: 9°C (8°C) Light rain, 100% 🌧
>   - 10 PM: 7°C (6°C) Overcast clouds, 0% 🌧
>   - 3 AM: 5°C (3°C) Overcast clouds, 0% 🌧
>   - 5 AM: 4°C (2°C) Overcast clouds, 0% 🌧
> - Wind speed of 18mph
> - Humidity at 80%
> - Sun rises at 07:25. Sets at 17:01.

