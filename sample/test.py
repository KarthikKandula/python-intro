import unittest

from sample import sum

class TestSum(unittest.TestCase):
    def test_sum(self):
        """
        Test that it can sum a list of integers
        """
        data = 1 + 2 + 3
        result = sum(1,2,3)
        self.assertEqual(result, data)

        data = 3 + 4 + 5 + 6
        result = sum(3,4,5,6)
        self.assertEqual(result, data)

        data = 7+8+9
        result = sum(7,8,9)
        self.assertEqual(result, data)

if __name__ == '__main__':
    unittest.main()