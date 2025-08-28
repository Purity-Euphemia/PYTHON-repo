def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

sum = 0

for count in range(1, 6):
    num = int(input("Enter a number: "))
    check_even_odd(num)
    sum += num

print("Total sum =", sum)
