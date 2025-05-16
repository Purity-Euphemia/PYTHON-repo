password = input("Enter a password: ")

for number in range(8,16):

	counter = 0

for number in password:
	counter += 1
	
if counter < 8:
	print("very weak")
elif counter == 8:
	print("weak")
elif counter > 8 and counter < 16:
	print("strong")
elif counter > 16:
	print("very strong")

	