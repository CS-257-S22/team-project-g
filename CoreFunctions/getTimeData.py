import retrieveDataFromLocal
from conversionFunctions import *

dataSet = []

def getTimeRange(date1, date2):

    """ Crop dataSet to only consist of data within 2 dates. 

    Both params are strings with the format 'YYYY-MM-DD, dashes included
    Both start and end dates are inclusive. 
    Assumes the dates inputed are within range of the data set.
    """

    dataSet = retrieveDataFromLocal.retrieveData("Data/dummy_data.csv")
    spliceStart = toDateTime(splitDate(date1))
    spliceEnd = toDateTime(splitDate(date2))
    returnList = []

    for dataPoint in dataSet: 
        currDate = toDateTime(splitDate(dataPoint[0]))
        if (currDate >= spliceStart and currDate <= spliceEnd):
            returnList.append(dataSet[dataPoint])                      
    return returnList  
