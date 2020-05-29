import sys
import pprint
import requests
from dateutil.parser import parse


class CityInfo:
    def __init__(self, city):
        self.city = city

    def weather_forecast(self):
        pass


def _main(city):
    city_info = CityInfo("Moscow")
    forecast = city_info.weather_forecast()
    pprint.pprint(forecast)


if __name__ == "__main__":
    city = input('Enter the city').strip()
    _main(city)