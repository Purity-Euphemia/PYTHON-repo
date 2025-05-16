numbers = 0
def get_product(* numbers):
	print ("this is the tuples", numbers)
	product = 1
	return product
	
for number in numbers:
	print("number in the loop", number)
	product *= numbers
	

print(get_product(3, 6, 5, 6, 7))
print (get_product(4, 3, 7, 9, 10, 15, 23, 21, 12, 45))

