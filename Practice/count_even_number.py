def count_even_numbers(numbers)
	counter = 0
	for count in numbers:
		if count % 2 == 0:
			counter += 1
	return counter