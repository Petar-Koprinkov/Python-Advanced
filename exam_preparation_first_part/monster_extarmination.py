from collections import deque

monsters_armor = deque(int(x) for x in input().split(","))
soldier_strikes = [int(x) for x in input().split(",")]

killed_monsters = 0
remaining_monster = len(monsters_armor)

while monsters_armor and soldier_strikes:
    current_monster = monsters_armor.popleft()
    current_soldier = soldier_strikes.pop()
    if current_soldier >= current_monster:
        current_soldier -= current_monster
        killed_monsters += 1
        if soldier_strikes:
            soldier_strikes[-1] += current_soldier
        else:
            if current_soldier != 0:
                soldier_strikes.append(current_soldier)
    elif current_monster > current_soldier:
        current_monster -= current_soldier
        monsters_armor.append(current_monster)

if killed_monsters == remaining_monster:
    print("All monsters have been killed!")

if not soldier_strikes:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")