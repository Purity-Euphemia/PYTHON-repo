def count_positive_and_negative(arr):
    positive_count = 0
    negative_count = 0

    for count in range(len(arr)):
        if arr[count] > 0:
            positive_count += 1
        elif arr[count] < 0:
            negative_count += 1

    print("Number of Positive Values:", positive_count)
    print("Number of Negative Values:", negative_count)


numbers = [3, -2, 0, 5, -1, 7, -6, 0]
count_positive_and_negative(numbers)
