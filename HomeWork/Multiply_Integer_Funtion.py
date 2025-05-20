def Multiply_Integer_Funtion(number1, number2):
	total = 0;
	if number1 <= 0 and number2 <= 0:
		print("Invalid number")
	else: 
		for number in range (0, number2):
			total = total + number1 
	return total
print(Multiply_Integer_Funtion(4, -9))