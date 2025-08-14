def number_to_words(n):
    ones = [
        "", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]

    tens = [
        "", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"
    ]

    if 1 <= n < 20:
        return ones[n]
    elif 20 <= n < 100:
        return tens[n // 10] + ('' if n % 10 == 0 else '-' + ones[n % 10])
    elif n == 100:
        return "one hundred"
    else:
        return "Number out of range"

try:
    num = int(input("Enter a number from 1 to 100: "))
    if 1 <= num <= 100:
        print("In words:", number_to_words(num))
    else:
        print("Please enter a number between 1 and 100.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
