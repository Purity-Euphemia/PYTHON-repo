scores = []
for count in range(10):
    score = int(input("Enter a score: "))
    scores.append(score)

sum_even_positions = 0
for count in range(1, 10, 2):  # 2nd, 4th, 6th, 8th, 10th (index 1,3,5,7,9)
    sum_even_positions += scores[count]

print("Sum at even positions:", sum_even_positions)