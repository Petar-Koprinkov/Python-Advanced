from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
honey_making_process = deque(x for x in input().split())
honey = 0

while working_bees and nectar:
    matched_bee = working_bees.popleft()
    matched_nectar = nectar.pop()
    symbol = honey_making_process.popleft()

    if symbol == "/" and matched_nectar == 0:
        continue

    while matched_nectar < matched_bee:
        if nectar:
            matched_nectar = nectar.pop()
        else:
            working_bees.appendleft(matched_bee)
            break

    if matched_bee <= matched_nectar:
        if symbol == "+":
            honey += abs(matched_bee + matched_nectar)
        elif symbol == "-":
            honey += abs(matched_bee - matched_nectar)
        elif symbol == "*":
            honey += abs(matched_bee * matched_nectar)
        elif symbol == "/":
            honey += abs(matched_bee / matched_nectar)

print(f"Total honey made: {honey}")

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
