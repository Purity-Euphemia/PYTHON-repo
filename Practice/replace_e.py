def replace_e(word):
    result = ""
    for letter in word:
        if letter == "e":
            result += "*"
        else:
            result += letter
    return result
