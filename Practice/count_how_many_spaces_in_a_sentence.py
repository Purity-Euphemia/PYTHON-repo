def count_how_many_spaces_in_a_sentence(words):
	letter = 0
	for word in words:
		if word == " ":
			letter += 1
	return letter