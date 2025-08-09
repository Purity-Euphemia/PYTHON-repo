
def array_function(numbers):
	value = []
	for number in numbers:
		value.append(number * 4)
	return value

value = [1, 2, 3, 4, 5, 6]
print(array_function(value))