def count_how_many_sentences_in_a_paragraph(words):
	counter = 0
	for count in words:
		if count == ".":
			counter += 1
	return counter
	