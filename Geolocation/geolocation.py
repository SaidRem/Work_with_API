import requests
from pprint import pprint


def geoloc():
    r = requests.get("http://freegeoip.app/json/").json()
    return r

def coordinates():
    r = geoloc()
    return dict(latitude=r["latitude"], longitude=r["longitude"])


if __name__ == "__main__":
    pprint(geoloc())
    print(f'Your coordinates:\n{coordinates()}')
