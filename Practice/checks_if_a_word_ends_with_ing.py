def checks_if_a_word_ends_with_ing(words):
	count = 0
	for counter in words:
		if counter[-3:] == "ing":
			count += 1
	return count