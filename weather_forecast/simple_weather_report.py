import sys
import requests

resp = requests.get(f"https://wttr.in/{' '.join(sys.argv[1:])}")

print(resp.text)
