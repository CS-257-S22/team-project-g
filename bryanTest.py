import unittest
import getTimeData



class TestSum(unittest.TestCase):
    def testDateToList(self):
        newList = getTimeData.dateToList("2020-15-22")
        correctList = [2020, 15, 22]
        self.assertEqual(newList, correctList)

    def testTrimSet(self):
        testSet = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
        newSet = getTimeData.trimSet(testSet, 1, 4)
        correctSet = [[2,3,4], [7,8,9], [12,13,14], [17,18,19]]
        self.assertEqual(newSet, correctSet)
    
    def testCreateReturnSet(self):
        testSet = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
        newSet = getTimeData.createReturnSet()
        correctSet = [0, 1, 2, 3, 4, 5]
        self.assertEqual(newSet, correctSet)
    
    def testGetTimeRange(self):
        testSet = getTimeData.retrieveData(("Data/dummy_data.csv"))
        newSet = getTimeData.getTimeRange("2020-04-20", "2021-06-01")
        correctSet = getTimeData.trimSet(testSet, 0, 4)
        self.assertEqual(newSet, correctSet)

    

if __name__ == '__main__':
    unittest.main()
