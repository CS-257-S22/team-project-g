import helperCheckInput as hCI

InvalidCountyStateMsg = "This count-state pair does not exist! Check spelling."
InvalidDateMsg = "Invalid dates! Check the order."


def checkFlaskInput(countyName, stateName, startDate, endDate): # !!! need to know what type the inputs will be
    return checkCountyState(countyName, stateName) and checkDate(startDate, endDate)

# Check if dates are within range and ordered correctly.
# Returns True if no error, or an error msg.
def checkCountyState(countyName,stateName):
    stateCountyData = open('the-zen-of-python.txt','r')
    for line in stateCountyData:
        dataList = line.split(",")
        if (countyName == dataList[0] and stateName == dataList[1]):
            return True
    return InvalidCountyStateMsg

# Check if dates are within range and ordered correctly.
# Returns True if no error, or an error msg.
def checkDate(start, end):
    return hCI.checkDates(start, end) # this may need to be updated depending on what type the input for checkFlaskInput are

