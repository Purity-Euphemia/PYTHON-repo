amount = input('Enter the principle: ')
amount = int(amount)

annual = input('Enter the annual rate: ')
annual = int(annual)
rate = annual / 1200

number = input('Enter the number of years: ')
number = int(number)

result = amount * (1 + rate) ** number

print(result)