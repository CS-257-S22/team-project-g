import unittest
from unittest import mock
from unittest.mock import patch
import sys
import os
import io

currentPath = os.path.dirname(__file__)
motherdir = os.path.join(currentPath,"..")
sys.path.append(motherdir)
import retrieveData as rD

dummyDataSetRelativePath = "Data/dummy_data.csv"
wrongFormatDataSetRelativePath = "Data/dakeTestIncorrectFormatData.csv"

class retrieveDataTest(unittest.TestCase):
    
    #Test if line 200 is correct in the resulting string list
    def testGetStringLinesFromFile(self):
        lines = rD.getStringLinesFromFile(dummyDataSetRelativePath)
        self.assertEqual(lines[199],"2021-06-21,Delaware,Pennsylvania,52541,1401,US\n")
        pass
    
    #Test if the dates are split properly
    def testSplitDate(self):
        dateString = "2020-1-1"
        dateList = rD.splitDate(dateString)
        self.assertEqual(dateList,['2020','1','1'],"splitDate() is not fucntioning properly")
    pass
 
    #Test if retrieveData identifies incorrectly formatted Data with a wrongly formatted dataset
    def testWrongFormatData(self):
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            rD.retrieveData(wrongFormatDataSetRelativePath) 
        self.assertEqual(fake_stdout.getvalue(), "Case format incorrect at line 1\nDate format incorrect at line 2\n")

if __name__ == '__main__':
    unittest.main()
