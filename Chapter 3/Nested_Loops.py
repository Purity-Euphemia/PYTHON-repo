largest = 0
second_largest = 0
for number in range (1, 11):
	number = int(input('Enter a number: '))
	if (number > largest):
		second_largest = largest
		largest = number
		
	if (number > second_largest and number != largest):
		second_largest = number

print ('largest', + largest)
print ('second_largest', + second_largest)