def adds_the_length_of_only_words_longer_than_3_characters(words):
	count = 0
	for word in words:
		if len(word) > 3:
			count += len(word)
	return count