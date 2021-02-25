import requests
import datetime as dt
from json.decoder import JSONDecodeError

with open('vk_api_token.txt') as f:
    token_vk = f.readline().strip()

URL = 'https://api.vk.com/method'
ACCESS_TOKEN = token_vk         # Token from vk to access data through vk API

def r_id_user(uid):
    "Returns user id."
    payload_user = dict(user_ids=uid, fields='bdate', 
                        access_token=ACCESS_TOKEN, v=5.71)
    request_user = requests.get(f'{URL}/users.get', params=payload_user)
    try:
        request_user = request_user.json()
        request_user = request_user['response']
        user_id = request_user[0]['id']
        return user_id
    except (JSONDecodeError, IndexError, KeyError):
        pass


def friends(user):
    "Returns list of dicts."
    id_user = r_id_user(user)
    payload_friends = dict(user_id=id_user, fields='bdate, occupation',
                           access_token=ACCESS_TOKEN, v=5.71)
    response = requests.get(f'{URL}/friends.get', params=payload_friends)
    try:
        response = response.json()
        response = response['response']['items']
        
    except (JSONDecodeError, KeyError):
        pass
    return response[:3]


# TODO
# friends data to sqlite3

if __name__ == '__main__':
    user = input('Enter user id or nickname:\n=> ')
    res = friends(user)
    print(res)
