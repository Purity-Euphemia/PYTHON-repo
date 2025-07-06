def cube_list(values):
    for count in range(len(values)):
        values[count] **= 3
    return values

values = [1, 2, 3, 4, 5,6,7,8,9,10]
result = cube_list(values)
print(result)