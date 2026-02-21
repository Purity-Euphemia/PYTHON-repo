def remove_empty_strings(words):
    result = []
    for word in words:
        if word != "":
            result.append(word)
    return result
