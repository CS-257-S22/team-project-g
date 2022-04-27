import unittest
import sys
import os
#access mother directory
currentPath = os.path.dirname(__file__)
motherdir = os.path.join(currentPath,"..")
sys.path.append(motherdir)
from FlaskApp import *
import checkFlaskInput as cFI
import helperCheckInput as hCI

class flaskTestCheckInput(unittest.TestCase):
    
    def testCheckTypicalDate(self):
        '''test if valid input is true'''
        self.assertTrue(cFI.checkDate("2020-2-1","2020-9-1"))
        
    def testCheckErrorDate(self):
        '''test if invalid input gives an error message'''
        self.assertEqual('Invalid dates! Use YYYY-MM-DD format and enter dates during COVID outbreaks!', cFI.checkDate("2000-2-1","2020-9-1"))
        
if __name__ == '__main__':
    unittest.main()
   