def unique_characters(text):
    result = ""
    for char in text:
        if char not in result:
            result += char
    return result
