from dakeFlask import *
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

class flaskTest(unittest.TestCase):
    
    def testHome(self):
        '''test homepage content'''
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(b"""
            In this function, you can get graphs of covid cases and deaths numbers to day<br/>
            Due to the fact that we are operating on a dummy data set, this apps is designed to display graphs for Autauga, Alabama<br/>
            Please input a start date and an end date in the route, in the following format:<br/>
            .../graph/startdate/enddate<br/>
            try:<br/>
            .../graph/2020-1-1/2020-12-1
            """, response.data)
        
    def testWrongDates(self):
        '''test the case when input is wrong'''
        self.app = app.test_client()
        response = self.app.get('/graph/21/00', follow_redirects=True)
        self.assertEqual(b"Please enter corret dates! Try .../graph/2020-1-1/2020-12-1", response.data)
        
    def testNoData(self):
        '''test the case when no data is found'''
        self.app = app.test_client()
        response = self.app.get('/graph/2020-1-1/2020-1-2', follow_redirects=True)
        self.assertEqual(b"Data Not Found!", response.data)   
         
    def testCorrectData(self):
        '''test if image is printed for right input'''
        self.app = app.test_client()
        response = self.app.get('/graph/2020-2-1/2021-3-1', follow_redirects=True)
        self.assertTrue(str(response.data).startswith('''b"<img src=''')) 
        
if __name__ == '__main__':
    unittest.main()
   
