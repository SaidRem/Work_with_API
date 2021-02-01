import requests


with open("api_key.txt") as f:
    API_KEY = f.readline().rstrip()


URL_API = r"http://api.openweathermap.org/data/2.5"


def today_weather(city=None, msr="metric"):
    """Returns current weather in a city"""
    if city:
        p = dict(q=city, units=msr, appid=API_KEY)
    else:
        p = dict(q="Astrakhan", units=msr, appid=API_KEY)
    r = requests.get(f"{URL_API}//weather", params=p)
    r = r.json()
    return r


if __name__ == "__main__":
    city = input("Enter city name => ")
    if city:
        print(today_weather(city=city))
    else:
        print(today_weather())

