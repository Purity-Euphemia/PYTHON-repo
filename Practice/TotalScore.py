total_score = 0
for number in range (1, 11):
	score = int(input(f" enter the student score for student{number}: "))
	total_score += score
	average = total_score / 10


print(f" the total score is {total_score} and the average is {average} ")
