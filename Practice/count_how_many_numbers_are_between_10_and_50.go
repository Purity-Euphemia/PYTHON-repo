def count_how_many_numbers_are_between_10_and_50(numbers):
	counter = 0
	for count in numbers:
		if count  > 10 and count < 50:
			counter += 1
	return counter