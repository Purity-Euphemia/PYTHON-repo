def count_how_many_times_the_letter_e_appers(words):
	counter = 0
	for count in words:
		if count == "e":
			counter += 1
	return counter