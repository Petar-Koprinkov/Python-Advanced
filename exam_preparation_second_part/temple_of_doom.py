from collections import deque

tools = deque(int(x) for x in input().split())
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances and challenges:
    current_tool = tools.popleft()
    current_substance = substances.pop()
    result = current_tool * current_substance

    if result in challenges:
        challenges.remove(result)
    elif result not in challenges:
        current_tool += 1
        tools.append(current_tool)
        current_substance -= 1
        if current_substance == 0:
            continue
        else:
            substances.append(current_substance)

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")