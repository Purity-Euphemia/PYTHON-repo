from problem import  Problem


class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.__name = name # is now only accessible within the class(private)
        self.__age = age
        self.gender = gender
        self.__problems = []

    def add_problem(self, problem: Problem):
        self.__problems.append(problem)




p1 = Person("john",22,"Male")



