def unpack_collection(collection):
    result = [0,0,0,0]
    for index in range(4):
        result[index] += collection[index]
    return result


my_list = [16, 27, 9, 4, 5, 60, 7, 8, 9]
print("The first function ", unpack_collection(my_list))


def unparking_collection(collection):
    first_number, second_number, third_number, *_ = collection
    return first_number, second_number, third_number


print("The second function ", unparking_collection(my_list))


def unparking_collection(collection):
    first_number, second_number, third_number, *other = collection
    return first_number, second_number, third_number, other


print("The third function ", unparking_collection(my_list))


def slice_collection(numbers):
    return numbers[0: 8: 1]


print("The fouth function ", slice_collection(my_list))



def slice_collection(numbers):
    return numbers[0: 8: 2]


print("The fifth function ", slice_collection(my_list))


def slice_collection(numbers):
    return numbers[0: 8: 4]


print("The sixth function ", slice_collection(my_list))



def slice_collection(numbers):
    return numbers[4:-1: 4]


print("The seventh function ", slice_collection(my_list))


def slice_collection(numbers):
    return numbers[5: -1: 1]


print("The eighth function ", slice_collection(my_list))


def slice_collection(numbers):
    return numbers[: : ]


print("The ninth function ", slice_collection(my_list))


def sort_collection(numbers):
    numbers.sort()
    return numbers


print("The tenth function ", sort_collection(my_list))


def sort_collection(numbers):
    numbers.sort(reverse=True)
    return numbers


print("The eleventh function ", sort_collection(my_list))


def is_odd(number):
    return number % 2 == 1


def filter_collection(collection):
    return list(filter(is_odd, collection))


print("The twelveth function ", filter_collection(my_list))

my_list = [33, 22, 8, 9, 6, 2, 7]

def filter_with_lambda(collection):
    return list(filter(lambda number: number % 2 == 1, collection))


print("The thirteenth function ", filter_with_lambda(my_list))


def sum_collection(collection):
    sum_all_numbers = sum(map(lambda number : number, collection))
    return sum_all_numbers


print("The sum function ", sum_collection([2, 3, 4]))


