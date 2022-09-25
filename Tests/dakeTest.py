import unittest
from unittest import mock
from unittest.mock import patch
import sys
import os
import io
#access mother directory
currentPath = os.path.dirname(__file__)
motherdir = os.path.join(currentPath,"..")
sys.path.append(motherdir)

#test module retrieveData
from CoreFunctions.retrieveDataFromLocal import retrieveData, getStringLinesFromFile
from CoreFunctions.helperClasses import *

dummyDataSetRelativePath = "Data/dummy_data.csv"
wrongFormatDataSetRelativePath = "../Data/TestData/dakeTest_incorrect_format_data.csv"

class retrieveDataFromLocalTest(unittest.TestCase):
    
    def testGetStringLinesFromFile(self):
        '''Test if line 200 is correct in the resulting string list'''
        lines = getStringLinesFromFile(dummyDataSetRelativePath)
        self.assertEqual(lines[199],"2021-06-21,Delaware,Pennsylvania,52541,1401,US\n")
        pass
    
    def testSplitDate(self):
        '''Test if the dates are split properly'''
        dateString = "2020-1-1"
        dateList = splitDate(dateString)
        self.assertEqual(dateList,['2020','1','1'],"splitDate() is not fucntioning properly")
    pass
 
    def testWrongFormatData(self):
        '''Test if retrieveData identifies incorrectly formatted Data with a wrongly formatted dataset'''
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            retrieveData(wrongFormatDataSetRelativePath) 
        self.assertEqual(fake_stdout.getvalue(), "Case format incorrect at line 1\nDate format incorrect at line 2\n")
        
#test module makeGraph.py        
import CoreFunctions.makeGraph as mG     
class makeGraphTest(unittest.TestCase):
    
    # Given that graphing it self cannot be automatically tested, 
    # test whether the main helper functions, claurlateYtickSize is working
    def testcalculateYTickSize(self):
        '''test whether y tick sizes are correctly calculated'''
        cases = ['0','130', '200', '350', '1000', '5000']
        expectedTickSize = [10, 100, 100, 100, 1000]
        for i in range(5):
            result = mG.calculateYTickSize(cases[:i+2])
            message = "error in " + str(i) + "th value"
            self.assertEqual(result,expectedTickSize[i], message)
        pass

import CoreFunctions.helperCheckInput as hCI

class helperCheckInputTest(unittest.TestCase):
    def testCorrectCheckValidDate(self):
        date = ['2021', '2', '3']
        self.assertTrue(hCI.checkValidDate(date))
        
    def testWrongCheckValidDate(self):
        date = ['20', '-1', '3']
        self.assertFalse(hCI.checkValidDate(date))
            
if __name__ == '__main__':
    unittest.main()
   