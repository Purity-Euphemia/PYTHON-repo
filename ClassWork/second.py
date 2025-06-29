scores = []
for count in range(10):
    score = int(input("Enter a score: "))
    scores.append(score)

total = 0
for count in scores:
    total += count

average = total / 10
print("Average:", average)