import unittest

from string_function import string_function

class TestStringFunction(unittest.TestCase):
    def test_string_function(self):
        self.assertEqual("helloce", string_function("hello"))

    def test_add_function_can_be_add_in_middle(self):
        self.assertEqual("helceloo", string_function("helloo"))

    def test_the_length_of_the_word_is_it_divisible_by_2(self):
        self.assertEqual("helceloo", string_function("helloo"))

    def test_the_length_of_the_word_is_not_divisible_by_2(self):
        self.assertEqual("helloce", string_function("hello"))
