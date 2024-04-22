from collections import deque

line = deque(input().split(" "))
main_colours = ['red',
                'yellow',
                'blue',
                ]
secondary_colours = {'orange': ['red', 'yellow'],
                     'purple': ['red', 'blue'],
                     'green': ['blue', 'yellow'],
                     }
collected_colours = []

while line:
    first_string = line.popleft()
    last_string = line.pop() if len(line) > 0 else ""

    if first_string + last_string in main_colours or first_string + last_string in secondary_colours:
        collected_colours.append(first_string + last_string)
    elif last_string + first_string in main_colours or last_string + first_string in secondary_colours:
        collected_colours.append(last_string + first_string)
    else:
        if len(first_string) > 1:
            line.insert(len(line) // 2, first_string[:-1])
        if len(last_string) > 1:
            line.insert(len(line) // 2, last_string[:-1])

for colour in collected_colours:
    if colour in secondary_colours:
        for el in secondary_colours[colour]:
            if el not in collected_colours:
                collected_colours.remove(colour)

print(collected_colours)





