score = int(input("Enter your score: "))
if type (score) == int:
	if score >= 49 and score <= 100:
		print("You pass")
		print("Your score is", score)
	elif score > 0 and score <= 49:
		print("You fail")
		print("Your score is", score)
	else:
		print("invalid score")
else:
	print("invalid type")