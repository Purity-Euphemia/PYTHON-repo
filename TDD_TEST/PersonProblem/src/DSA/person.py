from ENUM import ProblemType
from person_problem import Problem

class Person:
    def __init__(self):
        self.problems = []

    def add_problem(self, name, type):
        problem = Problem(name,type)
        self.problems.append(problem)

    def solve_problem(self, name):
        for problem in self.problems:
            if problem.name == name:
                problem.solve()
                return True
        return False

    def get_problem(self):
        return self.problems

    def solve_problem_with_money(self):
        for problem in self.problems:
            if problem.type == ProblemType.FINANCIAL and not problem.is_solved:
                problem.solve()
                return True
        return False



