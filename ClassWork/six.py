scores = []
for count in range(10):
    score = int(input("Enter a score: "))
    scores.append(score)

total = 0  # Sum of even numbers
count = 0  # Count of even numbers

for count in scores:
    if count % 2 == 0:
        total += count
        count += 1

if count != 0:
    average = total / count
    print("Average of even numbers:", average)
else:
    print("No even numbers entered.")