def is_palindrome_full(word):
	for count in range(len(word) // 2):
		if word[count] != word[-count - 1]:
			return False
	return True