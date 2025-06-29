scores = []
for count in range(10):
    score = int(input("Enter score: "))
    scores.append(score)

total = 0
for count in scores:
    total += count

print("Total sum:", total)