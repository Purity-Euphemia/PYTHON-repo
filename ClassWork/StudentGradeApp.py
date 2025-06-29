students = int(input("How many students? "))
subjects = int(input("How many subjects? "))


scores = []

for count in range(students):
	print(F"\nEntring scores for student {count + 1}")
	student_scores = []


	for counter in range(subjects):
		while True:
			score = int(input(f"Enter score for subject {counter + 1}: "))
			if 0 <= score <= 100:
				student_scores.append(score)
				break
			else:
				print("Score must be between 0 and 100. try again.")

	scores.append(student_scores)



print("\n--- Class Summary ---")

for count in range(students):
	total = sum(scores[counter])
	average = total / subjects
	print(f"Student {count + 1}: Total = {total}, Average = {average:.2f}")