from collections import deque

quantity_of_water = int(input())
name = input()
name_queue = deque()

while name != "Start":
    name_queue.append(name)

    name = input()

data = input().split()

while data[0] != "End":
    if len(data) == 1:
        data = int(data[0])
        if quantity_of_water >= data:
            quantity_of_water -= data
            print(f"{name_queue.popleft()} got water")
        else:
            print(f"{name_queue.popleft()} must wait")

    elif len(data) == 2:
        add_water = int(data[1])
        quantity_of_water += add_water

    data = input().split()

print(f"{quantity_of_water} liters left")

