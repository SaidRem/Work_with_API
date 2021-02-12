import requests
from pprint import pprint


with open("api_key.txt") as f:
    API_KEY = f.readline().rstrip()


URL_API = r"http://api.openweathermap.org/data/2.5"


def today_weather(city=None, msr="metric"):
    """Returns current weather in the city"""
    city = city if city else "Moscow"
    p = dict(q=city, units=msr, appid=API_KEY)
    r = requests.get(f"{URL_API}//weather", params=p)
    r = r.json()
    return r

def weather_5d_forecast(city=None, msr="metric"):
    city = city if city else "Moscow"
    p = dict(q=city, units=msr, appid=API_KEY)
    r = requests.get(f"{URL_API}//forecast", params=p)
    r = r.json()
    return r

def forecast_reader():
    weather = weather_5d_forecast()
    for w in weather['list']:
        pprint(w)
        more = input('More? (y-yes, n-no)=> ')
        if more != 'y':
            return


if __name__ == "__main__":
    weather = input(f"Enter: t - 'today weather'\n{7*' '}f - 'five days weather': ")
    if weather == 'f':
        city = input("Enter city name => ")
        pprint(weather_5d_forecast(city=city if city else None))
    else:
        city = input("Enter city name => ")
        print(today_weather(city=city if city else None))

