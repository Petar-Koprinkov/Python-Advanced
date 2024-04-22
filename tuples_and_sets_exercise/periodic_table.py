n = int(input())
table = set()

for _ in range(n):
    line = [x for x in input().split()]
    table.update(line)

print(*table, sep="\n")
