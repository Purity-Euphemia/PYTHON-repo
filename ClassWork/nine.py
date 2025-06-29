total = 0

for count in range(10):
    score = int(input("Enter score: "))
    if 0 <= score <= 100:
        total += score

print("Sum of valid scores:", total)