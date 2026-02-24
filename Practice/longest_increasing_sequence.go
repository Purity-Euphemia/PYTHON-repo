def longest_increasing_sequence(numbers):
    longest = []
    current = []

    for num in numbers:
        if not current or num > current[-1]:
            current.append(num)
        else:
            current = [num]

        if len(current) > len(longest):
            longest = current

    return longest
