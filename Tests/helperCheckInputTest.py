import unittest
import sys
import os
#access mother directory
currentPath = os.path.dirname(__file__)
motherdir = os.path.join(currentPath,"..")
sys.path.append(motherdir)
from FlaskApp import *
import CoreFunctions.helperCheckInput as hCI

class helperCheckInputTest(unittest.TestCase):
    
    def testCheckTypicalDates(self):
        '''test if valid input is true'''
        self.assertTrue(hCI.checkDates("2020-2-1","2020-9-1"))
        
    def testCheckErrorDates(self):
        '''test if invalid input gives an error message'''
        self.assertEqual('Invalid dates! Use YYYY-MM-DD format and enter dates during COVID outbreaks!', hCI.checkDates("2000-2-1","2020-9-1"))
    
    def testCheckTypicalCountyState(self):
        '''test a typical county-state pair and see if the check function returns true'''
        county = "Rice"
        state = "Minnesota"
        result = hCI.checkCountyState(county,state)
        self.assertEqual(result, True)
        
    def testCheckWrongCountyState(self):
        '''test an error county-state pair and see if the check function returns an error message'''
        county = "R"
        state = "M"
        result = hCI.checkCountyState(county,state)
        self.assertEqual(result, "This county-state pair does not exist! Check spelling.") 
       
if __name__ == '__main__':
    unittest.main()
   