text = tuple(input())
my_dict = {}

for element in text:
    if element not in my_dict:
        my_dict[element] = 0
    my_dict[element] += 1

for key, value in sorted(my_dict.items()):
    print(f"{key}: {value} time/s")