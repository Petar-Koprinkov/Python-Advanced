def negative_positive(*args):
    positive_numbers = 0
    negative_numbers = 0
    for num in args:
        if num >= 0:
            positive_numbers += num
        else:
            negative_numbers += num

    return positive_numbers, negative_numbers


number = [int(x) for x in input().split()]

print(negative_positive(*number)[1])
print(negative_positive(*number)[0])

if abs(negative_positive(*number)[0]) > abs(negative_positive(*number)[1]):
    print("The positives are stronger than the negatives")
elif abs(negative_positive(*number)[1]) > abs(negative_positive(*number)[0]):
    print("The negatives are stronger than the positives")