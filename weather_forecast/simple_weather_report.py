import sys
import requests

def weather(city):
    resp = requests.get(f"https://wttr.in/city")
    print(resp.text)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        weather(' '.join(sys.argv[1:]))
    else:
        weather(input('Enter your city => '))
