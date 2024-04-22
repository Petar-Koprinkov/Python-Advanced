n = int(input())
matrix = []
knights = []


for row in range(n):
    spot = [x for x in input()]
    matrix.append(spot)
    for col in range(n):
        if matrix[row][col] == "K":
            knights.append([row, col])


possible_moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
removed_knights = 0

while True:
    max_hits = 0
    max_knight = [0, 0]
    for row_knight, col_knights in knights:
        hits = 0
        for move in possible_moves:
            new_row = row_knight + move[0]
            new_col = col_knights + move[1]
            if 0 <= new_row < n and 0 <= new_col < n:
                if matrix[new_row][new_col] == "K":
                    hits += 1

        if max_hits < hits:
            max_hits = hits
            max_knight = [row_knight, col_knights]

    if max_hits == 0:
        break
    knights.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = "O"
    removed_knights += 1


print(removed_knights)
