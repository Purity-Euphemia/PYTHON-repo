number1 = int(input('Enter the purchase price of a dollar: '))
number2 = int(input('Enter the amount paid: '))

subtract = number2 - number1

quarters = subtract / 25 
print("your quarters: ", + quarters)

dimes = subtract / 10 
print("your dimes: ", + dimes)

nickels = subtract / 5 
print("your nickels: ", + nickels)

pennies = subtract / 1 
print("your pennies: ", + pennies)
