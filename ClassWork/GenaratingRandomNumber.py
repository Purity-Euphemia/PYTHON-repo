import random;
counter1 = 0;
counter2 = 0;

for counter in range(1, 11):
	substractOne = random.randrange(1, 101);
	substractTwo = random.randrange(1, 101);

	for count in range(1, 3):
		print("what is ", substractOne, " - ", substractTwo);
		userInput = input()

		result = substractOne - substractTwo;

		if (userInput != result):
			print("incorrect answer");
			counter1 += 1;
	
		if (userInput == result):
			print("correct")
			counter2 += 1
			break;


	
	
print("the number of correct input", counter1)
print("the number of wrong input", counter2)