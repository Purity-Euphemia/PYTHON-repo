import random
numbers = []

for count in range(1, 11):
	numbers.append(random.randrange(1, 51));

sum = 0
length = 0

for count in numbers:
	length += 1
	sum += count
	
average = sum / length

print(numbers)	
print("Average of the numbers: ", average)

	


