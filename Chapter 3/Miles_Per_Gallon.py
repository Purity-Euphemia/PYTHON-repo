total = 0
division = 0
number_count = 0
count = 0


gallons = float(input('Enter the gallon used (-1 to end): '))
milesdriven = float(input('Enter the milesdriven: '))

while count != -1:
	division = milesdriven / gallons
	total = total + division
	number_count += 1
	number = int(input('Enter a number to keep on going 0R -1 to quit: '))

	print('The miles per gallon: ', division)
	print('The total gallon used: ', total)

	