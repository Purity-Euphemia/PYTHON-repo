""" checking for palindrome numbers"""
number = int(input('Enter any five numbers: '))

Number1 = (number // 10000) % 10
Number2 = (number // 1000) % 10
Number3 = (number // 100) % 10
Number4 = (number // 10) % 10
Number5 = (number // 1) % 10

front = Number1, " ", Number2, " ", Number3, " ", Number4, " ", Number5

back = Number5, " ", Number4, " ", Number3, " ", Number2, " ", Number1

if back == front:
	print('The number is palindrome')
else:
	print('The number is not palindrome')