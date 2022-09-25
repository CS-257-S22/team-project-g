#Includes functions that retrieve data from a .csv file and process them.
from datetime import datetime
import os
from CoreFunctions.helperCheckInput import *
from CoreFunctions.conversionFunctions import *
from CoreFunctions.indexDictionary import *
from CoreFunctions.helperClasses import *

#data path of the dataset .csv file relative to this folder
dataSet = [] 
#2-d array data set in the format [Date (as a list of form [Year, Month, Day]), County, State, Confirmed Cases, Confirmed Deaths]

def getDataCombination(location, dateRange):
    """
    Inputs: 
    locations is a Location object
    dateRange is a DateRange object

    Output:
    returns a DataCombanation object for graphing and displaying raw data
    """
    dataSet = getDataWithLocationAndDateRange(location, dateRange)
    dates = getDates(dataSet)
    confirmedCases = getConfirmedCases(dataSet)
    confirmedDeaths = getConfirmedDeaths(dataSet)
    return DataCombination(dates, confirmedCases, confirmedDeaths)

def getDataWithLocationAndDateRange(location, dateRange):
    '''
    returns a list of data that fits the given location and daterange in 
    the format [Date (as a list of form [Year, Month, Day]), County, State, Confirmed Cases, Confirmed Deaths]
    
    locations is a Location object
    dateRange is a DateRange object
    '''

    list = getCountyStateData(location.county, location.state)
    list = getDateRangeData(list, dateRange)
    return list

def getDateRangeData(dataSet, dateRange):
    '''
    trim a list with a dateRange
    return the first subset of record within that daterange'''
    startDate = toDateTime(dateRange.startDate)
    endDate = toDateTime(dateRange.endDate)
    newList = []
    for line in dataSet:
        line = list(line)
        line[dateIndex] = splitDate(line[dateIndex])
        thisdate = toDateTime(line[dateIndex])
        if(thisdate < startDate): continue
        if(thisdate > endDate): break
        newList.append(line)
    return newList

def getDates(dataSet):
    '''return the column of dates from a list '''
    
    dates = [i[dateIndex] for i in dataSet]
    return dates

def getConfirmedCases(dataSet):
    '''return the column of death numbers from a list '''
    
    deaths = [int(i[confirmedCaseseIndex]) for i in dataSet]
    return deaths

def getConfirmedDeaths(dataSet):
    '''return the column of confirmed cases from a list '''
    deaths = [int(i[confirmedDeathsIndex]) for i in dataSet]
    return deaths

def getStateNames(dataSet):
    '''input data set'''
    '''trim date set to just state names'''
    '''out put list of state names'''
    stateNames = []
    for line in dataSet:
        stateNames.append(line[stateIndex])
    return  stateNames

def retrieveData(relativeDataPath):
    '''get data from a relative path to this file, return a dataSet[] variable that stores the data'''
    absoluteDataPath = convertRealtivePathToAbsolutePath(relativeDataPath)
    stringLines = getStringLinesFromFile(absoluteDataPath)
    storeData(stringLines)
    return dataSet

def getStringLinesFromFile(filePath):
    '''Get lines as a list of strings from file'''
    with open(filePath) as file:
        stringLines  = file.readlines()[1:]
    file.close()
    return stringLines

def getCountyStateData(county, state):
    '''returns a list of data that fits the county and state from dataSet'''
    path = "../Data/sub-Data/" + county + "," + state + ".csv" 
    return retrieveData(path)
    
def convertRealtivePathToAbsolutePath(relativeDataPath):
    '''Calculate and return absolute path of the file'''
    currentPath = os.path.dirname(__file__)
    return os.path.join(currentPath, relativeDataPath)

def storeData(stringLines):
    '''Break each line into lists and store them in dataSet'''
    lineNum = 0
    for i in stringLines:
        lineNum+= 1 # keep track of line number for error message
        listLine = convertStringLinetoList(i)
        listLine.pop() # remove last column
        if(checkDataFormat(listLine, lineNum)):
            dataSet.append(listLine)   #skip the line if not formatted correctly
def getDataCombination(location, dateRange):
    """
    Inputs: 
    locations is a Location object
    dateRange is a DateRange object

    Output:
    returns a DataCombanation object for graphing and displaying raw data
    """
    dataSet = getDataWithLocationAndDateRange(location, dateRange)
    dates = getDates(dataSet)
    confirmedCases = getConfirmedCases(dataSet)
    confirmedDeaths = getConfirmedDeaths(dataSet)
    return DataCombination(dates, confirmedCases, confirmedDeaths)

def getDataWithLocationAndDateRange(location, dateRange):
    '''
    returns a list of data that fits the given location and daterange in 
    the format [Date (as a list of form [Year, Month, Day]), County, State, Confirmed Cases, Confirmed Deaths]
    
    locations is a Location object
    dateRange is a DateRange object
    '''

    list = getCountyStateData(location.county, location.state)
    list = getDateRangeData(list, dateRange)
    return list

def getDateRangeData(dataSet, dateRange):
    '''
    trim a list with a dateRange
    return the first subset of record within that daterange'''
    startDate = toDateTime(dateRange.startDate)
    endDate = toDateTime(dateRange.endDate)
    newList = []
    for line in dataSet:
        line = list(line)
        line[dateIndex] = splitDate(line[dateIndex])
        thisdate = toDateTime(line[dateIndex])
        if(thisdate < startDate): continue
        if(thisdate > endDate): break
        newList.append(line)
    return newList

def getDates(dataSet):
    '''return the column of dates from a list '''
    
    dates = [i[dateIndex] for i in dataSet]
    return dates

def getConfirmedCases(dataSet):
    '''return the column of death numbers from a list '''
    
    deaths = [int(i[confirmedCaseseIndex]) for i in dataSet]
    return deaths

def getConfirmedDeaths(dataSet):
    '''return the column of confirmed cases from a list '''
    deaths = [int(i[confirmedDeathsIndex]) for i in dataSet]
    return deaths

def getStateNames(dataSet):
    '''input data set'''
    '''trim date set to just state names'''
    '''out put list of state names'''
    stateNames = []
    for line in dataSet:
        stateNames.append(line[stateIndex])
    return  stateNames
def checkDataFormat(listLine,lineNum):
    '''Check if data on listLine is formatted correctly, print an error message if not; return a boolean value'''
    if(checkValidDate(splitDate(listLine[dateIndex])) == False):
        print("Date format incorrect at line " + str(lineNum))
        return False
    if(not checkNumberFormat(listLine[3])):
        print("Case format incorrect at line " + str(lineNum))
        return False
    if(not checkNumberFormat(listLine[4])):
        print("Case format incorrect at line " + str(lineNum))
        return False
    return True

def convertStringLinetoList(stringLine):
    '''Converts a line in the chart of type string to a list'''
    listLine = []
    for i in stringLine.split(","):
        listLine.append(i)
    return listLine

def checkNumberFormat(num):
    '''Check if a case number is formatted correctly, return a boolean value'''
    try:
        case = int(num)
    except:
        return False
    if(case < 0):
        return False
    return True
