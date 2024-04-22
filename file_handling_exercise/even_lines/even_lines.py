symbols = "-,.!?"

with open("text.txt", "r") as file:
    for row_index, text_line in enumerate(file.readlines()):
        if row_index % 2 == 0:
            for char in text_line:
                if char in symbols:
                    text_line = text_line.replace(char, "@")
            print(" ".join(reversed(text_line.split())))

