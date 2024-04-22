import os

dictionary = {}
directory = "../"


def info(folder):
    for doc in os.listdir(folder):
        file = os.path.join(folder, doc)
        if os.path.isfile(file):
            extension = doc.split(".")[-1]
            if extension not in dictionary:
                dictionary[extension] = []
            dictionary[extension].append(doc)
        else:
            info(file)


info(directory)

with open(os.path.join(directory, "output.txt"), "w") as output_file:
    for ext, file_name in sorted(dictionary.items()):
        output_file.write(f".{ext}\n")
        for name in sorted(file_name):
            output_file.write(f"- - -{name}\n")

