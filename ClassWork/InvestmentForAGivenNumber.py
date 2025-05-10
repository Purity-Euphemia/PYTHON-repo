investment_amount = 0

investment_amount = int(input('Enter a investment amount: '))
interest_rate = int(input('Enter a annual rate: '))
year = int(input('Enter a number of years: '))

monthRate = interest_rate / 100
 
for year in range(1, year+1):
	amount = investment_amount * (1 + monthRate) ** year
	print(f'amount:{amount:,.2f}')