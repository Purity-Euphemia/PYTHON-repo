
def Display_Integer_Funtion(number):
	remainder = 0
	sum = 0
	if number <= 0 or number > 10000:
		print("Invalid number")
	else: 
		while (number > 0):
			remainder = number % 10
			sum = sum + remainder
			number = number // 10
	return sum
print(Display_Integer_Funtion(932))