def cPrime(number):
    if not isinstance(number, int) or number <= 1:
        print("Please enter a whole number greater than 1.")
        return

    is_prime = True
    for count in range(2, int(number ** 0.5) + 1):
        if number % count == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a Prime Number.")
    else:
        print(f"{number} is a Non-Prime Number.")


cPrime(17)  # Change 17 to test other numbers
