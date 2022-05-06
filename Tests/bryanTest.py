import unittest
import getTimeData
import retrieveData

testData = retrieveData.retrieveData("Data/dummy_data.csv")

class TestSum(unittest.TestCase):

    def testGetTimeRange(self):
        ''' 
        test if getTimeRange from getTimeData works
        '''
        testCorrect = []
        for groupIndex in testData:
            if groupIndex == 11 or groupIndex == 20 or groupIndex == 74:
                testCorrect.append(testData[groupIndex])
        testSet = testData 
        newSet = getTimeData.getTimeRange("2021-02-17", "2021-02-20") 
        self.assertEqual(newSet, testCorrect) 

if __name__ == '__main__':
    unittest.main()
