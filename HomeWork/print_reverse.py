def print_reverse(array):
	new_array = []

	for count in range(len(array)):
		new_array.append(array[len(array) -1 - count])

	return new_array


value = [1, 2, 3, 4, 5, 6]
result = print_reverse(value)
print(result)