def total_characters(words):
    count = 0
    for word in words:
        count += len(word)
    return count
