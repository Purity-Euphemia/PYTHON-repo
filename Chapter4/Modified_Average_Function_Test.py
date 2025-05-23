import Modified_Average_Function
import unittest

class average(unittest.TestCase):
	
	def test_that_Modified_Average_Function_exists(self):
		Modified_Average_Function.average(5, 10, 15)

	def test_that_average_is_correct(self):
		actual = Modified_Average_Function.average(5, 10, 15)
		expected = 10.0
		self.assertEqual(actual, expected)

		actual = Modified_Average_Function.average(5, 10, 15, 20)
		expected = 12.5
		self.assertEqual(actual, expected)
