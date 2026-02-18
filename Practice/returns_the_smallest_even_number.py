def returns_the_smallest_even_number(numbers):
    smallest = None
    for count in numbers:
        if count % 2 == 0:
            if smallest is None or count < smallest:
                smallest = count
    return smallest
