def count_uppercase(sentence):
    count = 0
    for char in sentence:
        if char.isupper():
            count += 1
    return count
