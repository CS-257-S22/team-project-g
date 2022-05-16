#Includes functions that retrieve data from a .csv file and process them.
import sys
import csv
from conversionFunctions import *
from datetime import datetime
from helperCheckInput import *
import os
from indexDictionary import *

#use the database if operating on server, else use the local .csv files
try:
    from retrieveDataFromDatabase import *
except:
    from retrieveDataFromLocal import *

def getDataWithLocationAndDateRange(location, dateRange):
    '''
    returns a list of data that fits the given location and daterange in 
    the format [Date (as a list of form [Year, Month, Day]), County, State, Confirmed Cases, Confirmed Deaths]
    
    locations is a list of 2 [county,state]
    dateRange is a list of 2 [[Year, Month, Day],[Year, Month, Day]] (startDate and endDate)
    '''
    
    county = location[0]
    state = location [1]
    list = getCountyStateData(county, state)
    list = getDateRangeData(list, dateRange)
    return list

def getDateRangeData(list, dateRange):
    '''
    trim a list with a dateRange [[Year, Month, Day],[Year, Month, Day]] 
    return the first subset of record within that daterange'''
    startDate = dateRange[0]
    startDate = toDateTime(startDate)
    endDate = dateRange [1]
    endDate = toDateTime(endDate)
    newList = []
    for line in list:
        thisdate = toDateTime(line[0])
        if(thisdate < startDate): continue
        if(thisdate > endDate): break
        newList.append(line)
    return newList

def getDates(list):
    '''return the column of dates from a list '''
    
    dates = [i[dateIndex] for i in list]
    return dates

def getConfirmedCases(list):
    '''return the column of death numbers from a list '''
    
    deaths = [int(i[confirmedCaseseIndex]) for i in list]
    return deaths

def getConfirmedDeaths(list):
    '''return the column of confirmed cases from a list '''
    deaths = [int(i[confirmedDeathsIndex]) for i in list]
    return deaths

def getStateNames(dataSet):
    '''input data set'''
    '''trim date set to just state names'''
    '''out put list of state names'''
    stateNames = []
    for line in dataSet:
        stateNames.append(line[stateIndex])
    return  stateNames

