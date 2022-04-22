import retrieveData as rD

def getDataForGraph(location, dateRange):
    '''
    takes a location and a dateRange and returns a combination of data, dataComb for graphing    
    locations is a list of 2 [county,state]
    dateRange is a list of 2 [[Year, Month, Day],[Year, Month, Day]] (startDate and endDate)
    
    dataComb[0] is a list of dates[]
    dataComb[1] is a list of confirmed cases[]
    dataComb[2] is a list of confirmed Deaths[]
    '''
    list = rD.getDataWithLocationAndDateRange(location, dateRange)
    dates = getDates(list)
    if(dates == []):
        return False
    confirmedCases = getConfirmedCases(list)
    confirmedDeaths = getConfirmedDeaths(list)
    dataComb = [dates, confirmedCases, confirmedDeaths]
    return dataComb

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