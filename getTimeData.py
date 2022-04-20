import retrieveData

dataSet = []
  
# crops dataSet to only consist of data within 2 dates.
def getTimeRange(date1, date2):
    dataSet = retrieveData.retrieveData("Data/dummy_data.csv")
    startDate = dateToList(date1)
    endDate = dateToList(date2)
    returnList = []
    for dataPoint in range(len(dataSet)): 
        currDate = strToIntList(dataSet[dataPoint][0])
        if (currDate[0] >= startDate[0] and currDate[0] < endDate[0]):
            if (currDate[1] >= startDate[1] and currDate[1] < endDate[1]):
                if currDate[2] >= startDate[2] and currDate[2] < endDate[2]:
                    print("hit")
                    returnList.append(dataSet[dataPoint])                      
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

def strToIntList (dateList):
    year = int(dateList[0])
    month = int(dateList[1])
    day = int(dateList[2])
    return [year, month, day]       
