import unittest
import SamProductionCode
import sys

class CommandLineTest(unittest.TestCase):
    #Test if the empty comand line response works
    def testComandLineArguments(self):
        outPut = SamProductionCode.getComadLine();
        self.assertEqual(sys.argv[1:],outPut);
    def testEmptyComandLine(self):
        outPut = SamProductionCode.CheckComadLine([]);
        self.assertEqual(outPut,("No arguments, Try -s or -d"));
    def testFalseCompareArgument(self):
       self.assertFalse(SamProductionCode.compareArgument(""))
    def testTrueCompareArgument(self):
       self.assertEqual(SamProductionCode.compareArgument("-help"),"–state or -s “StateName” –daterange or -d “YYYY-MM-DD”’")
    def testCheckValidDates(self):
        outPut = SamProductionCode.checkValidDate("2020-1-1")
        self.assertEqual(outPut,["2020","1","1"])
    def testFalseCheckValidDates(self):
        outPut = SamProductionCode.checkValidDate("2020-1")
        self.assertFalse(outPut)
    def testArg1(self):
        outPut = SamProductionCode.CheckComadLineArg1(["-s"]);
        self.assertEqual(outPut,("Please input state name, Try: -s texas"));
    def testFullComandLine(self):
       outPut = SamProductionCode.CheckComadLine(["-s","-d","texas","2020-1-1","2002-1-1"]);
       self.assertEqual(outPut,("Please input valid date, Try: -d 2020-1-1 2020-1-2"));


if __name__ == '__main__':
    unittest.main()