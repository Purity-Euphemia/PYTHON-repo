remainder = 0
sum = 0
	
number = int(input("Enter an number between 1 to 10000: "))
if number <= 0 or number > 10000:
	print("Invalid number")
else: 
	while (number > 0):
		remainder = number % 10
		sum = sum + remainder
		number = number // 10
	

	print(f"The sum of the number: {sum}")