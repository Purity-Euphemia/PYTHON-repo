def categorize_numbers(*numbers, divisible_by=5):
total = []
count = 0
for number in numbers:
	if number % divisible_by == 0:
		total = total + [number]
		count = count + 1
	if count == 0:
		return "No divisible number found"
	else:
		return total