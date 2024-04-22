def movie_organizer(*args):
    result = ''
    dictionary = {}
    for movie, genre in args:
        if genre not in dictionary:
            dictionary[genre] = []
        dictionary[genre].append(movie)

    sorted_dictionary = sorted(dictionary.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for genre, movies in sorted_dictionary:
        result += f"{genre} - {len(movies)}\n"
        for movie in sorted(movies):
            result += f"* {movie}\n"

    return result


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

