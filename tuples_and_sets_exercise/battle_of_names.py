n = int(input())
even_set = set()
odd_set = set()

for row in range(1, n + 1):
    name = input()

    result = sum([ord(char) for char in name]) // row

    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

even_set_sum = sum(even_set)
odd_set_sum = sum(odd_set)

if even_set_sum == odd_set_sum:
    total_result = odd_set.union(even_set)
elif even_set_sum < odd_set_sum:
    total_result = odd_set.difference(even_set)
elif even_set_sum > odd_set_sum:
    total_result = odd_set.symmetric_difference(even_set)

print(*total_result, sep=", ")
