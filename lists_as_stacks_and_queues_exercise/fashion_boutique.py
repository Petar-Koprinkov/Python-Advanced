from collections import deque

clothes = deque([int(x) for x in input().split()])
store = int(input())
rack = 1
storage = store

while clothes:
    if storage >= clothes[-1]:
        storage -= clothes.pop()
    else:
        rack += 1
        storage = store

print(rack)


