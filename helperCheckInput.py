from conversionFunctions import *
from datetime import datetime
dataStartTime = datetime(2020, 1, 22)
dataEndTime = datetime(2022, 4, 9)

InvalidDateErrorMsg = "Invalid dates! Try the other order!"
DateOutofRangeErrorMsg = "Date range outside of data!"

def checkValidDate(dateList):
    '''
    input: date in List form [Year, Month, Date]
    output: True if the date is formatted correctly
            False if the date is formatted incorrectly
    '''
    try:
        year = int(dateList[0])
        month = int(dateList[1])
        day = int(dateList[2])
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


def checkDates(startDate, endDate):
    """
    input: startDate and endDate in list form [Year, Month, Date]
    output: True if the dates are in range and valid
            An error message if not
    """
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