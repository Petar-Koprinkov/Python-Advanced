matrix = [[int(x) for x in input().split()] for row in range(int(input()))]

primary_diagonal = [matrix[row][row] for row in range(len(matrix))]
secondary_diagonal = [matrix[row][-row - 1] for row in range(len(matrix))]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
