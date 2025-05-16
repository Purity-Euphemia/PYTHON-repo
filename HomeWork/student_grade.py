
counter = 1
score = 0
highest = 0
Name = " "

number = int(input('Enter the number of student: '))

for value in range(0, number):
	name = input('Enter a name: ')
	score = int(input('Enter a score: '))
	
	if (score > highest):
		highest = score
		Name = name



print(Name, "is the highest with score: ", highest)