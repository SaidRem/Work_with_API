import requests
import os
from pprint import pprint
from json.decoder import JSONDecodeError

# URLs
URL_ROOT = 'https://swapi.dev/api/'
URL_PEOPLE = 'https://www.swapi.tech/api/people/'
URL_PLANETS = 'https://swapi.dev/api/planets/'
URL_STARSHIPS = 'https://swapi.dev/api/planets/'
URL_FILMS = 'https://swapi.dev/api/films/'
URL_VEHICLES = 'https://swapi.dev/api/vehicles/'

def root():
    '''
    Provides information on all available resources within the API.
    '''
    try:
        result = requests.get(URL_ROOT).json()
    except (JSONDecodeError, IndexError, KeyError):
        pass
    return result

def get_people(name=None, url=None):
    '''
    Returns dict object with characters of the Star Wars
    if not specified name of a character.
       '''
    # params = dict(page=2, limit=10) # notation for getting pages
    if name:
        people = requests.get(URL_PEOPLE + name).json()
    elif url:
        people = requests.get(url).json()
    else:
        people = requests.get(URL_PEOPLE).json()
    return people



# Let's get info about some planets in Star Wars Universe
def planets(name=None):
    ''' 
    Returns dict object with planets of Star Wars Universe.
    '''
    if name:
        planets = requests.get(URL_PLANETS + name).json()
    else:
        planets = requests.get(URL_PLANETS).json()
    return planets


def starships(name=None):
    """
    Returns data for a transport craft that has
    hyperdrive capability.
    """
    if name:
        starships = requests.get(URL_STARSHIPS + name).json()
    else:
        starships = requests.get(URL_STARSHIPS).json()
    return starships


def vehicles(name=None):
    """
    A Vehicle resource is a single transport craft that
    does not have hyperdrive capability.
    """
    if name:
        vehicle = requests.get(URL_VEHICLES + name).json()
    else:
        vehicle = requests.get(URL_VEHICLES).json()
    return vehicle


def films(name=None):
    if name:
        film = requests.get(URL_FILMS + name).json()
    else:
        film = requests.get(URL_FILMS).json()
    return film

if __name__ == '__main__':
    # print(get_people('1/')) # Info about Luke Skywalker.
    # print(get_people())        # First page of characters list.
    pprint(vehicles())
    # nex = get_people()['next']
    # print(get_people(url=nex))
    # print(starships())
