def mystery(number):
    value = 0
    for count in range(number):
        value += number ** 2
    return value



print(mystery(10))