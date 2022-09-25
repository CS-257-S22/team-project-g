import unittest
import sys
import os
import io
#access mother directory
currentPath = os.path.dirname(__file__)
motherdir = os.path.join(currentPath,"..")
sys.path.append(motherdir)

#test module retrieveData
import CoreFunctions.retrieveDataFromDatabase as rD
from CoreFunctions.helperClasses import *

class retrieveDataFromdatabaseTest(unittest.TestCase):

    def testTypicalData(self):
        '''Test if the function can retrieve data for a random typical input'''
        location = Location("Autauga", "Alabama")
        dateRange = DateRange("2022-3-1", "2022-3-2")
        dataSet = rD.getDataCombination(location, dateRange)
        print(dataSet.confirmedcases)
        print(dataSet.confirmeddeaths)
        self.assertEqual(dataSet.confirmedcases, [15520, 15528])
        self.assertEqual(dataSet.confirmeddeaths, [195, 198])

if __name__ == '__main__':
    unittest.main()
   