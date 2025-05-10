sum = 0
average = 0
product = 1
smallest = 0
largest = 0

for number in range(4):
	numbers = int(input('Enter a number: '))
	sum = sum + numbers
	product = product * numbers

average = sum / 4

if numbers > largest:
	largest = numbers

if numbers != largest:
	largest = smallest
	smallest = numbers

print ('the sum: ', sum)
print ('the average: ', average)
print ('the product: ', product)
print ('the largest: ', largest)
print ('the smallest: ', smallest)

