import random


def random_number_generator(numbers):
    counter = 0
    random_number = random.randint(1, 1001)
    if number < random_number:
        return "too low" + " try again"
    elif number > random_number:
        return "too high" + " try again"
    else:
            return "win"


for number in range(3):
    number = int(input("Enter a number: "))
    print(random_number_generator(number))