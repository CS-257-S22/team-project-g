# An integral function that checks different inputs 
from tabnanny import check
from conversionFunctions import *
from datetime import datetime

dataStartTime = datetime(2020, 1, 22)
dataEndTime = datetime(2022, 4, 9)

invalidDateErrorMsg = "Invalid dates! Use YYYY-MM-DD format and enter dates during COVID outbreaks!"
wrongOrderMsg = "Wrong order of dates!" 
dateOutofRangeErrorMsg = "Date range outside of data!"
InvalidCountyStateMsg = "This county-state pair does not exist! Check spelling."

def helperCheckInput(countyName, stateName, startDate, endDate):
    """
    checks if all the input is correct
    input:  countyName in String
            stateName in String
            startDate in String
            endDate in String
    return: True if all the input are correct
            Error message(s) if not
    """
    checkcountyStateResult = checkCountyState(countyName, stateName)
    checkDateResult = checkDates(startDate, endDate)
    checkInputResult = []
    if (checkcountyStateResult != True):
        checkInputResult.append(checkcountyStateResult)

    if (checkDateResult != True):
        checkInputResult.append(checkDateResult)
        
    if (checkInputResult == []):
        return True
    
    return checkInputResult


def checkCountyState(countyName,stateName):
    """
    Check if dates are within range and ordered correctly.
    Returns True if no error, or an error msg.
    """
    stateCountyData = open('Data/countyStateNameToLineNumber.txt','r')
    for line in stateCountyData:
        dataList = line.split(",")
        if (countyName == dataList[0] and stateName == dataList[1]):
            stateCountyData.close()
            return True
    stateCountyData.close()
    return InvalidCountyStateMsg

def checkValidDate(dateList):
    """
    input: date in List form [Year, Month, Date]
    output: True if the date is formatted correctly
            False if the date is formatted incorrectly
    """
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
    try:
        startDate = splitDate(startDate)
        endDate = splitDate(endDate)
    except:
        return invalidDateErrorMsg
    
    if (checkValidDate(startDate) == False or checkValidDate(endDate) == False):
        return invalidDateErrorMsg
    
    try:
        startDate = toDateTime(startDate)
        endDate = toDateTime(endDate)
    except:
        return invalidDateErrorMsg
    
    if (startDate > endDate):
        return wrongOrderMsg
    
    if (endDate < dataStartTime or startDate > dataEndTime):
        return(dateOutofRangeErrorMsg)
    
    return True
if __name__ == "__main__":
    print(checkCountyState("Rice", "Minnesota"))