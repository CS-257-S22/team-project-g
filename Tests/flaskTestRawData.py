import unittest
import sys
import os

#access mother directory
currentPath = os.path.dirname(__file__)
motherdir = os.path.join(currentPath,"..")
sys.path.append(motherdir)
from FlaskApp import *
import CoreFunctions.displayRawData as dR

class rawDataTest(unittest.TestCase):
    maxDiff = None
    def testBasicData(self):
        '''Integral test with basic input'''
        
        self.app = app.test_client()
        response = self.app.get('/Rice/Minnesota/2020-2-1/2020-2-10', follow_redirects=True)
        response = str(response.data)
        location = Location("Rice", "Minnesota")
        dateRange = DateRange("2020-2-1", "2020-2-10")

        self.assertIn(dR.displayRawData(location, dateRange), response)

    def testOutofRangeDates(self):
        '''Integral test of the case with dates that are out of range'''
        self.app = app.test_client()
        response = self.app.get('/Rice/Minnesota/2020-1-1/2020-1-20/', follow_redirects=True)
        response = str(response.data)
        isCorrect =  "Date range outside of data!" in response
        self.assertTrue(isCorrect)
        
    def testWrongOrderDates(self):
        '''Integral test of the case with dates that are ordered incorrectly'''
        self.app = app.test_client()
        response = self.app.get('/Rice/Minnesota/2020-4-1/2020-3-1/', follow_redirects=True)
        response = str(response.data)
        isCorrect =  "Wrong order of dates!" in response
        self.assertTrue(isCorrect)
        
    def testWrongLocation(self):
        '''Integral test of the case with wrong county-state pair'''
        self.app = app.test_client()
        response = self.app.get('/R/M/2020-2-1/2020-3-1/', follow_redirects=True)
        response = str(response.data)
        isCorrect =  "This county-state pair does not exist! Check spelling." in response
        self.assertTrue(isCorrect)



if __name__ == '__main__':
    unittest.main()