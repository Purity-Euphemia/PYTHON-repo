def Maxi(numbers):
	max = numbers[0]
	for number in numbers:
		if number > max:
		max = number	


	return max


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(Maxi(list))
	