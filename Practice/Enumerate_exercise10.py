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
print(cart[0].upper())

print("we have", len(scores), "scores")
scores2 = scores[0:3:2]
x, y = scores2
print(x, y)

for score in scores:
	print(score)

for index in range(len(scores)):
	print(index)

for value in enumerate(cart):
	print(value)

scores.append(99)
scores.pop(1)
cart[4].insert(0, 6)
scores.extend([34, 67, 87, 65])
new_list = cart * 3
print(new_list)

