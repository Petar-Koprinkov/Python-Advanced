from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption_index = deque(int(x) for x in input().split())
amount_of_fuel_needed = deque(int(x) for x in input().split())
altitude = 0
goal = []


while initial_fuel and additional_consumption_index and amount_of_fuel_needed:
    current_initial_fuel = initial_fuel.pop()
    current_index = additional_consumption_index.popleft()
    current_fuel_needed = amount_of_fuel_needed[0]
    result = current_initial_fuel - current_index

    if result < current_fuel_needed:
        altitude += 1
        print(f"John did not reach: Altitude {altitude}")
        break
    elif result >= current_fuel_needed:
        altitude += 1
        print(f"John has reached: Altitude {altitude}")
        goal.append(f"Altitude {altitude}")
        amount_of_fuel_needed.popleft()

if amount_of_fuel_needed and goal:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(goal)}")
elif amount_of_fuel_needed and not goal:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
elif not amount_of_fuel_needed:
    print("John has reached all the altitudes and managed to reach the top!")








