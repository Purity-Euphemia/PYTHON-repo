def even_number(numbers):
	even = []
	for count in numbers:
		if count % 2 == 0:
			even.append(count)
	return even


even = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_number(even))