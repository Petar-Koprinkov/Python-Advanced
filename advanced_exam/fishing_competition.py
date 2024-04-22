n = int(input())
matrix = []
ship = []
catch = 0
SUCCESSFUL_SEASON = 20
Flag = False

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "S":
            ship = [row,col]

ship_movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

while True:
    command = input()

    if command == "collect the nets":
        break

    ship_row = int(ship[0])
    ship_col = int(ship[1])

    new_row = ship_row + int(ship_movement[command][0])
    new_col = ship_col + int(ship_movement[command][1])

    if new_row == n:
        new_row = 0
    if new_col == n:
        new_col = 0
    if new_row < 0:
        new_row = n - 1
    if new_col < 0:
        new_col = n - 1

    if matrix[new_row][new_col] == "W":
        ship = [new_row, new_col]
        Flag = True
        break
    elif matrix[new_row][new_col] == "-":
        matrix[ship_row][ship_col] = "-"
        matrix[new_row][new_col] = "S"
        ship = [new_row, new_col]
    else:
        catch += int(matrix[new_row][new_col])
        matrix[ship_row][ship_col] = "-"
        matrix[new_row][new_col] = "S"
        ship = [new_row, new_col]

if Flag:
    row_ship = ship[0]
    col_ship = ship[1]
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the "
          f"ship: [{row_ship},{col_ship}]")

elif not Flag:

    if catch >= SUCCESSFUL_SEASON:
        print("Success! You managed to reach the quota!")
    elif SUCCESSFUL_SEASON > catch:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {SUCCESSFUL_SEASON - catch} tons of "
              f"fish more.")

    if catch > 0:
        print(f"Amount of fish caught: {catch} tons.")

    for row in matrix:
        print(*row, sep='')










