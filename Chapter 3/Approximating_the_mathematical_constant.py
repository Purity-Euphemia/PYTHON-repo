number = 1000000
value = 0.0

for count in range(number):
	value = value + (-1) ** count / (2 * count + 1)
	
constant = value * 4
print(constant)