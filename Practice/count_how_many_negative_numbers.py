def count_how_many_negative_numbers(numbers):
	counter = 0
	for count in numbers:
		if count < 0:
			counter += 1
	return counter