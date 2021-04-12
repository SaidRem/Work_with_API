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
    if r.status_code != 200:
        return f"Not Found the city: {city}"
    r = r.json()
    return r

def print_today_temp(city):
    r = today_weather(city)
    temp_keys = r['main'].keys()
    for k in temp_keys:
        print('| {:^12} |'.format(k), end='')
    print('\n' + '-' * 100)
    for k in temp_keys:
        print('| {:^12} |'.format(r['main'][k]), end='')
    return None

def weather_5d_forecast(city=None, msr="metric"):
    city = city if city else "Moscow"
    p = dict(q=city, units=msr, appid=API_KEY)
    r = requests.get(f"{URL_API}//forecast", params=p)
    if r.status_code != 200:
        return f"Not Found the city: {city}"
    r = r.json()
    return r

def forecast_reader():
    weather = weather_5d_forecast()
    for w in weather['list']:
        pprint(w)
        more = input('More? (y-yes, n-no)=> ')
        if more != 'y':
            return None


if __name__ == "__main__":
    weather = input(f"Enter: t - 'today weather'\n{7*' '}f - 'five days weather': ")
    if weather == 'f':
        city = input("Enter city name => ")
        pprint(weather_5d_forecast(city=city if city else None)['list'][0])
    else:
        city = input("Enter city name => ")
        pprint(today_weather(city=city if city else None))

