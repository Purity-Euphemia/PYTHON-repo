def even_count(array):
    even = 0
    for num in array:
        if num % 2 == 0:
            even += 1
    return even

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_count(values)

print("Number of even elements:", result)
