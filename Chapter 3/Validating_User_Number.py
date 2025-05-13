passes = 0
failure = 0
count = 1
value = 0

for number in range(10):
	value = int(input('Enter an integer 1 and 2: '))

	if value == 1:
		passes = passes + 1
	else:
		failure = failure + 1

print("number of passes: ", passes)
print("number of failure: ", failure)
