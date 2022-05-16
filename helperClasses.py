# Stores classes that are used across functions 
from conversionFunctions import *

class Location:
    # a class with 2 variables, couty and states in string
    def __init__(self, county, state):
        """Initialize the class with string inputs"""
        self.state = state
        self.county = county

class DateRange:
     # a class with 2 variables, 
     # startdate and enddate in as lists [Year, Month, Date]
    def __init__(self, startDateString,endDateString):
        """
        Initialize the class with string inputs
        startDateString and endDateString are Strings of format "YYYY-MM-DD"
        """
        self.startDate = splitDate(startDateString)
        self.endDate = splitDate(endDateString)