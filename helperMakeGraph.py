import retrieveData as rD
from datetime import datetime

dataSetCountySate = []
global dates
global deaths
global confirmedCases

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
    return rD.retrieveData(path)

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

def getDates(list):
    '''return the column of dates from a list '''
    
    dates = [i[0] for i in list]
    return dates

def getConfirmedCases(list):
    '''return the column of death numbers from a list '''
    
    deaths = [int(i[3]) for i in list]
    return deaths

def getConfirmedDeaths(list):
    '''return the column of confirmed cases from a list '''
    deaths = [int(i[4]) for i in list]
    return deaths