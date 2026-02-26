def count_spaces_and_tabs(text):
    count = 0
    for char in text:
        if char == " " or char == "\t":
            count += 1
    return count
