import unittest
import sys
sys.path.append("C:\CS 257 Code\G")
import getDayWithMostCases

class CommandLineTest(unittest.TestCase):
    #Test spitting out the arguments
    def test_is_state_in_data(self):
        result = getDayWithMostCases.stateInData("Minnesota")
        self.assertTrue(result) 

    def test_day_list_to_str(self):
        result = getDayWithMostCases.dayListToStr(["2022", "04", "18"])
        self.assertEqual(result, "April 18, 2022")

    def test_get_day_with_most_cases(self):
        result = getDayWithMostCases.getDayWithMostCases("Minnesota")
        self.assertEqual(result, "On September 18, 2021 in Minnesota there were 2433 cases.")

if __name__ == '__main__':
    unittest.main()