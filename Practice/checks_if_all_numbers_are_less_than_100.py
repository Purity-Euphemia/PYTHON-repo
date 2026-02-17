def checks_if_all_numbers_are_less_than_100(numbers):
	for count in numbers:
		if count >= 100:
			return True
		else:
			return False