def sum_greater_than_10(numbers):
    total = 0
    for num in numbers:
        if num > 10:
            total += num
    return total
