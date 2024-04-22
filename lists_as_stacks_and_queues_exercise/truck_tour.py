from collections import deque
n = int(input())
pumps = deque([[int(x) for x in input().split()]for _ in range(n)])
start_position = 0
stops = 0


while stops < n:
    total_petrol = 0
    for index in range(n):
        gas = pumps[index][0]
        distance = pumps[index][1]
        total_petrol += gas
        if total_petrol < distance:
            pumps.rotate(-1)
            stops = 0
            start_position += 1
            break
        else:
            total_petrol -= distance
            stops += 1

print(start_position)






