def team_lineup(*args):
    dictionary = {}
    result = ""

    for football_name, country in args:
        if country not in dictionary.keys():
            dictionary[country] = []
        dictionary[country].append(football_name)

    sorted_dictionary = sorted(dictionary.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for football_country, names in sorted_dictionary:
        result += f"{football_country}:\n"
        for name in names:
            result += f"  -{name}\n"

    return result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))

