# Weather Report

A personal script that uses the [OpenWeatherMap](https://openweathermap.org/api/one-call-api) API to send a daily weather report to Telegram.

## Usage

The script needs a trigger to run at a certain time. I run the script at 7am every morning via a cron job.

```sh
0 7 * * * cd weather-report/ && /usr/bin/python3 weather-report/main.py
```

## Configuration File

You must create a file named `config.yml` which contains _real_ key/values below. An example file named `config_template.yml` is also provided in the repository.

## Output

The script will send a message in the following format to Telegram.

> Wednesday 07 June 2023
> 
> - Mainly Scattered clouds.
> - High of 19°C. Low of 6°C.
>   - 7 AM:
>     - 10°C feels 9°C
>     - Overcast clouds
>     - 0% chance of rain
>   - 12 PM:
>     - 17°C feels 17°C
>     - Scattered clouds
>     - 0% chance of rain
>   - 5 PM:
>     - 18°C feels 18°C
>     - Scattered clouds
>     - 0% chance of rain
>   - 10 PM:
>     - 8°C feels 6°C
>     - Clear sky
>     - 0% chance of rain
>   - 3 AM:
>     - 6°C feels 3°C
>     - Few clouds
>     - 0% chance of rain
>   - 5 AM:
>     - 6°C feels 3°C
>     - Few clouds
>     - 0% chance of rain
> - Wind speed of 12mph
> - Humidity at 69%
> - Sun rises at 04:42. Sets at 21:13.

