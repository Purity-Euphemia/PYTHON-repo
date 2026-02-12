def is_palindrome3(word):
	correctWord = ""
	for letter in word:
		if letter.isalnum():
			correctWord = correctWord + letter.lower()
	for count in range(len(correctWord) // 2):
		if correctWord[count] != correctWord[- count - 1]:
			return False
	return True