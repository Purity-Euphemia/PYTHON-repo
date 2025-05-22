import categorize_numbers_functions
import unittest

class Test_categorize_numbers(unittest.TestCase):
	
	def test_that_categorize_numbers_exists(self):
		categorize_numbers_functions.categorize_numbers((15, 21, 30, 10), -3)

	def test_that_categorize_numbers_is_correct(self):
		actual = categorize_numbers_functions.categorize_numbers((15, 21, 30, 10), -3)
		expected = [15, 21, 30]
		self.assertEqual(actual, expected)

		actual = categorize_numbers_functions.categorize_numbers((12, 50, 25, 10), 5)
		expected = [50, 25, 10]
		self.assertEqual(actual, expected)