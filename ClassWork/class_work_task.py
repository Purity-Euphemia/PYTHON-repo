import random
numbers = []


def genarate_random_numbers():
    for count in range(1, 11):
        number = random.randint(1, 51)
        numbers.append(number)
    print(numbers)


def length_of_list():
    length = 0
    for number in numbers:
        length += 1
    return length

def generate_even_numbers():
        sum = 0
        count = 0
        for number in numbers:
            if count % 2 == 0:
                sum += number
            count += 1
        print("THE SUM OF EVEN: ", sum)

def generate_odd_numbers():
    sum = 0
    count = 0
    for number in numbers:
        if count % 2 == 1:
            sum += number
        count += 1
    print("THE SUM OF ODD: ", sum)

def multiply_numbers():
    sum = 1
    count = 1
    for number in numbers:
        if count % 3 == 0:
            sum *= number
        count += 1
    print("THE PRODUCT OF MUTIPLY: ", sum)

def average_numbers():
    sum = 0
    average = 0
    for number in numbers:
        sum += number
    average = sum / length_of_list()
    print("THE AVERAGE: ", average)








genarate_random_numbers()
print(length_of_list())
generate_even_numbers()
generate_odd_numbers()
multiply_numbers()
average_numbers()