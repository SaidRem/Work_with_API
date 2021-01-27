import requests
import time as tm
import datetime as dt
from json.decoder import JSONDecodeError
from collections import Counter

with open('vk_api_token.txt') as f:
    token_vk = f.readline().strip()

URL = 'https://api.vk.com/method'
ACCESS_TOKEN = token_vk         # Token from vk to access data through vk API

# VK API: https://api.vk.com/method/METHOD_NAME?PARAMETERS&access_token=ACCESS_TOKEN&v=V

def r_id_user(uid):
    payload_user = dict(user_ids=uid, fields='bdate', 
                        access_token=ACCESS_TOKEN, v=5.71)
    request_user = requests.get(f'{URL}/users.get', params=payload_user)
    try:
        request_user = request_user.json()['response']
        user_id = request_user[0]['id']
        return user_id
    except (JSONDecodeError, IndexError, KeyError):
        pass

def friends_bdays(id_user):
    payload_friends = dict(user_id=id_user, fields='bdate',
                           access_token=ACCESS_TOKEN, v=5.71)
    result = requests.get(f'{URL}/friends.get', params=payload_friends).json()['response']['items']
    return result
    

def calc_age(uid):
    # today_year = dt.datetime.fromtimestamp(tm.time()).year
    today_year = dt.datetime.now().year
    
    id_user = r_id_user(uid)
    list_friends = friends_bdays(id_user)
#     print(list_friends[:5])


    list_of_bdate = []
    for friend in list_friends:
        if 'bdate' in friend and len(friend['bdate']) > 7:
            list_of_bdate.append(friend['bdate'])
            
#     print(list_of_bdate)
    
    list_of_years = [int(d[-4:]) for d in list_of_bdate]
    list_of_ages = [today_year - year for year in list_of_years]
    d_of_ages = Counter(list_of_ages)
    tuples_ages = list(d_of_ages.items())
    sorted_ages = sorted(tuples_ages, key=lambda x: (x[1], -x[0]), reverse=True)

    return sorted_ages

    
if __name__ == '__main__':
    user = input('Enter user id or nickname:\n=> ')
    res = calc_age(user)
    print(res)
