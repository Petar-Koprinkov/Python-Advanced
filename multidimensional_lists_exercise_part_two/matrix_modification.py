n = int(input())

matrix = [[int(x) for x in input().split()] for row in range(n)]

while True:
    command = input().split()

    if command[0] == "END":
        break
    if command[0] == "Add":
        row1 = int(command[1])
        col1 = int(command[2])
        value = int(command[3])
        if 0 <= row1 < len(matrix) and 0 <= col1 < len(matrix):
            matrix[row1][col1] += value
        else:
            print("Invalid coordinates")
    elif command[0] == "Subtract":
        row1 = int(command[1])
        col1 = int(command[2])
        value = int(command[3])
        if 0 <= row1 < len(matrix) and 0 <= col1 < len(matrix):
            matrix[row1][col1] -= value
        else:
            print("Invalid coordinates")

[print(*row) for row in matrix]
