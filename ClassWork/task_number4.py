import random;
numbers = []
for count in range(11):
        numbers.append(random.randrange(1, 51));
sum_odd_numbers = 0
for count in numbers:
    if count % 2 == 1:
        sum_odd_numbers += count

print("Sum of odd numbers:", sum_odd_numbers)

