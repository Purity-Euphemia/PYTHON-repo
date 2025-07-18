def string_function(word, value="ce"):
    if(len(word) % 2 == 0):
        middle = len(word)//2
        word = word[:middle] + value + word[middle:]
        return word
    else:
        return word + value

#print(string_function("helloo"))