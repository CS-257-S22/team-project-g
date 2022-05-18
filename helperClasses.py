# Stores classes that are used across functions 
from conversionFunctions import *

class Location:
    # a class with 2 variables, couty and states in string
    def __init__(self, county, state):
        """Initialize the class with string inputs"""
        self.state = state
        self.county = county

class DateRange:
     # a class with 2 variables, startdate and enddate
     # startdate and enddate in as lists [Year, Month, Date]
    def __init__(self, startDateString,endDateString):
        """
        Initialize the class with string inputs
        startDateString and endDateString are Strings of format "YYYY-MM-DD"
        """
        self.startDate = splitDate(startDateString)
        self.endDate = splitDate(endDateString)

class DataCombination:
    # a class with 3 variables: dates, confirmedcases, confirmeddeaths
    # dates is a list of ['YYYY', 'MM', 'DD'] Dates
    # confirmedcases is a list of number of confirmed cases during this date range
    # confirmedcases is a list of number of confirmed deaths during this date range
    def __init__(self, dates, confirmedcases, confirmeddeaths):
        """
        Initialize the class with string inputs
        startDateString and endDateString are Strings of format "YYYY-MM-DD"
        """
        self.dates = dates
        self.confirmedcases = confirmedcases
        self.confirmeddeaths = confirmeddeaths
