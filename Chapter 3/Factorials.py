factorial = 1

number = int(input("Enter a nonnegative integer: "))

if (number < 0):
	print("Wrong number")
else:
	for value in range(1, number + 1):
		factorial = factorial * value

print(f'the factorial: ', factorial)

	



