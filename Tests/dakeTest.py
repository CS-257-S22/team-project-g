import unittest
import sys
import os
currentPath = os.path.dirname(__file__)
motherdir = os.path.join(currentPath,"..")
sys.path.append(motherdir)
import ProductionCode

dummyDataSetRelativePath = "Data/dummy_data.csv"

class retrieveDataTest(unittest.TestCase):
    def testDataFormat():
        self.assertEqual()
        pass

if __name__ == '__main__':
    unittest.main()
