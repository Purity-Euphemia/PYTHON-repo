import random;
numbers = []
for count in range(11):
        numbers.append(random.randrange(1, 51));
sum_even_numbers = 0
for count in numbers:
    if count % 2 == 0:
        sum_even_numbers += count

print("Sum of even numbers:", sum_even_numbers)

