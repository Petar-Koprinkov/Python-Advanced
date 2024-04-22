from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(x) for x in input().split(", "))
milkshakes = 0

while milkshakes < 5 and chocolates and cups_of_milk:

    if chocolates[-1] <= 0 and cups_of_milk[0] <= 0:
        chocolates.pop()
        cups_of_milk.popleft()
        continue

    elif chocolates[-1] <= 0:
        chocolates.pop()
        continue

    elif cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue

    if len(chocolates) > 0 and len(cups_of_milk) > 0:

        first_chocolate = chocolates.pop()
        last_milk = cups_of_milk.popleft()

        if first_chocolate == last_milk:
            milkshakes += 1
        else:
            cups_of_milk.append(last_milk)
            chocolates.append(first_chocolate - 5)
    else:
        break

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")
else:
    print("Milk: empty")
