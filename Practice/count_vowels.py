def count_vowels(word):
	count = 0
	for letter in word:
		if letter.isalpha():
			if letter.lower() in "aeiou":
				count += 1
	return count