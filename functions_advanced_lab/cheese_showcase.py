def sorting_cheeses(**kwargs):
    result = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    total = ""

    for name, quantity in result:
        total += f"{name}\n"
        quantity = sorted(quantity, reverse=True)
        total += "\n".join(str(el) for el in quantity)
        total += "\n"
    return total


print(sorting_cheeses(Parmesan=[102, 120, 135], Camembert=[100, 100, 105, 500, 430], Mozzarella=[50, 125],))
