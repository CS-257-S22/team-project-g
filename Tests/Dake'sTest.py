import unittest
import ProductionCode

class CommandLineTest(unittest.TestCase):
    #Test spitting out the arguments
    def test_in_out(self):
        Output = ProductionCode.main("-a -b Minnesota")
        self.assertEqual(Output, "-a -b Minnesota")
        pass

    def test_county_with_most_cases_per_state(self):
        self
        pass

if __name__ == '__main__':
    unittest.main()
