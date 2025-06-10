"""
student_score1 = 50
student_score1 = 50
student_score1 = 50
student_score1 = 50
"""

#do this
#	  0   1   2   3    4
scores = [50, 34, 45, 50, 25]

cart = ['banana', 33, 'juice', 2.5, ["fish", "palm oil"], True]
print(cart[4][1])

print("we have", len(scores), "scores")
scores2 = scores[0:3:2]
x, y = scores2
print(x, y)

for score in scores:
	print(score)

for index in range(len(scores)):
	print(index)

for value, number in enumerate(cart):
	print(value, number)