def age_assignment(*args, **kwargs):
    result = {}
    total_result = ''
    for name in args:
        for key, value in kwargs.items():
            if key == name[0]:
                result[name] = value
    result = sorted(result.items(), key=lambda kvp: kvp[0])

    for name, age in result:
        total_result += f"{name} is {age} years old.\n"

    return total_result


print(age_assignment("Peter", "George", G=26, P=19))
print()
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
