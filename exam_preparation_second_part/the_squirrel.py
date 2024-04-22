n = int(input())
direction = [x for x in input().split(", ")]
matrix = []
squirrel = []
HAZELNUTS = 3
collected_hazelnuts = 0

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "s":
            squirrel = [row, col]

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

for move in direction:
    current_row = int(squirrel[0])
    current_col = int(squirrel[1])
    new_row = current_row + direction_mapper[move][0]
    new_col = current_col + direction_mapper[move][1]

    if not (0 <= new_row < n and 0 <= new_col < n):
        print("The squirrel is out of the field.")
        break
    elif matrix[new_row][new_col] == "h":
        matrix[current_row][current_col] = "*"
        squirrel = [new_row, new_col]
        matrix[new_row][new_col] = "s"
        collected_hazelnuts += 1
        if collected_hazelnuts == HAZELNUTS:
            print("Good job! You have collected all hazelnuts!")
            break
    elif matrix[new_row][new_col] == "*":
        matrix[current_row][current_col] = "*"
        matrix[new_row][new_col] = "s"
        squirrel = [new_row, new_col]
    elif matrix[new_row][new_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break
else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {collected_hazelnuts}")
