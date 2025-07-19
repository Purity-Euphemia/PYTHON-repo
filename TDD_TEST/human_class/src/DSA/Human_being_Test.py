import unittest
from Human_Being import Human_Being
from man_class import Man
from woman_class import Woman

class Human_Being_Test(unittest.TestCase):
    def test_valid_human_class(self):
        person = Human_Being("Onyii", 28)
        self.assertEqual(person.get_name(), "Onyii")
        self.assertEqual(person.get_age(), 28)

    def test_invalid_name(self):
        person = Human_Being("", 28)
        self.assertIsNone(person.get_name())

    def test_invalid_age(self):
        person = Human_Being("Onyii", -28)
        self.assertIsNone(person.get_age())

class Woman_Being_Test(unittest.TestCase):
    def test_valid_woman_class(self):
        woman = Woman("Onyii", 28)
        self.assertEqual(woman.get_name(), "Onyii")
        self.assertEqual(woman.get_age(), 28)
        self.assertEqual(woman.speak(), "My name is Onyii, and I am a woman")


class Man_Test(unittest.TestCase):
    def test_valid_man_class(self):
        man = Man("Jhon", 18)
        self.assertEqual(man.get_name(), "Jhon")
        self.assertEqual(man.get_age(), 18)
        self.assertEqual(man.speak(), "My name is Jhon, and I am a man")

