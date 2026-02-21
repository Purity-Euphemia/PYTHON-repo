def index_of_largest(numbers):
    largest = numbers[0]
    index = 0
    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
            index = i
    return index
