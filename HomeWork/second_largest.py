def second_largest(array):
    largest = 0
    second_largest = 0

    for count in range(len(array)):
        if array[count] > largest:
            second_largest = largest
            largest = array[count]
        elif array[count] > second_largest and array[count] != largest:
            second_largest = array[count]

    return second_largest


value = [10, 38, 78, 90, 4, 57, 22, 100]
print("Second largest:", second_largest(value))
