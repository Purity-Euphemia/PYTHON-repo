total = 0
count = 0

for count in range(10):
    score = int(input("Enter score: "))
    if 0 <= score <= 100:
        total += score
        count += 1

print("Sum of valid scores:", total)

if count != 0:
    average = total / count
    print("Average of valid scores:", average)
else:
    print("No valid scores entered.")