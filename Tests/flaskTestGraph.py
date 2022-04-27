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
import displayGraph as dG
from FlaskApp import *
import checkFlaskInput as cFI

class flaskTestGraph(unittest.TestCase):

    def testTypicalDates(self):
        '''Integral test the case with typical input'''
        self.app = app.test_client()
        response = self.app.get('/Rice/Minnesota/2020-2-1/2020-9-1/graph', follow_redirects=True)
        response = str(response.data)
        isCorrect = ("Rice, Minnesota" in response) and ("2020-2-1" in response) and ("2020-9-1" in response) and ("<img src='data:image/png;base64" in response)
        self.assertTrue(isCorrect)
    def testCheckDate(self):
        '''test if valid input is true'''
        self.assertTrue(cFI.checkDate("2020-2-1","2020-9-1"))
    def testErrorCheckDate(self):
        '''test if valid input is true'''
        self.assertEqual('Invalid dates! Use YYYY-MM-DD format and enter dates during COVID outbreaks!',cFI.checkDate("2000-2-1","2020-9-1"))
    
        
    def testOutofRangeDates(self):
        '''Integraol test the case with dates that are out of range'''
        self.app = app.test_client()
        response = self.app.get('/Rice/Minnesota/2020-1-1/2020-2-1', follow_redirects=True)
        response = str(response.data)
        isCorrect = ("Rice, Minnesota" in response) and ("2020-2-1" in response) and ("2020-9-1" in response) and ("<img src='data:image/png;base64" in response)
        self.assertTrue(isCorrect)
        
    def testWrongOrderDates(self):
        self.app = app.test_client()
        response = self.app.get('/Rice/Minnesota/2020-4-1/2020-3-1', follow_redirects=True)
        response = str(response.data)
        isCorrect = ("Rice, Minnesota" in response) and ("2020-2-1" in response) and ("2020-9-1" in response) and ("<img src='data:image/png;base64" in response)
        self.assertTrue(isCorrect)    
        
if __name__ == '__main__':
    unittest.main()
   
