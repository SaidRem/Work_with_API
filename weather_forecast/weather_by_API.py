import sys
import pprint
import requests
from dateutil.parser import parse


API_KEY_YAN_WEATHER = open('api_key_yandex_weather').readline()    # type in the key, recieved from yandex
API_KEY_YAN_GEO = open('api_key_yandex_geoloc').readline()         # type in the key, recieved from yandex
URL_YanWeather = (f"https://api.weather.yandex.ru/v1/forecast?lat={geo[0]}&lon"
                  f"={geo[1]}&extra=true")
URL_YanGeoLoc = (f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY_YAN_GEO}"
                 f"&format=json&geocode={city}")


class YandexWeather:

    def get(self, city):
        """Get weather forecast through yandex api"""
        headers = {'X-Yandex-API-Key': API_KEY_YAN_WEATHER}
        data = requests.get(URL_YanWeather, headers=headers).json()
        forecast = {
            'temp': data['fact']['temp'],
            'pressure': data['fact']['pressure_mm']
        }
        return forecast


class Geoloc:

    def get_point(city):
        data = requests.get(URL_YanGeoLoc).json()["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]["Point"]["pos"]
        return data.split()


class CityInfo:
    def __init__(self, city, forecast_provider=None):
        self.city = city.lower()
        self._forecast_provider = forecast_provider or YandexWeather()    # Default use yandex api

    def weather_forecast(self):
        return self._forecast_provider.get(self.city)


def main_p(city):
    city_info = CityInfo(city)
    forecast = city_info.weather_forecast()
    pprint.pprint(forecast)


if __name__ == "__main__":
    city = input('Enter the city').strip()
    main_p(city)
