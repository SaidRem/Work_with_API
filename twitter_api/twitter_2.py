import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# Create App:
# https://apps.twitter.com/


TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Acccount: ')
    if len(acct) < 1:
        break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': 5})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    js = json.loads(data)
    print(json.dumps(js, indent=4))
    # print remaining requests quota
    print(f'Remaining {headers["x-rate-limit-remaining"]}')

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('    Not status found')
            continue
        s = u['status']['text']
        print('    ', s[:50])