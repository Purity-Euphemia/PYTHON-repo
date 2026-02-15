def to_uppercase(word):
    result = ""
    for letter in word:
        result += chr(ord(letter) - 32)
    return result
