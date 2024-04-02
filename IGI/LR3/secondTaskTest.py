import unittest
from task2 import calculateEven

class SecondTaskUnitTest(unittest.TestCase):
    def testSecondTask(self):
        """Test for calculateEven function"""
        list_ = [1, 2, 4, 6, 3, 3, 78, 101, 345]
        res = calculateEven(list_)
        self.assertEqual(4, res)

if __name__ == '__main__':
    unittest.main()