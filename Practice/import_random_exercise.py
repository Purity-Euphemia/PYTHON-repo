import random
random.seed(10)

for number in range(20):
	print('H' if random.randrange(2) == 0 else 'T', end=' ')