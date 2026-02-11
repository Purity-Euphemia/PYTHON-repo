def is_palindrome2(word):
	correctWord = ""
	for letter in word:
		if letter.isalnum():
			correctWord = correctWord + letter.lower()
	for count in range(len(correctWord) // 2):
		if correctWord[count] != correctWord[-count - 1]:
			return False
	return True


print(is_palindrome("Madam"))
print(is_palindrome("nurses run"))
print(is_palindrome("Hello"))
