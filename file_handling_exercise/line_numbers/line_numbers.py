from string import punctuation

with open("text.txt", "r") as first_file, open("output.txt", "w") as second_file:
    for row_index, text_line in enumerate(first_file, start=1):
        letters_count = 0
        punctuations_count = 0
        for char in text_line:
            if char.isalpha():
                letters_count += 1
            elif char in punctuation:
                punctuations_count += 1

        second_file.write(f"Line {row_index}: {text_line.strip()} ({letters_count})({punctuations_count})\n")

