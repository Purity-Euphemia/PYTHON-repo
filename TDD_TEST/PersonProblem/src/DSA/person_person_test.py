import unittest

from ENUM import ProblemType
from person import Person
from Person_problem import Problem


class TestPersonProblem(unittest.TestCase):

    def test_add_problem(self):
        person = Person()
        person.add_problem("No money", ProblemType.FINANCIAL)

        self.assertEqual(len(person.problems), 1)
        self.assertEqual(person.problems[0].name, "No money")
        self.assertEqual(person.problems[0].type, ProblemType.FINANCIAL)
        self.assertFalse(person.problems[0].is_solved)


    def test_solve_problem(self):
        person = Person()
        person.add_problem("No money", ProblemType.FINANCIAL)
        result = person.solve_problem("No money")
        self.assertTrue(result)
        self.assertTrue(person.problems[0].is_solved)

    def test_solve_problem_with_money(self):
        person = Person()
        person.add_problem("No money", ProblemType.FINANCIAL)
        result = person.solve_problem_with_money()
        self.assertTrue(result)
        self.assertTrue(person.problems[0].is_solved)

    def test_solve_nonexisting_problem(self):
        person = Person()
        result = person.solve_problem("imaginary issue")
        self.assertFalse(result)

    def test_solve_nonexisting_problem_with_money(self):
        person = Person()
        result = person.solve_problem_with_money()
        self.assertFalse(result)
        self.assertEqual(len(person.problems), 0)

    def test_add_another_problem(self):
        person = Person()
        person.add_problem("No money to call pastor", ProblemType.SPIRITUAL)

        self.assertEqual(len(person.problems), 1)
        self.assertEqual(person.problems[0].name, "No money to call pastor")
        self.assertEqual(person.problems[0].type, ProblemType.SPIRITUAL)
        self.assertFalse(person.problems[0].is_solved)

    def test_solve_already_solved_problem(self):
        person = Person()
        person.add_problem("No money", ProblemType.SPIRITUAL)
        person.problems[0].solve()
        result = person.solve_problem_with_money()
        self.assertFalse(result)
        self.assertTrue(person.problems[0].is_solved)


    def test_solve_only_unsolved_financial_problem(self):
        person = Person()
        person.add_problem("Money issue", ProblemType.FINANCIAL)
        person.add_problem("Spiritual stress", ProblemType.SPIRITUAL)
        person.add_problem("Financial stress", ProblemType.FINANCIAL)
        person.problems[0].solve()
        result = person.solve_problem_with_money()
        self.assertTrue(result)
        self.assertTrue(person.problems[2].is_solved)


