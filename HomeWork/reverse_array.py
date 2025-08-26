def reverse_array(arr):
    result = [0] * len(arr)

    for count in range(len(arr)):
        result[count] = arr[len(arr) - count - 1]

    return result

numbers = [1, 2, 3, 4, 5, 6]
print(reverse_array(numbers))  