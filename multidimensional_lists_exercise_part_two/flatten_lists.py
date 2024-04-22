text = input().split("|")
matrix = []

for index in range(len(text) - 1, - 1, - 1):
    row = [int(x) for x in text[index].split()]
    if row:
        matrix.append(row)

for row in matrix:
    print(*row, end=" ")