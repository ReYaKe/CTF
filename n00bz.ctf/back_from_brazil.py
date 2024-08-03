import socket
import queue

minimum = 0
maximum = pow(10, 100)

current = maximum // 2

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('24.199.110.35', 43298)
sock.connect(server_address)

for _ in range(10):
    response: str = ''
    grid: [[int]] = []
    row: str = ''
    while len(grid) < 1000:
        response = sock.recv(4048).decode('utf-8')
        if '\n' not in response:
            row += response
        else:
            split_response: [str] = response.split('\n')
            row += split_response[0]
            grid.append(list(int(x) for x in row.split()))
            row = split_response[1]

    optimal = int(response.split('optimal: ', maxsplit=1)[1].split()[0])

    active: queue = queue.Queue(1000)
    active.put((0, 0))
    counter = 0
    while not active.empty():
        coords: (int, int) = active.get()
        counter += 1
        if coords[0] > 0 and coords[1] > 0:
            grid[coords[0]][coords[1]] += max(grid[coords[0] - 1][coords[1]], grid[coords[0]][coords[1] - 1])
        elif coords[0] > 0:
            grid[coords[0]][coords[1]] += grid[coords[0] - 1][coords[1]]
        elif coords[1] > 0:
            grid[coords[0]][coords[1]] += grid[coords[0]][coords[1] - 1]

        if coords[0] < 999 and coords[1] == 0:
            active.put((coords[0] + 1, coords[1]))
        if coords[1] < 999:
            active.put((coords[0], coords[1] + 1))

    if optimal == grid[999][999]:
        print(f'Found optimal sum: {optimal}!')
        path: str = ''
        coords: (int, int) = (999, 999)
        while True:
            if coords[0] > 0 and coords[1] > 0:
                a = grid[coords[0] - 1][coords[1]]
                b = grid[coords[0]][coords[1] - 1]
                if a > b:
                    path += 'r'
                    coords = (coords[0] - 1, coords[1])
                else:
                    path += 'd'
                    coords = (coords[0], coords[1] - 1)
            elif coords[0] > 0:
                path += 'r'
                coords = (coords[0] - 1, coords[1])
            elif coords[1] > 0:
                path += 'd'
                coords = (coords[0], coords[1] - 1)
            else:
                break

        solution: str = path[::-1]
        sock.send((solution + '\n').encode('utf-8'))
    else:
        print('Failed!')

print(sock.recv(4048).decode('utf-8'))
print(sock.recv(4048).decode('utf-8'))

'''
n = 1000

start = time.time()

for _ in range(10):
    eggs = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(0, 696969))
            print(row[j], end=' ')
        eggs.append(row)
        print()

    solution = solve(eggs)
    print("optimal: " + str(solution) + " ðŸ¥š")
    inputPath = input()
    inputAns = eggs[0][0]
    x = 0
    y = 0

    for direction in inputPath:
        match direction:
            case 'r':
                x += 1
            case 'd':
                y += 1
            case _:
                print("ðŸ¤”")
                exit()

        if x == n or y == n:
            print("out of bounds")
            exit()

        inputAns += eggs[x][y]



    if inputAns < solution:
        print(inputAns)
        print("you didn't find enough ðŸ¥š")
        exit()
    elif len(inputPath) < 2 * n - 2:
        print("noooooooooooooooo, I'm still in Brazil")
        exit()

    if int(time.time()) - start > 60:
        print("you ran out of time")
        exit()

print("tnxs for finding all my ðŸ¥š")
f = open("/flag.txt", "r")
print(f.read())
'''
