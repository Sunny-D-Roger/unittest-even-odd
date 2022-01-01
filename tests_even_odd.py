import unittest
from even_odd import even_odd_checker

class TestEvenOdd(unittest.TestCase):

    def test_result(self):
        result = even_odd_checker(6)
        msg = self.assertEqual(result, 'Odd')


if __name__ == '__main__':
    unittest.main()
