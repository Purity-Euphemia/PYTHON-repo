def adds_only_numbers_greater_than_50(numbers):
	counter = 0
	for count in numbers:
		if count > 50:
			counter += count
	return counter