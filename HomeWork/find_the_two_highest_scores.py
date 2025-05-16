counter = 1
score = 0
highest = 0
Name = " "
second_highest = 0
Name2 = " "
number = int(input('Enter the number of student: '))

for value in range(0, number):
	name = input('Enter a name: ')
	score = int(input('Enter a score: '))
	
	if (score > highest):
		highest = score
		Name = name

	if (score > second_highest and score != highest):
		second_highest = score
		Name2 = name


print(Name, "is the highest with score: ", highest)
print (Name2, "is the second_highest with score: ",  second_highest)