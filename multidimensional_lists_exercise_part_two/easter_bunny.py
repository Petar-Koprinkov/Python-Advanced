n = int(input())
matrix = []
bunny = []
for row in range(n):
    matrix.append([x for x in input().split()])
    for col in range(n):
        if matrix[row][col] == "B":
            bunny = [row, col]

possible_moves = {"up": [-1, 0], "down": [1, 0], "right": [0, 1], "left": [0, -1]}
max_direction = ""
max_eggs = float("-inf")
max_eggs_matrix = []

for direction, value in possible_moves.items():
    current_eggs = 0
    egg_matrix = []
    new_row = bunny[0] + value[0]
    new_col = bunny[1] + value[1]

    while 0 <= new_row < n and 0 <= new_col < n:
        if matrix[new_row][new_col] == "X":
            break

        current_eggs += int(matrix[new_row][new_col])
        egg_matrix.append([new_row, new_col])
        new_row += value[0]
        new_col += value[1]

    if current_eggs > max_eggs and egg_matrix:
        max_direction = direction
        max_eggs = current_eggs
        max_eggs_matrix = egg_matrix


print(max_direction)
[print(row) for row in max_eggs_matrix]
print(max_eggs)


