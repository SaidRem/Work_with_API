import requests

# URL
URL_PEOPLE = 'https://www.swapi.tech/api/people/'
URL_PLANETS = 'https://swapi.dev/api/planets/'

# Let's get info about first four character
def get_people(name=None):
    if name:
        people = requests.get(URL_PEOPLE + name).json()
    else:
        people = requests.get(URL_PEOPLE).json()
    return people



# Let's get info about some planets in Star Wars Universe
def planets():
    planets = requests.get(URL_PLANETS).json()
    return planets


if __name__ == '__main__':
    print(get_people('1/')) # Info about Luke Skywalker.
    print(get_people())     # First page of characters list.