import math

number = 10
value = 0.0

for count in range(number):
	value = value + (1) / math.factorial(count)
	
constant = value * 4
print(constant)