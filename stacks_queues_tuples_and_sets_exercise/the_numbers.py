first_line = set([int(x) for x in input().split()])
second_line = set([int(x) for x in input().split()])
n = int(input())

for i in range(n):
    data = input().split()
    command = data[0] + " " + data[1]
    number = [int(x) for x in data[2:]]

    if command == "Add First":
        first_line.update(number)
    elif command == "Add Second":
        second_line.update(number)
    elif command == "Remove First":
        first_line.difference_update(number)
    elif command == "Remove Second":
        second_line.difference_update(number)
    elif command == "Check Subset":
        print(first_line.issubset(second_line) or second_line.issubset(first_line))

first_line = sorted(first_line)
second_line = sorted(second_line)

print(*first_line, sep=", ")
print(*second_line, sep=", ")



