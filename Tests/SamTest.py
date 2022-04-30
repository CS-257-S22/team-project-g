from sre_parse import State
import unittest
import sys
import os

currentPath = os.path.dirname(__file__)
motherdir = os.path.join(currentPath,"..")
sys.path.append(motherdir)

import ProductionCode as pC

class strut():
    def __init__(self,County,State,StartDate,EndDate):
        self.County = County
        self.State = State
        self.StartDate = StartDate
        self.EndDate = EndDate


class CommandLineTest(unittest.TestCase):
    '''Test is invalid input returns error'''
    def testComandLineArguments(self):
        #confirms CheckComandline workd
        args = strut("County","State","Date1","date2")
        outPut = pC.callData(args)
        self.assertEqual(outPut,"")

if __name__ == '__main__':
    unittest.main()