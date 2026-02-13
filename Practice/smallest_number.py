def smallest_number(numbers):
	smallest = numbers[0]
	for count in numbers:
		if count < smallest:
			smallest = count
	return smallest