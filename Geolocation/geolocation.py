import requests
from pprint import pprint


def geoloc():
    r = requests.get("http://freegeoip.app/json/").json()
    return r


if __name__ == "__main__":
    pprint(geoloc())
