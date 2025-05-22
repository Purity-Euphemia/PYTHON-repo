def categorize_numbers(numbers, divisible_by):

	divisible_numbers = []

	for num in numbers:
		if num % divisible_by == 0:
			divisible_numbers.append(num)

	if divisible_numbers:
		return divisible_numbers
	else:
		return "No divisible number found"
	

print(categorize_numbers({15, 21, 30, 10}, -3))