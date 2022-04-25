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

class flaskTestGraph(unittest.TestCase):

    def testTypicalDates(self):
        '''test the case with typical input'''
        self.app = app.test_client()
        response = self.app.get('/Rice/Minnesota/2020-2-1/2020-9-1/graph', follow_redirects=True)
        response = str(response.data)
        isCorrect = ("Rice, Minnesota" in response) and ("2020-2-1" in response) and ("2020-9-1" in response) and ("<img src='data:image/png;base64" in response)
        self.assertTrue(isCorrect)
        
if __name__ == '__main__':
    unittest.main()
   
