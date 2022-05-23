from CoreFunctions.retrieveData import getDataCombination
from CoreFunctions.helperClasses import *
from CoreFunctions.getDayWithMostCases import dayListToStr

dataSet = []

def displayRawData(location, dateRange):
    '''
    Gets raw data from chosen data set to display in flask webpage.
    '''
    
    dataSet = getDataCombination(location,dateRange)

    cases = dataSet.confirmedcases
    deaths = dataSet.confirmeddeaths
    dates = dataSet.dates

    returnString = location.county + ", " + location.state + ": confirmed cases and deaths from " + dayListToStr(dateRange.startDate) + " to " + dayListToStr(dateRange.endDate) + "<br/> <br/>"
    
    for i in range(len(cases)):
        returnString += dayListToStr(dates[i]) + "--- Cases: " + str(cases[i]) + "     Deaths: " + str(deaths[i]) + "<br/>"

    return returnString
    


