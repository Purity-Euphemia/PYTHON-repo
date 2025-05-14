
number1 = int(input('Enter a number: '))
number2 = int(input('Enter a number: '))
number3 = int(input('Enter a number: '))

number1 = number1**2
number2 = number2**2
number3 = number3**2

if number1 + number2 == number3:
	print('This is an example of "brute_force" computing')
else:
	print('This is not')
