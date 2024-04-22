from collections import deque

n = int(input())
commands = deque(input().split())

matrix = []

miner_row, miner_col = 0, 0
coal = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "s":
            miner_row, miner_col = row, col
        elif matrix[row][col] == "c":
            coal += 1


def is_command_valid(r, c, size):
    return 0 <= r < size and 0 <= c < size


def up(r, c, n):
    r -= 1
    if is_command_valid(r, c, n):
        return r, c
    r += 1
    return r, c


def down(r, c, n):
    r += 1
    if is_command_valid(r, c, n):
        return r, c
    r -= 1
    return r, c


def left(r, c, n):
    c -= 1
    if is_command_valid(r, c, n):
        return r, c
    c += 1
    return r, c


def right(r, c, n):
    c += 1
    if is_command_valid(r, c, n):
        return r, c
    c -= 1
    return r, c


dictionary = {
    "up": up,
    "down": down,
    "right": right,
    "left": left,
}


while commands:
    command = commands.popleft()

    miner_row, miner_col = dictionary[command](miner_row, miner_col, n)

    if matrix[miner_row][miner_col] == "c":
        coal -= 1
        matrix[miner_row][miner_col] = "*"
        if not coal:
            print(f"You collected all coal! ({miner_row}, {miner_col})")
            break
    elif matrix[miner_row][miner_col] == "e":
        print(f"Game over! ({miner_row}, {miner_col})")
        break

    if not commands:
        print(f"{coal} pieces of coal left. ({miner_row}, {miner_col})")

