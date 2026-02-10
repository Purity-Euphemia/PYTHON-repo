def is_palindrome(word):
	correctWord = ""
	for count in word:
		correctWord = correctWord.lower()
	for count in range(len(correctWord) // 2):
		if correctWord[count] != correctWord[- count - 1]:
			return False
		return True

print(is_palindrome("level"))
print(is_palindrome("hello"))
