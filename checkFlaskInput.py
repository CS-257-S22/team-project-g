import helperCheckInput as hCI
import conversionFunctions as cF
InvalidCountyStateMsg = "This count-state pair does not exist! Check spelling."
InvalidDateMsg = "Invalid dates! Check the order."


def checkFlaskInput(countyName, stateName, startDate, endDate): # !!! need to know what type the inputs will be
    '''
    checks if all the input is correct
    input:  countyName in String
            stateName in String
            startDate in String
            endDate in String
    return: True if all the input are correct
            Error message(s) if not
    '''
    checkcountyStateResult = checkCountyState(countyName, stateName)
    checkDateResult = checkDate(startDate, endDate)
    checkInputResult = ""
    if (checkcountyStateResult != True):
        checkInputResult += checkcountyStateResult
        checkInputResult += "<br/>"
    if (checkDateResult != True):
        checkInputResult += checkDateResult
        checkInputResult += "<br/>"
    if (checkInputResult == ""):
        return True
    return checkInputResult

# Check if dates are within range and ordered correctly.
# Returns True if no error, or an error msg.
def checkCountyState(countyName,stateName):
    stateCountyData = open('Data/stateNameToLineNumber.txt','r')
    for line in stateCountyData:
        dataList = line.split(",")
        if (countyName == dataList[0] and stateName == dataList[1]):
            return True
    return InvalidCountyStateMsg

# Check if dates are within range and ordered correctly.
# Returns True if no error, or an error msg.
def checkDate(start, end):
    return hCI.checkDates(cF.splitDate(start), cF.splitDate(end)) # this may need to be updated depending on what type the input for checkFlaskInput are