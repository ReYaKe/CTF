import requests
from urllib.parse import unquote

URL = "http://natas28.natas.labs.overthewire.org/index.php"

session = requests.Session()
session.auth = ("natas28", "1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj")

auth = session.post(URL)



with open("encoded_queries.txt", "w") as file:
    for i in range(0, 26):
        PARAMS = {'query': 'a' * 9 + chr(97 + i)}
        req = session.get(url=URL, params=PARAMS)
        file.write(f"{chr(97 +i)} {i} {unquote(req.url).split("query=",1)[1]}\n")
        

with open("encoded_queries3.txt", "w") as file:
    for i in range(0, 26):
        PARAMS = {'query': 'a' * i}
        req = session.get(url=URL, params=PARAMS)
        file.write(f"Num of Chars {i} {unquote(req.url).split("query=",1)[1]}\n")

