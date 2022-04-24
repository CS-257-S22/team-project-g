from getDayWithMostCases import dayListToStr
import retrieveData
from flask import Flask
import getDayWithMostCases as gD

dataSet = []

# gets raw data from chosen data set to display in flask webpage
def displayRawData(location, dateRange):

    dataSet = retrieveData.getCountyStateData(location[0], location[1])
    dataSet = retrieveData.getDateRangeData(dataSet,dateRange)

    cases = retrieveData.getConfirmedCases(dataSet)
    deaths = retrieveData.getConfirmedDeaths(dataSet)

    returnString = location[0] + ", " + location[1] + ": confirmed cases and deaths from " + gD.dayListToStr(dateRange[0]) + " to " + gD.dayListToStr(dateRange[1]) + "\n"
    
    for i in cases:
        returnString += "Cases: " + cases[i] + "     Deaths: " + deaths[i] + "\n"

    return returnString
    


