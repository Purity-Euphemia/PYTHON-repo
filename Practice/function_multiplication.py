def calculate_product(*args):
    product = 1
    for number in args:
        product *= number
    return product

print(calculate_product(10,20,30,40))
