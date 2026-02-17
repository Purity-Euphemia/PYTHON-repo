def counts_consonants(words):
	count = 0
	letter = "aeiouAEIOU"
	for char in words:
		if char.isalpha() and char not in vowels:
			letter += 1
	return letter
	