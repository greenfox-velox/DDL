import unittest
from ddl_work import anagram
from ddl_work import count_letters

class MyFirstTestCases(unittest.TestCase):
    def setUp(self):
        self.str1 = 'almafa'
        self.str2 = 'famala'
        self.str3 = 'macskajancsi'
        self.str4 = 'jancsimacska'

    def test_is_it_anagram(self):
         self.assertTrue(anagram(self.str1, self.str2))

    def test_count_letters(self):
        self.assertEqual(count_letters(self.str3), count_letters(self.str4))
        print(count_letters(self.str3), count_letters(self.str3))


if __name__ == '__main__':
    unittest.main()
