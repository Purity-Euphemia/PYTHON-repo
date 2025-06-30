from tkinter.font import names


def covert_numbers_to_words(words):
    keys = {}

    for letter in words:
        if letter in keys:
            keys[letter] += 1
        else:
            keys[letter] = 1

    return keys



print(covert_numbers_to_words('google'))


