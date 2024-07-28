import socket


def count_live_cells(grid) -> int:
    return sum([sum(row) for row in grid])


def count_neighbors(grid :[[int]], row: int, col: int, wrap_around: bool = True) -> int:
    count = 0
    for i in range(row - 1, row + 2):
        i_adjusted = i
        if wrap_around:
            i_adjusted = len(grid) - 1 if i < 0 else 0 if i >= len(grid) else i
        elif i < 0 or i >= len(grid):
            continue
        for j in range(col - 1, col + 2):
            if i == row and j == col:
                continue
            j_adjusted = j
            if wrap_around:
                j_adjusted = len(grid[0]) - 1 if j < 0 else 0 if j >= len(grid[0]) else j
            elif j < 0 or j >= len(grid[0]):
                continue
            count += grid[i_adjusted][j_adjusted]
    return count


def simulate(board: [[int]]) -> [[int]]:
    next_board = list([[0] * len(row) for row in board])
    for i in range(len(board)):
        for j in range(len(board[0])):
            live_neighbors = count_neighbors(board, i, j)
            if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                next_board[i][j] = 0
            elif board[i][j] == 0 and live_neighbors == 3:
                next_board[i][j] = 1
            else:
                next_board[i][j] = board[i][j]
    return next_board


def parse_grid(grid_string: str) -> [[int]]:
    lines = grid_string.split('\n')
    grid: [[int]] = []
    for line in lines:
        row = [(1 if char == '■' else 0) for char in line]
        grid.append(row)
    return grid


def print_grid(grid: [[int]]):
    print('Grid state:')
    for row in grid:
        print(''.join([('■' if value == 1 else '.') for value in row]))
    print('---------------------------------------------------------------------------------')


def print_golly_pattern(grid: [[int]]):
    print(f'x = {len(grid[0])}, y = {len(grid)}, rule = B3/S23')
    for row in grid:
        line: str = ''
        for val in row:
            line += 'o' if val == 1 else 'b'
        line += '$'
        print(line)


s = socket.socket()
host = '34.69.226.63'
port = 31293
s.connect((host, port))

data = s.recv(8192).decode()
game_data: [str] = data.split("\n\n")[3:5]
grid: [[int]] = parse_grid(game_data[0])

while True:
    generations = int(game_data[1].split('after ')[1].split()[0])

    print(f'Simulating {generations} generations...')

    grid_growth = 10 + (generations // 2)
    for i in range(len(grid)):
        grid[i] = [0] * grid_growth + grid[i] + [0] * grid_growth
    for j in range(grid_growth):
        grid.insert(0, [0] * (70 + grid_growth * 2))
        grid.append([0] * (70 + grid_growth * 2))

    print_generations = False
    for gen in range(generations):
        grid = simulate(grid)
        if print_generations:
            print_grid(grid)

    live_cells = count_live_cells(grid)
    s.send((str(live_cells) + '\n').encode())

    response = s.recv(4096).decode()

    if 'Congratulations!' in response:
        print(response.split('flag: ')[1])
        break
    elif 'Correct!' in response:
        game_data = response.split("\n\n")[0:2]
        grid: [[int]] = parse_grid(game_data[0].split('Correct!\n')[1])
    else:
        print('Failed...')
        break

s.close()
