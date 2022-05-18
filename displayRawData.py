from getDayWithMostCases import dayListToStr
import retrieveData
from flask import Flask
from helperClasses import *
import getDayWithMostCases as gD

dataSet = []

def displayRawData(location, dateRange):
    '''
    Gets raw data from chosen data set to display in flask webpage.
    '''
    
    dataSet = retrieveData.getDataCombination(location,dateRange)

    cases = dataSet.confirmedcases
    deaths = dataSet.confirmeddeaths
    dates = dataSet.dates

    returnString = location.county + ", " + location.state + ": confirmed cases and deaths from " + gD.dayListToStr(dateRange.startDate) + " to " + gD.dayListToStr(dateRange.endDate) + "<br/> <br/>"
    
    for i in range(len(cases)):
        returnString += gD.dayListToStr(dates[i]) + "--- Cases: " + str(cases[i]) + "     Deaths: " + str(deaths[i]) + "<br/>"

    return returnString
    


