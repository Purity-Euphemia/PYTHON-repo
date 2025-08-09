class Human:
    def __init__(self, name, age, dob):
        self.name = name
        self.age = age
        self.dob = dob

        def __str__(self):
            return f'Human{self.name}, age: {self.age}, dob: {self.dob}'


h1 = Human("purity", 35, "1990")
print(h1)

