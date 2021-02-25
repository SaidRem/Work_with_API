import requests
from pprint import pprint

with open('api_token.txt') as f:
    API_TOKEN = f.readline().strip()

URL_API_KINO = 'https://api.kinopoisk.cloud'

def movie(id):
    res = requests.get(URL_API_KINO + f'/movies/{id}' + f'/token/{API_TOKEN}')
    return res.json()


if __name__ == '__main__':
    pprint(movie(1143242))
