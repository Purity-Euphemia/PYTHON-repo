import random
print('Guess my number')
computer = random.randrange (1, 11)

while True:
	num = int(input('Enter a number: '))
	if (num < 1 or num > 10):
		print('invalid number')
	elif(num == computer):
		print('correct')
		print('Congratulation')
		break

	elif(num > computer):
		print('Too high')

	elif(num < computer):
		print('Too low')

answer = int(input('press 1 to continue or 0 to quit: '))
if answer == 0:
	print('Thanks for playing')

elif answer == 1:
	computer = random.randrange (1, 11)
	print('\nNew game started!')
else:
	print('invalid input, qutting game')
			