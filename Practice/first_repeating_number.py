def first_repeating_number(numbers):
    seen = []
    for num in numbers:
        if num in seen:
            return num
        seen.append(num)
    return None
