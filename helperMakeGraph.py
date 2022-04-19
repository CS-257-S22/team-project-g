import retrieveData
from datetime import datetime

dataSet = retrieveData.retrieveData("Data\plot_test_data.csv")
global dates
global deaths
global confirmedCases

def getDataWithLocationAndDateRange(location, dateRange):
    county = location[0]
    state = location [1]
    list = getCountyStateData(county, state)
    list = getDateRangeData(list, dateRange)
    return list
    
def getCountyStateData(county, state):
    list = []
    for line in dataSet:
        if (not line[2] == state): continue
        if (not line[1] == county): continue
        list.append(line)
    return list

def getDateRangeData(list, dateRange):
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
    return datetime(int(date[0]),int(date[1]),int(date[2]))

def getDates(list):
    dates = [i[0] for i in list]
    return dates

def getConfirmedCases(list):
    deaths = [i[3] for i in list]
    return deaths

def getConfirmedDeaths(list):
    deaths = [i[4] for i in list]
    return deaths