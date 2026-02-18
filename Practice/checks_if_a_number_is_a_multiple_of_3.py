def checks_if_a_number_is_a_multiple_of_3(numbers):
	counter = 0
	for count in numbers:
		if count % 3 == 0:
			counter += 1
	return counter		