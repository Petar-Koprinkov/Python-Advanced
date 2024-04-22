from collections import deque

rows, cols = [int(x) for x in input().split()]
text = deque(input())
matrix = []


for row in range(rows):
    matrix.append([""] * cols)

for r in range(len(matrix)):
    for col in range(cols):
        if r % 2 == 0:
            matrix[r][col] = text[0]
        else:
            matrix[r][-1 - col] = text[0]

        text.rotate(-1)

[print(*row, sep="") for row in matrix]