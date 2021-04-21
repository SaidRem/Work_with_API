import requests
from pprint import pprint


with open("api_key.txt") as f:
    API_KEY = f.readline().rstrip()


URL_API = r"http://api.openweathermap.org/data/2.5"


class OpenW:
    def __init__(self, city=None, msr="metric"):
        city = city if city else "Moscow"
        self.params = dict(q=city, units=msr, appid=API_KEY)
        res = requests.get(f"{URL_API}//forecast", params=self.params)
        if res.status_code != 200:
            print(f"Not Found the city: {city}")
        self.five_dforecast = res.json()
    
    @property
    def mean_temp(self):
        temp = []
        for obj in self.five_dforecast['list']:
            temp.append(obj['main']['temp'])
        res = '{:.2f}'.format(sum(temp)/len(temp))
        return (f"Mean temperature from {self.five_dforecast['list'][0]['dt_txt']} to "
                f"{self.five_dforecast['list'][-1]['dt_txt']} is {res}")
    
    def __str__(self):
        pprint(self.five_dforecast['list'])


if __name__ == '__main__':
    city = input('Enter city\n=> ')
    ob = OpenW(city)
    # print(ob)
    print(ob.mean_temp)