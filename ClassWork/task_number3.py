import random;
numbers = []
for count in range(1, 11):
	numbers.append(random.randrange(1, 51));

length = 0
for count in numbers:
	length += 1

print("Length:", length)