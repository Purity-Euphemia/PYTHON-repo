princpal = 0;


princpal = int(input('Enter a princpal: '))
rate = int(input('Enter a annual rate: '))
year = int(input('Enter a number of years: '))

monthRate = rate / 1200
 
for year in range(1, 31):
	amount = princpal * (1 + monthRate) ** year
	print(amount)