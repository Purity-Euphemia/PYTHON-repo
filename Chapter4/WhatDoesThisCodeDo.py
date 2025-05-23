def mystery(number):
	count = 0
	for value in number:
		count = count + value ** 2
	return count