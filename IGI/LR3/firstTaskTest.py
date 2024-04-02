import unittest
from task1 import calculateSeries

class FirstTaskUnitTest(unittest.TestCase):
    def testCalculateSeries(self):
        """Test for the calculateSeries function"""
        x = 0.02
        eps = 0.0001
        res = calculateSeries(x, eps)
        self.assertEqual(2, res)

if __name__ == '__main__':
    unittest.main()
    