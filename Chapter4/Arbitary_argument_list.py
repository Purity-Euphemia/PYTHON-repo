def Multipication(*args):
	product = 1
	for value in args:
		product = product * value
	return product

print(Multipication(5, 10, 15))