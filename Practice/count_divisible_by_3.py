def count_divisible_by_3(numbers):
    counter = 0
    for num in numbers:
        if num % 3 == 0:
            counter += 1
    return counter
