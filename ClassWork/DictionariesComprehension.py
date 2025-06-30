def covert_numbers_to_words(words):
    return {letter: words.count(letter) for letter in words}


print(covert_numbers_to_words('google'))