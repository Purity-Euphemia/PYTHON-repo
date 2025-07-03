def covert_numbers_to_words(number):
    number_to_words = {
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',

    }
    #return number_to_words[numbers]
    return number_to_words.get(number, "invalid number") # to prevent invalid numbers thats not in the list

if __name__ == '__main__':
    number = int(input("Enter a number: "))
    number_to_words = covert_numbers_to_words(number)
    print(f" The number {number} is: {number_to_words}")
