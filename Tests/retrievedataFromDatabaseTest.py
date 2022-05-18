import unittest
import sys
import os
import io
#access mother directory
currentPath = os.path.dirname(__file__)
motherdir = os.path.join(currentPath,"..")
sys.path.append(motherdir)

#test module retrieveData
import retrieveDataFromDatabase as rD
from helperClasses import *

class retrieveDataFromdatabaseTest(unittest.TestCase):

    def testTypicalData(self):
        '''Test if the function can retrieve data for a random typical input'''
        location = Location("Autauga", "Alabama")
        dataSet = rD.getCountyStateData(location.county, location.state)
        #Use a random day to check if the dataset retrieved is correct
        instance = [['2022', '04', '08'], 'Autauga', 'Alabama', 15744, 213]
        self.assertIn(instance, dataSet)
    pass

if __name__ == '__main__':
    unittest.main()
   