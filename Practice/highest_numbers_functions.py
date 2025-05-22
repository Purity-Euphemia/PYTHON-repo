def highest_numbers_functions(numbers, divisible_by):

	highest_numbers = []

	for num in numbers:
		if num % divisible_by == 0:
			highest_numbers.append(num)

		if num < highest_numbers:
			return highest_numbers
		else:
			return "No divisible number found"
	

print(highest_numbers_functions({15, 21, 30, 10}, -3))