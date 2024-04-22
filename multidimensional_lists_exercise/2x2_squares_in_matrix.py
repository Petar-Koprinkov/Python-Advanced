rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()]for row in range(rows)]

sequences = 0

for row in range(rows - 1):
    for col in range(cols- 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            sequences += 1

print(sequences)
