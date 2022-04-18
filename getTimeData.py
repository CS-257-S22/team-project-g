import retrieveData

dataSet = retrieveData.retrieveData("Data/dummy_data.csv")
  
# crops dataSet to only consist of data within 2 dates.
def getTimeRange(date1, date2):
    startDate = dateToList(date1)
    endDate = dateToList(date2)
    startTrim = 0
    endTrim = 0
    for dateLine in range(len(dataSet[0])):
        currDate = dateToList(dataSet[0][date])

        if currDate[0] <= startDate[0]:
            startTrim = dateLine
        elif currDate[1] <= startDate[1]:
            startTrim = dateLine
        elif currDate[2] <= startDate[2]:
            startTrim = dateLine
        
        if currDate[0] > endDate[0]:
            endTrim = dateLine
            break
        elif currDate[1] > endDate[1]:
            endTrim = dateLine
            break
        elif currDate[2] > endDate[2]:
            endTrim = dateLine
            break 

    returnSet = createReturnSet()
    return trimSet(returnSet, startTrim, endTrim)

# trims a 2d array of data based on start end lines
def trimSet(returnList, start, end):
    for column in range(len(dataSet)):
        returnList[column] = dataSet[column][start:end + 1]
    return returnList

# creates set whose values will be replaced later
def createReturnSet():
    returnSet = []
    for c in range(len(dataSet)):
        returnSet.append(c)
    return returnSet  

# Converts a "YYYY-MM-DD" string to a list of [year, month, day]        
def dateToList (date):
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:])
    return [year, month, day]        

# maybe unecessary
# # returns true if dates are within in the original dataSet timeframe
# def rangeExists(startDate, endDate):
#     yearS = int(startDate[0])
#     monthS = int(startDate[1])
#     dayS = int(startDate[2])
#     yearE = int(endDate[0])
#     monthE = int(endDate[1])
#     dayE = int(endDate[2])

#     if(yearS < 2018 or yearE > 2022):
#         return False
#     if(monthS > 12 or monthE < 1):
#         return False
#     if(dayS > 31 or dayE < 1):
#         return False
#     return True 