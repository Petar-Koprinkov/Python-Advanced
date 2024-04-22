def accommodate_new_pets(available_capacity, maximum_weight, *args):
    result = []
    dictionary = {}
    for pet_type, pet_weight in args:

        if available_capacity <= 0:
            result += f"You did not manage to accommodate all pets!"
            break
        if pet_weight > maximum_weight:
            continue
        if pet_type not in dictionary:
            dictionary[pet_type] = 0
        dictionary[pet_type] += 1
        available_capacity -= 1
    else:
        result.append(f"All pets are accommodated! Available capacity: {available_capacity}.")

    result.append(f"Accommodated pets:")

    for pet, count in sorted(dictionary.items()):
        result.append(f"{pet}: {count}")

    return "\n".join(result)


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))


