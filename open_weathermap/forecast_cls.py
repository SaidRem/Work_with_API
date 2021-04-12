import requests
from pprint import pprint


with open("api_key.txt") as f:
    API_KEY = f.readline().rstrip()


URL_API = r"http://api.openweathermap.org/data/2.5"


class OpenW:
    def __init__(self, city, msr="metric"):
        self.p = dict(q=city, units=msr, appid=API_KEY)
        res = requests.get(f"{URL_API}//forecast", params=p)
        if res.status_code != 200:
            print(f"Not Found the city: {city}")
        self.5dforecast = res.json()
