def return_the_first_number_divisible_by_7(numbers):
	counter = 0
	for count in numbers:
		if count % 7 == 0:
			return count