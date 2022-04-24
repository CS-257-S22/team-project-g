from datetime import datetime

dataStartTime = datetime(2020, 1, 22)
dataEndTime = datetime(2022, 4, 9)

InvalidDateErrorMsg = "Invalid dates! Try the other order!"
DateOutofRangeErrorMsg = "Date range outside of data!"

def toDateTime(date):
    '''convert date [Year, Month, Day] to a datetime object'''
    return datetime(int(date[0]),int(date[1]),int(date[2]))

def checkValidDate(dateString):
    '''
    input: date in String form
    output: a list of 3 Strings, [Year, Month, Date] if the date is formatted correctly
            False if the date is formatted incorrectly
    '''
    try:
        dates = dateString.split("-")
    except: 
        return False
    
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
    return dates

def checkDate(startDate, endDate):
    
    if (checkValidDate(startDate) == False or checkValidDate(endDate) == False):
        print(InvalidDateErrorMsg)
        return InvalidDateErrorMsg
    
    try:
        startDate = toDateTime(startDate)
        endDate = toDateTime(endDate)
    except:
        print(InvalidDateErrorMsg)
        return InvalidDateErrorMsg
    
    if (startDate > endDate):
        print(InvalidDateErrorMsg)
        return InvalidDateErrorMsg
    
    if (endDate < dataStartTime or startDate > dataEndTime):
        print(DateOutofRangeErrorMsg)
        return(DateOutofRangeErrorMsg)
    
    return True