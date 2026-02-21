def count_words_with_a(words):
    count = 0
    for word in words:
        if "a" in word.lower():
            count += 1
    return count
