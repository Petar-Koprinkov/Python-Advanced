from collections import deque

quantity = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

while orders and quantity >= orders[0]:
    quantity -= orders.popleft()

if not orders:
    print(f"Orders complete")
else:
    print(f"Orders left:", *orders, sep=' ')
