list_nums = [10, 20, 30, 40, 50]
list_colours = ['red', 'green', 'blue']
list_colours[2] = "yellow"

list_colours.append('purple')


list = [1, 2, 3, 4, 5]
list.remove(list[2])

list_name = ['Alice', 'Bob', 'Charlie']


list_numbers = [4, 1, 3, 9, 2]
list_numbers.sort()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def even_index_elements(nums):
    result = []
    for index in nums:
        if index % 2 == 0:
            result.append(index)
    return result


list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2

name = ["lamb", "Kit", "Yam", "Kings", "Dogs", "Man"]
def string(name):
    result = []
    for index in range(len(name)):
        if len(name[index]) == 3:
            result.append(name[index])
    return result









print(list_nums[2])

print(list_colours)

print(list)

print(len(list_name))
print(list_numbers)
print(even_index_elements(nums))
print(concatenated_list)
print(string(name))
