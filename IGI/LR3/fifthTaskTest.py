import unittest
from task5 import findMaxAbsoluteElement, multiplyElementsBetweenZeros

lst = [1, 0, 7.32, 9, 2, -3.5, 0, 1]

class FifthTaskUnitTest(unittest.TestCase):
    def testFindMaxAbsoluteElement(self):
        res = findMaxAbsoluteElement(lst)
        self.assertEqual(3, res)

    def testMultiplyElementsBetweenZeros(self):
        res = multiplyElementsBetweenZeros(lst)
        self.assertEqual(-461.15999999999997, res)


if __name__ == '__main__':
    unittest.main()


