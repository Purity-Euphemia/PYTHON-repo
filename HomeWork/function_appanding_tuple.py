def appending_tuple(number):
    value = []
    for count in number:
        value.append (count)
    return value

numbers = [1,2,3,4,5]
numbers.extend([6,7])
result = appending_tuple(numbers)
print(result)
