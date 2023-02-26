import unittest

from sample import sum,ignore_3

class TestSum(unittest.TestCase):
    def test_sum(self):
        """
        Test sum() function from sample.py
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

    def test_ignore_3(self):
        """
        Test ignore_3() function from sample.py
        """
        data = 1+2
        result = ignore_3(1,2,3)
        self.assertEqual(result, data)

        data = 4+5+6
        result = ignore_3(3,4,5,6)
        self.assertEqual(result, data)

        data = 7+8+9+9
        result = ignore_3(7,8,9,9,3)
        self.assertEqual(result, data)

        data = 0+0+0
        result = ignore_3(3,3,3,0)
        self.assertEqual(result, data)

        data = 0
        result = ignore_3(0)
        self.assertEqual(result, data)

if __name__ == '__main__':
    unittest.main()
