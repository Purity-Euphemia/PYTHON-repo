import unittest
from BankAccount import BankAccount

class TestBank(unittest.TestCase):
	def test_account_create(self):
		account = BankAccount.create_account("PURITY", "1234567890","09187656443")
		self.assertIsNotNone(account)
		self.assertEqual(1,len(BankAccount.account))