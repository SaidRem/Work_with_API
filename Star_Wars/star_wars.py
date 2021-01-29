import requests
import os
# URLs
URL_PEOPLE = 'https://www.swapi.tech/api/people/'
URL_PLANETS = 'https://swapi.dev/api/planets/'
URL_STARSHIPS = 'https://swapi.dev/api/planets/'

def get_people(name=None):
    '''
    Returns dict object with characters of the Star Wars
    if not specified name of a character.
       '''
    if name:
        people = requests.get(URL_PEOPLE + name).json()
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
    if name:
        starships = requests.get(URL_STARSHIPS + name).json()
    else:
        starships = requests.get(URL_STARSHIPS).json()
    return starships

if __name__ == '__main__':
    print(get_people('1/')) # Info about Luke Skywalker.
    print(get_people())     # First page of characters list.
    print(starships())
