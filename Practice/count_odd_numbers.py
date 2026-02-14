def count_odd_numbers(numbers):
	counter = 0
	for num in numbers:
		if num % 2 != 0:
			counter += 1
	return counter
