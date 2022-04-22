import sys
import csv
from datetime import datetime
import os

#data path of the dataset .csv file relative to this folder
dataSet = [] 
#2-d array data set in the format [Date (as a list of form [Year, Month, Day]), County, State, Confirmed Cases, Confirmed Deaths]

def retrieveData(relativeDataPath):
    '''get data from a relative path to this file, return a dataSet[] variable that stores the data'''
    absoluteDataPath = convertRealtivePathToAbsolutePath(relativeDataPath)
    stringLines = getStringLinesFromFile(absoluteDataPath)
    storeData(stringLines)
    return dataSet

def convertRealtivePathToAbsolutePath(relativeDataPath):
    '''Calculate and return absolute path of the file'''
    currentPath = os.path.dirname(__file__)
    return os.path.join(currentPath, relativeDataPath)

def getStringLinesFromFile(filePath):
    '''Get lines as a list of strings from file'''
    with open(filePath) as file:
        stringLines  = file.readlines()[1:]
    file.close()
    return stringLines

def storeData(stringLines):
    '''Break each line into lists and store them in dataSet'''
    lineNum = 0
    for i in stringLines:
        lineNum+= 1 # keep track of line number for error message
        listLine = convertStringLinetoList(i)
        listLine.pop() # remove last column
        listLine[0] = splitDate(listLine[0]) #process date String and make it a list
        if(checkDataFormat(listLine, lineNum)):
            dataSet.append(listLine)   #skip the line if not formatted correctly
            
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

def getCountyStateData(county, state):
    '''returns a list of data that fits the county and state from dataSet'''
    path = "Data/sub-Data/" + county + "," + state + ".csv" 
    return retrieveData(path)

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
        
def toDateTime(date):
    '''convert date [Year, Month, Day] to a datetime object'''
    return datetime(int(date[0]),int(date[1]),int(date[2]))

def checkDataFormat(listLine,lineNum):
    '''Check if data on listLine is formatted correctly, print an error message if not; return a boolean value'''
    if(not checkDateFormat(listLine[0])):
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

def splitDate(dateString):
    '''Split date in to a list [Year, Month, Day]'''
    dates = dateString.split("-")
    return dates

def checkDateFormat(dates):
    '''Check if a dates string list is formatted correctly, returns a boolean value'''
    try:
        year = int(dates[0])
        month = int(dates[1])
        day = int(dates[2])
    except:
        return False
    if(year < 2018):
        return False
    if(year > 2022):
        return False
    if(month > 12):
        return False
    if(month < 1):
        return False
    if(day > 31):
        return False
    if(day < 1):
        return False
    return True
    
def checkNumberFormat(num):
    '''Check if a case number is formatted correctly, return a boolean value'''
    try:
        case = int(num)
    except:
        return False
    if(case < 0):
        return False
    return True