def even_odd(*args):

    sign = args[-1]
    even_list = []
    odd_list = []

    if sign == "even":
        for num in args[:-1]:
            if num % 2 == 0:
                even_list.append(num)
        return even_list
    elif sign == "odd":
        for num in args[:-1]:
            if num % 2 != 0:
                odd_list.append(num)
        return odd_list


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))