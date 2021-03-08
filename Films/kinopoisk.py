import requests
from pprint import pprint

with open('api_token.txt') as f:
    API_TOKEN = f.readline().strip()

URL_API_KINO = 'https://api.kinopoisk.cloud'

def movie(id):
    res = requests.get(f'{URL_API_KINO}/movies/{id}/token/{API_TOKEN}')
    return res.json()

def tv_series(id):
    res = requests.get(f'{URL_API_KINO}/tv-series/{id}/token/{API_TOKEN}')
    return res.json()


if __name__ == '__main__':
    pprint(movie(1143242))
