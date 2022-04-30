from sre_parse import State
import unittest
import sys
import io
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
    '''
    def testComandLineArguments(self):
        #confirms CheckComandline workd
        args = strut("County","State","Date1","date2")
        outPut = pC.callData(args)
        self.assertEqual(outPut,"")
    '''
    def testCheckComadLine(self):
        argv = ["Rice","Minnesota","2020-3-1","2020-3-5"]
        args = pC.CheckComadLine(argv)
        self.assertEqual(args.County, "Rice")
        self.assertEqual(args.State, "Minnesota")
        self.assertEqual(args.StartDate, "2020-3-1")
        self.assertEqual(args.EndDate, "2020-3-5")
        
    def testWrongStateCountyPair(self):
        args = strut("County","State","StartDate","EndDate")
        args.County = "R"
        args.State = "M"
        args.StartDate = "2020-3-1"
        args.EndDate = "2020-3-5"
        result = pC.callData(args)
        self.assertEqual(result, "This county-state pair does not exist! Check spelling.<br/>")
        
    def testWrongDateOrder(self):
        args = strut("County","State","StartDate","EndDate")
        args.County = "Rice"
        args.State = "Minnesota"
        args.StartDate = "2020-3-1"
        args.EndDate = "2020-2-1"
        result = pC.callData(args)
        self.assertEqual(result, "Wrong order of dates!<br/>")
        
    def testWrongDatezFormat(self):
        args = strut("County","State","StartDate","EndDate")
        args.County = "Rice"
        args.State = "Minnesota"
        args.StartDate = "202-1"
        args.EndDate = "202-1"
        result = pC.callData(args)
        self.assertEqual(result, "Invalid dates! Use YYYY-MM-DD format and enter dates during COVID outbreaks!<br/>")
        
    def testTypicalDataRaw(self):
        args = strut("County","State","StartDate","EndDate")
        args.County = "Rice"
        args.State = "Minnesota"
        args.StartDate = "2020-6-1"
        args.EndDate = "2020-6-2"
        args.graph = False
        result = pC.callData(args)
        expectedResult ="Rice, Minnesota: confirmed cases and deaths from June 1, 2020 to June 2, 2020<br/> "\
                        "<br/>June 01, 2020--- Cases: 462     Deaths: 2<br/>June 02, 2020--- Cases: 467     Deaths: 2<br/>"
        self.assertEqual(result,expectedResult)
        
    def testTypicalDataGraph(self):
        args = strut("County","State","StartDate","EndDate")
        args.County = "Rice"
        args.State = "Minnesota"
        args.StartDate = "2020-6-1"
        args.EndDate = "2021-6-2"
        args.graph = True

if __name__ == '__main__':
    unittest.main()