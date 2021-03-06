import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_2_and_3_is_5(self):
        self.assertEqual(extend.add(12, 23), 35)

    def test_add_4_and_1_is_5(self):
        self.assertEqual(extend.add(122, 112), 234)

    def test_max_of_three_first(self):
        self.assertEqual(extend.max_of_three(10, 0, 1), 10)

    def test_max_of_three_third(self):
        self.assertEqual(extend.max_of_three(13, 24, 45), 45)

    def test_median_four(self):
        self.assertEqual(extend.median([7, 9, 12, 13]), 15)

    def test_median_five(self):
        self.assertEqual(extend.median([7, 9, 12, 13, 16]), 12)

    def test_is_vovel_a(self):
        self.assertTrue(extend.is_vovel('a'))

    def test_is_vovel_u(self):
        self.assertTrue(extend.is_vovel('u'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('Bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('kolbice'), 'kovolbiviceve')

if __name__ == '__main__':
    unittest.main()
