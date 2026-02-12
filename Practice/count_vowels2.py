def count_vowels2(word):
	counter = 0
	for count in word:
		if count in "aeiou":
			counter += 1
	return counter