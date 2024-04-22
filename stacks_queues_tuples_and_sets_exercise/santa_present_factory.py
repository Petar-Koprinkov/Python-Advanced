from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

present = {
    150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}

crafted_present = {}

while materials and magic:
    result = materials[-1] * magic[0]

    if result in present:
        new_toy = present[result]
        if new_toy not in crafted_present:
            crafted_present[new_toy] = 0
        crafted_present[new_toy] += 1
        materials.pop()
        magic.popleft()

    elif result < 0:
        materials.append(materials.pop() + magic.popleft())

    elif result > 0:
        magic.popleft()
        materials[-1] += 15

    elif materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()

    elif materials[-1] == 0:
        materials.pop()

    elif magic[0] == 0:
        magic.popleft()

if ("Doll" in crafted_present and "Wooden train" in crafted_present) or \
        ("Teddy bear" in crafted_present and "Bicycle" in crafted_present):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for key, value in sorted(crafted_present.items()):
    print(f"{key}: {value}")









