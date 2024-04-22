data = input().split()
rows = int(data[0])
cols = int(data[1])
matrix = [[x for x in input().split()]for row in range(rows)]

while True:
    command = input().split()

    if command[0] == "END":
        break
    elif command[0] == "swap":
        if len(command[1:]) == 4:
            row1 = int(command[1])
            col1 = int(command[2])
            row2 = int(command[3])
            col2 = int(command[4])

            if row1 in range(rows) and row2 in range(rows) and col1 in range(cols) and col2 in range(cols):
                matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
                [print(*row) for row in matrix]
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
