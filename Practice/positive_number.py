def positive_number(numbers):
	count = 0
	for counter in numbers:
		if counter > 0:
			return "positive"
		elif counter < 0:
			return "negative"
		else:
			return "Zero"
