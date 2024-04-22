def even_odd_filter(**kwargs):
    for key, value in kwargs.items():
        if key == "even":
            kwargs[key] = [x for x in value if x % 2 == 0]
        elif key == "odd":
            kwargs[key] = [x for x in value if x % 2 != 0]

    result = sorted(kwargs.items(), key=lambda kvp: -len(kvp[1]))
    return dict(result)



print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
