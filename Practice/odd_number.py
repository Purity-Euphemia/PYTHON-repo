def odd_number():
	for number in range(0, 10, 2):
		if number % 2 == 1:
			return number


print(odd_number())