rows, cols = [int(x) for x in input().split(",")]
matrix = []
mouse = []
cheese_count = 0

for row in range(rows):
    matrix.append([el for el in input()])
    for col in range(cols):
        if matrix[row][col] == "M":
            mouse = [row, col]
        if matrix[row][col] == "C":
            cheese_count += 1

possible_moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

command = input()
eaten_cheese = 0

while command != "danger":
    current_row = mouse[0]
    current_col = mouse[1]
    new_row_mouse = current_row + possible_moves[command][0]
    new_col_mouse = current_col + possible_moves[command][1]
    mouse = [new_row_mouse, new_col_mouse]
    if not (0 <= new_row_mouse < rows and 0 <= new_col_mouse < cols):
        print("No more cheese for tonight!")
        break
    elif matrix[new_row_mouse][new_col_mouse] == "C":
        matrix[new_row_mouse][new_col_mouse] = "M"
        matrix[current_row][current_col] = "*"
        eaten_cheese += 1
        if eaten_cheese == cheese_count:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif matrix[new_row_mouse][new_col_mouse] == "T":
        matrix[new_row_mouse][new_col_mouse] = "M"
        matrix[current_row][current_col] = "*"
        print("Mouse is trapped!")
        break
    elif matrix[new_row_mouse][new_col_mouse] == "@":
        mouse = [current_row, current_col]
        command = input()
        continue
    elif matrix[new_row_mouse][new_col_mouse] == "*":
        matrix[new_row_mouse][new_col_mouse] = "M"
        matrix[current_row][current_col] = "*"
    command = input()
else:
    print("Mouse will come back later!")

for row in matrix:
    print(*row, sep='')






