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
import retrieveData as rD

dummyDataSetRelativePath = "Data/dummy_data.csv"
wrongFormatDataSetRelativePath = "Data/dakeTest_incorrect_format_data.csv"

class retrieveDataTest(unittest.TestCase):
    
    def testGetStringLinesFromFile(self):
        '''Test if line 200 is correct in the resulting string list'''
        lines = rD.getStringLinesFromFile(dummyDataSetRelativePath)
        self.assertEqual(lines[199],"2021-06-21,Delaware,Pennsylvania,52541,1401,US\n")
        pass
    
    def testSplitDate(self):
        '''Test if the dates are split properly'''
        dateString = "2020-1-1"
        dateList = rD.splitDate(dateString)
        self.assertEqual(dateList,['2020','1','1'],"splitDate() is not fucntioning properly")
    pass
 
    def testWrongFormatData(self):
        '''Test if retrieveData identifies incorrectly formatted Data with a wrongly formatted dataset'''
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            rD.retrieveData(wrongFormatDataSetRelativePath) 
        self.assertEqual(fake_stdout.getvalue(), "Case format incorrect at line 1\nDate format incorrect at line 2\n")
        
#test module makeGraph.py        
import makeGraph as mG     
class makeGraphTest(unittest.TestCase):
    
    # Given that graphing it self cannot be automatically tested, 
    # test whether the main helper functions, claurlateYtickSize is working
    def testcalculateYTickSize(self):
        '''test whether y tick sizes are correctly calculated'''
        cases = ['130', '200', '350', '1000', '5000']
        expectedTickSize = [10, 100, 100, 100, 1000]
        for i in range(5):
            result = mG.calculateYTickSize(cases[:i+1])
            message = "error in " + str(i) + "th value"
            self.assertEqual(result,expectedTickSize[i], message)
        pass
    
#Manually test plotting
plotTestDataRelativePath = "Data/plot_test_data.csv"
plotTestDataSet = rD.retrieveData(plotTestDataRelativePath) 
<<<<<<< HEAD
dates = [i[0] for i in plotTestDataSet] #make dates list for test
confirmedCases = [int(i[3]) for i in plotTestDataSet] #make confirmed cases list for test
confirmedDeaths = [int(i[4]) for i in plotTestDataSet] #make confirmed deaths list for test
location = plotTestDataSet[0][1:3] #make Location list for test
def manualTestConfirmedCasesGraph():
    '''test making a confirmed cases graph out of a dummy data'''
    mG.makeConfirmedCasesGraph(dates,confirmedCases,location)
    
def manualTestConfirmedDeathsGraph():
    '''test making a deaths graph out of a dummy data'''
    mG.makeConfirmedDeathsGraph(dates,confirmedDeaths,location)
=======

def manualGraphing():
    '''test making a confirmed cases graph out of a dummy data'''
    location = ["Autauga", "Alabama"]
    dateRange = [['2020', '2', '1'] , ['2021', '10', '1']]
    mG.makeGraph(location,dateRange)
>>>>>>> b5d4327f2803aed414af3a6801fb96587f56dfb3
    
if __name__ == '__main__':
    manualGraphing()
    unittest.main()
   