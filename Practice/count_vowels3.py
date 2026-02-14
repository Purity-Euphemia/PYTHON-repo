def count_vowels(word):
	counter = 0
	for letter in word.lower():
		if letter in "aeiou":
			counter += 1
	return counter
