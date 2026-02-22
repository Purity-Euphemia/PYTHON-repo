def count_four_letter_words(words):
    count = 0
    for word in words:
        if len(word) == 4:
            count += 1
    return count
