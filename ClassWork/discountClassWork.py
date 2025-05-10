amount = int(input('Enter a spending: '))

if amount >= 1000 and amount < 10000:
	discount = amount * 0.05
	print('The discount: ', discount)

if amount >= 10000 and amount < 50000:
	discount = amount * 0.10
	print('The discount: ', discount)

if amount >= 50000:
	discount = amount * 0.20
	print('The discount: ', discount)

price_after_discount = amount - discount
print(f'The amount is: {price_after_discount:,.2f}')