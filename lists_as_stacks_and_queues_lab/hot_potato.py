from collections import deque

names = deque(input().split())
n = int(input()) # or - 1

while len(names) != 1:
    names.rotate(-n + 1) # or - 1 in "n = int(input) - 1"
    print(f"Removed {names.popleft()}")

print(f"Last is {''.join(names)}")


