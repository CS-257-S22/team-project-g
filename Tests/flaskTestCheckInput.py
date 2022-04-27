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

class flaskCheckInput(unittest.TestCase):
   
    def testCheckDate(self):
        '''test if valid input is true'''
        self.assertTrue(cFI.checkDate("2020-2-1","2020-9-1"))
    def testErrorCheckDate(self):
        '''test if valid input is true'''
        self.assertEqual('Invalid dates! Use YYYY-MM-DD format and enter dates during COVID outbreaks!',cFI.checkDate("2000-2-1","2020-9-1"))

        
if __name__ == '__main__':
    unittest.main()
   