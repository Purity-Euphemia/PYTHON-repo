scores = []
for count in range(10):
    score = int(input("Enter a score: "))
    scores.append(score)

sum_even_numbers = 0
for count in scores:
    if count % 2 == 0:
        sum_even_numbers += count

print("Sum of even numbers:", sum_even_numbers)