total_score = 0
Score = 0
number = 0
number += 1
while Score != -1:
	Score = int(input(f"Enter the student score for student {number}: "))
	total_score += Score
	average = total_score / number
print(f"The total score is {total_score} and the average is {average} ")