def count_greater_than_average(numbers):
    average = sum(numbers) / len(numbers)
    count = 0
    for num in numbers:
        if num > average:
            count += 1
    return count
