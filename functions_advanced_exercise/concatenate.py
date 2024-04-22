def concatenate(*args, **kwargs):
    text = ""
    for string in args:
        text += string

    for key, value in kwargs.items():
        if key in text:
            text = text.replace(key, value)

    return text