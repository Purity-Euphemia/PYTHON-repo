import unittest
from PhoneBook import PhoneBook
from Contact import Contact


class PhoneBookTest(unittest.TestCase):

    def test_add_contact(self):
        phonebook = PhoneBook()
        contact = Contact("John", "Smith", "09012345678")
        phonebook.add_contact(contact)
        self.assertEqual(len(phonebook.get_all_contact()), 1)

    def test_add_second_contact(self):
        phonebook = PhoneBook()
        contact = Contact("John", "Smith", "0912345678")
        phonebook.add_contact(contact)
        contact = Contact("Ade", "Smith", "0912345679")
        phonebook.add_contact(contact)
        self.assertEqual(len(phonebook.get_all_contact()), 2)

    def test_remove_contact(self):
        phonebook = PhoneBook()
        contact = Contact("John", "Smith", "0912345678")
        phonebook.add_contact(contact)
        contact = Contact("Ade", "Smith", "0912345678")
        phonebook.add_contact(contact)
        phonebook.remove_contact("0912345678")
        self.assertEqual(len(phonebook.get_all_contact()), 1)

    def test_find_by_phone(self):
        phonebook = PhoneBook()
        contact = Contact("John", "Smith", "0912345678")
        phonebook.add_contact(contact)
        result = phonebook.find_by_phone_number("0912345678")
        self.assertIsNotNone(result)

    def test_find_by_phone_not_found(self):
        phonebook = PhoneBook()
        self.assertIsNone(phonebook.find_by_phone_number("0912345674"))

    def test_find_by_first_name(self):
        phonebook = PhoneBook()
        contact1 = Contact("John", "Smith", "0912345678")
        contact2 = Contact("Ade", "Smith", "0912345679")
        phonebook.add_contact(contact1)
        phonebook.add_contact(contact2)
        results = phonebook.find_by_first_name("John")
        self.assertEqual(len(results), 1)

    def test_find_by_last_name(self):
        phonebook = PhoneBook()
        contact1 = Contact("John", "Smith", "0912345678")
        contact2 = Contact("Ade", "Jude", "0912345679")
        phonebook.add_contact(contact1)
        phonebook.add_contact(contact2)
        results = phonebook.find_by_last_name("Smith")
        self.assertEqual(len(results), 1)

    def test_find_by_last_name_not_found(self):
        phonebook = PhoneBook()
        result = phonebook.find_by_last_name("Nonexistent")
        self.assertEqual(result, None)

    def test_edit_contact_success(self):
        phonebook = PhoneBook()
        old_contact = Contact("John", "Smith", "0912345678")
        phonebook.add_contact(old_contact)

        new_contact = Contact("John", "Okafor", "0912345674")
        result = phonebook.edit_contact("0912345678", new_contact)
        self.assertTrue(result)

    def test_edit_contact_not_found(self):
        phonebook = PhoneBook()
        new_contact = Contact("John", "Smith", "0912345678")
        phonebook.edit_contact("0912345678", new_contact)
        self.assertIsNone(phonebook.find_by_phone_number("0912345678"))

