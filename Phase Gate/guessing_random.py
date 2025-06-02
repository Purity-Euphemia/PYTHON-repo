import random;


for counter in range (1, 11):

	substract_one = random.randrange(1, 100);
	substract_two = random.randrange(1, 100);

print(f"what is {substract_one} - {substract_two}");

userInput = input("what is ?");

result = substract_one - substract_two;

counter1 = 0;
counter2 = 0;
if (userInput != result):
	counter1 = counter1 + 1
	print("invalid number")
	


if (userInput == result):
	counter2 = counter + 2
	print("correct")
	


	
	
print(f"the number of correct input{counter1}")
print(f"the number of wrong input{counter2}")