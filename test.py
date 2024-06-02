import requests
import math


API_KEY = '630dea8006f357522839852b2064a460'

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit


def calculate_relative_humidity(temperature_celsius, humidity_percentage):
    # Calculate vapor pressure (e)
    saturation_vapor_pressure = 6.112 * math.exp((17.62 * temperature_celsius) / (243.12 + temperature_celsius))
    vapor_pressure = (humidity_percentage / 100) * saturation_vapor_pressure

    # Calculate relative humidity
    relative_humidity = (vapor_pressure / saturation_vapor_pressure) * 100
    return relative_humidity
def getWeatherData(location):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + location + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        temp = celsius_to_fahrenheit(main["temp"])
        humidity = main["humidity"]
        hi = celsius_to_fahrenheit(main["feels_like"])
        rh = calculate_relative_humidity(main["temp"], humidity)/100
        return hi, temp, rh
    else:
        return None, None, None

hi,temp,humidity = getWeatherData("mahasamund")
print(hi, temp, humidity)

