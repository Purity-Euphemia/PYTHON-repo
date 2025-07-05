def average(*args):
    average = 0
    for number in args:
        average += number
        average /= 2
    return average

print(average(10,20,30,40))