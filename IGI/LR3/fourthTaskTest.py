import unittest
from task4 import countWordsLessThanFive, findShortestDWord, printWordsInOrder, string, dictInit

class FourthTaskUnitTest(unittest.TestCase):

    def setUp(self):
        dictInit(string)

    def testFindShortestDWord(self):
        res = findShortestDWord()
        self.assertEqual('and', res)

    def testCountWordsLessThenFive(self):
        res = countWordsLessThanFive(string)
        self.assertEqual(37, res)

    def testPrintWordsInOrder(self):
        lst = ['considering', 'daisy-chain', 'pleasure', 'suddenly', 'whether', 'trouble', 'getting', 'picking',
               'daisies', 'sleepy', 'stupid', 'making', 'Rabbit', 'could', 'would', 'worth', 'White', 'close',
               'mind', 'well', 'made', 'feel', 'very', 'when', 'with', 'pink', 'eyes', 'she', 'was', 'her',
               'own', 'for', 'the', 'hot', 'day', 'and', 'ran', 'So', 'in', 'as', 'of', 'be', 'up', 'by', 'a']
        res = printWordsInOrder(string)
        self.assertEqual(lst, res)

if __name__ == '__main__':
    unittest.main()