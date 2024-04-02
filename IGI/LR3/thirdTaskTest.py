import unittest
from task3 import countSpaces

class ThirdTaskUnitTest(unittest.TestCase):
    def testThirdTask(self):
        string = "hhs shhjshjdsh h  hsjjs kis"
        res = countSpaces(string)
        self.assertEqual(5, res)

if __name__ == '__main__':
    unittest.main()