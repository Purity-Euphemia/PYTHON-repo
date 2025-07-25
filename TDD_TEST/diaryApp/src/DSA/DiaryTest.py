import unittest

from Diary import Diary


class DiaryTest(unittest.TestCase):
    def test_new_diary_is_locked(self):
        diary : Diary = Diary("Username", "Password")
        self.assertTrue(diary.is_locked())

    def test_unlock_diary_with_correct_password(self):
        diary : Diary = Diary("Username", "Password")
        self.assertFalse(diary.unlock("Password"))

    def test_is_empty_diary(self):
        diary : Diary = Diary("Username", "Password")
        self.assertTrue(diary.is_empty())

    def test_unlock_diary_with_wrong_password(self):
        diary : Diary = Diary("Username", "Password")
        diary.is_locked()
        self.assertRaises(ValueError, diary.unlock, "Wrong password")


    def test_add_entry_when_unlocked(self):
        diary : Diary = Diary("Username", "Password")
        diary.unlock("Password")
        diary.add_entry("My Day", "It was my day")
        self.assertEqual(1,len(diary.get_entries()))

    def test_multiple_entries(self):
        diary : Diary = Diary("Username", "Password")
        diary.unlock("Password")
        diary.add_entry("Day 1", "It was my day")
        diary.add_entry("Day 2", "It was my turn")
        self.assertEqual(2,len(diary.get_entries()))

    def test_add_entry_when_locked_raises_exception(self):
        diary : Diary = Diary("Username", "Password")
        diary.is_locked()
        self.assertRaises(ValueError, diary.add_entry, "Ooops", "Should not be allowed")

    def test_get_entries_returns_correct_content(self):
        diary : Diary = Diary("Username", "Password")
        diary.unlock("Password")
        diary.add_entry("Day 1", "It was my day")
        entries = diary.get_entries()
        self.assertEqual(entries[0]["title"], "Day 1")
        self.assertEqual(entries[0]["content"], "It was my day")

    def test_diary_is_not_empty_after_adding_entry(self):
        diary : Diary = Diary("Username", "Password")
        diary.unlock("Password")
        diary.add_entry("Not Empty", "Definitely not")
        self.assertFalse(diary.is_empty())
