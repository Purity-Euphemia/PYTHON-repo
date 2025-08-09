from Human import Human

class Employee(Human):
    def __init__(self, name, age, dob, employee_id):
        super().__init__(name, age, dob)
        self.employee_id = employee_id

    def __str__(self):
        return f"{super().__str__()}, employee_id: {self.employee_id}"

class Facilitator(Employee):
    ...

e1 = Employee("Purity", 35, "1990", 1)
print(e1)

