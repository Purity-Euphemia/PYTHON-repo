def is_palindrome_ignore_case(word):
    word = word.lower()
    return word == word[::-1]
