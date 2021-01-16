import requests

# Some urls
url_people = 'https://www.swapi.tech/api/people/'
url_planets = 'https://swapi.dev/api/planets/'

# Let's get info about first four character

all_people = requests.get(url_people).json()

