import socket

minimum = 0
maximum = pow(10, 100)

current = maximum // 2

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('24.199.110.35', 41199)
sock.connect(server_address)

response: str = ''

while True:
    print(current)
    sock.send((str(current) + '\n').encode('utf-8'))
    response = sock.recv(4048).decode('utf-8')
    print(response)
    print(f'diff: {maximum - minimum}')
    if 'small' in response:
        minimum = current
    elif 'large' in response:
        maximum = current
    else:
        print(sock.recv(4048))
        break
    current = (minimum + maximum) // 2

'''
from random import randint
import time
ans = randint(0, pow(10, 100))
start_time = int(time.time())
turns = 0
while True:
    turns += 1

    inp = input()

    if int(time.time()) > start_time + 60:
        print("you ran out of time you silly goose")
        break

    if "q" in inp:
        print("you are no fun you silly goose")
        break

    if not inp.isdigit():
        print("give me a number you silly goose")
        continue

    inp = int(inp)
    if inp > ans:
        print("your answer is too large you silly goose")
    elif inp < ans:
        print("your answer is too small you silly goose")
    else:
        print("congratulations you silly goose")
        f = open("/flag.txt", "r")
        print(f.read())

    if turns > 500:
        print("you have a skill issue you silly goose")

'''
